# Rendus de contrôle de la planche CMF, sans modifier le fichier : une caméra, un moteur, une taille.
# Mesure, sur l'image enregistrée (valeurs affichées, sRGB 0-255), le gris 18 %, le blanc, le noir et le fond.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup <fichier.blend> --python tool\exercices_cmf\rendus.py -- <camera> <EEVEE|CYCLES> <pourcent> <sortie.png> [controle] [rasante]

import os
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view

argv = sys.argv[sys.argv.index("--") + 1:]
cam_name, engine, pct, out = argv[0], argv[1], int(argv[2]), argv[3]
opts = set(argv[4:])
sc = bpy.context.scene
vl = bpy.context.view_layer


def lc(name):
    def walk(l):
        if l.collection.name == name:
            return l
        for k in l.children:
            r = walk(k)
            if r:
                return r
    return walk(vl.layer_collection)


if "controle" in opts:
    lc("Contrôle").exclude = False
if "rasante" in opts:
    lc("Lumière rasante").exclude = False
if "sanslumiere" in opts:
    lc("Éclairage").exclude = True
if "sansmonde" in opts:
    next(n for n in sc.world.node_tree.nodes if n.type == 'BACKGROUND').inputs["Strength"].default_value = 0.0
for o in opts:
    if o.startswith("area="):
        bpy.data.lights["Area_Principale"].energy = float(o[5:])
    if o.startswith("monde="):
        next(n for n in sc.world.node_tree.nodes if n.type == 'BACKGROUND').inputs["Strength"].default_value = float(o[6:])
    if o.startswith("emit="):
        p = next(n for n in bpy.data.materials["Fond_Blanc"].node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
        p.inputs["Emission Strength"].default_value = float(o[5:])
if "standard" in opts:
    sc.view_settings.view_transform = 'Standard'
sc.camera = bpy.data.objects[cam_name]
sc.render.engine = 'BLENDER_EEVEE' if engine == "EEVEE" else 'CYCLES'
if engine == "CYCLES":
    sc.cycles.samples = int(os.environ.get("CMF_CYCLES_SAMPLES", sc.cycles.samples))
sc.render.resolution_percentage = pct
sc.render.use_stamp_filename = False
sc.render.filepath = out
bpy.ops.render.render(write_still=True)
print("RENDU", out)

im = bpy.data.images.load(out)
w, h = im.size
px = list(im.pixels)


def sample(ob_name=None, co=None, r=4):
    from mathutils import Vector
    p = bpy.data.objects[ob_name].matrix_world.translation if ob_name else Vector(co)
    v = world_to_camera_view(sc, sc.camera, p)
    cx, cy = int(v.x * w), int(v.y * h)
    acc = [0, 0, 0]
    n = 0
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            if 0 <= x < w and 0 <= y < h:
                i = (y * w + x) * 4
                for c in range(3):
                    acc[c] += px[i + c]
                n += 1
    return tuple(round(a / max(n, 1) * 255) for a in acc)


if cam_name == "CAM_Planche":
    if "controle" in opts:
        for nm in ("Controle_Gris_18", "Controle_Blanc_90", "Controle_Noir_3"):
            print("MESURE", nm, sample(nm))
    for nm, co in (("fond_haut_droite", (0.30, 0.22, 0)), ("fond_bas_gauche", (-0.30, -0.24, 0)),
                   ("fond_centre_haut", (0.0, 0.24, 0))):
        print("MESURE", nm, sample(co=co))
    for nm in ("Emplacement_4", "Emplacement_1", "Emplacement_8", "Emplacement_5"):
        print("MESURE", nm, sample(nm, r=10))
