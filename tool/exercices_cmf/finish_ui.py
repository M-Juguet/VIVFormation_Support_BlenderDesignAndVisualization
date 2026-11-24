# Passe d'interface d'un fichier de la planche CMF, dans une vraie fenêtre Blender : espace CMF avec
# l'Asset Browser (Current File) et le LISEZ-MOI en bas, l'Outliner réduit, l'onglet Material, la vue
# caméra cadrée ; les autres espaces retirés sauf Shading ; vignettes des actifs. Enregistre, puis quitte.
# Le Blender du formateur n'est pas touché : fenêtre séparée, configuration temporaire
# (BLENDER_USER_CONFIG), et tool/production/capture.lock posé pendant la passe (construire.ps1).
#
# Usage (PowerShell), depuis la racine du dépôt :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-exercices-cmf"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 <fichier.blend> --python tool\exercices_cmf\finish_ui.py
# Repris de tool/exercices_ch4/finish_ui.py.

import os

import bpy

BASE = os.path.basename(bpy.data.filepath)
LOG = os.environ.get("UI_LOG")
BOTTOM_H = 300       # hauteur de la bande du bas (Asset Browser et LISEZ-MOI)
OUTLINER_H = 230     # hauteur de l'Outliner


def log(*a):
    print(*a)
    if LOG:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(" ".join(str(x) for x in a) + "\n")


def win():
    w = bpy.context.window_manager.windows[0]
    return w, w.screen


def find(s, typ, ui=None):
    for a in s.areas:
        if a.type == typ and (ui is None or a.ui_type == ui):
            return a
    return None


def steps():
    # 0. les autres espaces de travail retirés, sauf Shading : workspace.delete retire l'espace actif
    w, s = win()
    keep = ("CMF", "Shading")
    for name in [ws.name for ws in bpy.data.workspaces if ws.name not in keep]:
        w, s = win()
        w.workspace = bpy.data.workspaces[name]
        yield 0.5
        w, s = win()
        with bpy.context.temp_override(window=w):
            bpy.ops.workspace.delete()
        yield 0.4
    w, s = win()
    w.workspace = bpy.data.workspaces["CMF"]
    yield 1.0
    w, s = win()
    log("ESPACES", [ws.name for ws in bpy.data.workspaces], "| actif", w.workspace.name)
    log("UI_AVANT", BASE, w.workspace.name, [(a.type, a.x, a.y, a.width, a.height) for a in s.areas])
    # 1. la Timeline devient l'Asset Browser, plus haute
    t = find(s, 'DOPESHEET_EDITOR')
    t.type = 'FILE_BROWSER'
    t.ui_type = 'ASSETS'
    yield 0.8
    w, s = win()
    t = find(s, 'FILE_BROWSER')
    delta = BOTTOM_H - t.height
    if abs(delta) > 2:
        with bpy.context.temp_override(window=w, screen=s):
            bpy.ops.screen.area_move(x=t.x + t.width // 2, y=t.y + t.height + 1, delta=delta)
    yield 0.6
    # 2. la bande du bas est coupée en deux : Asset Browser à gauche, LISEZ-MOI à droite
    w, s = win()
    t = find(s, 'FILE_BROWSER')
    before = {a.as_pointer() for a in s.areas}
    with bpy.context.temp_override(window=w, screen=s, area=t):
        bpy.ops.screen.area_split(direction='VERTICAL', factor=0.64,
                                  cursor=(t.x + int(t.width * 0.64), t.y + t.height // 2))
    yield 0.8
    w, s = win()
    bottom = sorted([a for a in s.areas if a.type == 'FILE_BROWSER'], key=lambda a: a.x)
    log("SPLIT", [(a.x, a.width) for a in bottom], "nouvelle" if any(a.as_pointer() not in before for a in s.areas) else "aucune")
    right = bottom[-1]
    right.type = 'TEXT_EDITOR'
    yield 0.6
    w, s = win()
    te = find(s, 'TEXT_EDITOR')
    sp = te.spaces.active
    sp.text = bpy.data.texts["LISEZ-MOI"]
    sp.show_word_wrap = True
    sp.show_line_numbers = False
    sp.show_syntax_highlight = False
    sp.top = 0
    ab = find(s, 'FILE_BROWSER')
    asp = ab.spaces.active
    try:
        asp.params.asset_library_reference = 'LOCAL'
    except Exception as e:
        log("BIBLIO_ERR", repr(e))
    asp.show_region_toolbar = True
    yield 0.8
    # 3. l'Outliner réduit, collections repliées
    w, s = win()
    o = find(s, 'OUTLINER')
    delta = o.height - OUTLINER_H
    if abs(delta) > 2:
        with bpy.context.temp_override(window=w, screen=s):
            bpy.ops.screen.area_move(x=o.x + o.width // 2, y=o.y, delta=delta)
    yield 0.6
    w, s = win()
    o = find(s, 'OUTLINER')
    reg = next(r for r in o.regions if r.type == 'WINDOW')
    with bpy.context.temp_override(window=w, screen=s, area=o, region=reg):
        for _ in range(4):
            bpy.ops.outliner.show_one_level(open=False)
        bpy.ops.outliner.show_one_level(open=True)
    # 4. un emplacement actif, l'onglet Material
    vl = bpy.context.view_layer
    for ob in vl.objects:
        ob.select_set(False)
    e5 = bpy.data.objects["Emplacement_5"]
    e5.select_set(True)
    vl.objects.active = e5
    yield 0.8
    w, s = win()
    p = find(s, 'PROPERTIES')
    try:
        p.spaces.active.context = 'MATERIAL'
    except Exception as e:
        log("ONGLET_ERR", repr(e))
    # 5. la vue caméra cadrée
    v = find(s, 'VIEW_3D')
    reg = next(r for r in v.regions if r.type == 'WINDOW')
    with bpy.context.temp_override(window=w, screen=s, area=v, region=reg):
        bpy.ops.view3d.view_center_camera()
    yield 0.8
    # 6. vignettes des actifs
    w, s = win()
    assets = [m for m in bpy.data.materials if m.asset_data]
    for m in assets:
        m.asset_generate_preview()
    yield 8.0 + 0.4 * len(assets)
    log("VIGNETTES", len(assets), "manquantes :",
        [m.name for m in assets if m.preview is None or m.preview.image_size[0] == 0])
    w, s = win()
    for scr in bpy.data.screens:
        for a in scr.areas:
            for sp in a.spaces:
                if sp.type == 'FILE_BROWSER' and sp.params is not None and hasattr(sp.params, "directory"):
                    sp.params.directory = b"/" * 1200
                    sp.params.directory = b"//"
    te = find(s, 'TEXT_EDITOR')
    if te:
        te.spaces.active.top = 0
    log("UI_APRES", BASE, [ws.name for ws in bpy.data.workspaces],
        [(a.type, a.ui_type, a.x, a.y, a.width, a.height) for a in s.areas],
        "| onglet", find(s, 'PROPERTIES').spaces.active.context)
    yield 0.6
    bpy.context.preferences.filepaths.save_version = 0
    with bpy.context.temp_override(window=w):
        bpy.ops.wm.save_mainfile(compress=True)
    log("UI_ENREGISTRE", BASE)
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
bpy.app.timers.register(lambda: os._exit(2), first_interval=180.0)   # sécurité : quitte toujours
