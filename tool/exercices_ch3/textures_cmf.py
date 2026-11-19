# Crée les cinq images de finition du chapitre 3 (plan : _resources/plans/PRC02-plan-chap3.md, fiche D),
# sans aucune source extérieure : elles sont libres de droits (CC0) par construction.
#   tool/exercices_ch3/textures_cmf/<nom>.png  (source, utilisée par les scripts de construction)
#   _resources/exercices/PRC02_ch3_textures_cmf.zip  (le dossier textures_cmf/, distribué aux apprenants)
#
# Toutes les images sont périodiques : bruit filtré par transformée de Fourier, cellules de Voronoi sur
# un tore, ou motif sur une grille entière. Répétées en 2 x 2, elles ne montrent aucune couture.
# 512 x 512 px : la projection Box en Material Preview n'en demande pas plus (par délégation : le plan
# prévoyait 1024 px ; 512 px divisent par quatre le poids des fichiers d'exercice).
#
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 -Script tool\exercices_ch3\textures_cmf.py
# Option : « -- planche <dossier> » écrit aussi une planche de contrôle 2 x 2 de chaque image.

import os
import sys
import zipfile

import bpy
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "textures_cmf")
ZIP = os.path.join(ROOT, "_resources", "exercices", "PRC02_ch3_textures_cmf.zip")
N = 512
rng = np.random.default_rng(20261119)


def norm(a):
    a = a - a.min()
    return a / max(a.max(), 1e-9)


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


def fft_noise(f0, width, n=N):
    """Bruit périodique : spectre aléatoire limité à une bande autour de f0 cycles par tuile."""
    fx = np.fft.fftfreq(n) * n
    kx, ky = np.meshgrid(fx, fx)
    k = np.hypot(kx, ky)
    amp = np.exp(-((k - f0) / width) ** 2)
    amp[0, 0] = 0
    ph = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return norm(np.real(np.fft.ifft2(amp * ph)))


def voronoi(count, n=N):
    """Distances F1 et F2 aux germes, sur un tore (la tuile se raccorde). Les germes gardent un écart
    minimal : deux germes trop proches dessinent un éventail sombre au lieu d'une cellule."""
    gap = 0.6 / np.sqrt(count)
    pts = []
    while len(pts) < count:
        p = rng.random(2)
        ok = True
        for q in pts:
            d = np.abs(p - q)
            d = np.minimum(d, 1 - d)
            if np.hypot(*d) < gap:
                ok = False
                break
        if ok:
            pts.append(p)
    pts = np.array(pts)
    u = (np.arange(n) + 0.5) / n
    X, Y = np.meshgrid(u, u)
    f1 = np.full((n, n), 9.0)
    f2 = np.full((n, n), 9.0)
    for px, py in pts:
        dx = np.abs(X - px)
        dy = np.abs(Y - py)
        dx = np.minimum(dx, 1 - dx)
        dy = np.minimum(dy, 1 - dy)
        d = np.hypot(dx, dy)
        f2 = np.where(d < f1, f1, np.minimum(f2, d))
        f1 = np.minimum(f1, d)
    return f1, f2


# ---------------------------------------------------------------------------- les cinq images
def grain_structure():
    """Peinture structurée : des bosses douces, environ 25 par tuile, et un voile plus fin."""
    a = 0.75 * fft_noise(5.0, 1.6) + 0.25 * fft_noise(14.0, 4.0)
    return smoothstep(0.15, 0.9, norm(a))


def grain_cuir():
    """Cuir grainé : 40 cellules par tuile, creux le long des bords, et un bruit fin."""
    f1, f2 = voronoi(40)
    edge = smoothstep(0.0, 0.03, f2 - f1)            # 0 sur le bord d'une cellule, 1 au centre
    dome = 1 - norm(f1) * 0.35                       # chaque cellule légèrement bombée
    fine = fft_noise(60.0, 20.0)
    wobble = fft_noise(10.0, 3.0)                    # des cellules plus ou moins hautes
    return norm(edge * dome * (0.75 + 0.25 * wobble) * 0.85 + 0.15 * fine)


def serge(n=N, tows=8):
    """Sergé 2 x 2 : hauteur et couleur. Les mèches verticales (chaîne) et horizontales (trame)
    passent dessus deux cellules, dessous deux cellules, décalées d'une cellule à chaque rangée."""
    u = (np.arange(n) + 0.5) / n * tows
    X, Y = np.meshgrid(u, u)
    i = np.floor(X).astype(int)
    j = np.floor(Y).astype(int)
    fx = X - i
    fy = Y - j
    warp_on_top = ((i + j) % 4) < 2
    # mèche de chaîne (verticale) : bombée en travers (x), plonge aux bouts de sa portée (y)
    run_w = ((i + j) % 4).astype(float)              # 0 ou 1 : première ou seconde cellule de la portée
    along_w = np.where(warp_on_top, (run_w + fy) / 2, 0.5)
    run_t = ((i + j + 2) % 4).astype(float)
    along_t = np.where(~warp_on_top, (run_t + fx) / 2, 0.5)
    across_w = np.sin(np.pi * fx)
    across_t = np.sin(np.pi * fy)
    dip_w = np.sin(np.pi * np.clip(along_w, 0, 1)) ** 0.35
    dip_t = np.sin(np.pi * np.clip(along_t, 0, 1)) ** 0.35
    h = np.where(warp_on_top, across_w * dip_w, across_t * dip_t)
    # fibres : fines stries dans le sens de la mèche
    fib = np.where(warp_on_top, np.sin(fx * np.pi * 26) ** 2, np.sin(fy * np.pi * 26) ** 2)
    height = norm(h * 0.92 + 0.08 * fib)
    # couleur : du noir au gris très sombre, reflet léger au centre de chaque mèche
    col = 0.03 + 0.16 * (np.where(warp_on_top, across_w, across_t) ** 3) + 0.025 * fib
    col = col * np.where(warp_on_top, 1.0, 0.82)      # la trame paraît un peu plus sombre
    return height, np.clip(col, 0, 1)


def tole_larmee(n=N, cells=4):
    """Tôle larmée : une larme par cellule, à + 45° et - 45° en damier, fond plat noir."""
    u = (np.arange(n) + 0.5) / n * cells
    X, Y = np.meshgrid(u, u)
    i = np.floor(X).astype(int)
    j = np.floor(Y).astype(int)
    cx = X - i - 0.5
    cy = Y - j - 0.5
    ang = np.where((i + j) % 2 == 0, np.pi / 4, -np.pi / 4)
    ca, sa = np.cos(ang), np.sin(ang)
    a = cx * ca + cy * sa                               # le long de la larme
    b = -cx * sa + cy * ca                              # en travers
    L, W = 0.36, 0.085                                  # demi-longueur, demi-largeur (en cellules)
    t = np.clip(a / L, -1, 1)
    half = W * np.sqrt(np.clip(1 - t * t, 0, 1))        # profil en lentille
    inside = (np.abs(a) <= L) & (np.abs(b) <= half + 1e-6)
    r = np.where(half > 1e-6, np.abs(b) / np.maximum(half, 1e-6), 9)
    dome = np.sqrt(np.clip(1 - np.clip(r, 0, 1) ** 2, 0, 1)) * np.sqrt(np.clip(1 - t * t, 0, 1))
    edge = smoothstep(1.0, 0.82, r) * smoothstep(1.0, 0.9, np.abs(t))
    return np.where(inside, 0.25 + 0.75 * dome, 0) * edge


# ---------------------------------------------------------------------------- écriture
def save_png(name, gray=None, rgb=None):
    os.makedirs(OUT, exist_ok=True)
    if rgb is None:
        rgb = np.stack([gray] * 3, axis=-1)
    px = np.ones((N, N, 4), dtype=np.float32)
    px[..., :3] = rgb
    im = bpy.data.images.new(name, N, N, alpha=False)
    if gray is None:
        im.colorspace_settings.name = 'sRGB'
    else:
        im.colorspace_settings.name = 'Non-Color'
    im.pixels = px[::-1].ravel()                         # Blender range les rangées du bas vers le haut
    path = os.path.join(OUT, name + ".png")
    sc = bpy.context.scene
    st = sc.render.image_settings
    st.file_format = 'PNG'
    st.color_mode = 'BW' if gray is not None else 'RGB'
    st.color_depth = '8'
    st.compression = 100
    im.save_render(path, scene=sc)
    bpy.data.images.remove(im)
    print("IMAGE", name, os.path.getsize(path), "octets")
    return path


def planche(folder, name, arr):
    """Contrôle du raccord : l'image répétée en 2 x 2."""
    big = np.tile(arr, (2, 2, 1)) if arr.ndim == 3 else np.tile(arr, (2, 2))
    if big.ndim == 2:
        big = np.stack([big] * 3, axis=-1)
    h, w = big.shape[:2]
    px = np.ones((h, w, 4), dtype=np.float32)
    px[..., :3] = big
    im = bpy.data.images.new("planche_" + name, w, h, alpha=False)
    im.pixels = px[::-1].ravel()
    im.filepath_raw = os.path.join(folder, "planche_" + name + ".png")
    im.file_format = 'PNG'
    im.save()
    bpy.data.images.remove(im)


def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    folder = args[1] if len(args) > 1 and args[0] == "planche" else None
    h, c = serge()
    images = {
        "grain_structure": grain_structure(),
        "grain_cuir": grain_cuir(),
        "carbone_serge_relief": h,
        "tole_larmee": tole_larmee(),
    }
    paths = []
    for name, arr in images.items():
        paths.append(save_png(name, gray=arr.astype(np.float32)))
        if folder:
            planche(folder, name, arr)
    rgb = np.stack([c, c * 1.0, c * 1.04], axis=-1).astype(np.float32)   # noir à peine bleuté
    paths.append(save_png("carbone_serge_couleur", rgb=rgb))
    if folder:
        planche(folder, "carbone_serge_couleur", rgb)
    os.makedirs(os.path.dirname(ZIP), exist_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(paths):
            z.write(p, "textures_cmf/" + os.path.basename(p))
        z.writestr("textures_cmf/LISEZ-MOI.txt",
                   "PRC02 · Chapitre 3 · Images de finition\r\n"
                   "Cinq images raccordables, créées par VIV Formation, libres de droits (CC0 1.0).\r\n"
                   "Images de relief (Color Space : Non-Color) : grain_structure, grain_cuir, carbone_serge_relief, tole_larmee.\r\n"
                   "Image de couleur (Color Space : sRGB) : carbone_serge_couleur.\r\n"
                   "Taille réelle d'une tuile et Scale du nœud Mapping : grain_structure 20 mm (50) ; grain_cuir 40 mm (25) ;\r\n"
                   "carbone_serge 16 mm (62.5) ; tole_larmee 120 mm (8.33).\r\n")
    print("ZIP", ZIP, os.path.getsize(ZIP), "octets")


main()
