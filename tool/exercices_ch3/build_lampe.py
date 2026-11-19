# Construit les fichiers de la lampe du chapitre 3 (plan : _resources/plans/PRC02-plan-chap3.md) :
#   - fiche A : _resources/exercices/PRC02_ch3_lampe_a_habiller.blend, le fichier de travail de secours :
#     la lampe du chapitre 2 sans matière, et les corrigés masqués « Corrigé coloris A » (X + 0,75 m)
#     et « Corrigé coloris B » (X + 1,50 m), objets suffixés _A et _B, matières suffixées _corrige ;
#   - fiche A2 : tool/exercices_ch3/_construction/PRC02_ch3_lampe_habillage/PRC02_ch3_lampe_habillage.blend
#     et son blender_assets.cats.txt : l'état attendu de lampe_habillage_v002.blend, sous les vrais noms
#     (livrés en zip par livrer.py). Source du fichier de secours du chapitre 4 et du défi procédural.
#
# Usage, depuis la racine du dépôt (la bibliothèque, fiche B, doit être construite avant A2) :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 `
#       -Script tool\exercices_ch3\build_lampe.py [-- a|a2]
# La lampe est lue dans _resources/exercices/PRC02_ch2_lampe_modele.blend, sans modifier ce fichier.

import os
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import commun as C   # noqa: E402
import matieres as M   # noqa: E402

OUT_A = os.path.join(C.EX, "PRC02_ch3_lampe_a_habiller.blend")
OUT_A2 = os.path.join(C.LAMPE_DIR, "PRC02_ch3_lampe_habillage.blend")

# pièce -> matière, pour chaque coloris
COLORIS_A = {
    "Socle": "Structure_Vert", "Tête": "Peinture_Vert", "Grille_aeration": "ABS_Noir", "Interrupteur": "ABS_Noir",
    "Interrupteur_crans": "ABS_Noir", "Bras_bas": "Alu_Brosse", "Bras_haut": "Alu_Brosse",
    "Articulation_bas": "Chrome", "Articulation_milieu": "Chrome", "Articulation_haut": "Chrome",
    "Câble": "PVC_Mat_Noir", "Ampoule": "Verre_Clair", "Douille": "Alu_Naturel",
}
COLORIS_B = dict(COLORIS_A, **{
    "Socle": "Structure_Blanche", "Tête": "Laque_Blanche", "Bras_bas": "Alu_Anodise_Noir", "Bras_haut": "Alu_Anodise_Noir",
    "Articulation_bas": "Laiton", "Articulation_milieu": "Laiton", "Articulation_haut": "Laiton",
    "Douille": "Laiton", "Ampoule": "Verre_Depoli",
})

LISEZ_MOI_A = """PRC02 · Chapitre 3 · Habiller la lampe
Enregistrez ce fichier sous lampe_habillage_v001.blend.
Corrigés : collections « Corrigé coloris A » (sections 1 à 3) et « Corrigé coloris B » (atelier), œil fermé dans l'Outliner.
Leurs matières portent le suffixe _corrige. Valeurs indicatives : composez votre propre gamme.

SECTION 1 · Les matières (onglet Material, vue Material Preview)
Socle
- Socle et tête : une peinture partagée. Interrupteur, ses crans et la grille : ABS noir partagé.
- Bras : aluminium, Metallic 1, Roughness 0,3. Articulations : chrome, Metallic 1, Roughness 0,03.
- Câble : PVC noir, Roughness 0,7.
- Ampoule : Transmission > Weight 1, Roughness 0, Thin Wall coché.
  Onglet Render > Raytracing ; onglet Material > Settings > Raytraced Transmission.
★  Coat > Weight 1 sur la peinture : une laque. Un verre dépoli : Roughness 0,4.
★★ Intérieur blanc de la tête : un second emplacement de matière, puis Solidify > Materials > Material Offset 1.

SECTION 2 · Les finitions (espace Shading)
Socle
- Bras brossés : Texture Coordinate (Object) > Mapping (Scale Z 0,02) > Noise Texture (Scale 1000)
  > Bump (Strength 0,15) > Normal du Principled.
- Socle : rendez sa matière indépendante (compteur), Coat 0, Roughness 0,6.
  Image Texture : textures_cmf/grain_structure.png, Non-Color, Box, Blend 0,25.
  Mapping Scale 50, Bump Strength 0,2.
- File > External Data > Pack Resources, puis enregistrez.
★  ABS grainé : Noise Scale 1500, Bump Strength 0,05.
★★ Articulations microbillées : Noise Scale 2000, Bump Strength 0,03, Roughness 0,5.

SECTION 3 · La bibliothèque
Socle
- Mark as Asset sur toutes vos matières ; catalogues Métaux, Plastiques et peintures, Verres.
- Glissez la vignette de Chrome sur la douille.
- File > Append > PRC02_bibliotheque_CMF > PRC02_ch3_nuancier_cmf.blend > Material > Alu_Naturel,
  puis glissez-la sur la douille.
- Gardez le fichier blender_assets.cats.txt à côté de votre fichier : il contient vos catalogues.
- Corrigé du rangement : la bibliothèque PRC02_bibliotheque_CMF elle-même.
★  Une description et des étiquettes pour chaque actif.
   File > Link d'une matière du nuancier : elle arrive grisée, en lecture seule. Puis Ctrl + Z.
★★ Edit > Preferences > Asset Libraries > + : déclarez PRC02_bibliotheque_CMF,
   puis glissez une vignette de la bibliothèque sur une pièce.

ATELIER · Le coloris B
Socle
- Duplicate Collection sur Lampe ; renommez la copie Lampe_coloris_B ; G X = 750mm.
- Changez au moins quatre matières, dont une peinture et un métal :
  rendez-les d'abord indépendantes (compteur), puis renommez-les.
- Le coloris A ne doit pas bouger.
★  Une gamme complète, rangée en actifs ; une matière récupérée du nuancier par File > Append.
★★ Un coloris C premium : laiton, carbone, verre fumé.
Enregistrez sous lampe_habillage_v002.blend (bouton +).
"""

LISEZ_MOI_A2 = """PRC02 · Chapitre 3 · La lampe habillée
Le résultat attendu en fin de chapitre (lampe_habillage_v002.blend) : coloris A dans la collection Lampe, coloris B dans Lampe_coloris_B.
Les matières sont des actifs, rangés dans les catalogues Métaux, Plastiques et peintures et Verres (Asset Browser > Current File).
Gardez le fichier blender_assets.cats.txt à côté de ce fichier : il contient les catalogues.
Pour repartir de ce fichier : File > Save As, sous lampe_habillage_v002.blend.
"""


def load_lampe():
    """La collection Lampe du chapitre 2, sans référence faible ni couche UV."""
    with bpy.data.libraries.load(C.SRC_CH2, link=False) as (src, dst):
        assert "Lampe" in src.collections, src.collections
        dst.collections = ["Lampe"]
    col = dst.collections[0]
    bpy.context.scene.collection.children.link(col)
    C.drop_weak_references()
    for coll in (bpy.data.collections,):
        for idb in list(coll):
            if idb.library_weak_reference:
                name = idb.name
                cp = idb.copy()
                idb.user_remap(cp)
                coll.remove(idb)
                cp.name = name
    col = bpy.data.collections["Lampe"]
    for me in bpy.data.meshes:                     # aucune pièce n'a de dépliage UV
        while me.uv_layers:
            me.uv_layers.remove(me.uv_layers[0])
    objs = list(col.objects)
    names = sorted(o.name for o in objs)
    want = sorted(list(COLORIS_A) + ["Grille_pivot", "Interrupteur_pivot"])
    assert names == want, names
    return col, objs


def dress(mapping, objs, mats, strip=""):
    for o in objs:
        if o.type == 'EMPTY':
            continue
        base = o.name[:-len(strip)] if strip and o.name.endswith(strip) else o.name
        C.assign(o, mats[mapping[base]])


def build_a():
    sc = C.reset_scene(raytracing=False)
    col, objs = load_lampe()
    root = sc.collection
    c_a = C.new_collection("Corrigé coloris A", root)
    c_b = C.new_collection("Corrigé coloris B", root)
    mats = {}
    for name in sorted(set(COLORIS_A.values()) | set(COLORIS_B.values())):
        mats[name] = M.lampe(name, new_name=name + "_corrige")
    A = C.copy_objects(objs, c_a, "_A", (0.75, 0, 0))
    B = C.copy_objects(objs, c_b, "_B", (1.50, 0, 0))
    dress(COLORIS_A, A.values(), mats, "_A")
    dress(COLORIS_B, B.values(), mats, "_B")
    lc = bpy.context.view_layer.layer_collection.children
    lc["Corrigé coloris A"].hide_viewport = True
    lc["Corrigé coloris B"].hide_viewport = True
    txt = C.text_block(LISEZ_MOI_A)
    C.setup_layout(txt, 'SOLID', eye=(-0.55, -0.85, 0.55), target=(0.0, 0, 0.21), distance_k=0.8)
    C.select_only(bpy.data.objects["Socle"])
    C.finalize(OUT_A, groups_expected=["Smooth by Angle"])
    print("MATIERES", sorted(m.name for m in bpy.data.materials))


def append_from_nuancier(names):
    """Comme File > Append, dossier Material : la matière arrive modifiable et garde son statut d'actif."""
    with bpy.data.libraries.load(C.NUANCIER, link=False) as (src, dst):
        dst.materials = list(names)          # la liste est remplacée par les matières lues
    C.drop_weak_references()
    return {n: bpy.data.materials[n] for n in names}


def build_a2():
    sc = C.reset_scene(raytracing=True)
    col, objs = load_lampe()
    root = sc.collection
    c_b = C.new_collection("Lampe_coloris_B", root)
    mats = append_from_nuancier(["Alu_Naturel", "Laiton"])
    for name in sorted(set(COLORIS_A.values()) | set(COLORIS_B.values())):
        if name not in mats:
            mats[name] = M.lampe(name)
    for name, m in mats.items():
        if m.asset_data is None:
            m.asset_mark()
        ad = m.asset_data
        ad.author = M.AUTHOR
        ad.license = M.LICENSE
        ad.description = M.LAMPE_DESCRIPTION[name]
        ad.catalog_id = M.CATS_LAMPE[M.LAMPE_CATALOGUE[name]]
    dress(COLORIS_A, objs, mats)
    B = C.copy_objects(objs, c_b, ".001", (0.75, 0, 0))    # les noms que donne Duplicate Collection
    dress(COLORIS_B, B.values(), mats, ".001")
    txt = C.text_block(LISEZ_MOI_A2)
    C.setup_layout(txt, 'MATERIAL', eye=(0.55, -1.75, 0.75), target=(0.40, 0, 0.20), distance_k=0.85)
    C.select_only(bpy.data.objects["Bras_bas"])
    os.makedirs(C.LAMPE_DIR, exist_ok=True)
    M.write_catalogs(C.LAMPE_DIR, M.CATS_LAMPE)
    C.finalize(OUT_A2, groups_expected=["Smooth by Angle"])
    print("ACTIFS", sorted((m.name, m.asset_data.catalog_id[-2:]) for m in bpy.data.materials if m.asset_data))


if __name__ == "__main__":
    which = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    if not which or "a" in which:
        build_a()
    if not which or "a2" in which:
        build_a2()
