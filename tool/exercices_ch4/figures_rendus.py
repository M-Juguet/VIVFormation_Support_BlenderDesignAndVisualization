# Figures du chapitre 4 tirées de rendus EEVEE du fichier de secours, depuis une copie de travail en
# mémoire (le fichier n'est jamais enregistré). Écrit les JPEG dans assets/images/.
#   4.1  lamp_three_visuals_target_blender.jpg   4.10 raytracing_off_on_blender.jpg
#   4.13 view_transform_comparison_blender.jpg   4.14 hdri_comparison_blender.jpg
#   4.19 light_types_comparison_blender.jpg      4.21 area_size_comparison_blender.jpg
#   4.23 three_point_steps_blender.jpg           4.25 strip_light_reflection_blender.jpg
#   4.29 focal_length_comparison_blender.jpg     4.33 dof_comparison_blender.jpg
#   4.39 atelier_situation_blender.jpg           4.40 atelier_paliers_blender.jpg
# Les images du corrigé (rendus.py, mode corrige) doivent exister dans tool/exercices_ch4/_construction/images.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup _resources\exercices\PRC02_ch4_lampe_en_studio.blend ^
#       --python tool\exercices_ch4\figures_rendus.py -- [figure ...]

import math
import os
import sys

import bpy
import numpy as np
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
IMG = os.path.join(ROOT, "assets", "images")
CORR = os.path.join(HERE, "_construction", "images")
TMP = os.path.join(HERE, "_construction", "tmp")
os.makedirs(TMP, exist_ok=True)
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ONLY = set(args)
sc = bpy.context.scene
O = bpy.data.objects
W = bpy.data.worlds
T = Vector((0.11, 0.0, 0.22))
ROT_INTERIEUR = 135


# ---------------------------------------------------------------------------- images
def load(path):
    im = bpy.data.images.load(path)
    w, h = im.size
    px = np.array(im.pixels[:], dtype=np.float32).reshape(h, w, 4)[::-1].copy()   # haut en premier
    bpy.data.images.remove(im)
    return px


def resize(px, w):
    """Réduction par moyenne de zones (pas d'interpolation)."""
    h0, w0 = px.shape[:2]
    h = max(1, round(h0 * w / w0))
    ys = (np.arange(h + 1) * h0 / h).astype(int)
    xs = (np.arange(w + 1) * w0 / w).astype(int)
    c = np.cumsum(np.cumsum(np.pad(px, ((1, 0), (1, 0), (0, 0))), axis=0), axis=1)
    s = c[ys[1:]][:, xs[1:]] - c[ys[:-1]][:, xs[1:]] - c[ys[1:]][:, xs[:-1]] + c[ys[:-1]][:, xs[:-1]]
    area = ((ys[1:] - ys[:-1])[:, None] * (xs[1:] - xs[:-1])[None, :])[..., None]
    return s / area


def to_height(px, h):
    return resize(px, max(1, round(px.shape[1] * h / px.shape[0])))


def hcat(parts, gap=8):
    h = max(p.shape[0] for p in parts)
    sep = np.ones((h, gap, 4), dtype=np.float32)
    out = []
    for i, p in enumerate(parts):
        if i:
            out.append(sep)
        out.append(p)
    return np.concatenate(out, axis=1)


def vcat(parts, gap=8):
    w = max(p.shape[1] for p in parts)
    sep = np.ones((gap, w, 4), dtype=np.float32)
    out = []
    for i, p in enumerate(parts):
        if i:
            out.append(sep)
        out.append(p)
    return np.concatenate(out, axis=0)


def save(px, name, width=1200):
    if px.shape[1] > width:
        px = resize(px, width)
    h, w = px.shape[:2]
    im = bpy.data.images.new("fig", w, h, alpha=False)
    flat = px[::-1].copy()
    flat[..., 3] = 1.0
    im.pixels = flat.ravel()
    im.filepath_raw = os.path.join(IMG, name)
    im.file_format = 'JPEG'
    sc.render.image_settings.quality = 90
    im.save(filepath=os.path.join(IMG, name), quality=90)
    bpy.data.images.remove(im)
    print("FIGURE", name, w, "x", h)


# ---------------------------------------------------------------------------- scène
def base(world="Monde_Studio", lights=False, view='Khronos PBR Neutral', samples=64):
    sc.render.engine = 'BLENDER_EEVEE'
    sc.eevee.use_raytracing = True
    sc.eevee.taa_render_samples = samples
    sc.view_settings.view_transform = view
    sc.world = W[world]
    for c in bpy.data.collections:
        c.hide_render = c.name in ("Corrigé caméras", "Corrigé paliers", "Lampe_coloris_B", "Mise_en_situation",
                                   "Nuancier", "Corrigé éclairage")
    bpy.data.collections["Corrigé éclairage"].hide_render = not lights
    for n in ("Key_corrige", "Fill_corrige", "Rim_corrige", "Reflet_bande_corrige"):
        O[n].hide_render = False


def set_rot(world, deg):
    mp = next(n for n in W[world].node_tree.nodes if n.type == 'MAPPING')
    mp.inputs["Rotation"].default_value[2] = math.radians(deg)


def shoot(cam, res, tag):
    sc.camera = cam if not isinstance(cam, str) else O[cam]
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    path = os.path.join(TMP, tag + ".png")
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    return load(path)


def temp_camera(name, loc, target, lens):
    cd = bpy.data.cameras.new(name)
    cd.lens = lens
    cd.clip_start = 0.01
    ob = bpy.data.objects.new(name, cd)
    sc.collection.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    return ob


def temp_light(kind, loc, target, power, size=0.5, kelvin=5500):
    li = bpy.data.lights.new("tmp_" + kind, kind)
    li.energy = power
    li.use_temperature = True
    li.temperature = kelvin
    if kind == 'AREA':
        li.size = size
    if kind == 'SPOT':
        li.spot_size = math.radians(45)
    ob = bpy.data.objects.new("tmp_" + kind, li)
    sc.collection.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    return ob


def want(k):
    return not ONLY or k in ONLY


# ---------------------------------------------------------------------------- figures
if want("4.1"):
    parts = [load(os.path.join(CORR, n)) for n in
             ("PRC02_ch4_corrige_heros.png", "PRC02_ch4_corrige_detail.png", "PRC02_ch4_corrige_situation.png")]
    save(hcat([to_height(p, 540) for p in parts], 12), "lamp_three_visuals_target_blender.jpg")

if want("4.10"):
    base(view='AgX')
    sc.collection.children["Nuancier"].hide_render = False
    sc.eevee.use_raytracing = False
    a = shoot("CAM_banc_essai", (1280, 720), "rt_off")
    sc.eevee.use_raytracing = True
    b = shoot("CAM_banc_essai", (1280, 720), "rt_on")
    save(hcat([a[60:660, 80:1200], b[60:660, 80:1200]]), "raytracing_off_on_blender.jpg")

if want("4.13"):
    base(world="Monde_Studio")
    bpy.data.collections["Nuancier"].hide_render = False
    cam = temp_camera("tmp_nuancier", (0.66, -0.95, 0.30), (0.61, -0.15, 0.03), 60)
    parts = []
    for v in ("AgX", "Standard", "Khronos PBR Neutral"):
        sc.view_settings.view_transform = v
        parts.append(shoot(cam, (900, 420), "vt_" + v[:3]))
    save(hcat(parts), "view_transform_comparison_blender.jpg")

if want("4.14"):
    base()
    set_rot("Monde_Interieur", ROT_INTERIEUR)
    parts = []
    for w in ("Monde_Studio", "Monde_Interieur", "Monde_Exterieur"):
        sc.world = W[w]
        parts.append(shoot("CAM_banc_essai", (960, 540), "hdri_" + w)[40:520, 60:900])
    save(hcat(parts), "hdri_comparison_blender.jpg")

KEY_POS = (-0.60, -0.90, 0.90)
if want("4.19"):
    base(world="Monde_Neutre")
    parts = []
    for kind, power in (('POINT', 60), ('SUN', 3.0), ('SPOT', 60), ('AREA', 20)):
        li = temp_light(kind, KEY_POS, T, power)
        parts.append(shoot("CAM_heros_corrige", (960, 540), "type_" + kind)[60:540, 120:900])
        bpy.data.objects.remove(li)
    save(vcat([hcat(parts[:2]), hcat(parts[2:])]), "light_types_comparison_blender.jpg")

if want("4.21"):
    base(world="Monde_Neutre")
    parts = []
    for size in (0.05, 1.5):
        li = temp_light('AREA', KEY_POS, T, 20, size=size)
        parts.append(shoot("CAM_heros_corrige", (960, 540), "taille_%s" % size)[60:540, 120:900])
        bpy.data.objects.remove(li)
    save(hcat(parts), "area_size_comparison_blender.jpg")

if want("4.23"):
    base(world="Monde_Neutre", lights=True)
    O["Reflet_bande_corrige"].hide_render = True
    parts = []
    for on in (("Key_corrige",), ("Key_corrige", "Fill_corrige"), ("Key_corrige", "Fill_corrige", "Rim_corrige")):
        for n in ("Key_corrige", "Fill_corrige", "Rim_corrige"):
            O[n].hide_render = n not in on
        parts.append(shoot("CAM_heros_corrige", (960, 540), "trois_%d" % len(on))[40:540, 160:860])
    save(hcat(parts), "three_point_steps_blender.jpg")

if want("4.25"):
    base(world="Monde_Neutre", lights=True)
    parts = []
    for strip in (False, True):
        O["Reflet_bande_corrige"].hide_render = not strip
        px = shoot("CAM_heros_corrige", (1920, 1080), "bande_%d" % strip)
        parts.append(px[100:640, 880:1500])
    save(hcat(parts), "strip_light_reflection_blender.jpg")

if want("4.29"):
    base(world="Monde_Studio")
    eye = O["CAM_heros_corrige"].location.copy()
    d = (eye - T).normalized()
    dist85 = (eye - T).length
    parts = []
    for f in (24, 50, 100):
        cam = temp_camera("tmp_%d" % f, T + d * dist85 * f / 85, T, f)
        parts.append(shoot(cam, (720, 540), "focale_%d" % f)[:, 170:720])   # à 24 mm, le bout du fond entre à gauche
    save(hcat(parts), "focal_length_comparison_blender.jpg")

if want("4.33"):
    base(world="Monde_Neutre", lights=True)
    cam = O["CAM_detail_corrige"]
    parts = []
    for fs in (1.4, 8.0):
        cam.data.dof.aperture_fstop = fs
        parts.append(shoot(cam, (800, 800), "dof_%s" % fs))
    save(hcat(parts), "dof_comparison_blender.jpg")

if want("4.39"):
    save(load(os.path.join(CORR, "PRC02_ch4_corrige_situation.png")), "atelier_situation_blender.jpg")

if want("4.40"):
    parts = [load(os.path.join(CORR, n)) for n in
             ("corrige_profil_ortho.png", "corrige_gamme.png", "PRC02_ch4_corrige_situation_allumee.png")]
    save(hcat([to_height(p, 540) for p in parts], 12), "atelier_paliers_blender.jpg")
