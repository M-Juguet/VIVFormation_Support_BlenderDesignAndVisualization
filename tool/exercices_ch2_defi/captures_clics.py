# Captures qui demandent de déplier une rubrique repliée de l'éditeur de propriétés : Python ne
# peut pas le faire, on simule donc des clics sur les en-têtes (option --enable-event-simulate).
# Fenêtre Blender séparée, configuration temporaire, rien n'est enregistré.
#
# Usage (PowerShell), depuis la racine du dépôt :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-captures-defi"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 _resources\exercices\PRC02_ch2_defi_modelisation.blend `
#       --python tool\exercices_ch2_defi\captures_clics.py -- <dossier_sortie>
#
# Les coordonnées des clics (pixels de la capture, origine en haut à gauche) ont été relevées sur
# les captures brutes de captures_brutes.py, avec la même disposition (colonne de droite élargie).

import os
import sys

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv = [a for a in sys.argv]
exec(open(os.path.join(HERE, "captures_brutes.py"), encoding="utf-8").read().split("# ---------------------------------------------------------------------------- les étapes")[0])

H = 960


def click(x, y_img):
    w = win()
    y = H - y_img
    w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='PRESS', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='RELEASE', x=x, y=y)


def c237():
    show_collections({"Etape_1_Subdivision"})
    select(["E1_Pratique_Crease"])
    props('MODIFIER')
    yield 1.0
    shot("c237_avant")
    click(1064, 495)          # en-tête « Advanced »
    yield 1.0
    shot("c237_advanced")


def c254():
    show_collections({"Etape_5_Booleens"})
    cut = O["E5_Coupe_Hublot"]
    select([cut.name])
    cut.display_type = 'WIRE'
    cut.hide_render = True
    props('OBJECT')
    yield 1.0
    shot("c254_avant")
    click(1092, 341)          # Transform : replier
    yield 0.8
    shot("c254_transform_replie")
    click(1100, 571)          # Viewport Display : déplier
    yield 0.8
    shot("c254_viewport_display")
    click(1100, 571)          # Viewport Display : replier
    yield 0.6
    click(1100, 538)          # Visibility : déplier
    yield 0.8
    shot("c255_visibility")
    cut.display_type = 'SOLID'
    cut.hide_render = False


def c260():
    show_collections({"Etape_6_Normales", "Corrigé étape 6"})
    k = O["E6_Pratique_Fuselage_corrige"]
    select([k.name])
    for m in k.modifiers:
        m.show_expanded = m.name == "DataTransfer"
    props('MODIFIER')
    yield 1.0
    shot("c260_avant")
    # en-têtes repliés relevés sur c260_avant, puis ajustés ci-dessous si besoin
    click(1064, FCD_Y)        # Face Corner Data : déplier
    yield 0.8
    shot("c260_face_corner")
    click(1064, FCD_Y)        # replier
    yield 0.6
    click(1076, TOPO_Y)       # Topology Mapping : déplier
    yield 0.8
    shot("c260_topology")


FCD_Y = int(os.environ.get("FCD_Y", "711"))
TOPO_Y = int(os.environ.get("TOPO_Y", "773"))
STEPS = [("237", c237), ("254", c254), ("260", c260)]


def runner():
    yield from layout_for_captures()
    for key, fn in STEPS:
        if ONLY and key not in ONLY:
            continue
        try:
            for d in fn():
                yield d
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("ECHEC", key, repr(e))
        yield 0.5


_it = None


def tick():
    global _it
    try:
        if _it is None:
            _it = runner()
        return next(_it)
    except StopIteration:
        os._exit(0)
    except Exception:
        import traceback
        traceback.print_exc()
        os._exit(1)


bpy.app.timers.register(tick, first_interval=3.0)
bpy.app.timers.register(lambda: os._exit(2), first_interval=300.0)
