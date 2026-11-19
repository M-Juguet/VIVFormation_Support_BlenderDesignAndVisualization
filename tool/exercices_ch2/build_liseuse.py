# Construit le fichier 4 du chapitre 2 : _resources/exercices/PRC02_ch2_liseuse_depart.blend
# (défi ★★ « La liseuse de cabine », plan : _resources/plans/PRC02-plan-chap2.md, fichier 4).
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 `
#       -Script tool\exercices_ch2\build_liseuse.py
# Puis : finish_ui.py, verifier_blend.py, rendus_controle.py.
#
# Repère : la paroi de la cabine est le plan y = 0 ; la cabine est du côté des y négatifs ; z monte.
# Dimensions en mètres ; le fichier affiche des millimètres. Les outils viennent de build_lampe.py.

import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lampe as B  # noqa: E402

OUT = os.path.join(B.EX, "PRC02_ch2_liseuse_depart.blend")

LISEZ_MOI = """LISEZ-MOI · Défi ★★ · La liseuse de cabine
Une liseuse à col de cygne, fixée à la paroi au-dessus de l'accoudoir.
Même méthode que la lampe : chaque volume du gabarit devient une pièce propre.
Valeurs indicatives. N'appliquez aucun modificateur. Ctrl + Espace agrandit ce texte.
Corrigé : collection « Corrigé », masquée (œil fermé dans l'Outliner).
D'abord : File > Save As, sous liseuse_modele_v001.blend.

1. Platine : Bevel (Amount 2 mm, Segments 2), puis Shade Auto Smooth.
2. Vis : Add > Mesh > Cylinder (Vertices 16, Radius 2.5 mm, Depth 2 mm), R X 90.
   N > Item : Location 27, -9, 160 mm. Mirror : axe X seul, Mirror Object = Platine.
3. Bouton : 16 crans de 1 x 4 x 1 mm, à 5 mm de l'axe. Le bouton est couché :
   l'Empty tourne autour de Y. De combien ?
4. Col de cygne : Cursor to Selected sur Repere_col. Add > Curve > Bézier, Tab,
   supprimez un point, Selection to Cursor sur l'autre. Vue de droite (3), Curve Pen :
   3 points jusqu'au dos de la tête. Geometry > Bevel : Round, Depth 4 mm, Fill Caps.
5. Tête_liseuse : X > Faces sur la grande face, Solidify 1.5 mm, Shade Auto Smooth.
6. Diffuseur : sur Repere_diffuseur, comme l'ampoule, un demi-profil en vue de face :
   l'axe, le bord à 17.5 mm, un dôme de 4 mm. Screw : Axis Z, Merge coché à 0.1 mm.
   N > Item : Location 0, -276.1, 150.2 mm ; Rotation X -36.87°.
Contrôle : le col part de la platine et entre dans le dos de la tête ;
rien ne traverse la paroi ni l'accoudoir. Ctrl + S.
"""

T, RX, RY = B.T, B.RX, B.RY
COL_PTS = [(0, -0.004, 0.150), (0, -0.090, 0.215), (0, -0.180, 0.225), (0, -0.250, 0.185)]
COL_TYPES = ['ALIGNED', 'AUTO', 'AUTO', 'ALIGNED']
COL_HANDLES = {0: ((0, 0.010, 0.150), (0, -0.040, 0.150)), 3: ((0, -0.226, 0.217), (0, -0.262, 0.169))}
M_TETE = T((0, -0.2635, 0.167)) @ RX(-36.87)


def tete(name, col, closed=True):
    ob = B.cylinder(name, 0.020, 0.045, col, M_TETE, seg=32, r2=0.012)
    if not closed:
        B.open_shell(ob)
    return ob


def platine(name, col):
    return B.box(name, (0.070, 0.008, 0.040), (0, 0, 0), col, T((0, -0.004, 0.150)))


def bouton(name, col):
    return B.cylinder(name, 0.005, 0.004, col, T((0.020, -0.010, 0.140)) @ RX(90))


def col_de_cygne(name, col, depth):
    ob = B.bezier(name, COL_PTS, COL_TYPES, col, handles=COL_HANDLES)
    cu = ob.data
    cu.resolution_u = 24
    if depth:
        cu.bevel_mode = 'ROUND'
        cu.bevel_depth = depth
        cu.bevel_resolution = 4
        cu.use_fill_caps = True
    return ob


def build():
    sc = B.reset_scene()
    root = sc.collection
    c_ctx = B.new_collection("Contexte", root)
    c_gab = B.new_collection("Gabarit_liseuse", root)
    c_lis = B.new_collection("Liseuse", root)
    c_cor = B.new_collection("Corrigé", root)

    # Contexte : la paroi et l'accoudoir
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.5)
    bmesh.ops.scale(bm, vec=(0.5, 0.4, 1), verts=bm.verts)
    paroi = B.mesh_from_bm("Paroi", bm, c_ctx, T((0, 0, 0.20)) @ RX(90))
    acc = B.box("Accoudoir", (0.50, 0.15, 0.05), (0, 0, 0), c_ctx, T((0, -0.075, 0.025)))
    for o in (paroi, acc):
        o.hide_select = True
    paroi.color = (0.62, 0.66, 0.74, 1)
    acc.color = (0.45, 0.45, 0.50, 1)

    # Gabarit : fil de fer, non sélectionnable
    gab = [platine("Platine_G", c_gab), bouton("Bouton_G", c_gab), tete("Tête_G", c_gab),
           col_de_cygne("Col_G", c_gab, 0.0)]
    for o in gab:
        o.display_type = 'WIRE'
        o.hide_select = True

    # Copies de travail, sans modificateur, et les deux repères
    work_platine = platine("Platine", c_lis)
    bouton("Bouton", c_lis)
    tete("Tête_liseuse", c_lis)
    B.empty("Repere_col", 0.005, c_lis, T((0, -0.004, 0.150)))
    B.empty("Repere_diffuseur", 0.005, c_lis, T((0.150, -0.200, 0.300)))

    # Corrigé
    pl = platine("Platine_corrige", c_cor)
    B.bevel(pl, 0.002, 2)
    B.auto_smooth(pl)
    vis = B.cylinder("Vis_corrige", 0.0025, 0.002, c_cor, T((0.027, -0.009, 0.160)) @ RX(90), seg=16)
    m = vis.modifiers.new("Mirror", 'MIRROR')
    m.use_axis = (True, False, False)
    m.mirror_object = pl
    B.auto_smooth(vis)
    bt = bouton("Bouton_corrige", c_cor)
    B.bevel(bt, 0.0003, 2)
    B.auto_smooth(bt)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=(0.001, 0.004, 0.001), verts=bm.verts)
    bmesh.ops.translate(bm, vec=(0.005, 0, 0), verts=bm.verts)
    cr = B.mesh_from_bm("Bouton_crans_corrige", bm, c_cor, T((0.020, -0.010, 0.140)))
    pv = B.empty("Bouton_pivot_corrige", 0.004, c_cor, T((0.020, -0.010, 0.140)) @ RY(22.5))
    B.parent_keep(pv, cr)
    B.array_ring(cr, pv, 16)
    col_de_cygne("Col_de_cygne_corrige", c_cor, 0.004)
    th = tete("Tête_liseuse_corrige", c_cor, closed=False)
    B.solidify(th)
    B.auto_smooth(th)
    df = B.bezier("Diffuseur_corrige", [(0, 0, 0), (0.0175, 0, 0), (0, 0, -0.004)], ['VECTOR', 'VECTOR', 'ALIGNED'], c_cor,
                  T((0, -0.2761, 0.1502)) @ RX(-36.87), handles={2: ((0.010, 0, -0.004), (-0.010, 0, -0.004))})
    B.screw(df)

    B.controls(list(c_cor.objects) + [paroi, acc], "liseuse")
    bpy.context.view_layer.layer_collection.children["Corrigé"].hide_viewport = True

    # Vue d'ouverture : œil (0.30, -0.55, 0.32), cible (0, -0.13, 0.17)
    B.setup_ui(LISEZ_MOI, work_platine, 'RANDOM')
    eye, target = Vector((0.30, -0.55, 0.32)), Vector((0, -0.13, 0.17))
    for area in bpy.data.screens["Layout"].areas:
        if area.type == 'VIEW_3D':
            r3d = area.spaces.active.region_3d
            r3d.view_location = target
            r3d.view_rotation = (target - eye).to_track_quat('-Z', 'Y')
            r3d.view_distance = (target - eye).length
    B.finalize(OUT)


if __name__ == "__main__":
    build()
