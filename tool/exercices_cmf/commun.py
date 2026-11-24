# Outils communs aux scripts de la planche CMF : scène, collections, images empaquetées à chemin
# relatif, nœuds, enregistrement. Repris de tool/exercices_ch4/commun.py.

import os

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
EX = os.path.join(ROOT, "_resources", "exercices")
WORK = os.path.join(HERE, "_construction")              # dossiers intermédiaires, non suivis par git
PLANCHE_DIR = os.path.join(WORK, "PRC02_CMF_planche")     # le contenu du zip livré
VIERGE = os.path.join(PLANCHE_DIR, "PRC02_CMF_planche_vierge.blend")
EXEMPLE = os.path.join(PLANCHE_DIR, "PRC02_CMF_planche_exemple.blend")
CH3 = os.path.join(ROOT, "tool", "exercices_ch3")          # recettes et images de la bibliothèque CMF
STUDIOLIGHTS = os.path.join(os.path.dirname(bpy.app.binary_path), "%d.%d" % bpy.app.version[:2],
                            "datafiles", "studiolights", "world")


def lin(h):
    """Hexadécimal sRGB vers couleur linéaire (RGBA)."""
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (out[0], out[1], out[2], 1.0)


def new_collection(name, parent):
    c = bpy.data.collections.new(name)
    parent.children.link(c)
    return c


def layer_collection(name):
    def walk(lc):
        if lc.collection.name == name:
            return lc
        for k in lc.children:
            r = walk(k)
            if r:
                return r
        return None
    lc = walk(bpy.context.view_layer.layer_collection)
    assert lc is not None, name
    return lc


def set_relative_path(im, rel):
    """Remplace le chemin d'une image empaquetée par //rel. Le chemin est un tampon de taille fixe,
    enregistré en entier : on l'écrase d'abord sur toute sa longueur."""
    assert im.packed_file is not None, im.name
    im.filepath_raw = "/" * 1200
    im.filepath_raw = "//" + rel
    for pf in im.packed_files:
        pf.filepath = "/" * 1200
        pf.filepath = "//" + rel


def pack_image(path, rel, colorspace=None):
    im = bpy.data.images.load(path)
    if colorspace:
        im.colorspace_settings.name = colorspace
    im.pack()
    set_relative_path(im, rel)
    return im


def text_block(name, body):
    txt = bpy.data.texts.get(name) or bpy.data.texts.new(name)
    txt.clear()
    txt.write(body)
    txt.cursor_set(0)
    return txt


def assign(ob, mat):
    ob.data.materials.clear()
    ob.data.materials.append(mat)


def deselect_all():
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = None


# ---------------------------------------------------------------------------- nœuds
def node(nt, typ, x, y, **props):
    n = nt.nodes.new(typ)
    n.location = (x, y)
    for k, v in props.items():
        setattr(n, k, v)
    return n


def feed(nt, sock, v):
    if isinstance(v, bpy.types.NodeSocket):
        nt.links.new(v, sock)
    else:
        sock.default_value = v


def math(nt, op, a, b=None, x=0, y=0, clamp=False):
    m = node(nt, "ShaderNodeMath", x, y, operation=op, use_clamp=clamp)
    feed(nt, m.inputs[0], a)
    if b is not None:
        feed(nt, m.inputs[1], b)
    return m.outputs[0]


def map_range(nt, v, fmin, fmax, tmin=0.0, tmax=1.0, x=0, y=0, smooth=True):
    m = node(nt, "ShaderNodeMapRange", x, y, data_type='FLOAT',
             interpolation_type='SMOOTHSTEP' if smooth else 'LINEAR', clamp=True)
    for i, val in enumerate((v, fmin, fmax, tmin, tmax)):
        feed(nt, m.inputs[i], val)
    return m.outputs[0]


def mix_color(nt, fac, a, b, x=0, y=0):
    m = node(nt, "ShaderNodeMix", x, y, data_type='RGBA', blend_type='MIX', clamp_factor=True)
    feed(nt, m.inputs[0], fac)
    feed(nt, m.inputs[6], a)
    feed(nt, m.inputs[7], b)
    return m.outputs[2]


def finalize(path):
    """Groupes de nœuds locaux, bibliothèques retirées, enregistrement compressé sans .blend1."""
    for ng in list(bpy.data.node_groups):
        if ng.library is not None:
            ng.make_local(clear_asset_data=True)
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    while len(bpy.data.libraries):
        lib = bpy.data.libraries[0]
        print("BIBLIOTHEQUE retirée :", lib.name)
        bpy.data.libraries.remove(lib)
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
