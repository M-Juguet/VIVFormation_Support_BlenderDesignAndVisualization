# Construit _resources/exercices/PRC02_init_rangee_sieges.blend
# (initiation PRC02, demi-journée 2, activité B « La rangée de sièges »).
#
# Usage, depuis la racine du dépôt :
#   "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --factory-startup ^
#       --python tool\exercices_initiation\build_rangee_sieges.py
#
# Le siège cible et le corrigé sont construits avec les mêmes opérateurs que ceux
# du pas à pas du LISEZ-MOI : le script vérifie ainsi que les valeurs fonctionnent.
# La silhouette de 1,75 m est reprise de modele_projet_organise.blend.

import math
import os

import bmesh
import bpy
from mathutils import Euler, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
EXO = os.path.join(ROOT, "_resources", "exercices")
TARGET = os.path.join(EXO, "PRC02_init_rangee_sieges.blend")
SOURCE_SILHOUETTE = os.path.join(EXO, "modele_projet_organise.blend")

# --- Dimensions du pavé de départ (mètres) -------------------------------------
SEAT_W, SEAT_D, SEAT_H = 0.46, 0.50, 0.12  # X, Y, Z
SEAT_X0 = 0.27  # bord du siège côté couloir : demi-couloir de 0,25 m + 2 cm
SEAT_Z0 = 0.33  # dessous de l'assise ; le dessus est à 0,45 m

# --- Valeurs du pas à pas (identiques au LISEZ-MOI) -----------------------------
LOOP_SLIDE_Y = 0.15  # G Y 0.15 : bande arrière de 10 cm
BACK_EXTRUDE = 0.65  # E 0.65 : dossier
BACK_TILT_Y = 0.12  # G Y 0.12 : inclinaison du dossier
BACK_BEVEL = 0.04  # Ctrl + B 0.04
BACK_BEVEL_SEGMENTS = 3
CUSHION_INSET = 0.025  # I 0.025
CUSHION_EXTRUDE = 0.03  # E 0.03
FOOT_INSET = 0.12  # I 0.12 (grande face du dessous seulement)
FOOT_EXTRUDE = 0.33  # E 0.33 : le pied touche le sol
ARRAY_SIDE_FACTOR = 1.05  # premier Array, Relative Offset X
ARRAY_SIDE_COUNT = 2
ARRAY_ROW_PITCH = 0.8  # deuxième Array, Constant Offset Y : le pas
ARRAY_ROW_COUNT = 6

# --- Décor ----------------------------------------------------------------------
FLOOR_X = 1.8  # plancher de -1,8 à 1,8 m : assez large pour une cabine 3+3
FLOOR_Y = (-1.0, 9.0)
AISLE_HALF = 0.25
TARGET_SEAT_X = -2.5  # centre du siège cible, hors du plancher

GREY = (0.62, 0.62, 0.62)
ORANGE = (0.93, 0.5, 0.16)

LISEZ_MOI = """LISEZ-MOI : survolez cette zone et appuyez sur Ctrl + Espace pour l'agrandir (même raccourci pour revenir).
Pour retrouver la Timeline ici : sélecteur de type d'éditeur, en haut à gauche de cette zone.

LA RANGÉE DE SIÈGES
PRC02 Design et visualisation temps réel avec Blender, initiation, demi-journée 2. Blender 5.2 LTS.

SITUATION
Aménagement de cabine. Vous proposez un siège passager et la configuration d'une rangée. Le même siège se retrouve dans un train, un avion ou un car.
Vous partez du pavé gris, Siège, et vous le façonnez avec les outils d'édition. Les modificateurs construisent ensuite toute la cabine à partir de ce seul siège.
Le siège orange, à gauche du plancher, montre le siège terminé. La silhouette mesure 1,75 m : elle donne l'échelle.
Les valeurs sont en mètres et données à titre indicatif : vos proportions peuvent différer.

AVANT DE COMMENCER
- L'origine de Siège, le petit point orange, est placée exprès sur l'axe du couloir (x = 0), et non au centre du pavé. Le modificateur Mirror s'en sert pour placer les sièges de l'autre côté du couloir : ne la déplacez pas.
- Le siège regarde vers vous en vue de face (1 du pavé numérique). 3 donne la vue de profil, Ctrl + 7 la vue de dessous.
- En Mode Édition, 1, 2 et 3 (rangée principale du clavier) choisissent la sélection par sommets, arêtes ou faces.
- Après une opération, F9 rouvre ses réglages pour corriger une valeur sans tout refaire.
- Attention : après E, Échap annule le déplacement, pas l'extrusion. Pour tout annuler, Ctrl + Z.

SOCLE (environ 35 min)
1. Cliquez Siège, puis . (pavé numérique) pour le cadrer. Tab pour passer en Mode Édition.
2. Ctrl + R, puis survolez une arête qui va de l'avant vers l'arrière du pavé : l'aperçu jaune fait le tour du pavé. Clic gauche, puis clic droit pour laisser la boucle au milieu. Tapez ensuite G Y 0.15 et Entrée : la boucle recule et isole une bande de 10 cm à l'arrière.
3. Appuyez sur 3 (sélection par faces). Cliquez la face du dessus de la bande arrière, puis E 0.65 et Entrée : le dossier monte.
4. La face du haut du dossier reste sélectionnée : G Y 0.12 et Entrée. Le dossier s'incline vers l'arrière.
5. Toujours sur cette face : Ctrl + B, tournez la molette jusqu'à 3 segments, tapez 0.04, puis Entrée. Le haut du dossier s'arrondit.
6. Cliquez la face du dessus de l'assise, devant le dossier. I 0.025 et Entrée, puis E 0.03 et Entrée : un coussin.
7. Ctrl + 7 (pavé numérique) pour voir le dessous. Cliquez la grande face du dessous, à l'avant. I 0.12 et Entrée, puis E 0.33 et Entrée : le pied descend jusqu'au sol.
8. Tab pour revenir en Mode Objet. Dans l'éditeur de propriétés, ouvrez l'onglet Modifiers (la clé à molette), puis Add Modifier > Generate :
   a. Array : Count 2. Relative Offset reste coché ; réglez son Factor X à 1.05. Deux sièges côte à côte.
   b. Un deuxième Array : décochez Relative Offset, cochez Constant Offset, réglez Distance X à 0 et Distance Y à 0.8, puis Count à 6. Six rangs : cette distance est le pas entre deux rangs.
   c. Mirror : Axis X est déjà coché. Les sièges se reflètent de l'autre côté du couloir. Vous obtenez une cabine 2+2 de 24 sièges.
9. Tab, puis A pour tout sélectionner, puis S X 0.9 et Entrée : le siège s'affine de 10 %, et les 24 sièges changent en même temps. C'est l'intérêt des modificateurs : toute la cabine se recalcule à partir d'un seul siège. Ctrl + Z si vous préférez revenir à la largeur d'origine, puis Tab.

★ POUR ALLER PLUS LOIN
- Le pas : dans le deuxième Array, essayez par exemple une Distance Y de 0.78, puis de 0.95. Comparez l'espace entre deux rangs en vue de profil (3), avec la silhouette pour l'échelle.
- Une cabine 3+3 : passez le Count du premier Array à 3. Le plancher reste assez large.
- Un couloir plus large : Tab, A, puis G X 0.05 et Entrée. Le Mirror suit, et le couloir s'élargit de 10 cm. Puis Tab.
- Des formes plus douces : ajoutez un modificateur Bevel (Amount 0.01, Segments 2), puis remontez-le en haut de la pile avec la flèche de son en-tête > Move to First.
- L'ordre compte : remontez le Mirror en haut de la pile (Move to First) et observez la cabine. Remettez-le ensuite en bas (Move to Last).

★★ DÉFIS
- Des accoudoirs : en Mode Édition, sélectionnez les deux faces latérales de l'assise, à gauche et à droite (Maj + clic ; tournez autour du siège pour atteindre la seconde). Alt + E > Extrude Individual Faces, tapez 0.04 puis Entrée : chaque face sort de 4 cm. Sélectionnez ensuite les faces du dessus des deux petits blocs créés, puis E 0.2 et Entrée. Le premier Array écarte tout seul les sièges.
- Une première classe 2+1 : supprimez le Mirror (la croix de son en-tête). Siège sélectionné, Alt + D puis Échap crée une copie liée, restée en place, qui partage le maillage. Sur cette copie, passez le Count du premier Array à 1, puis G X -1 et Entrée : un siège seul de l'autre côté du couloir. Modifiez ensuite l'un des sièges en Mode Édition : l'autre côté suit, puisque le maillage est partagé.

CORRIGÉ
La collection Corrigé, masquée, contient la cabine terminée (étapes 1 à 8). Cliquez l'œil de la collection dans l'Outliner pour l'afficher, et masquez Siège pour mieux la voir.
"""


# --- Outils ---------------------------------------------------------------------
def material(name, rgb):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*rgb, 1.0)
    if mat.node_tree is None:
        mat.use_nodes = True
    mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*rgb, 1.0)
    return mat


def new_collection(name, parent=None):
    col = bpy.data.collections.new(name)
    (parent or bpy.context.scene.collection).children.link(col)
    return col


def plane_object(name, x0, x1, y0, y1, mat, col):
    """Rectangle horizontal à z = 0, une seule face, échelle appliquée."""
    me = bpy.data.meshes.new(name)
    me.from_pydata([(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)], [], [(0, 1, 2, 3)])
    me.materials.append(mat)
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    return ob


def text_object(name, body, size, loc, mat, col):
    cu = bpy.data.curves.new(name, "FONT")
    cu.body = body
    cu.size = size
    cu.align_x = "CENTER"
    cu.align_y = "CENTER"
    cu.materials.append(mat)
    ob = bpy.data.objects.new(name, cu)
    ob.location = loc
    col.objects.link(ob)
    return ob


def activate(ob):
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = ob
    ob.select_set(True)


def new_seat_block(name, mat, col):
    """Le pavé de départ : 0,46 × 0,50 × 0,12 m, origine sur l'axe du couloir."""
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((
            SEAT_X0 + SEAT_W / 2 + v.co.x * SEAT_W,
            v.co.y * SEAT_D,
            SEAT_Z0 + SEAT_H / 2 + v.co.z * SEAT_H,
        ))
    bm.to_mesh(me)
    bm.free()
    me.materials.append(mat)
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    return ob


def select_only(ob, face_pred=None, vert_pred=None):
    """Sélectionne des faces (ou des sommets) en Mode Édition, comme un clic."""
    bm = bmesh.from_edit_mesh(ob.data)
    bm.normal_update()
    for elems in (bm.faces, bm.edges, bm.verts):
        for el in elems:
            el.select_set(False)
    count = 0
    if face_pred:
        for f in bm.faces:
            if face_pred(f):
                f.select_set(True)
                count += 1
    if vert_pred:
        for v in bm.verts:
            if vert_pred(v):
                v.select_set(True)
                count += 1
        for e in bm.edges:
            if e.verts[0].select and e.verts[1].select:
                e.select_set(True)
    bm.select_flush_mode()
    bmesh.update_edit_mesh(ob.data)
    return count


def center(f):
    return f.calc_center_median()


def step_loop_cut(ob):
    """Étape 2 : Ctrl + R au milieu, puis G Y 0.15.
    loopcut_slide plante Blender 5.2.1 en script : la boucle est créée sur
    l'anneau d'arêtes avec subdivide_edges, ce qui donne la même géométrie."""
    bm = bmesh.from_edit_mesh(ob.data)
    ring = [e for e in bm.edges if abs(e.verts[0].co.y - e.verts[1].co.y) > 1e-4]
    assert len(ring) == 4, len(ring)
    bmesh.ops.subdivide_edges(bm, edges=ring, cuts=1, use_grid_fill=True)
    bmesh.update_edit_mesh(ob.data)
    n = select_only(ob, vert_pred=lambda v: abs(v.co.y) < 1e-5)
    assert n == 4, n
    bpy.ops.transform.translate(value=(0, LOOP_SLIDE_Y, 0))


def seat_edit_steps(ob, foot_mode="front_face"):
    """Étapes 2 à 7 du LISEZ-MOI, avec les opérateurs de Blender."""
    activate(ob)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.context.tool_settings.mesh_select_mode = (False, False, True)

    step_loop_cut(ob)

    # 3. Face du dessus de la bande arrière : E 0.65.
    top = SEAT_Z0 + SEAT_H
    n = select_only(ob, face_pred=lambda f: f.normal.z > 0.99 and abs(center(f).z - top) < 1e-4
                    and center(f).y > LOOP_SLIDE_Y)
    assert n == 1, n
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, BACK_EXTRUDE)})
    # 4. G Y 0.12 sur la face extrudée, toujours sélectionnée.
    bpy.ops.transform.translate(value=(0, BACK_TILT_Y, 0))
    # 5. Ctrl + B : 0.04, 3 segments.
    bpy.ops.mesh.bevel(offset=BACK_BEVEL, segments=BACK_BEVEL_SEGMENTS, affect="EDGES")

    # 6. Face du dessus de l'assise : I 0.025, puis E 0.03.
    n = select_only(ob, face_pred=lambda f: f.normal.z > 0.99 and abs(center(f).z - top) < 1e-4
                    and center(f).y < LOOP_SLIDE_Y)
    assert n == 1, n
    bpy.ops.mesh.inset(thickness=CUSHION_INSET, depth=0)
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, CUSHION_EXTRUDE)})

    # 7. Grande face du dessous : I 0.12, puis E 0.33.
    if foot_mode == "front_face":
        pred = lambda f: f.normal.z < -0.99 and center(f).y < LOOP_SLIDE_Y
        inset = FOOT_INSET
    else:  # variante écartée : les deux faces du dessous, I 0.15
        pred = lambda f: f.normal.z < -0.99
        inset = 0.15
    n = select_only(ob, face_pred=pred)
    bpy.ops.mesh.inset(thickness=inset, depth=0)
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, -FOOT_EXTRUDE)})

    bpy.ops.object.mode_set(mode="OBJECT")
    return n


def add_cabin_stack(ob):
    """Étape 8 : Array, Array, Mirror, avec les valeurs par défaut de Blender
    pour tout ce que le LISEZ-MOI ne demande pas de changer."""
    activate(ob)
    bpy.ops.object.modifier_add(type="ARRAY")
    a1 = ob.modifiers[-1]
    a1.count = ARRAY_SIDE_COUNT
    a1.relative_offset_displace = (ARRAY_SIDE_FACTOR, 0, 0)
    bpy.ops.object.modifier_add(type="ARRAY")
    a2 = ob.modifiers[-1]
    a2.use_relative_offset = False
    a2.use_constant_offset = True
    a2.constant_offset_displace = (0, ARRAY_ROW_PITCH, 0)
    a2.count = ARRAY_ROW_COUNT
    bpy.ops.object.modifier_add(type="MIRROR")
    mirror = ob.modifiers[-1]
    assert tuple(mirror.use_axis) == (True, False, False)
    return a1, a2, mirror


def islands(ob):
    """Nombre de parties séparées du maillage évalué (sièges)."""
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    me = ev.to_mesh()
    bm = bmesh.new()
    bm.from_mesh(me)
    seen, parts = set(), 0
    for v in bm.verts:
        if v.index in seen:
            continue
        parts += 1
        stack = [v]
        while stack:
            cur = stack.pop()
            if cur.index in seen:
                continue
            seen.add(cur.index)
            stack.extend(e.other_vert(cur) for e in cur.link_edges)
    xs = [ev.matrix_world @ v.co for v in bm.verts]
    bbox = (Vector((min(p.x for p in xs), min(p.y for p in xs), min(p.z for p in xs))),
            Vector((max(p.x for p in xs), max(p.y for p in xs), max(p.z for p in xs))))
    bm.free()
    ev.to_mesh_clear()
    return parts, bbox


# --- Construction ---------------------------------------------------------------
def build():
    # Scène d'usine vidée.
    for name in ("Cube", "Camera", "Light"):
        ob = bpy.data.objects.get(name)
        if ob:
            bpy.data.objects.remove(ob, do_unlink=True)
    old = bpy.data.collections.get("Collection")
    if old:
        bpy.data.collections.remove(old)
    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

    scene = bpy.context.scene
    scene.cursor.location = (0, 0, 0)

    m_dep = material("Exercice_départ", GREY)
    m_cib = material("Exercice_cible", ORANGE)
    m_txt = material("Exercice_texte", (0.92, 0.92, 0.92))
    m_txt2 = material("Exercice_texte_secondaire", (0.65, 0.65, 0.65))
    m_floor = material("Cabine_plancher", (0.30, 0.31, 0.33))
    m_aisle = material("Cabine_couloir", (0.42, 0.38, 0.33))

    c_seat = new_collection("Siège")
    c_target = new_collection("Siège cible")
    c_cabin = new_collection("Cabine")
    c_text = new_collection("Textes")
    c_fix = new_collection("Corrigé")

    # Cabine : plancher en deux bandes de part et d'autre du couloir (aucune face superposée).
    floor = bpy.data.meshes.new("Plancher")
    y0, y1 = FLOOR_Y
    floor.from_pydata(
        [(-FLOOR_X, y0, 0), (-AISLE_HALF, y0, 0), (-AISLE_HALF, y1, 0), (-FLOOR_X, y1, 0),
         (AISLE_HALF, y0, 0), (FLOOR_X, y0, 0), (FLOOR_X, y1, 0), (AISLE_HALF, y1, 0)],
        [], [(0, 1, 2, 3), (4, 5, 6, 7)])
    floor.materials.append(m_floor)
    ob_floor = bpy.data.objects.new("Plancher", floor)
    c_cabin.objects.link(ob_floor)
    plane_object("Couloir", -AISLE_HALF, AISLE_HALF, y0, y1, m_aisle, c_cabin)

    # Silhouette de 1,75 m, reprise du modèle de projet organisé.
    with bpy.data.libraries.load(SOURCE_SILHOUETTE, link=False) as (src, dst):
        dst.objects = ["Silhouette_1m75"]
    sil = dst.objects[0]
    c_cabin.objects.link(sil)
    sil.location = (0, -0.8, 0)
    sil.rotation_euler = (0, 0, 0)
    for lib in list(bpy.data.libraries):
        bpy.data.libraries.remove(lib)

    # Siège de départ (gris), cible (orange), corrigé (gris, avec la pile).
    seat = new_seat_block("Siège", m_dep, c_seat)

    target = new_seat_block("Siège_cible", m_cib, c_target)
    seat_edit_steps(target)
    target.location.x = TARGET_SEAT_X - (SEAT_X0 + SEAT_W / 2)

    fixed = new_seat_block("Siège_corrigé", m_dep, c_fix)
    seat_edit_steps(fixed)
    add_cabin_stack(fixed)

    # Textes au sol.
    text_object("Titre", "Rangée de sièges", 0.8, (0, -2.25, 0.01), m_txt, c_text)
    text_object("Texte_départ", "départ", 0.4, (0.75, -0.62, 0.01), m_txt2, c_text)
    text_object("Texte_cible", "cible", 0.4, (TARGET_SEAT_X, -0.62, 0.01), m_txt2, c_text)
    text_object("Légende", "gris : siège de départ   ·   orange : siège cible", 0.5,
                (0, -3.25, 0.01), m_txt2, c_text)

    # Corrigé masqué dans la vue (œil fermé dans l'Outliner).
    bpy.context.view_layer.layer_collection.children["Corrigé"].hide_viewport = True

    # Texte LISEZ-MOI.
    txt = bpy.data.texts.new("LISEZ-MOI")
    txt.write(LISEZ_MOI)
    txt.cursor_set(0)

    # Affichage : Solid, Studio, couleur des matériaux, contour des objets.
    shading = scene.display.shading
    shading.light = "STUDIO"
    shading.color_type = "MATERIAL"
    shading.show_object_outline = True

    view_rot = Euler((math.radians(58), 0, math.radians(-28))).to_quaternion()
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == "VIEW_3D":
                sp = area.spaces.active
                sp.shading.type = "SOLID"
                sp.shading.light = "STUDIO"
                sp.shading.color_type = "MATERIAL"
                sp.shading.show_object_outline = True
                if screen.name == "Layout":
                    r3d = sp.region_3d
                    r3d.view_perspective = "PERSP"
                    r3d.view_location = (-0.5, 2.2, 0.4)
                    r3d.view_rotation = view_rot
                    r3d.view_distance = 11.5
            # Navigateurs de fichiers (espace actif ou non) : dossier « // ».
            # Le champ est un tampon de taille fixe : écrire « // » seul laisse la fin
            # de l'ancien chemin (C:\Users\<nom>\Documents) après le zéro final.
            # On l'écrase d'abord entièrement.
            for space in area.spaces:
                if space.type == "FILE_BROWSER" and space.params is not None:
                    space.params.directory = b"/" * 1200
                    space.params.directory = b"//"

    # Workspace Layout : la Timeline devient un Text Editor qui affiche le LISEZ-MOI.
    layout = bpy.data.screens["Layout"]
    done = False
    for area in layout.areas:
        if area.type == "DOPESHEET_EDITOR":
            area.type = "TEXT_EDITOR"
            sp = area.spaces.active
            sp.text = txt
            sp.show_word_wrap = True
            sp.show_line_numbers = False
            sp.show_syntax_highlight = False
            sp.top = 0
            done = True
            break
    assert done, "zone Timeline introuvable"

    # Siège actif à l'ouverture, en Mode Objet.
    activate(seat)

    # Contrôles avant enregistrement.
    parts, (lo, hi) = islands(fixed)
    assert parts == 24, parts
    assert abs(lo.z) < 1e-6, lo.z
    print("CONTROLE corrigé :", parts, "sièges, bbox", tuple(round(v, 3) for v in lo),
          tuple(round(v, 3) for v in hi))
    _, (tlo, thi) = islands(target)
    print("CONTROLE cible : bbox", tuple(round(v, 3) for v in tlo), tuple(round(v, 3) for v in thi),
          "sommets", len(target.data.vertices), "faces", len(target.data.polygons))

    bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    bpy.context.preferences.filepaths.save_version = 0      # pas de copie .blend1
    bpy.ops.wm.save_as_mainfile(filepath=TARGET, compress=True)
    print("ENREGISTRE", TARGET, os.path.getsize(TARGET))


if __name__ == "__main__":
    build()
