# Rendus de contrôle EEVEE des fichiers du chapitre 2 : l'état de travail, puis chaque corrigé.
# Le fichier n'est pas enregistré : caméra et monde sont ajoutés en mémoire seulement.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup _resources\exercices\PRC02_ch2_lampe_depart.blend ^
#       --python tool\exercices_ch2\rendus_controle.py -- <dossier_de_sortie_absolu> [rendu ...]
#
# Chaque rendu montre une liste de collections (chemin « parent/enfant » pour une sous-collection),
# cadre les objets visibles depuis une direction donnée, puis écrit un PNG.

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
sc.render.resolution_x = 1100
sc.render.resolution_y = 800
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
# matière grise neutre, pour lire les formes (les fichiers n'ont pas de matière)
gris = bpy.data.materials.new("Controle_gris")
gris.use_nodes = True
bsdf = gris.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Roughness"].default_value = 0.45
for o in bpy.data.objects:
    if o.type in ('MESH', 'CURVE') and not o.material_slots:
        o.data.materials.append(gris)
    if o.type in ('MESH', 'CURVE'):
        if tuple(o.color[:3]) != (1.0, 1.0, 1.0):
            m = bpy.data.materials.new("Controle_" + o.name)
            m.use_nodes = True
            b = m.node_tree.nodes["Principled BSDF"]
            b.inputs["Base Color"].default_value = o.color
            b.inputs["Roughness"].default_value = 0.45
            o.data.materials.clear()
            o.data.materials.append(m)


def layer_collections(lc, path=""):
    for c in lc.children:
        p = (path + "/" if path else "") + c.collection.name
        yield p, c
        yield from layer_collections(c, p)


def show(paths):
    """Affiche exactement les collections données (et leurs parents), exclut les autres."""
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
    vis = []
    for o in vl.objects:
        if o.type in ('MESH', 'CURVE') and o.display_type not in ('WIRE', 'BOUNDS') and not o.hide_render:
            vis.append(o)
    return vis


def frame(objs, direction, lens=50, margin=1.05, look=None):
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for o in objs:
        oe = o.evaluated_get(dg)
        if o.type == 'CURVE':
            # la boîte englobante d'une courbe évaluée n'est pas fiable : on lit son maillage
            me = oe.to_mesh()
            pts += [oe.matrix_world @ v.co for v in me.vertices]
            oe.to_mesh_clear()
        else:
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


AV = (0.75, -0.95, 0.55)     # trois quarts avant droit, un peu en hauteur
# (nom, collections, objets à cadrer (None = tous les visibles), direction, focale, marge)
PRESETS = {
    "PRC02_ch2_lampe_depart.blend": [
        ("f1_travail", ["Lampe"], None, AV, 50, 1.0),
        ("f1_corrige", ["Corrigé"], None, AV, 50, 1.0),
        ("f1_corrige_dessous_tete", ["Corrigé"], ["Tête_corrige", "Douille_corrige", "Ampoule_corrige"], (0.9, -0.5, -0.9), 50, 1.0),
        ("f1_corrige_socle", ["Corrigé"], ["Socle_corrige", "Interrupteur_corrige"], (0.3, -0.7, 0.9), 50, 0.8),
        ("f1_paliers", ["Corrigé défis/Paliers"], None, (0.35, -1, 0.35), 50, 1.0),
        ("f1_paliers_molette", ["Corrigé défis/Paliers"], ["Molette_milieu_corrige", "Articulation_milieu_paliers"], (0.5, -1, 0.3), 50, 1.6),
        ("f1_paliers_rainure", ["Corrigé défis/Paliers"], ["Socle_paliers"], (0.2, -1, 0.35), 50, 0.7),
        ("f1_chape", ["Corrigé défis/Chape"], ["Chape_corrige", "Articulation_haut_chape"], (0.6, -1, 0.5), 50, 1.5),
        ("f1_tulipe", ["Corrigé défis/Tulipe"], ["Tête_tulipe_corrige", "Douille_tulipe", "Articulation_haut_tulipe"], (0.5, -1, 0.1), 50, 1.1),
        ("f1_ressorts", ["Corrigé défis/Ressorts"], ["Bras_bas_ressorts", "Ressort_corrige", "Articulation_bas_ressorts"], (0.5, -1, 0.3), 50, 1.0),
        ("f1_percage", ["Corrigé défis/Perçage"], ["Socle_percage"], (0.2, -0.6, 1.0), 50, 0.8),
        ("f1_grille_tete", ["Corrigé défis/Grille tête"], ["Tête_grille_tete", "Grille_tete_corrige"], (-0.6, -0.8, 0.9), 50, 1.1),
        ("f1_defis_tous", ["Corrigé défis"], None, (0.4, -1, 0.5), 35, 1.0),
    ],
    "PRC02_ch2_lampe_modele.blend": [
        ("f2_modele", ["Lampe"], None, AV, 50, 1.0),
        ("f2_modele_face", ["Lampe"], None, (0, -1, 0.05), 50, 1.0),
    ],
    "PRC02_ch2_liseuse_depart.blend": [
        ("f4_travail", ["Contexte", "Liseuse"], ["Platine", "Bouton", "Tête_liseuse"], (0.30, -0.55, 0.32), 45, 1.6),
        ("f4_corrige", ["Contexte", "Corrigé"], None, (0.30, -0.55, 0.32), 45, 1.0),
        ("f4_corrige_proche", ["Corrigé"], ["Platine_corrige", "Bouton_corrige", "Vis_corrige"], (0.4, -1, 0.35), 50, 1.3),
        ("f4_corrige_tete", ["Corrigé"], ["Tête_liseuse_corrige", "Diffuseur_corrige"], (0.3, -0.5, -0.8), 50, 1.3),
    ],
    "PRC02_ch2_demos_secteurs.blend": [
        ("f5_auto", ["Auto_capot"], None, (0.6, -1, 0.7), 50, 1.0),
        ("f5_aero", ["Aero_soufflante"], None, (0.5, -1, 0.4), 50, 1.0),
        ("f5_ferro_main", ["Ferro_main_courante"], None, (0.4, -1, 0.4), 50, 1.0),
        ("f5_ferro_roue", ["Ferro_roue"], None, (0.6, -1, 0.3), 50, 1.0),
    ],
}

base = os.path.basename(bpy.data.filepath)
for (name, cols, names, direction, lens, margin) in PRESETS[base]:
    if ONLY and name not in ONLY:
        continue
    vis = show(cols)
    objs = [bpy.data.objects[n] for n in names] if names else vis
    frame(objs, direction, lens, margin)
    sc.render.filepath = os.path.join(OUT, name + ".png")
    bpy.ops.render.render(write_still=True)
    print("RENDU", name, len(vis), "objets visibles")
