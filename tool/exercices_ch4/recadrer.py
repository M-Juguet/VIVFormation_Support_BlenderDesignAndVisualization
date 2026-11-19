# Recadre les captures brutes de captures_brutes.py et écrit les figures d'interface du chapitre 4
# (JPEG) dans assets/images/, ainsi que l'image comparative des moteurs (figure 4.6 et PNG du corrigé).
# Les captures d'interface gardent leur résolution d'origine : aucune réduction, pour que l'échelle
# d'affichage calculée par echelles.py reste celle de l'interface. Repris de tool/exercices_ch3/recadrer.py.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup --python tool\exercices_ch4\recadrer.py -- <dossier_captures_brutes> [figure ...]
#
# Une figure est une liste de rangées ; une rangée, une liste de morceaux (capture, rectangle). Un
# rectangle est (x0, y0, x1, y1) en pixels de la capture 1600 x 960, origine en haut à gauche, ou :
#   ("menu", marge)        : le menu ouvert, isolé par différence avec la capture « _avant » ;
#   ("camera",)            : le cadre de la caméra, relevé au moment de la capture (CAM_BOX).
# Options : "flou" (rectangles floutés : chemins du poste), "hauteur" (morceaux ramenés à une même
# hauteur, pour les images de rendu), "largeur" (largeur finale, pour les images de rendu seulement).

import json
import os
import sys

import bpy
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
IMG = os.path.join(ROOT, "assets", "images")
CORR = os.path.join(HERE, "_construction", "images")
args = sys.argv[sys.argv.index("--") + 1:]
SRC = args[0]
ONLY = set(args[1:])


def load(path):
    im = bpy.data.images.load(path)
    w, h = im.size
    px = np.array(im.pixels[:], dtype=np.float32).reshape(h, w, 4)[::-1].copy()   # haut en premier
    bpy.data.images.remove(im)
    return px


def cap(name):
    return load(os.path.join(SRC, name + ".png"))


def info(name):
    with open(os.path.join(SRC, name + ".json"), encoding="utf-8") as f:
        return json.load(f)


def resize(px, w):
    """Réduction par moyenne de zones. Agrandir laisserait des zones vides (division par zéro, pixels
    NaN qui noircissent ensuite toute l'image) : on le refuse."""
    h0, w0 = px.shape[:2]
    if w > w0:
        raise ValueError(f"resize() ne fait que réduire ({w0} -> {w} px demandés)")
    h = max(1, round(h0 * w / w0))
    ys = (np.arange(h + 1) * h0 / h).astype(int)
    xs = (np.arange(w + 1) * w0 / w).astype(int)
    c = np.cumsum(np.cumsum(np.pad(px, ((1, 0), (1, 0), (0, 0))), axis=0), axis=1)
    s = c[ys[1:]][:, xs[1:]] - c[ys[:-1]][:, xs[1:]] - c[ys[1:]][:, xs[:-1]] + c[ys[:-1]][:, xs[:-1]]
    area = ((ys[1:] - ys[:-1])[:, None] * (xs[1:] - xs[:-1])[None, :])[..., None]
    return s / area


def to_height(px, h):
    return resize(px, max(1, round(px.shape[1] * h / px.shape[0])))


def blur(px, r, k=9):
    x0, y0, x1, y1 = r
    reg = px[y0:y1, x0:x1, :3]
    for _ in range(3):
        for axis in (0, 1):
            pad = np.pad(reg, ((k, k), (0, 0), (0, 0)) if axis == 0 else ((0, 0), (k, k), (0, 0)), mode='edge')
            acc = np.zeros_like(reg)
            for d in range(-k, k + 1):
                acc += pad[k + d:k + d + reg.shape[0]] if axis == 0 else pad[:, k + d:k + d + reg.shape[1]]
            reg = acc / (2 * k + 1)
    px[y0:y1, x0:x1, :3] = reg


def menu_rect(name, marge, avant=None):
    px = cap(name)
    before = cap(avant or name.rsplit("_", 1)[0] + "_avant")
    d = np.abs(px[..., :3] - before[..., :3]).max(axis=2) > 0.08
    d[:30, :] = False
    d[928:, :] = False
    ys, xs = np.nonzero(d)
    return (max(0, xs.min() - marge), max(0, ys.min() - marge), min(px.shape[1], xs.max() + 1 + marge),
            min(px.shape[0], ys.max() + 1 + marge))


def pad_rows(parts, gap):
    h = max(p.shape[0] for p in parts)
    out = []
    for i, p in enumerate(parts):
        if p.shape[0] < h:
            fill = np.ones((h - p.shape[0], p.shape[1], 4), dtype=np.float32)
            fill[..., :3] = p[-1:, :, :3].mean(axis=(0, 1))
            p = np.concatenate([p, fill], axis=0)
        if i:
            out.append(np.ones((h, gap, 4), dtype=np.float32))
        out.append(p)
    return np.concatenate(out, axis=1)


def stack(rows, gap):
    w = max(r.shape[1] for r in rows)
    out = []
    for i, r in enumerate(rows):
        if r.shape[1] < w:
            fill = np.ones((r.shape[0], w - r.shape[1], 4), dtype=np.float32)
            fill[..., :3] = 0.157          # le gris sombre de l'interface
            r = np.concatenate([r, fill], axis=1)
        if i:
            out.append(np.ones((gap, w, 4), dtype=np.float32))
        out.append(r)
    return np.concatenate(out, axis=0)


def save(px, name, kind="jpg"):
    h, w = px.shape[:2]
    im = bpy.data.images.new("fig", w, h, alpha=False)
    flat = px[::-1].copy()
    flat[..., 3] = 1.0
    im.pixels = flat.ravel()
    path = os.path.join(IMG if kind == "jpg" else CORR, name)
    if kind == "jpg":
        bpy.context.scene.render.image_settings.quality = 92
        im.file_format = 'JPEG'
        im.save(filepath=path, quality=92)
    else:
        im.filepath_raw = path
        im.file_format = 'PNG'
        im.save()
    bpy.data.images.remove(im)
    print("FIGURE", name, w, "x", h, flush=True)


P = (1040, 330, 1595)          # colonne de l'éditeur de propriétés : x0, y0 (sous l'en-tête), x1
FIGS = {
    "4.2": ("append_collection_browser_blender.jpg",
            [[("402_append_collection", (0, 40, 700, 168)), ("402_append_collection", (1300, 90, 1600, 270))],
             [("402_append_collection", (0, 890, 450, 924)), ("402_append_collection", (1255, 890, 1600, 924))]],
            {"flou": [("402_append_collection", (190, 45, 700, 70))]}),
    "4.3": ("shading_pie_menu_blender.jpg", [[("403_pie", ("menu", 16, "403_pie_avant"))]], {}),
    "4.5": ("rendered_popover_blender.jpg", [[("405_popover", (655, 20, 990, 430))]], {}),
    "4.7": ("render_engine_menu_blender.jpg", [[("407_engine", (P[0], P[1], P[2], 500))]], {}),
    "4.8": ("render_window_slots_blender.jpg",
            [[("408_fenetre_rendu", (660, 34, 1600, 62))], [("408_fenetre_rendu", (0, 64, 560, 90))],
             [("408_fenetre_rendu", (320, 229, 1280, 768))]], {}),
    "4.9": ("eevee_raytracing_panel_blender.jpg", [[("409_raytracing", (P[0], P[1], P[2], 690))]], {}),
    "4.11": ("eevee_sampling_panel_blender.jpg", [[("411_sampling", (P[0], P[1], P[2], 715))]], {}),
    "4.12": ("color_management_view_menu_blender.jpg", [[("412_color_menu", (P[0], 440, P[2], 790))]], {}),
    "4.15": ("world_browse_menu_blender.jpg", [[("415_world_browse", (P[0], P[1], P[2], 720))]], {}),
    "4.16": ("world_surface_hdri_blender.jpg", [[("416_world_surface_ouvert", (1060, 320, 1595, 800))]], {}),
    "4.17": ("world_nodes_hdri_blender.jpg", [[("417_world_nodes", (140, 270, 1460, 730))]], {}),
    "4.18": ("add_light_menu_blender.jpg", [[("418_light_menu", (115, 232, 360, 395))]], {}),
    "4.20": ("light_properties_area_blender.jpg", [[("420_light_area", (P[0], P[1], P[2], 750))]], {}),
    "4.22": ("three_point_lighting_top_blender.jpg", [[("422_dessus", (150, 150, 900, 820))]], {}),
    "4.24": ("outliner_lights_collection_blender.jpg", [[("424_outliner", (1016, 60, 1595, 300))]], {}),
    "4.26": ("view_cameras_align_menus_blender.jpg",
             [[("426_cameras", (24, 238, 378, 360)), ("426_align", (8, 238, 382, 484))]], {}),
    "4.27": ("sidebar_view_lock_camera_blender.jpg", [[("427_sidebar", (670, 95, 985, 500))]], {}),
    "4.28": ("camera_lens_panel_blender.jpg", [[("428_lens", (P[0], P[1], P[2], 720))]], {}),
    "4.30": ("composition_guides_panel_blender.jpg", [[("430_composition", (P[0], 585, P[2], 930))]], {}),
    "4.31": ("camera_view_thirds_blender.jpg", [[("431_camview", (62, 100, 1005, 790))]], {}),
    "4.32": ("camera_dof_panel_blender.jpg", [[("432_dof", (P[0], P[1], P[2], 705))]], {}),
    "4.34": ("output_format_panel_blender.jpg", [[("434_format", (P[0], P[1], P[2], 640))]], {}),
    "4.35": ("format_presets_menu_blender.jpg", [[("435_presets", (1250, 500, 1595, 925))]], {}),
    "4.36": ("render_menu_blender.jpg", [[("436_render_menu", (5, 22, 255, 245))]], {}),
    "4.37": ("image_save_as_blender.jpg",
             [[("437_save_as", (0, 40, 950, 200)), ("437_save_as", (1320, 80, 1600, 530))],
              [("437_save_as", (0, 890, 600, 924)), ("437_save_as", (1255, 890, 1600, 924))]],
             {"flou": [("437_save_as", (190, 45, 950, 70))]}),
    "4.38": ("eevee_film_panel_blender.jpg", [[("438_film", (P[0], 640, P[2], 810))]], {}),
    "4.41": ("spot_light_panel_blender.jpg", [[("441_spot", (P[0], 450, P[2], 875))]], {}),
}


def build(key):
    fname, rows, opts = FIGS[key]
    flous = {}
    for c, r in opts.get("flou", []):
        flous.setdefault(c, []).append(r)
    out = []
    for row in rows:
        parts = []
        for name, spec in row:
            px = cap(name)
            for r in flous.get(name, []):
                blur(px, r)
            if spec[0] == "menu":
                spec = menu_rect(name, spec[1], spec[2] if len(spec) > 2 else None)
            x0, y0, x1, y1 = [int(v) for v in spec]
            parts.append(px[y0:y1, x0:x1])
        out.append(pad_rows(parts, 8))
    save(stack(out, 8), fname)


def camera_crop(name):
    x0, y0, x1, y1 = info(name)["CAM_BOX"]
    return cap(name)[y0:y1, x0:x1]


def fig_4_4():
    a = to_height(camera_crop("404_mp_off"), 400)
    b = to_height(camera_crop("404_mp_on"), 400)
    px = pad_rows([a, b], 10)
    save(resize(px, 1200) if px.shape[1] > 1200 else px, "material_preview_scene_world_blender.jpg")


def fig_4_6():
    # Le cadre de la caméra couvre toute la largeur de la vue 3D : la capture Material Preview garde la
    # barre d'outils à gauche. On retire la même fraction de largeur aux trois images (même cadrage),
    # puis on les ramène à la plus petite hauteur (resize() ne fait que réduire).
    mp = camera_crop("406_mp_banc")
    ee = load(os.path.join(CORR, "comparatif_eevee.png"))
    cy = load(os.path.join(CORR, "comparatif_cycles.png"))
    x0, _, x1, _ = info("406_mp_banc")["CAM_BOX"]
    f = (info("406_mp_banc")["VIEW_3D_TOOLS"][2] + 3 - x0) / (x1 - x0)
    parts = [p[:, int(round(p.shape[1] * f)):] for p in (mp, ee, cy)]
    h = min(p.shape[0] for p in parts)
    full = pad_rows([to_height(p, h) for p in parts], 16)
    save(full, "PRC02_ch4_comparatif_moteurs.png", kind="png")
    save(resize(full, 1920), "engines_comparison_blender.jpg")


if __name__ == "__main__":
    for key in list(FIGS) + ["4.4", "4.6"]:
        if ONLY and key not in ONLY:
            continue
        try:
            if key == "4.4":
                fig_4_4()
            elif key == "4.6":
                fig_4_6()
            else:
                build(key)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("ECHEC", key, repr(e), flush=True)
