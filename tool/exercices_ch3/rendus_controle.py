# Rendus de contrôle EEVEE des fichiers du chapitre 3 : l'état de travail, puis chaque corrigé.
# Le fichier n'est pas enregistré : caméra, monde et Raytracing sont réglés en mémoire seulement.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup <fichier.blend> --python tool\exercices_ch3\rendus_controle.py -- <dossier_sortie> [rendu ...]
# Repris de tool/exercices_ch2/rendus_controle.py.

import math
import os
import sys

import bpy
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:]
OUT = args[0]
ONLY = set(args[1:])
os.makedirs(OUT, exist_ok=True)
HDRI = os.path.join(os.path.dirname(bpy.app.binary_path), "%d.%d" % bpy.app.version[:2],
                    "datafiles", "studiolights", "world", "studio.exr")

sc = bpy.context.scene
sc.render.resolution_x = 1200
sc.render.resolution_y = 800
sc.eevee.taa_render_samples = 48
sc.eevee.use_raytracing = True
w = bpy.data.worlds.new("Controle")
sc.world = w
w.use_nodes = True
env = w.node_tree.nodes.new("ShaderNodeTexEnvironment")
env.image = bpy.data.images.load(HDRI)
w.node_tree.links.new(env.outputs["Color"], w.node_tree.nodes["Background"].inputs["Color"])
cam_data = bpy.data.cameras.new("Controle")
cam_data.clip_start = 0.001
cam = bpy.data.objects.new("Controle", cam_data)
sc.collection.objects.link(cam)
sc.camera = cam
vl = bpy.context.view_layer
gris = bpy.data.materials.new("Controle_gris")
gris.use_nodes = True
gris.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.45
for o in bpy.data.objects:
    if o.type in ('MESH', 'CURVE') and not any(s.material for s in o.material_slots):
        o.data.materials.clear()
        o.data.materials.append(gris)


def layer_collections(lc, path=""):
    for c in lc.children:
        p = (path + "/" if path else "") + c.collection.name
        yield p, c
        yield from layer_collections(c, p)


def show(paths):
    keep = set()
    for p in paths:
        parts = p.split("/")
        for i in range(1, len(parts) + 1):
            keep.add("/".join(parts[:i]))
    for p, lc in layer_collections(vl.layer_collection):
        inside = any(p == k or p.startswith(k + "/") for k in paths)
        lc.exclude = not (p in keep or inside)
        lc.hide_viewport = False
    vl.update()
    return [o for o in vl.objects if o.type in ('MESH', 'CURVE') and not o.hide_render]


def frame(objs, direction, lens=50, margin=1.05):
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for o in objs:
        oe = o.evaluated_get(dg)
        me = oe.to_mesh()
        pts += [oe.matrix_world @ v.co for v in me.vertices]
        oe.to_mesh_clear()
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    c = (lo + hi) / 2
    r = (hi - lo).length / 2
    cam_data.lens = lens
    d = Vector(direction).normalized()
    dist = r * margin / math.sin(min(cam_data.angle_x, cam_data.angle_y) / 2)
    cam.location = c + d * dist
    cam.rotation_euler = (c - cam.location).to_track_quat('-Z', 'Y').to_euler()


AV = (0.75, -0.95, 0.55)
DEF = (0.35, -1, 0.75)
PRESETS = {
    "PRC02_ch3_nuancier_cmf.blend": [
        ("b_nuancier", ["Support", "Grille_Metallic_Roughness", "Nuancier"], None, DEF, 50, 0.95),
        ("b_grille", ["Grille_Metallic_Roughness"], None, (0, -1, 0.45), 50, 1.0),
        ("b_metaux", ["Nuancier"], [o for o in ("Pastille_Alu_Naturel", "Pastille_Titane_Satine")], (0.0, -1, 0.5), 50, 0.9),
        ("b_verres", ["Nuancier"], ["Pastille_Verre_Clair", "Pastille_Polycarbonate_Rouge"], (0.0, -1, 0.4), 50, 1.0),
        ("b_textures", ["Nuancier"], ["Pastille_Cuir_Graine_Noir", "Pastille_Tole_Larmee"], (0.0, -1, 0.4), 50, 1.1),
        ("b_peintures", ["Nuancier"], ["Pastille_Laque_Rouge", "Pastille_Peinture_Metallisee_Bleu"], (0.0, -1, 0.4), 50, 1.0),
    ],
    "PRC02_ch3_lampe_a_habiller.blend": [
        ("a_travail", ["Lampe"], None, AV, 50, 1.0),
        ("a_corrige_A", ["Corrigé coloris A"], None, AV, 50, 1.0),
        ("a_corrige_B", ["Corrigé coloris B"], None, AV, 50, 1.0),
        ("a_corrige_A_bras", ["Corrigé coloris A"], ["Bras_bas_A", "Articulation_milieu_A"], (0.4, -1, 0.3), 50, 0.7),
        ("a_corrige_A_socle", ["Corrigé coloris A"], ["Socle_A", "Interrupteur_A"], (0.3, -0.8, 0.8), 50, 0.8),
        ("a_corrige_A_ampoule", ["Corrigé coloris A"], ["Tête_A", "Ampoule_A", "Douille_A"], (0.9, -0.5, -0.9), 50, 1.0),
        ("a_bras_proche", ["Corrigé coloris A"], ["Bras_bas_A"], (0.3, -1, 0.15), 50, 0.12),
        ("a_socle_proche", ["Corrigé coloris A"], ["Socle_A"], (0.4, -1, 0.6), 50, 0.45),
    ],
    "PRC02_ch3_lampe_habillage.blend": [
        ("a2_deux_coloris", ["Lampe", "Lampe_coloris_B"], None, (0.3, -1, 0.45), 50, 0.95),
        ("a2_coloris_A", ["Lampe"], None, AV, 50, 1.0),
        ("a2_coloris_B", ["Lampe_coloris_B"], None, AV, 50, 1.0),
    ],
    "PRC02_ch3_finitions_triplanaires.blend": [
        ("c_travail", ["Pièces"], None, DEF, 50, 1.0),
        ("c_corrige", ["Corrigé"], None, DEF, 50, 1.0),
        ("c_corrige_accoudoirs", ["Corrigé"], ["Accoudoir_corrige", "Accoudoir_jumeau_corrige"], (0.3, -1, 0.8), 50, 0.9),
        ("c_travail_accoudoirs", ["Pièces"], ["Accoudoir", "Accoudoir_jumeau"], (0.3, -1, 0.8), 50, 0.9),
        ("c_corrige_coque", ["Corrigé"], ["Coque_retroviseur_corrige"], (0.6, -1, 0.5), 50, 1.0),
        ("c_corrige_carbone", ["Corrigé"], ["Panneau_carbone_corrige", "Marchepied_corrige"], (0.3, -1, 0.9), 50, 0.9),
    ],
}

base = os.path.basename(bpy.data.filepath)
for (name, cols, names, direction, lens, margin) in PRESETS[base]:
    if ONLY and name not in ONLY:
        continue
    vis = show(cols)
    objs = [bpy.data.objects[n] for n in names] if names else [o for o in vis if not o.name.startswith("Etiquette")]
    frame(objs, direction, lens, margin)
    sc.render.filepath = os.path.join(OUT, name + ".png")
    bpy.ops.render.render(write_still=True)
    print("RENDU", name, len(vis), "objets visibles")
