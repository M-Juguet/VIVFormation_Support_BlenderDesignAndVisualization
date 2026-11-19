# Construit les deux fichiers du chapitre 4 (plan : _resources/plans/PRC02-plan-chap4.md) :
#   - _resources/exercices/PRC02_ch4_lampe_en_studio.blend : le fichier de secours, le studio avec les
#     collections Lampe (coloris A) et Lampe_coloris_B de la lampe habillée du chapitre 3 (fiche A2) ;
#   - _resources/exercices/PRC02_ch4_studio.blend : le même studio, sans la lampe, où l'apprenant
#     amène la sienne par File > Append.
# Les corrigés sont dans trois collections masquées : « Corrigé éclairage », « Corrigé caméras » et
# « Corrigé paliers ». Les réglages de rendu et le monde attendus sont dans les lignes « Corrigé » du
# LISEZ-MOI.
#
# La lampe est lue dans _resources/exercices/PRC02_ch3_lampe_habillage.zip, décompressé dans
# tool/exercices_ch4/_construction/, sans modifier le zip. Les HDRI de Poly Haven sont lues dans
# tool/exercices_ch4/hdri/ ; studio.exr vient de l'installation de Blender. Toutes sont empaquetées.
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 -Script tool\exercices_ch4\build_studio.py

import math
import os
import sys

import bpy
import bmesh
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commun as C   # noqa: E402

ROT_INTERIEUR = 135      # rotation Z (degrés) du Mapping de Monde_Interieur, donnée par la ligne « Corrigé » de l'HDRI

AUTEURS_HDRI = "studio.exr (fournie avec Blender), artist_workshop (Oliksiy Yakovlyev) et docklands_01 (Savva Zakharov), Poly Haven, licence CC0"

LISEZ_MOI = """PRC02 · Chapitre 4 · Mettre en scène et exporter
Blender 5.2 LTS. Corrigés : collections « Corrigé éclairage », « Corrigé caméras » et « Corrigé paliers », œil fermé dans l'Outliner. Pour en voir une au rendu, ouvrez son œil et son appareil photo.

DÉMARRER
{demarrer}

1 · PARAMÉTRER EEVEE (caméra CAM_banc_essai)
- Z : passez de Material Preview à Rendered. En Material Preview, cochez puis décochez Scene World (menu Viewport Shading).
- F12 : un rendu dans l'emplacement 1 (menu Slot de la fenêtre de rendu), Raytracing décoché.
- Onglet Render : cochez Raytracing, la case du chapitre 3 que ce fichier n'a pas. Emplacement 2, puis F12. Comparez avec J : le chrome, la laque, le verre.
- Render > Samples : 128. F12. Notez les deux temps de rendu.
- Color Management > View : AgX, Standard, Khronos PBR Neutral. Regardez le nuancier.
Seul : gardez Raytracing, un nombre d'échantillons adapté à votre poste et une transformation de vue. Ctrl + S.
Corrigé : Raytracing coché, Render > Samples 128, View Khronos PBR Neutral.

2 · ÉCLAIRER PAR HDRI
- Onglet World : choisissez Monde_Studio, Monde_Interieur, puis Monde_Exterieur. Un F12 dans un emplacement différent pour chacun.
- Rotation Z du Mapping : placez le reflet principal sur la tête.
Seul : choisissez l'ambiance de votre vue de situation.
Corrigé : Monde_Interieur, rotation Z du Mapping {rot} °.

3 · ÉCLAIRER EN STUDIO
- Onglet World : Monde_Neutre.
- Add > Light > Area. Nommez-la Key. À 45°, au-dessus et sur le côté, tournée vers la lampe. Cochez Temperature pour régler les kelvins.
- Fill : du côté opposé, un tiers de la puissance de Key, plus grande.
- Rim : derrière et au-dessus, jusqu'au liseré clair sur la tête.
- M > New Collection : Eclairage_studio.
- Allumez-les une à une avec l'œil, puis les trois.
Seul : Monde_Studio à Strength 0,3, lumières allumées. Gardez la combinaison que vous préférez.
★ Une Area Rectangle longue : une ligne de reflet sur la tête. Key à 4500 K, Rim à 7000 K.
Corrigé : collection « Corrigé éclairage », avec Monde_Neutre.

4 · CAMÉRA ET EXPORT
- Add > Camera. View > Cameras > Align Active Camera to View (Ctrl + Alt + 0 du pavé). Nommez-la CAM_heros.
- Focal Length : 85mm. N > View > Lock Camera to View : cadrez en naviguant, puis décochez.
- Viewport Display > Composition Guides > Thirds.
- CAM_detail : 100mm, sur un détail (interrupteur et grille, articulation ou ampoule). Un Empty Mise_au_point sur ce détail. Depth of Field : Focus Object, F-Stop entre 5,6 et 8.
- Masquez la collection Nuancier (œil et appareil photo). CAM_heros active (Ctrl + 0 du pavé). Format 1920 × 1080. F12.
- Image > Save As : rendus/lampe_heros_<initiales>_v001.png, PNG, Color Management sur Follow Scene.
Seul : CAM_detail active, résolution 1080 × 1080, F12, rendus/lampe_detail_<initiales>_v001.png.
Corrigé : collection « Corrigé caméras » ; images PRC02_ch4_corrige_heros.png et PRC02_ch4_corrige_detail.png.

ATELIER · LE CONCEPT FINAL
Revue de design demain matin : présentez votre lampe en trois visuels.
- V1 Héros, CAM_heros, 1920 × 1080 : lampe_heros_<initiales>_v001.png
- V2 Détail, CAM_detail, 1080 × 1080 : lampe_detail_<initiales>_v001.png
- V3 Situation, CAM_situation, 1920 × 1080 : lampe_situation_<initiales>_v001.png (Mise_en_situation visible, Studio masqué, une HDRI)
- File > External Data > Pack Resources, puis Ctrl + S.
- Copiez les trois PNG dans le dossier de la galerie.
Socle : les trois vues et le fichier empaqueté.
★  Une vue héros à fond transparent (Film > Transparent, RGBA).
★  Une vue technique de profil : caméra Orthographic, Monde_Neutre.
★  La gamme : File > Append, collection Lampe_coloris_B de lampe_habillage_v002.blend (fichier de secours : ouvrez son œil et son appareil photo). Une caméra CAM_gamme cadre les deux lampes : lampe_gamme_<initiales>_v001.png
★★ La lampe allumée : un Spot dans la tête, Temperature 2700 K, Eclairage_studio éteint. Sur l'ampoule, la matière Ampoule_allumee, dans la liste des matières.
★★ Le même studio pour un autre objet.
Avant d'envoyer : nuancier masqué (œil et appareil photo), bonne résolution pour chaque vue, noms vérifiés.
Corrigé : CAM_situation_corrige (« Corrigé caméras ») et « Corrigé paliers » ; images PRC02_ch4_corrige_*.png.

POUR ALLER PLUS LOIN (notions nouvelles)
- Spot : rubrique Beam Shape, Angle et Blend.
- Votre propre ampoule allumée : rubrique Emission de la matière.
- L'éclat de l'ampoule : nœud Glare, type Bloom, dans le compositeur.
- Toutes les vues d'un coup : un marqueur par caméra, Marker > Bind Camera to Markers, chemin de sortie, Render > Render Animation.
- Des lumières qui suivent la lampe : contrainte Damped Track.

PERDU EN COURS DE ROUTE ?
Ouvrez PRC02_ch4_lampe_en_studio.blend, enregistrez-le sous lampe_rendu_v001.blend, puis suivez les lignes « Corrigé ».

HDRI : {hdri}.
"""

DEMARRER_STUDIO = """- Votre lampe du chapitre 3 : File > Append, lampe_habillage_v002.blend, dossier Collection, collection Lampe.
- Vous avez fait le défi procédural à la place de l'atelier ? Même geste avec votre lampe, gardée dans la collection Lampe, ou avec la lampe habillée du chapitre 3 (PRC02_ch3_lampe_habillage.zip). Sinon, ouvrez PRC02_ch4_lampe_en_studio.blend.
- Puis File > Save As : lampe_rendu_v001.blend.
- L'ampoule ne laisse plus voir le fond de la tête : c'est normal, la section 1 explique pourquoi.
Corrigé : PRC02_ch4_lampe_en_studio.blend montre la lampe en place."""

DEMARRER_SECOURS = """- La lampe habillée du chapitre 3 est déjà là. Son coloris B attend, masqué, dans la collection Lampe_coloris_B.
- File > Save As : lampe_rendu_v001.blend.
- L'ampoule ne laisse plus voir le fond de la tête : c'est normal, la section 1 explique pourquoi."""

STUDIO_MATS = {"Fond_studio", "CMF_rouge", "CMF_bleu", "CMF_blanc", "Ref_chrome", "Ref_gris_18", "Bois_clair",
               "Papier", "Ampoule_allumee"}

LAMPE_A = ["Socle", "Grille_aeration", "Grille_pivot", "Interrupteur", "Interrupteur_crans", "Interrupteur_pivot",
           "Articulation_bas", "Articulation_milieu", "Articulation_haut", "Bras_bas", "Bras_haut", "Tête",
           "Douille", "Ampoule", "Câble"]


# ---------------------------------------------------------------------------- géométrie
def mesh_object(name, col, verts, faces, smooth=False):
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    for p in me.polygons:
        p.use_smooth = smooth
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    return ob


def fond_cyclo(col, mat):
    """Sol, raccord en quart de cercle et mur, d'une seule pièce, extrudés sur X de -1,9 à 2,1."""
    prof = [(-1.4, 0.0), (0.45, 0.0)]
    for i in range(17):
        t = math.radians(90 * i / 16)
        prof.append((0.5 + 0.4 * math.sin(t), 0.4 - 0.4 * math.cos(t)))
    prof += [(0.9, 0.45), (0.9, 1.6)]
    verts = [(x, y, z) for (y, z) in prof for x in (-1.9, 2.1)]
    faces = [(2 * i, 2 * i + 1, 2 * i + 3, 2 * i + 2) for i in range(len(prof) - 1)]
    ob = mesh_object("Fond_cyclo", col, verts, faces, smooth=True)
    ob.data.materials.append(mat)
    return ob


def box(name, col, size, center, rot_z=0.0):
    sx, sy, sz = (s / 2 for s in size)
    verts = [(x, y, z) for x in (-sx, sx) for y in (-sy, sy) for z in (-sz, sz)]
    faces = [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)]
    ob = mesh_object(name, col, verts, faces)
    ob.location = center
    ob.rotation_euler = (0, 0, math.radians(rot_z))
    return ob


def sphere(name, col, loc, r, mat):
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=r)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    while me.uv_layers:
        me.uv_layers.remove(me.uv_layers[0])
    ob = bpy.data.objects.new(name, me)
    col.objects.link(ob)
    ob.location = loc
    ob.data.materials.append(mat)
    return ob


# ---------------------------------------------------------------------------- lumières et caméras
def area_light(name, col, loc, target, size, power, kelvin, shape='SQUARE', size_y=None):
    li = bpy.data.lights.new(name, 'AREA')
    li.shape = shape
    li.size = size
    if size_y is not None:
        li.size_y = size_y
    li.energy = power
    li.use_temperature = True
    li.temperature = kelvin
    ob = bpy.data.objects.new(name, li)
    col.objects.link(ob)
    ob.location = loc
    if target is not None:
        C.aim(ob, target)
    return ob


def camera(name, col, loc, target, lens, ortho=None, rot=None):
    cd = bpy.data.cameras.new(name)
    cd.lens = lens
    if ortho:
        cd.type = 'ORTHO'
        cd.ortho_scale = ortho
    ob = bpy.data.objects.new(name, cd)
    col.objects.link(ob)
    ob.location = loc
    if target is not None:
        C.aim(ob, target)
    if rot is not None:
        ob.rotation_euler = [math.radians(a) for a in rot]
    return ob


# ---------------------------------------------------------------------------- mondes
def world_hdri(name, path, rel, strength=1.0):
    w = bpy.data.worlds.new(name)
    w.use_nodes = True
    nt = w.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputWorld")
    out.location = (300, 0)
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.location = (100, 0)
    bg.inputs["Strength"].default_value = strength
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    env.location = (-200, 0)
    env.image = C.pack_image(path, rel)
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.location = (-400, 0)
    mp.vector_type = 'POINT'
    tc = nt.nodes.new("ShaderNodeTexCoord")
    tc.location = (-600, 0)
    nt.links.new(tc.outputs["Generated"], mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"], env.inputs["Vector"])
    nt.links.new(env.outputs["Color"], bg.inputs["Color"])
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    w.use_fake_user = True
    return w


def world_neutre():
    w = bpy.data.worlds.new("Monde_Neutre")
    w.use_nodes = True
    bg = next(n for n in w.node_tree.nodes if n.type == 'BACKGROUND')
    bg.inputs["Color"].default_value = (0.03, 0.03, 0.03, 1.0)
    bg.inputs["Strength"].default_value = 1.0
    w.color = (0.03, 0.03, 0.03)
    w.use_fake_user = True
    return w


# ---------------------------------------------------------------------------- la bande de reflet
def place_strip(strip, cam, tete_name="Tête", dist=0.6):
    """Place la bande lumineuse pour que son reflet passe sur la tête laquée, vue depuis cam :
    la face de la tête la mieux tournée renvoie le regard de la caméra vers le haut, à 45° environ."""
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    tete = bpy.data.objects[tete_name].evaluated_get(dg)
    me = tete.to_mesh()
    mw = tete.matrix_world
    nmat = mw.to_3x3().inverted().transposed()
    eye = cam.matrix_world.translation
    sc = bpy.context.scene
    best = None
    for p in me.polygons:
        c = mw @ p.center
        n = (nmat @ p.normal).normalized()
        d = (c - eye).normalized()
        if n.dot(-d) < 0.35:
            continue
        hit, loc, _nrm, _i, obj, _m = sc.ray_cast(dg, eye, d)
        if not hit or obj.name != tete_name or (loc - c).length > 0.004:
            continue
        r = d - 2 * d.dot(n) * n
        score = abs(r.z - 0.7)
        if best is None or score < best[0]:
            best = (score, c, r)
    tete.to_mesh_clear()
    assert best is not None
    _s, c, r = best
    axis = Vector((-0.5, 0.0, 0.866))             # axe de la tête (rotation Y -30°)
    x = (axis - axis.dot(r) * r).normalized()     # la longueur de la bande suit l'axe de la tête
    z = r.normalized()                            # la face émettrice (-Z) regarde la tête
    y = z.cross(x)
    m = Matrix((x, y, z)).transposed().to_4x4()
    m.translation = c + dist * r
    strip.matrix_world = m
    bpy.context.view_layer.update()
    corners = [strip.matrix_world @ Vector((sx * 0.5, sy * 0.03, 0)) for sx in (-1, 1) for sy in (-1, 1)]
    proj = [tuple(round(v, 2) for v in world_to_camera_view(sc, cam, p)[:2]) for p in corners]
    print("BANDE", tuple(round(v, 3) for v in m.translation), "reflet en", tuple(round(v, 3) for v in c),
          "coins dans CAM_heros :", proj)


# ---------------------------------------------------------------------------- le studio
def build():
    sc = C.reset_scene()
    root = sc.collection
    studio = C.new_collection("Studio", root)
    nuancier = C.new_collection("Nuancier", root)
    situ = C.new_collection("Mise_en_situation", root)
    c_ecl = C.new_collection("Corrigé éclairage", root)
    c_cam = C.new_collection("Corrigé caméras", root)
    c_pal = C.new_collection("Corrigé paliers", root)

    fond, _ = C.material("Fond_studio", "C8C8C8", 0.7)
    fond_cyclo(studio, fond)
    banc = camera("CAM_banc_essai", studio, (0.55, -2.30, 0.55), (0.22, -0.03, 0.18), 60)
    sc.camera = banc

    for (name, mname, col, rough, metal, x) in (
            ("Nuancier_rouge", "CMF_rouge", "C8102E", 0.35, 0.0, 0.45),
            ("Nuancier_bleu", "CMF_bleu", "0057B8", 0.35, 0.0, 0.53),
            ("Nuancier_blanc", "CMF_blanc", "F2F2F2", 0.35, 0.0, 0.61),
            ("Ref_chrome", "Ref_chrome", "E0E0E0", 0.03, 1.0, 0.69),
            ("Ref_gris", "Ref_gris_18", "767676", 0.5, 0.0, 0.77)):
        m, _ = C.material(mname, col, rough, metal)
        sphere(name, nuancier, (x, -0.15, 0.03), 0.03, m)

    bois, _ = C.material("Bois_clair", "B89268", 0.45)
    pl = box("Plateau_bureau", situ, (1.4, 0.8, 0.03), (0.10, 0.0, -0.015))
    pl.data.materials.append(bois)
    papier, _ = C.material("Papier", "E9E4D8", 0.8)
    ca = box("Carnet", situ, (0.21, 0.148, 0.012), (0.24, -0.14, 0.006), rot_z=-15)
    ca.data.materials.append(papier)

    # matière fournie pour le palier ★★ : l'ampoule allumée, sans objet, gardée par un Fake User
    m, p = C.material("Ampoule_allumee", "FFF4E0", 0.4)
    p.inputs["Emission Color"].default_value = C.lin("FFA957")
    p.inputs["Emission Strength"].default_value = 10.0
    m.use_fake_user = True

    # « Corrigé éclairage » : le studio en trois points et la bande de reflet
    area_light("Key_corrige", c_ecl, (-0.60, -0.90, 0.90), C.T, 0.5, 20, 5500)
    area_light("Fill_corrige", c_ecl, (1.00, -0.60, 0.45), C.T, 0.8, 5, 6000)
    area_light("Rim_corrige", c_ecl, (0.30, 0.80, 0.90), (0.23, 0.0, 0.38), 0.3, 15, 6500)
    strip = area_light("Reflet_bande_corrige", c_ecl, (0.15, -0.35, 0.95), None, 1.0, 10, 6500,
                       shape='RECTANGLE', size_y=0.06)

    # « Corrigé caméras » : les trois vues de l'atelier
    heros = camera("CAM_heros_corrige", c_cam, (1.60, -2.10, 0.65), C.T, 85)
    heros.data.show_composition_thirds = True
    mp = bpy.data.objects.new("Mise_au_point_corrige", None)
    mp.empty_display_type = 'PLAIN_AXES'
    mp.empty_display_size = 0.02
    c_cam.objects.link(mp)
    mp.location = (0.055, 0.0, 0.031)
    det = camera("CAM_detail_corrige", c_cam, (0.33, -0.22, 0.20), (0.035, -0.01, 0.03), 100)
    det.data.dof.use_dof = True
    det.data.dof.focus_object = mp
    det.data.dof.aperture_fstop = 8.0
    camera("CAM_situation_corrige", c_cam, (-0.30, -0.85, 0.45), (0.0, 0.0, 0.21), 35)

    # « Corrigé paliers » : la lampe allumée, la gamme, la vue technique
    sp = bpy.data.lights.new("Spot_lampe_corrige", 'SPOT')
    sp.spot_size = math.radians(70)
    sp.spot_blend = 0.3
    sp.energy = 12
    sp.use_temperature = True
    sp.temperature = 2700
    sp.shadow_soft_size = 0.0
    so = bpy.data.objects.new("Spot_lampe_corrige", sp)
    c_pal.objects.link(so)
    so.location = (0.254, 0.0, 0.338)
    so.rotation_euler = (0.0, math.radians(-30), 0.0)
    camera("CAM_gamme_corrige", c_pal, (0.85, -3.00, 0.70), (0.37, 0.0, 0.20), 70)
    camera("CAM_profil_ortho_corrige", c_pal, (-0.01, -2.00, 0.40), None, 50, ortho=0.95, rot=(85, 0, 0))

    # les quatre mondes
    w_studio = world_hdri("Monde_Studio", os.path.join(C.STUDIOLIGHTS, "studio.exr"), "hdri/studio.exr")
    world_hdri("Monde_Interieur", os.path.join(C.HDRI_DIR, "artist_workshop_2k.hdr"), "hdri/artist_workshop_2k.hdr")
    world_hdri("Monde_Exterieur", os.path.join(C.HDRI_DIR, "docklands_01_2k.hdr"), "hdri/docklands_01_2k.hdr")
    world_neutre()
    sc.world = w_studio

    # la lampe du chapitre 3, pour le fichier de secours (et pour placer la bande de reflet)
    with bpy.data.libraries.load(C.extract_a2(), link=False) as (src, dst):
        assert "Lampe" in src.collections and "Lampe_coloris_B" in src.collections, src.collections
        dst.collections = ["Lampe", "Lampe_coloris_B"]
    for col in dst.collections:
        root.children.link(col)
    # les matières de la lampe sont des actifs (chapitre 3) ; la copie qui retire la référence faible
    # perd ce statut : on le relève avant, puis on le rend aux copies, comme le ferait File > Append
    actifs = {}
    for m in bpy.data.materials:
        ad = m.asset_data
        if ad is not None:
            actifs[m.name] = (ad.description, ad.author, ad.license, ad.catalog_id, [t.name for t in ad.tags])
    C.drop_weak_references()
    for name, (desc, author, lic, cat, tags) in actifs.items():
        m = bpy.data.materials[name]
        if m.asset_data is None:
            m.asset_mark()
        ad = m.asset_data
        ad.description, ad.author, ad.license, ad.catalog_id = desc, author, lic, cat
        for t in tags:
            if t not in ad.tags:
                ad.tags.new(t)
    for im in bpy.data.images:             # l'image de finition, lue dans A2, garde un chemin absolu
        if im.type == 'IMAGE' and not im.filepath.startswith("//"):
            C.set_relative_path(im, "textures_cmf/" + os.path.basename(im.filepath))
    for name in ("Mise_en_situation", "Corrigé éclairage", "Corrigé caméras", "Corrigé paliers"):
        c = bpy.data.collections[name]          # après Lampe dans l'Outliner
        root.children.unlink(c)
        root.children.link(c)
    lampe = bpy.data.collections["Lampe"]
    names = sorted(o.name for o in lampe.objects)
    assert names == sorted(LAMPE_A), names
    names_b = sorted(o.name for o in bpy.data.collections["Lampe_coloris_B"].objects)
    assert names_b == sorted(n + ".001" for n in LAMPE_A), names_b
    place_strip(strip, heros)

    for name in ("Mise_en_situation", "Corrigé éclairage", "Corrigé caméras", "Corrigé paliers", "Lampe_coloris_B"):
        C.hide_collection(name)
    for me in bpy.data.meshes:
        while me.uv_layers:
            me.uv_layers.remove(me.uv_layers[0])

    # 1. le fichier de secours
    txt = C.text_block(LISEZ_MOI.format(demarrer=DEMARRER_SECOURS, rot=ROT_INTERIEUR, hdri=AUTEURS_HDRI))
    C.setup_layout(txt, eye=(0.55, -2.30, 0.55), target=(0.22, -0.03, 0.18), distance_k=0.62)
    C.deselect_all()
    C.finalize(C.SECOURS, groups_expected=["Smooth by Angle"])

    # 2. le studio : la même scène, sans la lampe
    for cname in ("Lampe", "Lampe_coloris_B"):
        c = bpy.data.collections[cname]
        for o in list(c.objects):
            bpy.data.objects.remove(o)
        bpy.data.collections.remove(c)
    for m in list(bpy.data.materials):         # les matières de la lampe sont des actifs : Fake User
        if m.name not in STUDIO_MATS:
            bpy.data.materials.remove(m)
    for im in list(bpy.data.images):
        if im.name == "grain_structure.png":
            bpy.data.images.remove(im)
    txt.clear()
    txt.write(LISEZ_MOI.format(demarrer=DEMARRER_STUDIO, rot=ROT_INTERIEUR, hdri=AUTEURS_HDRI))
    txt.cursor_set(0)
    C.finalize(C.STUDIO, groups_expected=[])
    print("MATIERES", sorted(m.name for m in bpy.data.materials))
    print("MONDES", sorted((w.name, w.use_fake_user) for w in bpy.data.worlds))


if __name__ == "__main__":
    build()
