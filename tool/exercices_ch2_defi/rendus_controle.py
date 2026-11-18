# Rendus de contrôle EEVEE du fichier du défi, rangée par rangée, état « pratique » puis « corrigé ».
# Le fichier n'est pas enregistré : caméra et monde sont ajoutés en mémoire seulement.
#
# Usage :
#   blender.exe -b --factory-startup _resources\exercices\PRC02_ch2_defi_modelisation.blend ^
#       --python tool\exercices_ch2_defi\rendus_controle.py -- <dossier_de_sortie_absolu> [rangée ...]

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
sc.render.resolution_y = 700
sc.eevee.taa_render_samples = 32
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
ROWS = {
    "1": ("Etape_1_Subdivision", "Corrigé étape 1", (0.35, -1, 0.75)),
    "2": ("Etape_2_Shrinkwrap", "Corrigé étape 2", (0.2, -1, 0.45)),
    "3": ("Etape_3_Cas_usage", "Corrigé étape 3", (0.2, -1, 0.45)),
    "4": ("Etape_4_Reglages", "Corrigé étape 4", (0.2, -1, 0.6)),
    "5": ("Etape_5_Booleens", "Corrigé étape 5", (0.2, -1, 0.35)),
    "6": ("Etape_6_Normales", "Corrigé étape 6", (0.2, -1, 0.35)),
    "A": ("Atelier_Retroviseur", "Corrigé atelier", (0.6, -1, 0.35)),
}


def all_layer_collections(lc):
    yield lc
    for c in lc.children:
        yield from all_layer_collections(c)


def frame(objs, direction, lens=50, margin=1.05, look=None):
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for o in objs:
        oe = o.evaluated_get(dg)
        pts += [oe.matrix_world @ Vector(c) for c in oe.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    c = (lo + hi) / 2 if look is None else Vector(look)
    r = (hi - lo).length / 2
    cam_data.lens = lens
    d = Vector(direction).normalized()
    dist = r * margin / math.sin(min(cam_data.angle_x, cam_data.angle_y) / 2)
    cam.location = c + d * dist
    cam.rotation_euler = (c - cam.location).to_track_quat('-Z', 'Y').to_euler()


def show(row_col, corr_col, corrected):
    for lc in all_layer_collections(vl.layer_collection):
        if lc.collection is sc.collection:
            continue
        name = lc.collection.name
        lc.exclude = name not in (row_col, "Corrigé défi modélisation", corr_col)
        if name == "Corrigé défi modélisation":
            lc.exclude = not corrected
        if name == corr_col:
            lc.exclude = not corrected
    corr_names = set()
    if corrected:
        corr_names = {o.name[:-len("_corrige")] for o in bpy.data.collections[corr_col].objects if o.name.endswith("_corrige")}
    vis = []
    for o in bpy.data.collections[row_col].objects:
        hidden = o.name in corr_names or o.display_type in ('WIRE', 'BOUNDS') or o.name.endswith("_reference")
        if corrected and o.name.startswith(("E3_Defi_Grille", "E5_Defi_Coupe", "Retro_Coupe", "E5_Coupe")):
            hidden = True
        o.hide_render = hidden
        if not hidden and o.type in ('MESH', 'FONT'):
            vis.append(o)
    if corrected:
        for o in bpy.data.collections[corr_col].objects:
            if o.display_type in ('WIRE', 'BOUNDS'):
                o.hide_render = True
            elif o.type == 'MESH':
                o.hide_render = False
                vis.append(o)
    return vis


# Gros plans : (nom, rangée, corrigé affiché ?, objets à cadrer, direction, focale, marge)
ZOOMS = [
    ("z1_carters", "1", True, ["E1_Exemple_Sans", "E1_Exemple_Crease", "E1_Pratique_Crease_corrige"], (0.3, -1, 0.8), 60, 1.0),
    ("z1_capot", "1", True, ["E1_Defi_Capot_corrige"], (0.5, -1, 0.6), 60, 1.0),
    ("z2_trappes", "2", False, ["E2_Exemple_Trappe_plate", "E2_Exemple_Trappe"], (0.0, -1, 0.15), 60, 1.0),
    ("z2_plaque", "2", True, ["E2_Pratique_Plaque_corrige"], (0.5, -1, 0.3), 60, 1.0),
    ("z3_hublots", "3", True, ["E3_Exemple_Hublot", "E3_Defi_Hublot_3_corrige"], (0.0, -1, 0.1), 60, 1.0),
    ("z3_bandeau", "3", True, ["E3_Exemple_Bandeau", "E3_Pratique_Bandeau_corrige"], (0.0, -1, 0.0), 60, 1.0),
    ("z3_prises", "3", True, ["E3_Exemple_Prise", "E3_Pratique_Prise_corrige", "E3_Defi_Grille_corrige"], (0.2, -1, 0.9), 60, 1.0),
    ("z3_prise_pratique", "3", False, ["E3_Pratique_Prise"], (0.2, -1, 0.5), 60, 1.2),
    ("z4_modes", "4", False, ["E4_Exemple_Mode_1", "E4_Exemple_Mode_4", "E4_Etiquette_1"], (0.0, -0.6, 1), 60, 1.0),
    ("z4_cadre8", "4", False, ["E4_Pratique_Cadre_8"], (0.0, -1, 0.1), 60, 1.2),
    ("z4_cadre8_corrige", "4", True, ["E4_Pratique_Cadre_8_corrige"], (0.0, -1, 0.1), 60, 1.2),
    ("z4_jonc", "4", True, ["E4_Defi_Jonc_corrige"], (0.3, -1, 0.5), 60, 1.0),
    ("z5_porte", "5", False, ["E5_Exemple_Porte"], (0.3, -1, 0.3), 60, 1.0),
    ("z5_hublot_corrige", "5", True, ["E5_Pratique_Fuselage_corrige"], (0.3, -1, 0.2), 90, 0.25),
    ("z5_joint_corrige", "5", True, ["E5_Defi_Nez_corrige"], (0.3, -1, 0.2), 90, 0.3),
    ("z6_brut", "6", False, ["E6_Exemple_Brut"], (0.35, -1, 0.3), 90, 0.25),
    ("z6_propre", "6", False, ["E6_Exemple_Propre"], (0.35, -1, 0.3), 90, 0.25),
    ("z6_platine", "6", False, ["E6_Pratique_Platine"], (0.5, -1, 0.5), 60, 1.0),
    ("z6_platine_corrige", "6", True, ["E6_Pratique_Platine_corrige"], (0.5, -1, 0.5), 60, 1.0),
    ("z6_joint_dt", "6", True, ["E6_Defi_Nez_corrige"], (0.3, -1, 0.2), 90, 0.3),
    ("zA_arriere", "A", True, ["Retro_Coque_corrige", "Retro_Platine_corrige"], (0.45, 1, 0.35), 60, 1.05),
    ("zA_avant", "A", True, ["Retro_Coque_corrige", "Retro_Platine_corrige"], (0.6, -1, 0.3), 60, 1.05),
    ("zA_pratique", "A", False, ["Retro_Coque", "Retro_Platine", "Retro_Clignotant"], (0.6, -1, 0.3), 60, 1.05),
]
LOOK = {
    "z5_hublot_corrige": "E5_Pratique_Fuselage_corrige",
    "z6_brut": "E6_Exemple_Brut",
    "z6_propre": "E6_Exemple_Propre",
}

if "zoom" in ONLY:
    for (name, key, corrected, names, direction, lens, margin) in ZOOMS:
        row_col, corr_col, _ = ROWS[key]
        show(row_col, corr_col, corrected)
        objs = [bpy.data.objects[n] for n in names]
        look = None
        if name in LOOK:
            look = bpy.data.objects[LOOK[name]].location.copy()
        if name.startswith(("z5_joint", "z6_joint")):
            o = bpy.data.objects[names[0]]
            look = o.location + Vector((0.25, -0.62, 0.35))
        frame(objs, direction, lens, margin, look)
        sc.render.filepath = os.path.join(OUT, name + ".png")
        bpy.ops.render.render(write_still=True)
        print("RENDU", name)
    sys.exit(0)

for key, (row_col, corr_col, direction) in ROWS.items():
    if ONLY and key not in ONLY:
        continue
    for corrected in (False, True):
        vis = show(row_col, corr_col, corrected)
        meshes = [o for o in vis if o.type == 'MESH']
        frame(meshes, direction)
        sc.render.filepath = os.path.join(OUT, "rangee_%s_%s.png" % (key, "corrige" if corrected else "pratique"))
        bpy.ops.render.render(write_still=True)
        print("RENDU", sc.render.filepath, len(meshes), "objets")
