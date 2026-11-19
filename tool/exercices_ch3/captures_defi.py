# Captures brutes (fenêtre entière) des figures d'interface du défi procédural (section 4 du chapitre 3).
# Ouvre une VRAIE fenêtre Blender, séparée de celle du formateur, avec une configuration temporaire.
# Rien n'est enregistré : le fichier .blend n'est pas modifié sur le disque.
#
# Usage (PowerShell), depuis la racine du dépôt, verrou tool\production\capture.lock posé :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-captures-defi"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 _resources\exercices\PRC02_ch3_defi_procedural.blend `
#       --python tool\exercices_ch3\captures_defi.py -- <dossier_captures_brutes> [étape ...]
# Les figures se recadrent ensuite avec recadrer_defi.py. Repris de captures_brutes.py.

import json
import os
import sys

import bpy

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = args[0] if args else os.path.join(os.environ.get("TEMP", "."), "captures_defi")
ONLY = set(args[1:])
os.makedirs(OUT, exist_ok=True)
H = 960

prefs = bpy.context.preferences
prefs.use_preferences_save = False
prefs.view.ui_scale = 1.25
prefs.view.show_tooltips = False
prefs.view.show_splash = False
prefs.view.smooth_view = 0
O = bpy.data.objects
UI = 1.25


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


def close_popups():
    w = win()
    w.event_simulate(type='ESC', value='PRESS')
    w.event_simulate(type='ESC', value='RELEASE')


def warp_xy(x, y_img):
    win().cursor_warp(int(x), int(H - y_img))


def click(x, y_img, button='LEFTMOUSE'):
    w = win()
    y = int(H - y_img)
    w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=int(x), y=y)
    w.event_simulate(type=button, value='PRESS', x=int(x), y=y)
    w.event_simulate(type=button, value='RELEASE', x=int(x), y=y)


def set_workspace(name):
    win().workspace = bpy.data.workspaces[name]
    yield 1.5


def node_area():
    return area('NODE_EDITOR')


def node_box(ne, nodes):
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


def activate(obj_name):
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    ob = O[obj_name]
    ob.select_set(True)
    vl.objects.active = ob


def full(on=True):
    ne = node_area()
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.screen.screen_full_area() if on else bpy.ops.screen.back_to_previous()


def band(name, obj_name, pick, maxw=1300, maxh=800, menu=None, zoom_in=0, group=False, after=None, isolate=False):
    """Le Shader Editor agrandi à toute la fenêtre, cadré sur les nœuds choisis par pick(nt), réduit
    jusqu'à ce qu'ils tiennent dans maxw x maxh pixels. menu : un chemin de propriété du nœud actif
    (ex. « active_node.noise_type ») dont le menu s'ouvre à côté du nœud, capturé en <name>_menu.
    group : entrer d'abord dans le nœud de groupe sélectionné. after(ne, nt) : un geste avant la capture.
    isolate : capturer une copie de la matière, réduite aux nœuds choisis (la matière d'origine revient
    ensuite sur la pièce)."""
    activate(obj_name)
    ob = O[obj_name]
    m0 = ob.active_material
    m1 = None
    if isolate:
        m1 = m0.copy()
        ob.active_material = m1
        keep = set(n.name for n in pick(m1.node_tree))
        for n in list(m1.node_tree.nodes):
            if n.name not in keep:
                m1.node_tree.nodes.remove(n)
    yield 0.8
    full(True)
    yield 1.2
    ne = node_area()
    sp = ne.spaces.active
    if group:
        nt0 = sp.edit_tree
        gn = next(n for n in nt0.nodes if n.type == 'GROUP')
        for n in nt0.nodes:
            n.select = n is gn
        nt0.nodes.active = gn
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.node.group_edit(exit=False)
        yield 1.0
    nt = sp.edit_tree
    nodes = list(nt.nodes) if isolate else pick(nt)    # la copie isolée ne garde que les nœuds choisis
    for n in nt.nodes:
        n.select = n in nodes
    reg = region(ne)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.view_selected()
    yield 0.6
    # View Selected centre sans agrandir : on agrandit tant que la bande reste dans maxw x maxh,
    # puis on réduit si un pas a dépassé
    for _ in range(10):
        b = node_box(ne, nodes)
        if (b[2] - b[0]) * 1.3 > maxw or (b[3] - b[1]) * 1.3 > maxh:
            break
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_in()
        yield 0.3
    for _ in range(12):
        b = node_box(ne, nodes)
        if b[2] - b[0] <= maxw and b[3] - b[1] <= maxh:
            break
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_out()
        yield 0.3
    for _ in range(zoom_in):
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_in()
        yield 0.3
    for n in nt.nodes:
        n.select = False
    if after:
        after(ne, nt)
    yield 0.8
    box = node_box(ne, nodes)
    shot(name, extra={"NODES_BOX": box})
    if menu:
        nt.nodes.active = nodes[0]
        warp_xy(box[2] + 230, box[1] + 40)
        yield 0.3
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.wm.context_menu_enum('INVOKE_DEFAULT', data_path=menu)
        yield 1.0
        shot(name + "_menu")
        close_popups()
        yield 0.5
    if group:
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.node.group_edit(exit=True)
        yield 0.5
    full(False)
    yield 1.2
    if m1 is not None:
        ob.active_material = m0
        bpy.data.materials.remove(m1)


def by_type(*types):
    return lambda nt: [n for n in nt.nodes if n.type in types]


def by_idname(*names):
    return lambda nt: [n for n in nt.nodes if n.bl_idname in names]


def all_but(*types):
    return lambda nt: [n for n in nt.nodes if n.type not in types]


def call_menu(name, at=(0.3, 0.75)):
    ne = node_area()
    win().cursor_warp(int(ne.x + ne.width * at[0]), int(ne.y + ne.height * at[1]))
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.wm.call_menu('INVOKE_DEFAULT', name=name)


# ---------------------------------------------------------------------------- les étapes
def f_menus():
    """Les sous-menus de Maj + A, ouverts dans le Shader Editor agrandi, loin de son en-tête."""
    activate("E1_Pratique")
    yield 1.0
    full(True)
    yield 1.2
    ne = node_area()
    sp = ne.spaces.active
    for n in sp.edit_tree.nodes:
        n.location.y += 3000            # les nœuds hors de vue : un fond uni derrière les menus
    yield 1.0
    shot("u_menus_avant")
    for key, menu in (("color", "NODE_MT_category_shader_color"), ("math", "NODE_MT_category_shader_math"),
                      ("vector", "NODE_MT_category_shader_vector"),
                      ("displacement", "NODE_MT_category_shader_displacement")):
        call_menu(menu, at=(0.3, 0.75))
        yield 1.2
        shot("u_menu_" + key)
        close_popups()
        yield 0.6
    for n in sp.edit_tree.nodes:
        n.location.y -= 3000
    full(False)
    yield 1.2


def f_overlay():
    activate("E1_Exemple_Noise")
    yield 1.0
    shot("u_overlay_avant")
    ne = node_area()
    hdr = region(ne, 'HEADER')
    win().cursor_warp(hdr.x + hdr.width - 60, hdr.y + hdr.height // 2)
    with bpy.context.temp_override(**ov(ne, 'HEADER')):
        bpy.ops.wm.call_panel('INVOKE_DEFAULT', name="NODE_PT_overlay", keep_open=True)
    yield 1.2
    shot("u_overlay")
    close_popups()
    yield 0.6


def f_preview():
    yield from band("u_preview", "E1_Exemple_Noise", all_but(), maxw=1080, maxh=640)


def f_noeuds_e1():
    yield from band("u_noise", "E1_Exemple_Noise", by_type('TEX_NOISE'), maxw=330, maxh=560,
                    menu="active_node.noise_type")
    yield from band("u_voronoi", "E1_Exemple_Voronoi", by_type('TEX_VORONOI'), maxw=330, maxh=560,
                    menu="active_node.feature")
    yield from band("u_wave", "E1_Exemple_Wave", by_type('TEX_WAVE'), maxw=330, maxh=560)
    yield from band("u_gabor", "E1_Exemple_Gabor", by_type('TEX_GABOR'), maxw=330, maxh=560)


def f_noeuds_e2():
    yield from band("u_ramp", "E2_Pratique_Mouchete_corrige", by_type('VALTORGB'), maxw=420, maxh=520,
                    menu="active_node.color_ramp.interpolation")
    yield from band("u_maprange", "E2_Pratique_Planche_corrige", by_type('MAP_RANGE'), maxw=330, maxh=560)
    yield from band("u_math", "E2_Pratique_Mouchete_corrige", by_type('MATH'), maxw=330, maxh=400,
                    menu="active_node.operation")
    yield from band("u_mouchete", "E2_Exemple_Coque", all_but('OUTPUT_MATERIAL'), maxw=1080, maxh=640, isolate=True)
    yield from band("u_planche", "E2_Pratique_Planche_corrige", all_but('OUTPUT_MATERIAL'), maxw=1080, maxh=640,
                    isolate=True)


def f_noeuds_e3():
    def mixes(nt):
        ms = [n for n in nt.nodes if n.type == 'MIX']
        ms.sort(key=lambda n: -n.location.y)
        return ms[:2]
    yield from band("u_mix", "E3_Pratique_Main_courante_corrige", mixes, maxw=330, maxh=580)
    yield from band("u_sepxyz", "E3_Pratique_Main_courante_corrige", by_type('SEPXYZ'), maxw=330, maxh=400)
    yield from band("u_patine", "E3_Pratique_Main_courante_corrige", all_but('OUTPUT_MATERIAL'), maxw=1400, maxh=860)


def f_noeuds_e4():
    def b2(nt):
        bs = [n for n in nt.nodes if n.type == 'BUMP']
        return [max(bs, key=lambda n: n.location.x)]
    yield from band("u_bump", "E4_Pratique_Boitier_corrige", b2, maxw=330, maxh=560)
    yield from band("u_bumps", "E4_Pratique_Boitier_corrige", all_but('OUTPUT_MATERIAL'), maxw=1080, maxh=640,
                    isolate=True)
    yield from band("u_coat", "E4_Pratique_Coque_corrige", by_type('BUMP', 'BSDF_PRINCIPLED', 'TEX_NOISE', 'TEX_COORD'),
                    maxw=1300, maxh=860, isolate=True)


def f_noeuds_e5():
    def masque(nt):
        mc = next(n for n in nt.nodes if n.type == 'MIX')
        return [n for n in nt.nodes if n.location.x < mc.location.x - 10 and n.type != 'FRAME']
    yield from band("u_bords", "E5_Pratique_Socle_corrige", masque, maxw=1400, maxh=760, isolate=True)
    yield from band("u_vecmath", "E5_Defi_Coffret_corrige", by_type('VECT_MATH'), maxw=330, maxh=400)
    yield from band("u_ao", "E5_Pratique_Marchepied_corrige", by_type('AMBIENT_OCCLUSION'), maxw=330, maxh=400)


def f_noeuds_e6():
    yield from band("u_tole", "E6_Pratique_Grille_corrige", all_but('OUTPUT_MATERIAL'), maxw=1080, maxh=640,
                    isolate=True)
    yield from band("u_cuir", "E6_Pratique_Accoudoir_corrige", all_but('OUTPUT_MATERIAL', 'BSDF_PRINCIPLED'),
                    maxw=1000, maxh=560, isolate=True)
    yield from band("u_checker", "E6_Pratique_Assise_corrige", by_type('TEX_CHECKER'), maxw=330, maxh=420)
    yield from band("u_tissu", "E6_Pratique_Assise_corrige", all_but('OUTPUT_MATERIAL'), maxw=1400, maxh=860,
                    isolate=True)
    yield from band("u_gradient", "E6_Defi_Molette_corrige", by_type('TEX_GRADIENT'), maxw=330, maxh=300,
                    menu="active_node.gradient_type")
    yield from band("u_molette", "E6_Defi_Molette_corrige", all_but('OUTPUT_MATERIAL', 'BSDF_PRINCIPLED'),
                    maxw=1400, maxh=760, isolate=True)
    yield from band("u_carbone", "E6_Defi_Panneau_corrige",
                    lambda nt: [n for n in nt.nodes if n.type in ('SEPXYZ', 'MATH', 'TEX_COORD')], maxw=1400, maxh=760,
                    isolate=True)


def f_groupes():
    g = bpy.data.node_groups.get("PRC_Usure_Bords_corrige")
    if g is not None:
        g.name = "PRC_Usure_Bords"             # le nom que l'apprenant donne (en mémoire seulement)
    t = bpy.data.node_groups.get("PRC_Tole_Perforee_corrige")
    if t is not None:
        t.name = "PRC_Tole_Perforee"
    # le menu Node, avec Make Group
    activate("E7_Pratique_Socle")
    yield 1.0
    shot("u_node_menu_avant")
    ne = node_area()
    hdr = region(ne, 'HEADER')
    win().cursor_warp(hdr.x + 200, hdr.y + hdr.height // 2)
    with bpy.context.temp_override(**ov(ne, 'HEADER')):
        bpy.ops.wm.call_menu('INVOKE_DEFAULT', name="NODE_MT_node")
    yield 1.2
    shot("u_node_menu")
    close_popups()
    yield 0.6
    # l'intérieur du groupe
    yield from group_inside()
    # la barre latérale, onglet Group, prise Largeur active
    activate("E7_Pratique_Socle_corrige")
    yield 0.8
    full(True)
    yield 1.2
    ne = node_area()
    sp = ne.spaces.active
    nt0 = sp.edit_tree
    gn = next(n for n in nt0.nodes if n.type == 'GROUP')
    for n in nt0.nodes:
        n.select = n is gn
    nt0.nodes.active = gn
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.group_edit(exit=False)
    yield 1.0
    sp.show_region_ui = True
    yield 1.0
    grp = sp.edit_tree
    item = next(i for i in grp.interface.items_tree if getattr(i, "name", "") == "Largeur")
    grp.interface.active = item
    try:
        region(ne, 'UI').active_panel_category = 'Group'
    except Exception as e:
        print("CATEGORIE", repr(e))
    yield 1.5
    shot("u_sidebar_group")
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.group_edit(exit=True)
    yield 0.5
    sp.show_region_ui = False
    full(False)
    yield 1.2
    # Maj + A > Group
    activate("E7_Pratique_Socle")
    yield 1.0
    full(True)
    yield 1.2
    sp = node_area().spaces.active
    for n in sp.edit_tree.nodes:
        n.location.y += 3000            # un fond uni derrière le menu
    yield 1.0
    shot("u_add_group_avant")
    try:
        call_menu("NODE_MT_group_add", at=(0.3, 0.75))
    except Exception as e:
        print("MENU GROUP", repr(e))
    yield 1.2
    shot("u_add_group")
    close_popups()
    yield 0.6
    for n in sp.edit_tree.nodes:
        n.location.y -= 3000
    full(False)
    yield 1.2
    # le groupe en service
    yield from band("u_group_use", "E7_Pratique_Socle_corrige", all_but('OUTPUT_MATERIAL'), maxw=1300, maxh=700)


def repack(nt, gap_x=40, gap_y=30):
    """Range les nœuds en colonnes d'après leurs dimensions affichées (nœuds repliés compris)."""
    ui = bpy.context.preferences.system.ui_scale
    cols = {}
    for n in nt.nodes:
        cols.setdefault(round(n.location.x / 10), []).append(n)
    keys = sorted(cols)
    x = min(n.location.x for n in nt.nodes)
    top = max(n.location.y for n in nt.nodes)
    for k in keys:
        nodes = sorted(cols[k], key=lambda n: -n.location.y)
        w = max(n.dimensions.x for n in nodes) / ui
        y = top
        for n in nodes:
            n.location = (x, y)
            y -= n.dimensions.y / ui + gap_y
        x += w + gap_x


def group_inside():
    """L'intérieur du groupe d'usure : Group Input et Group Output dépliés, les nœuds du calcul repliés
    (Ctrl + H) et resserrés, pour une bande lisible. Sur une copie du groupe et de la matière."""
    name = "E7_Pratique_Socle_corrige"
    activate(name)
    ob = O[name]
    m0 = ob.active_material
    m1 = m0.copy()
    ob.active_material = m1
    gn = next(n for n in m1.node_tree.nodes if n.type == 'GROUP')
    g0 = gn.node_tree
    gname = g0.name
    g1 = g0.copy()
    g0.name = "_origine"
    g1.name = gname
    gn.node_tree = g1
    for n in g1.nodes:
        if n.type not in ('GROUP_INPUT', 'GROUP_OUTPUT'):
            n.hide = True
    yield 0.8
    full(True)
    yield 1.2
    ne = node_area()
    sp = ne.spaces.active
    nt0 = sp.edit_tree
    for n in nt0.nodes:
        n.select = n is gn
    nt0.nodes.active = gn
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.group_edit(exit=False)
    yield 1.2
    nt = sp.edit_tree
    repack(nt)
    yield 0.8
    nodes = list(nt.nodes)
    for n in nodes:
        n.select = True
    reg = region(ne)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.view_selected()
    yield 0.6
    for _ in range(10):
        b = node_box(ne, nodes)
        if (b[2] - b[0]) * 1.3 > 1400 or (b[3] - b[1]) * 1.3 > 700:
            break
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_in()
        yield 0.3
    for _ in range(12):
        b = node_box(ne, nodes)
        if b[2] - b[0] <= 1400 and b[3] - b[1] <= 700:
            break
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_out()
        yield 0.3
    for n in nodes:
        n.select = False
    yield 0.8
    shot("u_group_inside", extra={"NODES_BOX": node_box(ne, nodes)})
    with bpy.context.temp_override(**ov(ne)):
        bpy.ops.node.group_edit(exit=True)
    yield 0.5
    full(False)
    yield 1.2
    ob.active_material = m0
    bpy.data.materials.remove(m1)
    bpy.data.node_groups.remove(g1)
    g0.name = gname


def f_frame():
    activate("E5_Pratique_Socle_corrige")
    yield 0.8
    full(True)
    yield 1.2
    ne = node_area()
    sp = ne.spaces.active
    nt = sp.edit_tree
    mc = next(n for n in nt.nodes if n.type == 'MIX')
    mask = [n for n in nt.nodes if n.location.x < mc.location.x - 10]
    fr = nt.nodes.new("NodeFrame")          # Ctrl + J, fait par l'API : le même cadre
    for n in mask:
        loc = n.location_absolute.copy()
        n.parent = fr
        n.location_absolute = loc
    yield 0.8
    fr.label = "Masque d'usure"
    fr.label_size = 24
    for n in nt.nodes:
        n.select = n is fr
    nt.nodes.active = fr
    sp.show_region_ui = True
    yield 1.0
    try:
        region(ne, 'UI').active_panel_category = 'Node'
    except Exception as e:
        print("CATEGORIE", repr(e))
    # le cadre et ses nœuds sélectionnés : View Selected, deux fois (le cadre prend sa taille au dessin)
    for n in nt.nodes:
        n.select = n is fr or n in mask
    reg = region(ne)
    for _ in range(2):
        win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.node.view_selected()
        yield 0.8
    for _ in range(10):
        b = node_box(ne, [fr])
        if b[2] - b[0] <= 900 and b[3] - b[1] <= 560 and b[0] > reg.x + 10:
            break
        with bpy.context.temp_override(**ov(ne)):
            bpy.ops.view2d.zoom_out()
        yield 0.3
    for n in nt.nodes:
        n.select = n is fr
    nt.nodes.active = fr
    yield 1.0
    shot("u_frame", extra={"NODES_BOX": node_box(ne, [fr])})
    sp.show_region_ui = False
    full(False)
    yield 1.2


def f_outliner():
    o = area('OUTLINER')
    with bpy.context.temp_override(**ov(o)):
        bpy.ops.screen.screen_full_area()
    yield 1.2
    o = area('OUTLINER')
    sp = o.spaces.active
    sp.display_mode = 'LIBRARIES'
    sp.filter_text = "PRC_Usure"
    yield 1.0
    reg = region(o)
    win().cursor_warp(reg.x + reg.width // 2, reg.y + reg.height // 2)
    with bpy.context.temp_override(**ov(o)):
        try:
            bpy.ops.outliner.expanded_toggle()
        except Exception as e:
            print("DEPLIER", repr(e))
    yield 1.0
    shot("u_outliner_recon")
    ry = int(os.environ.get("OUTLINER_ROW", "3"))
    x = reg.x + 455                       # le menu s'ouvre à droite des noms des lignes
    y_img = H - (reg.y + reg.height) + int(20 * UI * (ry - 0.5))
    click(x, y_img)
    yield 0.8
    shot("u_outliner_avant")
    click(x, y_img, 'RIGHTMOUSE')
    yield 1.2
    shot("u_outliner_menu")
    close_popups()
    yield 0.6
    sp.filter_text = ""
    sp.display_mode = 'VIEW_LAYER'
    with bpy.context.temp_override(**ov(o)):
        bpy.ops.screen.back_to_previous()
    yield 1.2


STEPS = [("menus", f_menus), ("preview", f_preview), ("e1", f_noeuds_e1),
         ("e2", f_noeuds_e2), ("e3", f_noeuds_e3), ("e4", f_noeuds_e4), ("e5", f_noeuds_e5), ("e6", f_noeuds_e6),
         ("groupes", f_groupes), ("frame", f_frame), ("outliner", f_outliner)]


def runner():
    for lc in bpy.context.view_layer.layer_collection.children:
        lc.hide_viewport = False
        for k in lc.children:
            k.hide_viewport = False
    yield from set_workspace("Shading")
    for key, fn in STEPS:
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
                if win().screen.show_fullscreen:
                    full(False)
            except Exception:
                pass
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
