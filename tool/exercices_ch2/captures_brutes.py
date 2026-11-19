# Captures brutes (fenêtre entière) des figures 2.1 à 2.32 du chapitre 2.
# Ouvre une VRAIE fenêtre Blender, séparée de celle du formateur, avec une configuration
# temporaire. Rien n'est enregistré : les fichiers .blend ne sont pas modifiés sur le disque.
#
# Usage (PowerShell), depuis la racine du dépôt, verrou tool\production\capture.lock posé :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-captures-ch2"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup --enable-event-simulate `
#       -p 0 0 1600 960 _resources\exercices\PRC02_ch2_lampe_depart.blend `
#       --python tool\exercices_ch2\captures_brutes.py -- <dossier_sortie> [figure ...]
# Les figures 2.6, 2.29 et 2.32 se prennent dans les fichiers 5, 2 et 4 (même commande, autre fichier).
#
# Chaque étape prépare l'interface, attend qu'elle se redessine, puis enregistre la fenêtre entière
# en PNG, avec un JSON qui donne la place des éditeurs (pixels, origine en haut à gauche). Pour un
# menu, une capture « _avant » est prise juste avant de l'ouvrir : recadrer.py isole le menu par
# différence. Les clics simulés (en-têtes de panneaux, menu d'un modificateur) utilisent des
# coordonnées relevées sur une première série de captures.
# Repris de tool/exercices_ch2_defi/captures_brutes.py.

import json
import math
import os
import sys

import bmesh
import bpy
from mathutils import Euler, Matrix, Vector

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = args[0] if args else os.path.join(os.environ.get("TEMP", "."), "captures_ch2")
ONLY = set(args[1:])
os.makedirs(OUT, exist_ok=True)
H = 960

prefs = bpy.context.preferences
prefs.use_preferences_save = False
prefs.view.ui_scale = 1.25
prefs.view.show_tooltips = False
prefs.view.show_splash = False
O = bpy.data.objects


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


def show_collections(names):
    """Affiche les collections de premier niveau nommées, masque les autres (œil)."""
    for lc in bpy.context.view_layer.layer_collection.children:
        lc.hide_viewport = lc.collection.name not in names
        for k in lc.children:
            k.hide_viewport = False


def mode(m):
    if m == 'OBJECT' and bpy.context.mode == 'OBJECT':
        return
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.object.mode_set(mode=m)


def select(names, active=None):
    vl = bpy.context.view_layer
    if bpy.context.mode != 'OBJECT':
        mode('OBJECT')
    for o in vl.objects:
        o.select_set(False)
    for n in names:
        o = O[n]
        o.hide_set(False)
        o.select_set(True)
    vl.objects.active = O[active or names[-1]] if names else None


def deselect_all():
    for o in bpy.context.view_layer.objects:
        o.select_set(False)


def eval_points(names):
    """Sommets évalués (repère monde) : la boîte englobante d'une courbe évaluée n'est pas fiable."""
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for n in names:
        e = O[n].evaluated_get(dg)
        me = e.to_mesh()
        pts += [e.matrix_world @ v.co for v in me.vertices]
        e.to_mesh_clear()
    return pts


def view_on(names, rot=None, axis=None, zoom=1.0, persp='PERSP'):
    """Cadre les objets nommés : une boîte temporaire à leurs dimensions, puis View Selected."""
    pts = eval_points(names)
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    me = bpy.data.meshes.new("_cadre")
    me.from_pydata([(x, y, z) for x in (lo.x, hi.x) for y in (lo.y, hi.y) for z in (lo.z, hi.z)], [], [])
    box = bpy.data.objects.new("_cadre", me)
    bpy.context.scene.collection.objects.link(box)
    prev_mode = bpy.context.mode
    if prev_mode != 'OBJECT':
        mode('OBJECT')
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    box.select_set(True)
    vl.objects.active = box
    r3d = v3d().region_3d
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        if axis:
            bpy.ops.view3d.view_axis(type=axis)
        bpy.ops.view3d.view_selected(use_all_regions=False)
    if rot is not None:
        r3d.view_rotation = Euler([math.radians(a) for a in rot]).to_quaternion()
    r3d.view_perspective = 'ORTHO' if axis else persp
    r3d.view_distance *= zoom
    bpy.data.objects.remove(box)
    bpy.data.meshes.remove(me)


def frame(names, rot=(62, 0, -22), zoom=1.0, persp='PERSP', keep_selection=False):
    view_on(names, rot=rot, zoom=zoom, persp=persp)
    if keep_selection:
        select(names)
    else:
        deselect_all()


def ortho(axis, names, zoom=1.0):
    view_on(names, axis=axis, zoom=zoom)
    select(names)


def shading(color='RANDOM', cavity=True, wire=False, floor=False, light='STUDIO', single=(0.8, 0.8, 0.8)):
    sp = v3d()
    sp.shading.type = 'SOLID'
    sp.shading.light = light
    sp.shading.color_type = color
    sp.shading.single_color = single
    sp.shading.show_cavity = cavity
    sp.shading.show_object_outline = True
    sp.overlay.show_wireframes = wire
    sp.overlay.show_floor = floor
    sp.overlay.show_axis_x = floor
    sp.overlay.show_axis_y = floor
    sp.overlay.show_cursor = False
    sp.overlay.show_text = False
    sp.overlay.show_stats = False
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


def close_popups():
    # Échap referme le menu ou le camembert ouvert ; un aller-retour plein écran, en secours
    w = win()
    w.event_simulate(type='ESC', value='PRESS')
    w.event_simulate(type='ESC', value='RELEASE')


def click(x, y_img):
    w = win()
    y = H - y_img
    w.event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='PRESS', x=x, y=y)
    w.event_simulate(type='LEFTMOUSE', value='RELEASE', x=x, y=y)


def hover(x, y_img):
    win().event_simulate(type='MOUSEMOVE', value='NOTHING', x=x, y=H - y_img)


def rect(a, kind='WINDOW'):
    r = region(a, kind)
    return [r.x, H - (r.y + r.height), r.x + r.width, H - r.y]


def shot(name):
    path = os.path.join(OUT, name + ".png")
    s = win().screen
    info = {}
    for a in s.areas:
        try:
            info[a.type] = rect(a)
        except StopIteration:
            pass
    with bpy.context.temp_override(window=win(), screen=s):
        bpy.ops.screen.screenshot(filepath=path, check_existing=False)
    with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(info, f)
    print("CAPTURE", path)


def layout_for_captures():
    """Générateur : élargit la colonne de droite, ramène l'Outliner à 260 px et réduit la zone LISEZ-MOI.
    screen.area_move est refusé tant que la souris survole une région : curseur sur la bordure."""
    w = win()
    p = area('PROPERTIES')
    w.cursor_warp(p.x - 1, p.y + p.height // 2)
    yield 0.5
    with bpy.context.temp_override(window=w, screen=w.screen):
        bpy.ops.screen.area_move(x=p.x - 1, y=p.y + p.height // 2, delta=-330)
    yield 0.5
    t = area('TEXT_EDITOR')
    w.cursor_warp(t.x + t.width // 2, t.y + t.height + 1)
    yield 0.5
    with bpy.context.temp_override(window=w, screen=w.screen):
        bpy.ops.screen.area_move(x=t.x + t.width // 2, y=t.y + t.height + 1, delta=40 - t.height)
    yield 0.5
    o = area('OUTLINER')
    w.cursor_warp(o.x + o.width // 2, o.y - 1)
    yield 0.5
    with bpy.context.temp_override(window=w, screen=w.screen):
        bpy.ops.screen.area_move(x=o.x + o.width // 2, y=o.y - 1, delta=-(OUTLINER_H - o.height))
    yield 0.5


OUTLINER_H = int(os.environ.get("OUTLINER_H", "260"))


# ---------------------------------------------------------------------------- objets temporaires
def temp_mesh_copy(src, name, matrix):
    ob = O[src].copy()
    ob.data = O[src].data.copy()
    ob.name = name
    bpy.context.scene.collection.objects.link(ob)
    ob.matrix_world = matrix
    return ob


def remove(name):
    if name in O:
        bpy.data.objects.remove(O[name])


def temp_curve(name, pts, types, loc):
    cu = bpy.data.curves.new(name, 'CURVE')
    cu.dimensions = '3D'
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(pts) - 1)
    for bp, p, t in zip(sp.bezier_points, pts, types):
        bp.co = p
        bp.handle_left_type = bp.handle_right_type = t
    ob = bpy.data.objects.new(name, cu)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = loc
    return ob


# ---------------------------------------------------------------------------- section 1
def f201():
    show_collections({"Gabarit", "Lampe"})
    shading('RANDOM')
    frame(["Socle", "Tête", "Articulation_haut"], rot=(66, 0, 38), zoom=1.0)
    yield 1.5
    shot("201_gabarit_copie")


def f202():
    show_collections({"Gabarit", "Lampe"})
    select(["Socle"])
    yield 0.6
    props('MODIFIER')
    yield 0.8
    shot("202_menu_generate_avant")
    call_menu("OBJECT_MT_modifier_add_generate", 'PROPERTIES', at=(0.25, 0.92))
    yield 1.2
    shot("202_menu_generate")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f204():
    show_collections({"Corrigé"})
    o = O["Bras_bas_corrige"]
    select([o.name])
    expand_only(o, {"Mirror"})
    yield 0.6
    props('MODIFIER')
    yield 1.0
    shot("204_panneau_mirror")


def f203():
    # menu de l'en-tête du Mirror : clic sur la flèche (coordonnées relevées sur 204_panneau_mirror)
    show_collections({"Corrigé"})
    o = O["Bras_bas_corrige"]
    select([o.name])
    expand_only(o, {"Mirror"})
    yield 0.6
    props('MODIFIER')
    yield 1.0
    shot("203_menu_entete_avant")
    click(HDR_X, HDR_Y)
    yield 1.2
    shot("203_menu_entete")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f205():
    show_collections({"Corrigé"})
    shading('RANDOM')
    keep = {"Bras_bas_corrige", "Socle_corrige"}
    for o in bpy.data.collections["Corrigé"].objects:
        o.hide_set(o.name not in keep)
    o = O["Bras_bas_corrige"]
    ortho('TOP', [o.name], zoom=0.75)
    select([o.name])
    yield 1.5
    shot("205_tiges_doubles")
    # le piège : la tige non décalée, déplacée de 10 mm en Mode Objet, avec un Mirror sur Y
    t = temp_mesh_copy("Bras_bas_A", "Piege", O["Bras_bas_A"].matrix_world.copy())
    t.display_type = 'SOLID'
    t.hide_select = False
    for v in t.data.vertices:
        v.co.x *= 0.5
        v.co.y *= 0.5
    t.location.y += 0.010
    m = t.modifiers.new("Mirror", 'MIRROR')
    m.use_axis = (False, True, False)
    o.hide_set(True)
    select([t.name])
    yield 1.5
    shot("205_piege_origine")
    remove("Piege")
    for o in bpy.data.collections["Corrigé"].objects:
        o.hide_set(False)


def f207():
    show_collections({"Lampe"})
    shading('RANDOM')
    o = O["Tête"]
    frame([o.name], rot=(115, 0, -50), zoom=1.25)
    select([o.name])
    mode('EDIT')
    bpy.context.tool_settings.mesh_select_mode = (False, False, True)
    bm = bmesh.from_edit_mesh(o.data)
    big = min(bm.faces, key=lambda f: f.calc_center_median().z)
    for f in bm.faces:
        f.select = f is big
    bm.select_flush_mode()
    bmesh.update_edit_mesh(o.data)
    yield 1.0
    shot("207_menu_delete_avant")
    call_menu("VIEW3D_MT_edit_mesh_delete", at=(0.62, 0.62))
    yield 1.2
    shot("207_menu_delete")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5
    mode('OBJECT')


def f208():
    show_collections({"Corrigé"})
    o = O["Tête_corrige"]
    select([o.name])
    expand_only(o, {"Solidify"})
    yield 0.6
    props('MODIFIER')
    yield 1.0
    shot("208_panneau_solidify")


def f209():
    show_collections({"Corrigé"})
    shading('RANDOM')
    O["Ampoule_corrige"].hide_set(True)
    frame(["Tête_corrige"], rot=(150, 0, 50), zoom=0.95)
    yield 1.5
    shot("209_tete_dessous")
    t = O["Tête_corrige"]
    r3d = v3d().region_3d
    # le bord vu de l'extérieur et d'un peu plus bas : la tranche de 1,5 mm se lit
    P = t.matrix_world @ Vector((0.0, -0.0600, -0.055))
    cam = t.matrix_world @ Vector((0.0, -0.0600 - 0.5, -0.055 - 0.35))
    r3d.view_perspective = 'PERSP'
    r3d.view_location = P
    r3d.view_rotation = (P - cam).to_track_quat('-Z', 'Y')
    r3d.view_distance = 0.035
    yield 1.5
    shot("209_bord_coque")
    O["Ampoule_corrige"].hide_set(False)


def f210():
    show_collections({"Corrigé"})
    o = O["Socle_corrige"]
    select([o.name])
    expand_only(o, {"Bevel"})
    yield 0.6
    props('MODIFIER')
    yield 1.0
    shot("210_panneau_bevel")


def f211():
    show_collections({"Lampe"})
    select(["Tête"])
    yield 0.6
    shot("211_menu_object_avant")
    call_menu("VIEW3D_MT_object", at=(0.30, 0.95))
    yield 1.0
    hover(*SHADE_AUTO)
    yield 1.0
    shot("211_menu_object")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f212():
    show_collections({"Corrigé"})
    shading('SINGLE', cavity=False)
    o = O["Tête_corrige"]
    select([o.name])
    expand_only(o, set())
    yield 0.6
    props('MODIFIER')
    for k in ("Ampoule_corrige", "Douille_corrige"):
        O[k].hide_set(True)
    frame([o.name], rot=(68, 0, 40), zoom=0.9)
    select([o.name])
    yield 1.2
    shot("212_pile_lisse")
    sm = o.modifiers["Smooth by Angle"]
    sm.show_viewport = False
    flags = [p.use_smooth for p in o.data.polygons]
    for p in o.data.polygons:
        p.use_smooth = False
    o.data.update()
    yield 1.2
    shot("212_facettes")
    sm.show_viewport = True
    for p, f in zip(o.data.polygons, flags):
        p.use_smooth = f
    o.data.update()
    for k in ("Ampoule_corrige", "Douille_corrige"):
        O[k].hide_set(False)


def f213():
    show_collections({"Lampe"})
    deselect_all()
    yield 0.6
    shot("213_menu_empty_avant")
    call_menu("VIEW3D_MT_empty_add", at=(0.40, 0.80))
    yield 1.2
    shot("213_menu_empty")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f214():
    show_collections({"Corrigé"})
    o = O["Grille_aeration_corrige"]
    select([o.name])
    expand_only(o, {"Array"})
    yield 0.6
    props('MODIFIER')
    yield 1.0
    for (x, y) in ARRAY_CLICKS:
        click(x, y)
        yield 0.8
    shot("214_panneau_array")


def f215():
    show_collections({"Corrigé"})
    shading('RANDOM')
    p = O["Grille_pivot_corrige"]
    size = p.empty_display_size
    p.empty_display_size = 0.11
    p.show_in_front = True
    ortho('TOP', ["Socle_corrige"], zoom=1.15)
    select([p.name])
    yield 1.5
    shot("215_couronne_grille")
    p.empty_display_size = size
    p.show_in_front = False


def f216():
    show_collections({"Corrigé"})
    shading('RANDOM')
    frame(["Socle_corrige"], rot=(55, 0, 30), zoom=1.0)
    select(["Grille_pivot_corrige", "Grille_aeration_corrige"], active="Grille_aeration_corrige")
    yield 0.8
    shot("216_menu_parent_avant")
    a, _x, _y = warp('VIEW_3D', (0.55, 0.55))
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.object.parent_set('INVOKE_DEFAULT')
    yield 1.2
    shot("216_menu_parent")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f217():
    show_collections({"Corrigé"})
    shading('RANDOM')
    frame(["Interrupteur_crans_corrige"], rot=(50, 0, 25), zoom=1.6)
    yield 1.5
    shot("217_molette_crans")


# ---------------------------------------------------------------------------- section 2
def f218():
    show_collections({"Lampe"})
    deselect_all()
    yield 0.6
    shot("218_menu_curve_avant")
    call_menu("VIEW3D_MT_curve_add", at=(0.40, 0.80))
    yield 1.2
    shot("218_menu_curve")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


ANAT = "Anatomie"


def anatomy_curve():
    remove(ANAT)
    pts = [(0, 0, 0), (0.08, 0, 0.06), (0.17, 0, 0.01), (0.25, 0, 0.07)]
    ob = temp_curve(ANAT, pts, ['VECTOR', 'AUTO', 'ALIGNED', 'FREE'], (1.0, 0, 0.2))
    sp = ob.data.splines[0]
    b = sp.bezier_points
    b[2].handle_left = (0.135, 0, -0.01)
    b[2].handle_right = (0.205, 0, 0.03)
    b[3].handle_left = (0.215, 0, 0.11)
    b[3].handle_right = (0.29, 0, 0.09)
    ob.data.resolution_u = 24
    return ob


def f219():
    show_collections(set())
    shading('RANDOM')
    ob = anatomy_curve()
    ortho('FRONT', [ob.name], zoom=1.15)
    select([ob.name])
    mode('EDIT')
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.curve.select_all(action='SELECT')
    v3d().overlay.display_handle = 'ALL'
    yield 1.5
    shot("219_anatomie")
    # positions à l'écran des points et des poignées, pour les étiquettes de la figure
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    a = area('VIEW_3D')
    r = region(a)
    r3d = v3d().region_3d
    pts = []
    for bp in ob.data.splines[0].bezier_points:
        row = {}
        for k in ('co', 'handle_left', 'handle_right'):
            p2 = location_3d_to_region_2d(r, r3d, ob.matrix_world @ getattr(bp, k))
            row[k] = [round(r.x + p2.x), round(H - (r.y + p2.y))]
        row['type'] = bp.handle_left_type
        pts.append(row)
    with open(os.path.join(OUT, "219_anatomie_points.json"), "w", encoding="utf-8") as f:
        json.dump(pts, f)


def f220():
    ob = O[ANAT] if ANAT in O else anatomy_curve()
    show_collections(set())
    if bpy.context.mode != 'EDIT_CURVE':
        ortho('FRONT', [ob.name], zoom=1.3)
        select([ob.name])
        mode('EDIT')
    yield 0.6
    shot("220_menu_handle_avant")
    a, _x, _y = warp('VIEW_3D', (0.62, 0.62))
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.curve.handle_type_set('INVOKE_DEFAULT')
    yield 1.2
    shot("220_menu_handle")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f221():
    ob = O[ANAT] if ANAT in O else anatomy_curve()
    show_collections(set())
    if bpy.context.mode != 'EDIT_CURVE':
        ortho('FRONT', [ob.name], zoom=1.3)
        select([ob.name])
        mode('EDIT')
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.wm.tool_set_by_id(name="builtin.pen")
    yield 1.2
    shot("221_curve_pen")
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.wm.tool_set_by_id(name="builtin.select_box")
    mode('OBJECT')
    remove(ANAT)


def f222():
    show_collections({"Corrigé"})
    select(["Câble_corrige"])
    yield 0.6
    props('DATA')
    yield 1.0
    shot("222_onglet_data_courbe")


def f223():
    # rubrique Geometry et sous-rubrique Bevel : dépliées par clics (coordonnées relevées sur 222)
    show_collections({"Corrigé"})
    select(["Câble_corrige"])
    yield 0.6
    props('DATA')
    yield 1.0
    for (x, y) in GEO_CLICKS:
        click(x, y)
        yield 0.8
    shot("223_geometry_bevel")


def f224():
    show_collections({"Corrigé"})
    shading('RANDOM', floor=True)
    frame(["Câble_corrige", "Socle_corrige"], rot=(62, 0, -52), zoom=0.8)
    yield 1.5
    shot("224_cable")
    v3d().overlay.show_floor = False


def f225():
    show_collections({"Lampe"})
    select(["Tête"])
    yield 0.6
    shot("225_pie_snap_avant")
    a, _x, _y = warp('VIEW_3D', (0.5, 0.5))
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.call_menu_pie('INVOKE_DEFAULT', name="VIEW3D_MT_snap_pie")
    yield 1.2
    shot("225_pie_snap")
    close_popups()
    yield 0.5
    close_popups()
    yield 0.5


def f226():
    show_collections({"Corrigé"})
    select(["Ampoule_corrige"])
    yield 0.6
    props('MODIFIER')
    yield 1.0
    shot("226_panneau_screw")


def f227():
    show_collections({"Croquis"})
    shading('RANDOM')
    src = O["Ampoule_corrige"]
    ob = src.copy()
    ob.data = src.data.copy()
    ob.name = "Ampoule_demo"
    bpy.context.scene.collection.objects.link(ob)
    ob.matrix_world = Matrix.Translation((0.5, 0, 0))
    sc = ob.modifiers["Screw"]
    sc.show_in_editmode = False
    ortho('FRONT', [ob.name], zoom=1.05)
    select([ob.name])
    mode('EDIT')
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.curve.select_all(action='SELECT')
    v3d().overlay.display_handle = 'ALL'
    yield 1.5
    shot("227_profil")
    mode('OBJECT')
    show_collections(set())
    deselect_all()
    yield 1.2
    shot("227_ampoule")
    sc.merge_threshold = 0.01
    yield 1.2
    shot("227_sommet_aplati")
    remove("Ampoule_demo")


# ---------------------------------------------------------------------------- section 3
def f228():
    show_collections({"Gabarit", "Corrigé"})
    shading('RANDOM')
    ortho('FRONT', ["Socle_corrige", "Tête_corrige", "Câble_corrige"], zoom=1.0)
    deselect_all()
    yield 1.5
    shot("228_gabarit_face")
    frame(["Socle_corrige", "Tête_corrige", "Câble_corrige"], rot=(66, 0, 38), zoom=0.95)
    yield 1.5
    shot("228_gabarit_perspective")


def f230():
    show_collections({"Corrigé"})
    shading('SINGLE', cavity=True, single=(0.82, 0.82, 0.84))
    frame(["Socle_corrige", "Tête_corrige", "Câble_corrige"], rot=(70, 0, 32), zoom=0.9)
    yield 1.5
    shot("230_lampe_finale")


def f231():
    show_collections({"Corrigé défis"})
    o = O["Socle_percage"]
    select([o.name])
    expand_only(o, {"Boolean"})
    yield 0.6
    props('MODIFIER')
    yield 1.0
    shot("231_panneau_boolean")


# ---------------------------------------------------------------------------- autres fichiers
def f206():
    # fichier 5 : la moitié de capot, en Mode Édition, et son panneau Mirror
    o = O["Capot_moitie"]
    shading('OBJECT')
    frame([o.name], rot=(58, 0, 28), zoom=1.0)
    select([o.name])
    expand_only(o, {"Mirror"})
    yield 0.6
    props('MODIFIER')
    mode('EDIT')
    yield 1.5
    shot("206_capot_edition")
    mode('OBJECT')


def f229():
    # fichier 2 : l'Outliner de la lampe modélisée, collection Lampe dépliée
    select(["Bras_bas"])
    yield 1.0
    shot("229_outliner")


def f232():
    # fichier 4 : la liseuse finie, sur sa paroi
    show_collections({"Contexte", "Corrigé"})
    shading('RANDOM')
    deselect_all()
    eye, target = Vector((0.30, -0.50, 0.30)), Vector((0.0, -0.13, 0.18))
    r3d = v3d().region_3d
    r3d.view_perspective = 'PERSP'
    r3d.view_location = target
    r3d.view_rotation = (target - eye).to_track_quat('-Z', 'Y')
    r3d.view_distance = (target - eye).length * 0.95
    yield 1.5
    shot("232_liseuse")


HDR_X, HDR_Y = [int(v) for v in os.environ.get("HDR_XY", "1513,435").split(",")]
SHADE_AUTO = tuple(int(v) for v in os.environ.get("SHADE_AUTO", "219,639").split(","))
ARRAY_CLICKS = [(1065, 700), (1065, 543)]   # Object Offset : déplier ; Relative Offset : replier
GEO_CLICKS = [tuple(int(v) for v in p.split(",")) for p in os.environ.get("GEO_CLICKS", "").split(";") if p]

STEPS_FILE1 = [("201", f201), ("202", f202), ("204", f204), ("203", f203), ("205", f205), ("207", f207),
               ("208", f208), ("209", f209), ("210", f210), ("211", f211), ("212", f212), ("213", f213),
               ("214", f214), ("215", f215), ("216", f216), ("217", f217), ("218", f218), ("219", f219),
               ("220", f220), ("221", f221), ("222", f222), ("223", f223), ("224", f224), ("225", f225),
               ("226", f226), ("227", f227), ("228", f228), ("230", f230), ("231", f231)]
STEPS_OTHER = {"PRC02_ch2_demos_secteurs.blend": [("206", f206)],
               "PRC02_ch2_lampe_modele.blend": [("229", f229)],
               "PRC02_ch2_liseuse_depart.blend": [("232", f232)]}


def runner():
    yield from layout_for_captures()
    base = os.path.basename(bpy.data.filepath)
    steps = STEPS_OTHER.get(base, STEPS_FILE1)
    for key, fn in steps:
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
bpy.app.timers.register(lambda: os._exit(2), first_interval=600.0)   # sécurité : quitte toujours
