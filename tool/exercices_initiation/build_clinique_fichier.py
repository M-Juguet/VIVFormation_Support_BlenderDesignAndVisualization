# Construit _resources/exercices/PRC02_init_clinique_fichier.blend
# (initiation PRC02, demi-journée 2, activité C « La clinique du fichier »).
#
# Usage, depuis la racine du dépôt :
#   "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --factory-startup ^
#       --python tool\exercices_initiation\build_clinique_fichier.py
#
# Le fichier livré contient cinq pièces « malades » (gris) et, à côté de chacune,
# la même pièce saine (orange) pour comparer. Les repères fixes sont gris foncé.
# Les tailles des zones de l'interface se règlent à part (impossible en arrière-plan).

import math
import os

import bmesh
import bpy
from mathutils import Matrix, Vector

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT = os.path.join(ROOT, "_resources", "exercices", "PRC02_init_clinique_fichier.blend")

# --------------------------------------------------------------------------
# Scène vierge
# --------------------------------------------------------------------------
scene = bpy.context.scene
for ob in list(bpy.data.objects):
    bpy.data.objects.remove(ob, do_unlink=True)
for col in list(bpy.data.collections):
    bpy.data.collections.remove(col)
for block in (bpy.data.meshes, bpy.data.cameras, bpy.data.lights, bpy.data.materials):
    for item in list(block):
        block.remove(item)

scene.unit_settings.system = 'METRIC'
scene.unit_settings.length_unit = 'METERS'
scene.unit_settings.scale_length = 1.0
scene.cursor.location = (0.0, 0.0, 0.0)


# --------------------------------------------------------------------------
# Matériaux (mêmes valeurs que exercices_modelisation_primitives.blend)
# --------------------------------------------------------------------------
def make_material(name, grey_or_rgb):
    rgb = (grey_or_rgb,) * 3 if isinstance(grey_or_rgb, float) else grey_or_rgb
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*rgb, 1.0)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*rgb, 1.0)
    return mat


MAT_DEPART = make_material("Exercice_départ", 0.62)
MAT_CIBLE = make_material("Exercice_cible", (0.93, 0.5, 0.16))
MAT_TEXTE = make_material("Exercice_texte", 0.92)
MAT_TEXTE_2 = make_material("Exercice_texte_secondaire", 0.65)
MAT_REPERE = make_material("Exercice_repère", 0.3)


# --------------------------------------------------------------------------
# Outils
# --------------------------------------------------------------------------
def new_collection(name, parent=None):
    col = bpy.data.collections.new(name)
    (parent or scene.collection).children.link(col)
    return col


def object_from_bmesh(name, bm, collection, material, location=(0, 0, 0), mesh_name=None):
    me = bpy.data.meshes.new(mesh_name or name)
    bm.to_mesh(me)
    bm.free()
    me.materials.append(material)
    ob = bpy.data.objects.new(name, me)
    ob.location = location
    collection.objects.link(ob)
    return ob


def box_bmesh(sx, sy, sz):
    """Pavé centré sur l'origine, de dimensions sx × sy × sz (échelle dans le maillage)."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=(sx, sy, sz), verts=bm.verts)
    return bm


def shade_smooth(me, sharp_angle=None):
    if hasattr(me, "shade_smooth"):
        me.shade_smooth()
    else:
        for p in me.polygons:
            p.use_smooth = True
    if sharp_angle is not None:
        # Équivalent de Shade Auto Smooth : arêtes vives au-delà de l'angle donné.
        me.set_sharp_from_angle(angle=math.radians(sharp_angle))


def add_text(name, body, location, size, material, collection):
    curve = bpy.data.curves.new(name, 'FONT')
    curve.body = body
    curve.size = size
    curve.align_x = 'CENTER'
    curve.align_y = 'TOP' if "\n" in body else 'BOTTOM_BASELINE'
    curve.materials.append(material)
    ob = bpy.data.objects.new(name, curve)
    ob.location = (location[0], location[1], 0.01)
    collection.objects.link(ob)
    return ob


# --------------------------------------------------------------------------
# Disposition : une rangée de patients, pièce malade à gauche, pièce saine à droite
# --------------------------------------------------------------------------
PITCH = 8.0          # écart entre deux patients (m)
PAIR = 1.7           # demi-écart entre pièce malade et pièce saine
TITLE_Y = -2.75
LABEL_Y = -1.55
patients_x = [i * PITCH for i in range(5)]

col_textes = None  # créée à la fin pour rester en bas de l'Outliner


# ---------------- Patient 1 : le carénage cabossé (normales inversées) ------
# En Solid, les faces inversées sont éclairées à l'envers : le flanc paraît enfoncé.
def carenage_bmesh():
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=1.0)
    bmesh.ops.scale(bm, vec=(1.2, 0.7, 0.55), verts=bm.verts)
    return bm


col1 = new_collection("Patient 1 - Carénage")
x = patients_x[0]
bm = carenage_bmesh()
bm.faces.ensure_lookup_table()
# Une plaque de faces sur le flanc avant droit, bien visible dans la vue de départ.
flipped = [f for f in bm.faces
           if f.calc_center_median().x > 0.1 and f.calc_center_median().y < -0.15
           and f.calc_center_median().z > -0.15]
bmesh.ops.reverse_faces(bm, faces=flipped)
carenage = object_from_bmesh("Carénage", bm, col1, MAT_DEPART, (x - PAIR, 0, 0.55))
shade_smooth(carenage.data)

bm = carenage_bmesh()
carenage_sain = object_from_bmesh("Carénage_sain", bm, col1, MAT_CIBLE, (x + PAIR, 0, 0.55))
shade_smooth(carenage_sain.data)


# ---------------- Patient 2 : l'accoudoir déformé (échelle non appliquée) ---
def add_bevel(ob, width):
    mod = ob.modifiers.new("Bevel", 'BEVEL')
    mod.width = width
    mod.segments = 4
    mod.limit_method = 'ANGLE'
    return mod


col2 = new_collection("Patient 2 - Accoudoir")
x = patients_x[1]
ACC = (2.4, 0.5, 0.4)
accoudoir = object_from_bmesh("Accoudoir", box_bmesh(1, 1, 1), col2, MAT_DEPART,
                              (x - PAIR, 0, ACC[2] / 2))
accoudoir.scale = ACC
add_bevel(accoudoir, 0.1)
accoudoir_sain = object_from_bmesh("Accoudoir_sain", box_bmesh(*ACC), col2, MAT_CIBLE,
                                   (x + PAIR, 0, ACC[2] / 2))
add_bevel(accoudoir_sain, 0.1)
# Les deux accoudoirs mesurent 2,4 m : on les tourne de 90° pour qu'ils tiennent côte à côte.
for ob in (accoudoir, accoudoir_sain):
    ob.rotation_euler = (0, 0, math.radians(90))


# ---------------- Patient 3 : le bouton qui ne s'arrondit pas (sommets en double)
def bouton_bmesh():
    return box_bmesh(1.4, 1.4, 0.6)


def add_subsurf(ob):
    mod = ob.modifiers.new("Subdivision", 'SUBSURF')
    mod.levels = 2
    mod.render_levels = 2
    return mod


col3 = new_collection("Patient 3 - Bouton")
x = patients_x[2]
bm = bouton_bmesh()
bm.faces.ensure_lookup_table()
top = [f for f in bm.faces if f.normal.z > 0.9]
# Équivalent de E puis Échap : extrusion de la face du dessus, sans déplacement.
bmesh.ops.extrude_face_region(bm, geom=top)
restes = [f for f in top if f.is_valid]  # selon la version, la face d'origine subsiste
if restes:
    bmesh.ops.delete(bm, geom=restes, context='FACES_ONLY')
bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
bouton = object_from_bmesh("Bouton", bm, col3, MAT_DEPART, (x - PAIR, 0, 0.3))
add_subsurf(bouton)
shade_smooth(bouton.data)

bouton_sain = object_from_bmesh("Bouton_sain", bouton_bmesh(), col3, MAT_CIBLE, (x + PAIR, 0, 0.3))
add_subsurf(bouton_sain)
shade_smooth(bouton_sain.data)


# ---------------- Patient 4 : les hublots jumeaux (données partagées) --------
def hublot_bmesh(stretch_z=1.0):
    """Hublot debout face à -Y : disque, cadre (Inset) et vitre en retrait."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=32,
                          radius1=0.4, radius2=0.4, depth=0.12)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(math.radians(90), 3, 'X'))
    bm.normal_update()
    bm.faces.ensure_lookup_table()
    front = [f for f in bm.faces if f.normal.y < -0.9]
    ret = bmesh.ops.inset_region(bm, faces=front, thickness=0.08, depth=0.0)
    # La face avant d'origine devient la vitre : on la recule de 4 cm.
    vitre = front[0]
    bmesh.ops.translate(bm, verts=list(vitre.verts), vec=(0, 0.04, 0))
    if stretch_z != 1.0:
        bmesh.ops.scale(bm, vec=(1, 1, stretch_z), verts=bm.verts)
    return bm


col4 = new_collection("Patient 4 - Hublots")
x = patients_x[3]
HUB_Z = 0.75
me_hublot = bpy.data.meshes.new("Hublot")
hublot_bmesh().to_mesh(me_hublot)
me_hublot.materials.append(MAT_DEPART)
shade_smooth(me_hublot, sharp_angle=30)
hublot_g = bpy.data.objects.new("Hublot_gauche", me_hublot)
hublot_d = bpy.data.objects.new("Hublot_droit", me_hublot)  # copie liée (Alt + D)
hublot_g.location = (x - PAIR - 0.5, 0, HUB_Z)
hublot_d.location = (x - PAIR + 0.5, 0, HUB_Z)
for ob in (hublot_g, hublot_d):
    col4.objects.link(ob)

for name, stretch, dx in (("Hublot_gauche_sain", 1.0, -0.5), ("Hublot_droit_sain", 1.5, 0.5)):
    ob = object_from_bmesh(name, hublot_bmesh(stretch), col4, MAT_CIBLE, (x + PAIR + dx, 0, HUB_Z))
    shade_smooth(ob.data, sharp_angle=30)


# ---------------- Patient 5 : la porte qui tourne mal (origine mal placée) ---
col5 = new_collection("Patient 5 - Porte")
x = patients_x[4]
DOOR = (1.0, 0.06, 1.8)
POST = (0.1, 0.12, 1.9)


def cadre(collection, cx, suffix):
    """Montant côté charnières, montant côté serrure et linteau, plus deux charnières."""
    bm = bmesh.new()
    for px in (cx - DOOR[0] / 2 - POST[0] / 2, cx + DOOR[0] / 2 + POST[0] / 2):
        part = box_bmesh(*POST)
        bmesh.ops.translate(part, verts=part.verts, vec=(px, 0, POST[2] / 2))
        tmp = bpy.data.meshes.new("tmp")
        part.to_mesh(tmp)
        part.free()
        bm.from_mesh(tmp)
        bpy.data.meshes.remove(tmp)
    linteau = box_bmesh(DOOR[0] + 2 * POST[0], POST[1], 0.1)
    bmesh.ops.translate(linteau, verts=linteau.verts, vec=(cx, 0, POST[2] + 0.05))
    tmp = bpy.data.meshes.new("tmp")
    linteau.to_mesh(tmp)
    linteau.free()
    bm.from_mesh(tmp)
    bpy.data.meshes.remove(tmp)
    frame = object_from_bmesh("Cadre" + suffix, bm, collection, MAT_REPERE)

    bm = bmesh.new()
    for hz in (0.35, 1.45):
        part = bmesh.new()
        bmesh.ops.create_cone(part, cap_ends=True, segments=16, radius1=0.03, radius2=0.03, depth=0.2)
        bmesh.ops.translate(part, verts=part.verts, vec=(cx - DOOR[0] / 2, -DOOR[1] / 2, hz))
        tmp = bpy.data.meshes.new("tmp")
        part.to_mesh(tmp)
        part.free()
        bm.from_mesh(tmp)
        bpy.data.meshes.remove(tmp)
    hinges = object_from_bmesh("Charnières" + suffix, bm, collection, MAT_REPERE)
    for ob in (frame, hinges):
        ob.hide_select = True
    return frame, hinges


cx = x - PAIR
cadre(col5, cx, "")
porte = object_from_bmesh("Porte", box_bmesh(*DOOR), col5, MAT_DEPART, (cx, 0, DOOR[2] / 2 + 0.01))

cx = x + PAIR
cadre(col5, cx, "_sain")
# Pièce saine : origine sur l'arête des charnières, porte ouverte de 90° (R Z 90).
bm = box_bmesh(*DOOR)
bmesh.ops.translate(bm, verts=bm.verts, vec=(DOOR[0] / 2, DOOR[1] / 2, DOOR[2] / 2))
porte_saine = object_from_bmesh("Porte_saine", bm, col5, MAT_CIBLE,
                                (cx - DOOR[0] / 2, -DOOR[1] / 2, 0.01))
porte_saine.rotation_euler = (0, 0, math.radians(90))


# --------------------------------------------------------------------------
# Textes au sol
# --------------------------------------------------------------------------
col_textes = new_collection("Textes")
titres = [
    "1 · Le carénage cabossé",
    "2 · L'accoudoir déformé",
    "3 · Le bouton qui\nne s'arrondit pas",
    "4 · Les hublots jumeaux",
    "5 · La porte qui\ntourne mal",
]
for i, (px, titre) in enumerate(zip(patients_x, titres), start=1):
    ob = add_text(f"Patient{i}_titre", titre, (px, TITLE_Y), 0.8, MAT_TEXTE, col_textes)
    if "\n" in titre:
        # Les titres sur deux lignes partent du haut : on aligne leur première ligne.
        ob.location.y = TITLE_Y + 0.6
    add_text(f"Patient{i}_texte_malade", "à soigner", (px - PAIR, LABEL_Y), 0.4, MAT_TEXTE_2, col_textes)
    add_text(f"Patient{i}_texte_sain", "sain", (px + PAIR, LABEL_Y), 0.4, MAT_TEXTE_2, col_textes)

centre_x = (patients_x[0] + patients_x[-1]) / 2
add_text("Légende",
         "gris : pièce à soigner   ·   orange : pièce saine, pour comparer   ·   gris foncé : repère fixe",
         (centre_x, -5.4), 0.5, MAT_TEXTE_2, col_textes)


# --------------------------------------------------------------------------
# LISEZ-MOI
# --------------------------------------------------------------------------
LISEZ_MOI = """LISEZ-MOI : survolez cette zone et appuyez sur Ctrl + Espace pour l'agrandir (même raccourci pour revenir).
Pour retrouver la Timeline ici : sélecteur de type d'éditeur, en haut à gauche de cette zone.

LA CLINIQUE DU FICHIER
PRC02 Design et visualisation temps réel avec Blender, initiation, demi-journée 2. Blender 5.2 LTS.

Un collègue vous confie cinq pièces d'une maquette. Chacune présente un défaut. Diagnostiquez, puis soignez.
Chaque collection contient un patient : la pièce à soigner, en gris, et la même pièce saine, en orange, pour comparer. Les éléments gris foncé sont des repères fixes : ils ne se sélectionnent pas.
Lisez le symptôme, cherchez la cause, puis soignez la pièce grise. L'indice vous met sur la piste. Les solutions sont à la fin de ce texte : cherchez d'abord.

AVANT DE COMMENCER
- Cliquez la pièce grise, puis . (pavé numérique) pour la cadrer.
- / (pavé numérique) isole la sélection ; la même touche ramène toute la scène.
- Une erreur ? Ctrl + Z.

PATIENT 1 - LE CARÉNAGE CABOSSÉ
SYMPTÔME : le carénage devrait être lisse et bombé. Pourtant, son flanc avant paraît enfoncé, avec des bords en escalier.
MISSION : rendez au carénage son aspect lisse, sans modifier sa forme.
INDICE : tournez autour du carénage : le creux est-il réel ? Puis, en haut à droite de la vue 3D, ouvrez le menu Overlays (la petite flèche à droite des deux cercles) et cochez Face Orientation. Que signale le rouge ? Décochez ensuite Face Orientation.

PATIENT 2 - L'ACCOUDOIR DÉFORMÉ
SYMPTÔME : les arrondis de l'accoudoir sont irréguliers : très étirés aux extrémités, presque vifs sur les côtés.
MISSION : obtenez des arrondis réguliers, comme sur la pièce saine, sans toucher au modificateur Bevel.
INDICE : appuyez sur N, onglet Item. Comparez la ligne Scale de l'accoudoir et celle de la pièce saine.

PATIENT 3 - LE BOUTON QUI NE S'ARRONDIT PAS
SYMPTÔME : la pièce saine est arrondie partout. Le bouton à soigner garde un dessus plat, bordé d'une arête vive.
MISSION : rendez au bouton son arrondi.
INDICE : passez en Mode Édition (Tab) et cochez Statistics dans le menu Overlays. Combien de sommets (Vertices) ? Un pavé en a 8.

PATIENT 4 - LES HUBLOTS JUMEAUX
SYMPTÔME : modifiez un hublot en Mode Édition : l'autre change aussi.
MISSION : étirez le hublot de droite de 50 % en hauteur, sans changer celui de gauche. Travaillez en Mode Édition, pour garder une échelle à 1 (voir le patient 2) : Tab, A, S, Z, 1.5, Entrée.
INDICE : sélectionnez un hublot. Dans l'éditeur de propriétés, onglet Object Data (le triangle vert), regardez le chiffre à droite du nom du maillage.

PATIENT 5 - LA PORTE QUI TOURNE MAL
SYMPTÔME : R, Z, 90, Entrée devrait ouvrir la porte sur ses charnières. Elle tourne sur elle-même, au milieu de l'ouverture. Ctrl + Z pour la remettre en place.
MISSION : ouvrez la porte de 90°, en la faisant pivoter sur ses charnières.
INDICE : un objet tourne autour de son origine, le petit point orange visible quand il est sélectionné. Où est-il sur la porte ?

SOLUTIONS (à lire après avoir cherché)

PATIENT 1 : la forme n'est pas creuse. Une partie des faces a sa normale inversée : elle pointe vers l'intérieur, et la vue l'éclaire à l'envers. Face Orientation affiche ces faces en rouge.
Soin : sélectionnez le carénage, Tab, A pour tout sélectionner, puis Maj + N (Recalculate Outside). Tab pour revenir : le flanc redevient lisse.

PATIENT 2 : l'échelle de l'accoudoir n'est pas appliquée : Scale vaut 2,4 ; 0,5 ; 0,4. Le Bevel calcule sa largeur avant l'échelle, qui l'étire en longueur et l'écrase sur les côtés.
Soin : en Mode Objet, Ctrl + A > Scale. Scale revient à 1,000 et les arrondis deviennent réguliers.

PATIENT 3 : une extrusion a été annulée avec Échap. Les nouveaux sommets sont restés exactement sur les anciens : 12 sommets au lieu de 8. Ces faces de hauteur nulle empêchent la Subdivision Surface d'arrondir le bord.
Soin : Tab, A, puis M > By Distance. Blender fusionne les 4 sommets en double. Tab pour revenir : le bouton est arrondi.
À retenir : pour annuler une extrusion, Ctrl + Z, pas Échap.

PATIENT 4 : les deux hublots sont des copies liées (Alt + D). Ils partagent le même maillage, Hublot : le chiffre 2 l'indique.
Soin : Ctrl + Z si vous avez déjà étiré les deux. Sélectionnez le hublot de droite. Dans l'onglet Object Data, cliquez sur le chiffre 2 : le hublot reçoit sa propre copie du maillage. Puis Tab, A, S, Z, 1.5, Entrée : seul le hublot de droite s'étire.

PATIENT 5 : l'origine de la porte est en son centre. Une rotation se fait autour de l'origine.
Soin : sélectionnez la porte, Tab, puis 2 pour la sélection par arêtes. Cliquez l'arête verticale avant de la porte, côté charnières. Maj + S > Cursor to Selected : le curseur 3D s'y place. Tab, puis menu Object > Set Origin > Origin to 3D Cursor. Enfin, R, Z, 90, Entrée : la porte s'ouvre sur ses charnières.
Maj + C ramène ensuite le curseur 3D au centre du monde (et recadre la vue).
"""

txt = bpy.data.texts.new("LISEZ-MOI")
txt.write(LISEZ_MOI)
txt.cursor_set(0)


# --------------------------------------------------------------------------
# Interface : Text Editor à la place de la Timeline, vue 3D en Solid
# --------------------------------------------------------------------------
scene.display.shading.light = 'STUDIO'
scene.display.shading.color_type = 'MATERIAL'
scene.display.shading.show_object_outline = True

for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'FILE_BROWSER':
            params = area.spaces.active.params
            if params is not None:
                params.directory = b"//"

layout = bpy.data.screens["Layout"]
for area in layout.areas:
    if area.type == 'DOPESHEET_EDITOR' or (area.type == 'TIMELINE'):
        area.type = 'TEXT_EDITOR'
        space = area.spaces.active
        space.text = txt
        space.show_word_wrap = True
        space.show_line_numbers = False
        space.show_syntax_highlight = False
        space.top = 0
    elif area.type == 'VIEW_3D':
        space = area.spaces.active
        space.shading.type = 'SOLID'
        space.shading.light = 'STUDIO'
        space.shading.color_type = 'MATERIAL'
        space.shading.show_object_outline = True
        r3d = space.region_3d
        r3d.view_perspective = 'PERSP'
        r3d.view_location = (centre_x, -1.0, 0.0)
        r3d.view_rotation = Matrix.Rotation(math.radians(50), 3, 'X').to_quaternion()
        r3d.view_distance = 30.0

for ob in bpy.data.objects:
    ob.select_set(False)
bpy.context.view_layer.objects.active = None

bpy.context.preferences.filepaths.save_version = 0      # pas de copie .blend1
bpy.ops.wm.save_as_mainfile(filepath=OUTPUT, compress=True, relative_remap=True)
print("ENREGISTRÉ", OUTPUT, os.path.getsize(OUTPUT))
