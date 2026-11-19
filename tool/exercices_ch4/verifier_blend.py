# Vérifie un fichier .blend livré du chapitre 4 : aucun chemin absolu, aucun nom d'utilisateur,
# aucune bibliothèque ni référence faible vers un autre fichier, aucun texte d'extension, et les
# réglages attendus. Repris de tool/exercices_ch2_defi/verifier_blend.py, avec un motif de lecteur
# plus strict (un octet binaire suivi de « d:\ » n'est pas un chemin).
#
# Usage, depuis la racine du dépôt :
#   "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" -b --factory-startup ^
#       _resources\exercices\PRC02_ch2_lampe_depart.blend --python tool\exercices_ch2\verifier_blend.py
#
# Le fichier est compressé en zstd sur plusieurs trames : il est relu avec read_across_frames=True.

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
# les octets des images empaquetées (HDRI de plusieurs Mo) contiennent par hasard des suites comme
# « K:/-. » : on les retire avant la recherche, qui reste stricte sur tout le reste du fichier
retires = 0
for im in bpy.data.images:
    if im.packed_file is not None:
        b = im.packed_file.data
        n = data.count(b)
        data = data.replace(b, b"")
        retires += n * len(b)
print("OCTETS D'IMAGES EMPAQUETEES RETIRES DE LA RECHERCHE", retires)
motifs = [rb"(?<![\x21-\x7e])[A-Za-z]:[\\/][\x20-\x7e]{2}", rb"\\Users\\", rb"/Users/", rb"AppData", rb"Program Files",
          rb"Documents", rb"/tmp/", rb"/home/", rb"Geo-Scatter", rb"PRC02_ch2_lampe", rb"_construction", rb"studiolights", rb"exercices_ch4"]
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
weak = [i.name for c in (bpy.data.objects, bpy.data.meshes, bpy.data.curves, bpy.data.images, bpy.data.node_groups,
                         bpy.data.materials) for i in c if i.library_weak_reference]
print("REFERENCES FAIBLES", weak)
print("GROUPES DE NOEUDS", [(g.name, g.library) for g in bpy.data.node_groups])
print("TEXTES", [t.name for t in bpy.data.texts])
print("IMAGES", [(i.name, i.filepath, i.packed_file is not None) for i in bpy.data.images if i.type == 'IMAGE'])
print("CHEMINS EXTERNES", bpy.utils.blend_paths(absolute=False))


def tree(lc, d=0):
    c = lc.collection
    print("COLLECTION", "  " * d + c.name, "| objets", len(c.objects), "| œil fermé" if lc.hide_viewport else "")
    for k in lc.children:
        tree(k, d + 1)


tree(bpy.context.view_layer.layer_collection)
cibles = []
for o in bpy.data.objects:
    for m in o.modifiers:
        if m.type == 'ARRAY' and m.use_object_offset and m.offset_object is None:
            cibles.append((o.name, m.name))
        if m.type == 'BOOLEAN' and m.object is None:
            cibles.append((o.name, m.name))
        if m.type == 'NODES' and m.node_group is None:
            cibles.append((o.name, m.name))
print("MODIFICATEURS SANS CIBLE", cibles)
print("ECHELLES DIFFERENTES DE 1", [o.name for o in bpy.data.objects if any(abs(s - 1) > 1e-6 for s in o.scale)])
print("RAYTRACING", sc.eevee.use_raytracing)
print("MATIERES", sorted(m.name for m in bpy.data.materials))
print("ACTIFS", sorted((m.name, m.asset_data.catalog_id) for m in bpy.data.materials if m.asset_data))
print("COUCHES UV", [m.name for m in bpy.data.meshes if m.uv_layers])
print("SANS MATIERE", [o.name for o in bpy.data.objects if o.type in ('MESH', 'CURVE') and not any(s.material for s in o.material_slots)])
print("MONDES", sorted((w.name, w.use_fake_user) for w in bpy.data.worlds), "| actif", sc.world.name)
print("IMAGES EMPAQUETEES", [(i.name, i.filepath, [pf.filepath for pf in i.packed_files]) for i in bpy.data.images if i.type == 'IMAGE'])
print("RENDU", sc.render.resolution_x, sc.render.resolution_y, sc.render.image_settings.file_format,
      sc.render.image_settings.color_mode, sc.render.filepath, "| echantillons", sc.eevee.taa_render_samples,
      sc.eevee.taa_samples, "| vue", sc.view_settings.view_transform, "| camera", sc.camera.name)
print("MASQUEES", [c.name for c in bpy.data.collections if c.hide_render])
