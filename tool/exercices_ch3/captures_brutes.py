# Captures brutes (fenêtre entière) des figures du chapitre 3.
# Ouvre une VRAIE fenêtre Blender, séparée de celle du formateur, avec une configuration temporaire.
# Rien n'est enregistré : les fichiers .blend ne sont pas modifiés sur le disque. Les matières sont
# créées en mémoire, d'après tool/exercices_ch3/matieres.py, pour reproduire chaque étape du chapitre.
#
# Usage (PowerShell), depuis la racine du dépôt, verrou tool\production\capture.lock posé :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-captures-ch3"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 <fichier.blend> --python tool\exercices_ch3\captures_brutes.py -- <dossier_sortie> [étape ...]
# Une passe par fichier : la lampe à habiller (fiche A), la lampe habillée (A2), le nuancier (B) et les
# finitions triplanaires (C). Les clics simulés utilisent des coordonnées relevées sur une première
# série de captures (variables d'environnement, voir en bas).
# Repris de tool/exercices_ch2/captures_brutes.py.

import json
import math
import os
import sys

import bpy
from mathutils import Euler, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import matieres as M   # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = args[0] if args else os.path.join(os.environ.get("TEMP", "."), "captures_ch3")
ONLY = set(args[1:])
os.makedirs(OUT, exist_ok=True)
H = 960
NUANCIER = os.path.join(HERE, "_construction", "PRC02_bibliotheque_CMF", "PRC02_ch3_nuancier_cmf.blend")
BIBLIO_DIR = os.path.dirname(NUANCIER)

prefs = bpy.context.preferences
prefs.use_preferences_save = False
prefs.view.ui_scale = 1.25
prefs.view.show_tooltips = False
prefs.view.show_splash = False
prefs.view.smooth_view = 0          # les vues se recadrent d'un coup (pas d'animation à attendre)
O = bpy.data.objects
BASE = os.path.basename(bpy.data.filepath)


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


def mode(m):
    if bpy.context.mode == m or (m == 'OBJECT' and bpy.context.mode == 'OBJECT'):
        return
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.object.mode_set(mode=m)


def select(names, active=None):
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    for n in names:
        O[n].select_set(True)
    vl.objects.active = O[active or names[-1]] if names else None


def deselect_all():
    for o in bpy.context.view_layer.objects:
        o.select_set(False)


def eval_points(names):
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for n in names:
        e = O[n].evaluated_get(dg)
        me = e.to_mesh()
        pts += [e.matrix_world @ v.co for v in me.vertices]
        e.to_mesh_clear()
    return pts


def view_on(names, rot=None, zoom=1.0, persp='PERSP', a=None, eye=None):
    """Cadre les objets nommés : une boîte temporaire à leurs dimensions, puis View Selected.
    eye : direction de la cible vers l'œil, à la place des angles rot."""
    pts = eval_points(names)
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    me = bpy.data.meshes.new("_cadre")
    me.from_pydata([(x, y, z) for x in (lo.x, hi.x) for y in (lo.y, hi.y) for z in (lo.z, hi.z)], [], [])
    box = bpy.data.objects.new("_cadre", me)
    bpy.context.scene.collection.objects.link(box)
    vl = bpy.context.view_layer
    prev = [o for o in vl.objects if o.select_get()]
    act = vl.objects.active
    for o in vl.objects:
        o.select_set(False)
    box.select_set(True)
    vl.objects.active = box
    a = a or area('VIEW_3D')
    r3d = a.spaces.active.region_3d
    if eye is not None:
        r3d.view_rotation = (-Vector(eye).normalized()).to_track_quat('-Z', 'Y')
    elif rot is not None:
        r3d.view_rotation = Euler([math.radians(x) for x in rot]).to_quaternion()
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.view3d.view_selected(use_all_regions=False)
    r3d.view_perspective = persp
    r3d.view_distance *= zoom
    bpy.data.objects.remove(box)
    bpy.data.meshes.remove(me)
    for o in prev:
        o.select_set(True)
    vl.objects.active = act


def look(kind='MATERIAL', a=None, hdri='studio.exr', rotate=0.0):
    sp = (a or area('VIEW_3D')).spaces.active
    sp.shading.type = kind
    if kind == 'MATERIAL':
        sp.shading.studio_light = hdri
        sp.shading.studiolight_rotate_z = math.radians(rotate)
        sp.shading.use_scene_lights = False
        sp.shading.use_scene_world = False
        sp.shading.studiolight_background_alpha = 0.0     # fond uni, même dans l'espace Shading
    sp.overlay.show_floor = False
    sp.overlay.show_axis_x = False
    sp.overlay.show_axis_y = False
    sp.overlay.show_cursor = False
    sp.overlay.show_text = False
    sp.overlay.show_stats = False
    sp.overlay.show_look_dev = False
    sp.overlay.show_outline_selected = True
    sp.overlay.show_object_origins = False
    sp.show_gizmo_navigate = False
    sp.clip_start = 0.001


def props(context):
    a = area('PROPERTIES')
    a.spaces.active.context = context
    return a


def expand_only(o, keep):
    for m in o.modifiers:
        m.show_expanded = m.name in keep


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


def call_panel(name, a_kind='VIEW_3D', at=(0.9, 0.97)):
    a, _x, _y = warp(a_kind, at)
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.call_panel('INVOKE_DEFAULT', name=name, keep_open=True)


def close_popups():
    w = win()
    w.event_simulate(type='ESC', value='PRESS')
    w.event_simulate(type='ESC', value='RELEASE')


def click(x, y_img, button='LEFTMOUSE', ctrl=False):
    w = win()
    y = H - y_img
    w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
    w.event_simulate(type=button, value='PRESS', x=x, y=y, ctrl=ctrl)
    w.event_simulate(type=button, value='RELEASE', x=x, y=y, ctrl=ctrl)


def hover(x, y_img):
    win().event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=H - y_img)


def wheel(a_kind, n, down=True):
    a, x, y = warp(a_kind, (0.5, 0.5))
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
    print("CAPTURE", path)


def move_border(a_kind, side, delta):
    """Déplace la bordure d'une zone : 'top' (bordure haute) ou 'left' (bordure gauche).
    screen.area_move est refusé tant qu'une région est active sous la souris : un mouvement simulé
    sur la bordure la désactive ; on essaie quelques positions de part et d'autre de la bordure."""
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
    p = area('PROPERTIES')
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
    w = win()
    w.workspace = bpy.data.workspaces[name]
    yield 1.5


def node_area():
    return area('NODE_EDITOR')


def node_view_all(a=None):
    a = a or node_area()
    reg = region(a)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.node.view_all()


def node_view_selected(nodes, a=None, zoom=0):
    """À appeler après un redessin : un nœud tout juste créé n'a pas encore de dimensions.
    View Selected centre sans agrandir : zoom_in agrandit ensuite autour du centre."""
    a = a or node_area()
    nt = a.spaces.active.edit_tree
    for n in nt.nodes:
        n.select = n in nodes
    reg = region(a)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.node.view_selected()
        for _ in range(zoom):
            bpy.ops.view2d.zoom_in()
    for n in nt.nodes:
        n.select = False


def node_box(ne, nodes):
    """Boîte des nœuds donnés, en pixels de la capture (origine en haut à gauche). Les positions des
    nœuds sont en unités d'interface : elles se multiplient par l'échelle de l'interface ; leurs
    dimensions sont déjà à l'échelle."""
    reg = region(ne)
    v2d = reg.view2d
    ui = bpy.context.preferences.system.ui_scale
    xs, ys = [], []
    for n in nodes:
        x0, y0 = n.location_absolute.x * ui, n.location_absolute.y * ui
        w, h = n.dimensions
        for vx, vy in ((x0, y0), (x0 + w, y0 - h)):
            rx, ry = v2d.view_to_region(vx, vy, clip=False)
            xs.append(reg.x + rx)
            ys.append(H - (reg.y + ry))
    return [min(xs), min(ys), max(xs), max(ys)]


def node_band(name, nodes, maxw=1250, maxh=740, minh=0):
    """Le Shader Editor agrandi, cadré sur les nœuds donnés, réduit jusqu'à ce qu'ils tiennent dans
    maxw x maxh pixels : une bande large, lisible à l'échelle 0,55 dans l'application. minh : agrandit
    ensuite jusqu'à cette hauteur au moins (gros plan d'un seul nœud), sans dépasser maxw x maxh."""
    ne = node_area()
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.screen.screen_full_area()
    yield 1.2
    ne = node_area()
    nt = ne.spaces.active.edit_tree
    for n in nt.nodes:
        n.select = n in nodes
    win().cursor_warp(region(ne).x + region(ne).width // 2, region(ne).y + region(ne).height // 2)
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.view_selected()
    yield 0.6
    for _ in range(8):
        b = node_box(ne, nodes)
        if b[2] - b[0] <= maxw and b[3] - b[1] <= maxh:
            break
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_out()
        yield 0.4
    for _ in range(12):
        b = node_box(ne, nodes)
        if b[3] - b[1] >= minh:
            break
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_in()
        yield 0.4
        b = node_box(ne, nodes)
        if b[2] - b[0] > maxw or b[3] - b[1] > maxh:
            with bpy.context.temp_override(**ov(ne)):
                bpy.ops.view2d.zoom_out()
            yield 0.4
            break
    for n in nt.nodes:
        n.select = False
    yield 0.8
    shot(name, extra={"NODES_BOX": node_box(ne, nodes)})
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.screen.back_to_previous()
    yield 1.2


def node_max(name, zoom=0):
    """Capture du Shader Editor agrandi à toute la fenêtre, tous les nœuds cadrés, puis retour."""
    ne = node_area()
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.screen.screen_full_area()
    yield 1.2
    ne = node_area()
    for n in ne.spaces.active.edit_tree.nodes:
        n.select = False
    node_view_all(ne)
    if zoom:
        with bpy.context.temp_override(**ov(ne)):
            for _ in range(zoom):
                bpy.ops.view2d.zoom_in()
    yield 1.2
    shot(name)
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.screen.back_to_previous()
    yield 1.2


# ---------------------------------------------------------------------------- matières en mémoire
def mat(name, color, metallic=0.0, rough=0.5, opts=None):
    m = bpy.data.materials.get(name)
    if m is None:
        m = M.principled(name, color, metallic, rough, opts or {})
    return m


def give(names, m):
    for n in names:
        o = O[n]
        o.data.materials.clear()
        o.data.materials.append(m)


def principled(m):
    return next(n for n in m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')


def panel(m, which, open_=True):
    """Ouvre une rubrique du Principled : Diffuse, Subsurface, Specular, Transmission, Coat, Sheen,
    Emission, Thin Film (ordre des panel_states)."""
    order = ["Diffuse", "Subsurface", "Specular", "Transmission", "Coat", "Sheen", "Emission", "Thin Film"]
    p = principled(m)
    for i, s in enumerate(p.panel_states):
        if order[i] == which:
            s.is_collapsed = not open_


def clean_corriges():
    """Retire les corrigés de la fiche A (mémoire seulement) : listes de matières et vue propres."""
    for cname in ("Corrigé coloris A", "Corrigé coloris B", "Corrigé"):
        c = bpy.data.collections.get(cname)
        if c is None:
            continue
        for o in list(c.objects):
            bpy.data.objects.remove(o)
        bpy.data.collections.remove(c)
    for m in list(bpy.data.materials):
        if m.name.endswith("_corrige"):
            bpy.data.materials.remove(m)


S1 = {}


def s1_state():
    """L'état de la lampe à la fin de la section 1 (matières réglées dans le Principled seul)."""
    sc = bpy.context.scene
    sc.eevee.use_raytracing = True
    S1["Peinture_Vert"] = pv = mat("Peinture_Vert", "2F5D3A", 0, 0.4, {"coat": (1, 0.03)})
    principled(pv).inputs["Coat Weight"].default_value = 1
    principled(pv).inputs["Roughness"].default_value = 0.4
    S1["ABS_Noir"] = mat("ABS_Noir", "1A1A1A", 0, 0.15)
    S1["Alu_Naturel"] = mat("Alu_Naturel", "E6E7E8", 1, 0.3)
    S1["Chrome"] = mat("Chrome", "C4C5C5", 1, 0.03)
    S1["PVC_Mat_Noir"] = mat("PVC_Mat_Noir", "161616", 0, 0.7)
    S1["Verre_Clair"] = mat("Verre_Clair", "FFFFFF", 0, 0.0, {"glass": (1.5, True)})
    give(["Socle", "Tête"], S1["Peinture_Vert"])
    give(["Interrupteur", "Interrupteur_crans", "Grille_aeration"], S1["ABS_Noir"])
    give(["Bras_bas", "Bras_haut"], S1["Alu_Naturel"])
    give(["Articulation_bas", "Articulation_milieu", "Articulation_haut"], S1["Chrome"])
    give(["Câble"], S1["PVC_Mat_Noir"])
    give(["Ampoule"], S1["Verre_Clair"])


LAMP = ["Socle", "Tête", "Articulation_haut", "Câble", "Bras_bas"]
AV = (66, 0, -32)        # trois quarts avant gauche, un peu au-dessus


# ---------------------------------------------------------------------------- fiche A : section 1
def f302():
    look('MATERIAL')
    view_on(LAMP, rot=AV, zoom=1.0)
    deselect_all()
    yield 4.0
    shot("302_material_preview")


def f303():
    look('MATERIAL')
    yield 1.0
    shot("303_popover_avant")
    call_panel("VIEW3D_PT_shading")
    yield 2.0
    shot("303_popover")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f304():
    select(["Socle"])
    props('MATERIAL')
    yield 1.0
    shot("304_onglet_material_vide")


def f305():
    select(["Socle"])
    m = mat("Peinture_Vert", "2F5D3A", 0, 0.5)
    give(["Socle"], m)
    props('MATERIAL')
    yield 1.5
    shot("305_rubrique_surface")


def f306():
    m = mat("Peinture_Vert", "2F5D3A", 0, 0.5)
    give(["Socle", "Tête"], m)
    mat("ABS_Noir", "1A1A1A", 0, 0.15)
    give(["Interrupteur"], bpy.data.materials["ABS_Noir"])
    select(["Tête"])
    props('MATERIAL')
    yield 1.5
    shot("306_liste_avant")
    if not os.environ.get("RECON"):
        click(*BROWSE)
        yield 1.5
        shot("306_liste")
        close_popups()
        yield 0.5


def f308():
    s1_state()
    m = S1["Peinture_Vert"]
    panel(m, "Coat")
    select(["Tête"])
    props('MATERIAL')
    look('MATERIAL')
    view_on(["Tête"], rot=(75, 0, -40), zoom=1.15)
    deselect_all()
    O["Tête"].select_set(True)
    bpy.context.view_layer.objects.active = O["Tête"]
    yield 1.0
    wheel('PROPERTIES', 6)
    yield 1.0
    click(1122, 672)                  # en-tête de la rubrique Coat, après défilement
    yield 3.0
    shot("308_coat")
    click(1122, 672)
    wheel('PROPERTIES', 6, down=False)
    panel(m, "Coat", False)


def f309():
    s1_state()
    m = S1["Verre_Clair"]
    panel(m, "Transmission")
    select(["Ampoule"])
    props('MATERIAL')
    yield 1.0
    wheel('PROPERTIES', 5)
    yield 1.0
    click(1149, 697)                  # en-tête de la rubrique Transmission
    yield 1.5
    shot("309_transmission")
    click(1149, 697)
    wheel('PROPERTIES', 5, down=False)
    panel(m, "Transmission", False)


def f310():
    s1_state()
    look('MATERIAL')
    sc = bpy.context.scene
    m = S1["Verre_Clair"]
    p = principled(m)
    deselect_all()
    look('MATERIAL', rotate=150)
    view_on(["Ampoule", "Douille"], eye=(0.75, -0.45, -0.55), zoom=1.6)
    for key, rt, thin in (("a", False, False), ("b", True, False), ("c", True, True)):
        sc.eevee.use_raytracing = rt
        m.use_raytrace_refraction = rt
        p.inputs["Thin Wall"].default_value = thin
        yield 5.0
        shot("310_ampoule_" + key)
    p.inputs["Thin Wall"].default_value = True
    sc.eevee.use_raytracing = True
    m.use_raytrace_refraction = True


def f311():
    props('RENDER')
    yield 1.5
    shot("311_onglet_render")


def f312():
    s1_state()
    select(["Ampoule"])
    props('MATERIAL')
    yield 1.0
    wheel('PROPERTIES', 30)
    yield 1.5
    shot("312_settings")
    wheel('PROPERTIES', 30, down=False)
    yield 0.5


def f313():
    s1_state()
    select(["Ampoule"])
    props('MATERIAL')
    yield 1.5
    shot("313_thin_wall")


def f314():
    s1_state()
    v = mat("Voyant_Vert", "1A1A1A", 0, 0.3)
    p = principled(v)
    p.inputs["Emission Color"].default_value = M.lin("3CFF6E")
    p.inputs["Emission Strength"].default_value = 6.0
    give(["Interrupteur"], v)
    panel(v, "Emission")
    select(["Interrupteur"])
    props('MATERIAL')
    look('MATERIAL')
    view_on(["Interrupteur", "Socle"], rot=(55, 0, -25), zoom=0.55)
    yield 1.0
    wheel('PROPERTIES', 7)
    yield 1.0
    click(1134, 672)                  # en-tête de la rubrique Emission
    yield 3.0
    shot("314_emission")
    click(1134, 672)
    wheel('PROPERTIES', 7, down=False)
    give(["Interrupteur"], S1["ABS_Noir"])


def f315():
    s1_state()
    blanc = mat("Blanc_Interieur", "EDEDE8", 0, 0.6)
    t = O["Tête"]
    t.data.materials.append(blanc)
    t.modifiers["Solidify"].material_offset = 1
    select(["Tête"])
    props('MATERIAL')
    look('MATERIAL')
    view_on(["Tête", "Ampoule"], rot=(140, 0, -70), zoom=1.1)
    deselect_all()
    yield 4.0
    shot("315_deux_emplacements")


def f316():
    t = O["Tête"]
    select(["Tête"])
    expand_only(t, {"Solidify"})
    props('MODIFIER')
    yield 1.5
    shot("316_solidify_avant")
    if not os.environ.get("RECON"):
        click(*SOLIDIFY_MAT)
        yield 1.0
        shot("316_solidify_materials")


def f317():
    select(["Bras_haut", "Bras_bas"], active="Bras_bas")
    look('SOLID')
    yield 0.8
    shot("317_menu_link_avant")
    call_menu("VIEW3D_MT_make_links", at=(0.45, 0.7))
    yield 1.2
    shot("317_menu_link")
    close_popups()
    yield 0.5
    look('MATERIAL')


def f331():
    s1_state()
    select(["Bras_bas"])
    props('MATERIAL')
    yield 1.5
    shot("331_nom_avant")
    if not os.environ.get("RECON"):
        click(*MAT_NAME, button='RIGHTMOUSE')
        yield 1.2
        shot("331_menu_mark")
        close_popups()
        yield 0.5


def f332():
    t = area('TEXT_EDITOR')
    hx = region(t, 'HEADER')
    yield 0.5
    shot("332_type_editeur_avant")
    click(hx.x + 18, H - (hx.y + hx.height // 2))
    yield 1.2
    shot("332_type_editeur")
    close_popups()
    yield 0.5


def f340():
    yield 0.5
    shot("340_menu_file_avant")
    call_menu("TOPBAR_MT_file", at=(0.05, 0.98))
    yield 0.6
    hover(82, 329)                    # Append... en surbrillance ; le sous-menu New se referme
    yield 0.8
    shot("340_menu_file")
    close_popups()
    yield 0.5


def f344():
    # File > External Data : Pack Resources
    yield 0.5
    shot("344_external_data_avant")
    call_menu("TOPBAR_MT_file_external_data", at=(0.05, 0.98))
    yield 0.6
    hover(110, 87)                    # Pack Resources en surbrillance
    yield 0.8
    shot("344_external_data")
    close_popups()
    yield 0.5


def f345():
    # Outliner : menu contextuel d'une collection (Duplicate Collection)
    vl = bpy.context.view_layer
    vl.active_layer_collection = vl.layer_collection.children["Lampe"]
    yield 0.5
    shot("345_menu_collection_avant")
    call_menu("OUTLINER_MT_collection", 'OUTLINER', at=(0.4, 0.6))
    yield 1.2
    shot("345_menu_collection")
    close_popups()
    yield 0.5


def f342():
    s1_state()
    with bpy.data.libraries.load(NUANCIER, link=True) as (src, dst):
        dst.materials = ["Verre_Fume"]
    lm = dst.materials[0]
    give(["Ampoule"], lm)
    select(["Ampoule"])
    props('MATERIAL')
    yield 2.0
    shot("342_matiere_liee")
    give(["Ampoule"], S1["Verre_Clair"])


def f341():
    """File > Append, à l'intérieur du fichier du nuancier : le dialogue s'ouvre dans sa propre fenêtre,
    capturée seule. Le chemin est flouté au recadrage."""
    n0 = len(bpy.context.window_manager.windows)
    a = area('VIEW_3D')
    win().cursor_warp(a.x + a.width // 2, a.y + a.height // 2)
    d = NUANCIER + os.sep
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.append('INVOKE_DEFAULT', filepath=d, directory=d, filename="")
    yield 2.5
    wins = bpy.context.window_manager.windows
    if len(wins) > n0:
        w2 = wins[len(wins) - 1]
        for ar in w2.screen.areas:
            if ar.type == 'FILE_BROWSER':
                sp = ar.spaces.active
                sp.show_region_toolbar = False
                if sp.params is not None:
                    sp.params.display_type = 'LIST_VERTICAL'
        yield 1.5
        path = os.path.join(OUT, "341_append_dossiers.png")
        with bpy.context.temp_override(window=w2):
            bpy.ops.screen.screenshot(filepath=path, check_existing=False)
        info = {"WINDOW_SIZE": [w2.width, w2.height]}
        for ar in w2.screen.areas:
            for kind in ('WINDOW', 'HEADER', 'UI', 'TOOLS', 'TOOL_PROPS', 'EXECUTE'):
                try:
                    r = region(ar, kind)
                except StopIteration:
                    continue
                info[ar.type + ("" if kind == 'WINDOW' else "_" + kind)] = [r.x, w2.height - (r.y + r.height), r.x + r.width, w2.height - r.y]
        with open(os.path.join(OUT, "341_append_dossiers.json"), "w", encoding="utf-8") as f:
            json.dump(info, f)
        print("CAPTURE", path, flush=True)
        with bpy.context.temp_override(window=w2):
            bpy.ops.wm.window_close()
        yield 1.0
    else:
        print("ECHEC 341 : pas de fenêtre Append", flush=True)


# ---------------------------------------------------------------------------- fiche A : section 2
def f318():
    s1_state()
    yield from set_workspace("Shading")
    look('MATERIAL')
    select(["Bras_bas"])
    view_on(LAMP, rot=AV, zoom=0.9)
    O["Bras_bas"].select_set(True)
    yield 1.5
    node_view_all()
    with bpy.context.temp_override(**ov(node_area())):
        bpy.ops.view2d.zoom_out()
        bpy.ops.view2d.scroll_up(deltay=40)
    yield 4.0
    shot("318_espace_shading")


def f319():
    s1_state()
    yield from set_workspace("Shading")
    select(["Bras_bas"])
    props('MATERIAL')
    node_view_all()
    yield 2.0
    shot("319_noeud_et_onglet")
    m = bpy.data.materials["Alu_Naturel"]
    yield from node_band("319_noeuds", [principled(m), next(n for n in m.node_tree.nodes if n.type == 'OUTPUT_MATERIAL')], maxw=880)


def f320():
    yield from set_workspace("Shading")
    select(["Bras_bas"])
    node_view_all()
    yield 1.0
    shot("320_menu_add_avant")
    call_menu("NODE_MT_add", 'NODE_EDITOR', at=(0.25, 0.8))
    yield 1.2
    shot("320_menu_add")
    close_popups()
    yield 0.6
    call_menu("NODE_MT_category_shader_texture", 'NODE_EDITOR', at=(0.25, 0.8))
    yield 1.2
    shot("320_menu_texture")
    close_popups()
    yield 0.6


def arm_view(name, zoom, rotate=0):
    """Le bras du haut, presque à l'horizontale, dans la grande vue 3D de l'espace Layout."""
    yield from set_workspace("Layout")
    look('MATERIAL', rotate=rotate)
    deselect_all()
    view_on(["Bras_haut"], eye=(0.02, -1, 0.1), zoom=zoom)
    yield 5.0
    shot(name)


def chain_noise(m, stage):
    """Les étapes de la section 2 sur Alu_Naturel : 1 lien Noise > Base Color ; 2 coordonnées Object ;
    3 Bump ; 4 Mapping (le brossé)."""
    nt = m.node_tree
    p = principled(m)
    for n in list(nt.nodes):
        if n.type not in ('BSDF_PRINCIPLED', 'OUTPUT_MATERIAL'):
            nt.nodes.remove(n)
    # nœuds serrés (pas de 185 unités) : la bande tient à côté de la vue de la tige, à un zoom proche de 1
    nz = nt.nodes.new("ShaderNodeTexNoise")
    nz.location = (-185 if stage <= 2 else -370, 300)
    nodes = [nz, p]
    if stage == 1:
        nt.links.new(nz.outputs["Color"], p.inputs["Base Color"])
        return nodes
    tc = nt.nodes.new("ShaderNodeTexCoord")
    tc.location = (nz.location.x - 185, 300)
    nz.inputs["Scale"].default_value = 1000
    nz.inputs["Detail"].default_value = 4
    nodes.insert(0, tc)
    vec = tc.outputs["Object"]
    if stage >= 4:
        mp = nt.nodes.new("ShaderNodeMapping")
        mp.location = (nz.location.x - 185, 300)
        tc.location = (nz.location.x - 370, 300)
        mp.inputs["Scale"].default_value = (1, 1, 0.02)
        nt.links.new(vec, mp.inputs["Vector"])
        vec = mp.outputs["Vector"]
        nodes.insert(1, mp)
    nt.links.new(vec, nz.inputs["Vector"])
    if stage == 2:
        nt.links.new(nz.outputs["Color"], p.inputs["Base Color"])
        return nodes
    b = nt.nodes.new("ShaderNodeBump")
    b.location = (-185, 60)
    b.inputs["Strength"].default_value = 0.15 if stage >= 4 else 0.2
    nt.links.new(nz.outputs[0], b.inputs["Height"])
    nt.links.new(b.outputs["Normal"], p.inputs["Normal"])
    nodes.insert(-1, b)
    return nodes


def f321():
    s1_state()
    yield from set_workspace("Shading")
    look('MATERIAL')
    m = S1["Alu_Naturel"]
    nodes = chain_noise(m, 1)
    select(["Bras_bas"])
    yield 1.0
    node_view_all()
    deselect_all()
    view_on(["Bras_bas"], rot=(80, 0, -15), zoom=0.3)
    yield 4.0
    shot("321_noise_base_color")
    yield from node_band("321_noeuds", [n for n in m.node_tree.nodes if n.type in ('TEX_NOISE', 'BSDF_PRINCIPLED')], maxw=900)
    yield from arm_view("321_bras", 0.25, rotate=200)


def f322():
    s1_state()
    yield from set_workspace("Shading")
    look('MATERIAL')
    m = S1["Alu_Naturel"]
    nodes = chain_noise(m, 2)
    select(["Bras_bas"])
    yield 1.0
    node_view_all()
    deselect_all()
    view_on(["Bras_bas"], rot=(80, 0, -15), zoom=0.3)
    yield 4.0
    shot("322_coordonnees_object")
    yield from node_band("322_noeuds", [n for n in m.node_tree.nodes if n.type in ('TEX_COORD', 'TEX_NOISE', 'BSDF_PRINCIPLED')], maxw=900)
    yield from arm_view("322_bras", 0.25, rotate=200)


def f323():
    s1_state()
    yield from set_workspace("Shading")
    look('MATERIAL')
    m = S1["Alu_Naturel"]
    nodes = chain_noise(m, 3)
    select(["Bras_bas"])
    yield 1.0
    yield 1.0
    yield from node_band("323_chaine_bump", [n for n in m.node_tree.nodes if n.type in ('TEX_NOISE', 'BUMP', 'BSDF_PRINCIPLED')], maxw=900)
    yield from arm_view("323_bras", 0.25, rotate=200)


def f324():
    s1_state()
    yield from set_workspace("Shading")
    look('MATERIAL')
    m = S1["Alu_Naturel"]
    m.name = "Alu_Brosse"
    look('MATERIAL', rotate=200)
    nodes = chain_noise(m, 4)
    select(["Bras_bas"])
    yield 1.0
    node_view_all()
    deselect_all()
    view_on(["Bras_bas"], rot=(80, 0, -10), zoom=0.2)
    yield 5.0
    shot("324_brosse")
    yield from node_band("324_noeuds", [n for n in m.node_tree.nodes if n.type in ('TEX_COORD', 'MAPPING', 'TEX_NOISE', 'BUMP')], maxw=900)
    yield from arm_view("324_bras", 0.25, rotate=200)
    m.name = "Alu_Naturel"


def f327():
    s1_state()
    look('MATERIAL')
    m = M.lampe("Structure_Vert")
    give(["Socle"], m)
    tex = next(n for n in m.node_tree.nodes if n.type == 'TEX_IMAGE')
    deselect_all()
    keep = {"Socle", "Grille_aeration", "Interrupteur", "Interrupteur_crans"}
    for o in bpy.context.view_layer.objects:
        o.hide_set(o.name not in keep)
    view_on(["Socle"], eye=(0.7, -0.7, 0.28), zoom=0.62)
    for key, blend in (("a", 0.0), ("b", 0.25)):
        tex.projection_blend = blend
        yield 5.0
        shot("327_blend_" + key)
    for o in bpy.context.view_layer.objects:
        o.hide_set(False)


# ---------------------------------------------------------------------------- fiche A : le lot PBR du socle
def socle_structure():
    """La fin de la recette de la peinture structurée : la tête laquée, le socle en Structure_Vert."""
    s1_state()
    m = bpy.data.materials.get("Structure_Vert") or M.lampe("Structure_Vert")
    give(["Socle"], m)
    return m


def f_p1():
    """L'onglet Material du socle : le bouclier (Fake User) activé, puis le bouton de copie."""
    m = socle_structure()
    select(["Socle"])
    props('MATERIAL')
    yield 1.5
    shot("p1_bouclier_avant")
    m.use_fake_user = True
    area('PROPERTIES').tag_redraw()
    yield 1.5
    shot("p1_bouclier")
    print("UTILISATEURS", m.name, m.users, "fake", m.use_fake_user, flush=True)
    m.use_fake_user = False
    area('PROPERTIES').tag_redraw()
    yield 0.5


def f_p2():
    """Maj + A > Displacement, dans le Shader Editor : le nœud Normal Map, à côté de Bump."""
    socle_structure()
    yield from set_workspace("Shading")
    select(["Socle"])
    node_view_all()
    yield 1.0
    shot("p2_menu_displacement_avant")
    call_menu("NODE_MT_category_shader_displacement", 'NODE_EDITOR', at=(0.25, 0.8))
    yield 1.2
    shot("p2_menu_displacement")
    close_popups()
    yield 0.6


def socles_rangee(names):
    """Des copies du socle, une par matière, en rangée le long de X (mémoire seulement)."""
    s = O["Socle"]
    objs = []
    for i, name in enumerate(names):
        o = s if i == 0 else s.copy()
        if i:
            o.data = s.data.copy()
            s.users_collection[0].objects.link(o)
            o.name = "Socle_essai_%d" % i
        o.location = (0.21 * i, -0.40, 0.0125)
        give([o.name], bpy.data.materials.get(name) or (M.lampe(name) if name in M.LAMPE else M.pbr(name)))
        objs.append(o)
    return objs


def f_p3():
    """La chaîne du lot : vue d'ensemble dans une bande du Shader Editor, gros plans des nœuds (les trois
    images, puis l'image des normales avec le Normal Map), et le socle en noyer dans la grande vue 3D."""
    s1_state()
    m = bpy.data.materials.get("Bois_Noyer") or M.pbr("Bois_Noyer")
    give(["Socle"], m)
    yield from set_workspace("Shading")
    look('MATERIAL')
    select(["Socle"])
    yield 1.0
    node_view_all()
    yield 1.0
    nodes = m.node_tree.nodes
    yield from node_band("p3_chaine_pbr", [n for n in nodes if n.type != 'OUTPUT_MATERIAL'], maxw=1250, maxh=900)
    imgs = sorted((n for n in nodes if n.type == 'TEX_IMAGE'), key=lambda n: -n.location.y)
    nm = next(n for n in nodes if n.type == 'NORMAL_MAP')
    for key, group in (("diff", [imgs[0]]), ("nor", [imgs[2], nm])):
        yield from node_band("p3_gros_plan_" + key, group, maxw=900, maxh=430, minh=380)


def f_p4():
    """Le même socle, quatre finitions : peinture structurée, noyer, béton, palissandre."""
    s1_state()
    objs = socles_rangee(["Structure_Vert", "Bois_Noyer", "Beton_Lisse", "Palissandre_Verni"])
    look('MATERIAL', rotate=30)
    keep = {o.name for o in objs}
    for o in bpy.context.view_layer.objects:
        o.hide_set(o.name not in keep)
    deselect_all()
    view_on([o.name for o in objs], eye=(0, -1, 0.75), zoom=0.9)
    yield 6.0
    shot("p4_quatre_socles")
    for o in bpy.context.view_layer.objects:
        o.hide_set(False)


def f_p5():
    """Option : Ctrl + Maj + T de Node Wrangler, sur le Principled d'une matière neuve : la chaîne créée."""
    import addon_utils
    addon_utils.enable("node_wrangler", default_set=True, persistent=False)
    s1_state()
    m = bpy.data.materials.new("Essai_Node_Wrangler")
    try:
        m.use_nodes = True
    except Exception:
        pass
    give(["Socle"], m)
    yield from set_workspace("Shading")
    look('MATERIAL')
    select(["Socle"])
    yield 1.0
    node_view_all()
    yield 1.0
    ne = node_area()
    nt = m.node_tree
    p = principled(m)
    lot = "walnut_veneer_02"
    folder = os.path.join(M.TEX_PBR, lot) + os.sep
    files = [{"name": "%s_%s_1k.jpg" % (lot, c)} for c in ("diff", "rough", "nor_gl")]
    with bpy.context.temp_override(**ov(ne)):
        for n in nt.nodes:
            n.select = (n == p)          # posée juste avant l'appel : un redessin la perdrait
        nt.nodes.active = p
        r = bpy.ops.node.nw_add_textures_for_principled(directory=folder, files=files, relative_path=False)
    print("NODE WRANGLER", r, sorted(n.bl_idname for n in nt.nodes), flush=True)
    for n in nt.nodes:
        if n.type == 'TEX_IMAGE':
            print("  IMAGE", n.image.name, n.projection, n.image.colorspace_settings.name, flush=True)
        if n.type == 'TEX_COORD':
            print("  TC", [l.from_socket.name for l in nt.links if l.from_node == n], flush=True)
    yield 1.5
    node_view_all()
    yield 1.0
    yield from node_band("p5_node_wrangler", [n for n in nt.nodes if n.type not in ('OUTPUT_MATERIAL', 'FRAME')], maxw=1250, maxh=760)


# ---------------------------------------------------------------------------- fiche C
def chain_cuir(m, projection='FLAT'):
    nt = m.node_tree
    p = principled(m)
    tex = next(n for n in nt.nodes if n.type == 'TEX_IMAGE')
    tex.location = (-450, 150)
    tex.projection = projection
    tex.projection_blend = 0.3
    tc = nt.nodes.new("ShaderNodeTexCoord")
    tc.location = (-820, 150)
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.location = (-635, 150)
    mp.inputs["Scale"].default_value = (25, 25, 25)
    nt.links.new(tc.outputs["Object"], mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"], tex.inputs["Vector"])
    b = nt.nodes.new("ShaderNodeBump")
    b.location = (-170, -60)
    b.inputs["Strength"].default_value = 0.3
    nt.links.new(tex.outputs["Color"], b.inputs["Height"])
    nt.links.new(b.outputs["Normal"], p.inputs["Normal"])
    for n in nt.nodes:
        n.select = False
    nt.nodes.active = tex
    tex.select = True
    return tex


def f325():
    m = bpy.data.materials["Cuir_Graine_Noir"]
    tex = chain_cuir(m, 'FLAT')
    select(["Accoudoir"])
    ne = node_area()
    ne.spaces.active.show_region_ui = False
    yield 1.5
    node_view_selected([tex], zoom=4)
    look('MATERIAL')
    deselect_all()
    view_on(["Accoudoir"], rot=(62, 0, -28), zoom=0.62)
    yield 4.0
    shot("325_projection_avant")
    if not os.environ.get("RECON"):
        click(*PROJ_MENU)
        yield 1.2
        shot("325_projection_menu")
        close_popups()
        yield 0.5
    tex.projection = 'BOX'
    yield 4.0
    shot("326_box_reglee")
    shot("328_color_space_avant")
    if not os.environ.get("RECON"):
        click(*CSPACE_MENU)
        yield 1.2
        shot("328_color_space_menu")
        close_popups()
        yield 0.5
    yield from node_band("326_chaine_cuir", [n for n in m.node_tree.nodes if n.type in ('TEX_COORD', 'MAPPING', 'TEX_IMAGE', 'BUMP')], maxw=1150)
    # Blend : une image contrastée (la tôle larmée) en couleur, sur la coque de rétroviseur, vue à 45°
    # entre les axes X et Y : c'est là que deux projections se rejoignent
    d = bpy.data.materials.new("Blend_Demo")
    try:
        d.use_nodes = True
    except Exception:
        pass
    pd = principled(d)
    pd.inputs["Roughness"].default_value = 0.55
    nt = d.node_tree
    tcd = nt.nodes.new("ShaderNodeTexCoord")
    mpd = nt.nodes.new("ShaderNodeMapping")
    mpd.inputs["Scale"].default_value = (20, 20, 20)
    imd = nt.nodes.new("ShaderNodeTexImage")
    imd.image = M.image("tole_larmee")
    imd.projection = 'BOX'
    nt.links.new(tcd.outputs["Object"], mpd.inputs["Vector"])
    nt.links.new(mpd.outputs["Vector"], imd.inputs["Vector"])
    nt.links.new(imd.outputs["Color"], pd.inputs["Base Color"])
    give(["Coque_retroviseur"], d)
    deselect_all()
    look('MATERIAL', rotate=120)
    view_on(["Coque_retroviseur"], eye=(0.7, -0.7, 0.2), zoom=0.55)
    for key, blend in (("0", 0.0), ("2", 0.2)):
        imd.projection_blend = blend
        yield 4.0
        shot("327c_blend_" + key)


def f329():
    m = bpy.data.materials["Cuir_Graine_Noir"]
    chain_cuir(m, 'BOX')
    look('MATERIAL')
    deselect_all()
    view_on(["Accoudoir", "Accoudoir_jumeau"], eye=(0.15, -0.5, 0.85), zoom=0.62)
    yield 5.0
    shot("329_echelle_non_appliquee")
    j = O["Accoudoir_jumeau"]
    select(["Accoudoir_jumeau"])
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    deselect_all()
    yield 5.0
    shot("329_echelle_appliquee")


# ---------------------------------------------------------------------------- fiche B
def f307():
    look('MATERIAL')
    for c in bpy.context.view_layer.layer_collection.children:
        c.hide_viewport = c.collection.name not in ("Grille_Metallic_Roughness", "Support")
    names = [o.name for o in bpy.data.collections["Grille_Metallic_Roughness"].objects]
    deselect_all()
    view_on(names, eye=(0, -0.75, 0.66), zoom=0.8)
    yield 5.0
    shot("307_grille")
    for c in bpy.context.view_layer.layer_collection.children:
        c.hide_viewport = False


def prefs_area(section, search=""):
    t = area('VIEW_3D')
    t.type = 'PREFERENCES'
    bpy.context.preferences.active_section = section
    bpy.context.window_manager.addon_search = search


def f330():
    prefs_area('ADDONS', "node wrangler")
    yield 2.0
    shot("330_node_wrangler")
    area('PREFERENCES').type = 'VIEW_3D'
    bpy.context.window_manager.addon_search = ""
    yield 1.0


def f336():
    libs = bpy.context.preferences.filepaths.asset_libraries
    lib = libs.new(name="PRC02_bibliotheque_CMF", directory="C:\\Formation\\PRC02_bibliotheque_CMF\\")
    prefs_area('ASSETS')
    yield 1.5
    try:
        bpy.context.preferences.filepaths.active_asset_library = len(libs) + 1   # après All Libraries et Essentials
    except Exception as e:
        print("ACTIVE_LIB", repr(e), flush=True)
    if not os.environ.get("RECON"):
        click(*OFFLINE)
    yield 2.0
    shot("336_asset_libraries")
    area('PREFERENCES').type = 'VIEW_3D'
    libs.remove(lib)
    yield 1.0


def f300():
    # vue d'ensemble du nuancier
    look('MATERIAL', rotate=180)
    deselect_all()
    names = [o.name for c in ("Nuancier", "Grille_Metallic_Roughness") for o in bpy.data.collections[c].objects]
    view_on(names, eye=(0.25, -0.8, 0.75), zoom=0.8)
    yield 5.0
    shot("300_nuancier")


# ---------------------------------------------------------------------------- fiche A2
def asset_browser(height=430):
    if any(a.type == 'FILE_BROWSER' for a in win().screen.areas):
        area('FILE_BROWSER').spaces.active.params.asset_library_reference = 'LOCAL'
        yield 1.0
        return
    t = area('TEXT_EDITOR')
    yield from move_border('TEXT_EDITOR', 'top', height - t.height)
    t = area('TEXT_EDITOR')
    t.type = 'FILE_BROWSER'
    yield 0.8
    fb = area('FILE_BROWSER')
    fb.ui_type = 'ASSETS'
    yield 1.0
    sp = fb.spaces.active
    sp.params.asset_library_reference = 'LOCAL'
    sp.params.catalog_id = ""
    yield 1.0


def f301():
    look('MATERIAL')
    deselect_all()
    names = [o.name for o in bpy.data.objects if o.type in ('MESH', 'CURVE')]
    view_on(names, rot=(72, 0, -12), zoom=0.78)
    yield 5.0
    shot("301_deux_coloris")


def f333():
    yield from asset_browser()
    fb = area('FILE_BROWSER')
    sp = fb.spaces.active
    sp.params.catalog_id = M.CATS_LAMPE["Métaux"]
    sp.show_region_tool_props = True
    yield 1.0
    try:
        sp.activate_asset_by_id(bpy.data.materials["Alu_Brosse"])
    except Exception as e:
        print("ACTIVATE", repr(e))
    look('MATERIAL')
    yield 4.0
    shot("333_asset_browser")


def f337():
    libs = bpy.context.preferences.filepaths.asset_libraries
    if "PRC02_bibliotheque_CMF" not in libs:
        libs.new(name="PRC02_bibliotheque_CMF", directory=BIBLIO_DIR)
    yield from asset_browser()
    yield 1.0
    shot("337_bibliotheques_avant")
    if not os.environ.get("RECON"):
        click(*LIB_MENU)
        yield 1.2
        shot("337_bibliotheques")
        close_popups()
        yield 0.5
    fb = area('FILE_BROWSER')
    sp = fb.spaces.active
    sp.params.asset_library_reference = 'PRC02_bibliotheque_CMF'
    sp.params.catalog_id = ""
    yield 6.0
    shot("339_import_avant")
    if not os.environ.get("RECON"):
        click(*IMPORT_MENU)
        yield 1.2
        shot("339_import_method")
        click(*IMPORT_LIST)
        yield 1.2
        shot("339_import_liste")
        close_popups()
        yield 0.5
        close_popups()
        yield 0.5


def f338():
    """Une vignette de Current File glissée sur la douille : le glisser est simulé, la capture est prise
    pendant le glisser, puis Échap l'annule."""
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    yield from asset_browser()
    look('MATERIAL')
    fb = area('FILE_BROWSER')
    sp = fb.spaces.active
    sp.params.catalog_id = M.CATS_LAMPE["Métaux"]
    sp.show_region_tool_props = False          # sans barre latérale : cinq vignettes par rangée
    for c in bpy.context.view_layer.layer_collection.children:
        c.hide_viewport = c.collection.name != "Lampe"
    O["Douille"].data.materials.clear()
    O["Ampoule"].hide_set(True)
    deselect_all()
    view_on(["Douille", "Tête"], eye=(0.55, -0.22, -0.8), zoom=0.95)
    yield 4.0
    shot("338_glisser_avant")
    if not os.environ.get("RECON"):
        v = area('VIEW_3D')
        r = region(v)
        bottom = O["Douille"].matrix_world @ Vector((0, 0, -0.0105))   # la face visible, côté ouverture
        p = location_3d_to_region_2d(r, v.spaces.active.region_3d, bottom)
        tx, ty = int(r.x + p.x), int(r.y + p.y)
        sx, sy = THUMB
        w = win()
        w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=sx, y=H - sy)
        w.event_simulate(type='LEFTMOUSE', value='PRESS', x=sx, y=H - sy)
        for k in range(1, 21):
            x = int(sx + (tx - sx) * k / 20)
            y = int((H - sy) + (ty - (H - sy)) * k / 20)
            w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
        yield 1.5
        shot("338_glisser")
        w.event_simulate(type='ESC', value='PRESS')
        w.event_simulate(type='ESC', value='RELEASE')
        w.event_simulate(type='LEFTMOUSE', value='RELEASE', x=tx, y=ty)
        yield 0.8
    O["Ampoule"].hide_set(False)
    for c in bpy.context.view_layer.layer_collection.children:
        c.hide_viewport = False


def f343():
    look('MATERIAL')
    deselect_all()
    names = [o.name for o in bpy.data.objects if o.type in ('MESH', 'CURVE')]
    view_on(names, rot=(85, 0, 0), zoom=0.9)
    yield 5.0
    shot("343_coloris_face")


# coordonnées relevées sur une première série de captures (image 1600 x 960, origine en haut à gauche)
BROWSE = env_xy("BROWSE_XY", "1083,499")          # liste des matières, onglet Material
SOLIDIFY_MAT = env_xy("SOLIDIFY_MAT_XY", "1135,768")   # sous-rubrique Materials du Solidify
MAT_NAME = env_xy("MAT_NAME_XY", "1240,499")      # nom de la matière, onglet Material
PROJ_MENU = env_xy("PROJ_XY", "778,721")          # menu Projection du nœud Image Texture (agrandi)
CSPACE_MENU = env_xy("CSPACE_XY", "813,809")      # menu Color Space du même nœud, en projection Box
LIB_MENU = env_xy("LIB_XY", "150,555")            # sélecteur de bibliothèque de l'Asset Browser
IMPORT_MENU = env_xy("IMPORT_XY", "495,517")      # Import Settings de l'Asset Browser
THUMB = env_xy("THUMB_XY", "763,610")             # vignette Chrome, catalogue Métaux (Asset Browser sans barre latérale)
IMPORT_LIST = env_xy("IMPORT_LIST_XY", "570,565")  # liste Import Method, dans Import Settings
OFFLINE = env_xy("OFFLINE_XY", "420,200")          # bouton Continue Offline des préférences

STEPS = {
    "PRC02_ch3_lampe_a_habiller.blend": [
        ("302", f302), ("303", f303), ("304", f304), ("305", f305), ("306", f306), ("308", f308), ("309", f309),
        ("310", f310), ("311", f311), ("312", f312), ("313", f313), ("314", f314), ("315", f315), ("316", f316),
        ("317", f317), ("331", f331), ("332", f332), ("340", f340), ("344", f344), ("345", f345), ("342", f342),
        ("341", f341), ("327", f327), ("318", f318), ("319", f319), ("320", f320), ("321", f321), ("322", f322),
        ("323", f323), ("324", f324),
        ("p1", f_p1), ("p2", f_p2), ("p3", f_p3), ("p4", f_p4), ("p5", f_p5)],
    "PRC02_ch3_finitions_triplanaires.blend": [("325", f325), ("329", f329)],
    "PRC02_ch3_nuancier_cmf.blend": [("300", f300), ("307", f307), ("330", f330), ("336", f336)],
    "PRC02_ch3_lampe_habillage.blend": [("301", f301), ("343", f343), ("333", f333), ("338", f338), ("337", f337)],
}


def runner():
    if BASE == "PRC02_ch3_lampe_a_habiller.blend":
        clean_corriges()
    if BASE != "PRC02_ch3_finitions_triplanaires.blend":
        yield from layout_for_captures()
    for key, fn in STEPS[BASE]:
        if ONLY and key not in ONLY:
            continue
        try:
            for delay in fn():
                yield delay
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("ECHEC", key, repr(e))
            try:
                mode('OBJECT')
            except Exception:
                pass
        # retour à l'espace de départ entre deux étapes
        ws = "Shading" if BASE == "PRC02_ch3_finitions_triplanaires.blend" else "Layout"
        if win().workspace.name != ws:
            yield from set_workspace(ws)
        yield 0.5


_it = None


def tick():
    global _it
    try:
        if _it is None:
            _it = runner()
        return next(_it)
    except StopIteration:
        print("CAPTURES TERMINEES")
        os._exit(0)
    except Exception:
        import traceback
        traceback.print_exc()
        os._exit(1)


bpy.app.timers.register(tick, first_interval=3.0)
bpy.app.timers.register(lambda: os._exit(2), first_interval=900.0)   # sécurité : quitte toujours
