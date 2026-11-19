# Passe d'interface d'un fichier du chapitre 4, dans une vraie fenêtre Blender : hauteur de la zone
# LISEZ-MOI, collections repliées dans l'Outliner, vignettes des actifs de la lampe. Enregistre, puis
# quitte. Le Blender du formateur n'est pas touché : fenêtre séparée, configuration temporaire, et
# tool/production/capture.lock posé pendant la passe.
#
# Usage (PowerShell), depuis la racine du dépôt :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-exercices-ch4"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 <fichier.blend> --python tool\exercices_ch4\finish_ui.py
# Repris de tool/exercices_ch3/finish_ui.py.

import os

import bpy

TARGET_H = 180       # hauteur de la zone LISEZ-MOI, en pixels
BASE = os.path.basename(bpy.data.filepath)
LOG = os.environ.get("UI_LOG")


def log(*a):
    print(*a)
    if LOG:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(" ".join(str(x) for x in a) + "\n")


def areas():
    w = bpy.context.window_manager.windows[0]
    return w, w.screen, {a.type: a for a in w.screen.areas}


def steps():
    w, s, A = areas()
    t = A['TEXT_EDITOR']
    w.cursor_warp(t.x + t.width // 2, t.y + t.height + 1)
    yield 0.6
    w, s, A = areas()
    t = A['TEXT_EDITOR']
    delta = TARGET_H - t.height
    if abs(delta) > 2:
        with bpy.context.temp_override(window=w, screen=s):
            bpy.ops.screen.area_move(x=t.x + t.width // 2, y=t.y + t.height + 1, delta=delta)
    yield 0.6
    # Outliner : tout replier, puis ne montrer que les collections, repliées
    w, s, A = areas()
    o = A['OUTLINER']
    reg = next(r for r in o.regions if r.type == 'WINDOW')
    w.cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(window=w, screen=s, area=o, region=reg):
        for _ in range(4):
            bpy.ops.outliner.show_one_level(open=False)
        bpy.ops.outliner.show_one_level(open=True)
    yield 0.8
    # vignettes des matières de la lampe, rangées en actifs au chapitre 3
    assets = [m for m in bpy.data.materials if m.asset_data]
    for m in assets:
        m.asset_generate_preview()
    if assets:
        yield 6.0 + 0.4 * len(assets)
        log("VIGNETTES", len(assets), "manquantes :",
            [m.name for m in assets if m.preview is None or m.preview.image_size[0] == 0])
    w, s, A = areas()
    for a in s.areas:
        if a.type == 'TEXT_EDITOR':
            a.spaces.active.top = 0
    log("UI_APRES", BASE, [(a.type, a.width, a.height) for a in s.areas])
    yield 0.6
    bpy.context.preferences.filepaths.save_version = 0
    with bpy.context.temp_override(window=w):
        bpy.ops.wm.save_mainfile(compress=True)
    log("UI_ENREGISTRE", bpy.data.filepath)
    yield 0.6


_it = None


def tick():
    global _it
    try:
        if _it is None:
            _it = steps()
        return next(_it)
    except StopIteration:
        os._exit(0)
    except Exception as e:
        import traceback
        traceback.print_exc()
        log("UI_ERR", repr(e))
        os._exit(1)


bpy.context.preferences.use_preferences_save = False
bpy.context.preferences.view.show_splash = False
bpy.app.timers.register(tick, first_interval=3.0)
bpy.app.timers.register(lambda: os._exit(2), first_interval=120.0)   # sécurité : quitte toujours
