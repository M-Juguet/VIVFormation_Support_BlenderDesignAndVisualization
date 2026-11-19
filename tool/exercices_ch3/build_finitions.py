# Construit la fiche C du chapitre 3 : _resources/exercices/PRC02_ch3_finitions_triplanaires.blend.
# Cinq pièces sans dépliage UV, une par secteur, aux matières « à compléter » (le Principled réglé et
# le nœud Image Texture déjà chargé, non relié), et la collection masquée « Corrigé » : les mêmes
# pièces, suffixées _corrige, décalées de Y - 0,60 m, avec leurs chaînes complètes.
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 -Script tool\exercices_ch3\build_finitions.py
# Puis finish_ui.py, qui ouvre le fichier sur l'espace Shading.

import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commun as C   # noqa: E402
import matieres as M   # noqa: E402

OUT = os.path.join(C.EX, "PRC02_ch3_finitions_triplanaires.blend")

LISEZ_MOI = """PRC02 · Chapitre 3 · Finitions triplanaires (défi)
Aucune pièce n'a de dépliage UV. Corrigé : collection « Corrigé » (œil fermé), matières suffixées _corrige.
Enregistrez ce fichier sous finitions_v001.blend avant de commencer.

Socle · L'accoudoir
- Texture Coordinate (Object) > Mapping (Scale 25) > Image Texture (grain_cuir) > Bump (Strength 0,3) > Normal.
- Image Texture : Non-Color, projection Box, Blend 0,3.
- L'accoudoir jumeau a un grain étiré : trouvez pourquoi, puis soignez-le.
★  La coque de rétroviseur
- Même chaîne avec grain_structure (Mapping Scale 100, Bump Strength 0,1).
- Réglez Blend jusqu'à ne plus voir de raccord sur les flancs courbes.
★★ Le marchepied et le panneau carbone
- Tôle larmée : relief marqué, Bump Strength 0,8, Mapping Scale 8,33.
- Carbone : deux images. La couleur (sRGB) va dans Base Color, le relief (Non-Color) dans Bump.
  Ajoutez un vernis : Coat Weight 1.
"""

COQUE = ("1A1A1A", 0, 0.45, {"image": ("grain_structure", 0.3, 100, 0.0001)})


def box(name, size, col, bevel_w=None, seg=3):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=size, verts=bm.verts)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    if bevel_w:
        b = ob.modifiers.new("Bevel", 'BEVEL')
        b.width = bevel_w
        b.segments = seg
        b.limit_method = 'ANGLE'
    return ob


def smooth_auto(ob):
    C.select_only(ob)
    bpy.ops.object.shade_auto_smooth()
    ob.select_set(False)


def coque(col):
    """Une demi-ellipsoïde de 220 x 120 x 140 mm, ouverte vers l'arrière (+Y), en coque de 2,5 mm."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=48, v_segments=24, radius=1.0)
    back = [v for v in bm.verts if v.co.y > 1e-6]
    bmesh.ops.delete(bm, geom=back, context='VERTS')
    bmesh.ops.scale(bm, vec=(0.110, 0.120, 0.070), verts=bm.verts)
    me = bpy.data.meshes.new("Coque_retroviseur")
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new("Coque_retroviseur", me)
    col.objects.link(ob)
    s = ob.modifiers.new("Solidify", 'SOLIDIFY')
    s.thickness = 0.0025
    s.offset = -1
    s.use_even_offset = True
    return ob


def panneau(col):
    """Un panneau de 300 x 200 mm, cintré de 45°. Le Bend sur l'axe Y courbe la longueur portée par Z
    local (vérifié : un plan couché en XY ne se courbe pas) : le panneau est construit debout, dans le
    plan YZ local, puis l'objet est couché par sa rotation."""
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=30, y_segments=20, size=0.5)
    bmesh.ops.scale(bm, vec=(0.300, 0.200, 1), verts=bm.verts)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(90), 3, 'Y'))
    me = bpy.data.meshes.new("Panneau_carbone")
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("Panneau_carbone", me)
    col.objects.link(ob)
    ob.rotation_euler = (0, math.radians(-90), 0)
    d = ob.modifiers.new("SimpleDeform", 'SIMPLE_DEFORM')
    d.deform_method = 'BEND'
    d.deform_axis = 'Y'
    d.angle = math.radians(45)
    s = ob.modifiers.new("Solidify", 'SOLIDIFY')
    s.thickness = 0.003
    s.offset = -1
    s.use_even_offset = True
    return ob


def pieces(col, suffix, dy, mats):
    """Les cinq pièces ; mats : nom de matière -> matière."""
    P = {}
    a = box("Accoudoir" + suffix, (0.300, 0.060, 0.050), col, 0.008, 4)
    a.location = (-0.35, dy, 0.025)
    j = box("Accoudoir_jumeau" + suffix, (0.150, 0.060, 0.050), col, 0.008, 4)
    j.location = (-0.35, dy + 0.15, 0.025)
    j.scale = (2.0, 1.0, 1.0)              # le piège : l'échelle n'est pas appliquée
    c = coque(col)
    c.name = c.data.name = "Coque_retroviseur" + suffix
    c.location = (0, dy, 0.07)
    m = box("Marchepied" + suffix, (0.600, 0.300, 0.020), col, 0.003, 2)
    m.location = (0.45, dy, 0.01)
    p = panneau(col)
    p.name = p.data.name = "Panneau_carbone" + suffix
    p.location = (0.45, dy + 0.35, 0.05)
    for ob in (a, j, c, m):
        smooth_auto(ob)
    C.assign(a, mats["Cuir_Graine_Noir"])
    C.assign(j, mats["Cuir_Graine_Noir"])
    C.assign(c, mats["Grainage_Retroviseur"])
    C.assign(m, mats["Tole_Larmee"])
    C.assign(p, mats["Carbone_Serge"])
    for ob in (a, j, c, m, p):
        P[ob.name] = ob
    return P


def build():
    sc = C.reset_scene(raytracing=True)
    root = sc.collection
    c_p = C.new_collection("Pièces", root)
    c_c = C.new_collection("Corrigé", root)
    start = {n: M.biblio(n, complete=False) for n in ("Cuir_Graine_Noir", "Tole_Larmee", "Carbone_Serge")}
    start["Grainage_Retroviseur"] = M.principled("Grainage_Retroviseur", *COQUE, complete=False)
    fini = {n: M.biblio(n, new_name=n + "_corrige") for n in ("Cuir_Graine_Noir", "Tole_Larmee", "Carbone_Serge")}
    fini["Grainage_Retroviseur"] = M.principled("Grainage_Retroviseur_corrige", *COQUE)
    P = pieces(c_p, "", 0.0, start)
    K = pieces(c_c, "_corrige", -0.60, fini)
    # dans le corrigé, l'échelle de l'accoudoir jumeau est appliquée (Ctrl + A > Scale)
    jc = K["Accoudoir_jumeau_corrige"]
    C.select_only(jc)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    jc.select_set(False)
    bpy.context.view_layer.layer_collection.children["Corrigé"].hide_viewport = True
    txt = C.text_block(LISEZ_MOI)
    C.setup_layout(txt, 'MATERIAL', eye=(0.35, -1.35, 0.85), target=(0.05, 0.10, 0.03), distance_k=0.75)
    C.select_only(P["Accoudoir"])
    C.finalize(OUT, groups_expected=["Smooth by Angle"])
    print("MATIERES", sorted(m.name for m in bpy.data.materials))


build()


def _controle():
    dg = bpy.context.evaluated_depsgraph_get()
    for n in ("Panneau_carbone", "Coque_retroviseur", "Accoudoir_jumeau"):
        e = bpy.data.objects[n].evaluated_get(dg)
        m = e.to_mesh()
        vs = [e.matrix_world @ v.co for v in m.vertices]
        print("CONTROLE", n, [round((max(v[i] for v in vs) - min(v[i] for v in vs)) * 1000, 1) for i in range(3)], "mm")
        e.to_mesh_clear()


_controle()
