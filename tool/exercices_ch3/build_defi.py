# Construit le fichier du défi facultatif « matières procédurales » du chapitre 3 (fiche F du plan
# _resources/plans/PRC02-plan-chap3-complement-procedural.md) :
#   _resources/exercices/PRC02_ch3_defi_procedural.blend
# Une rangée de pièces par étape (exemple terminé, pièces à compléter), la copie Lampe_defi de la lampe
# habillée (coloris A, d'après les scripts de la fiche A2) et la collection masquée « Corrigé défi
# procédural », une sous-collection par étape, objets et matières suffixés _corrige.
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 -Script tool\exercices_ch3\build_defi.py
# Puis finish_ui.py (espace Shading, LISEZ-MOI) et verifier_blend.py.
# La lampe est lue dans _resources/exercices/PRC02_ch2_lampe_modele.blend, sans modifier ce fichier.

import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_lampe as BL   # noqa: E402
import commun as C   # noqa: E402
import defi_recettes as R   # noqa: E402
import matieres as M   # noqa: E402

OUT = os.path.join(C.EX, "PRC02_ch3_defi_procedural.blend")
ROW = 0.32           # écart entre deux rangées (Y)
CORR_DX = 2.4        # décalage du corrigé (X)

LISEZ_MOI = """PRC02 · Chapitre 3 · Défi facultatif, hors programme : matières procédurales
Enregistrez ce fichier sous defi_procedural_v001.blend. Suivez la section 4 du chapitre 3 dans l'application.
Corrigés : collection « Corrigé défi procédural » (œil fermé), une sous-collection par étape, suffixe _corrige.
Affichez seulement la collection de l'étape en cours : l'affichage reste fluide.
Aperçu d'un nœud : Ctrl + Maj + clic sur le nœud. Retour : Ctrl + Maj + clic sur le Principled BSDF.
Valeurs indicatives, vérifiées sous EEVEE : retouchez-les à l'œil. Le relief se règle avec Strength du Bump.

PALIER 1
1 · Bruits : Noise (Scale 100), Voronoi (Distance to Edge), Wave (Rings, Z), Gabor (Frequency 6).
2 · Remapper : Color Ramp (Constant, curseur à 0,74), Map Range (To 0,08 à 0,35 vers Roughness),
    Math (Greater Than 0,74).
3 · Masques : un masque, trois Mix (Base Color, Metallic, Roughness).
    Patine aux extrémités : Separate XYZ (Z) > Absolute > Map Range > Multiply.
4 · Relief : Bump A > Normal du Bump B > Principled. Peau d'orange : Bump (Strength 0,15) > Coat Normal.

PALIER 2
5 · Usure : Texture Coordinate > Normal > Separate XYZ (Z) > Absolute > Color Ramp (0,10 / 0,50 / 0,90).
    Saleté : Ambient Occlusion (Distance 20mm) > Color Ramp (0,85 / 0,99).
    Rayures : Mapping (Z 0,02) > Noise (2000) > Color Ramp (0,68 / 0,70) > Roughness.
    Traces : Noise (25) > Map Range > Coat Roughness.
6 · Motifs : tôle perforée = Voronoi 2D (Scale 250, Randomness 0) > Greater Than 0,3 > Alpha.
    Cuir, tissu, et en défi moletage et carbone : recettes dans l'application.
7 · Groupes : remplacez le Color Ramp par Math et Map Range, puis Ctrl + G, Tab, barre latérale N > Group.
    Défi final : la collection Lampe_defi (rendez-la visible).
Les groupes « _corrige » de Maj + A > Group sont ceux du corrigé.
La case Raytracing est décochée : l'ampoule ne montre que l'environnement, c'est normal.
"""

TITRES = {
    1: "Étape 1 · Bruits", 2: "Étape 2 · Remapper", 3: "Étape 3 · Masques", 4: "Étape 4 · Relief",
    5: "Étape 5 · Usure", 6: "Étape 6 · Motifs", 7: "Étape 7 · Groupes",
}
COLLECTIONS = {
    1: "Etape_1_Bruits", 2: "Etape_2_Remapper", 3: "Etape_3_Masques", 4: "Etape_4_Relief",
    5: "Etape_5_Usure", 6: "Etape_6_Motifs", 7: "Etape_7_Groupes",
}


# ---------------------------------------------------------------------------- formes
def _obj(name, me, col, loc, rot=(0, 0, 0)):
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = rot
    return ob


def _bevel(ob, width, seg):
    b = ob.modifiers.new("Bevel", 'BEVEL')
    b.width = width
    b.segments = seg
    b.limit_method = 'ANGLE'
    return b


def smooth(ob):
    C.select_only(ob)
    bpy.ops.object.shade_auto_smooth()
    ob.select_set(False)


def box(name, size, col, loc, bevel=None, seg=3, rot=(0, 0, 0)):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=size, verts=bm.verts)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = _obj(name, me, col, loc, rot)
    if bevel:
        _bevel(ob, bevel, seg)
    smooth(ob)
    return ob


def cylinder(name, radius, depth, col, loc, verts=64, bevel=None, seg=3, rot=(0, 0, 0)):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=verts, radius1=radius, radius2=radius,
                          depth=depth)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = _obj(name, me, col, loc, rot)
    if bevel:
        _bevel(ob, bevel, seg)
    smooth(ob)
    return ob


def tile(name, col, loc):
    """Une plaquette de 80 x 80 x 4 mm, posée à plat."""
    return box(name, (0.080, 0.080, 0.004), col, (loc[0], loc[1], 0.002), bevel=0.0015, seg=3)


def handrail(name, col, loc):
    """Un tube de Ø 32 x 300 mm couché sur X : rotation non appliquée, son axe local Z suit le tube."""
    return cylinder(name, 0.016, 0.300, col, (loc[0], loc[1], 0.016), verts=64, bevel=0.002, seg=3,
                    rot=(0, math.radians(90), 0))


def shell(name, col, loc):
    """Une coque de rétroviseur : demi-ellipsoïde de 220 x 140 x 120 mm, ouverte vers l'arrière (+Y)."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=96, v_segments=48, radius=1.0)
    back = [v for v in bm.verts if v.co.y > 1e-6]
    bmesh.ops.delete(bm, geom=back, context='VERTS')
    bmesh.ops.scale(bm, vec=(0.110, 0.140, 0.060), verts=bm.verts)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = _obj(name, me, col, (loc[0], loc[1], 0.060))
    s = ob.modifiers.new("Solidify", 'SOLIDIFY')
    s.thickness = 0.0025
    s.offset = -1
    s.use_even_offset = True
    return ob


def bent_panel(name, col, loc, size=(0.300, 0.200), angle=25, thick=0.002):
    """Un panneau cintré, construit debout puis couché par sa rotation (le Bend sur Y ne courbe pas un
    plan couché en XY : décision 8 de la production du chapitre 3)."""
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=40, y_segments=28, size=0.5)
    bmesh.ops.scale(bm, vec=(size[0], size[1], 1), verts=bm.verts)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(90), 3, 'Y'))
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = _obj(name, me, col, (loc[0], loc[1], 0.03), (0, math.radians(-90), 0))
    d = ob.modifiers.new("SimpleDeform", 'SIMPLE_DEFORM')
    d.deform_method = 'BEND'
    d.deform_axis = 'Y'
    d.angle = math.radians(angle)
    s = ob.modifiers.new("Solidify", 'SOLIDIFY')
    s.thickness = thick
    s.offset = -1
    s.use_even_offset = True
    return ob


def curved_panel(name, col, loc, size=(0.300, 0.200), radius=0.6, thick=0.002):
    """Un panneau galbé dans le maillage lui-même : à plat dans le plan XY local, la recette du carbone
    lit X et Y (un panneau construit debout puis couché aurait X le long de sa normale)."""
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=60, y_segments=40, size=0.5)
    bmesh.ops.scale(bm, vec=(size[0], size[1], 1), verts=bm.verts)
    for v in bm.verts:
        v.co.z = v.co.x * v.co.x / (2 * radius)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = _obj(name, me, col, (loc[0], loc[1], 0.004))
    s = ob.modifiers.new("Solidify", 'SOLIDIFY')
    s.thickness = thick
    s.offset = -1
    s.use_even_offset = True
    return ob


def label(text, col, y, mat):
    return C.label(text, 0.014, (-0.08, y, 0.0005), (0, 0, 0), col, mat, align='RIGHT')


# ---------------------------------------------------------------------------- les rangées
def rangees(root, et):
    """Les pièces de travail : {étape: [(objet, matière de départ, recette du corrigé)]}."""
    P = {}
    cols = {k: C.new_collection(v, root) for k, v in COLLECTIONS.items()}

    def y(n):
        return -(n - 1) * ROW

    for n, c in cols.items():
        label(TITRES[n], c, y(n), et)

    # Étape 1 : quatre plaquettes d'exemple, la pratique, trois défis
    c, yy = cols[1], y(1)
    r = []
    for i, key in enumerate(("Noise", "Voronoi", "Wave", "Gabor")):
        ob = tile("E1_Exemple_" + key, c, (0.06 + 0.12 * i, yy))
        r.append((ob, R.e1("E1_Exemple_" + key, key), None))
    r.append((tile("E1_Pratique", c, (0.62, yy)), R.depart("E1_Pratique"), lambda nm: R.e1(nm, "Gabor_axe_x")))
    for i, key in enumerate(("Voronoi_bords", "Wave_anneaux", "Gabor_axe_x")):
        name = "E1_Defi_" + "ABC"[i]
        r.append((tile(name, c, (0.82 + 0.12 * i, yy)), R.depart(name), (lambda k: (lambda nm: R.e1(nm, k)))(key)))
    P[1] = r

    # Étape 2 : la coque de siège mouchetée, deux plaquettes, un défi
    c, yy = cols[2], y(2)
    coque = bent_panel("E2_Exemple_Coque", c, (0.12, yy), size=(0.200, 0.240), angle=30, thick=0.004)
    P[2] = [
        (coque, R.mouchete("E2_Exemple_Coque"), None),
        (tile("E2_Pratique_Mouchete", c, (0.42, yy)), R.depart("E2_Pratique_Mouchete", "2B2D2F", 0, 0.5),
         lambda nm: R.mouchete(nm, avec_math=True)),
        (tile("E2_Pratique_Planche", c, (0.56, yy)), R.depart("E2_Pratique_Planche", "151515", 0, 0.2), R.planche),
        (tile("E2_Defi", c, (0.76, yy)), R.depart("E2_Defi", "2B2D2F", 0, 0.5),
         lambda nm: R.mouchete(nm, deux_couleurs=True)),
    ]

    # Étape 3 : trois mains courantes
    c, yy = cols[3], y(3)
    P[3] = [
        (handrail("E3_Exemple_Main_courante", c, (0.15, yy)), R.patine("E3_Exemple_Main_courante"), None),
        (handrail("E3_Pratique_Main_courante", c, (0.55, yy)), R.depart("E3_Pratique_Main_courante", "E0C27A", 1, 0.25),
         R.patine),
        (handrail("E3_Defi_Main_courante", c, (0.95, yy)), R.depart("E3_Defi_Main_courante", "C8C8C6", 1, 0.15),
         lambda nm: R.patine(nm, metal="C8C8C6", depot="D9D4C7", r_metal=0.15, r_depot=0.8)),
    ]

    # Étape 4 : coques et boîtier
    c, yy = cols[4], y(4)
    P[4] = [
        (shell("E4_Exemple_Coque", c, (0.10, yy)), R.laque_orange("E4_Exemple_Coque"), None),
        (box("E4_Pratique_Boitier", (0.120, 0.080, 0.030), c, (0.38, yy, 0.015), bevel=0.003, seg=4),
         R.depart("E4_Pratique_Boitier", "D9DADB", 1, 0.45), R.boitier),
        (shell("E4_Pratique_Coque", c, (0.66, yy)), R.depart("E4_Pratique_Coque", "A3161A", 0, 0.4, (1, 0.03)),
         R.laque_orange),
        (shell("E4_Defi_Coque", c, (0.94, yy)), R.depart("E4_Defi_Coque", "1C3F7A", 1, 0.35, (1, 0.02)),
         R.metallisee),
    ]

    # Étape 5 : coffret, socle, marchepied, main courante, console, défi
    c, yy = cols[5], y(5)
    cof = box("E5_Exemple_Coffret", (0.200, 0.120, 0.080), c, (0.12, yy, 0.060), bevel=0.004, seg=4)
    pli = box("E5_Exemple_Plinthe", (0.240, 0.160, 0.020), c, (0.12, yy, 0.010), bevel=0.002, seg=2)
    base = box("E5_Pratique_Marchepied", (0.200, 0.200, 0.010), c, (0.74, yy, 0.005), bevel=0.001, seg=2)
    ribs = [box("E5_Pratique_Marchepied_nervure_%d" % (i + 1), (0.012, 0.180, 0.012), c,
                (0.74 + dx, yy, 0.016), bevel=0.002, seg=3) for i, dx in enumerate((-0.06, 0.0, 0.06))]
    dcof = box("E5_Defi_Coffret", (0.200, 0.120, 0.080), c, (1.86, yy, 0.060), bevel=0.004, seg=4)
    dpli = box("E5_Defi_Plinthe", (0.240, 0.160, 0.020), c, (1.86, yy, 0.010), bevel=0.002, seg=2)
    mp = R.depart("E5_Pratique_Marchepied", "9A9C9E", 1, 0.35)
    P[5] = [
        (cof, R.coffret("E5_Exemple_Coffret"), None),
        (pli, R.salete("E5_Exemple_Plinthe", base="4A4D50", metallic=0.0, rough=0.6), None),
        (cylinder("E5_Pratique_Socle", 0.090, 0.025, c, (0.42, yy, 0.0125), verts=64, bevel=0.003, seg=4),
         R.depart("E5_Pratique_Socle", "2F5D3A", 0, 0.45), R.peinture_usee),
        (base, mp, R.salete),
    ] + [(rb, mp, "meme") for rb in ribs] + [
        (handrail("E5_Pratique_Main_courante", c, (1.06, yy)), R.depart("E5_Pratique_Main_courante", "C8C8C6", 1, 0.08),
         R.rayures),
        (box("E5_Pratique_Console", (0.200, 0.120, 0.010), c, (1.46, yy, 0.005), bevel=0.002, seg=3),
         R.depart("E5_Pratique_Console", "0A0A0A", 0, 0.3, (1, 0.02)), R.traces),
        (dcof, R.depart("E5_Defi_Coffret", "2F5D3A", 0, 0.45), R.coffret),
        (dpli, R.depart("E5_Defi_Plinthe", "4A4D50", 0, 0.6),
         lambda nm: R.salete(nm, base="4A4D50", metallic=0.0, rough=0.6)),
    ]

    # Étape 6 : dalle, grille et son fond, accoudoir, assise, molette, panneau
    c, yy = cols[6], y(6)
    grille = box("E6_Pratique_Grille", (0.120, 0.080, 0.0015), c, (0.27, yy, 0.031), bevel=None)
    fond = box("E6_Fond", (0.160, 0.120, 0.002), c, (0.27, yy, 0.001), bevel=None)
    P[6] = [
        (box("E6_Exemple_Dalle", (0.120, 0.080, 0.006), c, (0.07, yy, 0.003), bevel=0.001, seg=2),
         R.dalle("E6_Exemple_Dalle"), None),
        (grille, R.depart("E6_Pratique_Grille", "B8B9BA", 1, 0.35), R.tole),
        (fond, R.depart("E6_Fond", "D04010", 0, 0.5), None),
        (box("E6_Pratique_Accoudoir", (0.300, 0.060, 0.050), c, (0.58, yy, 0.025), bevel=0.008, seg=4),
         R.depart("E6_Pratique_Accoudoir", "1E1B19", 0, 0.55), R.cuir),
        (box("E6_Pratique_Assise", (0.120, 0.120, 0.040), c, (0.92, yy, 0.020), bevel=0.010, seg=6),
         R.depart("E6_Pratique_Assise", "1F2A48", 0, 0.8), R.tissu),
        (cylinder("E6_Defi_Molette", 0.015, 0.040, c, (1.10, yy, 0.020), verts=128, bevel=0.001, seg=3),
         R.depart("E6_Defi_Molette", "C8C8C6", 1, 0.35), R.moletage),
        (curved_panel("E6_Defi_Panneau", c, (1.40, yy)), R.depart("E6_Defi_Panneau", "161618", 0, 0.3, (1, 0.02)),
         R.carbone),
    ]

    # Étape 7 : l'exemple de groupe et le socle à grouper
    c, yy = cols[7], y(7)
    g_grain = R.groupe_grain("PRC_Grain_Fin")
    P[7] = [
        (tile("E7_Exemple_Grain", c, (0.06, yy)), R.grain_groupe("E7_Exemple_Grain", g_grain), None),
        (cylinder("E7_Pratique_Socle", 0.090, 0.025, c, (0.32, yy, 0.0125), verts=64, bevel=0.003, seg=4),
         R.peinture_usee("E7_Pratique_Socle"), "groupe"),
    ]
    return cols, P


# ---------------------------------------------------------------------------- la lampe du défi final
def lampe_defi(root):
    col, objs = BL.load_lampe()          # la collection Lampe du chapitre 2, sans référence faible ni UV
    col.name = "Lampe_defi"
    mats = {name: M.lampe(name, new_name=name + "_defi") for name in sorted(set(BL.COLORIS_A.values()))}
    BL.dress(BL.COLORIS_A, objs, mats)
    off = Matrix.Translation(Vector((0.75, -2.30, 0.0)))
    for o in objs:
        o.name = o.name + "_defi"
        if o.data is not None:
            o.data.name = o.data.name + "_defi"
        if o.parent is None:
            o.matrix_basis = off @ o.matrix_basis
    return col, objs


def corriger_lampe(objs, c_corr, groupe):
    K = C.copy_objects(objs, c_corr, "_corrige", (CORR_DX, 0, 0))
    copies = {}
    for o in K.values():
        for slot in o.material_slots:
            m = slot.material
            if m is None:
                continue
            if m.name not in copies:
                cp = m.copy()
                cp.name = m.name + "_corrige"
                copies[m.name] = cp
            slot.material = copies[m.name]
    R.ajouter_usure(copies["Structure_Vert_defi"], groupe, "B8B9BA", (0, 0, 1))
    R.ajouter_usure(copies["Chrome_defi"], groupe, "E0C27A", (0, 0, 1), largeur=0.9, quantite=0.5)
    R.ajouter_salete(copies["ABS_Noir_defi"], 0.005)
    R.ajouter_rayures(copies["Alu_Brosse_defi"])
    R.ajouter_traces(copies["Peinture_Vert_defi"])
    return K


# ---------------------------------------------------------------------------- construction
def build():
    sc = C.reset_scene(raytracing=False)
    root = sc.collection
    et = R.depart("Etiquette", "2A2A2A", 0, 0.8)
    cols, P = rangees(root, et)
    lcol, lobjs = lampe_defi(root)
    corr = C.new_collection("Corrigé défi procédural", root)
    g_usure = R.groupe_usure("PRC_Usure_Bords_corrige", axe=True)
    g_tole = R.groupe_tole("PRC_Tole_Perforee_corrige")
    # pièces de travail : leur matière de départ
    for n, items in P.items():
        shared = None
        for ob, start, _rec in items:
            C.assign(ob, start)
    # corrigés : une sous-collection par étape
    for n, items in P.items():
        cc = C.new_collection("Corrigé étape %d" % n, corr)
        last = None
        for ob, start, rec in items:
            if rec is None:
                continue
            K = C.copy_objects([ob], cc, "_corrige", (CORR_DX, 0, 0))
            cp = K[ob.name]
            if rec == "meme":
                C.assign(cp, last)
                continue
            if rec == "groupe":
                last = R.usure_groupe(cp.name, g_usure)
            else:
                last = rec(cp.name)
            C.assign(cp, last)
        if n == 4:
            # 4.3 : la main courante de l'étape 3, avec sa patine en léger relief
            src = bpy.data.objects["E3_Pratique_Main_courante"]
            K = C.copy_objects([src], cc, "_corrige", (CORR_DX, -ROW, 0))
            cp = K[src.name]
            cp.name = cp.data.name = "E4_Relief_Main_courante_corrige"
            cp.location = (1.30 + CORR_DX, -3 * ROW, 0.016)        # au bout de la rangée 4 du corrigé
            C.assign(cp, R.patine("E4_Relief_Main_courante_corrige", relief=0.1))
        if n == 6:
            # le fond de la grille, pour voir à travers dans le corrigé
            K = C.copy_objects([bpy.data.objects["E6_Fond"]], cc, "_corrige", (CORR_DX, 0, 0))
        if n == 7:
            # ★★ la tôle perforée en millimètres, sur une copie de la grille et de son fond
            src = [bpy.data.objects["E6_Pratique_Grille"], bpy.data.objects["E6_Fond"]]
            K = C.copy_objects(src, cc, "_mm_corrige", (CORR_DX, -ROW, 0))
            g = K["E6_Pratique_Grille"]
            g.name = g.data.name = "E7_Grille_mm_corrige"
            f = K["E6_Fond"]
            f.name = f.data.name = "E7_Fond_mm_corrige"
            g.location = (0.62 + CORR_DX, -6 * ROW, 0.031)          # à côté du socle groupé
            f.location = (0.62 + CORR_DX, -6 * ROW, 0.001)
            C.assign(g, R.tole_groupe("E7_Grille_mm_corrige", g_tole))
            corriger_lampe(lobjs, cc, g_usure)
    # visibilité : les étapes 3 à 7, la lampe et les corrigés masqués à l'ouverture
    lc = bpy.context.view_layer.layer_collection.children
    for n in range(3, 8):
        lc[COLLECTIONS[n]].hide_viewport = True
    lc["Lampe_defi"].hide_viewport = True
    lc["Corrigé défi procédural"].hide_viewport = True
    # nœuds rangés en colonnes sans chevauchement ; rubrique Coat ouverte quand le vernis porte la recette
    for m in bpy.data.materials:
        if m.node_tree and m.name[:1] == "E" and m.name[1:2].isdigit():
            R.tidy(m.node_tree)
    for g in bpy.data.node_groups:
        if g.name.startswith("PRC_"):
            R.tidy(g)
    for name in ("E4_Exemple_Coque", "E4_Pratique_Coque_corrige", "E4_Defi_Coque_corrige", "E5_Pratique_Console_corrige"):
        p = next(n for n in bpy.data.materials[name].node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
        p.panel_states[4].is_collapsed = False          # Diffuse, Subsurface, Specular, Transmission, Coat…
    # un seul groupe « Smooth by Angle » : celui de la lampe du chapitre 2 et celui de Shade Auto Smooth
    for ng in list(bpy.data.node_groups):
        if ng.library is not None:
            ng.make_local(clear_asset_data=True)
    keep = bpy.data.node_groups.get("Smooth by Angle")
    for ng in list(bpy.data.node_groups):
        if ng is not keep and ng.name.startswith("Smooth by Angle"):
            ng.user_remap(keep)
            bpy.data.node_groups.remove(ng)
    txt = C.text_block(LISEZ_MOI)
    C.setup_layout(txt, 'MATERIAL', eye=(0.55, -0.95, 0.55), target=(0.55, -0.16, 0.0), distance_k=0.75)
    C.select_only(bpy.data.objects["E1_Pratique"])
    C.finalize(OUT, groups_expected=["Smooth by Angle", "PRC_Grain_Fin", "PRC_Usure_Bords_corrige",
                                     "PRC_Tole_Perforee_corrige"])
    print("MATIERES", len(bpy.data.materials), sorted(m.name for m in bpy.data.materials))
    print("OBJETS", len(bpy.data.objects))


build()
