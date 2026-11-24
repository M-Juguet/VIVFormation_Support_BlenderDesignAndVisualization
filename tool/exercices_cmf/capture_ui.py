# Capture de l'interface d'un fichier de la planche CMF, ouvert dans une fenêtre séparée (configuration
# temporaire), sans l'enregistrer : la vue caméra en Rendered a le temps de converger, puis la fenêtre
# est enregistrée en PNG (CAPTURE_OUT), et Blender quitte.
#
# Usage (PowerShell), depuis la racine du dépôt, avec tool/production/capture.lock posé :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-exercices-cmf"; $env:CAPTURE_OUT = "...\cmf_interface.png"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup -p 0 0 1600 960 <fichier.blend> `
#       --python tool\exercices_cmf\capture_ui.py

import os

import bpy

OUT = os.environ["CAPTURE_OUT"]
WAIT = float(os.environ.get("CAPTURE_WAIT", "25"))


def steps():
    if os.environ.get("CAPTURE_RENDERED") == "1":     # ce que voit le participant après le clic sur Rendered
        for a in bpy.context.window_manager.windows[0].screen.areas:
            if a.type == 'VIEW_3D':
                a.spaces.active.shading.type = 'RENDERED'
    yield WAIT
    w = bpy.context.window_manager.windows[0]
    with bpy.context.temp_override(window=w):
        bpy.ops.screen.screenshot(filepath=OUT)
    print("CAPTURE", OUT)
    yield 1.0


_it = None


def tick():
    global _it
    try:
        if _it is None:
            _it = steps()
        return next(_it)
    except StopIteration:
        os._exit(0)
    except Exception:
        import traceback
        traceback.print_exc()
        os._exit(1)


bpy.context.preferences.use_preferences_save = False
bpy.context.preferences.view.show_splash = False
bpy.app.timers.register(tick, first_interval=2.0)
bpy.app.timers.register(lambda: os._exit(2), first_interval=120.0)
