# Recettes des matières du chapitre 3, communes aux scripts de construction (fiches A, A2, B et C du
# plan _resources/plans/PRC02-plan-chap3.md). Importé par les scripts du dossier : sys.path.insert(0, HERE).
#
# Toutes les chaînes partent de Texture Coordinate, sortie Object : aucune pièce n'a de dépliage UV.
# Les couleurs sont données en hexadécimal sRGB, comme dans le sélecteur de couleur de Blender, et
# converties en valeurs linéaires pour Base Color.

import os

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "textures_cmf")
AUTHOR = "VIV Formation"
LICENSE = "CC0 1.0"

# Catalogues : UUID fixes, pour que les fichiers d'un même dossier partagent le même rangement.
CATS_BIBLIO = {
    "Métaux": "6f1c2a4e-3b7d-4c11-9a01-0c3e5b7d9a10",
    "Plastiques": "6f1c2a4e-3b7d-4c11-9a01-0c3e5b7d9a20",
    "Peintures": "6f1c2a4e-3b7d-4c11-9a01-0c3e5b7d9a30",
    "Verres": "6f1c2a4e-3b7d-4c11-9a01-0c3e5b7d9a40",
    "Finitions texturées": "6f1c2a4e-3b7d-4c11-9a01-0c3e5b7d9a50",
}
CATS_LAMPE = {
    "Métaux": "8a2d3f60-1e4b-4d7a-b2c3-5f6e7d8c9b01",
    "Plastiques et peintures": "8a2d3f60-1e4b-4d7a-b2c3-5f6e7d8c9b02",
    "Verres": "8a2d3f60-1e4b-4d7a-b2c3-5f6e7d8c9b03",
}

IMAGES = {  # nom : espace colorimétrique
    "grain_structure": "Non-Color",
    "grain_cuir": "Non-Color",
    "carbone_serge_couleur": "sRGB",
    "carbone_serge_relief": "Non-Color",
    "tole_larmee": "Non-Color",
}

# ---------------------------------------------------------------------------- la bibliothèque (fiche B)
# nom : (catalogue, couleur, metallic, roughness, réglages, étiquettes, description)
#   réglages : coat=(poids, roughness) ; glass=(ior, thin_wall) ; noise=(scale, detail, distance, mapping) ;
#              image=(nom, blend, mapping, distance) ; voronoi=(scale, distance) ; carbone=True
BIBLIO = {
    "Alu_Naturel": ("Métaux", "E6E7E8", 1, 0.3, {}, ["aluminium", "automobile", "aéronautique"],
                    "Aluminium naturel. Jante, carénage, bras de lampe."),
    "Alu_Brosse": ("Métaux", "E6E7E8", 1, 0.3, {"noise": (1000, 4, 0.00015, (1, 1, 0.02))},
                   ["aluminium", "brossé", "ferroviaire"],
                   "Aluminium brossé, rayé le long de l'axe Z de la pièce. Main courante, jante, bras de lampe."),
    "Alu_Microbille": ("Métaux", "D9DADB", 1, 0.5, {"noise": (2000, 4, 0.00003, None)}, ["aluminium", "microbillé"],
                       "Aluminium microbillé, mat et régulier. Boîtier, poignée, pièce d'instrument."),
    "Alu_Anodise_Bronze": ("Métaux", "8C6A4A", 1, 0.35, {}, ["aluminium", "anodisé"],
                           "Aluminium anodisé bronze. Enjoliveur, garniture de porte, accessoire de cabine."),
    "Alu_Anodise_Noir": ("Métaux", "2A2A2C", 1, 0.35, {}, ["aluminium", "anodisé"],
                         "Aluminium anodisé noir. Profilé, cadre d'écran, garniture de cabine."),
    "Inox_Poli": ("Métaux", "C8C8C6", 1, 0.08, {}, ["inox", "ferroviaire"],
                  "Inox poli. Main courante de train, équipement de galley, robinetterie."),
    "Chrome": ("Métaux", "C4C5C5", 1, 0.03, {}, ["chrome", "automobile"],
               "Chrome miroir. Calandre, logo, articulation de lampe."),
    "Laiton": ("Métaux", "E0C27A", 1, 0.25, {}, ["laiton"],
               "Laiton satiné. Douille, poignée, accessoire de luxe."),
    "Titane_Satine": ("Métaux", "A9A49C", 1, 0.4, {}, ["titane", "aéronautique"],
                      "Titane satiné. Pièce de structure, échappement, accessoire premium."),
    "ABS_Brillant_Noir": ("Plastiques", "1A1A1A", 0, 0.15, {}, ["ABS", "brillant"],
                          "ABS noir brillant. Coque de télécommande, enjoliveur, bouton."),
    "ABS_Graine_Noir": ("Plastiques", "1A1A1A", 0, 0.45, {"noise": (1500, 4, 0.00005, None)}, ["ABS", "grainé", "automobile"],
                        "ABS noir grainé. Planche de bord, coque de rétroviseur, tablette de siège."),
    "PP_Mat_Gris": ("Plastiques", "6E7072", 0, 0.6, {}, ["polypropylène", "mat"],
                    "Polypropylène gris mat. Garniture, bac, carter."),
    "PVC_Mat_Noir": ("Plastiques", "161616", 0, 0.7, {}, ["PVC", "câble"],
                     "PVC noir mat. Gaine de câble, jonc, profilé souple."),
    "Caoutchouc_Noir": ("Plastiques", "121212", 0, 0.85, {}, ["caoutchouc", "joint"],
                        "Caoutchouc noir. Joint de porte, pneu, patin."),
    "Laque_Rouge": ("Peintures", "A3161A", 0, 0.4, {"coat": (1, 0.03)}, ["laque", "automobile"],
                    "Laque rouge vernie. Carrosserie, livrée de train, carénage."),
    "Laque_Blanche": ("Peintures", "EDEDE8", 0, 0.4, {"coat": (1, 0.03)}, ["laque", "ferroviaire"],
                      "Laque blanche vernie. Caisse de train, fuselage, coque de lampe."),
    "Peinture_Structuree_Gris": ("Peintures", "4A4D50", 0, 0.6, {"image": ("grain_structure", 0.25, 50, 0.0002)},
                                 ["structurée", "ferroviaire"],
                                 "Peinture structurée grise, en projection Box. Socle, carter, panneau technique."),
    "Peinture_Metallisee_Bleu": ("Peintures", "1C3F7A", 1, 0.35, {"voronoi": (3000, 0.00002), "coat": (1, 0.02)},
                                 ["métallisée", "automobile"],
                                 "Peinture métallisée bleue vernie : des paillettes sous le vernis. Carrosserie."),
    "Verre_Clair": ("Verres", "FFFFFF", 0, 0.0, {"glass": (1.5, True)}, ["verre", "vitrage"],
                    "Verre clair à paroi fine (Thin Wall). Ampoule, vitre, pare-brise."),
    "Verre_Depoli": ("Verres", "FFFFFF", 0, 0.4, {"glass": (1.5, True)}, ["verre", "dépoli"],
                     "Verre dépoli à paroi fine. Ampoule, diffuseur, cloison vitrée."),
    "Verre_Fume": ("Verres", "5A5A5A", 0, 0.02, {"glass": (1.5, True)}, ["verre", "teinté", "aéronautique"],
                   "Verre fumé à paroi fine. Pare-soleil, hublot, toit vitré."),
    "Polycarbonate_Rouge": ("Verres", "C0141A", 0, 0.05, {"glass": (1.58, False)}, ["polycarbonate", "feu", "automobile"],
                            "Polycarbonate rouge en volume plein. Feu arrière, cabochon, voyant."),
    "Cuir_Graine_Noir": ("Finitions texturées", "1E1B19", 0, 0.55, {"image": ("grain_cuir", 0.3, 25, 0.0003)},
                         ["cuir", "sellerie", "aéronautique"],
                         "Cuir noir grainé, en projection Box. Accoudoir, siège, volant."),
    "Carbone_Serge": ("Finitions texturées", None, 0, 0.25, {"carbone": True, "coat": (1, 0.02)},
                      ["carbone", "aéronautique", "automobile"],
                      "Fibre de carbone en sergé 2 x 2, vernie. Panneau, coque, pièce de structure."),
    "Tole_Larmee": ("Finitions texturées", "9A9C9E", 1, 0.35, {"image": ("tole_larmee", 0.1, 8.33, 0.0008)},
                    ["tôle", "marchepied", "ferroviaire"],
                    "Tôle larmée en aluminium. Marchepied, plancher technique, passerelle."),
}

# ---------------------------------------------------------------------------- la lampe (fiches A et A2)
# coloris A, puis coloris B : (couleur, metallic, roughness, réglages)
LAMPE = {
    "Peinture_Vert": ("2F5D3A", 0, 0.4, {"coat": (1, 0.03)}),
    "Structure_Vert": ("2F5D3A", 0, 0.6, {"image": ("grain_structure", 0.25, 50, 0.0002)}),
    "ABS_Noir": ("1A1A1A", 0, 0.15, {"noise": (1500, 4, 0.00005, None)}),
    "Alu_Brosse": BIBLIO["Alu_Brosse"][1:5],
    "Chrome": BIBLIO["Chrome"][1:5],
    "PVC_Mat_Noir": BIBLIO["PVC_Mat_Noir"][1:5],
    "Verre_Clair": BIBLIO["Verre_Clair"][1:5],
    "Alu_Naturel": BIBLIO["Alu_Naturel"][1:5],
    "Structure_Blanche": ("EDEDE8", 0, 0.6, {"image": ("grain_structure", 0.25, 50, 0.0002)}),
    "Laque_Blanche": BIBLIO["Laque_Blanche"][1:5],
    "Alu_Anodise_Noir": ("2A2A2C", 1, 0.35, {"noise": (1000, 4, 0.00015, (1, 1, 0.02))}),
    "Laiton": BIBLIO["Laiton"][1:5],
    "Verre_Depoli": BIBLIO["Verre_Depoli"][1:5],
}
LAMPE_CATALOGUE = {
    "Peinture_Vert": "Plastiques et peintures", "Structure_Vert": "Plastiques et peintures",
    "ABS_Noir": "Plastiques et peintures", "PVC_Mat_Noir": "Plastiques et peintures",
    "Structure_Blanche": "Plastiques et peintures", "Laque_Blanche": "Plastiques et peintures",
    "Alu_Brosse": "Métaux", "Chrome": "Métaux", "Alu_Naturel": "Métaux", "Alu_Anodise_Noir": "Métaux",
    "Laiton": "Métaux", "Verre_Clair": "Verres", "Verre_Depoli": "Verres",
}
LAMPE_DESCRIPTION = {
    "Peinture_Vert": "Laque verte de la tête : Coat Weight 1, Coat Roughness 0,03.",
    "Structure_Vert": "Peinture structurée verte du socle, en projection Box.",
    "ABS_Noir": "ABS noir grainé : interrupteur et grille d'aération.",
    "Alu_Brosse": "Aluminium brossé. Bras de lampe ; convient aussi à une main courante ou à une jante.",
    "Chrome": "Chrome des articulations.",
    "PVC_Mat_Noir": "PVC noir mat du câble.",
    "Verre_Clair": "Verre clair de l'ampoule : Thin Wall et Raytraced Transmission.",
    "Alu_Naturel": "Aluminium naturel de la douille, récupéré du nuancier par File > Append.",
    "Structure_Blanche": "Coloris B : peinture structurée blanche du socle.",
    "Laque_Blanche": "Coloris B : laque blanche de la tête.",
    "Alu_Anodise_Noir": "Coloris B : aluminium anodisé noir, brossé, des bras.",
    "Laiton": "Coloris B : laiton des articulations et de la douille.",
    "Verre_Depoli": "Coloris B : verre dépoli de l'ampoule.",
}


# ---------------------------------------------------------------------------- outils
def lin(h):
    """Hexadécimal sRGB vers couleur linéaire (RGBA)."""
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (out[0], out[1], out[2], 1.0)


def image(name):
    """L'image de finition, empaquetée, au chemin relatif //textures_cmf/<nom>.png."""
    key = name + ".png"
    im = bpy.data.images.get(key)
    if im is None:
        im = bpy.data.images.load(os.path.join(TEX, key))
        im.name = key
        im.colorspace_settings.name = IMAGES[name]
        im.pack()
        im.filepath = "//textures_cmf/" + key
        for pf in im.packed_files:
            pf.filepath = "//textures_cmf/" + key
    return im


def nodes_of(mat):
    nt = mat.node_tree
    p = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED')
    o = next(n for n in nt.nodes if n.type == 'OUTPUT_MATERIAL')
    p.location = (0, 300)
    o.location = (330, 300)
    return nt, p, o


def coords(nt, x=-1150, y=150, mapping=None):
    """Texture Coordinate (Object), et un Mapping si demandé : renvoie la sortie à relier."""
    tc = nt.nodes.new("ShaderNodeTexCoord")
    tc.location = (x, y)
    out = tc.outputs["Object"]
    if mapping is not None:
        mp = nt.nodes.new("ShaderNodeMapping")
        mp.location = (x + 230, y)
        mp.inputs["Scale"].default_value = mapping
        nt.links.new(out, mp.inputs["Vector"])
        out = mp.outputs["Vector"]
    return out


def bump(nt, p, height_socket, distance, x=-300, y=-120):
    """Le relief se règle avec Strength, Distance gardant sa valeur par défaut (0,001) : sur une pièce de
    la taille de la lampe, une Distance de 0,0002 s'afficherait « 0.000 » dans le champ. Strength 0,2
    avec Distance 0,001 donne le même relief (le Bump mélange la normale d'origine et la normale
    perturbée : pour un petit relief, l'effet est proportionnel au produit des deux)."""
    b = nt.nodes.new("ShaderNodeBump")
    b.location = (x, y)
    b.inputs["Distance"].default_value = 0.001
    b.inputs["Strength"].default_value = round(distance / 0.001, 3)
    nt.links.new(height_socket, b.inputs["Height"])
    nt.links.new(b.outputs["Normal"], p.inputs["Normal"])
    return b


def image_node(nt, name, blend, x=-650, y=150):
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.location = (x, y)
    tex.image = image(name)
    tex.projection = 'BOX'
    tex.projection_blend = blend
    return tex


def principled(name, color, metallic, rough, opts, complete=True):
    """Une matière d'après sa recette. complete=False : le Principled réglé, et le nœud Image Texture
    déjà chargé mais non relié (« à compléter », fiche C)."""
    mat = bpy.data.materials.new(name)
    try:
        mat.use_nodes = True
    except Exception:
        pass
    nt, p, o = nodes_of(mat)
    if opts.get("carbone"):
        color = color or "1A1A1C"          # sans l'image, la base reste sombre, pas blanche
    if color:
        p.inputs["Base Color"].default_value = lin(color)
        mat.diffuse_color = lin(color)
    p.inputs["Metallic"].default_value = metallic
    p.inputs["Roughness"].default_value = rough
    mat.metallic = metallic
    mat.roughness = rough
    if "coat" in opts:
        w, r = opts["coat"]
        p.inputs["Coat Weight"].default_value = w
        p.inputs["Coat Roughness"].default_value = r
    if "glass" in opts:
        ior, thin = opts["glass"]
        p.inputs["Transmission Weight"].default_value = 1.0
        p.inputs["IOR"].default_value = ior
        p.inputs["Thin Wall"].default_value = thin
        mat.use_raytrace_refraction = True
    if not complete:
        # le nœud chargé garde la projection Flat par défaut : la démo montre d'abord ce qu'elle donne
        loaded = []
        if "image" in opts:
            loaded.append(image_node(nt, opts["image"][0], 0.0, x=-500, y=-150))
        if opts.get("carbone"):
            loaded.append(image_node(nt, "carbone_serge_couleur", 0.0, x=-500, y=250))
            loaded.append(image_node(nt, "carbone_serge_relief", 0.0, x=-500, y=-150))
        for tex in loaded:
            tex.projection = 'FLAT'
        return mat
    if "noise" in opts:
        scale, detail, dist, mapping = opts["noise"]
        vec = coords(nt, mapping=mapping)
        nz = nt.nodes.new("ShaderNodeTexNoise")
        nz.location = (-650, 150)
        nz.inputs["Scale"].default_value = scale
        nz.inputs["Detail"].default_value = detail
        nt.links.new(vec, nz.inputs["Vector"])
        bump(nt, p, nz.outputs[0], dist)
    if "voronoi" in opts:
        scale, dist = opts["voronoi"]
        vec = coords(nt)
        vo = nt.nodes.new("ShaderNodeTexVoronoi")
        vo.location = (-650, 150)
        vo.inputs["Scale"].default_value = scale
        nt.links.new(vec, vo.inputs["Vector"])
        bump(nt, p, vo.outputs["Distance"], dist)
    if "image" in opts:
        name_im, blend, mscale, dist = opts["image"]
        vec = coords(nt, mapping=(mscale, mscale, mscale))
        tex = image_node(nt, name_im, blend)
        nt.links.new(vec, tex.inputs["Vector"])
        bump(nt, p, tex.outputs["Color"], dist)
    if opts.get("carbone"):
        vec = coords(nt, mapping=(62.5, 62.5, 62.5))
        col = image_node(nt, "carbone_serge_couleur", 0.2, y=330)
        rel = image_node(nt, "carbone_serge_relief", 0.2, y=-60)
        nt.links.new(vec, col.inputs["Vector"])
        nt.links.new(vec, rel.inputs["Vector"])
        nt.links.new(col.outputs["Color"], p.inputs["Base Color"])
        bump(nt, p, rel.outputs["Color"], 0.0001)
        mat.diffuse_color = lin("1A1A1C")
    return mat


def biblio(name, complete=True, new_name=None):
    cat, color, metallic, rough, opts, _tags, _desc = BIBLIO[name]
    return principled(new_name or name, color, metallic, rough, opts, complete)


def lampe(name, new_name=None):
    color, metallic, rough, opts = LAMPE[name]
    return principled(new_name or name, color, metallic, rough, opts)


def mark(mat, catalogs, catalog, description, tags=()):
    mat.asset_mark()
    ad = mat.asset_data
    ad.author = AUTHOR
    ad.license = LICENSE
    ad.description = description
    for t in tags:
        ad.tags.new(t, skip_if_exists=True)
    ad.catalog_id = catalogs[catalog]


def write_catalogs(folder, catalogs):
    """Le fichier de catalogues, posé à côté du .blend (vérifié : Blender l'y cherche)."""
    lines = ["# This is an Asset Catalog Definition file for Blender.", "#",
             "# Empty lines and lines starting with `#` will be ignored.",
             "# The first non-ignored line should be the version indicator.",
             '# Other lines are of the format "UUID:catalog/path/for/assets:simple catalog name"', "",
             "VERSION 1", ""]
    for name, uid in catalogs.items():
        lines.append("%s:%s:%s" % (uid, name, name))
    path = os.path.join(folder, "blender_assets.cats.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    return path
