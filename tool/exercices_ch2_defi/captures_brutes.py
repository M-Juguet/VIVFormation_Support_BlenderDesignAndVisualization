# Captures brutes (fenêtre entière) pour les figures du défi de modélisation.
# Ouvre une VRAIE fenêtre Blender, séparée de celle du formateur, avec une configuration
# temporaire. Rien n'est enregistré : le fichier .blend n'est pas modifié sur le disque.
#
# Usage (PowerShell), depuis la racine du dépôt :
#   $env:BLENDER_USER_CONFIG = "$env:TEMP\blender-cfg-captures"
#   & "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --factory-startup -p 0 0 1600 960 `
#       _resources\exercices\PRC02_ch2_defi_modelisation.blend `
#       --python tool\exercices_ch2_defi\captures_brutes.py -- <dossier_sortie> [figure ...]
#
# Chaque étape prépare l'interface, attend qu'elle se redessine, puis enregistre la fenêtre
# entière en PNG. Le recadrage se fait ensuite avec recadrer.py.

import math
import os
import sys

import bpy
from mathutils import Euler, Vector

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = args[0] if args else os.path.join(os.environ.get("TEMP", "."), "captures_defi")
ONLY = set(args[1:])
os.makedirs(OUT, exist_ok=True)

prefs = bpy.context.preferences
prefs.use_preferences_save = False
prefs.view.ui_scale = 1.25
prefs.view.show_tooltips = False
prefs.view.show_splash = False


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
    lc = bpy.context.view_layer.layer_collection
    for c in lc.children:
        if c.collection.name == "Surfaces_reference":
            continue
        c.hide_viewport = c.collection.name not in names
        if c.collection.name == "Corrigé défi modélisation":
            c.hide_viewport = not any(n.startswith("Corrigé") for n in names)
            for k in c.children:
                k.hide_viewport = k.collection.name not in names


def select(names, active=None):
    vl = bpy.context.view_layer
    if bpy.context.mode != 'OBJECT':
        with bpy.context.temp_override(**ov(area('VIEW_3D'))):
            bpy.ops.object.mode_set(mode='OBJECT')
    for o in vl.objects:
        o.select_set(False)
    for n in names:
        o = bpy.data.objects[n]
        o.hide_set(False)
        o.select_set(True)
    vl.objects.active = bpy.data.objects[active or names[0]]


def frame(names, rot=(62, 0, -22), zoom=1.0, persp='PERSP'):
    select(names)
    sp = v3d()
    r3d = sp.region_3d
    r3d.view_perspective = persp
    r3d.view_rotation = Euler([math.radians(a) for a in rot]).to_quaternion()
    a = area('VIEW_3D')
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.view3d.view_selected(use_all_regions=False)
    r3d.view_distance *= zoom
    # pas de contour de sélection sur les captures ; l'objet actif reste celui des propriétés
    for o in bpy.context.view_layer.objects:
        o.select_set(False)


def layout_for_captures():
    """Générateur : élargit la colonne de droite et réduit la zone LISEZ-MOI.
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


def shading(kind='SOLID', matcap=None, cavity=True, wire=False, outline=True):
    sp = v3d()
    sp.shading.type = kind
    if kind == 'SOLID':
        sp.shading.light = 'MATCAP' if matcap else 'STUDIO'
        if matcap:
            sp.shading.studio_light = matcap
        sp.shading.color_type = 'MATERIAL'
        sp.shading.show_cavity = cavity
        sp.shading.show_object_outline = outline
    sp.overlay.show_wireframes = wire
    sp.overlay.show_floor = False
    sp.overlay.show_axis_x = False
    sp.overlay.show_axis_y = False
    sp.overlay.show_cursor = False
    sp.overlay.show_text = False
    sp.overlay.show_stats = False
    sp.show_gizmo_navigate = False


def props(context):
    a = area('PROPERTIES')
    a.spaces.active.context = context
    return a


def mode(m):
    with bpy.context.temp_override(**ov(area('VIEW_3D'))):
        bpy.ops.object.mode_set(mode=m)


def call_menu(name, a_kind='VIEW_3D', at=(0.35, 0.75)):
    a = area(a_kind)
    w = win()
    x = int(a.x + a.width * at[0])
    y = int(a.y + a.height * at[1])
    w.cursor_warp(x, y)
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.call_menu('INVOKE_DEFAULT', name=name)


def call_enum_menu(data_path, a_kind='PROPERTIES', at=(0.5, 0.6)):
    a = area(a_kind)
    w = win()
    w.cursor_warp(int(a.x + a.width * at[0]), int(a.y + a.height * at[1]))
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.wm.context_menu_enum('INVOKE_DEFAULT', data_path=data_path)


def close_popups():
    # un aller-retour plein écran referme les menus ouverts
    a = area('VIEW_3D')
    with bpy.context.temp_override(**ov(a)):
        bpy.ops.screen.screen_full_area()


def shot(name):
    path = os.path.join(OUT, name + ".png")
    with bpy.context.temp_override(window=win(), screen=win().screen):
        bpy.ops.screen.screenshot(filepath=path, check_existing=False)
    print("CAPTURE", path)


def add_mod(obj, kind, name=None, **kw):
    m = obj.modifiers.new(name or kind.title(), kind)
    for k, v in kw.items():
        setattr(m, k, v)
    return m


O = bpy.data.objects


# ---------------------------------------------------------------------------- les étapes
# Chaque fonction est un générateur : elle prépare, rend la main (yield délai), puis capture.
def f233():
    show_collections({"Etape_1_Subdivision", "Etape_2_Shrinkwrap", "Etape_3_Cas_usage", "Etape_4_Reglages",
                      "Etape_5_Booleens", "Etape_6_Normales", "Atelier_Retroviseur"})
    shading('SOLID')
    frame([o.name for o in bpy.context.view_layer.objects if o.type == 'MESH' and o.visible_get()
           and o.display_type not in ('WIRE', 'BOUNDS')], rot=(55, 0, -30), zoom=0.9)
    yield 1.5
    shot("233_overview")


def f234():
    show_collections({"Etape_1_Subdivision"})
    shading('SOLID', matcap='check_reflection_horizontal.exr', cavity=False)
    frame(["E1_Exemple_Sans", "E1_Exemple_Boucles", "E1_Exemple_Crease"], rot=(60, 0, -15), zoom=0.8)
    yield 1.5
    shot("234_carters_matcap")
    shading('SOLID')
    yield 1.0
    shot("234_carters_studio")


def f235():
    show_collections({"Corrigé étape 1"})
    shading('SOLID')
    o = O["E1_Pratique_Boucles_corrige"]
    frame([o.name], rot=(65, 0, -30), zoom=0.9)
    mode('EDIT')
    bpy.context.tool_settings.mesh_select_mode = (False, True, False)
    me = o.data
    import bmesh
    bm = bmesh.from_edit_mesh(me)
    for e in bm.edges:
        a, b = e.verts[0].co, e.verts[1].co
        e.select = abs(a.z - 0.016) < 1e-5 and abs(b.z - 0.016) < 1e-5
    bm.select_flush_mode()
    bmesh.update_edit_mesh(me)
    v3d().overlay.show_wireframes = False
    yield 1.5
    shot("235_boucle_maintien_edition")
    mode('OBJECT')


def f236():
    show_collections({"Etape_1_Subdivision"})
    shading('SOLID')
    frame(["E1_Pratique_Crease"], rot=(65, 0, -30), zoom=1.3)
    mode('EDIT')
    yield 0.8
    call_menu("VIEW3D_MT_edit_mesh_edges", at=(0.55, 0.85))
    yield 1.2
    shot("236_menu_edge_crease")
    close_popups()
    yield 0.6
    close_popups()
    yield 0.6
    mode('OBJECT')


def f237():
    show_collections({"Etape_1_Subdivision"})
    select(["E1_Pratique_Crease"])
    props('MODIFIER')
    yield 1.2
    shot("237_panneau_subdivision")


def f238():
    show_collections({"Etape_1_Subdivision", "Corrigé étape 1"})
    shading('SOLID', matcap='check_reflection_horizontal.exr', cavity=False)
    k = O["E1_Defi_Capot_corrige"]
    k.location.x += 0.75
    frame(["E1_Defi_Capot", k.name], rot=(58, 0, -10), zoom=0.85)
    yield 1.5
    shot("238_capot_crease")
    k.location.x -= 0.75
    shading('SOLID')


def f239():
    show_collections({"Etape_2_Shrinkwrap"})
    shading('SOLID')
    others = [O[n] for n in ("E2_Nez", "E2_Capot", "E2_Pratique_Plaque", "E2_Defi_Monogramme", "Titre_Etape_2_Shrinkwrap")]
    # de profil, le long du fuselage : la trappe plate décolle à ses bords
    for o in others + [O["E2_Exemple_Trappe"]]:
        o.hide_set(True)
    shading('SOLID', wire=True)
    f2 = O["E2_Fuselage"]
    top = f2.matrix_world @ Vector((0.0, 0.0, 0.075))     # bord haut de la trappe, au droit du fuselage

    def zoom_on_edge():
        r3d = v3d().region_3d
        r3d.view_location = top
        r3d.view_distance = 0.07
    frame(["E2_Exemple_Trappe_plate"], rot=(90, 0, -90), persp='ORTHO')
    zoom_on_edge()
    yield 1.5
    shot("239_trappe_plate_profil")
    O["E2_Exemple_Trappe"].hide_set(False)
    O["E2_Exemple_Trappe_plate"].hide_set(True)
    frame(["E2_Exemple_Trappe"], rot=(90, 0, -90), persp='ORTHO')
    zoom_on_edge()
    yield 1.5
    shot("239_trappe_conformee_profil")
    shading('SOLID')
    for o in others + [O["E2_Exemple_Trappe_plate"]]:
        o.hide_set(False)
    frame(["E2_Exemple_Trappe_plate", "E2_Exemple_Trappe"], rot=(80, 0, -20), zoom=1.3)
    yield 1.2
    shot("239_trappes_face")


def f240():
    show_collections({"Etape_2_Shrinkwrap"})
    select(["E2_Pratique_Plaque"])
    props('MODIFIER')
    yield 0.8
    call_menu("OBJECT_MT_modifier_add_deform", a_kind='PROPERTIES', at=(0.15, 0.80))
    yield 1.2
    shot("240_menu_deform")
    close_popups()
    yield 0.6
    close_popups()
    yield 0.6


def f241():
    show_collections({"Etape_2_Shrinkwrap"})
    p = O["E2_Pratique_Plaque"]
    select([p.name])
    m = add_mod(p, 'SHRINKWRAP', "Shrinkwrap", target=O["E2_Nez"])
    props('MODIFIER')
    shading('SOLID')
    frame([p.name], rot=(80, 0, -25), zoom=2.0)
    yield 1.5
    shot("241_panneau_shrinkwrap")
    # 2.42 : Offset 0 (scintillement), puis 0,2 mm
    shading('MATERIAL')
    frame([p.name], rot=(78, 0, -20), zoom=1.2)
    yield 3.0
    shot("242_offset_0")
    m.offset = 0.0002
    yield 2.0
    shot("242_offset_02")
    # 2.43 : Solidify en dessous, puis au-dessus
    shading('SOLID')
    s = add_mod(p, 'SOLIDIFY', "Solidify", thickness=0.002, offset=1.0)
    frame([p.name], rot=(70, 0, -55), zoom=0.9)
    yield 1.5
    shot("243_pile_solidify_dessous")
    p.modifiers.move(p.modifiers.find("Solidify"), 0)
    yield 1.5
    shot("243_pile_solidify_dessus")
    p.modifiers.clear()


def f244():
    show_collections({"Etape_3_Cas_usage"})
    p = O["E3_Pratique_Cadre"]
    select([p.name])
    add_mod(p, 'SHRINKWRAP', "Shrinkwrap", target=O["E3_Fuselage"], offset=0.0002)
    props('MODIFIER')
    yield 0.8
    call_enum_menu('object.modifiers["Shrinkwrap"].wrap_mode', at=(0.55, 0.62))
    yield 1.2
    shot("244_menu_snap_mode")
    close_popups()
    yield 0.6
    close_popups()
    yield 0.6
    # 2.45 : On Surface puis Above Surface, avec épaisseur
    m = p.modifiers["Shrinkwrap"]
    add_mod(p, 'SOLIDIFY', "Solidify", thickness=0.004, offset=1.0)
    shading('SOLID')
    frame([p.name], rot=(88, 0, -12), zoom=1.3)
    yield 1.5
    shot("245_cadre_on_surface")
    m.wrap_mode = 'ABOVE_SURFACE'
    yield 1.5
    shot("245_cadre_above_surface")
    p.modifiers.clear()


def f246():
    show_collections({"Etape_3_Cas_usage"})
    p = O["E3_Pratique_Bandeau"]
    select([p.name])
    m = add_mod(p, 'SHRINKWRAP', "Shrinkwrap", target=O["E3_Nez"], offset=0.0002)
    props('MODIFIER')
    shading('SOLID')
    frame(["E3_Nez"], rot=(90, 0, 0), zoom=0.75, persp='ORTHO')
    bpy.context.view_layer.objects.active = p     # les propriétés montrent le bandeau
    yield 1.5
    shot("247_bandeau_nearest_face")
    m.wrap_method = 'PROJECT'
    m.use_project_y = True
    yield 1.5
    shot("246_panneau_project")
    shot("247_bandeau_project_face")
    p.modifiers.clear()


def f248():
    show_collections({"Etape_3_Cas_usage"})
    p = O["E3_Pratique_Prise"]
    shading('SOLID')
    frame([p.name], rot=(55, 0, -20), zoom=1.4)
    mode('EDIT')
    bpy.context.tool_settings.mesh_select_mode = (True, False, False)
    yield 1.0
    call_menu("VIEW3D_MT_vertex_group", at=(0.6, 0.7))
    yield 1.2
    shot("248_menu_ctrl_g")
    close_popups()
    yield 0.6
    close_popups()
    yield 0.6
    g = p.vertex_groups.new(name="Raccord")
    p.vertex_groups.active_index = g.index
    props('DATA')
    yield 1.5
    shot("249_panneau_vertex_groups")
    mode('OBJECT')
    p.vertex_groups.remove(g)


def f250():
    show_collections({"Etape_3_Cas_usage", "Corrigé étape 3"})
    shading('SOLID')
    # sans groupe : copie temporaire aplatie, à gauche de l'exemple
    p = O["E3_Pratique_Prise"]
    k = O["E3_Pratique_Prise_corrige"]
    p.location.x -= 0.0
    m = add_mod(p, 'SHRINKWRAP', "Shrinkwrap", target=O["E3_Capot"], offset=0.0)
    add_mod(p, 'SOLIDIFY', "Solidify", thickness=0.002, offset=-1.0)
    p.location.x -= 0.0
    for o in (O["E3_Exemple_Prise"], k):
        o.hide_set(False)
    # on décale : pratique aplatie à gauche, corrigé (poids 1 et 0,5) au centre, exemple dégradé à droite
    ex = O["E3_Exemple_Prise"]
    moves = ((p, -0.53), (k, -0.20), (ex, 0.53))
    for o, dx in moves:
        o.location.x += dx
    frame([p.name, k.name, ex.name], rot=(52, 0, -6), zoom=0.62)
    yield 2.0
    shot("250_trois_prises")
    for o, dx in moves:
        o.location.x -= dx
    p.modifiers.clear()


def f251():
    show_collections({"Etape_4_Reglages"})
    shading('SOLID', wire=True)
    frame(["E4_Main_courante"], rot=(90, 0, 90), zoom=0.55, persp='ORTHO')
    yield 1.5
    shot("251_quatre_modes_bout")
    frame(["E4_Exemple_Mode_1", "E4_Exemple_Mode_4", "E4_Main_courante"], rot=(35, 0, 0), zoom=0.9)
    yield 1.5
    shot("251_quatre_modes_dessus")
    shading('SOLID')


def f252():
    show_collections({"Etape_4_Reglages"})
    p = O["E4_Pratique_Cadre_8"]
    shading('SOLID', wire=True)
    m = add_mod(p, 'SHRINKWRAP', "Shrinkwrap", target=O["E4_Fuselage"], offset=0.0002, wrap_mode='ABOVE_SURFACE')
    frame([p.name], rot=(80, 0, -35), zoom=1.15)
    yield 1.5
    shot("252_cadre8_seul")
    s = add_mod(p, 'SUBSURF', "Subdivision", levels=3, subdivision_type='SIMPLE')
    p.modifiers.move(p.modifiers.find("Subdivision"), 0)
    yield 1.5
    shot("252_cadre8_simple_dessus")
    s.subdivision_type = 'CATMULL_CLARK'
    s.levels = 2
    p.modifiers.move(p.modifiers.find("Subdivision"), 1)
    yield 1.5
    shot("252_cadre8_cc_dessous")
    p.modifiers.clear()
    shading('SOLID')


# ---------------------------------------------------------------------------- palier 2 et atelier
def open_object_panels():
    """Les rubriques Viewport Display et Visibility de l'onglet Object sont repliées par défaut,
    et Python ne peut pas déplier un panneau. On les réenregistre ouvertes, Transform repliée,
    avant le premier affichage de l'onglet Object dans cette session."""
    for name, closed in (("OBJECT_PT_transform", True), ("OBJECT_PT_display", False), ("OBJECT_PT_visibility", False)):
        cls = getattr(bpy.types, name, None)
        if cls is None:
            continue
        try:
            bpy.utils.unregister_class(cls)
            opts = set(getattr(cls, "bl_options", set()))
            opts = (opts | {'DEFAULT_CLOSED'}) if closed else (opts - {'DEFAULT_CLOSED'})
            cls.bl_options = opts
            bpy.utils.register_class(cls)
        except Exception as e:
            print("PANNEAU", name, e)


def collapse_modifiers(o, keep):
    for m in o.modifiers:
        m.show_expanded = m.name in keep


def f253():
    show_collections({"Etape_5_Booleens"})
    f = O["E5_Pratique_Fuselage"]
    cut = O["E5_Coupe_Hublot"]
    b = add_mod(f, 'BOOLEAN', "Boolean", object=cut)
    select([f.name])
    collapse_modifiers(f, {"Boolean"})
    props('MODIFIER')
    shading('SOLID')
    frame([cut.name], rot=(80, 0, -25), zoom=1.6)
    bpy.context.view_layer.objects.active = f
    yield 1.5
    shot("253_panneau_boolean")
    # 2.54 et 2.55 : l'objet de coupe, Display As et Renders
    bpy.context.view_layer.objects.active = cut
    cut.display_type = 'WIRE'
    cut.hide_render = True
    props('OBJECT')
    yield 1.5
    shot("254_object_display_visibility")
    # 2.56 : Bevel sous le Boolean, puis au-dessus
    bv = add_mod(f, 'BEVEL', "Bevel", width=0.001, segments=3, limit_method='ANGLE')
    shading('SOLID', matcap='check_reflection_horizontal.exr', cavity=False)
    frame([cut.name], rot=(78, 0, -28))
    r3d = v3d().region_3d
    # gros plan sur le bord haut de la découpe (230 x 330 mm, centrée sur l'origine du fuselage)
    r3d.view_location = f.matrix_world @ Vector((0.0, 0.0, 0.13))
    r3d.view_distance = 0.22
    bpy.context.view_layer.objects.active = f
    cut.hide_set(True)
    yield 1.5
    shot("256_bevel_dessous")
    f.modifiers.move(f.modifiers.find("Bevel"), f.modifiers.find("Boolean"))
    yield 1.5
    shot("256_bevel_dessus")
    f.modifiers.remove(f.modifiers["Bevel"])
    f.modifiers.remove(f.modifiers["Boolean"])
    cut.hide_set(False)
    cut.display_type = 'SOLID'
    cut.hide_render = False
    collapse_modifiers(f, {m.name for m in f.modifiers})
    shading('SOLID')


def f257():
    show_collections({"Etape_5_Booleens", "Corrigé étape 5"})
    n = O["E5_Defi_Nez_corrige"]
    c = O["E5_Defi_Coupe_Joint_corrige"]
    for o in (O["E5_Defi_Nez"], O["E5_Defi_Coupe_Joint"]):
        o.hide_set(True)
    shading('SOLID', wire=False)
    frame([c.name], rot=(78, 0, -20), zoom=1.3)
    select([c.name])
    collapse_modifiers(c, {"Shrinkwrap"})
    props('MODIFIER')
    bpy.context.view_layer.objects.active = c
    c.select_set(True)
    yield 1.5
    shot("257_coupe_sur_reference")
    for o in (O["E5_Defi_Nez"], O["E5_Defi_Coupe_Joint"]):
        o.hide_set(False)


def f258():
    show_collections({"Etape_6_Normales"})
    shading('SOLID', matcap='check_reflection_horizontal.exr', cavity=False)
    for nm in ("E6_Exemple_Brut", "E6_Exemple_Propre"):
        o = O[nm]
        frame([nm.replace("Exemple_", "Exemple_") + "_Coupe" if False else nm], rot=(80, 0, -30), zoom=1.0)
        r3d = v3d().region_3d
        r3d.view_location = o.matrix_world @ Vector((0, 0, 0))
        r3d.view_distance = 0.75
        yield 1.5
        shot("258_" + nm.split("_")[-1].lower())
    shading('SOLID')


def f259():
    show_collections({"Etape_6_Normales"})
    select(["E6_Pratique_Fuselage"])
    props('MODIFIER')
    collapse_modifiers(O["E6_Pratique_Fuselage"], set())
    yield 0.8
    call_menu("OBJECT_MT_modifier_add_edit", a_kind='PROPERTIES', at=(0.15, 0.80))
    yield 1.2
    shot("259_menu_edit")
    close_popups()
    yield 0.6
    close_popups()
    yield 0.6
    call_menu("OBJECT_MT_modifier_add_normals", a_kind='PROPERTIES', at=(0.15, 0.80))
    yield 1.2
    shot("262_menu_normals")
    close_popups()
    yield 0.6
    close_popups()
    yield 0.6
    collapse_modifiers(O["E6_Pratique_Fuselage"], {m.name for m in O["E6_Pratique_Fuselage"].modifiers})


def f260():
    show_collections({"Etape_6_Normales", "Corrigé étape 6"})
    k = O["E6_Pratique_Fuselage_corrige"]
    select([k.name])
    collapse_modifiers(k, {"DataTransfer", "Smooth by Angle"})
    props('MODIFIER')
    yield 1.5
    shot("260_panneau_data_transfer")
    collapse_modifiers(k, {m.name for m in k.modifiers})


def f261():
    show_collections({"Etape_6_Normales"})
    shading('SOLID', matcap='check_reflection_horizontal.exr', cavity=False)
    frame(["E6_Exemple_Propre"], rot=(80, 0, -30), zoom=0.8)
    a = area('VIEW_3D')
    w = win()
    w.cursor_warp(int(a.x + a.width - 120), int(a.y + a.height - 60))
    yield 0.8
    with bpy.context.temp_override(**ov(a, 'HEADER')):
        bpy.ops.wm.call_panel('INVOKE_DEFAULT', name="VIEW3D_PT_shading", keep_open=True)
    yield 1.5
    shot("261_matcap_reflection")
    close_popups()
    yield 0.6
    close_popups()
    yield 0.6
    shading('SOLID')


def f263():
    show_collections({"Etape_6_Normales", "Corrigé étape 6"})
    shading('SOLID', matcap='check_reflection_horizontal.exr', cavity=False)
    p = O["E6_Pratique_Platine"]
    k = O["E6_Pratique_Platine_corrige"]
    k.hide_set(True)
    frame([p.name], rot=(80, 0, -25), zoom=1.15)
    yield 1.5
    shot("263_platine_sans")
    k.hide_set(False)
    p.hide_set(True)
    yield 1.5
    shot("263_platine_wn")
    p.hide_set(False)
    shading('SOLID')


def f264():
    show_collections({"Atelier_Retroviseur", "Corrigé atelier"})
    for o in bpy.data.collections["Atelier_Retroviseur"].objects:
        o.hide_set(True)
    # les objets de coupe en fil de fer brouillent la lecture des vues
    for n in ("Retro_Coupe_Clignotant_corrige", "Retro_Coupe_Platine_corrige"):
        O[n].hide_set(True)
    shading('MATERIAL')
    names = ["Retro_Coque_corrige", "Retro_Platine_corrige", "Retro_Pied_corrige"]
    frame(names, rot=(75, 0, 150), zoom=0.95)
    yield 3.0
    shot("264_retro_arriere")
    frame(names, rot=(75, 0, -30), zoom=0.95)
    yield 2.5
    shot("264_retro_avant")
    # 2.66 : logement du clignotant, sans puis avec Data Transfer
    shading('SOLID', matcap='check_reflection_horizontal.exr', cavity=False)
    k = O["Retro_Coque_corrige"]
    frame(["Retro_Clignotant_corrige"], rot=(80, 0, -20), zoom=1.6)
    O["Retro_Clignotant_corrige"].hide_set(True)
    dt = k.modifiers["DataTransfer"]
    dt.show_viewport = False
    yield 1.5
    shot("266_logement_sans")
    dt.show_viewport = True
    yield 1.5
    shot("266_logement_dt")
    O["Retro_Clignotant_corrige"].hide_set(False)
    # 2.65 : le miroir et sa calotte de référence
    shading('SOLID')
    O["Retro_Miroir_reference"].hide_set(False)
    O["Retro_Coque_corrige"].hide_set(True)
    frame(["Retro_Miroir_corrige", "Retro_Miroir_reference"], rot=(80, 0, 160), zoom=0.9)
    yield 1.5
    shot("265_miroir_reference")
    O["Retro_Coque_corrige"].hide_set(False)
    for o in bpy.data.collections["Atelier_Retroviseur"].objects:
        o.hide_set(False)


STEPS = [("233", f233), ("234", f234), ("235", f235), ("236", f236), ("237", f237), ("238", f238),
         ("239", f239), ("240", f240), ("241", f241), ("244", f244), ("246", f246), ("248", f248),
         ("250", f250), ("251", f251), ("252", f252),
         ("253", f253), ("257", f257), ("258", f258), ("259", f259), ("260", f260), ("261", f261),
         ("263", f263), ("264", f264)]


def runner():
    # open_object_panels() : abandonné (change l'ordre des panneaux) ; voir captures_clics.py
    yield from layout_for_captures()
    for key, fn in STEPS:
        if ONLY and key not in ONLY:
            continue
        try:
            gen = fn()
            for delay in gen:
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
            # la zone texte du LISEZ-MOI devient une Timeline repliée : plus de place pour la vue
            _it = runner()
        return next(_it)
    except StopIteration:
        print("CAPTURES TERMINEES")
        os._exit(0)
    except Exception as e:
        import traceback
        traceback.print_exc()
        os._exit(1)


bpy.app.timers.register(tick, first_interval=3.0)
bpy.app.timers.register(lambda: os._exit(2), first_interval=600.0)   # sécurité : quitte toujours
