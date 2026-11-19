# Recadre les captures brutes de captures_brutes.py et écrit les figures 2.1 à 2.32 (JPEG) dans
# assets/images/.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup --python tool\exercices_ch2\recadrer.py -- <dossier_captures_brutes> [figure ...]
#
# Chaque figure est une grille de morceaux : une liste de rangées, chaque rangée une liste de
# morceaux mis côte à côte. Un morceau est (capture, mode) :
#   ("vue", marge)          : contour des objets sur le fond uni de la vue 3D, plus une marge ;
#   ("props", y0[, y1])     : l'éditeur de propriétés, de y0 jusqu'au dernier panneau (ou jusqu'à y1) ;
#   ("menu", marge)         : le menu ouvert, isolé par différence avec la capture « _avant » ;
#   ("menu_rows", y0, y1)   : idem, limité aux rangées y0 à y1 (un extrait d'un long menu) ;
#   ("zone", nom)           : une zone entière (OUTLINER…), d'après le JSON de la capture ;
#   (x0, y0, x1, y1)        : rectangle fixe (pixels, origine en haut à gauche).
# La figure 2.19 reçoit ensuite des étiquettes : un SVG posé sur l'image, exporté par Edge.

import json
import os
import subprocess
import sys

import bpy
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
IMG = os.path.join(ROOT, "assets", "images")
args = sys.argv[sys.argv.index("--") + 1:]
SRC = args[0]
ONLY = set(args[1:])
SIDE, FULL = 640, 1200
VIEW = (75, 100, 975, 890)     # zone utile de la vue 3D (sans barre d'outils, en-têtes ni gizmo)


def load(name):
    im = bpy.data.images.load(os.path.join(SRC, name + ".png"))
    w, h = im.size
    px = np.array(im.pixels[:], dtype=np.float32).reshape(h, w, 4)[::-1].copy()   # haut en premier
    bpy.data.images.remove(im)
    return px


def info(name):
    with open(os.path.join(SRC, name + ".json"), encoding="utf-8") as f:
        return json.load(f)


def bbox(mask):
    ys, xs = np.nonzero(mask)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def rect_of(name, spec, px):
    kind = spec[0]
    if kind == "vue":
        marge = spec[1]
        x0, y0, x1, y1 = VIEW
        reg = px[y0:y1, x0:x1, :3]
        bg = np.median(np.concatenate([reg[:6].reshape(-1, 3), reg[-6:].reshape(-1, 3)]), axis=0)
        mask = np.abs(reg - bg).max(axis=2) > 0.06
        bx0, by0, bx1, by1 = bbox(mask)
        return (max(x0, x0 + bx0 - marge), max(y0, y0 + by0 - marge), min(x1, x0 + bx1 + marge), min(y1, y0 + by1 + marge))
    if kind == "props":
        x0, ry0, x1, y1 = info(name)["PROPERTIES"]
        y0 = spec[1]
        if len(spec) > 2:
            return (x0, y0, x1 - 4, spec[2])
        # fond de l'éditeur : sous le dernier panneau, près du bas (on ignore les 20 dernières rangées)
        reg = px[y0:y1 - 20, x0:x1, :3]
        bg = np.median(reg[-15:, 10:200].reshape(-1, 3), axis=0)
        rows = np.nonzero(np.abs(reg[:, 8:-30] - bg).max(axis=2).max(axis=1) > 0.03)[0]
        return (x0, y0, x1 - 4, y0 + rows.max() + 10)
    if kind in ("menu", "menu_rows"):
        before = load(name + "_avant")
        d = np.abs(px[..., :3] - before[..., :3]).max(axis=2) > 0.08
        # la barre d'outils, les en-têtes et la barre d'état changent aussi quand un menu s'ouvre
        d[:30, :] = False
        d[900:, :] = False
        d[:, :70] = False
        bx0, by0, bx1, by1 = bbox(d)
        if kind == "menu":
            m = spec[1]
            return (max(0, bx0 - m), max(0, by0 - m), min(px.shape[1], bx1 + m), min(px.shape[0], by1 + m))
        return (bx0, spec[1], bx1, spec[2])
    if kind == "zone":
        return tuple(info(name)[spec[1]])
    return spec


def pad_to(p, h, w=None):
    out = p
    if p.shape[0] < h:
        pad = np.ones((h - p.shape[0], p.shape[1], 4), dtype=np.float32)
        pad[..., :3] = p[-1, -1, :3]
        out = np.concatenate([out, pad], axis=0)
    if w is not None and out.shape[1] < w:
        pad = np.ones((out.shape[0], w - out.shape[1], 4), dtype=np.float32)
        pad[..., :3] = out[-1, -1, :3]
        out = np.concatenate([out, pad], axis=1)
    return out


def hconcat(parts, gap=8):
    h = max(p.shape[0] for p in parts)
    out = []
    for i, p in enumerate(parts):
        out.append(pad_to(p, h))
        if i < len(parts) - 1:
            out.append(np.ones((h, gap, 4), dtype=np.float32))
    return np.concatenate(out, axis=1)


def vconcat(rows, gap=8):
    w = max(r.shape[1] for r in rows)
    out = []
    for i, r in enumerate(rows):
        out.append(pad_to(r, r.shape[0], w))
        if i < len(rows) - 1:
            out.append(np.ones((gap, w, 4), dtype=np.float32))
    return np.concatenate(out, axis=0)


def save(px, name, max_w):
    h, w = px.shape[:2]
    im = bpy.data.images.new("fig", w, h, alpha=False)
    im.pixels = px[::-1].ravel()
    if w > max_w:
        im.scale(max_w, int(round(h * max_w / w)))
    path = os.path.join(IMG, name)
    im.filepath_raw = path
    im.file_format = 'JPEG'
    bpy.context.scene.render.image_settings.quality = 92
    im.save(filepath=path, quality=92)
    print("FIGURE", name, im.size[0], "x", im.size[1])
    bpy.data.images.remove(im)
    return path


# (fichier, rangées de morceaux, largeur maximale)
FIGS = {
    "2.1": ("gabarit_wire_lamp_blender.jpg", [[("201_gabarit_copie", ("vue", 30))]], FULL),
    "2.2": ("add_modifier_generate_menu_blender.jpg", [[("202_menu_generate", ("menu_split", 10, 0.585))]], SIDE),
    "2.3": ("modifier_header_menu_blender.jpg", [[("203_menu_entete", (1022, 330, 1598, 640))]], SIDE),
    "2.4": ("mirror_modifier_panel_blender.jpg", [[("204_panneau_mirror", ("props", 335))]], SIDE),
    "2.5": ("mirror_arm_rods_blender.jpg", [[("205_tiges_doubles", ("vue", 20)), ("205_piege_origine", ("vue", 20))]], FULL),
    "2.6": ("mirror_clipping_bisect_blender.jpg", [[("206_capot_edition", ("vue", 20))]], SIDE),
    "2.7": ("delete_menu_faces_blender.jpg", [[("207_menu_delete", ("menu", 70))]], SIDE),
    "2.8": ("solidify_modifier_panel_blender.jpg", [[("208_panneau_solidify", ("props", 335))]], SIDE),
    "2.9": ("solidify_lamp_head_blender.jpg", [[("209_tete_dessous", ("vue", 15)), ("209_bord_coque", (75, 100, 975, 890))]], FULL),
    "2.10": ("bevel_modifier_angle_blender.jpg", [[("210_panneau_bevel", ("props", 335))]], SIDE),
    "2.11": ("object_menu_shade_auto_smooth_blender.jpg",
             [[("211_menu_object", (115, 32, 343, 56))], [("211_menu_object", (115, 470, 343, 735))]], SIDE),
    "2.12": ("modifier_stack_head_blender.jpg", [[("212_facettes", ("vue", 15)), ("212_pile_lisse", ("vue", 15))],
                                                 [("212_pile_lisse", ("props", 335, 530))]], FULL),
    "2.13": ("add_empty_menu_blender.jpg", [[("213_menu_empty", ("menu", 10))]], SIDE),
    "2.14": ("array_object_offset_panel_blender.jpg", [[("214_panneau_array", ("props", 335))]], SIDE),
    "2.15": ("radial_array_vent_grille_blender.jpg", [[("215_couronne_grille", ("vue", 20))]], SIDE),
    "2.16": ("parent_menu_blender.jpg", [[("216_menu_parent", ("menu", 40))]], SIDE),
    "2.17": ("radial_array_knob_blender.jpg", [[("217_molette_crans", ("vue", 10))]], SIDE),
    "2.18": ("add_curve_menu_blender.jpg", [[("218_menu_curve", ("menu", 10))]], SIDE),
    "2.19": ("bezier_anatomy_blender.jpg", [[("219_anatomie", (100, 250, 930, 690))]], FULL),
    "2.20": ("handle_type_menu_blender.jpg", [[("220_menu_handle", ("menu", 40))]], SIDE),
    "2.21": ("curve_pen_toolbar_blender.jpg", [[("221_curve_pen", (0, 30, 760, 560))]], SIDE),
    "2.22": ("curve_shape_panel_blender.jpg", [[("222_onglet_data_courbe", ("props", 335, 810))]], SIDE),
    "2.23": ("curve_geometry_bevel_panel_blender.jpg", [[("223_geometry_bevel", ("props", 335))]], SIDE),
    "2.24": ("cable_bezier_lamp_blender.jpg", [[("224_cable", (75, 100, 975, 890))]], FULL),
    "2.25": ("snap_pie_menu_blender.jpg", [[("225_pie_snap", ("menu", 10))]], SIDE),
    "2.26": ("screw_modifier_panel_blender.jpg", [[("226_panneau_screw", ("props", 335))]], SIDE),
    "2.27": ("bulb_profile_screw_blender.jpg", [[("227_profil", ("vue", 15)), ("227_ampoule", "meme"),
                                                 ("227_sommet_aplati", "meme")]], FULL),
    "2.28": ("lamp_model_vs_gabarit_blender.jpg", [[("228_gabarit_face", ("vue", 20)), ("228_gabarit_perspective", ("vue", 20))]], FULL),
    "2.29": ("outliner_lamp_model_blender.jpg", [[("229_outliner", ("zone", "OUTLINER"))]], SIDE),
    "2.30": ("lamp_model_final_blender.jpg", [[("230_lampe_finale", ("vue", 40))]], FULL),
    "2.31": ("boolean_difference_panel_blender.jpg", [[("231_panneau_boolean", ("props", 335))]], SIDE),
    "2.32": ("reading_light_challenge_blender.jpg", [[("232_liseuse", (120, 100, 975, 890))]], SIDE),
}


def build(key):
    fname, rows, max_w = FIGS[key]
    out_rows = []
    last = None
    for row in rows:
        parts = []
        for name, spec in row:
            px = load(name)
            if spec[0] == "menu_split":
                # un long menu, coupé en deux colonnes dans un blanc entre deux lignes
                x0, y0, x1, y1 = [int(v) for v in rect_of(name, ("menu", spec[1]), px)]
                m = px[y0:y1, x0:x1]
                ink = (m[..., :3].max(axis=2) > 0.55).sum(axis=1)
                want = int(m.shape[0] * spec[2])
                cut = min(range(want - 14, want + 15), key=lambda y: (ink[y], abs(y - want)))
                parts += [m[:cut], m[cut:]]
                continue
            r = last if spec == "meme" else rect_of(name, spec, px)
            last = r
            x0, y0, x1, y1 = [int(v) for v in r]
            parts.append(px[y0:y1, x0:x1])
        out_rows.append(hconcat(parts))
    return save(vconcat(out_rows), fname, max_w), last


def edge():
    for p in (os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Microsoft", "Edge", "Application", "msedge.exe"),
              os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft", "Edge", "Application", "msedge.exe")):
        if os.path.exists(p):
            return p
    raise FileNotFoundError("msedge.exe")


def attendre_fichier(path, timeout=60):
    """msedge.exe rend la main avant d'écrire la capture : on attend le fichier, puis une taille stable."""
    import time
    t0, last = time.time(), -1
    while time.time() - t0 < timeout:
        if os.path.exists(path):
            size = os.path.getsize(path)
            if size > 0 and size == last:
                return
            last = size
        time.sleep(0.5)
    raise TimeoutError(path)


def annotate_219(path, crop):
    """Étiquettes de l'anatomie d'une courbe : type de chaque point, point de contrôle, poignée."""
    with open(os.path.join(SRC, "219_anatomie_points.json"), encoding="utf-8") as f:
        pts = json.load(f)
    im = bpy.data.images.load(path)
    w, h = im.size
    bpy.data.images.remove(im)
    x0, y0, x1, y1 = crop
    k = w / (x1 - x0)

    def P(p):
        return ((p[0] - x0) * k, (p[1] - y0) * k)

    names = {"VECTOR": "Vector", "AUTO": "Automatic", "ALIGNED": "Aligned", "FREE": "Free"}
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="%d" height="%d">' % (w, h),
           '<image href="%s" x="0" y="0" width="%d" height="%d"/>' % (os.path.basename(path) + ".src.png", w, h),
           '<style>text{font-family:"Segoe UI",Arial,sans-serif;font-size:22px;fill:#FFFFFF}'
           '.b{fill:#1E2430;opacity:0.86} .l{stroke:#FFFFFF;stroke-width:1.6}</style>']

    def label(x, y, tx, ty, text):
        tw = 11.5 * len(text) + 18
        svg.append('<line class="l" x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f"/>' % (x, y, tx + tw / 2, ty))
        svg.append('<rect class="b" x="%.0f" y="%.0f" width="%.0f" height="34" rx="6"/>' % (tx, ty - 17, tw))
        svg.append('<text x="%.0f" y="%.0f">%s</text>' % (tx + 9, ty + 8, text))

    for i, p in enumerate(pts):
        cx, cy = P(p["co"])
        below = i % 2 == 0
        label(cx, cy, cx - 60, cy + (95 if below else -95), names[p["type"]])
    # point de contrôle et poignée, sur le point Aligned
    a = pts[2]
    cx, cy = P(a["co"])
    hx, hy = P(a["handle_right"])
    label(cx, cy, cx + 70, cy + 40, "point de contrôle")
    label(hx, hy, hx + 30, hy - 10, "poignée")
    svg.append("</svg>")
    src_png = path + ".src.png"
    # le fond : la figure JPEG, copiée à côté du SVG
    import shutil
    shutil.copyfile(path, src_png)
    svg_path = path + ".svg"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    tmp_png = path + ".annot.png"
    tmp = os.path.join(os.environ.get("TEMP", HERE), "edge-croquis-profile")
    subprocess.run([edge(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--user-data-dir=" + tmp, "--window-size=%d,%d" % (w, h), "--screenshot=" + tmp_png,
                    "file:///" + svg_path.replace("\\", "/")], check=True, timeout=120)
    attendre_fichier(tmp_png)
    im = bpy.data.images.load(tmp_png)
    px = np.array(im.pixels[:], dtype=np.float32)       # chargement immédiat (sinon relu depuis le nouveau chemin)
    w2, h2 = im.size
    bpy.data.images.remove(im)
    out = bpy.data.images.new("fig_annotee", w2, h2, alpha=False)
    out.pixels = px
    out.filepath_raw = path
    out.file_format = 'JPEG'
    out.save(filepath=path, quality=92)
    bpy.data.images.remove(out)
    for p in (src_png, svg_path, tmp_png):
        os.remove(p)
    print("ANNOTEE", path)


for key in FIGS:
    if ONLY and key not in ONLY:
        continue
    try:
        path, crop = build(key)
        if key == "2.19":
            annotate_219(path, crop)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("ECHEC", key, repr(e))
