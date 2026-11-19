# Fichier 3 du chapitre 2 : _resources/exercices/croquis_ampoule_profil.png
# (demi-profil de l'ampoule, à décalquer en vue de face avec Curve Pen).
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 `
#       -Script tool\exercices_ch2\croquis_ampoule.py
#
# Blender calcule la courbe de Bézier du corrigé (mêmes points, mêmes types de poignée que
# l'objet Ampoule de build_lampe.py) ; le script écrit un SVG, puis Microsoft Edge, sans interface,
# l'exporte en PNG de 1200 x 1200 px. Échelle : 10 px par millimètre ; la base de l'ampoule (z = 0)
# est à la ligne 1000, l'axe sur la colonne 600. Couleurs reprises des croquis du chapitre 1.

import os
import subprocess

import bpy
import numpy as np
from mathutils.geometry import interpolate_bezier

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT_PNG = os.path.join(ROOT, "_resources", "exercices", "croquis_ampoule_profil.png")
OUT_SVG = os.path.join(HERE, "croquis_ampoule_profil.svg")
REF = os.path.join(ROOT, "_resources", "exercices", "croquis_lampe_profil.png")

# Points du corrigé (mm) : (rayon, hauteur), type de poignée
PTS = [((0, 0), 'VECTOR'), ((13.5, 4), 'VECTOR'), ((13.5, 25), 'VECTOR'), ((25, 55), 'AUTO'), ((0, 80), 'ALIGNED')]
TOP_HANDLE = 12.0      # poignées horizontales du point 5, à ±12 mm


def couleur_ref():
    """Fond et trait des croquis du chapitre 1."""
    im = bpy.data.images.load(REF)
    w, h = im.size
    px = np.array(im.pixels[:], dtype=np.float32).reshape(h, w, 4)
    bg = px[5, 5, :3]
    dark = px.reshape(-1, 4)[np.argmin(px.reshape(-1, 4)[:, :3].sum(axis=1)), :3]
    bpy.data.images.remove(im)

    def to_hex(c):
        # pixels déjà en sRGB pour une image 8 bits : aucune conversion
        return "#%02X%02X%02X" % tuple(int(round(max(0, min(1, x)) * 255)) for x in c)
    return to_hex(bg), to_hex(dark)


def courbe():
    """Échantillonne la spline telle que Blender la calcule (poignées Auto résolues)."""
    cu = bpy.data.curves.new("Ampoule", 'CURVE')
    cu.dimensions = '3D'
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(PTS) - 1)
    for bp, ((r, z), t) in zip(sp.bezier_points, PTS):
        bp.co = (r / 1000, 0, z / 1000)
        bp.handle_left_type = bp.handle_right_type = t
    top = sp.bezier_points[-1]
    top.handle_left = (TOP_HANDLE / 1000, 0, 0.080)
    top.handle_right = (-TOP_HANDLE / 1000, 0, 0.080)
    ob = bpy.data.objects.new("Ampoule", cu)
    bpy.context.scene.collection.objects.link(ob)
    bpy.context.view_layer.update()
    pts = []
    bps = sp.bezier_points
    for a, b in zip(bps[:-1], bps[1:]):
        seg = interpolate_bezier(a.co, a.handle_right, b.handle_left, b.co, 48)
        if pts:
            seg = seg[1:]
        pts += [(v.x * 1000, v.z * 1000) for v in seg]
    return pts


def px(r, z):
    return 600 + r * 10, 1000 - z * 10


def svg(pts, bg, ink):
    right = " ".join("%.1f,%.1f" % px(r, z) for r, z in pts)
    left = " ".join("%.1f,%.1f" % px(-r, z) for r, z in pts)
    rmax, zmax = max(pts, key=lambda p: p[0])
    out = []
    a = out.append
    a('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200">')
    a('<rect width="1200" height="1200" fill="%s"/>' % bg)
    a('<style>text{font-family:"Segoe UI",Arial,sans-serif;fill:%s}</style>' % ink)
    # axe de révolution, trait mixte rouge
    a('<line x1="600" y1="1100" x2="600" y2="100" stroke="#C8332B" stroke-width="3" stroke-dasharray="36 10 6 10"/>')
    a('<text x="612" y="92" font-size="30" style="fill:#C8332B">axe</text>')
    # base (z = 0)
    a('<line x1="430" y1="1000" x2="770" y2="1000" stroke="%s" stroke-width="1.5" stroke-dasharray="6 8" opacity="0.6"/>' % ink)
    # moitié gauche, pour l'allure
    a('<polyline points="%s" fill="none" stroke="#B9BCC2" stroke-width="3" stroke-dasharray="14 10"/>' % left)
    # demi-profil droit
    a('<polyline points="%s" fill="none" stroke="%s" stroke-width="4" stroke-linejoin="round"/>' % (right, ink))
    # cote Ø 50 à la plus grande largeur
    yd = px(0, zmax)[1]
    x0, x1 = px(-rmax, 0)[0], px(rmax, 0)[0]
    ycote = yd - 150
    for x in (x0, x1):
        a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.5"/>' % (x, yd - 10, x, ycote - 14, ink))
    a('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (x0, ycote, x1, ycote, ink))
    for x, s in ((x0, 1), (x1, -1)):
        a('<path d="M%.1f,%.1f l%d,-8 l0,16 z" fill="%s"/>' % (x, ycote, 22 * s, ink))
    a('<text x="%.1f" y="%.1f" font-size="38" text-anchor="middle" style="paint-order:stroke;stroke:%s;stroke-width:10px">Ø 50</text>' % (450, ycote - 14, bg))
    # cote 80 (hauteur totale)
    xc = 1010
    for y in (1000, 200):
        a('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.5"/>' % (640 if y == 200 else 780, y, xc + 14, y, ink))
    a('<line x1="%d" y1="1000" x2="%d" y2="200" stroke="%s" stroke-width="2"/>' % (xc, xc, ink))
    for y, s in ((1000, -1), (200, 1)):
        a('<path d="M%d,%d l-8,%d l16,0 z" fill="%s"/>' % (xc, y, 22 * s, ink))
    a('<text x="%d" y="610" font-size="38" text-anchor="middle" transform="rotate(-90 %d 610)" style="paint-order:stroke;stroke:%s;stroke-width:10px">80</text>' % (xc - 18, xc - 18, bg))
    # pastilles numérotées
    for i, ((r, z), _t) in enumerate(PTS):
        x, y = px(r, z)
        dx = {0: -58, 1: 52, 2: 52, 3: 56, 4: -58}[i]
        dy = {0: 40, 1: 10, 2: 0, 3: 0, 4: -34}[i]
        a('<circle cx="%.1f" cy="%.1f" r="8" fill="%s"/>' % (x, y, ink))
        a('<circle cx="%.1f" cy="%.1f" r="24" fill="%s"/>' % (x + dx, y + dy, ink))
        a('<text x="%.1f" y="%.1f" font-size="30" font-weight="600" text-anchor="middle" style="fill:%s">%d</text>' % (x + dx, y + dy + 10, bg, i + 1))
    # légende
    a('<text x="60" y="1150" font-size="30">Ampoule · demi-profil · cotes en mm · 1 et 5 sur l\'axe</text>')
    a('</svg>')
    return "\n".join(out), rmax, zmax


def edge():
    for p in (os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Microsoft", "Edge", "Application", "msedge.exe"),
              os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft", "Edge", "Application", "msedge.exe")):
        if os.path.exists(p):
            return p
    raise FileNotFoundError("msedge.exe")


def attendre_fichier(path, timeout=60):
    """msedge.exe rend la main avant d'écrire la capture : on attend le fichier, puis une taille stable."""
    import time
    t0, last = time.time(), -1
    while time.time() - t0 < timeout:
        if os.path.exists(path):
            size = os.path.getsize(path)
            if size > 0 and size == last:
                return
            last = size
        time.sleep(0.5)
    raise TimeoutError(path)


def main():
    bg, ink = couleur_ref()
    pts = courbe()
    text, rmax, zmax = svg(pts, bg, ink)
    with open(OUT_SVG, "w", encoding="utf-8") as f:
        f.write(text)
    print("COULEURS", bg, ink, "| rayon maximal %.2f mm à z = %.2f mm" % (rmax, zmax))
    url = "file:///" + OUT_SVG.replace("\\", "/")
    tmp = os.path.join(os.environ.get("TEMP", HERE), "edge-croquis-profile")
    cmd = [edge(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
           "--user-data-dir=" + tmp, "--window-size=1200,1200", "--screenshot=" + OUT_PNG, url]
    if os.path.exists(OUT_PNG):
        os.remove(OUT_PNG)
    subprocess.run(cmd, check=True, timeout=120)
    attendre_fichier(OUT_PNG)
    im = bpy.data.images.load(OUT_PNG)
    print("PNG", OUT_PNG, tuple(im.size))
    assert tuple(im.size) == (1200, 1200), im.size


main()
