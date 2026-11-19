# Livre en zip les images du corrigé du chapitre 4 (fichiers séparés : ce sont des images exportées).
#   _resources/exercices/PRC02_ch4_images_corrige.zip : héros, détail, situation, situation allumée,
#   et l'image comparative Material Preview, EEVEE et Cycles.
# Usage, depuis la racine du dépôt, après rendus.py (mode corrige et comparatif) et recadrer.py (figure 4.6) :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I tool\exercices_ch4\livrer.py

import os
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(HERE, "_construction", "images")
OUT = os.path.join(ROOT, "_resources", "exercices", "PRC02_ch4_images_corrige.zip")
FILES = ["PRC02_ch4_corrige_heros.png", "PRC02_ch4_corrige_detail.png", "PRC02_ch4_corrige_situation.png",
         "PRC02_ch4_corrige_situation_allumee.png", "PRC02_ch4_comparatif_moteurs.png"]

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for f in FILES:
        z.write(os.path.join(SRC, f), "PRC02_ch4_images_corrige/" + f)
print("ZIP", OUT, os.path.getsize(OUT), "octets :", FILES)
