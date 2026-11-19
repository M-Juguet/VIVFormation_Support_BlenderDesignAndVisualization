# Captures brutes (fenêtre entière) des figures d'interface du chapitre 4.
# Ouvre une VRAIE fenêtre Blender, séparée de celle du formateur, avec une configuration temporaire.
# Rien n'est enregistré : le fichier de secours est ouvert, puis modifié en mémoire seulement
# (collection Eclairage_studio, caméras de l'apprenant), pour reproduire chaque étape du chapitre.
#
# Usage (PowerShell), depuis la racine du dépôt, verrou tool\production\capture.lock posé :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\exercices_ch4\lancer_captures.ps1 <dossier_sortie> [-Recon] [-Etapes 403,404]
# Les clics simulés utilisent des coordonnées relevées sur une passe de repérage (-Recon) : variables
# d'environnement, voir en bas. Repris de tool/exercices_ch3/captures_brutes.py.

import json
import math
import os
import sys

import bpy
from bpy_extras.view3d_utils import location_3d_to_region_2d
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = args[0] if args else os.path.join(os.environ.get("TEMP", "."), "captures_ch4")
ONLY = set(args[1:])
os.makedirs(OUT, exist_ok=True)
H = 960
A2 = os.path.join(HERE, "_construction", "PRC02_ch3_lampe_habillage", "PRC02_ch3_lampe_habillage.blend")
RECON = bool(os.environ.get("RECON"))

prefs = bpy.context.preferences
prefs.use_preferences_save = False
prefs.view.ui_scale = 1.25
prefs.view.show_tooltips = False
prefs.view.show_splash = False
prefs.view.smooth_view = 0
prefs.view.render_display_type = 'SCREEN'        # la fenêtre de rendu dans la fenêtre principale
prefs.view.filebrowser_display_type = 'SCREEN'   # la fenêtre de fichiers aussi : une seule capture
O = bpy.data.objects
sc = bpy.context.scene
T = Vector((0.11, 0.0, 0.22))


def env_xy(name, default):
    return tuple(int(v) for v in os.environ.get(name, default).split(","))


# ---------------------------------------------------------------------------- accès à l'interface
def win():
    return bpy.context.window_manager.windows[0]


def area(kind):
    return next(a for a in win().screen.areas if a.type == kind)


def region(a, kind='WINDOW'):
    return next(r for r in a.regions if r.type == kind)


def ov(a=None, kind='WINDOW'):
    w = win()
    d = dict(window=w, screen=w.screen)
    if a is not None:
        d.update(area=a, region=region(a, kind))
    return d


def v3d():
    return area('VIEW_3D').spaces.active


def select(names, active=None):
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    for n in names:
        O[n].select_set(True)
    vl.objects.active = O[active or names[-1]] if names else None


def deselect_all():
    select([])


def look(kind='MATERIAL', overlays=False):
    sp = v3d()
    sp.shading.type = kind
    if kind == 'MATERIAL':
        sp.shading.studio_light = 'studio.exr'
        sp.shading.use_scene_lights = False
        sp.shading.use_scene_world = False
    sp.overlay.show_overlays = overlays
    sp.overlay.show_floor = False
    sp.overlay.show_axis_x = False
    sp.overlay.show_axis_y = False
    sp.overlay.show_cursor = False
    sp.overlay.show_text = False
    sp.overlay.show_stats = False
    sp.overlay.show_object_origins = False
    sp.show_gizmo_navigate = False
    sp.clip_start = 0.001


def camera_view(cam_name):
    sc.camera = O[cam_name]
    r3d = v3d().region_3d
    r3d.view_perspective = 'CAMERA'
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.view3d.view_center_camera()


def camera_frame_box(cam_name):
    """Le cadre de la caméra, en pixels de la capture (origine en haut à gauche)."""
    a = area('VIEW_3D')
    r = region(a)
    cam = O[cam_name]
    pts = [cam.matrix_world @ v for v in cam.data.view_frame(scene=sc)]
    xs, ys = [], []
    for p in pts:
        q = location_3d_to_region_2d(r, a.spaces.active.region_3d, p)
        xs.append(r.x + q.x)
        ys.append(H - (r.y + q.y))
    return [int(min(xs)) + 2, int(min(ys)) + 2, int(max(xs)) - 2, int(max(ys)) - 2]


def view_from(eye, target, dist_k=1.0, persp='PERSP'):
    r3d = v3d().region_3d
    r3d.view_perspective = persp
    r3d.view_location = Vector(target)
    r3d.view_rotation = (Vector(target) - Vector(eye)).to_track_quat('-Z', 'Y')
    r3d.view_distance = (Vector(target) - Vector(eye)).length * dist_k


def props(context):
    a = area('PROPERTIES')
    a.spaces.active.context = context
    return a


def warp(a_kind, at):
    a = area(a_kind)
    x = int(a.x + a.width * at[0])
    y = int(a.y + a.height * at[1])
    win().cursor_warp(x, y)
    return a, x, y


def call_menu(name, a_kind='VIEW_3D', at=(0.35, 0.75)):
    a, _x, _y = warp(a_kind, at)
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.call_menu('INVOKE_DEFAULT', name=name)


def call_pie(name, a_kind='VIEW_3D', at=(0.5, 0.5)):
    a, _x, _y = warp(a_kind, at)
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.call_menu_pie('INVOKE_DEFAULT', name=name)


def call_panel(name, a_kind='VIEW_3D', at=(0.9, 0.97)):
    a, _x, _y = warp(a_kind, at)
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.call_panel('INVOKE_DEFAULT', name=name, keep_open=True)


def close_popups():
    w = win()
    for _ in range(2):
        w.event_simulate(type='ESC', value='PRESS')
        w.event_simulate(type='ESC', value='RELEASE')


def click(x, y_img, ctrl=False):
    w = win()
    y = H - y_img
    w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='PRESS', x=x, y=y, ctrl=ctrl)
    w.event_simulate(type='LEFTMOUSE', value='RELEASE', x=x, y=y, ctrl=ctrl)


def hover(x, y_img):
    win().event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=H - y_img)


def wheel(a_kind, n, down=True):
    _a, x, y = warp(a_kind, (0.5, 0.5))
    w = win()
    for _ in range(n):
        w.event_simulate(type='WHEELDOWNMOUSE' if down else 'WHEELUPMOUSE', value='PRESS', x=x, y=y)


def rect(a, kind='WINDOW'):
    r = region(a, kind)
    return [r.x, H - (r.y + r.height), r.x + r.width, H - r.y]


def shot(name, extra=None):
    path = os.path.join(OUT, name + ".png")
    s = win().screen
    info = {}
    for a in s.areas:
        for kind in ('WINDOW', 'HEADER', 'UI', 'TOOLS'):
            try:
                info[a.type + ("" if kind == 'WINDOW' else "_" + kind)] = rect(a, kind)
            except StopIteration:
                pass
        info[a.type + "_AREA"] = [a.x, H - (a.y + a.height), a.x + a.width, H - a.y]
    if extra:
        info.update(extra)
    with bpy.context.temp_override(window=win(), screen=s):
        bpy.ops.screen.screenshot(filepath=path, check_existing=False)
    with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(info, f)
    print("CAPTURE", path, flush=True)


def move_border(a_kind, side, delta):
    w = win()
    for off in (1, 2, 0, 3, -1):
        a = area(a_kind)
        if side == 'top':
            x, y = a.x + a.width // 2, a.y + a.height + off
        else:
            x, y = a.x - off, a.y + a.height // 2
        w.cursor_warp(x, y)
        w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
        yield 0.4
        try:
            with bpy.context.temp_override(window=w, screen=w.screen):
                bpy.ops.screen.area_move(x=x, y=y, delta=delta)
            yield 0.4
            return
        except RuntimeError as e:
            print("BORDURE", a_kind, side, off, repr(e))
    raise RuntimeError("bordure introuvable : " + a_kind)


def layout_for_captures():
    """Colonne de droite élargie, zone LISEZ-MOI réduite, Outliner à 260 px."""
    yield from move_border('PROPERTIES', 'left', -300)
    t = area('TEXT_EDITOR')
    yield from move_border('TEXT_EDITOR', 'top', 40 - t.height)
    o = area('OUTLINER')
    w = win()
    w.cursor_warp(o.x + o.width // 2, o.y - 1)
    yield 0.4
    with bpy.context.temp_override(window=w, screen=w.screen):
        bpy.ops.screen.area_move(x=o.x + o.width // 2, y=o.y - 1, delta=-(260 - o.height))
    yield 0.4


def set_workspace(name):
    win().workspace = bpy.data.workspaces[name]
    yield 1.5


def scroll_props_top():
    wheel('PROPERTIES', 40, down=False)


# ---------------------------------------------------------------------------- état « apprenant »
def copy_object(src, name, col):
    o = O[src].copy()
    o.data = O[src].data.copy()
    o.data.name = name
    o.name = name
    col.objects.link(o)
    return o


def learner_state():
    """Les objets que l'apprenant crée pendant la séance, copiés du corrigé, sous ses noms à lui."""
    root = sc.collection
    ecl = bpy.data.collections.new("Eclairage_studio")
    root.children.link(ecl)
    for n in ("Key", "Fill", "Rim"):
        copy_object(n + "_corrige", n, ecl)
    cams = bpy.data.collections.new("Cameras")
    root.children.link(cams)
    for n in ("CAM_heros", "CAM_detail", "CAM_situation"):
        copy_object(n + "_corrige", n, cams)
    mp = O["Mise_au_point_corrige"].copy()
    mp.name = "Mise_au_point"
    cams.objects.link(mp)
    O["CAM_detail"].data.dof.focus_object = mp
    sp = copy_object("Spot_lampe_corrige", "Spot_lampe", cams)
    sp.hide_set(True)
    sp.hide_render = True
    lc = bpy.context.view_layer.layer_collection.children
    for n in ("Eclairage_studio", "Cameras"):
        lc[n].hide_viewport = False
    sc.eevee.use_raytracing = True
    sc.eevee.taa_render_samples = 128
    sc.view_settings.view_transform = 'Khronos PBR Neutral'
    bpy.data.worlds["Monde_Neutre"].use_fake_user = True
    sc.world = bpy.data.worlds["Monde_Neutre"]
    sc.camera = O["CAM_banc_essai"]
    mpi = next(n for n in bpy.data.worlds["Monde_Interieur"].node_tree.nodes if n.type == 'MAPPING')
    mpi.inputs["Rotation"].default_value[2] = math.radians(135)


# ---------------------------------------------------------------------------- passe de repérage
def recon():
    for ctx in ('RENDER', 'WORLD', 'OUTPUT'):
        props(ctx)
        scroll_props_top()
        yield 1.2
        shot("r_" + ctx.lower())
    select(["Key"])
    yield 0.8
    props('DATA')
    yield 1.2
    shot("r_light_area")
    O["Spot_lampe"].hide_set(False)
    select(["Spot_lampe"])
    yield 0.8
    props('DATA')
    yield 1.2
    shot("r_light_spot")
    O["Spot_lampe"].hide_set(True)
    select(["CAM_heros"])
    yield 0.8
    props('DATA')
    yield 1.2
    shot("r_camera")
    v3d().show_region_ui = True
    yield 1.0
    shot("r_sidebar")
    v3d().show_region_ui = False


# coordonnées relevées sur la passe de repérage (image 1600 x 960, origine en haut à gauche).
# Les en-têtes de rubrique de l'éditeur de propriétés sont espacés de 33 px quand elles sont repliées ;
# la première est à y = 436.
HX = 1300                                           # abscisse d'un en-tête de rubrique (zone vide)
Y0, DY = 436, 33
ENGINE = env_xy("ENGINE_XY", "1430,395")           # champ Render Engine, onglet Render
VIEW_FIELD = env_xy("VIEW_XY", "1424,701")         # champ View, Color Management ouverte, après défilement
WORLD_BROWSE = env_xy("WORLD_BROWSE_XY", "1077,395")
PRESETS = env_xy("PRESETS_XY", "1543,391")         # bouton des préréglages de la rubrique Format
COMPO = env_xy("COMPO_XY", "1170,819")             # sous-rubrique Composition Guides
COLOR_INPUT = env_xy("COLOR_INPUT_XY", "1083,530")  # flèche qui déplie l'entrée Color du monde
MAPPING_INPUT = env_xy("MAPPING_INPUT_XY", "1083,747")  # puis celle de l'entrée Vector (Mapping)
SAVE_CM = env_xy("SAVE_CM_XY", "1405,283")          # rubrique Color Management de la fenêtre Save As
SIDEBAR_VIEW = env_xy("SIDEBAR_VIEW_XY", "997,240")
RENDER_ORDER = ["Sampling", "Light Paths", "Raytracing", "Volumes", "Curves", "Simplify", "Depth of Field",
                "Motion Blur", "Film", "Performance", "Grease Pencil", "Freestyle", "Color Management"]
CAMERA_ORDER = ["Lens", "Depth of Field", "Camera", "Safe Areas", "Background Images", "Viewport Display"]


def only_panel(order, name):
    """Ne laisse ouverte que la rubrique name : Ctrl + clic sur la première (seule ouverte, état connu),
    clic pour la replier (toutes repliées), puis Ctrl + clic sur la rubrique voulue."""
    click(HX, Y0, ctrl=True)
    yield 0.6
    click(HX, Y0)
    yield 0.6
    if name is not None:
        click(HX, Y0 + DY * order.index(name), ctrl=True)
        yield 1.0


def cancel_file_browser():
    """Ferme la fenêtre de fichiers ouverte dans la fenêtre principale (Cancel)."""
    fb = next((x for x in win().screen.areas if x.type == 'FILE_BROWSER'), None)
    if fb is not None:
        reg = region(fb)
        win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
        with bpy.context.temp_override(**ov(fb)):
            bpy.ops.file.cancel()
    yield 1.5
    assert any(x.type in ('VIEW_3D', 'IMAGE_EDITOR') for x in win().screen.areas), "fenêtre de fichiers restée ouverte"


# ---------------------------------------------------------------------------- section 1
def f402():
    """File > Append, dans le dossier Collection de la lampe habillée du chapitre 3."""
    a = area('VIEW_3D')
    win().cursor_warp(a.x + a.width // 2, a.y + a.height // 2)
    d = os.path.join(A2, "Collection") + os.sep
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.append('INVOKE_DEFAULT', filepath=d, directory=d, filename="")
    yield 2.5
    fb = area('FILE_BROWSER')
    sp = fb.spaces.active
    sp.show_region_toolbar = False
    if sp.params is not None:
        sp.params.display_type = 'LIST_VERTICAL'
        sp.params.filename = "Lampe"
    yield 1.5
    shot("402_append_collection")
    yield from cancel_file_browser()


def f403():
    look('MATERIAL')
    view_from((0.55, -2.30, 0.55), (0.22, -0.03, 0.18), 0.55)
    yield 3.0
    shot("403_pie_avant")
    call_pie("VIEW3D_MT_shading_pie")
    yield 1.5
    shot("403_pie")
    close_popups()
    yield 0.8


def f404():
    look('MATERIAL')
    sc.world = bpy.data.worlds["Monde_Studio"]
    camera_view("CAM_banc_essai")
    yield 4.0
    shot("404_mp_off", extra={"CAM_BOX": camera_frame_box("CAM_banc_essai")})
    v3d().shading.use_scene_world = True
    yield 4.0
    shot("404_mp_on", extra={"CAM_BOX": camera_frame_box("CAM_banc_essai")})
    v3d().shading.use_scene_world = False
    sc.world = bpy.data.worlds["Monde_Neutre"]
    v3d().region_3d.view_perspective = 'PERSP'


def f405():
    look('RENDERED')
    sc.world = bpy.data.worlds["Monde_Studio"]
    view_from((0.55, -2.30, 0.55), (0.22, -0.03, 0.18), 0.55)
    yield 4.0
    shot("405_popover_avant")
    call_panel("VIEW3D_PT_shading")
    yield 2.0
    shot("405_popover")
    close_popups()
    yield 0.8
    look('MATERIAL')
    sc.world = bpy.data.worlds["Monde_Neutre"]


def f406():
    """La vue Material Preview du banc d'essai, pour l'image comparative des moteurs."""
    look('MATERIAL')
    sc.world = bpy.data.worlds["Monde_Studio"]
    camera_view("CAM_banc_essai")
    yield 4.0
    shot("406_mp_banc", extra={"CAM_BOX": camera_frame_box("CAM_banc_essai")})
    sc.world = bpy.data.worlds["Monde_Neutre"]
    v3d().region_3d.view_perspective = 'PERSP'


def f407():
    props('RENDER')
    scroll_props_top()
    yield 1.0
    shot("407_engine_avant")
    click(*ENGINE)
    yield 1.2
    shot("407_engine")
    close_popups()
    yield 0.6


def f408():
    """F12 : la fenêtre de rendu, affichée dans la fenêtre principale."""
    sc.world = bpy.data.worlds["Monde_Studio"]
    sc.camera = O["CAM_banc_essai"]
    sc.render.resolution_percentage = 50
    sc.render.use_stamp = False
    a = area('VIEW_3D')
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.render.render('INVOKE_DEFAULT')
    yield 8.0
    shot("408_fenetre_rendu")
    ie = next((x for x in win().screen.areas if x.type == 'IMAGE_EDITOR'), None)
    if ie is not None:
        with bpy.context.temp_override(**ov(ie)):
            bpy.ops.screen.back_to_previous()
    yield 1.5
    sc.render.resolution_percentage = 100
    sc.world = bpy.data.worlds["Monde_Neutre"]


def props_panel(name, panel, ctx='RENDER', order=RENDER_ORDER):
    yield 0.8
    props(ctx)
    scroll_props_top()
    yield 1.0
    yield from only_panel(order, panel)
    yield 0.6
    shot(name)


def f409():
    yield from props_panel("409_raytracing", "Raytracing")


def f411():
    yield from props_panel("411_sampling", "Sampling")


def f412():
    yield from props_panel("412_color_avant", "Color Management")
    wheel('PROPERTIES', 12)
    yield 1.0
    shot("412_color_bas")
    click(*VIEW_FIELD)
    yield 1.2
    shot("412_color_menu")
    close_popups()
    yield 0.6


def f438():
    sc.render.film_transparent = True
    yield from props_panel("438_film", "Film")
    sc.render.film_transparent = False


# ---------------------------------------------------------------------------- section 2
def f415():
    sc.world = bpy.data.worlds["Monde_Interieur"]
    props('WORLD')
    scroll_props_top()
    yield 1.0
    shot("415_world_avant")
    click(*WORLD_BROWSE)
    yield 1.5
    shot("415_world_browse")
    close_popups()
    yield 0.6


def f416():
    sc.world = bpy.data.worlds["Monde_Interieur"]
    props('WORLD')
    scroll_props_top()
    yield 1.5
    shot("416_world_surface")
    # les entrées dépliées de la rubrique Surface : leur état est porté par les prises des nœuds
    nt = bpy.data.worlds["Monde_Interieur"].node_tree
    bg = next(n for n in nt.nodes if n.type == 'BACKGROUND')
    env = next(n for n in nt.nodes if n.type == 'TEX_ENVIRONMENT')
    bg.inputs["Color"].show_expanded = True
    env.inputs["Vector"].show_expanded = True
    area('PROPERTIES').tag_redraw()
    yield 1.5
    wheel('PROPERTIES', 6)
    yield 1.2
    shot("416_world_surface_ouvert")


def f417():
    sc.world = bpy.data.worlds["Monde_Interieur"]
    yield from set_workspace("Shading")
    ne = next(a for a in win().screen.areas if a.type == 'NODE_EDITOR')
    sp = ne.spaces.active
    sp.shader_type = 'WORLD'
    yield 1.5
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.screen.screen_full_area()
    yield 1.5
    ne = next(a for a in win().screen.areas if a.type == 'NODE_EDITOR')
    reg = region(ne)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.view_all()
    yield 1.2
    shot("417_world_nodes")
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.screen.back_to_previous()
    yield 1.2
    sp.shader_type = 'OBJECT'
    yield from set_workspace("Layout")


def f418():
    look('MATERIAL')
    view_from((0.55, -2.30, 0.55), (0.22, -0.03, 0.18), 0.55)
    yield 2.0
    shot("418_light_avant")
    call_menu("VIEW3D_MT_light_add", at=(0.3, 0.7))
    yield 1.2
    shot("418_light_menu")
    close_popups()
    yield 0.6


def f420():
    select(["Key"])
    yield 0.8
    props('DATA')
    scroll_props_top()
    yield 1.5
    shot("420_light_area")


def f422():
    """Vue de dessus, mode Solid : les trois lumières et leur direction autour de la lampe."""
    look('SOLID', overlays=True)
    sp = v3d()
    sp.overlay.show_floor = False
    sp.overlay.show_extras = True
    deselect_all()
    r3d = sp.region_3d
    r3d.view_perspective = 'ORTHO'
    r3d.view_rotation = (0, 0, 0, 1) and Vector((0, 0, -1)).to_track_quat('-Z', 'Y')
    r3d.view_location = Vector((0.2, -0.05, 0.3))
    r3d.view_distance = 2.4
    lc = bpy.context.view_layer.layer_collection.children
    hidden = [n for n in ("Studio", "Nuancier", "Cameras") if not lc[n].hide_viewport]
    for n in hidden:
        lc[n].hide_viewport = True
    for n in ("Key", "Fill", "Rim"):
        O[n].show_name = True
    yield 2.5
    shot("422_dessus")
    for n in hidden:
        lc[n].hide_viewport = False
    r3d.view_perspective = 'PERSP'
    look('MATERIAL')


def f424():
    o = area('OUTLINER')
    reg = region(o)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(o)):
        for _ in range(4):
            bpy.ops.outliner.show_one_level(open=False)
        bpy.ops.outliner.show_one_level(open=True)
    yield 0.8
    select(["Key"])
    with bpy.context.temp_override(**ov(o)):
        bpy.ops.outliner.show_active()
    yield 1.2
    shot("424_outliner")


def f441():
    O["Spot_lampe"].hide_set(False)
    select(["Spot_lampe"])
    yield 0.8
    props('DATA')
    scroll_props_top()
    yield 1.5
    shot("441_spot")
    O["Spot_lampe"].hide_set(True)


# ---------------------------------------------------------------------------- section 3
def f426():
    look('MATERIAL')
    view_from((0.55, -2.30, 0.55), (0.22, -0.03, 0.18), 0.55)
    yield 1.5
    shot("426_avant")
    call_menu("VIEW3D_MT_view_cameras", at=(0.3, 0.7))
    yield 1.2
    shot("426_cameras")
    close_popups()
    yield 0.6
    call_menu("VIEW3D_MT_view_align", at=(0.3, 0.7))
    yield 1.2
    shot("426_align")
    close_popups()
    yield 0.6


def f427():
    sp = v3d()
    sp.show_region_ui = True
    sp.lock_camera = True
    yield 1.0
    click(*SIDEBAR_VIEW)
    yield 1.2
    shot("427_sidebar")
    sp.lock_camera = False
    sp.show_region_ui = False
    yield 0.5


def f428():
    select(["CAM_heros"])
    yield from props_panel("428_lens", "Lens", ctx='DATA', order=CAMERA_ORDER)


def f430():
    select(["CAM_heros"])
    O["CAM_heros"].data.show_composition_thirds = True
    yield from props_panel("430_display", "Viewport Display", ctx='DATA', order=CAMERA_ORDER)
    click(*COMPO)
    yield 1.2
    shot("430_composition")


def f431():
    look('RENDERED', overlays=True)
    sc.world = bpy.data.worlds["Monde_Neutre"]
    sc.collection.children["Nuancier"].hide_viewport = True
    deselect_all()
    O["CAM_heros"].data.show_composition_thirds = True
    O["CAM_heros"].data.passepartout_alpha = 0.6
    camera_view("CAM_heros")
    sp = v3d()
    sp.overlay.show_extras = False
    yield 6.0
    shot("431_camview", extra={"CAM_BOX": camera_frame_box("CAM_heros")})
    sp.region_3d.view_perspective = 'PERSP'
    look('MATERIAL')


def f432():
    select(["CAM_detail"])
    yield from props_panel("432_dof", "Depth of Field", ctx='DATA', order=CAMERA_ORDER)


def f434():
    yield 0.8
    props('OUTPUT')
    scroll_props_top()
    yield 1.2
    shot("434_format")
    shot("435_presets_avant")
    call_panel("RENDER_PT_format_presets", a_kind='PROPERTIES', at=(0.9, 0.62))
    yield 1.2
    shot("435_presets")
    close_popups()
    yield 0.6


def f436():
    yield 0.5
    shot("436_render_avant")
    call_menu("TOPBAR_MT_render", a_kind='VIEW_3D', at=(0.15, 0.95))
    yield 1.2
    shot("436_render_menu")
    close_popups()
    yield 0.6


def f437():
    """Image > Save As de l'image rendue : la fenêtre de fichiers, dans la fenêtre principale."""
    sc.world = bpy.data.worlds["Monde_Studio"]
    sc.camera = O["CAM_banc_essai"]
    sc.render.resolution_percentage = 25
    a = area('VIEW_3D')
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.render.render('INVOKE_DEFAULT')
    yield 6.0
    ie = next((x for x in win().screen.areas if x.type == 'IMAGE_EDITOR'), None)
    if ie is None:
        print("ECHEC 437 : pas d'éditeur d'image")
        return
    reg = region(ie)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(ie)):
        bpy.ops.image.save_as('INVOKE_DEFAULT', save_as_render=True)
    yield 2.5
    fb = next((x for x in win().screen.areas if x.type == 'FILE_BROWSER'), None)
    if fb is not None:
        sp = fb.spaces.active
        sp.show_region_toolbar = False
        if sp.params is not None:
            sp.params.filename = "lampe_heros_MJ_v001.png"
    yield 1.5
    click(*SAVE_CM)
    yield 1.2
    shot("437_save_as")
    yield from cancel_file_browser()
    ie = next((x for x in win().screen.areas if x.type == 'IMAGE_EDITOR'), None)
    if ie is not None:
        with bpy.context.temp_override(**ov(ie)):
            bpy.ops.screen.back_to_previous()
    yield 1.0
    sc.render.resolution_percentage = 100
    sc.world = bpy.data.worlds["Monde_Neutre"]


STEPS = [("402", f402), ("403", f403), ("404", f404), ("405", f405), ("406", f406), ("407", f407),
         ("409", f409), ("411", f411), ("412", f412), ("438", f438), ("415", f415), ("416", f416),
         ("418", f418), ("420", f420), ("422", f422), ("424", f424), ("441", f441), ("426", f426),
         ("427", f427), ("428", f428), ("430", f430), ("431", f431), ("432", f432), ("434", f434),
         ("436", f436), ("417", f417), ("408", f408), ("437", f437)]


def runner():
    learner_state()
    yield from layout_for_captures()
    if RECON:
        yield from recon()
        return
    for key, fn in STEPS:
        if ONLY and key not in ONLY:
            continue
        try:
            for delay in fn():
                yield delay
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("ECHEC", key, repr(e), flush=True)
        if win().workspace.name != "Layout":
            yield from set_workspace("Layout")
        yield 0.5


_it = None


def tick():
    global _it
    try:
        if _it is None:
            _it = runner()
        return next(_it)
    except StopIteration:
        print("CAPTURES TERMINEES", flush=True)
        os._exit(0)
    except Exception:
        import traceback
        traceback.print_exc()
        os._exit(1)


bpy.app.timers.register(tick, first_interval=3.0)
bpy.app.timers.register(lambda: os._exit(2), first_interval=900.0)   # sécurité : quitte toujours
