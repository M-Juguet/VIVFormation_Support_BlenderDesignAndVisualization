# Outils communs aux scripts de construction du chapitre 3 : scène, copies sans référence faible,
# texte LISEZ-MOI, enregistrement. Repris de tool/exercices_ch2/build_lampe.py.

import os

import bpy
from mathutils import Matrix, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
EX = os.path.join(ROOT, "_resources", "exercices")
WORK = os.path.join(HERE, "_construction")          # dossiers intermédiaires, non suivis par git
BIBLIO_DIR = os.path.join(WORK, "PRC02_bibliotheque_CMF")
NUANCIER = os.path.join(BIBLIO_DIR, "PRC02_ch3_nuancier_cmf.blend")
LAMPE_DIR = os.path.join(WORK, "PRC02_ch3_lampe_habillage")
SRC_CH2 = os.path.join(EX, "PRC02_ch2_lampe_modele.blend")


def reset_scene(raytracing):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.name = "Scene"
    sc.render.engine = 'BLENDER_EEVEE'
    sc.eevee.use_raytracing = raytracing
    us = sc.unit_settings
    us.system = 'METRIC'
    us.length_unit = 'MILLIMETERS'
    us.scale_length = 1.0
    sc.render.filepath = "//"
    if sc.world is None:
        sc.world = bpy.data.worlds.new("World")
    return sc


def new_collection(name, parent):
    c = bpy.data.collections.new(name)
    parent.children.link(c)
    return c


def drop_weak_references():
    """Les données lues dans un autre .blend gardent une référence faible à ce fichier
    (library_weak_reference) : on les remplace par des copies, qui n'en ont pas."""
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.node_groups, bpy.data.images,
                 bpy.data.materials):
        for idb in list(coll):
            if idb.library_weak_reference:
                name = idb.name
                cp = idb.copy()
                idb.user_remap(cp)
                coll.remove(idb)
                cp.name = name


def copy_objects(objs, col, suffix, offset):
    """Copie un groupe d'objets (données comprises) dans col : parents, Empty d'un Array et objets
    de modificateurs pointent vers les copies. Les objets sans parent sont décalés de offset."""
    off = Matrix.Translation(Vector(offset))
    mp = {}
    for o in objs:
        c = o.copy()
        if o.data is not None:
            c.data = o.data.copy()
            c.data.name = o.data.name + suffix
        c.name = o.name + suffix
        col.objects.link(c)
        mp[o] = c
    for o, c in mp.items():
        if o.parent in mp:
            c.parent = mp[o.parent]
            c.matrix_parent_inverse = o.matrix_parent_inverse.copy()
            c.matrix_basis = o.matrix_basis.copy()
        else:
            c.parent = None
            c.matrix_basis = off @ o.matrix_basis
        for m in c.modifiers:
            for attr in ("offset_object", "mirror_object", "object"):
                tgt = getattr(m, attr, None)
                if tgt in mp:
                    setattr(m, attr, mp[tgt])
    return {o.name: c for o, c in mp.items()}


def assign(ob, mat):
    ob.data.materials.clear()
    ob.data.materials.append(mat)


def label(text, size, loc, rot, col, mat, align='CENTER'):
    cu = bpy.data.curves.new("Etiquette_" + text, 'FONT')
    cu.body = text
    cu.size = size
    cu.align_x = align
    cu.align_y = 'CENTER'
    ob = bpy.data.objects.new("Etiquette_" + text, cu)
    col.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = rot
    cu.materials.append(mat)
    ob.hide_select = True
    return ob


def text_block(body):
    txt = bpy.data.texts.new("LISEZ-MOI")
    txt.write(body)
    txt.cursor_set(0)
    return txt


def setup_layout(txt, shading_type, eye, target, props_context='MATERIAL', studio='studio.exr',
                 distance_k=0.8, lens=50):
    """Espace Layout : la Timeline devient le LISEZ-MOI, la vue 3D est cadrée et réglée."""
    rot = (Vector(target) - Vector(eye)).to_track_quat('-Z', 'Y')
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                sp = area.spaces.active
                sp.clip_start = 0.001
                sp.clip_end = 50.0
                sp.lens = lens
                sp.shading.type = 'SOLID'
                sp.shading.light = 'STUDIO'
                sp.shading.color_type = 'MATERIAL'
                sp.shading.show_cavity = False
                if screen.name in ("Layout", "Shading"):
                    r3d = sp.region_3d
                    r3d.view_perspective = 'PERSP'
                    r3d.view_location = Vector(target)
                    r3d.view_rotation = rot
                    r3d.view_distance = (Vector(target) - Vector(eye)).length * distance_k
                if screen.name == "Layout":
                    sp.shading.type = shading_type
                if screen.name in ("Layout", "Shading"):
                    try:
                        prev = sp.shading.type
                        sp.shading.type = 'MATERIAL'
                        sp.shading.studio_light = studio
                        sp.shading.type = prev if screen.name == "Layout" else 'MATERIAL'
                    except Exception as e:
                        print("STUDIO", screen.name, repr(e))
            if area.type == 'PROPERTIES':
                try:
                    area.spaces.active.context = props_context
                except TypeError:
                    pass
            for space in area.spaces:
                if space.type == 'FILE_BROWSER' and space.params is not None:
                    space.params.directory = b"/" * 1200
                    space.params.directory = b"//"
    layout = bpy.data.screens["Layout"]
    for area in layout.areas:
        if area.type == 'DOPESHEET_EDITOR':
            area.type = 'TEXT_EDITOR'
            sp = next(s for s in area.spaces if s.type == 'TEXT_EDITOR')
            sp.text = txt
            sp.show_word_wrap = True
            sp.show_line_numbers = False
            sp.show_syntax_highlight = False
            sp.top = 0
            return
    raise RuntimeError("zone Timeline introuvable")


def text_in_shading(txt):
    """Espace Shading : l'éditeur d'images, en bas à gauche, devient le LISEZ-MOI."""
    sh = bpy.data.screens["Shading"]
    for area in sh.areas:
        if area.type == 'IMAGE_EDITOR':
            area.type = 'TEXT_EDITOR'
            sp = next((s for s in area.spaces if s.type == 'TEXT_EDITOR'), None)
            if sp is None:
                print("SHADING : zone changée sans espace texte (arrière-plan) ; finish_ui.py s'en charge")
                area.type = 'IMAGE_EDITOR'
                return
            sp.text = txt
            sp.show_word_wrap = True
            sp.show_line_numbers = False
            sp.show_syntax_highlight = False
            sp.top = 0
            return
    raise RuntimeError("éditeur d'images introuvable dans Shading")


def select_only(ob):
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = ob
    if ob is not None:
        ob.select_set(True)


def finalize(path, groups_expected=None):
    """Groupes de nœuds locaux, bibliothèques retirées, enregistrement compressé sans .blend1."""
    for ng in list(bpy.data.node_groups):
        if ng.library is not None:
            ng.make_local(clear_asset_data=True)
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    while len(bpy.data.libraries):
        lib = bpy.data.libraries[0]
        print("BIBLIOTHEQUE retirée :", lib.name)
        bpy.data.libraries.remove(lib)
    for ng in bpy.data.node_groups:
        assert ng.library is None, ng.name
    groups = sorted(ng.name for ng in bpy.data.node_groups)
    if groups_expected is not None:
        assert groups == sorted(groups_expected), groups
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    weak = [i.name for c in (bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.images,
                             bpy.data.node_groups, bpy.data.materials) for i in c if i.library_weak_reference]
    assert not weak, weak
    bpy.context.preferences.filepaths.save_version = 0
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=path, compress=True, relative_remap=True)
    print("ENREGISTRE", path, os.path.getsize(path), "octets")
