# Recettes du défi facultatif « matières procédurales » du chapitre 3
# (plan : _resources/plans/PRC02-plan-chap3-complement-procedural.md). Importé par build_defi.py et
# captures_defi.py : sys.path.insert(0, HERE).
#
# Toutes les chaînes partent de Texture Coordinate : aucune pièce n'a de dépliage UV. Le relief se règle
# avec Strength, Distance gardant sa valeur par défaut (0,001), comme au chapitre 3 (décision de
# production du 19 novembre 2026) : Strength = Distance du plan x 1000, retouché à l'œil.
# Les couleurs sont en hexadécimal sRGB, comme dans le sélecteur de couleur de Blender.

import math

import bpy

from matieres import lin

DX = 210      # pas horizontal entre deux colonnes de nœuds (unités de l'éditeur)
DY = 190      # pas vertical


# ---------------------------------------------------------------------------- outils
class Chaine:
    """Une matière en cours de câblage : le Principled, le Material Output et des nœuds rangés en
    colonnes, de droite (col 0, juste avant le Principled) à gauche."""

    def __init__(self, name, color=None, metallic=0.0, rough=0.5, coat=None):
        self.m = bpy.data.materials.new(name)
        try:
            self.m.use_nodes = True
        except Exception:
            pass
        self.nt = self.m.node_tree
        self.p = next(n for n in self.nt.nodes if n.type == 'BSDF_PRINCIPLED')
        self.o = next(n for n in self.nt.nodes if n.type == 'OUTPUT_MATERIAL')
        self.p.location = (0, 300)
        self.o.location = (300, 300)
        if color:
            self.p.inputs["Base Color"].default_value = lin(color)
            self.m.diffuse_color = lin(color)
        self.p.inputs["Metallic"].default_value = metallic
        self.p.inputs["Roughness"].default_value = rough
        self.m.metallic = metallic
        self.m.roughness = rough
        if coat:
            self.p.inputs["Coat Weight"].default_value = coat[0]
            self.p.inputs["Coat Roughness"].default_value = coat[1]
        self._tc = None

    def node(self, kind, col, row, **kw):
        n = self.nt.nodes.new(kind)
        n.location = (-DX * (col + 1) - 40, 300 - DY * row)
        for k, v in kw.items():
            if k.startswith("i_"):
                n.inputs[k[2:].replace("_", " ")].default_value = v
            else:
                setattr(n, k, v)
        return n

    def link(self, a, b):
        self.nt.links.new(a, b)

    def tc(self, col, row=0):
        if self._tc is None:
            self._tc = self.node("ShaderNodeTexCoord", col, row)
        return self._tc

    def ramp(self, src, stops, col, row=0, interp='LINEAR'):
        r = self.node("ShaderNodeValToRGB", col, row)
        cr = r.color_ramp
        cr.interpolation = interp
        cr.elements[0].position = stops[0][0]
        cr.elements[0].color = stops[0][1]
        cr.elements[1].position = stops[-1][0]
        cr.elements[1].color = stops[-1][1]
        for pos, colr in stops[1:-1]:
            e = cr.elements.new(pos)
            e.color = colr
        if src is not None:
            self.link(src, r.inputs["Factor"])
        return r

    def bump(self, height, strength, col, row=1, normal_in=None, target="Normal"):
        b = self.node("ShaderNodeBump", col, row)
        b.inputs["Distance"].default_value = 0.001
        b.inputs["Strength"].default_value = strength
        self.link(height, b.inputs["Height"])
        if normal_in is not None:
            self.link(normal_in, b.inputs["Normal"])
        if target:
            self.link(b.outputs["Normal"], self.p.inputs[target])
        return b

    def view(self, sock):
        """L'aperçu : la sortie reliée directement à Surface (Ctrl + Maj + clic)."""
        self.link(sock, self.o.inputs["Surface"])

    def math(self, op, col, row, a=None, b=None, v1=None):
        n = self.node("ShaderNodeMath", col, row, operation=op)
        if v1 is not None:
            n.inputs[1].default_value = v1
        if a is not None:
            self.link(a, n.inputs[0])
        if b is not None:
            self.link(b, n.inputs[1])
        return n

    def maprange(self, src, col, row, fmin=0.0, fmax=1.0, tmin=0.0, tmax=1.0):
        n = self.node("ShaderNodeMapRange", col, row)
        n.inputs["From Min"].default_value = fmin
        n.inputs["From Max"].default_value = fmax
        n.inputs["To Min"].default_value = tmin
        n.inputs["To Max"].default_value = tmax
        if src is not None:
            self.link(src, n.inputs["Value"])
        return n

    def mix_color(self, fac, a, b, col, row, target="Base Color"):
        n = self.node("ShaderNodeMix", col, row, data_type='RGBA')
        n.inputs["A"].default_value = lin(a)
        n.inputs["B"].default_value = lin(b)
        n.inputs["Factor"].default_value = 0.5
        if fac is not None:
            self.link(fac, n.inputs["Factor"])
        if target:
            self.link(n.outputs["Result"], self.p.inputs[target])
        return n

    def mix_float(self, fac, a, b, col, row, target=None):
        n = self.node("ShaderNodeMix", col, row, data_type='FLOAT')
        n.inputs["A"].default_value = a
        n.inputs["B"].default_value = b
        if fac is not None:
            self.link(fac, n.inputs["Factor"])
        if target:
            self.link(n.outputs["Result"], self.p.inputs[target])
        return n


W = (1.0, 1.0, 1.0, 1.0)
K = (0.0, 0.0, 0.0, 1.0)

# hauteurs estimées des nœuds (unités de l'éditeur), pour les ranger sans chevauchement en arrière-plan,
# où Blender ne calcule pas encore leurs dimensions
HAUTEUR = {
    "ShaderNodeTexCoord": 250, "ShaderNodeTexNoise": 300, "ShaderNodeTexVoronoi": 300, "ShaderNodeTexWave": 330,
    "ShaderNodeTexGabor": 240, "ShaderNodeTexChecker": 200, "ShaderNodeTexGradient": 130, "ShaderNodeValToRGB": 250,
    "ShaderNodeMapRange": 260, "ShaderNodeMath": 170, "ShaderNodeMix": 220, "ShaderNodeSeparateXYZ": 140,
    "ShaderNodeVectorMath": 170, "ShaderNodeBump": 210, "ShaderNodeAmbientOcclusion": 190, "ShaderNodeMapping": 340,
    "ShaderNodeGroup": 230, "NodeGroupInput": 200,
}
ANCRES = ('BSDF_PRINCIPLED', 'OUTPUT_MATERIAL', 'GROUP_OUTPUT')


def tidy(nt, gap_x=40, gap_y=40, top=300):
    """Range les nœuds en colonnes serrées, de droite à gauche, sans chevauchement : chaque colonne
    (même abscisse) prend la largeur de son plus large nœud ; dans une colonne, les nœuds gardent leur
    ordre vertical. Le Principled, le Material Output et le Group Output ne bougent pas."""
    anchors = [n for n in nt.nodes if n.type in ANCRES]
    right = min((n.location.x for n in anchors), default=0)
    if any(n.type == 'BSDF_PRINCIPLED' for n in anchors):
        right = next(n for n in anchors if n.type == 'BSDF_PRINCIPLED').location.x
    cols = {}
    for n in nt.nodes:
        if n.type in ANCRES or n.type == 'FRAME':
            continue
        cols.setdefault(round(n.location.x / 10), []).append(n)
    x_right = right - gap_x
    for key in sorted(cols, reverse=True):
        nodes = sorted(cols[key], key=lambda n: -n.location.y)
        w = max(n.width for n in nodes)
        x = x_right - w
        y = top
        for n in nodes:
            n.location = (x, y)
            y -= HAUTEUR.get(n.bl_idname, 200) + gap_y
        x_right = x - gap_x


def depart(name, color=None, metallic=0.0, rough=0.5, coat=None):
    """Une matière à compléter : le Principled réglé, rien d'autre."""
    return Chaine(name, color, metallic, rough, coat).m


# ---------------------------------------------------------------------------- étape 1 : les bruits
def bruit(name, kind, out, **kw):
    """Une texture en aperçu : TC (Object) -> texture -> Surface. kind : NOISE, VORONOI, WAVE, GABOR."""
    c = Chaine(name)
    t = {"NOISE": "ShaderNodeTexNoise", "VORONOI": "ShaderNodeTexVoronoi", "WAVE": "ShaderNodeTexWave",
         "GABOR": "ShaderNodeTexGabor"}[kind]
    tex = c.node(t, 0, 0, **kw)
    c.link(c.tc(1).outputs["Object"], tex.inputs["Vector"])
    c.view(tex.outputs[out])
    return c


E1 = {   # nom : (texture, sortie, réglages)
    "Noise": ("NOISE", "Factor", {"i_Scale": 100}),
    "Noise_detail": ("NOISE", "Factor", {"i_Scale": 100, "i_Detail": 8, "i_Roughness": 0.7}),
    "Noise_distortion": ("NOISE", "Factor", {"i_Scale": 100, "i_Distortion": 2.0}),
    "Noise_ridged": ("NOISE", "Factor", {"i_Scale": 60, "i_Detail": 4, "noise_type": 'RIDGED_MULTIFRACTAL'}),
    "Noise_defaut": ("NOISE", "Factor", {}),
    "Voronoi": ("VORONOI", "Distance", {"i_Scale": 100}),
    "Voronoi_bords": ("VORONOI", "Distance", {"i_Scale": 100, "feature": 'DISTANCE_TO_EDGE'}),
    "Voronoi_couleur": ("VORONOI", "Color", {"i_Scale": 100}),
    "Wave": ("WAVE", "Factor", {"i_Scale": 40}),
    "Wave_ondule": ("WAVE", "Factor", {"i_Scale": 40, "i_Distortion": 4, "i_Detail": 4}),
    "Wave_anneaux": ("WAVE", "Factor", {"i_Scale": 40, "wave_type": 'RINGS', "rings_direction": 'Z'}),
    "Gabor": ("GABOR", "Value", {"i_Scale": 100}),
    "Gabor_serre": ("GABOR", "Value", {"i_Scale": 100, "i_Frequency": 6}),
    "Gabor_isotrope": ("GABOR", "Value", {"i_Scale": 100, "i_Anisotropy": 0.0}),
    "Gabor_axe_x": ("GABOR", "Value", {"i_Scale": 100, "i_Frequency": 6, "i_Orientation": 1.5708}),
}


def e1(name, key):
    kind, out, kw = E1[key]
    return bruit(name, kind, out, **kw).m


# ---------------------------------------------------------------------------- étape 2 : remapper
def mouchete(name, deux_couleurs=False, avec_math=False):
    c = Chaine(name, "2B2D2F", 0, 0.5)
    nz = c.node("ShaderNodeTexNoise", 1, 0, i_Scale=1500, i_Detail=0)
    c.link(c.tc(2).outputs["Object"], nz.inputs["Vector"])
    stops = [(0.0, lin("2B2D2F")), (0.74, lin("D8D6D0"))]
    if deux_couleurs:
        stops.append((0.82, lin("9B6B43")))
    r = c.ramp(nz.outputs["Factor"], stops, 0, 0, interp='CONSTANT')
    c.link(r.outputs["Color"], c.p.inputs["Base Color"])
    if avec_math:
        mth = c.math('GREATER_THAN', 0, 2, a=nz.outputs["Factor"], v1=0.74)
    return c.m


def planche(name):
    c = Chaine(name, "151515", 0, 0.2)
    nz = c.node("ShaderNodeTexNoise", 1, 1, i_Scale=40, i_Detail=3)
    c.link(c.tc(2, 1).outputs["Object"], nz.inputs["Vector"])
    mr = c.maprange(nz.outputs["Factor"], 0, 1, 0.35, 0.65, 0.08, 0.35)
    c.link(mr.outputs["Result"], c.p.inputs["Roughness"])
    return c.m


# ---------------------------------------------------------------------------- étape 3 : masques
def patine(name, metal="E0C27A", depot="3A3B2C", r_metal=0.25, r_depot=0.7, met_depot=0.0,
           extremites=True, relief=None):
    """Un masque, trois Mix. extremites : la patine seulement aux bouts (axe local Z du tube)."""
    c = Chaine(name, metal, 1, r_metal)
    nz = c.node("ShaderNodeTexNoise", 4, 0, i_Scale=40, i_Detail=6, i_Roughness=0.6)
    c.link(c.tc(5).outputs["Object"], nz.inputs["Vector"])
    r = c.ramp(nz.outputs["Factor"], [(0.50, K), (0.60, W)], 3, 0)
    mask = r.outputs["Color"]
    if extremites:
        sep = c.node("ShaderNodeSeparateXYZ", 4, 2)
        c.link(c.tc(5).outputs["Object"], sep.inputs["Vector"])
        ab = c.math('ABSOLUTE', 3, 2, a=sep.outputs["Z"])
        mr = c.maprange(ab.outputs["Value"], 2, 2, 0.08, 0.14)
        mul = c.math('MULTIPLY', 2, 0, a=mask, b=mr.outputs["Result"])
        mask = mul.outputs["Value"]
    c.mix_color(mask, metal, depot, 1, 0)
    c.mix_float(mask, 1.0, met_depot, 1, 1, target="Metallic")
    c.mix_float(mask, r_metal, r_depot, 1, 2, target="Roughness")
    if relief:
        c.bump(mask, relief, 0, 3)
    return c.m


# ---------------------------------------------------------------------------- étape 4 : relief
def boitier(name):
    c = Chaine(name, "D9DADB", 1, 0.45)
    n1 = c.node("ShaderNodeTexNoise", 2, 0, i_Scale=2000, i_Detail=0)
    c.link(c.tc(3).outputs["Object"], n1.inputs["Vector"])
    b1 = c.bump(n1.outputs["Factor"], 0.1, 1, 0, target=None)
    n2 = c.node("ShaderNodeTexNoise", 2, 2, i_Scale=150, i_Detail=4)
    c.link(c.tc(3).outputs["Object"], n2.inputs["Vector"])
    c.bump(n2.outputs["Factor"], 0.2, 0, 1, normal_in=b1.outputs["Normal"])
    return c.m


def peau_orange(c, col=1, row=2, strength=0.15):
    nz = c.node("ShaderNodeTexNoise", col + 1, row, i_Scale=600, i_Detail=1)
    c.link(c.tc(col + 2).outputs["Object"], nz.inputs["Vector"])
    return c.bump(nz.outputs["Factor"], strength, col, row, target="Coat Normal")


def laque_orange(name):
    c = Chaine(name, "A3161A", 0, 0.4, coat=(1, 0.03))
    peau_orange(c, 0, 1)
    return c.m


def metallisee(name):
    c = Chaine(name, "1C3F7A", 1, 0.35, coat=(1, 0.02))
    peau_orange(c, 0, 2)
    vo = c.node("ShaderNodeTexVoronoi", 1, 0, i_Scale=3000)
    c.link(c.tc(2).outputs["Object"], vo.inputs["Vector"])
    c.bump(vo.outputs["Distance"], 0.1, 0, 0)
    return c.m


# ---------------------------------------------------------------------------- étape 5 : usure
def masque_bords(c, variant="Z", col=6, row=0):
    """Le masque des arêtes, tiré de la normale de la pièce : Z (pièce de révolution d'axe Z) ou MAX
    (pièce prismatique). Renvoie la sortie du masque, cassé par un bruit."""
    tc = c.tc(col + 1, row)
    if variant == "Z":
        sep = c.node("ShaderNodeSeparateXYZ", col, row)
        c.link(tc.outputs["Normal"], sep.inputs["Vector"])
        ab = c.math('ABSOLUTE', col - 1, row, a=sep.outputs["Z"])
        r = c.ramp(ab.outputs["Value"], [(0.10, K), (0.50, W), (0.90, K)], col - 2, row)
    else:
        va = c.node("ShaderNodeVectorMath", col, row, operation='ABSOLUTE')
        c.link(tc.outputs["Normal"], va.inputs[0])
        sep = c.node("ShaderNodeSeparateXYZ", col - 1, row)
        c.link(va.outputs["Vector"], sep.inputs["Vector"])
        m1 = c.math('MAXIMUM', col - 2, row, a=sep.outputs["X"], b=sep.outputs["Y"])
        m2 = c.math('MAXIMUM', col - 2, row + 1, a=m1.outputs["Value"], b=sep.outputs["Z"])
        r = c.ramp(m2.outputs["Value"], [(0.80, W), (0.97, K)], col - 3, row)
    nz = c.node("ShaderNodeTexNoise", col - 2, row + 2, i_Scale=400, i_Detail=8, i_Roughness=0.7)
    c.link(tc.outputs["Object"], nz.inputs["Vector"])
    mul = c.math('MULTIPLY', col - 3 if variant == "Z" else col - 4, row + 1, a=r.outputs["Color"],
                 b=nz.outputs["Factor"])
    mr = c.maprange(mul.outputs["Value"], col - 4 if variant == "Z" else col - 5, row + 1, 0.30, 0.40)
    return mr.outputs["Result"]


def peinture_usee(name, variant="Z", peinture="2F5D3A", metal="B8B9BA"):
    c = Chaine(name, peinture, 0, 0.45)
    mask = masque_bords(c, variant, col=6 if variant == "Z" else 7)
    c.mix_color(mask, peinture, metal, 1, 0)
    c.link(mask, c.p.inputs["Metallic"])
    mr = c.maprange(mask, 1, 2, 0.0, 1.0, 0.45, 0.30)
    c.link(mr.outputs["Result"], c.p.inputs["Roughness"])
    return c.m


def masque_creux(c, col=4, row=0, distance=0.020):
    ao = c.node("ShaderNodeAmbientOcclusion", col, row)
    ao.inputs["Distance"].default_value = distance
    r = c.ramp(ao.outputs["AO"], [(0.85, W), (0.99, K)], col - 1, row)
    nz = c.node("ShaderNodeTexNoise", col, row + 2, i_Scale=200, i_Detail=6)
    c.link(c.tc(col + 1, row + 2).outputs["Object"], nz.inputs["Vector"])
    r2 = c.ramp(nz.outputs["Factor"], [(0.35, K), (0.65, W)], col - 1, row + 2)
    mul = c.math('MULTIPLY', col - 2, row + 1, a=r.outputs["Color"], b=r2.outputs["Color"])
    return mul.outputs["Value"]


def salete(name, base="9A9C9E", metallic=1.0, rough=0.35, distance=0.020):
    c = Chaine(name, base, metallic, rough)
    mask = masque_creux(c, distance=distance)
    c.mix_color(mask, base, "3B342C", 1, 0)
    c.mix_float(mask, metallic, 0.0, 1, 1, target="Metallic")
    mr = c.maprange(mask, 1, 2, 0.0, 1.0, rough, 0.9)
    c.link(mr.outputs["Result"], c.p.inputs["Roughness"])
    return c.m


def masque_rayures(c, col=3, row=0):
    mp = c.node("ShaderNodeMapping", col, row)
    mp.inputs["Scale"].default_value = (1, 1, 0.02)
    c.link(c.tc(col + 1, row).outputs["Object"], mp.inputs["Vector"])
    nz = c.node("ShaderNodeTexNoise", col - 1, row, i_Scale=2000, i_Detail=2)
    c.link(mp.outputs["Vector"], nz.inputs["Vector"])
    r = c.ramp(nz.outputs["Factor"], [(0.68, K), (0.70, W)], col - 2, row)
    return r.outputs["Color"]


def rayures(name):
    c = Chaine(name, "C8C8C6", 1, 0.08)
    mask = masque_rayures(c, 3, 1)
    mr = c.maprange(mask, 0, 1, 0.0, 1.0, 0.05, 0.5)
    c.link(mr.outputs["Result"], c.p.inputs["Roughness"])
    return c.m


def masque_traces(c, col=1, row=2):
    nz = c.node("ShaderNodeTexNoise", col, row, i_Scale=25, i_Detail=6, i_Roughness=0.7, i_Distortion=0.3)
    c.link(c.tc(col + 1, row).outputs["Object"], nz.inputs["Vector"])
    mr = c.maprange(nz.outputs["Factor"], col - 1, row, 0.55, 0.75, 0.02, 0.4)
    c.link(mr.outputs["Result"], c.p.inputs["Coat Roughness"])
    return mr


def traces(name):
    c = Chaine(name, "0A0A0A", 0, 0.3, coat=(1, 0.02))
    masque_traces(c)
    return c.m


def coffret(name):
    """Le coffret de quai : arêtes usées (variante prismatique), puis saleté au pied : deux couches."""
    c = Chaine(name, "2F5D3A", 0, 0.45)
    usure = masque_bords(c, "MAX", col=8, row=0)
    creux = masque_creux(c, col=5, row=4)
    m1 = c.mix_color(usure, "2F5D3A", "B8B9BA", 2, 0, target=None)
    m2 = c.mix_color(creux, "2F5D3A", "3B342C", 1, 0)
    c.link(m1.outputs["Result"], m2.inputs["A"])
    c.link(usure, c.p.inputs["Metallic"])
    mr = c.maprange(creux, 1, 2, 0.0, 1.0, 0.45, 0.9)
    c.link(mr.outputs["Result"], c.p.inputs["Roughness"])
    return c.m


# ---------------------------------------------------------------------------- étape 6 : motifs
def grille_reguliere(c, scale, col, row=0):
    v = c.node("ShaderNodeTexVoronoi", col, row, voronoi_dimensions='2D', i_Scale=scale, i_Randomness=0.0)
    c.link(c.tc(col + 1, row).outputs["Object"], v.inputs["Vector"])
    return v


def dalle(name):
    c = Chaine(name, "9A9C9E", 1, 0.35)
    v = grille_reguliere(c, 125, 2)
    r = c.ramp(v.outputs["Distance"], [(0.28, W), (0.32, K)], 1, 0)
    c.bump(r.outputs["Color"], 0.5, 0, 1)
    return c.m


def tole(name):
    c = Chaine(name, "B8B9BA", 1, 0.35)
    v = grille_reguliere(c, 250, 1)
    gt = c.math('GREATER_THAN', 0, 1, a=v.outputs["Distance"], v1=0.3)
    c.link(gt.outputs["Value"], c.p.inputs["Alpha"])
    return c.m


def cuir(name):
    c = Chaine(name, "1E1B19", 0, 0.55)
    v = c.node("ShaderNodeTexVoronoi", 2, 0, i_Scale=500, feature='DISTANCE_TO_EDGE')
    c.link(c.tc(3).outputs["Object"], v.inputs["Vector"])
    r = c.ramp(v.outputs["Distance"], [(0.0, K), (0.08, W)], 1, 0)
    c.bump(r.outputs["Color"], 0.2, 0, 1)
    return c.m


def tissu(name, S=500):
    c = Chaine(name, None, 0, 0.8)
    c.p.inputs["Sheen Weight"].default_value = 0.5
    tcn = c.tc(4, 1)
    ck = c.node("ShaderNodeTexChecker", 2, 0, i_Scale=S)          # le damier à part : une bande moins haute
    wa = c.node("ShaderNodeTexWave", 3, 0, i_Scale=round(0.314159 * S, 1), bands_direction='X')
    wb = c.node("ShaderNodeTexWave", 3, 2, i_Scale=round(0.314159 * S, 1), bands_direction='Y')
    for t in (ck, wa, wb):
        c.link(tcn.outputs["Object"], t.inputs["Vector"])
    mx = c.mix_float(ck.outputs["Factor"], 0, 0, 1, 1)
    c.link(wa.outputs["Factor"], mx.inputs["A"])
    c.link(wb.outputs["Factor"], mx.inputs["B"])
    c.bump(mx.outputs["Result"], 0.4, 0, 2)
    c.mix_color(mx.outputs["Result"], "141C30", "2E3D63", 0, 0)
    c.m.diffuse_color = lin("1F2A48")
    return c.m


def moletage(name, dents=60, rayon=0.015):
    c = Chaine(name, "C8C8C6", 1, 0.35)
    tcn = c.tc(6, 1)
    g = c.node("ShaderNodeTexGradient", 5, 0, gradient_type='RADIAL')
    c.link(tcn.outputs["Object"], g.inputs["Vector"])
    u = c.math('MULTIPLY', 4, 0, a=g.outputs["Factor"], v1=dents)
    sep = c.node("ShaderNodeSeparateXYZ", 5, 2)
    c.link(tcn.outputs["Object"], sep.inputs["Vector"])
    v = c.math('MULTIPLY', 4, 2, a=sep.outputs["Z"], v1=round(dents / (2 * math.pi * rayon), 1))
    a = c.math('ADD', 3, 0, a=u.outputs["Value"], b=v.outputs["Value"])
    d = c.math('SUBTRACT', 3, 2, a=u.outputs["Value"], b=v.outputs["Value"])
    pa = c.math('PINGPONG', 2, 0, a=a.outputs["Value"], v1=0.5)
    pb = c.math('PINGPONG', 2, 2, a=d.outputs["Value"], v1=0.5)
    mn = c.math('MINIMUM', 1, 1, a=pa.outputs["Value"], b=pb.outputs["Value"])
    c.bump(mn.outputs["Value"], 0.3, 0, 1)
    return c.m


def carbone(name, S=250):
    c = Chaine(name, None, 0, 0.3, coat=(1, 0.02))
    tcn = c.tc(7, 1)
    sep = c.node("ShaderNodeSeparateXYZ", 6, 1)
    c.link(tcn.outputs["Object"], sep.inputs["Vector"])
    fx = c.math('MULTIPLY', 5, 0, a=sep.outputs["X"], v1=S)
    fy = c.math('MULTIPLY', 5, 2, a=sep.outputs["Y"], v1=S)
    ix = c.math('FLOOR', 4, 0, a=fx.outputs["Value"])
    iy = c.math('FLOOR', 4, 2, a=fy.outputs["Value"])
    s = c.math('ADD', 3, 1, a=ix.outputs["Value"], b=iy.outputs["Value"])
    md = c.math('FLOORED_MODULO', 2, 1, a=s.outputs["Value"], v1=4)
    lt = c.math('LESS_THAN', 1, 1, a=md.outputs["Value"], v1=2)
    wa = c.node("ShaderNodeTexWave", 2, 3, i_Scale=round(0.314159 * S, 1), bands_direction='X')
    wb = c.node("ShaderNodeTexWave", 2, 4, i_Scale=round(0.314159 * S, 1), bands_direction='Y')
    for t in (wa, wb):
        c.link(tcn.outputs["Object"], t.inputs["Vector"])
    mx = c.mix_float(lt.outputs["Value"], 0, 0, 1, 3)
    c.link(wa.outputs["Factor"], mx.inputs["A"])
    c.link(wb.outputs["Factor"], mx.inputs["B"])
    c.bump(mx.outputs["Result"], 0.1, 0, 3)
    c.mix_color(lt.outputs["Value"], "0B0B0C", "26262A", 0, 1)
    c.m.diffuse_color = lin("161618")
    return c.m


# ---------------------------------------------------------------------------- étape 7 : groupes
def socket(g, name, io, typ, default=None, mn=None, mx=None, subtype=None):
    s = g.interface.new_socket(name, in_out=io, socket_type=typ)
    if subtype:
        s.subtype = subtype
    if default is not None:
        s.default_value = default
    if mn is not None:
        s.min_value = mn
    if mx is not None:
        s.max_value = mx
    return s


def groupe_grain(name="PRC_Grain_Fin"):
    """L'exemple de l'étape 7 : Noise et Bump, avec Échelle et Relief exposés."""
    g = bpy.data.node_groups.new(name, "ShaderNodeTree")
    g.description = "Grain fin : un Noise transformé en relief. Échelle : motifs par mètre ; Relief : Strength du Bump."
    socket(g, "Échelle", "INPUT", "NodeSocketFloat", 1500.0, 1.0, 10000.0)
    socket(g, "Relief", "INPUT", "NodeSocketFloat", 0.05, 0.0, 1.0, "FACTOR")
    socket(g, "Normal", "OUTPUT", "NodeSocketVector")
    N, L = g.nodes, g.links.new
    gi = N.new("NodeGroupInput"); gi.location = (-640, 0)
    go = N.new("NodeGroupOutput"); go.location = (260, 0)
    tc = N.new("ShaderNodeTexCoord"); tc.location = (-640, 260)
    nz = N.new("ShaderNodeTexNoise"); nz.location = (-400, 160)
    nz.inputs["Detail"].default_value = 4
    b = N.new("ShaderNodeBump"); b.location = (-150, 60)
    L(tc.outputs["Object"], nz.inputs["Vector"])
    L(gi.outputs["Échelle"], nz.inputs["Scale"])
    L(nz.outputs["Factor"], b.inputs["Height"])
    L(gi.outputs["Relief"], b.inputs["Strength"])
    L(b.outputs["Normal"], go.inputs["Normal"])
    return g


def groupe_usure(name="PRC_Usure_Bords", axe=True):
    """Le masque des bords usés en chiffres : Ping-Pong et Map Range à la place du Color Ramp.
    axe=True : l'entrée Axe et le Dot Product (défi ★) ; sinon Separate XYZ (Z)."""
    g = bpy.data.node_groups.new(name, "ShaderNodeTree")
    g.description = "Masque d'usure des arêtes, tiré de la normale. Pièce biseautée (Bevel) et lissée."
    if axe:
        socket(g, "Axe", "INPUT", "NodeSocketVector", (0.0, 0.0, 1.0))
    socket(g, "Largeur", "INPUT", "NodeSocketFloat", 0.8, 0.0, 1.0, "FACTOR")
    socket(g, "Quantité", "INPUT", "NodeSocketFloat", 0.4, 0.0, 1.0, "FACTOR")
    socket(g, "Échelle du bruit", "INPUT", "NodeSocketFloat", 400.0, 1.0, 10000.0)
    socket(g, "Masque", "OUTPUT", "NodeSocketFloat")
    N, L = g.nodes, g.links.new

    def n(kind, x, y, **kw):
        nd = N.new(kind)
        nd.location = (x, y)
        for k, v in kw.items():
            setattr(nd, k, v)
        return nd
    gi = n("NodeGroupInput", -1500, -150)
    go = n("NodeGroupOutput", 300, 0)
    tc = n("ShaderNodeTexCoord", -1500, 250)
    if axe:
        dot = n("ShaderNodeVectorMath", -1280, 250, operation='DOT_PRODUCT')
        L(tc.outputs["Normal"], dot.inputs[0])
        L(gi.outputs["Axe"], dot.inputs[1])
        comp = dot.outputs["Value"]
    else:
        sep = n("ShaderNodeSeparateXYZ", -1280, 250)
        L(tc.outputs["Normal"], sep.inputs["Vector"])
        comp = sep.outputs["Z"]
    ab = n("ShaderNodeMath", -1070, 250, operation='ABSOLUTE')
    L(comp, ab.inputs[0])
    pp = n("ShaderNodeMath", -860, 250, operation='PINGPONG')
    pp.inputs[1].default_value = 0.5
    L(ab.outputs["Value"], pp.inputs[0])
    x2 = n("ShaderNodeMath", -650, 250, operation='MULTIPLY')
    x2.inputs[1].default_value = 2.0
    L(pp.outputs["Value"], x2.inputs[0])
    inv = n("ShaderNodeMath", -860, 20, operation='SUBTRACT')
    inv.inputs[0].default_value = 1.0
    L(gi.outputs["Largeur"], inv.inputs[1])
    mr = n("ShaderNodeMapRange", -440, 250)
    L(x2.outputs["Value"], mr.inputs["Value"])
    L(inv.outputs["Value"], mr.inputs["From Min"])
    nz = n("ShaderNodeTexNoise", -650, -120)
    nz.inputs["Detail"].default_value = 8
    nz.inputs["Roughness"].default_value = 0.7
    L(tc.outputs["Object"], nz.inputs["Vector"])
    L(gi.outputs["Échelle du bruit"], nz.inputs["Scale"])
    mul = n("ShaderNodeMath", -230, 150, operation='MULTIPLY')
    L(mr.outputs["Result"], mul.inputs[0])
    L(nz.outputs["Factor"], mul.inputs[1])
    s0 = n("ShaderNodeMath", -650, -420, operation='SUBTRACT')
    s0.inputs[0].default_value = 0.7
    L(gi.outputs["Quantité"], s0.inputs[1])
    s1 = n("ShaderNodeMath", -440, -420, operation='ADD')
    s1.inputs[1].default_value = 0.1
    L(s0.outputs["Value"], s1.inputs[0])
    mr2 = n("ShaderNodeMapRange", 0, 150)
    L(mul.outputs["Value"], mr2.inputs["Value"])
    L(s0.outputs["Value"], mr2.inputs["From Min"])
    L(s1.outputs["Value"], mr2.inputs["From Max"])
    L(mr2.outputs["Result"], go.inputs["Masque"])
    return g


def groupe_tole(name="PRC_Tole_Perforee"):
    g = bpy.data.node_groups.new(name, "ShaderNodeTree")
    g.description = "Tôle perforée, réglée en millimètres : pas de la grille et diamètre des trous. Sortie vers Alpha."
    socket(g, "Pas (mm)", "INPUT", "NodeSocketFloat", 4.0, 0.5, 50.0)
    socket(g, "Diamètre (mm)", "INPUT", "NodeSocketFloat", 2.4, 0.1, 49.0)
    socket(g, "Alpha", "OUTPUT", "NodeSocketFloat")
    N, L = g.nodes, g.links.new
    gi = N.new("NodeGroupInput"); gi.location = (-900, -100)
    go = N.new("NodeGroupOutput"); go.location = (200, 0)
    tc = N.new("ShaderNodeTexCoord"); tc.location = (-900, 250)
    sc = N.new("ShaderNodeMath"); sc.location = (-660, 100); sc.operation = 'DIVIDE'
    sc.inputs[0].default_value = 1000.0
    L(gi.outputs["Pas (mm)"], sc.inputs[1])
    v = N.new("ShaderNodeTexVoronoi"); v.location = (-440, 250)
    v.voronoi_dimensions = '2D'
    v.inputs["Randomness"].default_value = 0.0
    L(tc.outputs["Object"], v.inputs["Vector"])
    L(sc.outputs["Value"], v.inputs["Scale"])
    ra = N.new("ShaderNodeMath"); ra.location = (-660, -150); ra.operation = 'DIVIDE'
    L(gi.outputs["Diamètre (mm)"], ra.inputs[0])
    L(gi.outputs["Pas (mm)"], ra.inputs[1])
    hf = N.new("ShaderNodeMath"); hf.location = (-440, -150); hf.operation = 'MULTIPLY'
    hf.inputs[1].default_value = 0.5
    L(ra.outputs["Value"], hf.inputs[0])
    gt = N.new("ShaderNodeMath"); gt.location = (-200, 100); gt.operation = 'GREATER_THAN'
    L(v.outputs["Distance"], gt.inputs[0])
    L(hf.outputs["Value"], gt.inputs[1])
    L(gt.outputs["Value"], go.inputs["Alpha"])
    return g


def grain_groupe(name, group):
    c = Chaine(name, "1A1A1A", 0, 0.45)
    gn = c.node("ShaderNodeGroup", 0, 1)
    gn.node_tree = group
    c.link(gn.outputs["Normal"], c.p.inputs["Normal"])
    return c.m


def usure_groupe(name, group, peinture="2F5D3A", metal="B8B9BA", axe=(0, 0, 1), largeur=0.8, quantite=0.4):
    c = Chaine(name, peinture, 0, 0.45)
    gn = c.node("ShaderNodeGroup", 2, 0)
    gn.node_tree = group
    gn.width = 200
    if "Axe" in gn.inputs:
        gn.inputs["Axe"].default_value = axe
    gn.inputs["Largeur"].default_value = largeur
    gn.inputs["Quantité"].default_value = quantite
    mask = gn.outputs["Masque"]
    c.mix_color(mask, peinture, metal, 1, 0)
    c.link(mask, c.p.inputs["Metallic"])
    mr = c.maprange(mask, 1, 2, 0.0, 1.0, 0.45, 0.30)
    c.link(mr.outputs["Result"], c.p.inputs["Roughness"])
    return c.m


def tole_groupe(name, group, pas=4.0, diametre=2.4):
    c = Chaine(name, "B8B9BA", 1, 0.35)
    gn = c.node("ShaderNodeGroup", 0, 1)
    gn.node_tree = group
    gn.inputs["Pas (mm)"].default_value = pas
    gn.inputs["Diamètre (mm)"].default_value = diametre
    c.link(gn.outputs["Alpha"], c.p.inputs["Alpha"])
    return c.m


# ---------------------------------------------------------------------------- le défi final
def ajouter_usure(mat, group, metal, axe, largeur=0.8, quantite=0.45):
    """Ajoute l'usure des bords à une matière de la lampe : la couleur d'origine passe au métal du dessous."""
    nt = mat.node_tree
    p = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED')
    gn = nt.nodes.new("ShaderNodeGroup"); gn.node_tree = group; gn.location = (-700, 700); gn.width = 200
    gn.inputs["Axe"].default_value = axe
    gn.inputs["Largeur"].default_value = largeur
    gn.inputs["Quantité"].default_value = quantite
    mc = nt.nodes.new("ShaderNodeMix"); mc.data_type = 'RGBA'; mc.location = (-300, 700)
    base = p.inputs["Base Color"]
    if base.links:
        nt.links.new(base.links[0].from_socket, mc.inputs["A"])
    else:
        mc.inputs["A"].default_value = base.default_value[:]
    mc.inputs["B"].default_value = lin(metal)
    nt.links.new(gn.outputs["Masque"], mc.inputs["Factor"])
    nt.links.new(mc.outputs["Result"], base)
    mm = nt.nodes.new("ShaderNodeMix"); mm.data_type = 'FLOAT'; mm.location = (-300, 500)
    mm.inputs["A"].default_value = p.inputs["Metallic"].default_value
    mm.inputs["B"].default_value = 1.0
    nt.links.new(gn.outputs["Masque"], mm.inputs["Factor"])
    nt.links.new(mm.outputs["Result"], p.inputs["Metallic"])


def ajouter_rayures(mat):
    nt = mat.node_tree
    p = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED')
    tc = nt.nodes.new("ShaderNodeTexCoord"); tc.location = (-1000, 800)
    mp = nt.nodes.new("ShaderNodeMapping"); mp.location = (-800, 800)
    mp.inputs["Scale"].default_value = (1, 1, 0.02)
    nz = nt.nodes.new("ShaderNodeTexNoise"); nz.location = (-600, 800)
    nz.inputs["Scale"].default_value = 2000
    nz.inputs["Detail"].default_value = 2
    r = nt.nodes.new("ShaderNodeValToRGB"); r.location = (-400, 800)
    r.color_ramp.elements[0].position = 0.68
    r.color_ramp.elements[0].color = K
    r.color_ramp.elements[1].position = 0.70
    r.color_ramp.elements[1].color = W
    mr = nt.nodes.new("ShaderNodeMapRange"); mr.location = (-150, 800)
    mr.inputs["To Min"].default_value = p.inputs["Roughness"].default_value
    mr.inputs["To Max"].default_value = 0.6
    L = nt.links.new
    L(tc.outputs["Object"], mp.inputs["Vector"])
    L(mp.outputs["Vector"], nz.inputs["Vector"])
    L(nz.outputs["Factor"], r.inputs["Factor"])
    L(r.outputs["Color"], mr.inputs["Value"])
    L(mr.outputs["Result"], p.inputs["Roughness"])


def ajouter_traces(mat):
    nt = mat.node_tree
    p = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED')
    tc = nt.nodes.new("ShaderNodeTexCoord"); tc.location = (-700, 800)
    nz = nt.nodes.new("ShaderNodeTexNoise"); nz.location = (-500, 800)
    for k, v in (("Scale", 25), ("Detail", 6), ("Roughness", 0.7), ("Distortion", 0.3)):
        nz.inputs[k].default_value = v
    mr = nt.nodes.new("ShaderNodeMapRange"); mr.location = (-280, 800)
    for k, v in (("From Min", 0.55), ("From Max", 0.75), ("To Min", 0.02), ("To Max", 0.4)):
        mr.inputs[k].default_value = v
    nt.links.new(tc.outputs["Object"], nz.inputs["Vector"])
    nt.links.new(nz.outputs["Factor"], mr.inputs["Value"])
    nt.links.new(mr.outputs["Result"], p.inputs["Coat Roughness"])


def ajouter_salete(mat, distance=0.005):
    nt = mat.node_tree
    p = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED')
    ao = nt.nodes.new("ShaderNodeAmbientOcclusion"); ao.location = (-700, 900)
    ao.inputs["Distance"].default_value = distance
    r = nt.nodes.new("ShaderNodeValToRGB"); r.location = (-500, 900)
    r.color_ramp.elements[0].position = 0.85
    r.color_ramp.elements[0].color = W
    r.color_ramp.elements[1].position = 0.99
    r.color_ramp.elements[1].color = K
    mc = nt.nodes.new("ShaderNodeMix"); mc.data_type = 'RGBA'; mc.location = (-250, 900)
    base = p.inputs["Base Color"]
    if base.links:
        nt.links.new(base.links[0].from_socket, mc.inputs["A"])
    else:
        mc.inputs["A"].default_value = base.default_value[:]
    mc.inputs["B"].default_value = lin("4A4034")
    nt.links.new(ao.outputs["AO"], r.inputs["Factor"])
    nt.links.new(r.outputs["Color"], mc.inputs["Factor"])
    nt.links.new(mc.outputs["Result"], base)
