# Livre la planche CMF en un zip : _resources/exercices/PRC02_CMF_planche.zip, avec le dossier
# PRC02_CMF_planche/ (les deux .blend, blender_assets.cats.txt qui range les actifs, le mémo PDF s'il existe).
# Le fichier de catalogues doit rester à côté des .blend : c'est lui qui range les actifs de Current File.
# Puis relit chaque fichier décompressé : aucun chemin absolu ni nom d'utilisateur.
#
# Usage, depuis la racine du dépôt, après construire.ps1 :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I tool\exercices_cmf\livrer.py

import io
import os
import re
import zipfile

import zstandard

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(HERE, "_construction", "PRC02_CMF_planche")
OUT = os.path.join(ROOT, "_resources", "exercices", "PRC02_CMF_planche.zip")
MEMO = os.path.join(ROOT, "_resources", "PRC02-memo-cmf.pdf")
FILES = ["PRC02_CMF_planche_vierge.blend", "PRC02_CMF_planche_exemple.blend", "blender_assets.cats.txt"]

entries = [(os.path.join(SRC, f), "PRC02_CMF_planche/" + f) for f in FILES if os.path.exists(os.path.join(SRC, f))]
if os.path.exists(MEMO):
    entries.append((MEMO, "PRC02_CMF_planche/PRC02-memo-cmf.pdf"))
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for src, arc in entries:
        z.write(src, arc)
print("ZIP", OUT, os.path.getsize(OUT), "octets :", [a for _, a in entries])

# contrôle : chaque fichier décompressé, jamais les octets du zip
user = os.environ.get("USERNAME", "") or os.environ.get("USER", "")
motifs = [rb"\\Users\\", rb"/Users/", rb"AppData", rb"Program Files", rb"_construction", rb"exercices_cmf"]
if user:
    motifs += [re.escape(user.encode()), re.escape(user.lower().encode())]
with zipfile.ZipFile(OUT) as z:
    for info in z.infolist():
        data = z.read(info)
        if data[:4] == b"\x28\xb5\x2f\xfd":
            data = zstandard.ZstdDecompressor().stream_reader(io.BytesIO(data), read_across_frames=True).read()
        hits = [m for m in motifs if re.search(m, data)]
        print("CONTROLE", info.filename, len(data), "octets lus", "| motifs :", hits or "aucun")
