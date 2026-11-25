# Livre les lots de textures PBR du socle (chapitre 3, section 2) :
#   _resources/exercices/PRC02_ch3_textures_pbr.zip  (le dossier textures_pbr/, distribué aux apprenants)
#
# Les cartes viennent de Poly Haven (polyhaven.com), sous licence CC0 1.0. Elles ont été téléchargées une
# fois, le 25 novembre 2026, avec l'accord du formateur, en 1K et en JPG, depuis l'API publique
# (https://api.polyhaven.com/files/<lot>), puis contrôlées par leur empreinte MD5. Elles sont rangées dans
# tool/exercices_ch3/textures_pbr/<lot>/ (non suivi par git, comme les HDRI du chapitre 4).
#
# Le script vérifie chaque carte (taille, empreinte, en-tête JPEG sans segment de métadonnées qui contienne
# un chemin), écrit le zip avec un LISEZ-MOI, puis relit chaque fichier décompressé à la recherche de
# chemins absolus ou d'un nom d'utilisateur.
#
# Usage, depuis la racine du dépôt :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I tool\exercices_ch3\textures_pbr.py

import hashlib
import os
import re
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(HERE, "textures_pbr")
ZIP = os.path.join(ROOT, "_resources", "exercices", "PRC02_ch3_textures_pbr.zip")

# lot : (nom français, auteurs, taille réelle, matière du chapitre, Scale du Mapping sur le socle)
LOTS = {
    "walnut_veneer_02": ("placage de noyer", "Jenelle van Heerden", "1 m x 1 m", "Bois_Noyer", "2"),
    "granular_concrete": ("béton lisse", "Dario Barresi, Michael Jenkins", "2,4 m x 2,4 m", "Beton_Lisse", "4"),
    "rosewood_veneer1": ("palissandre verni", "Jenelle van Heerden", "2,43 m x 2,43 m", "Palissandre_Verni", "3"),
}
# carte : (Color Space, entrée du Principled)
CARTES = {
    "diff": ("sRGB", "Base Color"),
    "rough": ("Non-Color", "Roughness"),
    "nor_gl": ("Non-Color", "Normal, par un nœud Normal Map"),
    "disp": ("Non-Color", "option : Height d'un nœud Bump"),
}
# empreintes MD5 et tailles données par l'API de Poly Haven le 25 novembre 2026
MD5 = {
    "walnut_veneer_02_diff_1k.jpg": ("5f1198a623856d828387febc07a1811d", 592833),
    "walnut_veneer_02_rough_1k.jpg": ("52d8f00e50a49eb45dbca23f252d9ba6", 743210),
    "walnut_veneer_02_nor_gl_1k.jpg": ("0c463e1aea6016e70f87eba9d664ec56", 362888),
    "walnut_veneer_02_disp_1k.jpg": ("bfa7e9a6c03a73ba1d399993a2e4f626", 151005),
    "granular_concrete_diff_1k.jpg": ("189811555459ff4d539c862f2b478083", 854724),
    "granular_concrete_rough_1k.jpg": ("4905547af76bacba1e0163e80a797d3a", 392344),
    "granular_concrete_nor_gl_1k.jpg": ("f6cbde2f3fd386f76114cf99db46528f", 1234017),
    "granular_concrete_disp_1k.jpg": ("183b0af9bb5f7d0928a1a2b9daffae6d", 605497),
    "rosewood_veneer1_diff_1k.jpg": ("dc521e4adac8d21b4439bb920fbe0682", 836142),
    "rosewood_veneer1_rough_1k.jpg": ("b71bf78ab6ad4f98d8c08dc713a69e43", 234966),
    "rosewood_veneer1_nor_gl_1k.jpg": ("e5183b44a660e708bfcdfd9726c54c47", 327517),
    "rosewood_veneer1_disp_1k.jpg": ("a5f38c87fd2434a0b208425257d697ef", 439320),
}


def lisez_moi():
    lines = [
        "PRC02 · Chapitre 3 · Lots de textures PBR",
        "Trois lots de Poly Haven (polyhaven.com), sous licence CC0 1.0 : tout usage est permis,",
        "y compris commercial, sans attribution obligatoire. Définition 1K (1024 x 1024 pixels), format JPG.",
        "Téléchargés le 25 novembre 2026 ; chaque carte est inchangée.",
        "",
        "Les lots (dossier, source, taille réelle d'une tuile, matière du chapitre, Scale du Mapping sur le socle) :",
    ]
    for lot, (nom, auteurs, taille, matiere, scale) in LOTS.items():
        lines.append("- %s/ : %s, de %s. https://polyhaven.com/a/%s" % (lot, nom, auteurs, lot))
        lines.append("  Tuile de %s. Matière %s, Scale %s." % (taille, matiere, scale))
    lines += ["", "Les cartes de chaque lot (fin du nom du fichier, Color Space, entrée du Principled BSDF) :"]
    for carte, (espace, entree) in CARTES.items():
        lines.append("- %s : %s ; %s." % (carte, espace, entree))
    lines += [
        "",
        "Sans dépliage UV : chaque carte dans un nœud Image Texture en projection Box, Blend 0,25.",
        "Un seul Texture Coordinate (sortie Object) et un seul Mapping pour toutes les cartes.",
        "nor_gl est au format OpenGL, celui de Blender. Décompressez le dossier textures_pbr",
        "à côté de votre fichier de travail, comme textures_cmf.",
    ]
    return "\r\n".join(lines) + "\r\n"


def jpeg_meta(data):
    """Les segments APPn et COM d'un JPEG, jusqu'au début de l'image (SOS)."""
    assert data[:2] == b"\xff\xd8", "pas un JPEG"
    i, segs = 2, []
    while i < len(data) - 4:
        if data[i] != 0xFF:
            break
        m = data[i + 1]
        if m == 0xDA:      # SOS : la suite est l'image
            break
        ln = int.from_bytes(data[i + 2:i + 4], "big")
        if 0xE0 <= m <= 0xEF or m == 0xFE:
            segs.append((m, data[i + 4:i + 2 + ln]))
        i += 2 + ln
    return segs


def main():
    user = os.environ.get("USERNAME", "") or os.environ.get("USER", "")
    # un lecteur suivi de « :\ » ou « :/ », sauf après un caractère imprimable (« https:// » n'est pas un chemin)
    motifs = [rb"(?<![\x21-\x7e])[A-Za-z]:[\\/][\x20-\x7e]{2}", rb"\\Users\\", rb"/Users/", rb"AppData", rb"/home/", rb"Workspace"]
    if user:
        motifs += [re.escape(user.encode()), re.escape(user.lower().encode())]
    files = []
    for lot in LOTS:
        for carte in CARTES:
            name = "%s_%s_1k.jpg" % (lot, carte)
            path = os.path.join(SRC, lot, name)
            data = open(path, "rb").read()
            md5, size = MD5[name]
            assert len(data) == size and hashlib.md5(data).hexdigest() == md5, name
            for m, seg in jpeg_meta(data):
                for p in motifs:
                    assert not re.search(p, seg), (name, hex(m), p)
            files.append((lot, name, path))
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for lot, name, path in files:
            z.write(path, "textures_pbr/%s/%s" % (lot, name))
        z.writestr("textures_pbr/LISEZ-MOI.txt", lisez_moi().encode("utf-8"))
    print("ZIP", os.path.relpath(ZIP, ROOT), os.path.getsize(ZIP), "octets")
    # contrôle : chaque fichier relu décompressé, jamais les octets du zip
    bad = 0
    with zipfile.ZipFile(ZIP) as z:
        for info in z.infolist():
            assert not info.filename.startswith("/") and ":" not in info.filename and ".." not in info.filename
            data = z.read(info.filename)
            if info.filename.endswith(".jpg"):
                assert hashlib.md5(data).hexdigest() == MD5[os.path.basename(info.filename)][0]
                data = b"".join(seg for _m, seg in jpeg_meta(data))
            for p in motifs:
                if re.search(p, data):
                    print("TROUVE", info.filename, p)
                    bad += 1
            print("  ", info.filename, info.file_size)
    print("MOTIFS SUSPECTS :", bad)
    assert bad == 0


if __name__ == "__main__":
    main()
