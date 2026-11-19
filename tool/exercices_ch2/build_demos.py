# Construit le fichier 5 du chapitre 2 : _resources/exercices/PRC02_ch2_demos_secteurs.blend
# (les moments « Ailleurs » des démos ; plan : _resources/plans/PRC02-plan-chap2.md, fichier 5).
# Fichier léger, poste du formateur : des formes simples, sans détail ni matière, déjà terminées.
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 `
#       -Script tool\exercices_ch2\build_demos.py
#
# Quatre collections alignées sur X, espacées de 2 m. Dimensions en mètres ; affichage en millimètres.

import math
import os
import sys

import bmesh
import bpy
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lampe as B  # noqa: E402

OUT = os.path.join(B.EX, "PRC02_ch2_demos_secteurs.blend")
T, RX, RY, RZ = B.T, B.RX, B.RY, B.RZ

LISEZ_MOI = """LISEZ-MOI · Chapitre 2 · Démos « Ailleurs » (poste du formateur)
Ctrl + Espace agrandit ce texte. Quatre exemples déjà terminés, un par collection, espacés de 2 m sur X.
Pour cadrer un exemple : sélectionnez une pièce, puis . du pavé numérique.

Auto_capot · Symétrie : une moitié de capot, Mirror X avec Clipping et Bisect.
  Montrez : Tab, déplacez un sommet du bord central, il reste sur l'axe (Clipping).
Aero_soufflante · Répétition : un moyeu, une aube et un Empty ; Array (Legacy) en couronne de 18 aubes.
  Montrez : Count 18, puis 24 ; tournez l'Empty de 360° / Count.
Ferro_main_courante · Câble : deux poteaux et une main courante de tram en courbe de Bézier, Depth 16 mm.
  Montrez : Tab, déplacez un point ; Object Data > Geometry > Bevel > Depth.
Ferro_roue · Révolution : le demi-profil d'une roue ferroviaire (bandage, boudin, toile) et Screw.
  Montrez : Tab, retouchez le boudin ; toute la roue suit.
"""


def capot(col, x):
    """Moitié droite d'un capot galbé (x >= 0 en local), Mirror X avec Clipping et Bisect."""
    nu, nv = 6, 9
    bm = bmesh.new()
    vs = []
    for i in range(nu + 1):
        row = []
        for j in range(nv + 1):
            u, v = i / nu, j / nv
            px, py = 0.6 * u, -0.45 + 0.9 * v
            z = 0.10 * (1 - u ** 2) * (1 - 0.6 * (2 * v - 1) ** 2) - 0.04 * v
            if i == 2:
                z += 0.012                      # une ligne de caractère, à 20 cm de l'axe
            row.append(bm.verts.new((px, py, z)))
        vs.append(row)
    for i in range(nu):
        for j in range(nv):
            bm.faces.new((vs[i][j], vs[i + 1][j], vs[i + 1][j + 1], vs[i][j + 1]))
    ob = B.mesh_from_bm("Capot_moitie", bm, col, T((x, 0, 0.4)))
    m = ob.modifiers.new("Mirror", 'MIRROR')
    m.use_axis = (True, False, False)
    m.use_bisect_axis = (True, False, False)
    m.use_clip = True
    s = ob.modifiers.new("Subdivision", 'SUBSURF')
    s.levels = s.render_levels = 2
    so = ob.modifiers.new("Solidify", 'SOLIDIFY')
    so.thickness = 0.004
    so.offset = -1
    for p in ob.data.polygons:
        p.use_smooth = True
    return ob


def soufflante(col, x):
    c = Vector((x, 0, 0.7))
    moyeu = B.cylinder("Soufflante_moyeu", 0.15, 0.20, col, T(c) @ RX(90), seg=48, r2=0.06)
    B.auto_smooth(moyeu)
    # une aube : un pavé mince, vrillé de 10° à 45° du pied à la tête
    bm = bmesh.new()
    nseg = 6
    prev = None
    for k in range(nseg + 1):
        t = k / nseg
        r = 0.14 + (0.60 - 0.14) * t
        ang = math.radians(45 - 35 * t)
        cord, ep = 0.16 - 0.05 * t, 0.012
        pts = []
        for (a, b) in ((-cord / 2, -ep / 2), (cord / 2, -ep / 2), (cord / 2, ep / 2), (-cord / 2, ep / 2)):
            # (a, b) dans le plan perpendiculaire au rayon (Z), tourné de ang autour du rayon
            px = a * math.cos(ang) - b * math.sin(ang)
            py = a * math.sin(ang) + b * math.cos(ang)
            pts.append(bm.verts.new((px, py, r)))
        if prev:
            for i in range(4):
                bm.faces.new((prev[i], prev[(i + 1) % 4], pts[(i + 1) % 4], pts[i]))
        else:
            bm.faces.new(pts[::-1])
        prev = pts
    bm.faces.new(prev)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    # l'axe de la soufflante est Y : l'aube monte selon Z local, l'objet tourne autour de Y
    aube = B.mesh_from_bm("Soufflante_aube", bm, col, T(c) @ RX(90) @ RX(-90))
    piv = B.empty("Soufflante_pivot", 0.08, col, T(c) @ RY(20))
    B.parent_keep(piv, aube)
    a = B.array_ring(aube, piv, 18)
    return moyeu, aube


def main_courante(col, x):
    h = 0.75
    for k, px in enumerate((x, x + 1.5)):
        B.cylinder("Poteau_%d" % (k + 1), 0.016, h, col, T((px, 0, h / 2)), seg=24)
    pts = [(x, 0, h - 0.01), (x + 0.15, 0, h + 0.20), (x + 1.35, 0, h + 0.20), (x + 1.5, 0, h - 0.01)]
    handles = {0: ((x, 0, h - 0.08), (x, 0, h + 0.09)),
               1: ((x + 0.06, 0, h + 0.20), (x + 0.30, 0, h + 0.20)),
               2: ((x + 1.20, 0, h + 0.20), (x + 1.44, 0, h + 0.20)),
               3: ((x + 1.5, 0, h + 0.09), (x + 1.5, 0, h - 0.08))}
    ob = B.bezier("Main_courante", pts, ['ALIGNED'] * 4, col, handles=handles)
    cu = ob.data
    cu.bevel_mode = 'ROUND'
    cu.bevel_depth = 0.016
    cu.bevel_resolution = 4
    cu.use_fill_caps = True
    cu.resolution_u = 24
    return ob


def roue(col, x):
    """Demi-profil fermé (rayon, position sur l'essieu) d'une roue de Ø 0,84 m au roulement."""
    P = [((0.080, -0.090), 'VECTOR'), ((0.120, -0.090), 'VECTOR'), ((0.128, -0.022), 'AUTO'),
         ((0.350, -0.016), 'AUTO'), ((0.360, -0.0675), 'VECTOR'), ((0.432, -0.0675), 'VECTOR'),
         ((0.450, -0.052), 'AUTO'), ((0.425, -0.036), 'VECTOR'), ((0.420, 0.0675), 'VECTOR'),
         ((0.360, 0.0675), 'VECTOR'), ((0.350, 0.016), 'AUTO'), ((0.128, 0.022), 'AUTO'),
         ((0.120, 0.090), 'VECTOR'), ((0.080, 0.090), 'VECTOR')]
    P = P[::-1]          # sens de parcours : normales du Screw vers l'extérieur
    pts = [(r, 0, z) for (r, z), _t in P]
    ob = B.bezier("Roue_profil", pts, [t for _p, t in P], col, T((x, 0, 0.45)) @ RX(90), cyclic=True)
    s = B.screw(ob, steps=64)
    return ob


def build():
    sc = B.reset_scene()
    root = sc.collection
    cols = {}
    for k, name in enumerate(("Auto_capot", "Aero_soufflante", "Ferro_main_courante", "Ferro_roue")):
        cols[name] = (B.new_collection(name, root), 2.0 * k)
    cap = capot(*cols["Auto_capot"])
    soufflante(*cols["Aero_soufflante"])
    main_courante(*cols["Ferro_main_courante"])
    roue(*cols["Ferro_roue"])
    for o in bpy.data.objects:
        if o.type != 'EMPTY':
            o.color = B.GRIS
    B.controls([o for o in bpy.data.objects if o.type in ('MESH', 'CURVE')], "démos")
    B.setup_ui(LISEZ_MOI, cap, 'OBJECT')
    eye, target = Vector((0.9, -1.6, 1.3)), Vector((0.0, 0, 0.35))
    for area in bpy.data.screens["Layout"].areas:
        if area.type == 'VIEW_3D':
            sp = area.spaces.active
            sp.clip_start = 0.01
            sp.clip_end = 200
            r3d = sp.region_3d
            r3d.view_location = target
            r3d.view_rotation = (target - eye).to_track_quat('-Z', 'Y')
            r3d.view_distance = (target - eye).length
    B.finalize(OUT)


if __name__ == "__main__":
    build()
