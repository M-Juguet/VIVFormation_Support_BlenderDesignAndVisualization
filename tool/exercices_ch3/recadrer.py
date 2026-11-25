# Recadre les captures brutes de captures_brutes.py et écrit les figures 3.1 à 3.54 (JPEG), numérotées comme
# dans le texte du chapitre, dans
# assets/images/. Repris de tool/exercices_ch2/recadrer.py.
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup --python tool\exercices_ch3\recadrer.py -- <dossier_captures_brutes> [figure ...]
#
# Chaque figure est une grille de morceaux : une liste de rangées, chaque rangée une liste de morceaux
# mis côte à côte. Un morceau est (capture, mode) :
#   ("vue", marge)          : contour des objets sur le fond uni de la vue 3D, plus une marge ;
#   ("noeuds", marge)       : contour des nœuds sur le fond du Shader Editor, plus une marge ;
#   ("props", y0[, y1])     : l'éditeur de propriétés, de y0 jusqu'au dernier panneau (ou jusqu'à y1) ;
#   ("menu", marge)         : le menu ouvert, isolé par différence avec la capture « _avant » ;
#   ("zone", nom)           : une région entière (PROPERTIES, FILE_BROWSER_UI…), d'après le JSON ;
#   (x0, y0, x1, y1)        : rectangle fixe (pixels, origine en haut à gauche) ;
#   "meme"                  : le même rectangle que le morceau précédent.
# Options d'une figure : "flou" (rectangles floutés avant découpe : chemins du poste), "medaillon"
# (un petit panneau agrandi, posé dans un coin de la figure).

import json
import os
import sys

import bpy
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
IMG = os.path.join(ROOT, "assets", "images")
args = sys.argv[sys.argv.index("--") + 1:]
SRC = args[0]
ONLY = set(args[1:])
SIDE, FULL = 600, 1200


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


def blur(px, r, k=9):
    x0, y0, x1, y1 = r
    reg = px[y0:y1, x0:x1, :3]
    for _ in range(3):
        pad = np.pad(reg, ((k, k), (k, k), (0, 0)), mode='edge')
        acc = np.zeros_like(reg)
        for d in range(-k, k + 1):
            acc += pad[k + d:k + d + reg.shape[0], k:k + reg.shape[1]]
        reg = acc / (2 * k + 1)
        pad = np.pad(reg, ((k, k), (k, k), (0, 0)), mode='edge')
        acc = np.zeros_like(reg)
        for d in range(-k, k + 1):
            acc += pad[k:k + reg.shape[0], k + d:k + d + reg.shape[1]]
        reg = acc / (2 * k + 1)
    px[y0:y1, x0:x1, :3] = reg


def rect_of(name, spec, px):
    kind = spec[0]
    if kind in ("vue", "noeuds"):
        marge = spec[1]
        key = "VIEW_3D" if kind == "vue" else "NODE_EDITOR"
        r = info(name)[key]
        if kind == "vue":
            x0, y0, x1, y1 = r[0] + 74, r[1] + 66, r[2] - 12, r[3] - 6
            thr = 0.06
        else:
            x0, y0, x1, y1 = r[0] + 6, r[1] + 70, r[2] - 14, r[3] - 14
            thr = 0.14
        reg = px[y0:y1, x0:x1, :3]
        bg = np.median(np.concatenate([reg[:6].reshape(-1, 3), reg[-6:].reshape(-1, 3)]), axis=0)
        mask = np.abs(reg - bg).max(axis=2) > thr
        bx0, by0, bx1, by1 = bbox(mask)
        return (max(x0, x0 + bx0 - marge), max(y0, y0 + by0 - marge), min(x1, x0 + bx1 + marge), min(y1, y0 + by1 + marge))
    if kind == "props":
        x0, ry0, x1, y1 = info(name)["PROPERTIES"]
        y0 = spec[1]
        if len(spec) > 2:
            return (x0, y0, x1 - 4, spec[2])
        reg = px[y0:y1 - 20, x0:x1, :3]
        bg = np.median(reg[-15:, 10:200].reshape(-1, 3), axis=0)
        rows = np.nonzero(np.abs(reg[:, 8:-30] - bg).max(axis=2).max(axis=1) > 0.03)[0]
        return (x0, y0, x1 - 4, y0 + rows.max() + 10)
    if kind == "menu":
        avant = spec[2] if len(spec) > 2 else name + "_avant"
        before = load(avant)
        d = np.abs(px[..., :3] - before[..., :3]).max(axis=2) > 0.08
        d[:30, :] = False
        d[928:, :] = False
        bx0, by0, bx1, by1 = bbox(d)
        m = spec[1]
        return (max(0, bx0 - m), max(0, by0 - m), min(px.shape[1], bx1 + m), min(px.shape[0], by1 + m))
    if kind == "zone":
        return tuple(info(name)[spec[1]])
    if kind == "boite":
        # la boîte des nœuds mesurée à l'écran au moment de la capture, plus une marge
        x0, y0, x1, y1 = info(name)["NODES_BOX"]
        m = spec[1]
        return (max(0, x0 - m), max(0, y0 - m), min(px.shape[1], x1 + m), min(px.shape[0], y1 + m))
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


def resize(px, k):
    h, w = px.shape[:2]
    im = bpy.data.images.new("tmp", w, h, alpha=False)
    im.pixels = px[::-1].ravel()
    im.scale(int(round(w * k)), int(round(h * k)))
    w2, h2 = im.size
    out = np.array(im.pixels[:], dtype=np.float32).reshape(h2, w2, 4)[::-1].copy()
    bpy.data.images.remove(im)
    return out


def inset(fig, part, corner="tr", border=3):
    """Médaillon : un morceau agrandi, encadré de blanc, posé dans un coin de la figure."""
    h, w = part.shape[:2]
    framed = np.ones((h + 2 * border, w + 2 * border, 4), dtype=np.float32)
    framed[border:border + h, border:border + w] = part
    fh, fw = framed.shape[:2]
    m = 14
    y = m if corner[0] == "t" else fig.shape[0] - fh - m
    x = fig.shape[1] - fw - m if corner[1] == "r" else m
    fig[y:y + fh, x:x + fw] = framed
    return fig


def save(px, name, max_w):
    h, w = px.shape[:2]
    im = bpy.data.images.new("fig", w, h, alpha=False)
    im.pixels = px[::-1].ravel()
    if w > max_w:
        im.scale(max_w, int(round(h * max_w / w)))
    path = os.path.join(IMG, name)
    im.filepath_raw = path
    im.file_format = 'JPEG'
    im.save(filepath=path, quality=92)
    print("FIGURE", name, im.size[0], "x", im.size[1])
    bpy.data.images.remove(im)
    return path


P = 330     # haut de l'éditeur de propriétés (sous son en-tête), espace Layout des captures
# (fichier, rangées de morceaux, largeur maximale, options)
FIGS = {
    "3.1": ("lamp_cmf_target_blender.jpg", [[("301_deux_coloris", ("vue", 30))]], FULL, {}),
    "3.2": ("material_preview_button_blender.jpg", [[("302_material_preview", ("vue", 30))]], FULL,
            {"medaillon": ("302_material_preview", (928, 34, 1012, 62), 3.0, "tl")}),
    "3.3": ("material_preview_popover_blender.jpg", [[("303_popover", (880, 22, 1200, 355))]], SIDE, {}),
    "3.4": ("material_tab_new_blender.jpg", [[("304_onglet_material_vide", ("props", P, 520))]], SIDE, {}),
    "3.5": ("material_tab_surface_blender.jpg", [[("305_rubrique_surface", ("props", P))]], SIDE, {}),
    "3.6": ("material_browse_list_blender.jpg", [[("306_liste", (1058, 480, 1598, 822))]], SIDE, {}),
    "3.7": ("link_materials_menu_blender.jpg", [[("317_menu_link", ("menu", 10))]], SIDE, {}),
    "3.8": ("metallic_roughness_grid_blender.jpg", [[("307_grille", (80, 372, 1000, 585))]], FULL, {}),
    "3.9": ("principled_coat_panel_blender.jpg", [[("308_coat", (1062, 330, 1590, 850)), ("308_coat", (180, 100, 800, 820))]], FULL, {}),
    "3.10": ("principled_transmission_blender.jpg", [[("309_transmission", ("props", P, 928))]], SIDE, {}),
    "3.11": ("glass_raytracing_comparison_blender.jpg", [[("310_ampoule_a", (230, 240, 860, 760)), ("310_ampoule_b", "meme"),
                                                            ("310_ampoule_c", "meme")]], FULL, {}),
    "3.12": ("render_raytracing_checkbox_blender.jpg", [[("311_onglet_render", ("props", P))]], SIDE, {}),
    "3.13": ("material_settings_transmission_blender.jpg", [[("312_settings", ("props", P, 720))]], SIDE, {}),
    "3.14": ("principled_thin_wall_blender.jpg", [[("313_thin_wall", ("props", 330, 860))]], SIDE, {}),
    "3.15": ("principled_emission_panel_blender.jpg", [[("314_emission", (1062, 655, 1590, 760))], [("314_emission", (640, 230, 1000, 470))]], SIDE, {}),
    "3.16": ("material_slots_two_blender.jpg", [[("315_deux_emplacements", (1062, 330, 1590, 470)), ("315_deux_emplacements", (200, 90, 830, 690))]], FULL, {}),
    "3.17": ("solidify_material_offset_blender.jpg", [[("316_solidify_materials", ("props", P, 860))]], SIDE, {}),
    "3.18": ("shading_workspace_blender.jpg", [[("318_espace_shading", (0, 0, 1600, 960))]], FULL,
             {"flou": [("318_espace_shading", (150, 70, 242, 112)), ("318_espace_shading", (2, 151, 242, 481))]}),
    "3.19": ("principled_node_vs_tab_blender.jpg", [[("319_noeuds", ("boite", 14)), ("319_noeud_et_onglet", (1352, 470, 1598, 760))]], FULL, {}),
    "3.20": ("shader_editor_add_menu_blender.jpg", [[("320_menu_add", ("menu", 8, "320_menu_add_avant")),
                                                     ("320_menu_texture", ("menu", 8, "320_menu_add_avant"))]], FULL, {}),
    "3.21": ("node_link_noise_base_color_blender.jpg", [[("321_noeuds", ("boite", 14)), ("321_bras", (360, 200, 660, 760))]], FULL, {}),
    "3.22": ("texture_coordinate_node_blender.jpg", [[("322_noeuds", ("boite", 14)), ("322_bras", (360, 200, 660, 760))]], FULL, {}),
    "3.23": ("noise_bump_chain_blender.jpg", [[("323_chaine_bump", ("boite", 14)), ("323_bras", (360, 200, 660, 760))]], FULL, {}),
    "3.24": ("brushed_aluminium_blender.jpg", [[("324_noeuds", ("boite", 14)), ("324_bras", (360, 200, 660, 760))]], FULL, {}),
    "3.25": ("image_texture_projection_menu_blender.jpg", [[("325_projection_menu", (650, 596, 912, 850))]], SIDE, {}),
    "3.26": ("image_texture_box_node_blender.jpg", [[("326_box_reglee", (650, 596, 912, 850))]], SIDE, {}),
    "3.27": ("leather_chain_armrest_blender.jpg", [[("326_chaine_cuir", ("boite", 14))]], FULL, {}),
    "3.28": ("box_blend_comparison_blender.jpg", [[("327c_blend_0", (760, 110, 1160, 370)), ("327c_blend_2", "meme")]], FULL, {}),
    "3.29": ("image_color_space_menu_blender.jpg", [[("328_color_space_menu", (650, 596, 912, 900))]], SIDE, {}),
    "3.30": ("texture_scale_not_applied_blender.jpg", [[("329_echelle_non_appliquee", (440, 70, 1080, 478)),
                                                        ("329_echelle_appliquee", "meme")]], FULL, {}),
    # le lot PBR du socle (étapes p1 à p5 de captures_brutes.py)
    "3.31": ("shader_add_normal_map_blender.jpg", [[("p2_menu_displacement", ("menu", 8, "p2_menu_displacement_avant"))]], SIDE, {}),
    "3.32": ("material_fake_user_shield_blender.jpg", [[("p1_bouclier", ("props", P, 520))]], SIDE, {}),
    "3.33": ("pbr_chain_overview_blender.jpg", [[("p3_chaine_pbr", ("boite", 14))]], FULL, {}),
    "3.34": ("pbr_maps_closeup_blender.jpg", [[("p3_gros_plan_diff", ("boite", 14)), ("p3_gros_plan_nor", ("boite", 14))]], FULL, {}),
    "3.35": ("pbr_socle_lots_comparison_blender.jpg", [[("p4_quatre_socles", ("vue", 30))]], FULL, {}),
    "3.37": ("node_wrangler_principled_setup_blender.jpg", [[("p5_node_wrangler", (305, 200, 1294, 781))]], FULL,
             {"medaillon": ("p5_node_wrangler", (316, 356, 456, 440), 2.0, "bl")}),
    "3.38": ("file_external_data_pack_blender.jpg", [[("344_external_data", ("menu", 8))]], SIDE, {}),
    "3.36": ("preferences_node_wrangler_blender.jpg", [[("330_node_wrangler", (10, 70, 640, 360))]], SIDE, {}),
    "3.40": ("material_mark_as_asset_blender.jpg", [[("331_menu_mark", (1004, 448, 1598, 690))]], SIDE, {}),
    "3.41": ("asset_browser_editor_type_blender.jpg", [[("332_type_editeur", (10, 616, 960, 900))]], FULL, {}),
    "3.42": ("asset_browser_overview_blender.jpg", [[("333_asset_browser", ("zone", "FILE_BROWSER_AREA"))]], FULL, {}),
    "3.43": ("asset_catalog_new_blender.jpg", [[("333_asset_browser", (2, 535, 300, 730))]], SIDE, {}),
    "3.44": ("asset_metadata_sidebar_blender.jpg", [[("333_asset_browser", (715, 535, 1012, 928))]], SIDE, {}),
    "3.45": ("asset_drag_drop_material_blender.jpg", [[("338_glisser", (2, 100, 1012, 720))]], FULL, {}),
    "3.46": ("file_menu_link_append_blender.jpg", [[("340_menu_file", ("menu", 8))]], SIDE, {}),
    "3.47": ("file_append_blend_folders_blender.jpg", [[("341_append_dossiers", (0, 0, 1025, 430))]], FULL,
             {"flou": [("341_append_dossiers", (195, 10, 768, 42))]}),
    "3.48": ("preferences_asset_libraries_blender.jpg", [[("336_asset_libraries", (10, 66, 1003, 380))]], FULL,
             {"flou": [("336_asset_libraries", (415, 286, 965, 310))]}),
    "3.49": ("asset_library_selector_blender.jpg", [[("337_bibliotheques", ("menu", 8))]], SIDE, {}),
    "3.50": ("asset_import_method_menu_blender.jpg", [[("339_import_liste", (290, 500, 720, 700))]], SIDE, {}),
    "3.51": ("outliner_collection_menu_blender.jpg", [[("345_menu_collection", (936, 88, 1253, 365))]], SIDE, {}),
    "3.52": ("lamp_two_colorways_blender.jpg", [[("343_coloris_face", ("vue", 30))]], FULL, {}),
    "3.53": ("linked_material_readonly_blender.jpg", [[("342_matiere_liee", ("props", P, 860))]], SIDE, {}),
    "3.39": ("cmf_swatch_library_blender.jpg", [[("300_nuancier", (76, 98, 1010, 892))]], FULL, {}),
}


def build(key):
    fname, rows, max_w, opts = FIGS[key]
    flous = {}
    for cap, r in opts.get("flou", []):
        flous.setdefault(cap, []).append(r)
    out_rows = []
    last = None
    for row in rows:
        parts = []
        for name, spec in row:
            px = load(name)
            for r in flous.get(name, []):
                blur(px, r)
            r = last if spec == "meme" else rect_of(name, spec, px)
            last = r
            x0, y0, x1, y1 = [int(v) for v in r]
            parts.append(px[y0:y1, x0:x1])
        out_rows.append(hconcat(parts))
    fig = vconcat(out_rows)
    if "medaillon" in opts:
        cap, r, k, corner = opts["medaillon"]
        px = load(cap)
        x0, y0, x1, y1 = r
        fig = inset(fig, resize(px[y0:y1, x0:x1], k), corner)
    return save(fig, fname, max_w)


if __name__ == "__main__":       # importé par recadrer_defi.py pour ses outils, sans rien recadrer
    for key in FIGS:
        if ONLY and key not in ONLY:
            continue
        try:
            build(key)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("ECHEC", key, repr(e))
