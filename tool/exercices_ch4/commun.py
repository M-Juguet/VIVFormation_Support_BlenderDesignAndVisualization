# Outils communs aux scripts du chapitre 4 : scène, copies sans référence faible, texte LISEZ-MOI,
# mise en page, enregistrement. Repris de tool/exercices_ch3/commun.py.

import math
import os
import zipfile

import bpy
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
EX = os.path.join(ROOT, "_resources", "exercices")
WORK = os.path.join(HERE, "_construction")          # dossiers intermédiaires, non suivis par git
HDRI_DIR = os.path.join(HERE, "hdri")               # HDRI de Poly Haven, non suivies par git
ZIP_CH3 = os.path.join(EX, "PRC02_ch3_lampe_habillage.zip")
A2 = os.path.join(WORK, "PRC02_ch3_lampe_habillage", "PRC02_ch3_lampe_habillage.blend")
STUDIO = os.path.join(EX, "PRC02_ch4_studio.blend")
SECOURS = os.path.join(EX, "PRC02_ch4_lampe_en_studio.blend")
STUDIOLIGHTS = os.path.join(os.path.dirname(bpy.app.binary_path), "%d.%d" % bpy.app.version[:2],
                            "datafiles", "studiolights", "world")

T = (0.11, 0.0, 0.22)          # point de visée commun : le centre du corps de la lampe


def lin(h):
    """Hexadécimal sRGB vers couleur linéaire (RGBA)."""
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (out[0], out[1], out[2], 1.0)


def extract_a2():
    """La lampe habillée du chapitre 3 (fiche A2), lue dans son zip livré, sans le modifier."""
    with zipfile.ZipFile(ZIP_CH3) as z:
        z.extractall(WORK)
    assert os.path.exists(A2), A2
    return A2


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.name = "Scene"
    sc.render.engine = 'BLENDER_EEVEE'
    sc.eevee.use_raytracing = False          # décoché exprès : la section 1 l'explique
    sc.eevee.taa_render_samples = 64
    sc.eevee.taa_samples = 16
    us = sc.unit_settings
    us.system = 'METRIC'
    us.length_unit = 'MILLIMETERS'
    us.scale_length = 1.0
    r = sc.render
    r.resolution_x, r.resolution_y, r.resolution_percentage = 1920, 1080, 100
    r.filepath = "//rendus/"
    r.film_transparent = False
    im = r.image_settings
    im.file_format = 'PNG'
    im.color_mode = 'RGB'
    im.color_depth = '8'
    vs = sc.view_settings
    vs.view_transform = 'AgX'
    vs.look = 'None'
    vs.exposure = 0.0
    vs.gamma = 1.0
    return sc


def new_collection(name, parent):
    c = bpy.data.collections.new(name)
    parent.children.link(c)
    return c


def hide_collection(name, eye=True, render=True):
    c = bpy.data.collections[name]
    c.hide_render = render

    def walk(lc):
        if lc.collection == c:
            lc.hide_viewport = eye
            return True
        return any(walk(k) for k in lc.children)

    assert walk(bpy.context.view_layer.layer_collection), name


def drop_weak_references():
    """Les données lues dans un autre .blend gardent une référence faible à ce fichier
    (library_weak_reference) : on les remplace par des copies, qui n'en ont pas."""
    for coll in (bpy.data.collections, bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.node_groups,
                 bpy.data.images, bpy.data.materials):
        for idb in list(coll):
            if idb.library_weak_reference:
                name = idb.name
                cp = idb.copy()
                idb.user_remap(cp)
                coll.remove(idb)
                cp.name = name


def aim(ob, target):
    d = Vector(target) - ob.location
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()


def material(name, color, rough, metallic=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    p = next(n for n in m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
    p.inputs["Base Color"].default_value = lin(color)
    p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metallic
    m.diffuse_color = lin(color)
    m.roughness = rough
    m.metallic = metallic
    return m, p


def set_relative_path(im, rel):
    """Remplace le chemin d'une image empaquetée par //rel. Le chemin est un tampon de taille fixe,
    enregistré en entier : on l'écrase d'abord sur toute sa longueur, sinon la fin de l'ancien chemin
    absolu resterait dans le fichier, après le nouveau chemin plus court."""
    assert im.packed_file is not None, im.name
    im.filepath_raw = "/" * 1200
    im.filepath_raw = "//" + rel
    for pf in im.packed_files:
        pf.filepath = "/" * 1200
        pf.filepath = "//" + rel


def pack_image(path, rel):
    """Charge une image, l'empaquette et ne garde que le chemin relatif //rel, partout."""
    im = bpy.data.images.load(path)
    im.pack()
    set_relative_path(im, rel)
    return im


def text_block(body):
    txt = bpy.data.texts.new("LISEZ-MOI")
    txt.write(body)
    txt.cursor_set(0)
    return txt


def setup_layout(txt, eye, target, props_context='RENDER', distance_k=0.8, lens=50):
    """Espace Layout : la Timeline devient le LISEZ-MOI, la vue 3D est cadrée en Material Preview."""
    rot = (Vector(target) - Vector(eye)).to_track_quat('-Z', 'Y')
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                sp = area.spaces.active
                sp.clip_start = 0.001
                sp.clip_end = 50.0
                sp.lens = lens
                sp.shading.type = 'MATERIAL'
                try:
                    sp.shading.studio_light = 'studio.exr'
                except Exception as e:
                    print("STUDIO", screen.name, repr(e))
                if screen.name in ("Layout", "Shading"):
                    r3d = sp.region_3d
                    r3d.view_perspective = 'PERSP'
                    r3d.view_location = Vector(target)
                    r3d.view_rotation = rot
                    r3d.view_distance = (Vector(target) - Vector(eye)).length * distance_k
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


def deselect_all():
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = None


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
    groups = sorted(ng.name for ng in bpy.data.node_groups)
    if groups_expected is not None:
        assert groups == sorted(groups_expected), groups
    weak = [i.name for c in (bpy.data.collections, bpy.data.objects, bpy.data.meshes, bpy.data.curves,
                             bpy.data.images, bpy.data.node_groups, bpy.data.materials) for i in c
            if i.library_weak_reference]
    assert not weak, weak
    for im in bpy.data.images:
        if im.type == 'IMAGE':
            assert im.packed_file is not None and im.filepath.startswith("//"), (im.name, im.filepath)
    bpy.context.preferences.filepaths.save_version = 0
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=path, compress=True, relative_remap=True)
    print("ENREGISTRE", path, os.path.getsize(path), "octets")


def deg(v):
    return math.radians(v)
