# Passe d'interface du fichier du défi : agrandit la zone LISEZ-MOI (Text Editor, en bas du
# workspace Layout), enregistre, puis quitte. Le redimensionnement des zones demande une vraie
# fenêtre : ce script ne marche pas en arrière-plan. Il ouvre une fenêtre Blender séparée, avec
# une configuration temporaire : la session du formateur n'est pas touchée.
#
# Usage (PowerShell), depuis la racine du dépôt, juste après build_defi_modelisation.py :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-exercices"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup -p 0 0 1600 900 `
#       _resources\exercices\PRC02_ch2_defi_modelisation.blend --python tool\exercices_ch2_defi\finish_ui_defi.py
#
# Différence avec tool/exercices_initiation/finish_ui.py : dans Blender 5.2.1, screen.area_move
# est refusé tant que la souris survole une région. On place d'abord le curseur sur la bordure.

import os

import bpy

TARGET_H = 180      # hauteur de la zone LISEZ-MOI, en pixels
LOG = os.environ.get("UI_LOG")
state = {"step": 0}


def log(*a):
    print(*a)
    if LOG:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(" ".join(str(x) for x in a) + "\n")


def areas():
    w = bpy.context.window_manager.windows[0]
    return w, w.screen, {a.type: a for a in w.screen.areas}


def tick():
    try:
        w, s, A = areas()
        t = A['TEXT_EDITOR']
        step = state["step"]
        state["step"] += 1
        if step == 0:
            log("UI_AVANT", [(a.type, a.width, a.height) for a in s.areas])
            w.cursor_warp(t.x + t.width // 2, t.y + t.height + 1)
            return 0.6
        if step == 1:
            delta = TARGET_H - t.height
            if abs(delta) > 2:
                with bpy.context.temp_override(window=w, screen=s):
                    bpy.ops.screen.area_move(x=t.x + t.width // 2, y=t.y + t.height + 1, delta=delta)
            return 0.6
        if step == 2:
            w.cursor_warp(t.x + t.width // 2, t.y + t.height // 2)
            for a in s.areas:
                if a.type == 'TEXT_EDITOR':
                    a.spaces.active.top = 0
            log("UI_APRES", [(a.type, a.width, a.height) for a in s.areas])
            bpy.context.preferences.filepaths.save_version = 0
            with bpy.context.temp_override(window=w):
                bpy.ops.wm.save_mainfile(compress=True)
            log("UI_ENREGISTRE", bpy.data.filepath)
            return 0.6
        os._exit(0)
    except Exception as e:
        log("UI_ERR", repr(e))
        os._exit(1)


bpy.context.preferences.use_preferences_save = False
bpy.app.timers.register(tick, first_interval=2.0)
bpy.app.timers.register(lambda: os._exit(2), first_interval=40.0)   # sécurité : quitte toujours
