# Livre en zip les deux dossiers du chapitre 3 qui contiennent des actifs rangés : le fichier de
# catalogues doit accompagner le .blend (Blender le cherche à côté de lui).
#   _resources/exercices/PRC02_bibliotheque_CMF.zip      (fiche B : le nuancier et ses catalogues)
#   _resources/exercices/PRC02_ch3_lampe_habillage.zip   (fiche A2 : la lampe habillée et ses catalogues)
#
# Usage, depuis la racine du dépôt, après build_bibliotheque.py, build_lampe.py et finish_ui.py :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I tool\exercices_ch3\livrer.py

import os
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
WORK = os.path.join(HERE, "_construction")
EX = os.path.join(ROOT, "_resources", "exercices")

for folder in ("PRC02_bibliotheque_CMF", "PRC02_ch3_lampe_habillage"):
    src = os.path.join(WORK, folder)
    files = sorted(f for f in os.listdir(src) if f.endswith(".blend") or f == "blender_assets.cats.txt")
    assert any(f.endswith(".blend") for f in files) and "blender_assets.cats.txt" in files, files
    out = os.path.join(EX, folder + ".zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(os.path.join(src, f), folder + "/" + f)
    print("ZIP", out, os.path.getsize(out), "octets :", files)
