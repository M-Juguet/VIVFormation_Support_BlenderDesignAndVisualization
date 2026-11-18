# Passe d'interface d'un fichier d'exercice : agrandit la zone LISEZ-MOI (Text Editor, en bas
# du workspace Layout) à la hauteur des autres fichiers d'exercice, enregistre, capture la fenêtre
# puis quitte. Le redimensionnement des zones demande une vraie fenêtre : ce script ne marche pas
# en arrière-plan.
#
# Usage (PowerShell) :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-exercices"   # n'écrit rien dans la config du formateur
#   $env:UI_SHOT = "C:\chemin\capture.png"                          # facultatif
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup -p 0 0 1600 900 `
#       _resources\exercices\<fichier>.blend --python tool\exercices_initiation\finish_ui.py

import bpy, os

SHOT = os.environ.get("UI_SHOT")
TARGET_H = 151          # hauteur de la zone texte dans exercices_modelisation_primitives.blend
TARGET_OUTLINER_H = 326 # hauteur de l'Outliner dans le même fichier


def areas(win):
    return [(a.type, a.x, a.y, a.width, a.height) for a in win.screen.areas]


def resize():
    try:
        win = bpy.context.window_manager.windows[0]
        scr = win.screen
        txt = next(a for a in scr.areas if a.type == 'TEXT_EDITOR')
        v3d = next(a for a in scr.areas if a.type == 'VIEW_3D')
        print("UI_BEFORE", areas(win))
        delta = TARGET_H - txt.height
        if abs(delta) > 2:
            region = next(r for r in v3d.regions if r.type == 'WINDOW')
            with bpy.context.temp_override(window=win, screen=scr, area=v3d, region=region):
                bpy.ops.screen.area_move(x=txt.x + txt.width // 2, y=txt.y + txt.height + 1, delta=delta)
        # Outliner plus haut : il sert à masquer les kits, retrouver une pièce et lire les noms
        out = next(a for a in scr.areas if a.type == 'OUTLINER')
        delta = out.height - TARGET_OUTLINER_H
        if abs(delta) > 2:
            region = next(r for r in out.regions if r.type == 'WINDOW')
            with bpy.context.temp_override(window=win, screen=scr, area=out, region=region):
                bpy.ops.screen.area_move(x=out.x + out.width // 2, y=out.y - 1, delta=delta)
    except Exception as e:
        print("UI_ERR resize", repr(e))
    return None


def save_and_shoot():
    try:
        win = bpy.context.window_manager.windows[0]
        print("UI_AFTER", areas(win))
        for a in win.screen.areas:
            if a.type == 'TEXT_EDITOR':
                a.spaces.active.top = 0
        bpy.context.preferences.filepaths.save_version = 0   # pas de copie .blend1 à côté du fichier
        with bpy.context.temp_override(window=win):
            bpy.ops.wm.save_mainfile(compress=True)
        if SHOT:
            with bpy.context.temp_override(window=win, screen=win.screen):
                bpy.ops.screen.screenshot(filepath=SHOT, check_existing=False)
        print("UI_SAVED", bpy.data.filepath)
    except Exception as e:
        print("UI_ERR save", repr(e))
    return None


def quit_blender():
    try:
        bpy.ops.wm.quit_blender()
    except Exception:
        os._exit(0)
    return None


bpy.app.timers.register(resize, first_interval=2.0)
bpy.app.timers.register(save_and_shoot, first_interval=4.0)
bpy.app.timers.register(quit_blender, first_interval=6.5)
bpy.app.timers.register(lambda: os._exit(0), first_interval=30.0)   # sécurité : quitte toujours
