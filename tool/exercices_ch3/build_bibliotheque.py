# Construit la fiche B du chapitre 3 : la bibliothèque CMF de la classe.
#   tool/exercices_ch3/_construction/PRC02_bibliotheque_CMF/PRC02_ch3_nuancier_cmf.blend
#   tool/exercices_ch3/_construction/PRC02_bibliotheque_CMF/blender_assets.cats.txt
# Puis finish_ui.py (vignettes des actifs, hauteur du LISEZ-MOI) et livrer.py (le zip).
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 -Script tool\exercices_ch3\build_bibliotheque.py
# Toutes les dimensions sont en mètres ; le fichier affiche des millimètres.

import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commun as C   # noqa: E402
import matieres as M   # noqa: E402

LISEZ_MOI = """PRC02 · Bibliothèque CMF
Pour récupérer une matière dans votre fichier : File > Append > PRC02_ch3_nuancier_cmf.blend > Material.
La matière arrive modifiable, avec ses images.
Option, pour parcourir cette gamme dans l'Asset Browser de tous vos fichiers :
Edit > Preferences > Asset Libraries > + > choisissez le dossier PRC02_bibliotheque_CMF.
Toutes les valeurs sont indicatives. Les images sont créées par VIV Formation et libres de droits (CC0).
"""

ORDER = ["Métaux", "Plastiques", "Peintures", "Verres", "Finitions texturées"]
STEP_X, STEP_Y = 0.085, 0.135
X0, Y0 = -0.32, -0.33


def pastille_mesh():
    """Une plaquette CMF de 50 x 4 x 80 mm, debout (face vers -Y), origine au milieu du bord bas."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=(0.050, 0.004, 0.080), verts=bm.verts)
    bmesh.ops.translate(bm, vec=(0, 0, 0.040), verts=bm.verts)
    me = bpy.data.meshes.new("Pastille")
    bm.to_mesh(me)
    bm.free()
    return me


def sphere_mesh(name, r, seg=48, rings=24):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=rings, radius=r)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    return me


def smooth_auto(ob):
    C.select_only(ob)
    bpy.ops.object.shade_auto_smooth()
    ob.select_set(False)


def build():
    sc = C.reset_scene(raytracing=True)
    root = sc.collection
    c_sup = C.new_collection("Support", root)
    c_gri = C.new_collection("Grille_Metallic_Roughness", root)
    c_nua = C.new_collection("Nuancier", root)

    etq = M.principled("Etiquette", "111111", 0, 0.9, {})
    sup_mat = M.principled("Support_Gris", "8A8A8A", 0, 0.8, {})

    # le support : un plan de 1,05 x 0,90 m
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.5)
    bmesh.ops.scale(bm, vec=(1.05, 0.95, 1), verts=bm.verts)
    me = bpy.data.meshes.new("Support")
    bm.to_mesh(me)
    bm.free()
    sup = bpy.data.objects.new("Support", me)
    c_sup.objects.link(sup)
    sup.location = (-0.08, 0.06, 0)
    C.assign(sup, sup_mat)
    sup.hide_select = True

    # la grille Metallic / Roughness : rangée avant Metallic 0, rangée arrière Metallic 1
    roughs = [0, 0.1, 0.2, 0.4, 0.6, 1.0]
    for row, (metal, y, hexa) in enumerate(((0, 0.36, "808080"), (1, 0.45, "D0D0D0"))):
        for k, r in enumerate(roughs):
            name = "Grille_M%d_R%02d" % (metal, round(r * 10))
            mat = M.principled(name, hexa, metal, r, {})
            ob = bpy.data.objects.new(name, sphere_mesh(name, 0.022))
            c_gri.objects.link(ob)
            ob.location = (-0.20 + k * 0.08, y, 0.022)
            C.assign(ob, mat)
        C.label("Metallic %d" % metal, 0.013, (-0.36, y, 0.0005), (0, 0, 0), c_gri, etq, align='LEFT')
    for k, r in enumerate(roughs):
        txt = ("%g" % r).replace(".", ",")
        C.label(txt, 0.013, (-0.20 + k * 0.08, 0.315, 0.0005), (0, 0, 0), c_gri, etq)
    C.label("Roughness", 0.013, (-0.36, 0.315, 0.0005), (0, 0, 0), c_gri, etq, align='LEFT')

    # le nuancier : une rangée par catalogue
    plate = pastille_mesh()
    bille = sphere_mesh("Bille", 0.015)
    by_cat = {c: [n for n, v in M.BIBLIO.items() if v[0] == c] for c in ORDER}
    first = None
    for r, cat in enumerate(ORDER):
        y = Y0 + r * STEP_Y
        C.label(cat, 0.016, (-0.54, y + 0.01, 0.0005), (0, 0, 0), c_nua, etq, align='LEFT')
        for k, name in enumerate(by_cat[cat]):
            x = X0 + k * STEP_X
            mat = M.biblio(name)
            _cat, _col, _m, _r, _o, tags, desc = M.BIBLIO[name]
            M.mark(mat, M.CATS_BIBLIO, cat, desc, tags)
            me = plate.copy()
            me.name = "Pastille_" + name
            ob = bpy.data.objects.new("Pastille_" + name, me)
            c_nua.objects.link(ob)
            ob.matrix_world = Matrix.Translation((x, y, 0)) @ Matrix.Rotation(math.radians(-65), 4, 'X')
            bv = ob.modifiers.new("Bevel", 'BEVEL')
            bv.width = 0.0015
            bv.segments = 3
            bv.limit_method = 'ANGLE'
            C.assign(ob, mat)
            smooth_auto(ob)
            if first is None:
                first = ob
            if cat == "Verres":
                b = bpy.data.objects.new("Bille_" + name, bille.copy())
                c_nua.objects.link(b)
                b.location = (x, y - 0.05, 0.015)
                C.assign(b, mat)
            C.label(name, 0.0062, (x, y - 0.022, 0.0005), (0, 0, 0), c_nua, etq)
    bpy.data.meshes.remove(plate)
    bpy.data.meshes.remove(bille)

    txt = C.text_block(LISEZ_MOI)
    C.setup_layout(txt, 'MATERIAL', eye=(0.30, -0.95, 0.80), target=(-0.06, 0.02, 0.0), distance_k=0.9)
    C.select_only(first)
    os.makedirs(C.BIBLIO_DIR, exist_ok=True)
    M.write_catalogs(C.BIBLIO_DIR, M.CATS_BIBLIO)
    C.finalize(C.NUANCIER, groups_expected=["Smooth by Angle"])
    n_assets = sum(1 for m in bpy.data.materials if m.asset_data)
    print("ACTIFS", n_assets, "| IMAGES", [(i.name, i.colorspace_settings.name) for i in bpy.data.images if i.packed_file])


build()
