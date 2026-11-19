# Livre en zip les images du corrigé du chapitre 4 (fichiers séparés : ce sont des images exportées).
#   _resources/exercices/PRC02_ch4_images_corrige.zip : héros, détail, situation, situation allumée,
#   et l'image comparative Material Preview, EEVEE et Cycles.
# Les blocs de texte des PNG (tEXt, zTXt, iTXt) sont retirés : Blender y écrit à chaque rendu le chemin
# complet du .blend (« File »), la date et la caméra. Les pixels ne changent pas.
# Usage, depuis la racine du dépôt, après rendus.py (mode corrige et comparatif) et recadrer.py (figure 4.6) :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I tool\exercices_ch4\livrer.py

import os
import struct
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(HERE, "_construction", "images")
OUT = os.path.join(ROOT, "_resources", "exercices", "PRC02_ch4_images_corrige.zip")
FILES = ["PRC02_ch4_corrige_heros.png", "PRC02_ch4_corrige_detail.png", "PRC02_ch4_corrige_situation.png",
         "PRC02_ch4_corrige_situation_allumee.png", "PRC02_ch4_comparatif_moteurs.png"]
TEXT_CHUNKS = (b"tEXt", b"zTXt", b"iTXt")


def sans_metadonnees(data):
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "pas un PNG"
    out, i = [data[:8]], 8
    while i < len(data):
        length = struct.unpack(">I", data[i:i + 4])[0]
        chunk = data[i:i + 12 + length]
        if chunk[4:8] not in TEXT_CHUNKS:
            out.append(chunk)
        i += 12 + length
    return b"".join(out)


with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for f in FILES:
        with open(os.path.join(SRC, f), "rb") as fh:
            z.writestr("PRC02_ch4_images_corrige/" + f, sans_metadonnees(fh.read()))
print("ZIP", OUT, os.path.getsize(OUT), "octets :", FILES)
