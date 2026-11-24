# Gabarits de matières de la planche CMF : un groupe de nœuds par finition, aux entrées nommées en
# français (Couleur, Brillance, Relief, tailles en millimètres), et une matière « Gabarit_… » qui
# l'utilise. Aucun dépliage UV : coordonnées Object, projection Box pour l'image du motif, comme au
# chapitre 3. Le relief passe par un Bump réglé par Strength (entrée Relief), Distance restant à 0,001 :
# la hauteur est multipliée par la taille du détail en mm, pour qu'un même Relief donne la même pente
# quelle que soit la taille choisie.

import math as pymath

import bpy

import commun as C
from commun import feed, map_range, math, mix_color, node

PI2 = 2 * pymath.pi


def group(name, inputs, outputs=(("BSDF", "NodeSocketShader"),)):
    """inputs : (nom, type, défaut, min, max, sous-type) ; type 'C' couleur, 'F' nombre, 'A' angle."""
    ng = bpy.data.node_groups.new(name, 'ShaderNodeTree')
    for nm, typ, default, mn, mx, *rest in inputs:
        st = {'C': 'NodeSocketColor', 'F': 'NodeSocketFloat', 'A': 'NodeSocketFloat'}[typ]
        s = ng.interface.new_socket(name=nm, in_out='INPUT', socket_type=st)
        if typ == 'C':
            s.default_value = C.lin(default)
        else:
            if typ == 'A':
                s.subtype = 'ANGLE'
            elif rest and rest[0]:
                s.subtype = rest[0]
            s.default_value = default
            s.min_value = mn
            s.max_value = mx
    for nm, st in outputs:
        ng.interface.new_socket(name=nm, in_out='OUTPUT', socket_type=st)
    gi = node(ng, "NodeGroupInput", -1400, 0)
    go = node(ng, "NodeGroupOutput", 700, 0)
    return ng, gi.outputs, go.inputs


def obj_xyz(nt, x=-1200, y=-400):
    tc = node(nt, "ShaderNodeTexCoord", x, y)
    sep = node(nt, "ShaderNodeSeparateXYZ", x + 200, y)
    nt.links.new(tc.outputs["Object"], sep.inputs[0])
    return tc.outputs["Object"], sep.outputs


def noise(nt, vec, scale, detail=4.0, rough=0.55, x=-600, y=-300):
    n = node(nt, "ShaderNodeTexNoise", x, y)
    feed(nt, n.inputs["Vector"], vec)
    feed(nt, n.inputs["Scale"], scale)
    n.inputs["Detail"].default_value = detail
    n.inputs["Roughness"].default_value = rough
    return n.outputs[0]


def bump(nt, height, strength, x=200, y=-300):
    b = node(nt, "ShaderNodeBump", x, y)
    b.inputs["Distance"].default_value = 0.001
    feed(nt, b.inputs["Strength"], strength)
    feed(nt, b.inputs["Height"], height)
    return b.outputs["Normal"]


def principled(nt, x=450, y=0, **inputs):
    p = node(nt, "ShaderNodeBsdfPrincipled", x, y)
    for k, v in inputs.items():
        feed(nt, p.inputs[k.replace("_", " ")], v)
    return p


def rough_from(nt, brillance, x=0, y=200):
    return math(nt, 'SUBTRACT', 1.0, brillance, x=x, y=y, clamp=True)


def scale_mm(nt, size_mm, x=-900, y=-200):
    """Échelle d'une texture pour un détail de size_mm millimètres : 1000 / mm."""
    return math(nt, 'DIVIDE', 1000.0, size_mm, x=x, y=y)


# ---------------------------------------------------------------------------- les groupes
def g_laque():
    ng, I, O = group("GAB_Laque", [
        ("Couleur", 'C', "1F3A5F", 0, 0), ("Brillance", 'F', 0.85, 0, 1, 'FACTOR'),
        ("Vernis", 'F', 1.0, 0, 1, 'FACTOR'), ("Métallisé", 'F', 0.0, 0, 1, 'FACTOR'),
        ("Relief", 'F', 0.03, 0, 1, 'FACTOR'), ("Taille de la peau d'orange (mm)", 'F', 4.0, 0.1, 100)])
    vec, _ = obj_xyz(ng)
    nz = noise(ng, vec, scale_mm(ng, I["Taille de la peau d'orange (mm)"]), detail=2.0)
    h = math(ng, 'MULTIPLY', nz, I["Taille de la peau d'orange (mm)"], x=-300, y=-300)
    nrm = bump(ng, h, I["Relief"])
    r = rough_from(ng, I["Brillance"])
    p = principled(ng, Base_Color=I["Couleur"], Metallic=I["Métallisé"], Roughness=r,
                   Coat_Weight=I["Vernis"], Coat_Roughness=math(ng, 'MULTIPLY', r, 0.4, x=0, y=60),
                   Normal=nrm, Coat_Normal=nrm)
    ng.links.new(p.outputs[0], O["BSDF"])
    return ng


def g_plastique():
    ng, I, O = group("GAB_Plastique_Graine", [
        ("Couleur", 'C', "3A3D40", 0, 0), ("Brillance", 'F', 0.5, 0, 1, 'FACTOR'),
        ("Relief", 'F', 0.15, 0, 1, 'FACTOR'), ("Taille du grain (mm)", 'F', 0.6, 0.05, 20),
        ("Mouchetures", 'F', 0.0, 0, 1, 'FACTOR'), ("Moucheture claire", 'C', "DADDE0", 0, 0),
        ("Moucheture foncée", 'C', "121318", 0, 0), ("Taille des mouchetures (mm)", 'F', 1.0, 0.1, 20)])
    vec, _ = obj_xyz(ng)
    nz = noise(ng, vec, scale_mm(ng, I["Taille du grain (mm)"]), detail=6.0, rough=0.6)
    h = math(ng, 'MULTIPLY', nz, I["Taille du grain (mm)"], x=-300, y=-300)
    nrm = bump(ng, h, I["Relief"])
    # mouchetures : une cellule de Voronoi sur 2,5 diamètres, gardée selon sa couleur aléatoire
    cell = math(ng, 'MULTIPLY', I["Taille des mouchetures (mm)"], 2.5, x=-1100, y=300)
    vo = node(ng, "ShaderNodeTexVoronoi", -800, 400)
    ng.links.new(vec, vo.inputs["Vector"])
    feed(ng, vo.inputs["Scale"], scale_mm(ng, cell, x=-950, y=300))
    sep = node(ng, "ShaderNodeSeparateColor", -600, 500)
    ng.links.new(vo.outputs["Color"], sep.inputs[0])
    dot = map_range(ng, vo.outputs["Distance"], 0.22, 0.17, x=-600, y=300)
    keep = math(ng, 'LESS_THAN', sep.outputs[0], I["Mouchetures"], x=-400, y=500)
    m = math(ng, 'MULTIPLY', dot, keep, x=-200, y=400)
    tone = math(ng, 'GREATER_THAN', sep.outputs[1], 0.45, x=-400, y=650)
    speck = mix_color(ng, tone, I["Moucheture foncée"], I["Moucheture claire"], x=-200, y=650)
    col = mix_color(ng, m, I["Couleur"], speck, x=100, y=400)
    p = principled(ng, Base_Color=col, Roughness=rough_from(ng, I["Brillance"]), Normal=nrm)
    ng.links.new(p.outputs[0], O["BSDF"])
    return ng


def g_metal_brosse():
    ng, I, O = group("GAB_Metal_Brosse", [
        ("Couleur", 'C', "C8C8C6", 0, 0), ("Brillance", 'F', 0.7, 0, 1, 'FACTOR'),
        ("Relief", 'F', 0.15, 0, 1, 'FACTOR'), ("Finesse du brossage (mm)", 'F', 1.0, 0.05, 20),
        ("Rotation du brossage", 'A', 0.0, -6.3, 6.3)])
    vec, _ = obj_xyz(ng)
    # rayures le long de l'axe Z de la pièce (l'axe d'un tube) ; 90° les couche le long de X
    rot = node(ng, "ShaderNodeVectorRotate", -1000, -150, rotation_type='Y_AXIS')
    ng.links.new(vec, rot.inputs["Vector"])
    feed(ng, rot.inputs["Angle"], I["Rotation du brossage"])
    st = node(ng, "ShaderNodeVectorMath", -800, -150, operation='MULTIPLY')
    ng.links.new(rot.outputs[0], st.inputs[0])
    st.inputs[1].default_value = (1.0, 1.0, 0.02)
    nz = noise(ng, st.outputs[0], scale_mm(ng, I["Finesse du brossage (mm)"]), detail=4.0)
    h = math(ng, 'MULTIPLY', nz, I["Finesse du brossage (mm)"], x=-300, y=-300)
    nrm = bump(ng, h, I["Relief"])
    r = rough_from(ng, I["Brillance"])
    r2 = math(ng, 'ADD', r, math(ng, 'MULTIPLY', math(ng, 'SUBTRACT', nz, 0.5, x=-300, y=150), 0.12, x=-100, y=150),
              x=100, y=200, clamp=True)
    p = principled(ng, Base_Color=I["Couleur"], Metallic=1.0, Roughness=r2, Normal=nrm)
    ng.links.new(p.outputs[0], O["BSDF"])
    return ng


def g_motif_coord():
    ng, I, O = group("GAB_Coordonnees_Motif", [
        ("Taille du motif (mm)", 'F', 120.0, 1, 2000), ("Rotation", 'A', 0.0, -6.3, 6.3)],
        outputs=(("Vecteur", "NodeSocketVector"),))
    vec, _ = obj_xyz(ng)
    rot = node(ng, "ShaderNodeVectorRotate", -900, -150, rotation_type='Z_AXIS')
    ng.links.new(vec, rot.inputs["Vector"])
    feed(ng, rot.inputs["Angle"], I["Rotation"])
    sc = node(ng, "ShaderNodeVectorMath", -600, -150, operation='SCALE')
    ng.links.new(rot.outputs[0], sc.inputs[0])
    feed(ng, sc.inputs["Scale"], scale_mm(ng, I["Taille du motif (mm)"], x=-800, y=-350))
    # la projection Box lit une face tournée vers Z en (Y, X) : on échange X et Y pour que l'image
    # paraisse à l'endroit, vue de dessus (bas de l'image vers -Y)
    sep = node(ng, "ShaderNodeSeparateXYZ", -400, -150)
    cmb = node(ng, "ShaderNodeCombineXYZ", -200, -150)
    ng.links.new(sc.outputs[0], sep.inputs[0])
    ng.links.new(sep.outputs[0], cmb.inputs[1])
    ng.links.new(sep.outputs[1], cmb.inputs[0])
    ng.links.new(sep.outputs[2], cmb.inputs[2])
    ng.links.new(cmb.outputs[0], O["Vecteur"])
    return ng


def g_tissu():
    ng, I, O = group("GAB_Tissu", [
        ("Motif", 'C', "2A2F55", 0, 0), ("Couleur", 'C', "FFFFFF", 0, 0),
        ("Brillance", 'F', 0.1, 0, 1, 'FACTOR'), ("Velours", 'F', 0.5, 0, 1, 'FACTOR'),
        ("Relief", 'F', 0.35, 0, 1, 'FACTOR'), ("Taille de la trame (mm)", 'F', 0.8, 0.1, 20)])
    _, xyz = obj_xyz(ng)
    k = math(ng, 'DIVIDE', PI2 * 1000.0, I["Taille de la trame (mm)"], x=-1000, y=-500)
    sx = math(ng, 'SINE', math(ng, 'MULTIPLY', xyz[0], k, x=-800, y=-300), x=-600, y=-300)
    sy = math(ng, 'SINE', math(ng, 'MULTIPLY', xyz[1], k, x=-800, y=-500), x=-600, y=-500)
    w = math(ng, 'MULTIPLY', sx, sy, x=-400, y=-400)
    h = math(ng, 'MULTIPLY', w, math(ng, 'MULTIPLY', I["Taille de la trame (mm)"], 0.3, x=-400, y=-600),
             x=-200, y=-400)
    nrm = bump(ng, h, I["Relief"])
    tint = node(ng, "ShaderNodeMix", 0, 300, data_type='RGBA', blend_type='MULTIPLY', clamp_factor=True)
    tint.inputs[0].default_value = 1.0
    feed(ng, tint.inputs[6], I["Motif"])
    feed(ng, tint.inputs[7], I["Couleur"])
    p = principled(ng, Base_Color=tint.outputs[2], Roughness=rough_from(ng, I["Brillance"]),
                   Sheen_Weight=I["Velours"], Sheen_Roughness=0.35, Normal=nrm)
    ng.links.new(p.outputs[0], O["BSDF"])
    return ng


def g_perfore():
    ng, I, O = group("GAB_Perfore", [
        ("Couleur", 'C', "8A979E", 0, 0), ("Brillance", 'F', 0.45, 0, 1, 'FACTOR'),
        ("Relief", 'F', 0.3, 0, 1, 'FACTOR'), ("Pas des trous (mm)", 'F', 3.0, 0.2, 100),
        ("Diamètre des trous (mm)", 'F', 1.2, 0.05, 100), ("Quinconce", 'F', 1.0, 0, 1, 'FACTOR')])
    _, xyz = obj_xyz(ng)
    inv = math(ng, 'DIVIDE', 1000.0, I["Pas des trous (mm)"], x=-1000, y=-600)
    u = math(ng, 'MULTIPLY', xyz[0], inv, x=-800, y=-300)
    v = math(ng, 'MULTIPLY', xyz[1], inv, x=-800, y=-500)
    row = math(ng, 'FLOORED_MODULO', math(ng, 'FLOOR', v, x=-650, y=-650), 2.0, x=-500, y=-650)
    shift = math(ng, 'MULTIPLY', math(ng, 'MULTIPLY', row, 0.5, x=-350, y=-650), I["Quinconce"], x=-200, y=-650)
    u2 = math(ng, 'ADD', u, shift, x=-500, y=-300)
    fu = math(ng, 'SUBTRACT', math(ng, 'FRACT', u2, x=-350, y=-300), 0.5, x=-200, y=-300)
    fv = math(ng, 'SUBTRACT', math(ng, 'FRACT', v, x=-350, y=-500), 0.5, x=-200, y=-500)
    cmb = node(ng, "ShaderNodeCombineXYZ", -50, -400)
    ng.links.new(fu, cmb.inputs[0])
    ng.links.new(fv, cmb.inputs[1])
    ln = node(ng, "ShaderNodeVectorMath", 100, -400, operation='LENGTH')
    ng.links.new(cmb.outputs[0], ln.inputs[0])
    d = math(ng, 'MULTIPLY', ln.outputs["Value"], I["Pas des trous (mm)"], x=250, y=-400)
    r = math(ng, 'MULTIPLY', I["Diamètre des trous (mm)"], 0.5, x=100, y=-650)
    a = map_range(ng, d, math(ng, 'SUBTRACT', r, 0.03, x=250, y=-600), math(ng, 'ADD', r, 0.03, x=250, y=-750),
                  x=400, y=-500)
    h = math(ng, 'MULTIPLY', map_range(ng, d, r, math(ng, 'ADD', r, 0.25, x=250, y=-900), x=400, y=-800),
             0.25, x=550, y=-800)
    nrm = bump(ng, h, I["Relief"], x=550, y=-500)
    p = principled(ng, x=750, Base_Color=I["Couleur"], Roughness=rough_from(ng, I["Brillance"]), Alpha=a,
                   Normal=nrm)
    ng.links.new(p.outputs[0], O["BSDF"])
    return ng


def g_translucide():
    ng, I, O = group("GAB_Translucide_Cote", [
        ("Couleur", 'C', "EEECE8", 0, 0), ("Translucidité", 'F', 0.85, 0, 1, 'FACTOR'),
        ("Brillance", 'F', 0.65, 0, 1, 'FACTOR'), ("Relief", 'F', 0.35, 0, 1, 'FACTOR'),
        ("Pas des côtes (mm)", 'F', 5.0, 0.2, 200), ("Ondulation (mm)", 'F', 1.5, 0, 100),
        ("Longueur de l'onde (mm)", 'F', 90.0, 1, 2000)])
    _, xyz = obj_xyz(ng)
    xm = math(ng, 'MULTIPLY', xyz[0], 1000.0, x=-900, y=-300)
    ym = math(ng, 'MULTIPLY', xyz[1], 1000.0, x=-900, y=-500)
    wave = math(ng, 'SINE', math(ng, 'MULTIPLY', ym, math(ng, 'DIVIDE', PI2, I["Longueur de l'onde (mm)"],
                                                           x=-900, y=-700), x=-750, y=-500), x=-600, y=-500)
    xs = math(ng, 'ADD', xm, math(ng, 'MULTIPLY', wave, I["Ondulation (mm)"], x=-450, y=-500), x=-300, y=-300)
    rib = math(ng, 'ABSOLUTE', math(ng, 'SINE', math(ng, 'MULTIPLY', xs, math(
        ng, 'DIVIDE', pymath.pi, I["Pas des côtes (mm)"], x=-300, y=-700), x=-150, y=-300), x=0, y=-300), x=150, y=-300)
    h = math(ng, 'MULTIPLY', rib, math(ng, 'MULTIPLY', I["Pas des côtes (mm)"], 0.25, x=150, y=-500), x=300, y=-300)
    nrm = bump(ng, h, I["Relief"], x=450, y=-300)
    p = principled(ng, x=650, Base_Color=I["Couleur"], Roughness=rough_from(ng, I["Brillance"]),
                   Transmission_Weight=I["Translucidité"], Normal=nrm)
    p.inputs["Thin Wall"].default_value = True
    ng.links.new(p.outputs[0], O["BSDF"])
    return ng


def g_anodise():
    ng, I, O = group("GAB_Anodise_Degrade", [
        ("Couleur haut", 'C', "D8E0E6", 0, 0), ("Couleur bas", 'C', "6B7277", 0, 0),
        ("Début du dégradé (mm)", 'F', -60.0, -5000, 5000), ("Fin du dégradé (mm)", 'F', 50.0, -5000, 5000),
        ("Brillance", 'F', 0.6, 0, 1, 'FACTOR'), ("Relief", 'F', 0.05, 0, 1, 'FACTOR'),
        ("Taille du grain (mm)", 'F', 0.3, 0.05, 20)])
    vec, xyz = obj_xyz(ng)
    t = map_range(ng, math(ng, 'MULTIPLY', xyz[1], 1000.0, x=-900, y=300), I["Début du dégradé (mm)"],
                  I["Fin du dégradé (mm)"], x=-600, y=300)
    col = mix_color(ng, t, I["Couleur bas"], I["Couleur haut"], x=-300, y=300)
    nz = noise(ng, vec, scale_mm(ng, I["Taille du grain (mm)"]), detail=4.0)
    h = math(ng, 'MULTIPLY', nz, I["Taille du grain (mm)"], x=-300, y=-300)
    nrm = bump(ng, h, I["Relief"])
    p = principled(ng, Base_Color=col, Metallic=1.0, Roughness=rough_from(ng, I["Brillance"]), Normal=nrm)
    ng.links.new(p.outputs[0], O["BSDF"])
    return ng


# ---------------------------------------------------------------------------- les matières
def _material(name, ng, display):
    m = bpy.data.materials.new(name)
    try:
        m.use_nodes = True
    except Exception:
        pass
    nt = m.node_tree
    for n in list(nt.nodes):
        if n.type == 'BSDF_PRINCIPLED':
            nt.nodes.remove(n)
    out = next(n for n in nt.nodes if n.type == 'OUTPUT_MATERIAL')
    out.location = (300, 0)
    g = node(nt, "ShaderNodeGroup", 0, 0)
    g.node_tree = ng
    g.width = 260
    nt.links.new(g.outputs[0], out.inputs["Surface"])
    m.diffuse_color = C.lin(display)
    return m, g


GABARITS = [  # matière, groupe, couleur d'affichage, description
    ("Gabarit_Laque", g_laque, "1F3A5F",
     "Laque ou peinture : Couleur, Brillance, Vernis, Métallisé, peau d'orange (Relief et taille en mm)."),
    ("Gabarit_Plastique_Graine", g_plastique, "3A3D40",
     "Plastique grainé, avec mouchetures en option : Couleur, Brillance, Relief, taille du grain en mm."),
    ("Gabarit_Metal_Brosse", g_metal_brosse, "C8C8C6",
     "Métal brossé, rayé le long de l'axe Z de la pièce (axe d'un tube) ; Rotation du brossage 90° pour une plaque."),
    ("Gabarit_Tissu_Motif", g_tissu, "2A2F55",
     "Tissu à motif : l'image du motif (Open), sa taille en mm et sa rotation, Velours, Relief de la trame."),
    ("Gabarit_Perfore", g_perfore, "8A979E",
     "Tôle ou panneau perforé : pas et diamètre des trous en mm, en quinconce ou en ligne ; les trous sont transparents."),
    ("Gabarit_Translucide_Cote", g_translucide, "EEECE8",
     "Panneau translucide côtelé : Translucidité, pas des côtes et ondulation en mm."),
    ("Gabarit_Anodise_Degrade", g_anodise, "A0A8AE",
     "Aluminium anodisé en dégradé vertical : deux couleurs, début et fin du dégradé en mm le long de l'axe Y."),
]


def build_all(motif_image):
    """Crée les groupes et les matières gabarits. Renvoie {nom : (matière, nœud groupe, description)}."""
    out = {}
    coord = g_motif_coord()
    for name, fn, display, desc in GABARITS:
        ng = fn()
        m, g = _material(name, ng, display)
        if name == "Gabarit_Tissu_Motif":
            nt = m.node_tree
            tex = node(nt, "ShaderNodeTexImage", -350, 100, projection='BOX', projection_blend=0.15,
                       interpolation='Cubic')
            tex.image = motif_image
            cg = node(nt, "ShaderNodeGroup", -650, 100)
            cg.node_tree = coord
            cg.width = 220
            nt.links.new(cg.outputs[0], tex.inputs["Vector"])
            nt.links.new(tex.outputs["Color"], g.inputs["Motif"])
            g.location = (0, 0)
        if name == "Gabarit_Perfore":
            m.surface_render_method = 'DITHERED'
            m.use_transparent_shadow = True
        if name == "Gabarit_Translucide_Cote":
            m.use_raytrace_refraction = True
        out[name] = (m, g, desc)
    return out


def variant(src, name, values, coord_values=None):
    """Une copie réglée d'un gabarit : values = {entrée : valeur} (couleurs en hexadécimal)."""
    m = src.copy()
    m.name = name
    nt = m.node_tree
    g = next(n for n in nt.nodes if n.type == 'GROUP' and n.node_tree.name.startswith("GAB_")
             and n.node_tree.name != "GAB_Coordonnees_Motif")
    for k, v in values.items():
        s = g.inputs[k]
        s.default_value = C.lin(v) if isinstance(v, str) else v
        if isinstance(v, str) and k in ("Couleur", "Couleur haut", "Motif"):
            m.diffuse_color = C.lin(v)
    if coord_values:
        cg = next(n for n in nt.nodes if n.type == 'GROUP' and n.node_tree.name == "GAB_Coordonnees_Motif")
        for k, v in coord_values.items():
            cg.inputs[k].default_value = v
    return m
