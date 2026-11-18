# Construit _resources/exercices/PRC02_init_maquette_en_kit.blend
# Activité A de l'initiation PRC02 (demi-journée 1) : remonter un véhicule arrivé en vrac.
#
# Usage (Blender 5.2 LTS, en arrière-plan) :
#   "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --factory-startup --python tool\exercices_initiation\build_maquette_kit.py
# Option : définir KIT_VERIFY_DIR pour simuler la solution après l'enregistrement,
# contrôler qu'elle remplit exactement le gabarit et rendre deux images Workbench
# (état en vrac, état remonté) dans ce dossier. Le fichier enregistré n'est pas modifié.

import bpy, bmesh, math, os
from mathutils import Vector, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "_resources", "exercices", "PRC02_init_maquette_en_kit.blend")
VERIFY_DIR = os.environ.get("KIT_VERIFY_DIR")

D = math.radians


# ---------------------------------------------------------------- nettoyage
def reset_scene():
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.cameras,
                 bpy.data.lights, bpy.data.curves):
        for b in list(coll):
            coll.remove(b)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)


# ---------------------------------------------------------------- matériaux
def make_mat(name, rgb):
    m = bpy.data.materials.new(name)
    col = (rgb[0], rgb[1], rgb[2], 1.0)
    m.diffuse_color = col
    try:
        m.use_nodes = True
    except Exception:
        pass
    if m.node_tree:
        bsdf = m.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = col
            bsdf.inputs["Roughness"].default_value = 0.5
    return m


# ---------------------------------------------------------------- géométrie
def box(bm, c, s):
    M = Matrix.Translation(c) @ Matrix.Diagonal((s[0], s[1], s[2], 1.0))
    return bmesh.ops.create_cube(bm, size=1.0, matrix=M)["verts"]


def beam(bm, p, q, w, t):
    """Pavé de section w (X) x t, tendu de p à q dans le plan YZ."""
    p, q = Vector(p), Vector(q)
    v = q - p
    ang = math.atan2(v.z, v.y)
    M = (Matrix.Translation((p + q) / 2) @ Matrix.Rotation(ang, 4, 'X')
         @ Matrix.Diagonal((w, v.length, t, 1.0)))
    bmesh.ops.create_cube(bm, size=1.0, matrix=M)


AXES = {
    'X': Matrix.Rotation(D(90), 4, 'Y'),    # +Z -> +X
    'Y': Matrix.Rotation(D(-90), 4, 'X'),   # +Z -> +Y
    '-Y': Matrix.Rotation(D(90), 4, 'X'),   # +Z -> -Y
}


def cyl(bm, c, r, depth, axis, segs=24, r2=None):
    M = Matrix.Translation(c) @ AXES[axis]
    return bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=segs,
                                 radius1=r, radius2=r if r2 is None else r2,
                                 depth=depth, matrix=M)["verts"]


def prism_x(bm, prof, x0, x1):
    a = [bm.verts.new((x0, y, z)) for (y, z) in prof]
    b = [bm.verts.new((x1, y, z)) for (y, z) in prof]
    n = len(prof)
    bm.faces.new(a)
    bm.faces.new(b)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((a[i], a[j], b[j], b[i]))


def loft(bm, loops):
    vs = [[bm.verts.new(p) for p in loop] for loop in loops]
    n = len(loops[0])
    for a, b in zip(vs[:-1], vs[1:]):
        for i in range(n):
            j = (i + 1) % n
            bm.faces.new((a[i], a[j], b[j], b[i]))
    bm.faces.new(vs[0])
    bm.faces.new(vs[-1])


def profil_x(x, le, te, zc, t):
    """Section losange d'une aile, dans le plan YZ (bord d'attaque le, bord de fuite te)."""
    mid = le + 0.4 * (te - le)
    return [(x, le, zc), (x, mid, zc - t / 2), (x, te, zc), (x, mid, zc + t / 2)]


def profil_z(z, le, te, t):
    """Section losange d'une dérive, dans le plan XY."""
    mid = le + 0.4 * (te - le)
    return [(0, le, z), (t / 2, mid, z), (0, te, z), (-t / 2, mid, z)]


# ---------------------------------------------------------------- kit automobile
def auto_caisse(bm):
    box(bm, (0, 0, 0.60), (1.70, 4.20, 0.60))
    for v in bm.verts:
        if v.co.y < -2.0 and v.co.z > 0.8:
            v.co.z -= 0.12          # capot plongeant
        elif v.co.y > 2.0 and v.co.z > 0.8:
            v.co.z -= 0.05          # hayon


def auto_habitacle(bm):
    box(bm, (0, 0.10, 1.175), (1.50, 2.20, 0.55))
    for v in bm.verts:
        if v.co.z > 1.2:
            v.co.x *= 0.78
            v.co.y = 0.10 + (v.co.y - 0.10) * 0.6 + 0.20


def auto_roue(bm, c=(0.80, -1.30, 0.32)):
    cyl(bm, c, 0.32, 0.22, 'X')


# ---------------------------------------------------------------- kit ferroviaire
NEZ_PROFIL = [(-4.1, 0.85), (-2.5, 0.85), (-2.5, 3.15), (-3.3, 3.15), (-4.1, 2.0)]


def rail_parebrise(bm):
    p0, p1 = Vector((-4.1, 2.0)), Vector((-3.3, 3.15))
    d = p1 - p0
    length = d.length
    d.normalize()
    n = Vector((-d.y, d.x))                     # vers l'avant et le haut
    a, b = p0 + d * 0.1 * length, p0 + d * 0.9 * length
    prof = [a + n * 0.005, b + n * 0.005, b + n * 0.045, a + n * 0.045]
    prism_x(bm, [tuple(p) for p in prof], -1.0, 1.0)


def rail_pantographe(bm):
    box(bm, (0, 0.50, 3.22), (1.0, 0.8, 0.14))
    beam(bm, (0, 0.85, 3.29), (0, 0.30, 3.62), 0.12, 0.06)
    beam(bm, (0, 0.30, 3.62), (0, 0.70, 3.92), 0.10, 0.05)
    box(bm, (0, 0.70, 3.95), (1.6, 0.10, 0.05))


def rail_roue(bm, c=(0.75, -3.30, 0.33)):
    cyl(bm, c, 0.33, 0.13, 'X')


# ---------------------------------------------------------------- kit aéronautique
def aero_nez(bm):
    vs = cyl(bm, (0, -5.1, 1.55), 0.85, 2.2, '-Y', r2=0.06)
    for v in vs:
        t = (-4.0 - v.co.y) / 2.2
        v.co.z -= 0.25 * t * t


def aero_queue(bm):
    vs = cyl(bm, (0, 5.5, 1.55), 0.85, 3.0, 'Y', r2=0.22)
    for v in vs:
        t = (v.co.y - 4.0) / 3.0
        v.co.z += 0.45 * t * t


def aero_aile(bm):
    loft(bm, [profil_x(-6.5, 0.6, 1.6, 1.20, 0.10),
              profil_x(0.0, -0.4, 1.6, 0.95, 0.24),
              profil_x(6.5, 0.6, 1.6, 1.20, 0.10)])


def aero_empennage(bm):
    loft(bm, [profil_x(-2.2, 6.9, 7.6, 4.15, 0.06),
              profil_x(0.0, 6.3, 7.5, 4.15, 0.12),
              profil_x(2.2, 6.9, 7.6, 4.15, 0.06)])


def aero_derive(bm):
    loft(bm, [profil_z(2.0, 5.0, 7.3, 0.18), profil_z(4.15, 6.4, 7.55, 0.10)])


def aero_reacteur(bm, c=(1.30, 3.0, 2.15)):
    cyl(bm, c, 0.42, 2.2, 'Y')


def aero_roue(bm, c=(1.20, 0.80, 0.32)):
    cyl(bm, c, 0.32, 0.18, 'X')


# ---------------------------------------------------------------- description des kits
# Pièce : (nom de l'objet, nom du maillage, constructeur, matériau,
#          vrac = (x, y, rotation en degrés, échelle), masquée)
# Référence : pièce déjà en place, dont on tire des copies liées (Alt + D).
#   steps = gestes de la notice, dans l'ordre : ("ref", décalage) copie la référence seule,
#   ("all", décalage) copie toutes les instances déjà posées. Les positions obtenues
#   servent au gabarit et à la vérification.
# extra_copies : copies liées d'une pièce (le bogie arrière), à ajouter au gabarit.
KITS = [
    dict(
        key="aeronautique", title="Aéronautique", subtitle="Avion d'affaires", cx=-22.0,
        suffix="avion", cube="Cube.013",
        label_y=-11.6,
        pieces=[
            ("Fuselage", "Fuselage", lambda bm: cyl(bm, (0, 0, 1.55), 0.85, 8.0, 'Y'),
             "carrosserie", (5.5, -4.2, (0, 0, 90), 1.0), False),
            ("Nez", "Nez", aero_nez, "carrosserie", (-3.0, -4.6, (0, 0, 0), 0.5), False),
            ("Cône_de_queue", "Cône_de_queue", aero_queue, "carrosserie",
             (-4.5, 4.5, (0, 0, 180), 1.0), False),
            ("Aile", "Aile", aero_aile, "carrosserie", (0.0, -9.6, (0, 0, 180), 1.0), False),
            ("Empennage_horizontal", "Empennage_horizontal", aero_empennage, "carrosserie",
             (-4.5, 9.4, (0, 0, 0), 1.0), True),
            ("Cube.004", "Dérive", aero_derive, "carrosserie", (4.5, 6.0, (0, 90, 0), 1.0), False),
        ],
        refs=[
            dict(name="Réacteur_gauche", mesh="Réacteur_avion", build=aero_reacteur,
                 center=(1.30, 3.0, 2.15), mat="mecanique",
                 steps=[("ref", (-2.6, 0, 0))]),
            dict(name="Roue_principale_gauche", mesh="Roue_avion", build=aero_roue,
                 center=(1.20, 0.80, 0.32), mat="pneu",
                 steps=[("ref", (-2.4, 0, 0)), ("ref", (-1.2, -4.4, 0))]),
        ],
        extra_copies=[],
    ),
    dict(
        key="automobile", title="Automobile", subtitle="Voiture compacte", cx=0.0,
        suffix="voiture", cube="Cube.004",
        label_y=-5.6,
        pieces=[
            ("Caisse", "Caisse", auto_caisse, "carrosserie", (4.3, 0.6, (0, 0, 90), 1.0), False),
            ("Habitacle", "Habitacle", auto_habitacle, "vitrage", (-3.8, 1.6, (180, 0, 0), 1.0), False),
            ("Phare_gauche", "Phare_gauche", lambda bm: box(bm, (0.55, -2.125, 0.68), (0.40, 0.05, 0.12)),
             "optique", (-2.6, -3.9, (0, 0, 0), 1.0), False),
            ("Phare_droit", "Phare_droit", lambda bm: box(bm, (-0.55, -2.125, 0.68), (0.40, 0.05, 0.12)),
             "optique", (-1.6, -3.9, (0, 0, 0), 2.0), True),
            ("Cube.004", "Rétroviseur_gauche", lambda bm: box(bm, (0.93, -0.75, 0.96), (0.16, 0.08, 0.11)),
             "carrosserie", (2.4, -3.9, (0, 0, 45), 1.0), False),
            ("Rétroviseur_droit", "Rétroviseur_droit",
             lambda bm: box(bm, (-0.93, -0.75, 0.96), (0.16, 0.08, 0.11)),
             "carrosserie", (3.4, -3.9, (0, 0, 0), 1.0), False),
            ("Feux_arrière", "Feux_arrière", lambda bm: box(bm, (0, 2.125, 0.74), (1.40, 0.05, 0.10)),
             "feu", (0.0, 4.0, (0, 0, 0), 1.0), False),
        ],
        refs=[
            dict(name="Roue_avant_gauche", mesh="Roue_voiture", build=auto_roue,
                 center=(0.80, -1.30, 0.32), mat="pneu",
                 steps=[("ref", (-1.6, 0, 0)), ("all", (0, 2.6, 0))]),
        ],
        extra_copies=[],
    ),
    dict(
        key="ferroviaire", title="Ferroviaire", subtitle="Avant de tram", cx=17.0,
        suffix="tram", cube="Cube.009",
        label_y=-7.8,
        pieces=[
            ("Caisse", "Caisse", lambda bm: box(bm, (0, 1.0, 2.0), (2.4, 7.0, 2.3)),
             "carrosserie", (5.8, 1.0, (0, 0, 90), 1.0), False),
            ("Nez", "Nez", lambda bm: prism_x(bm, NEZ_PROFIL, -1.2, 1.2),
             "carrosserie", (-4.6, 3.5, (0, 0, 180), 1.0), False),
            ("Pare-brise", "Pare-brise", rail_parebrise, "vitrage", (-4.2, -1.0, (0, 0, 90), 1.0), False),
            ("Bogie", "Bogie", lambda bm: box(bm, (0, -2.4, 0.55), (2.1, 2.6, 0.30)),
             "mecanique", (4.5, -5.6, (0, 0, 0), 1.0), False),
            ("Cube.004", "Pantographe", rail_pantographe, "mecanique", (-4.2, -5.0, (0, 90, 0), 1.0), False),
            ("Phare_gauche", "Phare_gauche", lambda bm: box(bm, (0.8, -4.125, 1.25), (0.36, 0.05, 0.16)),
             "optique", (1.2, -6.4, (0, 0, 0), 1.0), False),
            ("Phare_droit", "Phare_droit", lambda bm: box(bm, (-0.8, -4.125, 1.25), (0.36, 0.05, 0.16)),
             "optique", (2.2, -6.4, (0, 0, 0), 0.5), True),
            ("Attelage", "Attelage", lambda bm: box(bm, (0, -4.35, 0.95), (0.30, 0.50, 0.30)),
             "mecanique", (-1.8, 6.2, (0, 0, 90), 1.0), False),
        ],
        refs=[
            dict(name="Roue_avant_gauche", mesh="Roue_tram", build=rail_roue,
                 center=(0.75, -3.30, 0.33), mat="pneu",
                 steps=[("ref", (-1.5, 0, 0)), ("all", (0, 1.8, 0)), ("all", (0, 5.2, 0))]),
        ],
        extra_copies=[("Bogie", (0, 5.2, 0))],
    ),
]

PALETTE = {
    "carrosserie": ("Kit_carrosserie", (0.80, 0.80, 0.78)),
    "vitrage": ("Kit_vitrage", (0.20, 0.27, 0.34)),
    "pneu": ("Kit_pneu", (0.10, 0.10, 0.11)),
    "optique": ("Kit_optique", (0.98, 0.86, 0.45)),
    "feu": ("Kit_feu_arrière", (0.80, 0.12, 0.10)),
    "mecanique": ("Kit_mécanique", (0.42, 0.44, 0.47)),
}


# ---------------------------------------------------------------- construction
def build_mesh(name, builder):
    bm = bmesh.new()
    builder(bm)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def translated(bm, builder, offset):
    before = set(bm.verts)
    builder(bm)
    for v in bm.verts:
        if v not in before:
            v.co += offset


def snap(v, step=0.05):
    return round(v / step) * step


def recentre(me, origin=None):
    """Place l'origine au centre de la boîte englobante (arrondi à 5 cm), ou à `origin`."""
    if origin is None:
        xs = [v.co for v in me.vertices]
        lo = Vector((min(c.x for c in xs), min(c.y for c in xs), min(c.z for c in xs)))
        hi = Vector((max(c.x for c in xs), max(c.y for c in xs), max(c.z for c in xs)))
        c = (lo + hi) / 2
        origin = Vector((snap(c.x), snap(c.y), snap(c.z)))
    origin = Vector(origin)
    me.transform(Matrix.Translation(-origin))
    me.update()
    return origin


def drop_to_floor(ob):
    """Pose l'objet au sol (z mini = 0) en tenant compte de sa rotation et de son échelle."""
    bpy.context.view_layer.update()
    mw = ob.matrix_world
    zmin = min((mw @ v.co).z for v in ob.data.vertices)
    ob.location.z -= zmin


def add_label(name, body, loc, size, mat, coll):
    cu = bpy.data.curves.new(name, 'FONT')
    cu.body = body
    cu.size = size
    cu.align_x = 'CENTER'
    cu.align_y = 'CENTER'
    cu.materials.append(mat)
    ob = bpy.data.objects.new(name, cu)
    ob.location = loc
    ob.hide_select = True
    coll.objects.link(ob)
    return ob


def build():
    reset_scene()
    scene = bpy.context.scene
    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.length_unit = 'METERS'
    scene.unit_settings.scale_length = 1.0

    mats = {k: make_mat(n, rgb) for k, (n, rgb) in PALETTE.items()}
    mat_txt = make_mat("Exercice_texte", (0.92, 0.92, 0.92))
    mat_txt2 = make_mat("Exercice_texte_secondaire", (0.65, 0.65, 0.65))

    report = {}
    for kit in KITS:
        cx = kit["cx"]
        kit_coll = bpy.data.collections.new(f"Kit {kit['title'].lower()}")
        scene.collection.children.link(kit_coll)
        ghost_coll = bpy.data.collections.new(f"Gabarit {kit['title'].lower()}")
        kit_coll.children.link(ghost_coll)

        ghost_builders = []
        targets = []
        hidden = []
        sfx = kit["suffix"]
        for (obname, mename, builder, matkey, vrac, is_hidden) in kit["pieces"]:
            ghost_builders.append(builder)
            obname = kit["cube"] if obname == "Cube.004" else f"{obname}_{sfx}"
            mename = f"{mename}_{sfx}"
            me = build_mesh(mename, builder)
            me.materials.append(mats[matkey])
            origin = recentre(me)
            ob = bpy.data.objects.new(obname, me)
            kit_coll.objects.link(ob)
            vx, vy, rot, sc = vrac
            ob.location = (cx + vx, vy, 0.0)
            ob.rotation_euler = (D(rot[0]), D(rot[1]), D(rot[2]))
            ob.scale = (sc, sc, sc)
            drop_to_floor(ob)
            targets.append((obname, mename, Vector((cx, 0, 0)) + origin))
            if is_hidden:
                hidden.append(ob)

        for ref in kit["refs"]:
            ref["obname"] = f"{ref['name']}_{sfx}"
            me = build_mesh(ref["mesh"], ref["build"])
            me.materials.append(mats[ref["mat"]])
            c = Vector(ref["center"])
            recentre(me, c)
            ob = bpy.data.objects.new(ref["obname"], me)
            ob.location = Vector((cx, 0, 0)) + c
            kit_coll.objects.link(ob)
            # positions des copies, d'après les gestes de la notice
            placed = [c.copy()]
            for mode, offset in ref["steps"]:
                srcs = placed[:1] if mode == "ref" else list(placed)
                placed += [p + Vector(offset) for p in srcs]
            ref["placed"] = placed
            for p in placed:
                ghost_builders.append(lambda bm, p=tuple(p), f=ref["build"]: f(bm, p))

        for piece_name, offset in kit["extra_copies"]:
            builder = next(p[2] for p in kit["pieces"] if p[0] == piece_name)
            ghost_builders.append(lambda bm, b=builder, o=Vector(offset): translated(bm, b, o))

        # gabarit : toute la forme finale, en fil de fer, non sélectionnable
        ghost_me = build_mesh(f"Gabarit_{kit['key']}", lambda bm: [g(bm) for g in ghost_builders])
        ghost = bpy.data.objects.new(f"Gabarit_{kit['key']}", ghost_me)
        ghost.location = (cx, 0, 0)
        ghost.display_type = 'WIRE'
        ghost.hide_select = True
        ghost.hide_render = True
        ghost_coll.objects.link(ghost)

        add_label(f"Titre_{kit['key']}", kit["title"], (cx, kit["label_y"], 0.01), 1.2, mat_txt, kit_coll)
        add_label(f"Sous-titre_{kit['key']}", f"{kit['subtitle']}  ·  fil de fer : la forme à remplir",
                  (cx, kit["label_y"] - 1.2, 0.01), 0.55, mat_txt2, kit_coll)

        bpy.context.view_layer.update()
        for ob in hidden:
            ob.hide_set(True)
        report[kit["key"]] = dict(targets=targets, refs=kit["refs"], cx=cx)

    write_readme(report)
    setup_ui()
    return report


# ---------------------------------------------------------------- LISEZ-MOI
def fmt_pos(v):
    return f"X {v.x:7.2f}   Y {v.y:6.2f}   Z {v.z:5.2f}"


def positions_table(kit_key, report):
    lines = []
    r = report[kit_key]
    for obname, mename, pos in r["targets"]:
        label = mename if obname.startswith("Cube.") else obname
        lines.append(f"  {label:<22}{fmt_pos(pos)}")
    return lines


def write_readme(report):
    L = []
    a = L.append
    a("LISEZ-MOI : survolez cette zone et appuyez sur Ctrl + Espace pour l'agrandir (même raccourci pour revenir).")
    a("Pour retrouver la Timeline ici : sélecteur de type d'éditeur, en haut à gauche de cette zone.")
    a("")
    a("LA MAQUETTE EN KIT")
    a("PRC02 Design et visualisation temps réel avec Blender, initiation, demi-journée 1. Blender 5.2 LTS.")
    a("")
    a("LA SITUATION")
    a("Un collègue vous envoie la maquette d'un concept pour la revue de design de demain. "
      "Le fichier est arrivé en vrac : des pièces sont déplacées, tournées ou à la mauvaise taille, "
      "une pièce est masquée et une autre a perdu son nom. Une seule roue est posée. "
      "Remontez la maquette.")
    a("")
    a("CHOISIR SON KIT")
    a("Trois kits, un par secteur : Aéronautique (avion d'affaires), Automobile (voiture compacte), "
      "Ferroviaire (avant de tram).")
    a("1. Dans l'Outliner, cliquez l'œil des deux kits que vous ne prenez pas : ils disparaissent de la vue.")
    a("2. Survolez la vue 3D et appuyez sur Origine (Home) : la vue cadre votre kit.")
    a("")
    a("LES REPÈRES")
    a("- Le fil de fer est le gabarit : la forme finale. Il ne se sélectionne pas.")
    a("- Une pièce est en place quand ses arêtes se superposent à celles du gabarit.")
    a("- Pour aligner, passez en vue orthographique : face (1), droite (3) et dessus (7) du pavé numérique. "
      "En perspective, l'œil se trompe facilement.")
    a("- L'avant du véhicule fait face à la vue de face (1). Gauche et droite s'entendent depuis le poste "
      "de conduite : le côté gauche est du côté des X positifs.")
    a("- Contrôle : une pièce en place affiche Rotation 0, 0, 0 et Scale 1, 1, 1 dans la barre latérale (N), "
      "onglet Item. Une rotation de 360° est juste aussi : c'est un tour complet.")
    a("- En cas d'erreur : Ctrl + Z.")
    a("")
    a("SOCLE : REMONTER LA MAQUETTE")
    a("1. Commencez par une pièce seulement déplacée : cliquez-la, puis G et X, Y ou Z pour la faire "
      "glisser sur un seul axe. Clic gauche pour valider, Échap pour annuler.")
    a("2. Une pièce est tournée : R, puis l'axe, puis l'angle (90, 180, 45...) et Entrée.")
    a("3. Une pièce n'a pas la bonne taille : S, puis 2 ou 0.5 et Entrée.")
    a("4. Une pièce manque : cherchez dans l'Outliner l'objet dont l'œil est fermé, et rouvrez-le.")
    a("5. Un objet porte un nom anonyme, Cube.0.. : trouvez ce que c'est, puis renommez-le "
      "(double-clic dans l'Outliner). Indice : dépliez-le dans l'Outliner, son maillage a gardé un nom parlant.")
    a("6. Posez les roues avec des copies liées, comme indiqué pour votre kit ci-dessous. "
      "Alt + D crée la copie et la déplace aussitôt : tapez l'axe, la valeur, puis Entrée.")
    a("Chaque nom se termine par le véhicule (_avion, _voiture, _tram) : deux objets d'un même fichier "
      "ne peuvent pas porter le même nom.")
    a("")
    a("KIT AÉRONAUTIQUE : AVION D'AFFAIRES")
    a("Pièces : Fuselage (tourné), Aile (tournée), Cône_de_queue (retourné), Nez (trop petit), "
      "Empennage_horizontal (masqué), Cube.013.")
    a("Réacteur_gauche_avion et Roue_principale_gauche_avion sont déjà en place.")
    a("1. Réacteur_gauche_avion : Alt + D, X, -2.6, Entrée : le réacteur droit.")
    a("2. Roue_principale_gauche_avion : Alt + D, X, -2.4, Entrée : la roue principale droite.")
    a("3. Roue_principale_gauche_avion : Alt + D, X, -1.2, Entrée, puis G, Y, -4.4, Entrée : "
      "la roue avant, sous le nez.")
    a("")
    a("KIT AUTOMOBILE : VOITURE COMPACTE")
    a("Pièces : Feux_arrière et Rétroviseur_droit (déplacés), Caisse (tournée), Habitacle (retourné), "
      "Phare_gauche, Phare_droit (masqué, trop grand), Cube.004.")
    a("Roue_avant_gauche_voiture est déjà en place.")
    a("1. Roue_avant_gauche_voiture : Alt + D, X, -1.6, Entrée : la roue d'en face. 1,6 m, c'est la voie.")
    a("2. Les deux roues avant (clic, puis Maj + clic) : Alt + D, Y, 2.6, Entrée : les roues arrière. "
      "2,6 m, c'est l'empattement.")
    a("")
    a("KIT FERROVIAIRE : AVANT DE TRAM")
    a("Pièces : Bogie (déplacé), Caisse (tournée), Nez (retourné), Pare-brise (tourné), Attelage (tourné), "
      "Phare_gauche, Phare_droit (masqué, trop petit), Cube.009.")
    a("Placez d'abord le Bogie_tram. Roue_avant_gauche_tram est déjà en place.")
    a("1. Roue_avant_gauche_tram : Alt + D, X, -1.5, Entrée : la roue d'en face, sur le même essieu.")
    a("2. Les deux roues : Alt + D, Y, 1.8, Entrée : le second essieu du bogie.")
    a("3. Les quatre roues et le Bogie_tram : Alt + D, Y, 5.2, Entrée : le bogie arrière.")
    a("")
    a("★ PRÉCISION")
    a("Pour un placement exact, saisissez les positions ci-dessous dans la barre latérale (N), onglet Item, "
      "champs Location : cliquez dans un champ, tapez la valeur, Entrée.")
    a("Raccourcis utiles : Alt + R remet la rotation à 0, Alt + S remet l'échelle à 1.")
    for kit in KITS:
        a("")
        a(f"{kit['title']} :")
        L.extend(positions_table(kit["key"], report))
    a("Les roues et le réacteur droit n'ont rien à saisir : les copies liées tombent juste.")
    a("")
    a("★★ DÉFIS")
    a("1. Toutes les roues d'un coup : cliquez une roue, Tab (Mode Édition), A, puis S, X, 1.4, Entrée, et Tab. "
      "Regardez les autres roues. Pourquoi ont-elles toutes changé ? Réponse en demi-journée 2.")
    a("2. Une variante : clic droit sur la collection de votre kit dans l'Outliner, Duplicate Collection, "
      "puis G et X pour décaler la copie de quelques mètres. Changez une proportion (empattement, hauteur, "
      "longueur du nez...) et comparez les deux versions.")
    a("3. La vue de la revue : Maj + A > Camera, puis orbitez jusqu'à un beau trois-quarts avant et "
      "Ctrl + Alt + 0 (pavé numérique) : la caméra prend votre point de vue. 0 pour regarder à travers.")
    a("")
    a("APRÈS L'ACTIVITÉ")
    a("Rangez votre kit en collections (touche M > New Collection : Carrosserie, Vitrage, Roues...), "
      "nommez les copies (Roue_arrière_gauche...), puis enregistrez sous un nouveau nom avec Maj + Ctrl + S, "
      "par exemple kit_ferroviaire_001.blend. Le bouton + de la fenêtre incrémente le numéro.")

    txt = bpy.data.texts.new("LISEZ-MOI")
    txt.write("\n".join(L) + "\n")
    txt.cursor_set(0)
    return txt


# ---------------------------------------------------------------- interface
def setup_ui():
    txt = bpy.data.texts["LISEZ-MOI"]
    scene = bpy.context.scene
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.color_type = 'MATERIAL'
    scene.display.shading.show_object_outline = True
    scr = bpy.data.screens["Layout"]
    for area in scr.areas:
        if area.type == 'DOPESHEET_EDITOR':
            area.type = 'TEXT_EDITOR'
            sp = area.spaces.active
            sp.text = txt
            sp.show_word_wrap = True
            sp.show_line_numbers = False
            sp.show_syntax_highlight = False
            sp.top = 0
        elif area.type == 'VIEW_3D':
            sp = area.spaces.active
            sp.shading.type = 'SOLID'
            sp.shading.light = 'STUDIO'
            sp.shading.color_type = 'MATERIAL'
            sp.shading.show_object_outline = True
            r3 = sp.region_3d
            r3.view_perspective = 'PERSP'
            r3.view_location = (-2.5, -2.5, 0.0)
            r3.view_rotation = Matrix.Rotation(D(46), 3, 'X').to_quaternion()
            r3.view_distance = 50.0
    # navigateur de fichiers du workspace Shading : pas de chemin absolu mémorisé
    for s in bpy.data.screens:
        for area in s.areas:
            if area.type == 'FILE_BROWSER':
                p = area.spaces.active.params
                if p is not None:
                    p.directory = b"//"


# ---------------------------------------------------------------- vérification
def verify(report):
    import json
    scene = bpy.context.scene
    os.makedirs(VERIFY_DIR, exist_ok=True)

    cam_data = bpy.data.cameras.new("Vérif")
    cam = bpy.data.objects.new("Vérif", cam_data)
    scene.collection.objects.link(cam)
    scene.camera = cam
    cam.location = (-3.0, -60.0, 34.0)
    cam.rotation_euler = (D(62), 0, 0)
    cam_data.lens = 32
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.render.resolution_x, scene.render.resolution_y = 1600, 900
    scene.render.resolution_percentage = 100
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.color_type = 'MATERIAL'
    scene.display.shading.show_object_outline = True
    for ob in bpy.data.objects:
        if ob.name.startswith("Gabarit_"):
            ob.hide_render = False

    scene.render.filepath = os.path.join(VERIFY_DIR, "kit_1_vrac.png")
    bpy.ops.render.render(write_still=True)

    # solution simulée : chaque pièce à sa place, puis les copies liées de la notice
    errors = {}
    for kit in KITS:
        r = report[kit["key"]]
        kit_coll = bpy.data.collections[f"Kit {kit['title'].lower()}"]
        world = []
        for obname, mename, pos in r["targets"]:
            ob = kit_coll.objects[obname]
            ob.hide_set(False)
            ob.location = pos
            ob.rotation_euler = (0, 0, 0)
            ob.scale = (1, 1, 1)
        for ref in kit["refs"]:
            src = kit_coll.objects[ref["obname"]]
            for p in ref["placed"][1:]:
                cp = src.copy()                       # copie liée : même maillage
                kit_coll.objects.link(cp)
                cp.location = Vector((r["cx"], 0, 0)) + p
        for piece_name, offset in kit["extra_copies"]:
            src = kit_coll.objects[f"{piece_name}_{kit['suffix']}"]
            cp = src.copy()
            kit_coll.objects.link(cp)
            cp.location = src.location + Vector(offset)
        bpy.context.view_layer.update()
        pts = set()
        for ob in kit_coll.objects:
            if ob.type != 'MESH' or ob.name.startswith("Gabarit_"):
                continue
            mw = ob.matrix_world
            for v in ob.data.vertices:
                q = mw @ v.co
                pts.add((round(q.x, 3), round(q.y, 3), round(q.z, 3)))
        ghost = bpy.data.objects[f"Gabarit_{kit['key']}"]
        gp = set()
        for v in ghost.data.vertices:
            q = ghost.matrix_world @ v.co
            gp.add((round(q.x, 3), round(q.y, 3), round(q.z, 3)))
        errors[kit["key"]] = dict(pieces=len(pts), gabarit=len(gp),
                                  manquants=len(gp - pts), en_trop=len(pts - gp))

    scene.render.filepath = os.path.join(VERIFY_DIR, "kit_2_remonte.png")
    bpy.ops.render.render(write_still=True)
    print("VERIF " + json.dumps(errors, ensure_ascii=False))


report = build()
bpy.context.preferences.filepaths.save_version = 0      # pas de copie .blend1
bpy.ops.wm.save_as_mainfile(filepath=OUT, compress=True, relative_remap=True)
print("SAVED", OUT, os.path.getsize(OUT))
if VERIFY_DIR:
    verify(report)
