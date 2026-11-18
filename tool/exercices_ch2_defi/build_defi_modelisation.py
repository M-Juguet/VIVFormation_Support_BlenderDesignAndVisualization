# Construit _resources/exercices/PRC02_ch2_defi_modelisation.blend
# (PRC02, chapitre 2, section 4 « Défi facultatif : modélisation avancée »).
#
# Usage, depuis la racine du dépôt :
#   "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --factory-startup ^
#       --python tool\exercices_ch2_defi\build_defi_modelisation.py
#
# Puis, pour agrandir la zone LISEZ-MOI (fenêtre réelle) : finish_ui_defi.py ; contrôle : verifier_blend.py
# (aucun chemin absolu) et rendus_controle.py (rendus EEVEE de chaque rangée et de chaque corrigé).
#
# Le plan de référence est _resources/plans/PRC02-plan-chap2-defi-modelisation.md.
# Les pièces à travailler sont construites sans modificateur (ou avec ceux que la recette
# suppose déjà là). Leur corrigé est construit avec la pile complète de la recette, à la
# même place, dans la collection masquée « Corrigé défi modélisation ».
# Toutes les dimensions sont en mètres (unités internes) ; le fichier affiche des millimètres.

import math
import os

import bmesh
import bpy
from mathutils import Euler, Matrix, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
TARGET = os.path.join(ROOT, "_resources", "exercices", "PRC02_ch2_defi_modelisation.blend")

ROW = 3.2           # écart entre les rangées des étapes (Y)
FUS_R = 1.0         # rayon du fuselage (avion d'affaires, Ø 2 m)
FUS_L = 2.4         # longueur du tronçon de fuselage
FUS_Z = 0.85        # hauteur de l'axe du tronçon au-dessus du sol de la scène
OFFSET = 0.0002     # 0,2 mm

LISEZ_MOI = """LISEZ-MOI : survolez cette zone et appuyez sur Ctrl + Espace pour l'agrandir (même raccourci pour revenir).

PRC02 · Chapitre 2 · Défi facultatif, hors programme : modélisation avancée
Enregistrez ce fichier sous defi_modelisation_v001.blend. Suivez la section 4 du chapitre 2 dans l'application.
Corrigés : collection « Corrigé défi modélisation » (œil fermé), une sous-collection par étape et une pour l'atelier.
Les corrigés sont à la place de vos pièces : affichez-les, puis masquez votre pièce (H) pour comparer.
Affichez seulement la collection de l'étape en cours. Vue locale : / du pavé numérique.
Couleurs : gris clair = carrosserie, gris sombre = détail fini, orange = pièce à travailler.
Valeurs indicatives, à taper avec leur unité : 0.2mm dans un champ, G X = 500mm pendant un geste.

PALIER 1
1 · Subdivision : Ctrl + 2. Boucles de maintien : Ctrl + R près des arêtes. Crease : Maj + E, 1.
    Les surfaces de référence sont prêtes : vous pouvez commencer à l'étape 2.
2 · Shrinkwrap : Add Modifier > Deform > Shrinkwrap, Target. Offset 0.2mm. Solidify EN DESSOUS.
3 · Hublot : Snap Mode = Above Surface. Bandeau : Project, axe Y. Prise d'air : Vertex Group « Raccord ».
4 · Les 4 modes : voir les étiquettes. Ordre : Subdivision, puis Shrinkwrap, puis Solidify.

PALIER 2
5 · Boolean, Difference. Objet de coupe : Display As = Wire, Renders décoché. Bevel SOUS le Boolean.
    Un objet de coupe se conforme sur la copie « _reference », jamais sur la pièce qu'il découpe.
6 ★★ · Data Transfer : Face Corner Data > Custom Normals ; Topology Mapping > Max Distance 0.3mm. Platine : Weighted Normal.
    Smooth by Angle : cliquez sur son épingle (Pin to Last), puis Data Transfer (ou Weighted Normal) > Move to Last.
    Les surfaces « _reference » sont masquées : Alt + H, ou l'œil dans l'Outliner, pour les voir.

ATELIER · Le rétroviseur : collection Atelier_Retroviseur. Consignes par paliers dans l'application.
Variantes ★★ : cadre de vitre frontale sur E3_Nez, hublot complet sur E3_Fuselage.
"""


# ---------------------------------------------------------------------------- outils
def srgb(hexs):
    h = hexs.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple((x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4) for x in c)


def material(name, hexs, rough, metal=0.0):
    m = bpy.data.materials.new(name)
    rgb = srgb(hexs)
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    m.diffuse_color = (*rgb, 1)
    m.roughness = rough
    m.metallic = metal
    return m


def collection(name, parent):
    c = bpy.data.collections.new(name)
    parent.children.link(c)
    return c


def link(ob, col):
    for c in list(ob.users_collection):
        c.objects.unlink(ob)
    col.objects.link(ob)
    return ob


def mesh_object(name, bm, mat, col, loc=(0, 0, 0), smooth=True):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    ob.location = loc
    if mat:
        me.materials.append(mat)
    for p in me.polygons:
        p.use_smooth = smooth
    return ob


def linked_copy(src, name, col, loc):
    ob = src.copy()
    ob.data = src.data
    ob.name = name
    col.objects.link(ob)
    ob.location = loc
    return ob


def full_copy(src, name, col):
    """Copie indépendante (maillage copié), même place, sans modificateur."""
    ob = src.copy()
    ob.data = src.data.copy()
    ob.data.name = name
    ob.name = name
    ob.modifiers.clear()
    col.objects.link(ob)
    return ob


def grid(nu, nv, fn, flip=False, bm=None):
    bm = bm or bmesh.new()
    vs = [[bm.verts.new(fn(i / nu, j / nv)) for j in range(nv + 1)] for i in range(nu + 1)]
    for i in range(nu):
        for j in range(nv):
            q = (vs[i][j], vs[i][j + 1], vs[i + 1][j + 1], vs[i + 1][j])
            bm.faces.new(tuple(reversed(q)) if flip else q)
    return bm, vs


def superellipse(a, b, n, t):
    c, s = math.cos(t), math.sin(t)
    return (a * math.copysign(abs(c) ** (2 / n), c), b * math.copysign(abs(s) ** (2 / n), s))


def ring_outline_bm(rings, seg, plane="XZ", depth=0.0, flip=False):
    """Anneau plat entre plusieurs contours. rings = [(a, b, n), ...] de l'extérieur vers l'intérieur."""
    bm = bmesh.new()
    loops = []
    for (a, b, n) in rings:
        row = []
        for i in range(seg):
            u, w = superellipse(a, b, n, 2 * math.pi * i / seg)
            co = (u, depth, w) if plane == "XZ" else (u, w, depth)
            row.append(bm.verts.new(co))
        loops.append(row)
    for r in range(len(loops) - 1):
        for i in range(seg):
            j = (i + 1) % seg
            q = (loops[r][i], loops[r][j], loops[r + 1][j], loops[r + 1][i])
            bm.faces.new(tuple(reversed(q)) if flip else q)
    return bm


def prism_bm(a, b, n, seg, y0, y1, center=(0, 0)):
    """Prisme fermé suivant Y, de section superellipse (objet de coupe)."""
    bm = bmesh.new()
    lo, hi = [], []
    for i in range(seg):
        u, w = superellipse(a, b, n, 2 * math.pi * i / seg)
        lo.append(bm.verts.new((center[0] + u, y0, center[1] + w)))
        hi.append(bm.verts.new((center[0] + u, y1, center[1] + w)))
    bm.faces.new(lo)
    bm.faces.new(list(reversed(hi)))
    for i in range(seg):
        j = (i + 1) % seg
        bm.faces.new((lo[i], lo[j], hi[j], hi[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return bm


def mod_subsurf(ob, lv=2, simple=False):
    s = ob.modifiers.new("Subdivision", "SUBSURF")
    s.levels = lv
    s.render_levels = lv
    if simple:
        s.subdivision_type = 'SIMPLE'
    return s


def mod_shrink(ob, target, method='NEAREST_SURFACEPOINT', offset=OFFSET, mode='ON_SURFACE', **kw):
    s = ob.modifiers.new("Shrinkwrap", "SHRINKWRAP")
    s.target = target
    s.wrap_method = method
    s.offset = offset
    s.wrap_mode = mode
    for k, v in kw.items():
        setattr(s, k, v)
    return s


def mod_solid(ob, t, off=1.0, even=True):
    s = ob.modifiers.new("Solidify", "SOLIDIFY")
    s.thickness = t
    s.offset = off
    s.use_even_offset = even
    return s


def mod_bevel(ob, w, seg, angle=True):
    b = ob.modifiers.new("Bevel", "BEVEL")
    b.width = w
    b.segments = seg
    b.limit_method = 'ANGLE' if angle else 'NONE'
    return b


def mod_bool(ob, cutter):
    b = ob.modifiers.new("Boolean", "BOOLEAN")
    b.operation = 'DIFFERENCE'
    b.object = cutter
    return b


def mod_transfer(ob, source, dist=0.0003):
    d = ob.modifiers.new("DataTransfer", "DATA_TRANSFER")
    d.object = source
    d.use_loop_data = True
    d.data_types_loops = {'CUSTOM_NORMAL'}
    d.loop_mapping = 'POLYINTERP_NEAREST'
    d.use_max_distance = True
    d.max_distance = dist
    return d


def auto_smooth(ob):
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    bpy.ops.object.shade_auto_smooth()
    ob.select_set(False)


def as_tool(ob, render=False):
    """Objet de coupe ou surface de référence : fil de fer, absent du rendu."""
    ob.display_type = 'WIRE'
    ob.hide_render = not render


def text(name, body, size, loc, mat, col, rot=(math.radians(90), 0, 0), align='LEFT'):
    cu = bpy.data.curves.new(name, 'FONT')
    cu.body = body
    cu.size = size
    cu.align_x = align
    ob = bpy.data.objects.new(name, cu)
    ob.location = loc
    ob.rotation_euler = rot
    cu.materials.append(mat)
    col.objects.link(ob)
    return ob


def evaluated_ray(target, origin, direction):
    """Point d'impact d'un rayon sur la cible évaluée (coordonnées monde), ou None."""
    dg = bpy.context.evaluated_depsgraph_get()
    te = target.evaluated_get(dg)
    mw = te.matrix_world
    inv = mw.inverted()
    o = inv @ Vector(origin)
    d = (inv.to_3x3() @ Vector(direction)).normalized()
    ok, loc, nor, idx = te.ray_cast(o, d)
    return (mw @ loc) if ok else None


def pin_last_order(ob):
    """Contrôle : Smooth by Angle est-il bien le dernier ?"""
    return [m.name for m in ob.modifiers]


# ---------------------------------------------------------------------------- surfaces de référence
def fuselage_bm(nu=12, na=10, length=FUS_L):
    # axe X à y = +R : la face avant du tronçon passe par y = 0 et regarde vers -Y
    def f(u, v):
        x = -length / 2 + length * u
        a = math.radians(-50 + 100 * v)
        return Vector((x, FUS_R - FUS_R * math.cos(a), FUS_R * math.sin(a)))
    bm, _ = grid(nu, na, f, flip=True)
    return bm


def nose_y(x, z):
    return -(0.40 * (1 - (x / 0.85) ** 2) + 0.25 * max(0.0, 1 - z / 1.2) ** 1.5)


def nose_bm():
    def f(u, v):
        x = -0.8 + 1.6 * u
        z = 1.2 * v
        return Vector((x, nose_y(x, z), z))
    bm, _ = grid(8, 6, f, flip=True)
    return bm


def hood_z(x, y):
    return 0.10 * (1 - (x / 0.55) ** 2) + 0.05 * (1 - ((y + 0.1) / 0.5) ** 2)


def hood_bm():
    def f(u, v):
        x = -0.5 + u
        y = -0.4 + 0.8 * v
        return Vector((x, y, hood_z(x, y)))
    bm, _ = grid(6, 6, f, flip=True)
    return bm


def handrail_bm():
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, segments=12, radius1=0.1, radius2=0.1, depth=0.5,
                          matrix=Matrix.Rotation(math.radians(90), 4, 'Y'))
    return bm


# ---------------------------------------------------------------------------- pièces
def carter_bm(loops=False):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Diagonal((0.12, 0.08, 0.04, 1)))
    if loops:
        for axis, half in ((0, 0.06), (1, 0.04), (2, 0.02)):
            for s in (-1, 1):
                no = Vector((0, 0, 0)); no[axis] = 1
                co = Vector((0, 0, 0)); co[axis] = s * (half - 0.004)
                geom = list(bm.verts) + list(bm.edges) + list(bm.faces)
                bmesh.ops.bisect_plane(bm, geom=geom, plane_co=co, plane_no=no)
    return bm


def hood_cage_bm():
    # capot de 600 x 400 mm, nervure centrale suivant X (rangée j = 2)
    def f(u, v):
        x = -0.3 + 0.6 * u
        y = -0.2 + 0.4 * v
        z = 0.05 * (1 - (x / 0.34) ** 2) + 0.03 * (1 - abs(y) / 0.2)
        return Vector((x, y, z))
    bm, vs = grid(6, 4, f, flip=True)
    return bm


def crease_edges(ob, pred, value):
    me = ob.data
    attr = me.attributes.get("crease_edge") or me.attributes.new("crease_edge", 'FLOAT', 'EDGE')
    for e in me.edges:
        a, b = me.vertices[e.vertices[0]].co, me.vertices[e.vertices[1]].co
        if pred(a, b):
            attr.data[e.index].value = value


def plate_xz_bm(w, h, nu, nv, y, cx=0.0, cz=0.0):
    bm, _ = grid(nu, nv, lambda u, v: Vector((cx - w / 2 + w * u, y, cz - h / 2 + h * v)), flip=True)
    return bm


def plate_xy_bm(w, h, nu, nv, z, cx=0.0, cy=0.0, ellipse=False):
    def f(u, v):
        s, t = 2 * u - 1, 2 * v - 1
        if ellipse:
            s, t = s * math.sqrt(1 - t * t / 2), t * math.sqrt(1 - s * s / 2)
        return Vector((cx + s * w / 2, cy + t * h / 2, z))
    bm, _ = grid(nu, nv, f)
    return bm


def scoop_bm(weights, z0):
    """Prise d'air : lèvre avant (y-) haute de 35 mm, arrière (y+) à plat. weights : none, binary, ring, smooth."""
    nu, nv = 16, 10
    sx, sy, hmax = 0.30, 0.20, 0.035
    bm = bmesh.new()
    dl = bm.verts.layers.deform.verify()
    vs = []
    for i in range(nu + 1):
        row = []
        for j in range(nv + 1):
            u, v = i / nu, j / nv
            prof = math.cos((u - 0.5) * math.pi) ** 0.6
            vt = bm.verts.new((-sx / 2 + sx * u, -sy / 2 + sy * v, z0 + hmax * prof * (1 - v) ** 1.3))
            border = i in (0, nu) or j == nv
            ring = (i in (1, nu - 1) and j >= 1) or (j == nv - 1 and 1 <= i <= nu - 1)
            if weights == "smooth":
                side = abs(u - 0.5) * 2
                w = max(min(1, max(0, (side - 0.55) / 0.45)), min(1, v ** 1.5))
            elif weights in ("binary", "select"):
                w = 1.0 if border else 0.0
            elif weights == "ring":
                w = 1.0 if border else (0.5 if ring else 0.0)
            else:
                w = 0.0
            if weights in ("smooth", "binary", "ring") and w > 0:
                vt[dl][0] = w
            vt.select = (weights == "select" and border)
            row.append(vt)
        vs.append(row)
    for i in range(nu):
        for j in range(nv):
            bm.faces.new((vs[i][j], vs[i + 1][j], vs[i + 1][j + 1], vs[i][j + 1]))
    bm.select_mode = {'VERT'}
    bm.select_flush_mode()
    return bm


def octagon_bm(y):
    return ring_outline_bm([(0.17, 0.17, 2), (0.12, 0.12, 2)], 8, "XZ", y, flip=True)


def porthole_frame_bm(y):
    # cadre de 280 x 380 mm, intérieur 210 x 310 mm, 96 points par contour
    return ring_outline_bm([(0.14, 0.19, 4.0), (0.1225, 0.1725, 4.0), (0.105, 0.155, 4.0)], 96, "XZ", y, flip=True)


def louvres_bm(z):
    bm = bmesh.new()
    for k in range(6):
        grid(18, 2, lambda u, v, k=k: Vector((-0.09 + 0.18 * u, 0.20 + 0.02 * k - 0.006 + 0.012 * v, z)), bm=bm)
    return bm


def joint_ring_bm(y, cx, cz):
    # ligne de joint : anneau de 4 mm autour d'une trappe de 300 x 200 mm
    bm = ring_outline_bm([(0.150, 0.100, 4.0), (0.146, 0.096, 4.0)], 128, "XZ", y, flip=True)
    bmesh.ops.translate(bm, verts=bm.verts, vec=(cx, 0, cz))
    return bm


def remap(t, table):
    keys = sorted(table)
    for a, b in zip(keys, keys[1:]):
        if a - 1e-6 <= t <= b + 1e-6:
            f = (t - a) / (b - a)
            return table[a] + f * (table[b] - table[a])
    return t


def mirror_shell_bm():
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=2.0)
    bmesh.ops.subdivide_edges(bm, edges=list(bm.edges), cuts=3, use_grid_fill=True)
    back = [f for f in bm.faces if f.calc_center_median().y > 0.999]
    bmesh.ops.delete(bm, geom=back, context='FACES')
    ytab = {-1.0: -1.0, -0.5: -0.55, 0.0: 0.05, 0.5: 0.82, 1.0: 1.0}
    for v in bm.verts:
        u, vv, w = v.co.x, remap(v.co.y, ytab), v.co.z
        t = (u + 1) / 2
        # coins arrondis dans le plan de l'ouverture, plus ronds vers le bout extérieur
        k = 0.20 + 0.55 * t
        ur = u * math.sqrt(1 - k * w * w / 2)
        wr = w * math.sqrt(1 - k * u * u / 2)
        tr = (ur + 1) / 2
        hz = 0.068 * (1 - 0.24 * t)
        z = wr * hz + 0.014 * t ** 2 - 0.006 * (1 - vv) / 2 * wr
        # profil en coin : le dessus file vers l'arrière, le bout extérieur s'amincit
        depth = 0.094 * (1 - 0.50 * t ** 2) * (1 - 0.32 * (w + 1) / 2)
        # face avant bombée : plus profonde au centre qu'aux bords
        depth *= 1 + 0.18 * (1 - (2 * t - 1) ** 2) * (1 - w * w)
        y = -depth * (1 - vv) / 2
        x = 0.235 * tr + 0.022 * (1 - vv) / 2 * tr
        v.co = Vector((x, y, z))
    return bm


MIRROR_C = Vector((0.115, -0.006 - 1.4, 0.004))


def mirror_ref_bm():
    def f(u, v):
        a = math.radians(-6 + 12 * u)
        b = math.radians(-4 + 8 * v)
        d = Vector((math.sin(a) * math.cos(b), math.cos(a) * math.cos(b), math.sin(b)))
        return MIRROR_C + d * 1.4
    bm, _ = grid(40, 24, f)
    return bm


def mirror_glass_bm():
    def f(u, v):
        s, t = 2 * u - 1, 2 * v - 1
        dx, dz = s * math.sqrt(1 - t * t / 2), t * math.sqrt(1 - s * s / 2)
        px, pz = 0.35 * s + 0.65 * dx, 0.35 * t + 0.65 * dz
        hz = 0.055 * (1 - 0.24 * (px + 1) / 2)
        return Vector((0.115 + 0.099 * px, -0.010, pz * hz + 0.012 * ((px + 1) / 2) ** 2))
    bm, _ = grid(24, 12, f, flip=True)
    return bm


def blink_bm():
    def f(u, v):
        x = 0.105 + 0.100 * u
        zc = -0.020 + 0.028 * u ** 1.6
        hh = 0.006 + 0.003 * (1 - u)
        return Vector((x, -0.20, zc + (2 * v - 1) * hh))
    bm, _ = grid(40, 3, f, flip=True)
    return bm


def foot_bm():
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Translation((-0.005, -0.045, -0.052)) @ Matrix.Diagonal((0.05, 0.04, 0.028, 1)))
    return bm


def platine_bm():
    bm = bmesh.new()
    pts = [(-0.11, -0.10), (0.03, -0.10), (0.03, -0.03), (-0.05, 0.0), (-0.11, -0.04)]
    vb = [bm.verts.new((-0.034, y, z)) for (y, z) in pts]
    vf = [bm.verts.new((-0.026, y, z)) for (y, z) in pts]
    bm.faces.new(vb)
    bm.faces.new(list(reversed(vf)))
    for i in range(len(pts)):
        j = (i + 1) % len(pts)
        bm.faces.new((vb[i], vb[j], vf[j], vf[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return bm


def platine_cut_bm():
    bm = bmesh.new()
    for (y, z, r) in [(-0.09, -0.085, 0.003), (0.015, -0.085, 0.003), (-0.09, -0.045, 0.003), (-0.035, -0.06, 0.006)]:
        bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=r, radius2=r, depth=0.03,
                              matrix=Matrix.Translation((-0.03, y, z)) @ Matrix.Rotation(math.radians(90), 4, 'Y'))
    return bm


def plate_holes_bm():
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0, matrix=Matrix.Diagonal((0.12, 0.008, 0.09, 1)))
    return bm


def plate_holes_cut_bm():
    bm = bmesh.new()
    for (hx, hz, r) in [(-0.04, 0.025, 0.003), (0.04, 0.025, 0.003), (0.0, -0.03, 0.003), (0.0, 0.0, 0.007)]:
        bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=r, radius2=r, depth=0.04,
                              matrix=Matrix.Translation((hx, 0, hz)) @ Matrix.Rotation(math.radians(90), 4, 'X'))
    return bm


def door_bm():
    def f(u, v):
        x = -0.45 + 0.9 * u
        z = 0.5 * v
        return Vector((x, -(0.05 * (1 - (x / 0.5) ** 2) + 0.03 * (1 - ((z - 0.25) / 0.3) ** 2)), z))
    bm, _ = grid(6, 4, f, flip=True)
    return bm


# ---------------------------------------------------------------------------- construction
def build():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.name = "Scene"
    scene.render.engine = 'BLENDER_EEVEE'
    us = scene.unit_settings
    us.system = 'METRIC'
    us.length_unit = 'MILLIMETERS'
    us.scale_length = 1.0
    scene.render.filepath = "//"
    if scene.world is None:
        scene.world = bpy.data.worlds.new("World")
    scene.tool_settings.mesh_select_mode = (True, False, False)

    m_body = material("Carrosserie", "#CCCCCC", 0.30)
    m_det = material("Detail", "#1A1A1C", 0.40)
    m_pra = material("Pratique", "#D9662A", 0.35)
    m_mir = material("Miroir", "#E6E6EA", 0.02, 1.0)

    root = scene.collection
    c_ref = collection("Surfaces_reference", root)
    c1 = collection("Etape_1_Subdivision", root)
    c2 = collection("Etape_2_Shrinkwrap", root)
    c3 = collection("Etape_3_Cas_usage", root)
    c4 = collection("Etape_4_Reglages", root)
    c5 = collection("Etape_5_Booleens", root)
    c6 = collection("Etape_6_Normales", root)
    ca = collection("Atelier_Retroviseur", root)
    cc = collection("Corrigé défi modélisation", root)
    k1 = collection("Corrigé étape 1", cc)
    k2 = collection("Corrigé étape 2", cc)
    k3 = collection("Corrigé étape 3", cc)
    k4 = collection("Corrigé étape 4", cc)
    k5 = collection("Corrigé étape 5", cc)
    k6 = collection("Corrigé étape 6", cc)
    ka = collection("Corrigé atelier", cc)

    # Les maillages de référence, partagés par copies liées. Les objets « source » sont rangés,
    # masqués, dans Surfaces_reference (collection exclue de la vue : rien à voir, rien à calculer).
    me_fus = mesh_object("Fuselage_ref", fuselage_bm(), m_body, c_ref)
    me_nez = mesh_object("Nez_ref", nose_bm(), m_body, c_ref)
    me_cap = mesh_object("Capot_ref", hood_bm(), m_body, c_ref)
    me_mc = mesh_object("Main_courante_ref", handrail_bm(), m_body, c_ref)
    for o in (me_fus, me_nez, me_cap):
        mod_subsurf(o, 2)
        auto_smooth(o)

    def target(src, name, col, loc, levels=2):
        o = linked_copy(src, name, col, loc)
        o.modifiers.clear()
        if src is not me_mc:
            mod_subsurf(o, levels)
            auto_smooth(o)
        return o

    titles = []

    def row_title(body, y, col):
        titles.append(text("Titre_" + col.name, body, 0.12, (-1.9, y - 0.9, 0.0), m_det, col))

    # ======================================================================= ÉTAPE 1
    y = 0.0
    row_title("Étape 1 · Surface de référence", y, c1)
    for k, (suffix, loops, crease) in enumerate((("Sans", False, False), ("Boucles", True, False), ("Crease", False, True))):
        o = mesh_object("E1_Exemple_" + suffix, carter_bm(loops), m_det, c1, (-1.2 + 0.2 * k, y, 0.02))
        if crease:
            crease_edges(o, lambda a, b: True, 1.0)
        mod_subsurf(o, 2)
    p_loops = mesh_object("E1_Pratique_Boucles", carter_bm(False), m_pra, c1, (-0.45, y, 0.02))
    p_crease = mesh_object("E1_Pratique_Crease", carter_bm(False), m_pra, c1, (-0.2, y, 0.02))
    mod_subsurf(p_crease, 2)
    d_cap = mesh_object("E1_Defi_Capot", hood_cage_bm(), m_pra, c1, (0.35, y, 0.0))
    mod_subsurf(d_cap, 2)
    # corrigés
    o = mesh_object("E1_Pratique_Boucles_corrige", carter_bm(True), m_det, k1, p_loops.location)
    mod_subsurf(o, 2)
    o = mesh_object("E1_Pratique_Crease_corrige", carter_bm(False), m_det, k1, p_crease.location)
    crease_edges(o, lambda a, b: a.z > 0.019 and b.z > 0.019, 1.0)
    mod_subsurf(o, 2)
    o = mesh_object("E1_Defi_Capot_corrige", hood_cage_bm(), m_det, k1, d_cap.location)
    crease_edges(o, lambda a, b: abs(a.y) < 1e-6 and abs(b.y) < 1e-6, 0.8)
    mod_subsurf(o, 2)

    # ======================================================================= ÉTAPE 2
    y = ROW
    row_title("Étape 2 · Le shrinkwrap", y, c2)
    f2 = target(me_fus, "E2_Fuselage", c2, (-0.6, y, FUS_Z))
    n2 = target(me_nez, "E2_Nez", c2, (2.2, y, 0.0))
    h2 = target(me_cap, "E2_Capot", c2, (4.3, y, 0.0))
    o = mesh_object("E2_Exemple_Trappe_plate", plate_xz_bm(0.20, 0.15, 20, 15, -0.0005, -0.6), m_det, c2, f2.location)
    mod_solid(o, 0.0015, 1.0)
    o = mesh_object("E2_Exemple_Trappe", plate_xz_bm(0.20, 0.15, 20, 15, -0.0005, -0.25), m_det, c2, f2.location)
    mod_shrink(o, f2)
    mod_solid(o, 0.0015, 1.0)
    hit = evaluated_ray(n2, (2.2, y - 2.0, 0.35), (0, 1, 0))
    # 25 mm devant le nez : le nez avance vers le bas, la plaque doit partir entièrement de
    # l'extérieur (sinon, en On Surface, ses sommets du bas finissent 0,2 mm dedans : étape 3.1)
    yp = hit.y - n2.location.y - 0.025
    p_pl = mesh_object("E2_Pratique_Plaque", plate_xz_bm(0.30, 0.12, 30, 12, yp, 0.0, 0.35), m_pra, c2, n2.location)
    zc = hood_z(0.25, 0.1) + 0.015
    d_mono = mesh_object("E2_Defi_Monogramme", plate_xy_bm(0.12, 0.06, 16, 8, zc, 0.25, 0.1, ellipse=True), m_pra, c2, h2.location)
    o = full_copy(p_pl, "E2_Pratique_Plaque_corrige", k2)
    o.data.materials[0] = m_det
    mod_shrink(o, n2)
    mod_solid(o, 0.002, 1.0)
    o = full_copy(d_mono, "E2_Defi_Monogramme_corrige", k2)
    o.data.materials[0] = m_det
    mod_shrink(o, h2)
    mod_solid(o, 0.002, 1.0)

    # ======================================================================= ÉTAPE 3
    y = 2 * ROW
    row_title("Étape 3 · Trois cas d'usage", y, c3)
    f3 = target(me_fus, "E3_Fuselage", c3, (-0.6, y, FUS_Z))
    n3 = target(me_nez, "E3_Nez", c3, (2.2, y, 0.0))
    h3 = target(me_cap, "E3_Capot", c3, (4.3, y, 0.0))
    # 3.1 hublot
    o = mesh_object("E3_Exemple_Hublot", porthole_frame_bm(-0.01), m_det, c3, f3.location)
    o.data.transform(Matrix.Translation((-0.9, 0, 0)))
    mod_shrink(o, f3, mode='ABOVE_SURFACE')
    mod_solid(o, 0.004, 1.0)
    auto_smooth(o)
    p_fr = mesh_object("E3_Pratique_Cadre", porthole_frame_bm(0.01), m_pra, c3, f3.location)
    p_fr.data.transform(Matrix.Translation((-0.3, 0, 0)))
    for dx, nm in ((0.0, "E3_Pratique_Cadre_corrige"), (0.5, "E3_Defi_Hublot_2_corrige"), (1.0, "E3_Defi_Hublot_3_corrige")):
        o = full_copy(p_fr, nm, k3)
        o.data.materials[0] = m_det
        o.location.x += dx
        mod_shrink(o, f3, mode='ABOVE_SURFACE')
        mod_solid(o, 0.004, 1.0)
        auto_smooth(o)
    # 3.2 bandeau
    o = mesh_object("E3_Exemple_Bandeau", plate_xz_bm(1.4, 0.06, 70, 3, -0.95, 0.0, 0.66), m_det, c3, n3.location)
    mod_shrink(o, n3, method='PROJECT', use_project_y=True)
    mod_solid(o, 0.002, 1.0)
    p_band = mesh_object("E3_Pratique_Bandeau", plate_xz_bm(1.4, 0.06, 70, 3, -0.95, 0.0, 0.42), m_pra, c3, n3.location)
    o = full_copy(p_band, "E3_Pratique_Bandeau_corrige", k3)
    o.data.materials[0] = m_det
    mod_shrink(o, n3, method='PROJECT', use_project_y=True)
    mod_solid(o, 0.002, 1.0)
    # 3.3 prise d'air
    z0 = max(hood_z(x, yy) for x in (-0.35, -0.2, -0.05, 0.05, 0.2, 0.35) for yy in (-0.1, 0.0, 0.1)) + 0.01
    o = mesh_object("E3_Exemple_Prise", scoop_bm("smooth", z0), m_det, c3, h3.location)
    o.data.transform(Matrix.Translation((-0.2, -0.05, 0)))
    o.vertex_groups.new(name="Raccord")
    mod_shrink(o, h3, offset=0.0, vertex_group="Raccord")
    mod_solid(o, 0.002, -1.0)
    auto_smooth(o)
    p_sc = mesh_object("E3_Pratique_Prise", scoop_bm("select", z0), m_pra, c3, h3.location)
    p_sc.data.transform(Matrix.Translation((0.2, -0.05, 0)))
    o = mesh_object("E3_Pratique_Prise_corrige", scoop_bm("ring", z0), m_det, k3, h3.location)
    o.data.transform(Matrix.Translation((0.2, -0.05, 0)))
    o.vertex_groups.new(name="Raccord")
    mod_shrink(o, h3, offset=0.0, vertex_group="Raccord")
    mod_solid(o, 0.002, -1.0)
    auto_smooth(o)
    # ★ grille de capot
    d_gr = mesh_object("E3_Defi_Grille", louvres_bm(0.25), m_pra, c3, h3.location)
    o = full_copy(d_gr, "E3_Defi_Grille_corrige", k3)
    o.data.materials[0] = m_det
    mod_shrink(o, h3, method='PROJECT', use_project_z=True, use_negative_direction=True)
    mod_solid(o, 0.003, 1.0)

    # ======================================================================= ÉTAPE 4
    y = 3 * ROW
    row_title("Étape 4 · Réglages et pile", y, c4)
    mc4 = linked_copy(me_mc, "E4_Main_courante", c4, (-0.9, y, 0.30))
    f4 = target(me_fus, "E4_Fuselage", c4, (1.4, y, FUS_Z))
    h4 = target(me_cap, "E4_Capot", c4, (4.1, y, 0.0))
    labels = (("NEAREST_SURFACEPOINT", "Nearest\nSurface Point", {}),
              ("PROJECT", "Project\n(Z, Negative)", {"use_project_z": True, "use_negative_direction": True}),
              ("NEAREST_VERTEX", "Nearest\nVertex", {}),
              ("TARGET_PROJECT", "Target Normal\nProject", {}))
    for k, (meth, lab, kw) in enumerate(labels):
        cx = -0.18 + 0.12 * k
        o = mesh_object("E4_Exemple_Mode_" + str(k + 1), plate_xy_bm(0.045, 0.16, 6, 40, 0.13, cx, 0.0), m_det, c4, mc4.location)
        mod_shrink(o, mc4, method=meth, offset=0.0003, **kw)
        o.show_wire = True
        text("E4_Etiquette_" + str(k + 1), lab, 0.016, (mc4.location.x + cx, y - 0.14, 0.14), m_det, c4, align='CENTER')
    p_oct = mesh_object("E4_Pratique_Cadre_8", octagon_bm(-0.01), m_pra, c4, f4.location)
    p_oct.show_wire = True
    o = full_copy(p_oct, "E4_Pratique_Cadre_8_corrige", k4)
    o.data.materials[0] = m_det
    mod_subsurf(o, 3, simple=True)
    mod_shrink(o, f4, mode='ABOVE_SURFACE')
    mod_solid(o, 0.004, 1.0)
    d_jonc = mesh_object("E4_Defi_Jonc", plate_xy_bm(0.6, 0.012, 6, 1, 0.22, 0.0, -0.28), m_pra, c4, h4.location)
    d_jonc.show_wire = True
    o = full_copy(d_jonc, "E4_Defi_Jonc_corrige", k4)
    o.data.materials[0] = m_det
    mod_subsurf(o, 2)
    mod_shrink(o, h4, mode='ABOVE_SURFACE')
    mod_solid(o, 0.003, 1.0)
    auto_smooth(o)

    # ======================================================================= ÉTAPE 5
    y = 4 * ROW
    row_title("Étape 5 · Booléens", y, c5)
    # exemple : portière en volume (40 mm) et logement de poignée
    door = mesh_object("E5_Exemple_Porte", door_bm(), m_body, c5, (-1.0, y, 0.25))
    mod_subsurf(door, 2)
    mod_solid(door, 0.04, -1.0)
    ys = -(0.05 * (1 - (0.15 / 0.5) ** 2) + 0.03 * (1 - ((0.30 - 0.25) / 0.3) ** 2))
    cut = mesh_object("E5_Exemple_Coupe", prism_bm(0.09, 0.02, 2.6, 64, ys - 0.2, ys + 0.015, (0.15, 0.30)), None, c5, door.location)
    as_tool(cut)
    mod_bool(door, cut)
    mod_bevel(door, 0.001, 3)
    auto_smooth(door)
    # pratique : fuselage et découpe de hublot
    f5 = target(me_fus, "E5_Pratique_Fuselage", c5, (1.6, y, FUS_Z))
    mod_solid(f5, 0.003, -1.0)
    f5.modifiers.move(f5.modifiers.find("Solidify"), 1)
    cut5 = mesh_object("E5_Coupe_Hublot", prism_bm(0.115, 0.165, 4.0, 96, -0.1, 0.1), m_pra, c5, f5.location)
    o = full_copy(f5, "E5_Pratique_Fuselage_corrige", k5)
    o.data = f5.data
    mod_subsurf(o, 2)
    mod_solid(o, 0.003, -1.0)
    k_cut5 = full_copy(cut5, "E5_Coupe_Hublot_corrige", k5)
    as_tool(k_cut5)
    mod_bool(o, k_cut5)
    mod_bevel(o, 0.001, 3)
    auto_smooth(o)
    # petit défi : ligne de joint sur le nez (peau de 6 mm), outil conformé sur la référence
    n5 = target(me_nez, "E5_Defi_Nez", c5, (4.0, y, 0.0))
    mod_solid(n5, 0.006, -1.0)
    n5.modifiers.move(n5.modifiers.find("Solidify"), 1)
    n5ref = target(me_nez, "E5_Nez_reference", c5, n5.location, levels=2)
    as_tool(n5ref)
    d_joint = mesh_object("E5_Defi_Coupe_Joint", joint_ring_bm(-0.9, 0.25, 0.35), m_pra, c5, n5.location)

    def nose_joint(col, name_nose, name_cut, transfer):
        o = full_copy(n5, name_nose, col)
        o.data = n5.data
        mod_subsurf(o, 2)
        mod_solid(o, 0.006, -1.0)
        c = full_copy(d_joint, name_cut, col)
        mod_shrink(c, n5ref, method='PROJECT', offset=0.0, use_project_y=True)
        mod_solid(c, 0.006, 0.0)
        as_tool(c)
        mod_bool(o, c)
        # Pas de Bevel : une ligne de joint reste vive, et un biseau sur une rainure aussi
        # étroite casse la géométrie (vérifié au rendu).
        if transfer:
            mod_transfer(o, n5ref)
        auto_smooth(o)
        return o
    nose_joint(k5, "E5_Defi_Nez_corrige", "E5_Defi_Coupe_Joint_corrige", False)

    # ======================================================================= ÉTAPE 6
    y = 5 * ROW
    row_title("Étape 6 ★★ · Normales propres", y, c6)

    def cut_fuselage(name, cut_name, col, loc, transfer, ref=None):
        # Smooth by Angle est épinglé en bas : les modificateurs ajoutés se rangent au-dessus.
        o = target(me_fus, name, col, loc)
        mod_solid(o, 0.003, -1.0)
        c = mesh_object(cut_name, prism_bm(0.115, 0.165, 4.0, 96, -0.1, 0.1), None, col, loc)
        as_tool(c)
        mod_bool(o, c)
        mod_bevel(o, 0.001, 3)
        if transfer:
            mod_transfer(o, ref)
        return o
    e6ref = target(me_fus, "E6_Exemple_reference", c6, (-1.0, y, FUS_Z), levels=2)
    as_tool(e6ref)
    cut_fuselage("E6_Exemple_Brut", "E6_Exemple_Brut_Coupe", c6, (-1.0 - 2.6, y, FUS_Z), False)
    cut_fuselage("E6_Exemple_Propre", "E6_Exemple_Propre_Coupe", c6, (-1.0, y, FUS_Z), True, e6ref)
    p6 = cut_fuselage("E6_Pratique_Fuselage", "E6_Coupe_Hublot", c6, (1.6, y, FUS_Z), False)
    p6ref = target(me_fus, "E6_Fuselage_reference", c6, p6.location, levels=2)
    as_tool(p6ref)
    o = cut_fuselage("E6_Pratique_Fuselage_corrige", "E6_Coupe_Hublot_corrige", k6, p6.location, True, p6ref)
    # platine percée
    plat = mesh_object("E6_Pratique_Platine", plate_holes_bm(), m_det, c6, (3.6, y, 0.3), smooth=True)
    pc = mesh_object("E6_Coupe_Platine", plate_holes_cut_bm(), None, c6, plat.location)
    as_tool(pc)
    mod_bool(plat, pc)
    mod_bevel(plat, 0.0008, 3)
    auto_smooth(plat)
    o = mesh_object("E6_Pratique_Platine_corrige", plate_holes_bm(), m_det, k6, plat.location)
    pck = mesh_object("E6_Coupe_Platine_corrige", plate_holes_cut_bm(), None, k6, plat.location)
    as_tool(pck)
    mod_bool(o, pck)
    mod_bevel(o, 0.0008, 3)
    w = o.modifiers.new("WeightedNormal", "WEIGHTED_NORMAL")
    w.keep_sharp = True
    auto_smooth(o)
    # défi : la ligne de joint du nez, nettoyée
    nose_joint(k6, "E6_Defi_Nez_corrige", "E6_Defi_Coupe_Joint_corrige", True)

    # ======================================================================= ATELIER
    y = 6 * ROW
    row_title("Atelier · Le rétroviseur", y, ca)
    L = Vector((0.0, y, 0.6))
    shell = mesh_object("Retro_Coque", mirror_shell_bm(), m_body, ca, L)
    mref = mesh_object("Retro_Miroir_reference", mirror_ref_bm(), None, ca, L)
    as_tool(mref)
    glass = mesh_object("Retro_Miroir", mirror_glass_bm(), m_mir, ca, L)
    blink = mesh_object("Retro_Clignotant", blink_bm(), m_pra, ca, L)
    foot = mesh_object("Retro_Pied", foot_bm(), m_body, ca, L)
    plate = mesh_object("Retro_Platine", platine_bm(), m_det, ca, L)
    pcut = mesh_object("Retro_Coupe_Platine", platine_cut_bm(), m_pra, ca, L)
    for o in (shell, glass, blink, foot, plate):
        for p in o.data.polygons:
            p.use_smooth = True
    # corrigé
    kshell = full_copy(shell, "Retro_Coque_corrige", ka)
    kref = full_copy(shell, "Retro_Coque_reference_corrige", ka)
    mod_subsurf(kref, 2)
    as_tool(kref)
    kref.hide_set(True)
    kblink = full_copy(blink, "Retro_Clignotant_corrige", ka)
    kblink.data.materials[0] = m_det
    kcut = full_copy(blink, "Retro_Coupe_Clignotant_corrige", ka)
    mod_shrink(kcut, kref, method='PROJECT', offset=0.0, use_project_y=True)
    mod_solid(kcut, 0.003, 0.0)
    as_tool(kcut)
    mod_subsurf(kshell, 2)
    mod_solid(kshell, 0.0025, -1.0)
    mod_bool(kshell, kcut)
    mod_bevel(kshell, 0.0004, 2)
    mod_transfer(kshell, kref)
    auto_smooth(kshell)
    mod_shrink(kblink, kref, method='PROJECT', offset=-0.0006, mode='ABOVE_SURFACE', use_project_y=True)
    mod_solid(kblink, 0.0015, 1.0)
    kglass = full_copy(glass, "Retro_Miroir_corrige", ka)
    mod_shrink(kglass, mref, offset=0.0)
    mod_solid(kglass, 0.002, -1.0)
    auto_smooth(kglass)
    kfoot = full_copy(foot, "Retro_Pied_corrige", ka)
    mod_bevel(kfoot, 0.004, 3, angle=False)
    auto_smooth(kfoot)
    kplate = full_copy(plate, "Retro_Platine_corrige", ka)
    kpcut = full_copy(pcut, "Retro_Coupe_Platine_corrige", ka)
    as_tool(kpcut)
    mod_bool(kplate, kpcut)
    mod_bevel(kplate, 0.0008, 3)
    w = kplate.modifiers.new("WeightedNormal", "WEIGHTED_NORMAL")
    w.keep_sharp = True
    auto_smooth(kplate)

    # ======================================================================= finitions
    # Les normales se règlent en dernier : Smooth by Angle, épinglé en bas par défaut, recalcule
    # les arêtes vives APRÈS Data Transfer ou Weighted Normal et dérègle leurs normales (vérifié au
    # rendu sur la ligne de joint). On le désépingle et on le place juste au-dessus d'eux.
    for o in bpy.data.objects:
        if o.type != 'MESH' or "Smooth by Angle" not in o.modifiers:
            continue
        idx = [i for i, m in enumerate(o.modifiers) if m.type in ('DATA_TRANSFER', 'WEIGHTED_NORMAL')]
        if idx:
            sm = o.modifiers["Smooth by Angle"]
            sm.use_pin_to_last = False
            o.modifiers.move(o.modifiers.find("Smooth by Angle"), idx[0])

    # Pas de couche UV (le défi n'en utilise pas).
    for me in bpy.data.meshes:
        while me.uv_layers:
            me.uv_layers.remove(me.uv_layers[0])

    vl = bpy.context.view_layer
    lc = vl.layer_collection.children
    lc["Surfaces_reference"].exclude = True
    for name in ("Etape_2_Shrinkwrap", "Etape_3_Cas_usage", "Etape_4_Reglages", "Etape_5_Booleens",
                 "Etape_6_Normales", "Atelier_Retroviseur"):
        lc[name].hide_viewport = True
    lc["Corrigé défi modélisation"].hide_viewport = True
    # surfaces de référence masquées dans la vue (H) : elles restent utilisables par les modificateurs
    for o in (n5ref, e6ref, p6ref):
        o.hide_set(True)

    # LISEZ-MOI
    txt = bpy.data.texts.new("LISEZ-MOI")
    txt.write(LISEZ_MOI)
    txt.cursor_set(0)

    shading = scene.display.shading
    shading.light = 'STUDIO'
    shading.color_type = 'MATERIAL'
    shading.show_object_outline = True
    shading.show_cavity = True

    view_rot = Euler((math.radians(62), 0, math.radians(-22))).to_quaternion()
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                sp = area.spaces.active
                sp.shading.type = 'SOLID'
                sp.shading.light = 'STUDIO'
                sp.shading.color_type = 'MATERIAL'
                sp.shading.show_object_outline = True
                sp.shading.show_cavity = True
                if screen.name == "Layout":
                    r3d = sp.region_3d
                    r3d.view_perspective = 'PERSP'
                    r3d.view_location = (-0.55, 0.0, 0.05)
                    r3d.view_rotation = view_rot
                    r3d.view_distance = 2.4
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

    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = p_loops
    p_loops.select_set(True)

    # ------------------------------------------------------------------- contrôles
    dg = bpy.context.evaluated_depsgraph_get()

    def ev(o):
        return o.evaluated_get(dg).data

    # la plaque plate décolle, la trappe conformée non
    print("CONTROLE monogramme corrigé, faces :", len(ev(bpy.data.objects["E2_Defi_Monogramme_corrige"]).polygons))
    g = bpy.data.objects["Retro_Miroir_corrige"]
    g.modifiers["Solidify"].show_viewport = False
    dg.update()
    ys_ = [v.co.y for v in ev(g).vertices]
    print("CONTROLE bombé du miroir, sans épaisseur (mm) :", round((max(ys_) - min(ys_)) * 1000, 2))
    g.modifiers["Solidify"].show_viewport = True
    dg.update()
    for nm in ("E5_Pratique_Fuselage_corrige", "E5_Defi_Nez_corrige", "E6_Pratique_Fuselage_corrige",
               "E6_Defi_Nez_corrige", "Retro_Coque_corrige", "E6_Pratique_Platine_corrige", "E5_Exemple_Porte"):
        o = bpy.data.objects[nm]
        base = len(o.data.vertices)
        print("CONTROLE", nm, "faces évaluées :", len(ev(o).polygons), "| pile :", pin_last_order(o))
    blk =ev(bpy.data.objects["Retro_Clignotant_corrige"])
    yb = [v.co.y for v in blk.vertices]
    print("CONTROLE clignotant corrigé y (mm) :", round(min(yb) * 1000, 1), round(max(yb) * 1000, 1))

    # Shade Auto Smooth LIE le groupe « Smooth by Angle » depuis les actifs livrés avec Blender
    # (chemin absolu vers Program Files). On le rend local et on retire la bibliothèque.
    for ng in list(bpy.data.node_groups):
        if ng.library is not None:
            ng.make_local(clear_asset_data=True)
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    # Deux blocs Library liés entre eux : supprimer le premier supprime aussi l'autre.
    while len(bpy.data.libraries):
        lib = bpy.data.libraries[0]
        print("BIBLIOTHEQUE retirée :", lib.name)
        bpy.data.libraries.remove(lib)
    for ng in bpy.data.node_groups:
        assert ng.library is None, ng.name
        print("GROUPE", ng.name, "utilisateurs", ng.users, "actif", ng.asset_data is not None)
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    bpy.context.preferences.filepaths.save_version = 0
    bpy.ops.wm.save_as_mainfile(filepath=TARGET, compress=True, relative_remap=True)
    print("ENREGISTRE", TARGET, os.path.getsize(TARGET))


if __name__ == "__main__":
    build()
