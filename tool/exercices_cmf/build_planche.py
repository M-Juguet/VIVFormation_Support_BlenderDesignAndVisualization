# Construit la planche CMF de PRC02, en deux fichiers, dans tool/exercices_cmf/_construction/PRC02_CMF_planche/ :
#   PRC02_CMF_planche_vierge.blend   les 8 emplacements en gris neutre, prêts à habiller
#   PRC02_CMF_planche_exemple.blend  la même planche, habillée (harmonie d'intérieur ferroviaire)
#   blender_assets.cats.txt          les catalogues des actifs (bibliothèque du chapitre 3, gabarits, exemple)
# Puis finish_ui.py (espace CMF, vignettes), verifier_blend.py et livrer.py (le zip).
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 -Script tool\exercices_cmf\build_planche.py
# Toutes les dimensions sont en mètres ; le fichier affiche des millimètres.
#
# La composition reprend les deux planches de référence (_resources/ref_CMF_01.png et ref_CMF_02.png) :
# les cotes sont relevées en pixels sur ref_CMF_01.png (1050 x 740), à 0,7 mm par pixel.

import math
import os
import sys

import bmesh
import bpy
import numpy as np
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import commun as C   # noqa: E402
import gabarits as G   # noqa: E402

sys.path.insert(0, C.CH3)
import matieres as M   # noqa: E402

MM_PX = 0.7          # millimètres par pixel de la référence
CX, CY = 525, 370    # centre de la référence : centre de la caméra de face

# réglages de la lumière, calibrés sur le gris 18 % (voir calibrer.py)
AREA_POWER = float(os.environ.get("CMF_AREA_W", "22"))
WORLD_STRENGTH = float(os.environ.get("CMF_WORLD", "0.10"))
FOND_EMISSION = float(os.environ.get("CMF_FOND_EMIT", "0.12"))
RASANTE_POWER = 60.0

CATS = {  # chemin du catalogue : UUID (ceux de la bibliothèque du chapitre 3 sont repris)
    "Bibliothèque CMF/Métaux": M.CATS_BIBLIO["Métaux"],
    "Bibliothèque CMF/Plastiques": M.CATS_BIBLIO["Plastiques"],
    "Bibliothèque CMF/Peintures": M.CATS_BIBLIO["Peintures"],
    "Bibliothèque CMF/Verres": M.CATS_BIBLIO["Verres"],
    "Bibliothèque CMF/Finitions texturées": M.CATS_BIBLIO["Finitions texturées"],
    "Gabarits": "6f1c2a4e-3b7d-4c11-9a01-0c3e5b7d9b10",
    "Planche exemple": "6f1c2a4e-3b7d-4c11-9a01-0c3e5b7d9b20",
}

# nom, pixels (x0, y0, x1, y1) sur la référence, bas de la plaque (mm), épaisseur (mm), rayon des coins (mm),
# chanfrein (mm), pastille (numéro, retrait en mm depuis le coin haut gauche)
PLAQUES = [
    ("Emplacement_4", (272, 188, 620, 635), 3.0, 3.0, 0.0, 0.5, ("4", 12)),
    ("Emplacement_1_bas", (25, 505, 335, 680), 8.0, 3.0, 0.0, 0.5, None),
    ("Emplacement_1", (25, 225, 335, 515), 12.0, 3.0, 0.0, 0.5, ("1", 12)),
    ("Emplacement_7", (795, 175, 1010, 680), 8.0, 4.0, 0.0, 0.6, ("7", 12)),
    ("Emplacement_5", (515, 145, 790, 697), 20.0, 6.0, 31.0, 1.5, ("5", 22)),
    ("Emplacement_3", (202, 410, 451, 697), 28.0, 1.5, 0.0, 0.3, ("3", 12)),
    ("Emplacement_8", (797, 481, 881, 697), 23.5, 3.0, 0.0, 0.5, ("8", 12)),
    ("Emplacement_2", (175, 507, 295, 722), 40.0, 2.0, 0.0, 0.4, ("2", 12)),
]
TUBE = ("Emplacement_6", (742, 257, 798, 722), 26.6)   # main courante couchée, posée sur le 5 et le 8

LISEZ_MOI = """PRC02 · Planche CMF — {titre}
Tout se fait dans l'espace CMF, en vue caméra, en Rendered (EEVEE). Les valeurs sont indicatives.

1. Habiller : glissez une matière de l'Asset Browser (en bas, Current File) sur un emplacement de la vue.
2. Régler sans abîmer le modèle : onglet Material, cliquez l'icône de copie à droite du nom de la matière, renommez-la, puis réglez.
3. Couleur : cliquez la case Couleur, onglet Hex, tapez le code (ex. 1F2A44). Brillance et Relief vont de 0 à 1 ; les tailles sont en mm.
4. Motif d'un tissu (Gabarit_Tissu_Motif) : Material > Surface > Motif > Open, choisissez votre image ; Taille du motif (mm) et Rotation juste dessous.
5. Vue rasante : cochez la collection « Lumière rasante » dans l'Outliner ; sélectionnez CAM_Rasante, puis View > Cameras > Set Active Object as Camera. Retour : même geste sur CAM_Planche.
6. Exporter : enregistrez le fichier, puis Ctrl + F12. L'image A4 paysage est écrite dans rendus/planche_0001.png, à côté du fichier.
Image finale : Render Properties > Render Engine > Cycles (256 échantillons et débruitage déjà réglés), puis Ctrl + F12. Revenez à EEVEE pour travailler.
Contrôle de l'exposition : cochez la collection « Contrôle » (gris 18 %, blanc, noir) ; le gris doit se lire vers 118 dans l'image. Ne touchez pas à Exposure ni au Look.
Les actifs gardent leurs catalogues si blender_assets.cats.txt reste à côté du fichier : ne séparez pas le dossier.
"""


def P(x, y):
    """Pixel de la référence vers mètres, dans le plan de la planche."""
    return ((x - CX) * MM_PX / 1000.0, (CY - y) * MM_PX / 1000.0)


# ---------------------------------------------------------------------------- scène
def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.name = "Planche CMF"
    sc.render.engine = 'BLENDER_EEVEE'
    ee = sc.eevee
    ee.use_raytracing = True
    ee.taa_render_samples = 128
    ee.taa_samples = 16
    ee.use_shadow_jitter_viewport = True
    cy = sc.cycles
    cy.samples = 256
    cy.preview_samples = 64
    cy.use_denoising = True
    cy.use_preview_denoising = True
    cy.device = 'CPU'
    us = sc.unit_settings
    us.system = 'METRIC'
    us.length_unit = 'MILLIMETERS'
    us.scale_length = 1.0
    r = sc.render
    r.resolution_x, r.resolution_y, r.resolution_percentage = 2339, 1654, 100   # A4 paysage à 200 dpi
    r.film_transparent = False
    r.filepath = "//rendus/planche_"
    r.use_file_extension = True
    for attr in dir(r):
        if attr.startswith("use_stamp") and isinstance(getattr(r, attr), bool):
            setattr(r, attr, False)
    im = r.image_settings
    im.file_format = 'PNG'
    im.color_mode = 'RGB'
    im.color_depth = '8'
    sc.frame_start = sc.frame_end = sc.frame_current = 1
    vs = sc.view_settings
    vs.view_transform = 'Khronos PBR Neutral'
    vs.look = 'None'
    vs.exposure = 0.0
    vs.gamma = 1.0
    sc.display_settings.display_device = 'sRGB'
    return sc


def outline(w, h, radius, seg):
    pts = []
    for cx, cy, a0 in ((w / 2 - radius, -h / 2 + radius, -90), (w / 2 - radius, h / 2 - radius, 0),
                       (-w / 2 + radius, h / 2 - radius, 90), (-w / 2 + radius, -h / 2 + radius, 180)):
        for k in range(seg + 1):
            a = math.radians(a0 + 90 * k / seg)
            pts.append((cx + radius * math.cos(a), cy + radius * math.sin(a)))
    return pts


def plate_mesh(name, w, h, t, radius, chamfer):
    """Plaque de w x h x t (m), centrée sur l'origine, coins arrondis (radius, mm ; 1 mm au moins),
    arêtes haut et bas chanfreinées (chamfer, mm) : quatre contours décalés, reliés par des bandes."""
    ch = chamfer / 1000.0
    r = max(radius, 1.0) / 1000.0
    seg = 12 if radius > 5 else 3
    rings = [(outline(w - 2 * ch, h - 2 * ch, r - ch, seg), -t / 2), (outline(w, h, r, seg), -t / 2 + ch),
             (outline(w, h, r, seg), t / 2 - ch), (outline(w - 2 * ch, h - 2 * ch, r - ch, seg), t / 2)]
    bm = bmesh.new()
    vs = [[bm.verts.new((x, y, z)) for x, y in pts] for pts, z in rings]
    bm.faces.new(list(reversed(vs[0])))
    bm.faces.new(vs[3])
    n = len(vs[0])
    for a, b in zip(vs[:-1], vs[1:]):
        for i in range(n):
            j = (i + 1) % n
            bm.faces.new((a[i], a[j], b[j], b[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.normal_update()
    for f in bm.faces:
        f.smooth = abs(f.normal.z) < 0.999 and abs(abs(f.normal.z) - 0.7071) > 0.05
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def tube_mesh(name, r, length):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=72, radius1=r, radius2=r, depth=length)
    bm.normal_update()
    edges = [e for e in bm.edges if all(abs(abs(v.co.z) - length / 2) < 1e-7 for v in e.verts)]
    bmesh.ops.bevel(bm, geom=edges, offset=0.0015, segments=3, profile=0.5, affect='EDGES', clamp_overlap=True)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.normal_update()
    for f in bm.faces:
        f.smooth = abs(f.normal.z) < 0.999
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def pastille(num, parent, top_z, loc_xy, coll, mat_disc, mat_num):
    """Pastille ronde bleu marine de 12 mm, numéro blanc, posée sur la plaque et liée à elle."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=48, radius1=0.006, radius2=0.006, depth=0.0004)
    cu = bpy.data.curves.new("chiffre_" + num, 'FONT')
    cu.body = num
    cu.size = 0.0072
    cu.align_x = 'CENTER'
    cu.align_y = 'CENTER'
    tmp = bpy.data.objects.new("chiffre_" + num, cu)
    coll.objects.link(tmp)
    bpy.context.view_layer.update()
    tme = bpy.data.meshes.new_from_object(tmp.evaluated_get(bpy.context.evaluated_depsgraph_get()))
    bpy.data.objects.remove(tmp)
    bpy.data.curves.remove(cu)
    vmap = {}
    for v in tme.vertices:
        vmap[v.index] = bm.verts.new((v.co.x, v.co.y - 0.0003, 0.00025))
    for p in tme.polygons:
        f = bm.faces.new([vmap[i] for i in p.vertices])
        f.material_index = 1
    bpy.data.meshes.remove(tme)
    me = bpy.data.meshes.new("Pastille_" + num)
    bm.to_mesh(me)
    bm.free()
    me.materials.append(mat_disc)
    me.materials.append(mat_num)
    ob = bpy.data.objects.new("Pastille_" + num, me)
    coll.objects.link(ob)
    ob.location = (loc_xy[0], loc_xy[1], top_z + 0.00025)
    ob.parent = parent
    ob.matrix_parent_inverse = parent.matrix_world.inverted()
    ob.hide_select = True
    return ob


def principled_mat(name, hexa, rough, metallic=0.0, emission=0.0):
    m = bpy.data.materials.new(name)
    try:
        m.use_nodes = True
    except Exception:
        pass
    p = next(n for n in m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
    p.inputs["Base Color"].default_value = C.lin(hexa)
    p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metallic
    if emission:
        p.inputs["Emission Color"].default_value = C.lin(hexa)
        p.inputs["Emission Strength"].default_value = emission
    m.diffuse_color = C.lin(hexa)
    m.roughness = rough
    return m


def aim(ob, target):
    d = Vector(target) - ob.location
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()


def motif_image():
    """Le motif du tissu de siège (5) : vagues stylisées vues à travers des côtes verticales, raccord
    parfait sur les quatre bords. 1024 px pour un raccord de 160 mm."""
    n = 1024
    u = np.arange(n) / n
    X, Y = np.meshgrid(u, u)
    tau = 2 * np.pi
    f = (np.sin(tau * (X + 0.18 * np.sin(tau * 2 * Y) + 0.06 * np.sin(tau * 3 * X)))
         * np.cos(tau * (Y + 0.22 * np.sin(tau * X)))
         + 0.45 * np.sin(tau * (2 * X - Y + 0.1 * np.cos(tau * 2 * Y))))
    shape = np.clip((f - 0.3) / 0.08, 0, 1)
    stripe = 0.5 + 0.5 * np.cos(tau * 28 * (X + 0.006 * np.sin(tau * 4 * Y) + 0.004 * np.sin(tau * 9 * Y)))
    t = shape * np.clip(stripe * 1.6 - 0.15, 0, 1) + (1 - shape) * 0.22 * stripe ** 4
    rng = np.random.default_rng(7)
    t = np.clip(t + rng.normal(0, 0.03, t.shape), 0, 1)
    navy = np.array([0x20, 0x1C, 0x44]) / 255.0
    teal = np.array([0x2A, 0x66, 0x62]) / 255.0
    rgb = navy[None, None, :] * (1 - t[..., None]) + teal[None, None, :] * t[..., None]
    rgba = np.concatenate([rgb, np.ones((n, n, 1))], axis=2)
    im = bpy.data.images.new("motif_tissu_vagues.png", n, n, alpha=False)
    im.pixels.foreach_set(rgba.astype(np.float32).ravel())
    path = os.path.join(C.WORK, "textures", "motif_tissu_vagues.png")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.filepath_raw = path
    im.file_format = 'PNG'
    im.save()
    bpy.data.images.remove(im)
    return C.pack_image(path, "textures/motif_tissu_vagues.png", "sRGB")


def mark(mat, catalog, desc, tags=()):
    mat.asset_mark()
    ad = mat.asset_data
    ad.author = M.AUTHOR
    ad.license = M.LICENSE
    ad.description = desc
    for t in tags:
        ad.tags.new(t, skip_if_exists=True)
    ad.catalog_id = CATS[catalog]


def write_catalogs(folder):
    lines = ["# This is an Asset Catalog Definition file for Blender.", "#",
             "# Empty lines and lines starting with `#` will be ignored.",
             "# The first non-ignored line should be the version indicator.",
             '# Other lines are of the format "UUID:catalog/path/for/assets:simple catalog name"', "",
             "VERSION 1", ""]
    for path, uid in CATS.items():
        lines.append("%s:%s:%s" % (uid, path, path.replace("/", "-")))
    with open(os.path.join(folder, "blender_assets.cats.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------- construction
def build_scene():
    sc = reset_scene()
    root = sc.collection
    c_planche = C.new_collection("Planche", root)
    c_empl = C.new_collection("Emplacements", root)
    c_past = C.new_collection("Pastilles", root)
    c_light = C.new_collection("Éclairage", root)
    c_ras = C.new_collection("Lumière rasante", root)
    c_cam = C.new_collection("Caméras", root)
    c_ctrl = C.new_collection("Contrôle", root)

    # le fond blanc : un plan de 10 x 10 m, légèrement lumineux pour se lire blanc à exposition juste
    fond_mat = principled_mat("Fond_Blanc", "FFFFFF", 0.9, emission=FOND_EMISSION)
    p = next(n for n in fond_mat.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
    p.inputs["Specular IOR Level"].default_value = 0.25
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=5.0)
    me = bpy.data.meshes.new("Fond_Blanc")
    bm.to_mesh(me)
    bm.free()
    fond = bpy.data.objects.new("Fond_Blanc", me)
    c_planche.objects.link(fond)
    C.assign(fond, fond_mat)
    fond.hide_select = True

    gris = principled_mat("Emplacement_Gris", "8C8C8C", 0.55)
    past_mat = principled_mat("Pastille_Marine", "0B2A4A", 0.45)
    num_mat = principled_mat("Pastille_Chiffre", "FFFFFF", 0.5)

    objs = {}
    for name, (x0, y0, x1, y1), z, t, radius, ch, past in PLAQUES:
        (ax, ay), (bx, by) = P(x0, y0), P(x1, y1)
        w, h = bx - ax, ay - by
        me = plate_mesh(name, w, h, t / 1000.0, radius, ch)
        ob = bpy.data.objects.new(name, me)
        c_empl.objects.link(ob)
        ob.location = ((ax + bx) / 2, (ay + by) / 2, (z + t / 2) / 1000.0)
        C.assign(ob, gris)
        objs[name] = ob
        if past:
            bpy.context.view_layer.update()
            inset = past[1] / 1000.0
            pastille(past[0], ob, (z + t) / 1000.0, (ax + inset, ay - inset), c_past, past_mat, num_mat)
    name, (x0, y0, x1, y1), zb = TUBE
    (ax, ay), (bx, by) = P(x0, y0), P(x1, y1)
    r = (bx - ax) / 2
    length = ay - by
    tube = bpy.data.objects.new(name, tube_mesh(name, r, length))
    c_empl.objects.link(tube)
    tube.location = ((ax + bx) / 2, (ay + by) / 2, zb / 1000.0 + r)
    tube.rotation_euler = (math.radians(90), 0, 0)     # axe du tube = axe Z de la pièce, couché le long de Y
    C.assign(tube, gris)
    objs[name] = tube
    bpy.context.view_layer.update()
    pastille("6", tube, zb / 1000.0 + 2 * r, ((ax + bx) / 2, ay - 0.011), c_past, past_mat, num_mat)

    # éclairage statique neutre : un grand Area au-dessus, légèrement en avant, et une HDRI de studio
    la = bpy.data.lights.new("Area_Principale", 'AREA')
    la.shape = 'RECTANGLE'
    la.size, la.size_y = 1.2, 0.8
    la.energy = AREA_POWER
    la.use_shadow_jitter = True
    area = bpy.data.objects.new("Area_Principale", la)
    c_light.objects.link(area)
    # au-dessus et en avant, juste hors du champ que la caméra de face voit en miroir : les laques et
    # les vernis ne sont pas voilés par le reflet de la lumière
    area.location = (0.0, -0.85, 1.40)
    aim(area, (0.0, 0.0, 0.0))
    ld = bpy.data.lights.new("Area_Debouchage", 'AREA')
    ld.shape = 'RECTANGLE'
    ld.size, ld.size_y = 1.2, 0.8
    ld.energy = AREA_POWER * 0.55
    ld.use_shadow_jitter = True
    deb = bpy.data.objects.new("Area_Debouchage", ld)
    c_light.objects.link(deb)
    deb.location = (0.0, 0.85, 1.40)
    aim(deb, (0.0, 0.0, 0.0))

    lr = bpy.data.lights.new("Area_Rasante", 'AREA')
    lr.shape = 'RECTANGLE'
    lr.size, lr.size_y = 0.9, 0.05
    lr.energy = RASANTE_POWER
    lr.use_shadow_jitter = True
    ras = bpy.data.objects.new("Area_Rasante", lr)
    c_ras.objects.link(ras)
    ras.location = (-0.30, 0.55, 0.07)
    aim(ras, (0.0, 0.0, 0.0))

    world = bpy.data.worlds.new("Studio_Neutre")
    try:
        world.use_nodes = True
    except Exception:
        pass
    nt = world.node_tree
    bg = next(n for n in nt.nodes if n.type == 'BACKGROUND')
    bg.inputs["Strength"].default_value = WORLD_STRENGTH
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    env.location = (-350, 300)
    env.image = C.pack_image(os.path.join(C.STUDIOLIGHTS, "studio.exr"), "hdri/studio.exr", "Linear Rec.709")
    neutre = nt.nodes.new("ShaderNodeHueSaturation")      # l'HDRI de studio tire vers le bleu : désaturée
    neutre.location = (-80, 300)
    neutre.inputs["Saturation"].default_value = 0.0
    nt.links.new(env.outputs["Color"], neutre.inputs["Color"])
    nt.links.new(neutre.outputs["Color"], bg.inputs["Color"])
    sc.world = world

    # caméras
    cp = bpy.data.cameras.new("CAM_Planche")
    cp.type = 'ORTHO'
    cp.ortho_scale = 1050 * MM_PX / 1000.0
    cp.clip_start, cp.clip_end = 0.05, 5.0
    cam = bpy.data.objects.new("CAM_Planche", cp)
    c_cam.objects.link(cam)
    cam.location = (0.0, 0.0, 1.2)
    sc.camera = cam
    cr = bpy.data.cameras.new("CAM_Rasante")
    cr.lens = 50
    cr.clip_start, cr.clip_end = 0.01, 20.0
    cr.dof.use_dof = False
    camr = bpy.data.objects.new("CAM_Rasante", cr)
    c_cam.objects.link(camr)
    camr.location = (0.02, -0.50, 0.20)
    aim(camr, (0.0, 0.03, 0.0))

    # contrôle de l'exposition : gris 18 %, blanc (90 %) et noir (3 %), en haut à gauche de la planche
    for k, (nm, hexa) in enumerate((("Controle_Gris_18", "767676"), ("Controle_Blanc_90", "F3F3F3"),
                                    ("Controle_Noir_3", "343434"))):
        me = plate_mesh(nm, 0.04, 0.04, 0.001, 0, 0.2)
        ob = bpy.data.objects.new(nm, me)
        c_ctrl.objects.link(ob)
        x, y = P(330 + k * 75, 115)
        ob.location = (x, y, 0.0005)
        C.assign(ob, principled_mat(nm, hexa, 0.9))
    C.layer_collection("Contrôle").exclude = True
    C.layer_collection("Lumière rasante").exclude = True
    return sc, objs


def build_assets():
    """Les 25 matières de la bibliothèque du chapitre 3 et les gabarits, marqués comme actifs."""
    for name, (cat, _col, _m, _r, _o, tags, desc) in M.BIBLIO.items():
        mat = M.biblio(name)
        mark(mat, "Bibliothèque CMF/" + cat, desc, tags)
    for im in bpy.data.images:
        if im.packed_file is not None and im.filepath.startswith("//textures_cmf/"):
            C.set_relative_path(im, "textures_cmf/" + os.path.basename(im.filepath))
    gabs = G.build_all(motif_image())
    for name, (m, g, desc) in gabs.items():
        mark(m, "Gabarits", desc, ["gabarit"])
    return {k: v[0] for k, v in gabs.items()}


def setup_ui(txt, sc):
    """Espace CMF : l'espace Layout renommé, vue caméra en Rendered. La passe finish_ui.py, dans une
    vraie fenêtre, place ensuite l'Asset Browser, le LISEZ-MOI, l'Outliner réduit et l'onglet Material."""
    ws = bpy.data.workspaces["Layout"]
    ws.name = "CMF"
    for screen in bpy.data.screens:
        for area in screen.areas:
            for space in area.spaces:
                if space.type == 'FILE_BROWSER' and space.params is not None:
                    space.params.directory = b"/" * 1200
                    space.params.directory = b"//"
            if area.type == 'VIEW_3D':
                sp = area.spaces.active
                sp.clip_start = 0.001
                sp.clip_end = 50.0
                if screen.name == "Layout" or screen == ws.screens[0]:
                    sp.shading.type = 'RENDERED'
                    sp.region_3d.view_perspective = 'CAMERA'
                    sp.overlay.show_floor = False
                    sp.overlay.show_axis_x = False
                    sp.overlay.show_axis_y = False
                    sp.overlay.show_cursor = False
                    sp.overlay.show_extras = False
                    sp.overlay.show_relationship_lines = False
                    sp.show_region_ui = False
                    sp.show_gizmo_navigate = True
                else:
                    sp.shading.type = 'MATERIAL'


def lisez_moi(titre):
    return C.text_block("LISEZ-MOI", LISEZ_MOI.format(titre=titre))


EXEMPLE = {  # emplacement : (matière, gabarit, réglages, coordonnées du motif)
    "Emplacement_1": ("Sol_Mouchete_Marine", "Gabarit_Plastique_Graine",
                      {"Couleur": "262B45", "Brillance": 0.35, "Relief": 0.12, "Taille du grain (mm)": 0.5,
                       "Mouchetures": 0.55, "Moucheture claire": "C9CED6", "Moucheture foncée": "0D0E16",
                       "Taille des mouchetures (mm)": 0.6}, None),
    "Emplacement_1_bas": ("Sol_Mouchete_Gris", "Gabarit_Plastique_Graine",
                          {"Couleur": "7B838A", "Brillance": 0.35, "Relief": 0.12, "Taille du grain (mm)": 0.5,
                           "Mouchetures": 0.5, "Moucheture claire": "D8DCE0", "Moucheture foncée": "2A2E35",
                           "Taille des mouchetures (mm)": 0.6}, None),
    "Emplacement_2": ("Anodise_Degrade_Argent", "Gabarit_Anodise_Degrade",
                      {"Couleur haut": "C5CED6", "Couleur bas": "656C71", "Début du dégradé (mm)": -55.0,
                       "Fin du dégradé (mm)": 45.0, "Brillance": 0.62}, None),
    "Emplacement_3": ("Perfore_Gris_Bleu", "Gabarit_Perfore",
                      {"Couleur": "7F8D95", "Brillance": 0.4, "Pas des trous (mm)": 3.5,
                       "Diamètre des trous (mm)": 1.1, "Quinconce": 1.0}, None),
    "Emplacement_4": ("Paroi_Gris_Chaud", "Gabarit_Laque",
                      {"Couleur": "C7C4BF", "Brillance": 0.35, "Vernis": 0.0, "Relief": 0.04,
                       "Taille de la peau d'orange (mm)": 1.5}, None),
    "Emplacement_5": ("Tissu_Siege_Vagues", "Gabarit_Tissu_Motif",
                      {"Brillance": 0.08, "Velours": 0.55, "Relief": 0.35, "Taille de la trame (mm)": 0.7},
                      {"Taille du motif (mm)": 130.0}),
    "Emplacement_6": ("Alu_Brosse", None, None, None),        # la main courante : matière de la bibliothèque
    "Emplacement_7": ("Translucide_Cote_Blanc", "Gabarit_Translucide_Cote",
                      {"Couleur": "F4F2EE", "Translucidité": 0.35, "Brillance": 0.55, "Pas des côtes (mm)": 6.0,
                       "Ondulation (mm)": 2.0}, None),
    "Emplacement_8": ("Laque_Prune", "Gabarit_Laque",
                      {"Couleur": "6A3B7C", "Brillance": 0.82, "Vernis": 1.0, "Relief": 0.02}, None),
}


def dress(objs, gabs):
    for empl, (name, gab, values, coord) in EXEMPLE.items():
        if gab is None:
            mat = bpy.data.materials[name]
        else:
            mat = G.variant(gabs[gab], name, values, coord)
            mark(mat, "Planche exemple", "Planche exemple : %s, d'après %s." % (name.replace("_", " "), gab), ["exemple"])
        C.assign(objs[empl], mat)


def main():
    os.makedirs(C.PLANCHE_DIR, exist_ok=True)
    only = os.environ.get("CMF_ONLY", "")
    sc, objs = build_scene()
    gabs = build_assets()
    setup_ui(None, sc)
    C.deselect_all()
    bpy.context.view_layer.objects.active = objs["Emplacement_5"]
    objs["Emplacement_5"].select_set(True)
    write_catalogs(C.PLANCHE_DIR)
    if only != "exemple":
        lisez_moi("fichier de travail (planche vierge)")
        C.finalize(C.VIERGE)
    if only != "vierge":
        dress(objs, gabs)
        lisez_moi("planche exemple, habillée")
        C.finalize(C.EXEMPLE)
    print("ACTIFS", sum(1 for m in bpy.data.materials if m.asset_data))


main()
