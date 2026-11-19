# Rendus EEVEE des figures du défi procédural (section 4 du chapitre 3) : planches de comparaison et vues
# des pièces, sous l'image d'environnement « studio » de Material Preview, sur un fond uni.
# Le fichier n'est pas enregistré : matières, caméra et monde sont créés en mémoire seulement.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup _resources\exercices\PRC02_ch3_defi_procedural.blend ^
#       --python tool\exercices_ch3\rendus_figures_defi.py -- <dossier_captures_brutes> [rendu ...]
# Les images r_*.png rejoignent les captures brutes ; recadrer_defi.py les assemble en figures.

import math
import os
import sys

import bpy
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import defi_recettes as R   # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
OUT = args[0]
ONLY = set(args[1:])
os.makedirs(OUT, exist_ok=True)
HDRI = os.path.join(os.path.dirname(bpy.app.binary_path), "%d.%d" % bpy.app.version[:2],
                    "datafiles", "studiolights", "world", "studio.exr")
O = bpy.data.objects

sc = bpy.context.scene
sc.eevee.taa_render_samples = 64
sc.eevee.use_raytracing = False            # comme le fichier des apprenants
# monde : l'image studio éclaire, un fond uni gris sombre se voit (comme Material Preview)
w = bpy.data.worlds.new("Figures")
sc.world = w
nt = w.node_tree
env = nt.nodes.new("ShaderNodeTexEnvironment")
env.image = bpy.data.images.load(HDRI)
lp = nt.nodes.new("ShaderNodeLightPath")
mix = nt.nodes.new("ShaderNodeMix")
mix.data_type = 'RGBA'
mix.inputs["B"].default_value = (0.030, 0.031, 0.033, 1.0)
nt.links.new(lp.outputs["Is Camera Ray"], mix.inputs["Factor"])
nt.links.new(env.outputs["Color"], mix.inputs["A"])
nt.links.new(mix.outputs["Result"], nt.nodes["Background"].inputs["Color"])
cam_data = bpy.data.cameras.new("Figures")
cam_data.clip_start = 0.001
cam = bpy.data.objects.new("Figures", cam_data)
sc.collection.objects.link(cam)
sc.camera = cam
vl = bpy.context.view_layer
for lc in vl.layer_collection.children:
    lc.exclude = False


def only(names):
    keep = set(names)
    for o in bpy.data.objects:
        if o.type in ('MESH', 'CURVE', 'FONT'):
            o.hide_render = o.name not in keep


def frame(names, direction, lens=60, margin=1.05):
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for n in names:
        oe = O[n].evaluated_get(dg)
        me = oe.to_mesh()
        pts += [oe.matrix_world @ v.co for v in me.vertices]
        oe.to_mesh_clear()
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    c = (lo + hi) / 2
    r = (hi - lo).length / 2
    cam_data.lens = lens
    d = Vector(direction).normalized()
    dist = r * margin / math.sin(min(cam_data.angle_x, cam_data.angle_y) / 2)
    cam.location = c + d * dist
    cam.rotation_euler = (c - cam.location).to_track_quat('-Z', 'Y').to_euler()


def give(names, mat):
    for n in names:
        o = O[n]
        o.data.materials.clear()
        o.data.materials.append(mat)


def shot(name, names, direction, res=(600, 600), lens=60, margin=1.05, rotate=0.0):
    if ONLY and name not in ONLY:
        return
    only(names)
    frame(names, direction, lens, margin)
    sc.render.resolution_x, sc.render.resolution_y = res
    env.texture_mapping.rotation[2] = math.radians(rotate)
    sc.render.filepath = os.path.join(OUT, name + ".png")
    bpy.ops.render.render(write_still=True)
    print("RENDU", name)


TILE = "E1_Pratique"
TOP = (0.0, -0.55, 1.0)


def tile(name, mat, direction=TOP):
    give([TILE], mat)
    shot(name, [TILE], direction, (520, 520), margin=0.78)


def apercu(name, socket_fn, **kw):
    """Une matière en aperçu : socket_fn(chaine) renvoie la sortie à montrer."""
    c = R.Chaine(name, **kw)
    c.view(socket_fn(c))
    return c.m


# ---------------------------------------------------------------------------- étape 1
for key in ("Noise_defaut", "Noise", "Noise_detail", "Noise_distortion", "Noise_ridged", "Voronoi", "Voronoi_bords",
            "Voronoi_couleur", "Wave", "Wave_ondule", "Wave_anneaux", "Gabor", "Gabor_serre", "Gabor_isotrope",
            "Gabor_axe_x"):
    tile("r_e1_" + key.lower(), R.e1("r_" + key, key))

# ---------------------------------------------------------------------------- étape 2
def ramp_apercu(stops, interp='LINEAR'):
    def fn(c):
        nz = c.node("ShaderNodeTexNoise", 1, 0, i_Scale=100)
        c.link(c.tc(2).outputs["Object"], nz.inputs["Vector"])
        if stops is None:
            return nz.outputs["Factor"]
        return c.ramp(nz.outputs["Factor"], stops, 0, 0, interp).outputs["Color"]
    return fn


tile("r_e2_brut", apercu("r_brut", ramp_apercu(None)))
tile("r_e2_contraste", apercu("r_contraste", ramp_apercu([(0.45, R.K), (0.55, R.W)])))
tile("r_e2_constant", apercu("r_constant", ramp_apercu([(0.0, R.K), (0.5, R.W)], 'CONSTANT')))
shot("r_e2_coque", ["E2_Exemple_Coque"], (0.25, -1, 0.9), (700, 600), margin=0.75)
give(["E2_Pratique_Planche"], R.planche("r_planche"))
shot("r_e2_planche", ["E2_Pratique_Planche"], (0.2, -1, 0.35), (700, 520), margin=0.72, rotate=40)

# ---------------------------------------------------------------------------- étape 3
HR = "E3_Pratique_Main_courante"
give([HR], R.patine("r_patine_partout", extremites=False))
shot("r_e3_partout", [HR], (0.0, -1, 0.35), (1000, 360), margin=0.62)
give([HR], R.patine("r_patine_ext"))
shot("r_e3_extremites", [HR], (0.0, -1, 0.35), (1000, 360), margin=0.62)

# ---------------------------------------------------------------------------- étape 4
give(["E4_Pratique_Boitier"], R.boitier("r_boitier"))
shot("r_e4_boitier", ["E4_Pratique_Boitier"], (0.55, -1, 0.75), (560, 560), margin=0.72)
CQ = "E4_Pratique_Coque"
for label, strength in (("lisse", 0.0), ("o15", 0.15), ("o30", 0.3)):
    c = R.Chaine("r_coque_" + label, "A3161A", 0, 0.4, coat=(1, 0.03))
    if strength:
        R.peau_orange(c, 0, 1, strength)
    give([CQ], c.m)
    shot("r_e4_coque_" + label, [CQ], (0.55, -1, 0.30), (560, 460), margin=0.32, rotate=20)

# ---------------------------------------------------------------------------- étape 5
SO = "E5_Pratique_Socle"
give([SO], apercu("r_bords_masque", lambda c: R.masque_bords(c, "Z", col=6)))
shot("r_e5_socle_masque", [SO], (0.45, -1, 0.75), (560, 440), margin=0.75)
give([SO], R.peinture_usee("r_bords_usure"))
shot("r_e5_socle_use", [SO], (0.45, -1, 0.75), (560, 440), margin=0.75)
shot("r_e5_coffret", ["E5_Exemple_Coffret", "E5_Exemple_Plinthe"], (0.6, -1, 0.55), (560, 440), margin=0.8)
give([SO], apercu("r_faux_positif", lambda c: R.masque_bords(c, "MAX", col=7)))
shot("r_e5_socle_faux", [SO], (0.45, -1, 0.75), (560, 440), margin=0.75)
MP = ["E5_Pratique_Marchepied"] + ["E5_Pratique_Marchepied_nervure_%d" % i for i in (1, 2, 3)]


def ao_brut(c):
    ao = c.node("ShaderNodeAmbientOcclusion", 0, 0)
    ao.inputs["Distance"].default_value = 0.020
    return ao.outputs["AO"]


def ao_rampe(c):
    ao = c.node("ShaderNodeAmbientOcclusion", 1, 0)
    ao.inputs["Distance"].default_value = 0.020
    return c.ramp(ao.outputs["AO"], [(0.85, R.W), (0.99, R.K)], 0, 0).outputs["Color"]


give(MP, apercu("r_ao_brut", ao_brut))
shot("r_e5_ao_brut", MP, (0.35, -1, 0.8), (520, 440), margin=0.75)
give(MP, apercu("r_ao_rampe", ao_rampe))
shot("r_e5_ao_rampe", MP, (0.35, -1, 0.8), (520, 440), margin=0.75)
give(MP, R.salete("r_salete"))
shot("r_e5_salete", MP, (0.35, -1, 0.8), (520, 440), margin=0.75)
RC = "E5_Pratique_Main_courante"
give([RC], apercu("r_rayures_masque", lambda c: R.masque_rayures(c, 3, 0)))
shot("r_e5_rayures_masque", [RC], (0.0, -1, 0.35), (1000, 330), margin=0.6)
give([RC], R.rayures("r_rayures"))
shot("r_e5_rayures", [RC], (0.0, -1, 0.35), (1000, 330), margin=0.6, rotate=60)
CO = "E5_Pratique_Console"
give([CO], R.depart("r_console", "0A0A0A", 0, 0.3, (1, 0.02)))
shot("r_e5_console_neuve", [CO], (0.3, -1, 0.42), (600, 400), margin=0.72, rotate=35)
give([CO], R.traces("r_traces"))
shot("r_e5_console_traces", [CO], (0.3, -1, 0.42), (600, 400), margin=0.72, rotate=35)

# ---------------------------------------------------------------------------- étape 6
shot("r_e6_dalle", ["E6_Exemple_Dalle"], (0.3, -1, 0.9), (480, 420), margin=0.75)
give(["E6_Pratique_Grille"], R.tole("r_tole"))
shot("r_e6_tole", ["E6_Pratique_Grille", "E6_Fond"], (0.3, -1, 1.1), (480, 420), margin=0.72)
give(["E6_Pratique_Accoudoir"], R.cuir("r_cuir"))
shot("r_e6_cuir", ["E6_Pratique_Accoudoir"], (0.45, -1, 0.6), (480, 420), margin=0.42)
give(["E6_Pratique_Assise"], R.tissu("r_tissu"))
shot("r_e6_tissu", ["E6_Pratique_Assise"], (0.45, -1, 0.75), (480, 420), margin=0.6)
give(["E6_Defi_Molette"], R.moletage("r_molette"))
shot("r_e6_molette", ["E6_Defi_Molette"], (0.4, -1, 0.35), (480, 420), margin=0.85)
give(["E6_Defi_Panneau"], R.carbone("r_carbone"))
shot("r_e6_carbone", ["E6_Defi_Panneau"], (0.3, -1, 0.9), (480, 420), margin=0.55)

# ---------------------------------------------------------------------------- vues d'ensemble
LAMPE = [o.name for o in bpy.data.collections["Lampe_defi"].all_objects if o.type in ('MESH', 'CURVE')]
LAMPE_C = [n + "_corrige" for n in LAMPE]
shot("r_lampe_neuve", LAMPE, (0.75, -0.95, 0.55), (560, 640), margin=0.95)
shot("r_lampe_atelier", LAMPE_C, (0.75, -0.95, 0.55), (560, 640), margin=0.95)
shot("r_lampe_socle", ["Socle_defi_corrige", "Articulation_bas_defi_corrige", "Grille_aeration_defi_corrige",
                       "Interrupteur_defi_corrige", "Interrupteur_crans_defi_corrige"], (0.45, -1, 0.6), (700, 520), margin=0.62)
CORR = [o.name for o in bpy.data.collections["Corrigé défi procédural"].all_objects if o.type in ('MESH', 'CURVE')]
shot("r_overview", CORR, (0.15, -1, 0.95), (1600, 1000), lens=50, margin=0.9)
print("RENDUS TERMINES")
