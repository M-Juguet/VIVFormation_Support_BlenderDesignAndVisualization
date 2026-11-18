# Vérifie un fichier .blend livré : aucun chemin absolu, aucun nom d'utilisateur, aucune
# bibliothèque liée, aucun texte d'extension, et les réglages attendus.
#
# Usage, depuis la racine du dépôt :
#   "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --factory-startup ^
#       _resources\exercices\PRC02_ch2_defi_modelisation.blend ^
#       --python tool\exercices_ch2_defi\verifier_blend.py
#
# Le contrôle des octets lit le fichier compressé (zstd en plusieurs trames) avec le module
# zstandard livré avec le Python de Blender.

import os
import re

import bpy
import zstandard

path = bpy.data.filepath
raw = open(path, "rb").read()
if raw[:4] == b"\x28\xb5\x2f\xfd":
    data = zstandard.ZstdDecompressor().stream_reader(open(path, "rb"), read_across_frames=True).read()
else:
    data = raw
print("FICHIER", os.path.basename(path), len(raw), "octets compressés,", len(data), "décompressés")

user = os.environ.get("USERNAME", "") or os.environ.get("USER", "")
motifs = [rb"[A-Za-z]:\\", rb"[A-Za-z]:/", rb"\\Users\\", rb"/Users/", rb"AppData", rb"Program Files",
          rb"Documents", rb"/tmp/", rb"/home/", rb"Geo-Scatter"]
if user:
    motifs.append(re.escape(user.encode()))
    motifs.append(re.escape(user.lower().encode()))
bad = 0
for m in motifs:
    for hit in re.finditer(m, data):
        s = max(0, hit.start() - 40)
        ctx = data[s:hit.end() + 60].replace(b"\x00", b".")
        print("TROUVE", m, ctx)
        bad += 1
        break
print("MOTIFS SUSPECTS :", bad)

sc = bpy.context.scene
us = sc.unit_settings
print("MOTEUR", sc.render.engine, "| unites", us.system, us.length_unit, us.scale_length)
print("BIBLIOTHEQUES", [l.filepath for l in bpy.data.libraries])
print("TEXTES", [t.name for t in bpy.data.texts])
print("IMAGES", [(i.name, i.filepath, i.packed_file is not None) for i in bpy.data.images])
print("COLLECTIONS", [c.name for c in bpy.data.collections])
missing = [o.name for o in bpy.data.objects for m in o.modifiers
           if (getattr(m, "target", 1) is None) or (getattr(m, "object", 1) is None)]
print("MODIFICATEURS SANS CIBLE", missing)
print("CHEMINS EXTERNES", bpy.utils.blend_paths(absolute=False))
