# Rendus EEVEE (et Cycles pour le comparatif) du fichier de secours du chapitre 4, depuis une copie de
# travail en mémoire : le fichier n'est jamais enregistré.
#   controle   : l'état d'ouverture (Raytracing décoché), puis Raytracing coché, caméra CAM_banc_essai ;
#   hdri       : Monde_Interieur, rotation du Mapping de 0 à 315°, pour choisir celle du corrigé ;
#   corrige    : les images du corrigé (héros, détail, situation, situation allumée, gamme, profil) ;
#   comparatif : EEVEE 64 échantillons et Cycles 128 échantillons débruité, en 1280 x 720, avec les temps.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup _resources\exercices\PRC02_ch4_lampe_en_studio.blend ^
#       --python tool\exercices_ch4\rendus.py -- <dossier_sortie> <mode> [pourcentage]

import math
import os
import sys
import time

import bpy

args = sys.argv[sys.argv.index("--") + 1:]
OUT = args[0]
MODE = args[1]
PCT = int(args[2]) if len(args) > 2 else 100
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene
O = bpy.data.objects
W = bpy.data.worlds
ROT_INTERIEUR = int(os.environ.get("ROT_INTERIEUR", "135"))


def show(**cols):
    """show(Studio=True, Nuancier=False, ...) : visibilité au rendu des collections nommées."""
    for name, vis in cols.items():
        bpy.data.collections[name].hide_render = not vis


def corrige_settings():
    sc.eevee.use_raytracing = True
    sc.eevee.taa_render_samples = 128
    sc.view_settings.view_transform = 'Khronos PBR Neutral'


def render(name, cam, res=(1920, 1080), world=None):
    sc.camera = O[cam]
    if world:
        sc.world = W[world]
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = PCT
    sc.render.filepath = os.path.join(OUT, name + ".png")
    t = time.time()
    bpy.ops.render.render(write_still=True)
    dt = time.time() - t
    print("RENDU", name, "%.1f s" % dt)
    return dt


def set_rot(world, deg):
    mp = next(n for n in W[world].node_tree.nodes if n.type == 'MAPPING')
    mp.inputs["Rotation"].default_value[2] = math.radians(deg)


if MODE == "controle":
    render("ctrl_ouverture", "CAM_banc_essai")
    sc.eevee.use_raytracing = True
    render("ctrl_raytracing", "CAM_banc_essai")
    show(**{"Lampe_coloris_B": True, "Nuancier": False})
    render("ctrl_coloris_B", "CAM_gamme_corrige")

elif MODE == "hdri":
    corrige_settings()
    for d in range(0, 360, 45):
        set_rot("Monde_Interieur", d)
        render("hdri_interieur_%03d" % d, "CAM_banc_essai", world="Monde_Interieur")
    set_rot("Monde_Interieur", 0)
    render("hdri_exterieur", "CAM_banc_essai", world="Monde_Exterieur")

elif MODE == "corrige":
    corrige_settings()
    only = set(args[3:])
    show(**{"Corrigé éclairage": True, "Nuancier": False})

    def want(k):
        return not only or k in only

    if want("heros"):
        render("PRC02_ch4_corrige_heros", "CAM_heros_corrige", world="Monde_Neutre")
    if want("detail"):
        render("PRC02_ch4_corrige_detail", "CAM_detail_corrige", (1080, 1080), world="Monde_Neutre")
    if want("profil"):
        render("corrige_profil_ortho", "CAM_profil_ortho_corrige", world="Monde_Neutre")
    if want("gamme"):
        show(**{"Lampe_coloris_B": True})
        render("corrige_gamme", "CAM_gamme_corrige", world="Monde_Neutre")
        show(**{"Lampe_coloris_B": False})
    if want("situation"):
        set_rot("Monde_Interieur", ROT_INTERIEUR)
        show(**{"Corrigé éclairage": False, "Studio": False, "Mise_en_situation": True})
        render("PRC02_ch4_corrige_situation", "CAM_situation_corrige", world="Monde_Interieur")
    if want("allumee"):
        show(**{"Corrigé éclairage": False, "Studio": False, "Mise_en_situation": True, "Corrigé paliers": True})
        amp = O["Ampoule"]
        amp.data.materials.clear()
        amp.data.materials.append(bpy.data.materials["Ampoule_allumee"])
        # la pièce en fin de journée : l'HDRI d'intérieur, très baissée, en mémoire seulement
        set_rot("Monde_Interieur", ROT_INTERIEUR)
        bg = next(n for n in W["Monde_Interieur"].node_tree.nodes if n.type == 'BACKGROUND')
        bg.inputs["Strength"].default_value = 0.12
        render("PRC02_ch4_corrige_situation_allumee", "CAM_situation_corrige", world="Monde_Interieur")

elif MODE == "comparatif":
    sc.eevee.use_raytracing = True
    sc.view_settings.view_transform = 'AgX'
    sc.world = W["Monde_Studio"]
    t_eevee = render("comparatif_eevee", "CAM_banc_essai", (1280, 720))
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = 128
    sc.cycles.use_denoising = True
    try:
        prefs = bpy.context.preferences.addons["cycles"].preferences
        prefs.compute_device_type = 'OPTIX'
        prefs.get_devices()
        for d in prefs.devices:
            d.use = True
        sc.cycles.device = 'GPU'
    except Exception as e:
        print("GPU", repr(e))
    t_cycles = render("comparatif_cycles", "CAM_banc_essai", (1280, 720))
    with open(os.path.join(OUT, "comparatif_temps.txt"), "w", encoding="utf-8") as f:
        f.write("eevee %.1f\ncycles %.1f\n" % (t_eevee, t_cycles))
