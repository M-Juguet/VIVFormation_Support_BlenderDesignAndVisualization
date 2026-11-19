# Construit les fichiers 1 et 2 du chapitre 2 (plan : _resources/plans/PRC02-plan-chap2.md) :
#   - _resources/exercices/PRC02_ch2_lampe_depart.blend : fichier de travail, avec le gabarit, la
#     copie de travail, les croquis, et les corrigés masqués (« Corrigé », « Corrigé défis ») ;
#   - _resources/exercices/PRC02_ch2_lampe_modele.blend : la lampe terminée, sans suffixe, point de
#     départ du chapitre 3.
#
# Usage, depuis la racine du dépôt (le croquis croquis_ampoule.py doit exister) :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 `
#       -Script tool\exercices_ch2\build_lampe.py [-- depart|modele]
# Puis : finish_ui.py (hauteur de la zone LISEZ-MOI, fenêtre réelle), verifier_blend.py, rendus_controle.py.
#
# La variante A est lue dans _resources/exercices/PRC02_ch1_blocage_lampe.blend, sans modifier ce fichier.
# Toutes les dimensions sont en mètres (unités internes) ; les fichiers affichent des millimètres.
# La même fonction lamp() construit la lampe du corrigé (noms suffixés) et celle du fichier 2.

import math
import os
import sys

import bmesh
import bpy
from mathutils import Euler, Matrix, Vector
from mathutils.bvhtree import BVHTree

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
EX = os.path.join(ROOT, "_resources", "exercices")
SRC_CH1 = os.path.join(EX, "PRC02_ch1_blocage_lampe.blend")
CROQUIS = os.path.join(EX, "croquis_ampoule_profil.png")
OUT1 = os.path.join(EX, "PRC02_ch2_lampe_depart.blend")
OUT2 = os.path.join(EX, "PRC02_ch2_lampe_modele.blend")

VARIANTE_A = ["Socle_A", "Interrupteur_A", "Articulation_bas_A", "Bras_bas_A", "Articulation_milieu_A",
              "Bras_haut_A", "Articulation_haut_A", "Tête_A"]
GRIS = (0.784, 0.784, 0.784, 1.0)          # #C8C8C8
ORANGE = (0.910, 0.569, 0.227, 1.0)        # #E8913A

LISEZ_MOI_DEPART = """LISEZ-MOI · Chapitre 2 · Du blocage au modèle
Les valeurs sont indicatives : adaptez-les à votre concept.
Ctrl + Espace agrandit ce texte. Règle du jour : n'appliquez aucun modificateur.
D'abord : File > Save As, sous lampe_modele_v001.blend. Puis Ctrl + S à chaque contrôle.

0 · REPÈRES
Gabarit : le blocage, en fil de fer. Lampe : vos pièces.
Corrigé : collection « Corrigé », masquée (œil fermé) ; défis : « Corrigé défis ».
Une pièce vous manque ? Prenez-la dans « Corrigé » : M vers Lampe, puis renommez-la.

1 · SYMÉTRIE (Bras_bas, Bras_haut)
1. Bras_bas : Tab, A, S Maj+Z Maj+Z 0.5 (deux fois : l'axe du bras), G Y = 10mm, Tab.
2. Modifiers > Add Modifier > Generate > Mirror : décochez X, cochez Y.
3. Bras_haut : Tab, A, S Maj+Z Maj+Z 0.5, G Y = 10mm, Tab. Puis Bras_haut sélectionné,
   Bras_bas actif : menu du Mirror > Copy to Selected.
★ Sur une copie, G Y = 10mm en Mode Objet : que fait le Mirror ? Réglez Mirror Object sur Socle.
Contrôle : vue de dessus (7), deux tiges par bras.

2 · ÉPAISSEUR (Tête, Socle, Bras)
1. Tête : Tab, 3, clic sur la grande face de l'ouverture, X > Faces, Tab.
2. Add Modifier > Generate > Solidify : Thickness 1.5 mm, Offset -1, Even Thickness.
3. Object > Shade Auto Smooth.
4. À vous, sur Socle : Add Modifier > Generate > Bevel.
   Amount 3 mm, Segments 3, Limit Method Angle (déjà réglé). Puis Shade Auto Smooth.
5. Bras_bas et Bras_haut, sélectionnés ensemble : Object > Shade Auto Smooth.
★ Offset à 1, puis -1 ; Thickness 1 mm, puis 3 mm.
  Tête : Bevel (Amount 0.5 mm, Segments 2), prévu à l'atelier.
Contrôle : pile de la tête = Solidify, Smooth by Angle ;
pile du socle = Bevel, Smooth by Angle.

3 · RÉPÉTITION (grille d'aération, interrupteur)
1. Maj + C. Add > Mesh > Cube, F9 : Size 2 mm. Renommez : Grille_aeration.
2. Tab, S X 6, G X = 76mm, G Z = 25mm, Tab.
3. Add > Empty > Plain Axes, R Z 10. Renommez : Grille_pivot.
4. Grille_aeration : Add Modifier > Generate > Array (Legacy).
   Décochez Relative Offset, cochez Object Offset > Grille_pivot. Count 36.
5. Clic sur Grille_pivot, Maj + clic sur Grille_aeration, Ctrl + P > Object.
6. À vous : Interrupteur devient une molette de 24 crans (1,5 x 1,5 x 6 mm, à 8 mm de l'axe).
   Nommez Interrupteur_crans et Interrupteur_pivot. Quelle rotation pour l'Empty ?
★ 30 crans ; une demi-couronne de lamelles à l'arrière du socle.
Contrôle : déplacez Grille_aeration, la couronne suit. Ctrl + Z.

4 · LE CÂBLE
1. Vue de dessus (7). Add > Curve > Bézier, F9 : Radius 50 mm. Renommez : Câble.
2. Tab. E sur un point d'extrémité, ou Ctrl + clic droit : 4 à 5 points,
   de l'arrière du socle vers le bord de la table. V : Vector ou Automatic.
3. Object Data > Geometry > Bevel : Round, Depth 2.5 mm, Fill Caps.
4. Aimantation Face : le premier point contre le flanc du socle.
5. À vous : retracez le câble avec l'outil Curve Pen, avec une boucle.
★ Shape > Resolution Preview U à 24.
Contrôle : vue de face (1), le câble repose sur la table.

5 · L'AMPOULE
1. Clic sur Repere_ampoule, Maj + S > Cursor to Selected.
2. Add > Curve > Bézier. Renommez : Ampoule. Tab. X > Vertices sur le point de droite.
   Point restant : Maj + S > Selection to Cursor, puis V > Vector.
3. Vue de face (1), outil Curve Pen : clic sur les points 2 et 3,
   cliquer-glisser vertical sur le point 4, cliquer-glisser horizontal sur le point 5.
4. Tab. Add Modifier > Generate > Screw : Axis Z, Steps 32,
   Merge coché, distance 0.1 mm (le champ à droite de la case).
5. N > Item : Location 211, 0, 411 mm ; Rotation Y 150°.
★ Retouchez une poignée : l'ampoule suit. Comparez Steps 16 et 48.
Contrôle : une ampoule lisse et fermée, au fond de la tête.

6 · ATELIER
1. Articulations : Cursor to Selected sur chaque sphère, X pour la supprimer,
   Add > Mesh > Cylinder (F9 : Vertices 32, Radius 15, 14 ou 12 mm, Depth 36 mm),
   R X 90. Bevel (2 mm, 2 segments, Angle) et Shade Auto Smooth. Renommez.
2. Douille : Cursor to Selected sur Tête, Add > Mesh > Cylinder
   (F9 : Radius 15 mm, Depth 20 mm, Rotation Y -30°), puis G Z Z = 45mm (le long de son axe).
   Bevel (1 mm, 2 segments) et Shade Auto Smooth.
3. Tête : Bevel (Amount 0.5 mm, Segments 2). Il se range au-dessus de Smooth by Angle.
4. Interrupteur : Bevel (Amount 0.5 mm, Segments 2) et Shade Auto Smooth.
5. Checklist : noms clairs ; échelles à 1 ; aucune face rouge (Face Orientation) ;
   modificateurs actifs ; silhouette conforme au gabarit (vues 1 et 3).
6. Masquez Gabarit. Ctrl + S : lampe_modele_v001.blend.
★ Molettes sur les articulations (Alt + D de la molette, de ses crans et de son Empty) ;
  rainure du socle ; sous-collections Pied, Bras, Tête.
★★ Voir les défis du chapitre dans l'application ; solutions dans « Corrigé défis ».
   La liseuse a son propre fichier, avec son corrigé.
"""

LISEZ_MOI_MODELE = """LISEZ-MOI · Chapitre 2 · La lampe modélisée
Ctrl + Espace agrandit ce texte.
La lampe modélisée au chapitre 2 : le corrigé de l'atelier, et le point de départ du chapitre 3.
Les modificateurs sont actifs : ne les appliquez pas.
Pour repartir de ce fichier : File > Save As, sous lampe_modele_v001.blend.
Gabarit (le blocage) et Croquis sont masqués : l'œil de l'Outliner les réaffiche.
"""


# ---------------------------------------------------------------------------- outils
def new_collection(name, parent):
    c = bpy.data.collections.new(name)
    parent.children.link(c)
    return c


def move_to(ob, col):
    for c in list(ob.users_collection):
        c.objects.unlink(ob)
    col.objects.link(ob)


def mesh_from_bm(name, bm, col, matrix=Matrix()):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    ob.matrix_world = matrix
    return ob


def copy_mesh(src, name, col, off):
    me = src.data.copy()
    me.name = name
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    ob.matrix_world = Matrix.Translation(off) @ src.matrix_basis   # matrix_world pas encore calculée après l'ajout
    return ob


def cylinder(name, r, depth, col, matrix, seg=32, r2=None):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r, radius2=r if r2 is None else r2, depth=depth)
    return mesh_from_bm(name, bm, col, matrix)


def box(name, size, center, col, matrix=Matrix()):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=size, verts=bm.verts)
    bmesh.ops.translate(bm, vec=center, verts=bm.verts)
    return mesh_from_bm(name, bm, col, matrix)


def empty(name, size, col, matrix):
    e = bpy.data.objects.new(name, None)
    e.empty_display_type = 'PLAIN_AXES'
    e.empty_display_size = size
    col.objects.link(e)
    e.matrix_world = matrix
    return e


def parent_keep(child, parent):
    """Comme Ctrl + P > Object : l'enfant garde sa place et ses valeurs de Location."""
    bpy.context.view_layer.update()
    child.parent = parent
    child.matrix_parent_inverse = parent.matrix_world.inverted()


def bevel(ob, w, seg):
    m = ob.modifiers.new("Bevel", 'BEVEL')
    m.width = w
    m.segments = seg
    m.limit_method = 'ANGLE'
    return m


def array_ring(ob, pivot, count):
    a = ob.modifiers.new("Array", 'ARRAY')       # Array (Legacy) dans le menu
    a.use_relative_offset = False
    a.use_object_offset = True
    a.offset_object = pivot
    a.count = count
    return a


def screw(ob, steps=32, offset=0.0, iterations=1, merge=True):
    s = ob.modifiers.new("Screw", 'SCREW')
    s.axis = 'Z'
    s.angle = math.radians(360)
    s.steps = steps
    s.render_steps = steps
    s.screw_offset = offset
    s.iterations = iterations
    s.use_merge_vertices = merge
    s.merge_threshold = 0.0001
    return s


def solidify(ob, t=0.0015):
    s = ob.modifiers.new("Solidify", 'SOLIDIFY')
    s.thickness = t
    s.offset = -1
    s.use_even_offset = True
    return s


def auto_smooth(ob):
    """Object > Shade Auto Smooth, comme l'apprenant : ajoute Smooth by Angle, épinglé en bas."""
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = ob
    ob.select_set(True)
    bpy.ops.object.shade_auto_smooth()
    ob.select_set(False)
    assert ob.modifiers[-1].type == 'NODES' and ob.modifiers[-1].use_pin_to_last, ob.name


def bezier(name, pts, types, col, matrix=Matrix(), handles=None, cyclic=False):
    cu = bpy.data.curves.new(name, 'CURVE')
    cu.dimensions = '3D'
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(pts) - 1)
    sp.use_cyclic_u = cyclic
    for bp, p, t in zip(sp.bezier_points, pts, types):
        bp.co = p
        bp.handle_left_type = bp.handle_right_type = t
    for i, (hl, hr) in (handles or {}).items():
        bp = sp.bezier_points[i]
        bp.handle_left_type = bp.handle_right_type = 'ALIGNED'
        bp.handle_left = hl
        bp.handle_right = hr
    ob = bpy.data.objects.new(name, cu)
    col.objects.link(ob)
    ob.matrix_world = matrix
    return ob


def open_shell(ob):
    """Mode Édition, X > Faces sur la grande face du cône (z local le plus bas)."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    f = min(bm.faces, key=lambda f: f.calc_center_median().z)
    bmesh.ops.delete(bm, geom=[f], context='FACES_ONLY')
    bm.to_mesh(ob.data)
    bm.free()


def T(v):
    return Matrix.Translation(Vector(v))


def RX(deg):
    return Matrix.Rotation(math.radians(deg), 4, 'X')


def RY(deg):
    return Matrix.Rotation(math.radians(deg), 4, 'Y')


def RZ(deg):
    return Matrix.Rotation(math.radians(deg), 4, 'Z')


# ---------------------------------------------------------------------------- la lampe terminée
def lamp(col, sfx, A, off=(0, 0, 0)):
    """La lampe du fichier 2 (tableau « Le corrigé »), noms suffixés par sfx, décalée de off."""
    off = Vector(off)
    L = {}

    def n(base):
        return base + sfx

    # Socle : Bevel 3 mm, puis Shade Auto Smooth
    so = copy_mesh(A["Socle_A"], n("Socle"), col, off)
    bevel(so, 0.003, 3)
    auto_smooth(so)
    L["Socle"] = so

    # Grille d'aération : une lamelle de 12 x 2 x 2 mm, origine au centre du socle, Empty tourné de 10°
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=0.002)
    bmesh.ops.scale(bm, vec=(6, 1, 1), verts=bm.verts)
    bmesh.ops.translate(bm, vec=(0.076, 0, 0.025), verts=bm.verts)
    gr = mesh_from_bm(n("Grille_aeration"), bm, col, T(off))
    gp = empty(n("Grille_pivot"), 0.010, col, T(off) @ RZ(10))
    parent_keep(gp, gr)
    array_ring(gr, gp, 36)
    L["Grille_aeration"], L["Grille_pivot"] = gr, gp

    # Interrupteur, et sa molette de 24 crans
    it = copy_mesh(A["Interrupteur_A"], n("Interrupteur"), col, off)
    bevel(it, 0.0005, 2)
    auto_smooth(it)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=(0.0015, 0.0015, 0.006), verts=bm.verts)
    bmesh.ops.translate(bm, vec=(0.008, 0, 0), verts=bm.verts)
    cr = mesh_from_bm(n("Interrupteur_crans"), bm, col, T(off + Vector((0.055, 0, 0.028))))
    ip = empty(n("Interrupteur_pivot"), 0.005, col, T(off + Vector((0.055, 0, 0.028))) @ RZ(15))
    parent_keep(ip, cr)
    array_ring(cr, ip, 24)
    L["Interrupteur"], L["Interrupteur_crans"], L["Interrupteur_pivot"] = it, cr, ip

    # Articulations : cylindres de 32 côtés, couchés sur Y, 36 mm de long
    for base, dia in (("Articulation_bas", 0.030), ("Articulation_milieu", 0.028), ("Articulation_haut", 0.024)):
        src = A[base + "_A"]
        ob = cylinder(n(base), dia / 2, 0.036, col, T(off + src.location) @ RX(90))
        bevel(ob, 0.002, 2)
        auto_smooth(ob)
        L[base] = ob

    # Bras : tige de 8 ou 7 mm décalée de 10 mm en Y (Mode Édition), Mirror sur Y
    for base in ("Bras_bas", "Bras_haut"):
        ob = copy_mesh(A[base + "_A"], n(base), col, off)
        for v in ob.data.vertices:
            v.co.x *= 0.5
            v.co.y = v.co.y * 0.5 + 0.010
        m = ob.modifiers.new("Mirror", 'MIRROR')
        m.use_axis = (False, True, False)
        auto_smooth(ob)
        L[base] = ob

    # Tête : coque ouverte, Solidify 1,5 mm vers l'intérieur, Bevel 0,5 mm (atelier)
    te = copy_mesh(A["Tête_A"], n("Tête"), col, off)
    open_shell(te)
    solidify(te)
    bevel(te, 0.0005, 2)
    auto_smooth(te)
    L["Tête"] = te

    # Douille : au fond de la tête, sur son axe
    do = cylinder(n("Douille"), 0.015, 0.020, col, T(off + Vector((0.2110, 0, 0.4110))) @ RY(-30))
    bevel(do, 0.001, 2)
    auto_smooth(do)
    L["Douille"] = do

    # Ampoule : demi-profil de Bézier et Screw (points du croquis, en mètres). Les points sont rangés
    # du sommet (5) vers la base (1), comme les pose Curve Pen à partir du point 1 sélectionné : il
    # ajoute chaque point avant lui. Dans cet ordre, les normales du Screw regardent vers l'extérieur
    # (dans l'ordre 1 vers 5, elles regardent toutes vers l'intérieur : vérifié dans Blender 5.2.1).
    am = bezier(n("Ampoule"), [(0, 0, 0.080), (0.025, 0, 0.055), (0.0135, 0, 0.025), (0.0135, 0, 0.004), (0, 0, 0)],
                ['ALIGNED', 'AUTO', 'VECTOR', 'VECTOR', 'VECTOR'], col,
                T(off + Vector((0.2110, 0, 0.4110))) @ RY(150),
                handles={0: ((-0.012, 0, 0.080), (0.012, 0, 0.080))})
    screw(am)
    L["Ampoule"] = am

    # Câble : courbe de Bézier, poignées Aligned horizontales, section ronde de 5 mm
    pts = [Vector(p) for p in ((-0.0895, 0, 0.010), (-0.140, 0.004, 0.0025), (-0.200, 0.050, 0.0025),
                               (-0.265, 0.030, 0.0025), (-0.330, -0.020, 0.0025))]
    hd = {}
    for i, p in enumerate(pts):
        if i == 0:
            d = Vector((-1, 0, 0))
        else:
            d = (pts[min(i + 1, len(pts) - 1)] - pts[i - 1])
            d.z = 0
            d.normalize()
        ln_prev = (p - pts[i - 1]).length / 3 if i > 0 else 0.015
        ln_next = (pts[i + 1] - p).length / 3 if i < len(pts) - 1 else ln_prev
        hd[i] = (tuple(p - d * ln_prev), tuple(p + d * ln_next))
    ca = bezier(n("Câble"), [tuple(p) for p in pts], ['ALIGNED'] * 5, col, T(off), handles=hd)
    cu = ca.data
    cu.bevel_mode = 'ROUND'
    cu.bevel_depth = 0.0025
    cu.bevel_resolution = 4
    cu.use_fill_caps = True
    cu.resolution_u = 24
    L["Câble"] = ca
    for o in L.values():
        if o.type != 'EMPTY':
            o.color = GRIS
    return L


# ---------------------------------------------------------------------------- les défis sur la lampe
def defi_paliers(c, A):
    off = Vector((0.8, 0, 0))
    L = lamp(c, "_paliers", A, off)
    vl = bpy.context.view_layer
    iloc = off + Vector((0.055, 0, 0.028))
    pied = new_collection("Pied", c)
    bras = new_collection("Bras", c)
    tete = new_collection("Tête", c)
    for part in ("bas", "milieu", "haut"):
        a = L["Articulation_" + part]
        # Alt + D sur l'interrupteur, ses crans et son Empty, sélectionnés ensemble
        for o in vl.objects:
            o.select_set(False)
        for k in ("Interrupteur", "Interrupteur_crans", "Interrupteur_pivot"):
            L[k].select_set(True)
        vl.objects.active = L["Interrupteur"]
        bpy.ops.object.duplicate(linked=True)
        dup = {o.name.rsplit(".", 1)[0]: o for o in bpy.context.selected_objects}
        tgt = Vector((a.location.x, off.y + 0.021, a.location.z))
        M = T(tgt) @ RX(-90) @ T(-iloc)
        for o in dup.values():
            if o.parent is None or not o.parent.select_get():
                o.matrix_world = M @ o.matrix_world
        mol = dup["Interrupteur_paliers"]
        crn = dup["Interrupteur_crans_paliers"]
        piv = dup["Interrupteur_pivot_paliers"]
        assert crn.modifiers["Array"].offset_object == piv and piv.parent == crn
        mol.name = mol.data.name = "Molette_%s_corrige" % part
        crn.name = "Molette_%s_crans_corrige" % part
        piv.name = "Molette_%s_pivot_corrige" % part
        for o in (mol, crn, piv):
            move_to(o, bras)
            if o.type != 'EMPTY':
                o.color = ORANGE
            o.select_set(False)
    # La copie liée partage son maillage : le nom de maillage revient à l'interrupteur
    L["Interrupteur"].data.name = "Interrupteur_paliers"
    # Rainure : deux boucles à z = 11,5 et 13,5 mm, la bande extrudée de 1 mm vers l'axe
    so = L["Socle"]
    bm = bmesh.new()
    bm.from_mesh(so.data)
    for zz in (-0.001, 0.001):
        bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, zz), plane_no=(0, 0, 1))
    band = [f for f in bm.faces if abs(f.normal.z) < 0.01 and abs(f.calc_center_median().z) < 0.0009]
    ret = bmesh.ops.extrude_face_region(bm, geom=band)
    for v in [g for g in ret["geom"] if isinstance(g, bmesh.types.BMVert)]:
        r = math.hypot(v.co.x, v.co.y)
        k = (r - 0.001) / r
        v.co.x *= k
        v.co.y *= k
    bmesh.ops.delete(bm, geom=band, context='FACES')
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    nm = sum(1 for e in bm.edges if not e.is_manifold)
    bm.to_mesh(so.data)
    bm.free()
    so.color = ORANGE
    print("CONTROLE rainure : faces de la bande", len(band), "| arêtes non manifold", nm)
    for k in ("Socle", "Grille_aeration", "Grille_pivot", "Interrupteur", "Interrupteur_crans", "Interrupteur_pivot", "Câble"):
        move_to(L[k], pied)
    for k in ("Articulation_bas", "Articulation_milieu", "Articulation_haut", "Bras_bas", "Bras_haut"):
        move_to(L[k], bras)
    for k in ("Tête", "Douille", "Ampoule"):
        move_to(L[k], tete)
    return L


def defi_chape(c, A):
    off = Vector((1.6, 0, 0))
    L = lamp(c, "_chape", A, off)
    prof = [(0, 0.0165), (0.021, 0.0165), (0.021, -0.003), (0.018, -0.003), (0.018, 0.0135), (0, 0.0135)]
    bm = bmesh.new()
    v0 = [bm.verts.new((-0.013, y, z)) for y, z in prof]
    v1 = [bm.verts.new((0.013, y, z)) for y, z in prof]
    bm.faces.new(v0[::-1])
    bm.faces.new(v1)
    for i in range(len(prof) - 1):          # pas de face dans le plan de symétrie (y = 0)
        bm.faces.new((v0[i], v0[i + 1], v1[i + 1], v1[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    ch = mesh_from_bm("Chape_corrige", bm, c, T(L["Articulation_haut"].location))
    m = ch.modifiers.new("Mirror", 'MIRROR')
    m.use_axis = (False, True, False)
    m.use_bisect_axis = (False, True, False)
    m.use_clip = True
    bevel(ch, 0.0005, 2)
    auto_smooth(ch)
    ch.color = ORANGE
    return L


def defi_tulipe(c, A):
    off = Vector((2.4, 0, 0))
    L = lamp(c, "_tulipe", A, off)
    t = L.pop("Tête")
    M = t.matrix_world.copy()
    bpy.data.objects.remove(t)
    tu = bezier("Tête_tulipe_corrige", [(0, 0, 0.055), (0.022, 0, 0.055), (0.026, 0, 0.025), (0.050, 0, -0.025), (0.064, 0, -0.055)],
                ['VECTOR', 'VECTOR', 'AUTO', 'AUTO', 'VECTOR'], c, M)
    screw(tu)
    solidify(tu)
    auto_smooth(tu)
    tu.color = ORANGE
    L["Tête_tulipe"] = tu
    return L


def defi_ressorts(c, A):
    off = Vector((0.8, 0.8, 0))
    L = lamp(c, "_ressorts", A, off)
    r = 0.00075
    # sens de parcours choisi pour que les normales du Screw regardent vers l'extérieur du fil
    pts = [(0.005 + r, 0, 0), (0.005, 0, -r), (0.005 - r, 0, 0), (0.005, 0, r)]
    rs = bezier("Ressort_corrige", pts, ['AUTO'] * 4, c, T(off + Vector((-0.0179, 0.025, 0.1188))) @ RY(15.64), cyclic=True)
    screw(rs, steps=16, offset=0.006, iterations=16, merge=False)
    m = rs.modifiers.new("Mirror", 'MIRROR')
    m.use_axis = (False, True, False)
    m.mirror_object = L["Bras_bas"]
    rs.color = ORANGE
    return L


def defi_percage(c, A):
    off = Vector((1.6, 0.8, 0))
    L = lamp(c, "_percage", A, off)
    g = L["Grille_aeration"]
    for v in g.data.vertices:
        v.co.z = 0.025 + (v.co.z - 0.025) * 3          # 6 mm de haut, de z = 22 à 28 mm
    g.display_type = 'WIRE'
    g.hide_render = True
    so = L["Socle"]
    b = so.modifiers.new("Boolean", 'BOOLEAN')         # se range au-dessus de Smooth by Angle (épinglé)
    b.operation = 'DIFFERENCE'
    b.object = g
    b.solver = 'EXACT'
    so.color = ORANGE
    return L


def defi_grille_tete(c, A):
    off = Vector((2.4, 0.8, 0))
    L = lamp(c, "_grille_tete", A, off)
    M = L["Tête"].matrix_world.copy()
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=(0.0015, 0.0015, 0.012), verts=bm.verts)
    bmesh.ops.transform(bm, matrix=T((0.0306, 0, 0.030)) @ RY(-19.07), verts=bm.verts)
    g = mesh_from_bm("Grille_tete_corrige", bm, c, M)
    p = bpy.data.objects.new("Grille_tete_pivot_corrige", None)
    p.empty_display_type = 'PLAIN_AXES'
    p.empty_display_size = 0.005
    c.objects.link(p)
    p.parent = g
    p.rotation_euler = (0, 0, math.radians(15))      # rotation locale, par rapport à la tête
    array_ring(g, p, 24)
    g.color = ORANGE
    return L


# ---------------------------------------------------------------------------- scène et interface
def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.name = "Scene"
    sc.render.engine = 'BLENDER_EEVEE'
    us = sc.unit_settings
    us.system = 'METRIC'
    us.length_unit = 'MILLIMETERS'
    us.scale_length = 1.0
    sc.render.filepath = "//"
    if sc.world is None:
        sc.world = bpy.data.worlds.new("World")
    return sc


def append_ch1():
    """Lit la variante A et les croquis du chapitre 1, sans modifier le fichier livré."""
    want = VARIANTE_A + ["Croquis_face", "Croquis_profil"]
    with bpy.data.libraries.load(SRC_CH1, link=False) as (src, dst):
        missing = [n for n in want if n not in src.objects]
        assert not missing, missing
        dst.objects = want
    A = {o.name: o for o in dst.objects}
    # Les maillages et les images ajoutés gardent une référence faible au fichier du chapitre 1
    # (library_weak_reference) : on les remplace par des copies, qui n'en ont pas.
    for coll in (bpy.data.meshes, bpy.data.images):
        for idb in list(coll):
            if idb.library_weak_reference:
                name = idb.name
                cp = idb.copy()
                idb.user_remap(cp)
                coll.remove(idb)
                cp.name = name
    for im in bpy.data.images:
        im.filepath = "//" + im.name
        for pf in im.packed_files:
            pf.filepath = "//" + im.name
    return A


def croquis_ampoule(col):
    im = bpy.data.images.load(CROQUIS)
    im.pack()
    im.filepath = "//croquis_ampoule_profil.png"
    for pf in im.packed_files:
        pf.filepath = "//croquis_ampoule_profil.png"
    e = bpy.data.objects.new("Croquis_ampoule", None)
    e.empty_display_type = 'IMAGE'
    e.data = im
    e.empty_display_size = 0.120
    e.empty_image_offset = (-0.5, -0.5)
    e.location = (0.500, 0, 0.040)
    e.rotation_euler = (math.radians(90), 0, 0)
    e.color = (1, 1, 1, 0.5)
    e.use_empty_image_alpha = True
    e.empty_image_depth = 'BACK'
    e.show_empty_image_perspective = False
    e.show_empty_image_orthographic = True
    e.show_empty_image_only_axis_aligned = True
    col.objects.link(e)
    r = empty("Repere_ampoule", 0.010, col, T((0.500, 0, 0)))
    return e, r


def setup_ui(text_body, active, color_type):
    sc = bpy.context.scene
    txt = bpy.data.texts.new("LISEZ-MOI")
    txt.write(text_body)
    txt.cursor_set(0)
    shading = sc.display.shading
    shading.light = 'STUDIO'
    shading.color_type = color_type
    shading.show_cavity = True
    eye, target = Vector((0.75, -0.95, 0.55)), Vector((0.15, 0, 0.21))
    rot = (target - eye).to_track_quat('-Z', 'Y')
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                sp = area.spaces.active
                sp.shading.type = 'SOLID'
                sp.shading.light = 'STUDIO'
                sp.shading.color_type = color_type
                sp.shading.show_cavity = True
                sp.clip_start = 0.001
                sp.clip_end = 50.0
                if screen.name == "Layout":
                    r3d = sp.region_3d
                    r3d.view_perspective = 'PERSP'
                    r3d.view_location = target
                    r3d.view_rotation = rot
                    r3d.view_distance = (target - eye).length * 0.8
            if area.type == 'PROPERTIES' and screen.name == "Layout":
                area.spaces.active.context = 'MODIFIER'
            for space in area.spaces:
                if space.type == 'FILE_BROWSER' and space.params is not None:
                    space.params.directory = b"/" * 1200
                    space.params.directory = b"//"
    layout = bpy.data.screens["Layout"]
    done = False
    for area in layout.areas:
        if area.type == 'DOPESHEET_EDITOR':
            area.type = 'TEXT_EDITOR'
            sp = area.spaces.active
            sp.text = txt
            sp.show_word_wrap = True
            sp.show_line_numbers = False
            sp.show_syntax_highlight = False
            sp.top = 0
            done = True
            break
    assert done, "zone Timeline introuvable"
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = active
    active.select_set(True)


def finalize(path):
    # Shade Auto Smooth LIE le groupe « Smooth by Angle » depuis l'installation de Blender :
    # on le rend local, puis on retire les bibliothèques (y compris celle du chapitre 1).
    for ng in list(bpy.data.node_groups):
        if ng.library is not None:
            ng.make_local(clear_asset_data=True)
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    while len(bpy.data.libraries):
        lib = bpy.data.libraries[0]
        print("BIBLIOTHEQUE retirée :", lib.name)
        bpy.data.libraries.remove(lib)
    for ng in bpy.data.node_groups:
        assert ng.library is None, ng.name
    groups = [ng.name for ng in bpy.data.node_groups]
    assert groups == ["Smooth by Angle"], groups
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    bpy.context.preferences.filepaths.save_version = 0
    bpy.ops.wm.save_as_mainfile(filepath=path, compress=True, relative_remap=True)
    print("ENREGISTRE", path, os.path.getsize(path), "octets")


# ---------------------------------------------------------------------------- contrôles
def evaluated(ob, dg):
    e = ob.evaluated_get(dg)
    try:
        me = e.to_mesh()
    except Exception:
        return None
    if me is None or not len(me.vertices):
        e.to_mesh_clear()
        return None
    vs = [e.matrix_world @ v.co for v in me.vertices]
    ps = [tuple(p.vertices) for p in me.polygons]
    e.to_mesh_clear()
    return vs, ps


def controls(objs, tag):
    dg = bpy.context.evaluated_depsgraph_get()
    data = {o.name: evaluated(o, dg) for o in objs if o.type in ('MESH', 'CURVE') and o.display_type != 'WIRE'}
    data = {k: v for k, v in data.items() if v}
    trees = {k: BVHTree.FromPolygons(v[0], v[1]) for k, v in data.items()}
    names = sorted(trees)
    hits = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if trees[a].overlap(trees[b]):
                hits.append((a, b))
    print("CONTROLE", tag, "contacts :", hits)
    for k in names:
        vs = data[k][0]
        lo = [round(min(v[i] for v in vs) * 1000, 1) for i in range(3)]
        hi = [round(max(v[i] for v in vs) * 1000, 1) for i in range(3)]
        print("CONTROLE", tag, k, "min", lo, "max", hi, "sommets", len(vs))
    for o in objs:
        if o.modifiers:
            print("PILE", o.name, [m.name for m in o.modifiers])


# ---------------------------------------------------------------------------- les deux fichiers
def build_depart():
    sc = reset_scene()
    A = append_ch1()
    root = sc.collection
    c_gab = new_collection("Gabarit", root)
    c_lam = new_collection("Lampe", root)
    c_cro = new_collection("Croquis", root)
    c_cor = new_collection("Corrigé", root)
    c_def = new_collection("Corrigé défis", root)
    for n in VARIANTE_A:
        o = A[n]
        c_gab.objects.link(o)
        o.display_type = 'WIRE'
        o.hide_select = True
    for n in ("Croquis_face", "Croquis_profil"):
        c_cro.objects.link(A[n])
    croquis_ampoule(c_cro)
    # copies de travail : maillages indépendants, sans modificateur, noms sans suffixe
    work = {}
    for n in VARIANTE_A:
        base = n[:-2]
        work[base] = copy_mesh(A[n], base, c_lam, (0, 0, 0))
    # corrigés
    K = lamp(c_cor, "_corrige", A)
    controls(list(K.values()), "corrigé")
    subs = {}
    for name, fn in (("Paliers", defi_paliers), ("Chape", defi_chape), ("Tulipe", defi_tulipe),
                     ("Ressorts", defi_ressorts), ("Perçage", defi_percage), ("Grille tête", defi_grille_tete)):
        sub = new_collection(name, c_def)
        subs[name] = fn(sub, A)
    for name in ("Chape", "Tulipe", "Ressorts", "Perçage", "Grille tête"):
        objs = list(bpy.data.collections[name].all_objects)
        controls(objs, name)
    controls(list(bpy.data.collections["Paliers"].all_objects), "Paliers")
    lc = bpy.context.view_layer.layer_collection.children
    lc["Corrigé"].hide_viewport = True
    lc["Corrigé défis"].hide_viewport = True
    setup_ui(LISEZ_MOI_DEPART, work["Bras_bas"], 'RANDOM')
    finalize(OUT1)


def build_modele():
    sc = reset_scene()
    A = append_ch1()
    root = sc.collection
    c_lam = new_collection("Lampe", root)
    c_gab = new_collection("Gabarit", root)
    c_cro = new_collection("Croquis", root)
    for n in VARIANTE_A:
        o = A[n]
        c_gab.objects.link(o)
        o.display_type = 'WIRE'
        o.hide_select = True
    for n in ("Croquis_face", "Croquis_profil"):
        c_cro.objects.link(A[n])
    croquis_ampoule(c_cro)
    L = lamp(c_lam, "", A)
    controls(list(L.values()), "modèle")
    lc = bpy.context.view_layer.layer_collection.children
    lc["Gabarit"].hide_viewport = True
    lc["Croquis"].hide_viewport = True
    setup_ui(LISEZ_MOI_MODELE, L["Bras_bas"], 'OBJECT')
    finalize(OUT2)


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    if not which or "depart" in which:
        build_depart()
    if not which or "modele" in which:
        build_modele()
