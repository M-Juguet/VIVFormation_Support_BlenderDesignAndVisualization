# Passe d'interface d'un fichier du chapitre 3, dans une vraie fenêtre Blender : hauteur de la zone
# LISEZ-MOI, collections de corrigé repliées dans l'Outliner, vignettes des actifs (la vue 3D en arrière-
# plan ne les calcule pas), espace Shading pour la fiche C. Enregistre, puis quitte.
# Le Blender du formateur n'est pas touché : fenêtre séparée, configuration temporaire, et
# tool/production/capture.lock posé pendant la passe.
#
# Usage (PowerShell), depuis la racine du dépôt :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-exercices-ch3"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 <fichier.blend> --python tool\exercices_ch3\finish_ui.py
# Repris de tool/exercices_ch2/finish_ui.py.

import os

import bpy

TARGET_H = 180       # hauteur de la zone LISEZ-MOI, en pixels
BASE = os.path.basename(bpy.data.filepath)
SHADING = BASE in ("PRC02_ch3_finitions_triplanaires.blend", "PRC02_ch3_defi_procedural.blend")
OPEN = {"PRC02_ch3_lampe_a_habiller.blend": ["Lampe"]}
TRI_X = 30
LOG = os.environ.get("UI_LOG")
SHOT = os.environ.get("UI_SHOT")


def log(*a):
    print(*a)
    if LOG:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(" ".join(str(x) for x in a) + "\n")


def win():
    return bpy.context.window_manager.windows[0]


def areas():
    w = win()
    return w, w.screen, {a.type: a for a in w.screen.areas}


def click(w, x, y):
    w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='PRESS', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='RELEASE', x=x, y=y)


def steps():
    w = win()
    if SHADING:
        w.workspace = bpy.data.workspaces["Shading"]
        yield 2.0
        w, s, A = areas()
        txt = bpy.data.texts["LISEZ-MOI"]
        if 'TEXT_EDITOR' not in A:
            # le navigateur de fichiers enregistrerait le chemin absolu du dossier : il devient le LISEZ-MOI
            fb = A['FILE_BROWSER']
            for space in fb.spaces:
                if space.type == 'FILE_BROWSER' and space.params is not None:
                    space.params.directory = b"/" * 1200      # écrase tout le tampon, puis chemin relatif
                    space.params.directory = b"//"
                    space.params.filename = ""
            yield 0.5
            fb.type = 'TEXT_EDITOR'
            yield 0.8
            # l'ancien espace, inactif, reste dans la zone : il ne se rafraîchit plus, on y remet //
            for space in fb.spaces:
                if space.type == 'FILE_BROWSER' and space.params is not None:
                    space.params.directory = b"/" * 1200
                    space.params.directory = b"//"
            sp = fb.spaces.active
            sp.text = txt
            sp.show_word_wrap = True
            sp.show_line_numbers = False
            sp.show_syntax_highlight = False
            sp.top = 0
        yield 0.8
        w, s, A = areas()
        ne = A['NODE_EDITOR']
        reg = next(r for r in ne.regions if r.type == 'WINDOW')
        w.cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
        with bpy.context.temp_override(window=w, screen=s, area=ne, region=reg):
            bpy.ops.node.view_all()
        v = A['VIEW_3D']
        v.spaces.active.shading.type = 'MATERIAL'
        yield 1.0
    else:
        # la zone LISEZ-MOI de l'espace Layout, à TARGET_H pixels
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
        # Outliner : tout replier, puis rouvrir le premier niveau ; déplier les collections de travail
        w, s, A = areas()
        o = A['OUTLINER']
        reg = next(r for r in o.regions if r.type == 'WINDOW')
        w.cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
        with bpy.context.temp_override(window=w, screen=s, area=o, region=reg):
            for _ in range(4):
                bpy.ops.outliner.show_one_level(open=False)
            bpy.ops.outliner.show_one_level(open=True)
        yield 0.8
        ui = bpy.context.preferences.system.ui_scale
        names = [c.name for c in bpy.context.scene.collection.children]
        for idx in range(len(names), 0, -1):
            if names[idx - 1] not in OPEN.get(BASE, names):
                continue
            y = reg.y + reg.height - int(20 * ui * (idx + 0.5)) - 1
            click(w, reg.x + int(TRI_X * ui), y)
        yield 0.8
    # vignettes des actifs
    assets = [m for m in bpy.data.materials if m.asset_data]
    for m in assets:
        m.asset_generate_preview()
    if assets:
        yield 6.0 + 0.4 * len(assets)
        missing = [m.name for m in assets if m.preview is None or m.preview.image_size[0] == 0]
        log("VIGNETTES", len(assets), "manquantes :", missing)
        if missing:
            for m in assets:
                if m.name in missing:
                    m.asset_generate_preview()
            yield 8.0
            log("VIGNETTES, 2e passe, manquantes :", [m.name for m in assets if m.preview is None or m.preview.image_size[0] == 0])
    w, s, A = areas()
    for a in s.areas:
        if a.type == 'TEXT_EDITOR':
            a.spaces.active.top = 0
    if SHOT:
        with bpy.context.temp_override(window=w, screen=s):
            bpy.ops.screen.screenshot(filepath=SHOT, check_existing=False)
    log("UI_APRES", BASE, [(a.type, a.width, a.height) for a in s.areas])
    yield 0.6
    if os.environ.get("UI_NOSAVE"):
        os._exit(0)
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
