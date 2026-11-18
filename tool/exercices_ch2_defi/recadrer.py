# Recadre les captures brutes de captures_brutes.py et écrit les figures JPEG dans assets/images/.
#
# Usage :
#   blender.exe -b --factory-startup --python tool\exercices_ch2_defi\recadrer.py -- <dossier_captures_brutes> [figure ...]
#
# Modes de recadrage (coordonnées en pixels, origine en haut à gauche, fenêtre de 1600 x 960) :
#   ("vue", marge)        : contour des objets sur le fond uni de la vue 3D, plus une marge ;
#   ("props", y_min)      : l'éditeur de propriétés, du haut des panneaux au dernier panneau ;
#   (x0, y0, x1, y1)      : rectangle fixe.

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

VIEW = (75, 100, 975, 895)     # zone utile de la vue 3D (sans barre d'outils, en-tête ni bouton Options)
PROPS = (1024, 232, 1598, 930)  # éditeur de propriétés élargi, sans la colonne d'onglets


def load(name):
    im = bpy.data.images.load(os.path.join(SRC, name + ".png"))
    w, h = im.size
    px = np.array(im.pixels[:], dtype=np.float32).reshape(h, w, 4)[::-1]   # haut en premier
    bpy.data.images.remove(im)
    return px


def bbox(mask):
    ys, xs = np.nonzero(mask)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def crop(px, spec):
    if spec[0] == "vue":
        marge = spec[1]
        x0, y0, x1, y1 = VIEW
        reg = px[y0:y1, x0:x1, :3]
        bg = np.median(np.concatenate([reg[:6].reshape(-1, 3), reg[-6:].reshape(-1, 3)]), axis=0)
        mask = np.abs(reg - bg).max(axis=2) > 0.06
        bx0, by0, bx1, by1 = bbox(mask)
        r = (max(x0, x0 + bx0 - marge), max(y0, y0 + by0 - marge), min(x1, x0 + bx1 + marge), min(y1, y0 + by1 + marge))
    elif spec[0] == "props":
        x0, y0, x1, y1 = PROPS
        y0 = spec[1] if len(spec) > 1 else y0
        reg = px[y0:y1, x0:x1, :3]
        bg = np.median(reg[-12:, 10:200].reshape(-1, 3), axis=0)
        # sans les bords (barre de défilement à droite)
        rows = np.nonzero(np.abs(reg[:, 8:-30] - bg).max(axis=2).max(axis=1) > 0.05)[0]
        print("PROPS fond", bg, "dernière ligne", rows.max())
        r = (x0 - 4, y0, x1, y0 + rows.max() + 12)
    else:
        r = spec
    x0, y0, x1, y1 = [int(v) for v in r]
    return px[y0:y1, x0:x1]


def hconcat(parts, gap=8):
    h = max(p.shape[0] for p in parts)
    out = []
    for i, p in enumerate(parts):
        if p.shape[0] < h:
            pad = np.ones((h - p.shape[0], p.shape[1], 4), dtype=np.float32)
            pad[..., :3] = p[0, 0, :3]
            p = np.concatenate([p, pad], axis=0)
        out.append(p)
        if i < len(parts) - 1:
            out.append(np.ones((h, gap, 4), dtype=np.float32))
    return np.concatenate(out, axis=1)


def save(px, name, max_w):
    h, w = px.shape[:2]
    im = bpy.data.images.new(name, w, h, alpha=False)
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


# figure : (fichier de sortie, [(capture, recadrage), ...], largeur maxi)
FIG = {
    "2.33": ("modeling_challenge_overview_blender.jpg", [("233_overview", ("vue", 30))], 1200),
    "2.34": ("subdivision_holding_loops_crease_blender.jpg",
             [("234_carters_studio", ("vue", 40)), ("234_carters_matcap", ("vue", 40))], 1200),
    "2.35": ("loop_cut_holding_loop_blender.jpg", [("235_boucle_maintien_edition", ("vue", 20))], 640),
    "2.36": ("edge_menu_edge_crease_blender.jpg", [("236_menu_edge_crease", (330, 100, 800, 800))], 640),
    "2.37": ("subdivision_advanced_use_creases_blender.jpg", [("../captures_clics/c237_advanced", ("props",))], 640),
    "2.38": ("crease_hood_character_line_blender.jpg", [("238_capot_crease", ("vue", 30))], 640),
    "2.39": ("shrinkwrap_principle_flat_vs_wrapped_blender.jpg",
             [("239_trappes_face", ("vue", 40)), ("239_trappe_plate_profil", (330, 180, 720, 900)),
              ("239_trappe_conformee_profil", (330, 180, 720, 900))], 1200),
    "2.40": ("add_modifier_deform_menu_blender.jpg", [("240_menu_deform", (700, 180, 1250, 900))], 640),
    "2.41": ("shrinkwrap_panel_default_blender.jpg", [("241_panneau_shrinkwrap", ("props",))], 640),
    "2.42": ("shrinkwrap_offset_z_fighting_blender.jpg",
             [("242_offset_0", (120, 250, 860, 760)), ("242_offset_02", (120, 250, 860, 760))], 1200),
    "2.43": ("shrinkwrap_solidify_stack_order_blender.jpg",
             [("243_pile_solidify_dessous", ("vue", 30)), ("243_pile_solidify_dessus", ("vue", 30))], 1200),
    "2.44": ("shrinkwrap_snap_mode_menu_blender.jpg", [("244_menu_snap_mode", (1024, 232, 1598, 700))], 640),
    "2.45": ("porthole_frame_fuselage_blender.jpg",
             [("245_cadre_on_surface", ("vue", 40)), ("245_cadre_above_surface", ("vue", 40))], 1200),
    "2.46": ("shrinkwrap_project_panel_blender.jpg", [("246_panneau_project", ("props",))], 640),
    "2.47": ("tram_nose_band_project_vs_nearest_blender.jpg",
             [("247_bandeau_project_face", ("vue", 10)), ("247_bandeau_nearest_face", ("vue", 10))], 1200),
    "2.48": ("vertex_group_menu_ctrl_g_blender.jpg", [("248_menu_ctrl_g", (200, 150, 800, 650))], 640),
    "2.49": ("vertex_groups_panel_weight_blender.jpg", [("249_panneau_vertex_groups", (1020, 232, 1598, 632))], 640),
    "2.50": ("hood_scoop_vertex_group_blender.jpg", [("250_trois_prises", ("vue", 20))], 1200),
    "2.51": ("shrinkwrap_four_modes_blender.jpg", [("251_quatre_modes_dessus", ("vue", 30))], 1200),
    "2.52": ("shrinkwrap_subdivision_order_blender.jpg",
             [("252_cadre8_seul", ("vue", 30)), ("252_cadre8_simple_dessus", ("vue", 30)),
              ("252_cadre8_cc_dessous", ("vue", 30))], 1200),
    # palier 2 et atelier (captures de captures_brutes4 et captures_clics)
    "2.53": ("boolean_panel_difference_solver_blender.jpg", [("../captures_brutes4/253_panneau_boolean", ("props",))], 640),
    "2.54": ("object_viewport_display_as_blender.jpg", [("../captures_clics/c254_viewport_display", (1020, 455, 1598, 872))], 640),
    "2.55": ("object_visibility_renders_blender.jpg", [("../captures_clics/c255_visibility", (1020, 500, 1598, 915))], 640),
    "2.56": ("boolean_bevel_order_blender.jpg",
             [("../captures_brutes4/256_bevel_dessus", (150, 160, 830, 760)),
              ("../captures_brutes4/256_bevel_dessous", (150, 160, 830, 760))], 1200),
    "2.57": ("boolean_cutter_reference_surface_blender.jpg",
             [("../captures_brutes4/257_coupe_sur_reference", (60, 160, 900, 820)),
              ("../captures_brutes4/257_coupe_sur_reference", ("props",))], 1200),
    "2.58": ("boolean_shading_vs_data_transfer_blender.jpg",
             [("../captures_brutes4/258_brut", (190, 150, 790, 750)),
              ("../captures_brutes4/258_propre", (190, 150, 790, 750))], 1200),
    "2.59": ("add_modifier_edit_menu_blender.jpg", [("../captures_brutes4/259_menu_edit", (840, 230, 1330, 620))], 640),
    "2.60": ("data_transfer_panel_custom_normals_blender.jpg",
             [("../captures_clics/c260_face_corner", (1020, 232, 1598, 930)),
              ("../captures_clics/c260_topology", (1020, 700, 1598, 930))], 1200),
    "2.61": ("matcap_reflection_check_blender.jpg", [("../captures_brutes4/261_matcap_reflection", (620, 60, 990, 800))], 640),
    "2.62": ("add_modifier_normals_menu_blender.jpg", [("../captures_brutes4/262_menu_normals", (840, 250, 1330, 470))], 640),
    "2.63": ("weighted_normal_plate_blender.jpg",
             [("../captures_brutes4/263_platine_sans", ("vue", 30)), ("../captures_brutes4/263_platine_wn", ("vue", 30))], 1200),
    "2.64": ("side_mirror_workshop_blender.jpg",
             [("../captures_brutes4/264_retro_arriere", ("vue", 30)),
              ("../captures_brutes4/264_retro_avant", ("vue", 30))], 1200),
    "2.65": ("side_mirror_convex_reference_blender.jpg", [("../captures_brutes4/265_miroir_reference", (130, 150, 900, 760))], 640),
    "2.66": ("side_mirror_indicator_recess_blender.jpg",
             [("../captures_brutes4/266_logement_sans", (130, 150, 900, 760)),
              ("../captures_brutes4/266_logement_dt", (130, 150, 900, 760))], 1200),
}

for key, (out, parts, max_w) in FIG.items():
    if ONLY and key not in ONLY:
        continue
    try:
        imgs = [crop(load(src), spec) for src, spec in parts]
        save(hconcat(imgs) if len(imgs) > 1 else imgs[0], out, max_w)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("ECHEC", key, e)
