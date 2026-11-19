# Recadre les captures brutes de captures_defi.py et les rendus de rendus_figures_defi.py, et écrit les
# figures 3.48 à 3.96 du défi procédural (section 4 du chapitre 3) dans assets/images/.
# Reprend les outils de recadrer.py (morceaux, menus isolés par différence, boîtes de nœuds).
#
# Usage, depuis la racine du dépôt :
#   blender.exe -b --factory-startup --python tool\exercices_ch3\recadrer_defi.py -- <dossier_captures_brutes> [figure ...]
#
# Modes de morceau ajoutés :
#   ("rendu", marge)                     : contour de la pièce sur le fond uni d'un rendu, plus une marge ;
#   ("menu_part", marge, avant, f0, f1)  : la partie d'un menu entre les fractions f0 et f1 de sa hauteur ;
#   ("zone_h", région, hauteur)          : le haut d'une région de l'interface, sur la hauteur donnée.
# Les figures pleine largeur font au plus 1400 px de large : elles s'affichent à 0,51 au moins.

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recadrer as Rc   # noqa: E402

ONLY = Rc.ONLY
SIDE, FULL = 600, 1400


def rect_of(name, spec, px):
    kind = spec[0] if isinstance(spec, tuple) else None
    if kind == "rendu":
        m = spec[1]
        bg = np.median(np.concatenate([px[:4, :, :3].reshape(-1, 3), px[-4:, :, :3].reshape(-1, 3)]), axis=0)
        mask = np.abs(px[..., :3] - bg).max(axis=2) > 0.03
        x0, y0, x1, y1 = Rc.bbox(mask)
        return (max(0, x0 - m), max(0, y0 - m), min(px.shape[1], x1 + m), min(px.shape[0], y1 + m))
    if kind == "menu_part":
        x0, y0, x1, y1 = Rc.rect_of(name, ("menu", spec[1], spec[2]), px)
        h = y1 - y0
        return (x0, y0 + int(h * spec[3]), x1, y0 + int(h * spec[4]))
    if kind == "zone_h":
        x0, y0, x1, _y1 = Rc.info(name)[spec[1]]
        return (x0, y0, x1, y0 + spec[2])
    return Rc.rect_of(name, spec, px)


def tiles(names, m=10):
    return [(n, ("rendu", m)) for n in names]


B, M = ("boite", 14), ("boite", 12)
FIGS = {
    "3.48": ("procedural_challenge_overview_blender.jpg", [[("r_overview", ("rendu", 24))]], FULL),
    "3.49": ("shader_add_submenus_blender.jpg", [[("u_menu_" + k, ("menu", 8, "u_menus_avant"))
                                                   for k in ("color", "math", "vector", "displacement")]], FULL),
    "3.50": ("node_preview_ctrl_shift_click_blender.jpg", [[("u_preview", B), ("r_e1_noise", ("rendu", 12))]], FULL),
    "3.51": ("noise_texture_node_blender.jpg", [[("u_noise", M), ("u_noise_menu", ("menu", -1, "u_noise"))]], SIDE),
    "3.52": ("noise_settings_comparison_blender.jpg", [tiles(["r_e1_noise_defaut", "r_e1_noise", "r_e1_noise_detail",
                                                              "r_e1_noise_distortion", "r_e1_noise_ridged"])], FULL),
    "3.53": ("voronoi_texture_node_blender.jpg", [[("u_voronoi", M), ("u_voronoi_menu", ("menu", -1, "u_voronoi"))]], SIDE),
    "3.54": ("voronoi_comparison_blender.jpg", [tiles(["r_e1_voronoi", "r_e1_voronoi_bords", "r_e1_voronoi_couleur"])], FULL),
    "3.55": ("wave_texture_node_blender.jpg", [[("u_wave", M)]], SIDE),
    "3.56": ("wave_comparison_blender.jpg", [tiles(["r_e1_wave", "r_e1_wave_ondule", "r_e1_wave_anneaux"])], FULL),
    "3.57": ("gabor_texture_node_blender.jpg", [[("u_gabor", M)]], SIDE),
    "3.58": ("gabor_comparison_blender.jpg", [tiles(["r_e1_gabor", "r_e1_gabor_serre", "r_e1_gabor_isotrope"])], FULL),
    "3.59": ("step1_target_tiles_blender.jpg", [tiles(["r_e1_voronoi_bords", "r_e1_wave_anneaux", "r_e1_gabor_axe_x"])], FULL),
    "3.60": ("color_ramp_node_blender.jpg", [[("u_ramp", M), ("u_ramp_menu", ("menu", -1, "u_ramp"))]], SIDE),
    "3.61": ("color_ramp_comparison_blender.jpg", [tiles(["r_e2_brut", "r_e2_contraste", "r_e2_constant"])], FULL),
    "3.62": ("speckled_plastic_blender.jpg", [[("u_mouchete", B), ("r_e2_coque", ("rendu", 12))]], FULL),
    "3.63": ("map_range_node_blender.jpg", [[("u_maprange", M)]], SIDE),
    "3.64": ("uneven_gloss_dashboard_blender.jpg", [[("u_planche", B), ("r_e2_planche", ("rendu", 12))]], FULL),
    "3.65": ("math_node_operations_blender.jpg", [[("u_math", M), ("u_math_menu", ("menu_part", -1, "u_math", 0.0, 0.78))]], FULL),
    "3.66": ("mix_color_and_float_nodes_blender.jpg", [[("u_mix", ("boite", 4))]], SIDE),
    "3.67": ("separate_xyz_node_blender.jpg", [[("u_sepxyz", M)]], SIDE),
    "3.68": ("one_mask_three_mixes_blender.jpg", [[("u_patine", B)]], FULL),
    "3.69": ("patina_handrail_comparison_blender.jpg", [[("r_e3_partout", ("rendu", 10))],
                                                        [("r_e3_extremites", ("rendu", 10))]], FULL),
    "3.70": ("bump_node_settings_blender.jpg", [[("u_bump", M)]], SIDE),
    "3.71": ("chained_bump_nodes_blender.jpg", [[("u_bumps", B), ("r_e4_boitier", ("rendu", 12))]], FULL),
    "3.72": ("principled_coat_normal_blender.jpg", [[("u_coat", B)]], FULL),
    "3.73": ("orange_peel_comparison_blender.jpg", [[("r_e4_coque_lisse", (0, 0, 560, 460)),
                                                     ("r_e4_coque_o15", "meme"), ("r_e4_coque_o30", "meme")]], FULL),
    "3.74": ("edge_wear_normal_chain_blender.jpg", [[("u_bords", B)]], FULL),
    "3.75": ("vector_math_node_blender.jpg", [[("u_vecmath", M)]], SIDE),
    "3.76": ("edge_wear_mask_comparison_blender.jpg", [tiles(["r_e5_socle_masque", "r_e5_socle_use", "r_e5_coffret",
                                                              "r_e5_socle_faux"], 12)], FULL),
    "3.77": ("ambient_occlusion_node_blender.jpg", [[("u_ao", M)]], SIDE),
    "3.78": ("dirt_crevices_comparison_blender.jpg", [tiles(["r_e5_ao_brut", "r_e5_ao_rampe", "r_e5_salete"], 12)], FULL),
    "3.79": ("scratches_handrail_blender.jpg", [[("r_e5_rayures_masque", ("rendu", 10))],
                                                [("r_e5_rayures", ("rendu", 10))]], FULL),
    "3.80": ("fingerprints_piano_black_blender.jpg", [tiles(["r_e5_console_neuve", "r_e5_console_traces"], 12)], FULL),
    "3.81": ("procedural_patterns_overview_blender.jpg", [tiles(["r_e6_dalle", "r_e6_tole", "r_e6_cuir"], 12),
                                                          tiles(["r_e6_tissu", "r_e6_molette", "r_e6_carbone"], 12)], FULL),
    "3.82": ("perforated_sheet_alpha_blender.jpg", [[("u_tole", B), ("r_e6_tole", ("rendu", 12))]], FULL),
    "3.83": ("leather_grain_procedural_blender.jpg", [[("u_cuir", B), ("r_e6_cuir", ("rendu", 12))]], FULL),
    "3.84": ("checker_texture_node_blender.jpg", [[("u_checker", M)]], SIDE),
    "3.85": ("seat_fabric_weave_blender.jpg", [[("u_tissu", B)]], FULL),
    "3.86": ("gradient_texture_radial_blender.jpg", [[("u_gradient", M), ("u_gradient_menu", ("menu", -1, "u_gradient"))]], SIDE),
    "3.87": ("knurling_procedural_blender.jpg", [[("u_molette", B)]], FULL),
    "3.88": ("carbon_twill_procedural_blender.jpg", [[("u_carbone", B)]], FULL),
    "3.89": ("node_make_group_menu_blender.jpg", [[("u_node_menu", ("menu_part", 4, "u_node_menu_avant", 0.577, 0.952))]], SIDE),
    "3.90": ("node_group_inside_blender.jpg", [[("u_group_inside", B)]], FULL),
    "3.91": ("node_group_sidebar_interface_blender.jpg", [[("u_sidebar_group", ("zone_h", "NODE_EDITOR_UI", 540))]], SIDE),
    "3.92": ("add_menu_group_list_blender.jpg", [[("u_add_group", ("menu", 8, "u_add_group_avant"))]], SIDE),
    "3.93": ("node_group_in_use_blender.jpg", [[("u_group_use", B)]], FULL),
    "3.94": ("node_frame_label_blender.jpg", [[("u_frame", M), ("u_frame", ("zone_h", "NODE_EDITOR_UI", 370))]], FULL),
    "3.95": ("node_group_mark_as_asset_blender.jpg", [[("u_outliner_menu", (0, 66, 520, 600))]], SIDE),
    "3.96": ("workshop_lamp_wear_blender.jpg", [[("r_lampe_neuve", ("rendu", 16)), ("r_lampe_atelier", ("rendu", 16)),
                                                 ("r_lampe_socle", ("rendu", 12))]], FULL),
}


def build(key):
    fname, rows, max_w = FIGS[key]
    out_rows = []
    last = None
    for row in rows:
        parts = []
        for name, spec in row:
            px = Rc.load(name)
            r = last if spec == "meme" else rect_of(name, spec, px)
            last = r
            x0, y0, x1, y1 = [int(v) for v in r]
            parts.append(px[y0:y1, x0:x1])
        out_rows.append(Rc.hconcat(parts))
    fig = Rc.vconcat(out_rows)
    return Rc.save(fig, fname, max_w)


for key in FIGS:
    if ONLY and key not in ONLY:
        continue
    try:
        build(key)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("ECHEC", key, repr(e))
