# Passe d'interface d'un fichier du chapitre 2 : agrandit la zone LISEZ-MOI (Text Editor, en bas
# du workspace Layout), replie dans l'Outliner les collections de corrigé, enregistre, puis quitte.
# Le redimensionnement des zones demande une vraie fenêtre : ce script ne marche pas en arrière-plan.
# Il ouvre une fenêtre Blender séparée, avec une configuration temporaire : le Blender du formateur
# n'est pas touché. Pendant la passe, tool/production/capture.lock signale la fenêtre aux autres sessions.
#
# Usage (PowerShell), depuis la racine du dépôt :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-exercices-ch2"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 _resources\exercices\PRC02_ch2_lampe_depart.blend --python tool\exercices_ch2\finish_ui.py
#
# Repris de tool/exercices_ch2_defi/finish_ui_defi.py (screen.area_move est refusé tant que la souris
# survole une région : le curseur est d'abord placé sur la bordure). L'Outliner : Python ne sait pas
# replier une ligne ; on simule un clic sur le triangle de chaque collection à replier, à la position
# lue dans la zone (ligne de 20 px à l'échelle 1, sous l'en-tête).

import os

import bpy

TARGET_H = 180      # hauteur de la zone LISEZ-MOI, en pixels
OUTLINER_H = 340     # hauteur de l'Outliner, en pixels : toutes les collections restent visibles
# collections dépliées à l'ouverture (les autres, dont les corrigés, restent repliées)
OPEN = {"PRC02_ch2_lampe_depart.blend": ["Lampe"], "PRC02_ch2_lampe_modele.blend": ["Lampe"],
        "PRC02_ch2_liseuse_depart.blend": ["Liseuse"]}
TOP = int(os.environ.get("UI_TOP", "1"))       # marge au-dessus de la première rangée
TRI_X = int(os.environ.get("UI_TRI_X", "30"))  # abscisse du triangle d'une collection de premier niveau
LOG = os.environ.get("UI_LOG")
SHOT = os.environ.get("UI_SHOT")
state = {"step": 0}


def log(*a):
    print(*a)
    if LOG:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(" ".join(str(x) for x in a) + "\n")


def areas():
    w = bpy.context.window_manager.windows[0]
    return w, w.screen, {a.type: a for a in w.screen.areas}


def click(w, x, y):
    w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='PRESS', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='RELEASE', x=x, y=y)


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
            o = A['OUTLINER']
            w.cursor_warp(o.x + o.width // 2, o.y - 1)
            return 0.6
        if step == 3:
            o = A['OUTLINER']
            delta = OUTLINER_H - o.height
            if abs(delta) > 2:
                with bpy.context.temp_override(window=w, screen=s):
                    bpy.ops.screen.area_move(x=o.x + o.width // 2, y=o.y - 1, delta=-delta)
            return 0.6
        if step == 4:
            # Outliner : tout replier, puis rouvrir le premier niveau (les collections, repliées)
            o = A['OUTLINER']
            reg = next(r for r in o.regions if r.type == 'WINDOW')
            w.cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
            with bpy.context.temp_override(window=w, screen=s, area=o, region=reg):
                for _ in range(4):
                    bpy.ops.outliner.show_one_level(open=False)
                bpy.ops.outliner.show_one_level(open=True)
            return 0.8
        if step == 5:
            # déplier les collections de travail (de bas en haut, pour que les rangées ne bougent pas) :
            # clic sur leur triangle ; les collections de corrigé restent repliées
            o = A['OUTLINER']
            reg = next(r for r in o.regions if r.type == 'WINDOW')
            ui = bpy.context.preferences.system.ui_scale
            row_h = 20 * ui
            names = [c.name for c in bpy.context.scene.collection.children]
            if os.environ.get("UI_NOCLICK"):
                return 0.6
            for idx in range(len(names), 0, -1):
                name = names[idx - 1]
                if name not in OPEN.get(os.path.basename(bpy.data.filepath), names):
                    continue
                y = reg.y + reg.height - int(row_h * (idx + 0.5)) - TOP
                x = reg.x + int(TRI_X * ui)
                log("UI_DEPLIE", name, "rangée", idx, "x", x, "y", y)
                click(w, x, y)
            return 0.8
        if step == 6:
            w.cursor_warp(t.x + t.width // 2, t.y + t.height // 2)
            for a in s.areas:
                if a.type == 'TEXT_EDITOR':
                    a.spaces.active.top = 0
            if SHOT:
                with bpy.context.temp_override(window=w, screen=s):
                    bpy.ops.screen.screenshot(filepath=SHOT, check_existing=False)
            log("UI_APRES", [(a.type, a.width, a.height) for a in s.areas])
            return 0.6
        if step == 7:
            if os.environ.get("UI_NOSAVE"):
                os._exit(0)
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
bpy.context.preferences.view.show_splash = False
bpy.app.timers.register(tick, first_interval=2.5)
bpy.app.timers.register(lambda: os._exit(2), first_interval=60.0)   # sécurité : quitte toujours
