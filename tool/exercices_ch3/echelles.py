# Calcule l'échelle d'affichage de chaque figure du chapitre 3 dans l'application : la colonne de texte
# fait 715 px ; une figure pleine largeur s'affiche dans 715 x 450 px au plus, une figure côte à côte
# dans 345 x 300 px au plus. Échelle = min(715 / L, 450 / H) ou min(345 / L, 300 / H). Une figure qui
# montre l'interface doit s'afficher à 0,5 au moins.
#
# Usage, depuis la racine du dépôt :
#   "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -I tool\exercices_ch3\echelles.py

import os
import re
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
MD = os.path.join(ROOT, "_resources", "PRC02-SU-26v01_chap3_matieres_finitions_sans_uv.md")


def jpeg_size(path):
    d = open(path, "rb").read()
    i = 2
    while i < len(d):
        if d[i] != 0xFF:
            i += 1
            continue
        m = d[i + 1]
        if m in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", d[i + 5:i + 9])
            return w, h
        ln = struct.unpack(">H", d[i + 2:i + 4])[0]
        i += 2 + ln
    raise ValueError(path)


def figures():
    text = open(MD, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'imagePath: "([^"]+)"\ncaption: "Figure (3\.\d+)', text):
        out.append((m.group(2), m.group(1), "côte à côte", m.start()))
    for m in re.finditer(r'!\[Figure (3\.\d+) :[^\]]*\]\(([^)]+)\)', text):
        out.append((m.group(1), m.group(2), "pleine largeur", m.start()))
    return sorted(out, key=lambda f: f[3])


def main():
    low = 0
    for num, path, kind, _pos in figures():
        w, h = jpeg_size(os.path.join(ROOT, path))
        s = min(715 / w, 450 / h) if kind == "pleine largeur" else min(345 / w, 300 / h)
        flag = "" if s >= 0.5 else "  < 0,5"
        low += s < 0.5
        print("%-5s %-15s %5d x %-4d échelle %.2f  %s%s" % (num, kind, w, h, s, os.path.basename(path), flag))
    print("FIGURES SOUS 0,5 :", low)


main()
