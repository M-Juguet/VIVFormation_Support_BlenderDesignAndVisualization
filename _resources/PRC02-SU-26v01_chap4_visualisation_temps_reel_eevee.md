## 1. Paramétrage d'EEVEE

> [!NOTE]
> Ce chapitre part de la lampe habillée au chapitre 3. Il réutilise les modes d'affichage (Basics 101), *Material Preview* et la case *Raytracing*, cochée pour le verre (chapitre 3), *File > Append* (chapitre 3) et l'œil et l'appareil photo de l'Outliner (Basics 101) : ils servent ici sans être redits. Il apporte le rendu, l'éclairage, la caméra et l'export. Les captures et les libellés correspondent à Blender 5.2 LTS, avec l'interface en anglais.

### Où l'on en est
La lampe de bureau a été bloquée au chapitre 1, modélisée au chapitre 2, puis habillée au chapitre 3. Dans ce dernier chapitre, vous la mettez en scène : vous la placez dans un studio, vous l'éclairez, vous la cadrez, puis vous en exportez des visuels de présentation.

À la fin de la demi-journée, vous savez :
- choisir le bon affichage selon le besoin : *Material Preview*, *Rendered* avec EEVEE, ou un rendu Cycles ;
- régler EEVEE pour un rendu fidèle : échantillons, *Raytracing*, transformation de vue ;
- éclairer un produit par une image HDRI, ou en studio avec trois lumières ;
- cadrer avec une focale adaptée, des guides de composition et une profondeur de champ ;
- exporter des visuels au bon format, nommés selon une convention.

L'atelier final vous demande trois visuels : une vue héros, un détail et une mise en situation. Les voici, tels que le corrigé les produit.

![Figure 4.1 : Le but du chapitre : les trois visuels du corrigé. À gauche, la vue héros, en studio ; au milieu, le détail de l'interrupteur et de la grille, avec une profondeur de champ ; à droite, la mise en situation sur un bureau, éclairée par une HDRI d'intérieur.](assets/images/lamp_three_visuals_target_blender.jpg)

```resource
title: "Fichier d'exercice : le studio"
description: "Le studio du chapitre : un fond courbe, un nuancier, un plateau de bureau en chêne masqué, quatre mondes (trois HDRI et un gris neutre) et une caméra de travail. Vous y amenez votre lampe par File > Append. Les corrigés sont dans les collections masquées « Corrigé éclairage », « Corrigé caméras » et « Corrigé paliers ». Le texte LISEZ-MOI donne les consignes de chaque partie et une ligne « Corrigé » par partie."
fileName: "PRC02_ch4_studio.blend (15.2 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch4_studio.blend"
```

```resource
title: "Fichier de secours : la lampe en studio"
description: "Le même studio, avec la lampe habillée du chapitre 3 déjà en place : le coloris A dans la collection Lampe, le coloris B masqué dans Lampe_coloris_B. Ouvrez-le si votre lampe du chapitre 3 n'est pas utilisable, ou si vous êtes perdu en cours de route, puis enregistrez-le sous lampe_rendu_v001.blend."
fileName: "PRC02_ch4_lampe_en_studio.blend (15.5 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch4_lampe_en_studio.blend"
```

### Recette · Amener la lampe dans le studio
Le chapitre 3 l'avait annoncé : *File > Append* amène la lampe dans son studio. C'est le geste de la douille, dans le dossier *Collection* au lieu du dossier *Material*.
- **1.** Ouvrez `PRC02_ch4_studio.blend`.
- **2.** *File > Append*. Allez dans votre dossier de travail, double-cliquez sur `lampe_habillage_v002.blend`, puis sur le dossier *Collection*.
- **3.** Choisissez la collection *Lampe*, puis *Append*. La lampe arrive à sa place, posée sur le fond du studio, avec ses matières.
- **4.** Enregistrez aussitôt sous `lampe_rendu_v001.blend` (*File > Save As*).
Contrôle : la lampe est posée sur le fond, et le titre de la fenêtre affiche `lampe_rendu_v001.blend`. Corrigé : le fichier de secours `PRC02_ch4_lampe_en_studio.blend` montre la lampe en place.

### Le dossier Collection
La fenêtre d'*Append* est celle du chapitre 3 (figure 3.41). Le dossier *Collection* contient les deux coloris : *Lampe*, le coloris A, et `Lampe_coloris_B`.

Choisissez *Lampe*. Le coloris B attend : il servira au palier ★ de l'atelier.

![Figure 4.2 : File > Append, à l'intérieur de lampe_habillage_v002.blend : le dossier Collection contient Lampe et Lampe_coloris_B. Choisissez Lampe. Le chemin du poste est flouté.](assets/images/append_collection_browser_blender.jpg)

> [!TIP]
> Trois points de départ sont possibles, au choix. Votre `lampe_habillage_v002.blend`, comme ci-dessus. Si vous avez fait le défi procédural à la place de l'atelier du chapitre 3 : votre propre lampe, gardée dans la collection *Lampe*, par le même geste, ou la lampe habillée du chapitre 3 (`PRC02_ch3_lampe_habillage.zip`), décompressée, par le même geste. Sinon, le fichier de secours. Au bout de trois minutes de difficulté, passez au fichier de secours : votre lampe pourra être mise en scène plus tard, dans le même studio.

> [!WARNING]
> L'ampoule ne laisse plus voir le fond de la tête, alors qu'elle le faisait au chapitre 3 : c'est normal, et la suite de cette section l'explique. Dans la fenêtre d'*Append*, choisissez la collection, pas les objets un par un : les *Empty* `Grille_pivot` et `Interrupteur_pivot` arrivent avec elle, et la grille et les crans en dépendent.

### Trois façons de voir la même scène
Vous connaissez les quatre modes d'affichage depuis Basics 101. Trois d'entre eux montrent la lampe de façon de plus en plus fidèle :
- *Material Preview* : EEVEE calcule les matières sous une image d'environnement intégrée à Blender. Les lumières et le monde de la scène sont ignorés. C'est l'affichage du chapitre 3, pour juger une matière ;
- *Rendered* : le moteur de rendu actif, avec les lumières et le monde de la scène. Avec EEVEE, c'est déjà presque l'image finale, en temps réel ;
- le rendu final, avec `F12` : le même moteur, avec plus d'échantillons, à la taille de l'image de sortie.

Le chapitre 3 avait laissé deux cases de côté, dans le menu *Viewport Shading* (figure 3.3) : *Scene Lights* et *Scene World*. Cochées en *Material Preview*, elles remplacent l'image intégrée par les lumières et le monde de votre scène.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/shading_pie_menu_blender.jpg"
caption: "Figure 4.3 : Le menu circulaire des modes d'affichage, ouvert par Z dans la vue 3D : Wireframe, Solid, Material Preview et Rendered."
title: "Le menu circulaire Z"
---
`Z`, le pointeur dans la vue 3D, ouvre un menu circulaire : les quatre modes d'affichage, autour du pointeur.

Glissez vers le mode voulu, ou cliquez dessus. C'est plus rapide que les boutons en haut à droite de la vue.
```

![Figure 4.4 : La lampe en Material Preview. À gauche, Scene World décochée : l'image intégrée à Blender. À droite, Scene World cochée : le monde du studio, Monde_Studio, éclaire la lampe.](assets/images/material_preview_scene_world_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/rendered_popover_blender.jpg"
caption: "Figure 4.5 : Le menu Viewport Shading en mode Rendered : Scene Lights et Scene World sont cochées, et Render Pass choisit la passe affichée."
title: "Le menu Viewport Shading en Rendered"
---
En mode *Rendered*, le même menu montre *Scene Lights* et *Scene World* cochées : la vue utilise l'éclairage de la scène.

*Render Pass* reste sur *Combined*, l'image complète.
```

### EEVEE et Cycles
Blender propose deux moteurs de rendu. **EEVEE** calcule l'image comme un moteur de jeu vidéo, avec des approximations : il est fait pour le temps réel. **Cycles** suit le trajet de la lumière (*path tracing*) : c'est la référence physique, avec des ombres et une lumière indirecte plus justes, mais une image prend plus de temps.

Le programme vise le temps réel : la formation n'utilise qu'EEVEE. Cycles n'est montré qu'en image, pour comparer.

![Figure 4.6 : La même scène, de gauche à droite : Material Preview, EEVEE (64 échantillons, 1 s) et Cycles (128 échantillons, débruité : 3 s avec la carte graphique, 11 s sans elle). Sous Cycles, les ombres et la lumière renvoyée par le fond sont plus douces.](assets/images/engines_comparison_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/render_engine_menu_blender.jpg"
caption: "Figure 4.7 : L'onglet Render, menu Render Engine ouvert : EEVEE, Workbench et Cycles."
title: "Le menu Render Engine"
---
Le moteur se choisit en haut de l'onglet *Render* (l'appareil photo), dans *Render Engine*. Restez sur EEVEE.

Les temps de la figure 4.6 viennent d'un poste récent, sur une scène simple. Sur une scène lourde, ou sans carte graphique puissante, l'écart grandit.
```

### Recette · Trois affichages
- **1.** Le pointeur dans la vue 3D, `Z`, puis *Material Preview*.
- **2.** `Z`, puis *Rendered* : la lampe prend la lumière du studio.
- **3.** Repassez en *Material Preview*. Dans le menu *Viewport Shading*, cochez *Scene World*, regardez, puis décochez-la.
Contrôle : vous passez d'un affichage à l'autre avec `Z`, et vous savez dire lequel montre l'éclairage de la scène.

### Rendre une image : F12 et les emplacements
`F12` (*Render > Render Image*) calcule l'image finale dans une fenêtre de rendu. Le temps de calcul s'affiche en haut de l'image.

La fenêtre de rendu garde plusieurs **emplacements** (*Slot*). Choisissez un emplacement dans son en-tête avant `F12` : le rendu s'y range. `J` passe d'un emplacement à l'autre : c'est le moyen le plus simple de comparer deux réglages.

Fermez la fenêtre de rendu quand vous avez fini : elle se rouvre au prochain `F12`.

![Figure 4.8 : La fenêtre de rendu : le champ Slot dans l'en-tête, et le temps de calcul (Time) en haut à gauche de l'image.](assets/images/render_window_slots_blender.jpg)

### Le Raytracing, expliqué
Au chapitre 3, vous avez coché la case *Raytracing* de l'onglet *Render* pour que le verre laisse voir ce qui est derrière lui. Le chapitre 3 promettait de l'expliquer : la voici.

Sans *Raytracing*, EEVEE estime les reflets et les transparences d'après l'image d'environnement : un métal poli reflète un monde lointain, pas les pièces voisines. Avec *Raytracing*, EEVEE suit les rayons dans ce qu'il voit à l'écran (méthode *Screen-Trace*) : le chrome reflète la tête, la laque prend des reflets justes, et le verre laisse voir la douille. *Fast GI Approximation*, qui en dépend, améliore aussi la lumière renvoyée par le décor.

Ce réglage coûte du temps de calcul. Et il appartient à la scène, pas à la lampe : l'Append a apporté la lampe et ses matières, pas les réglages de rendu de votre fichier du chapitre 3. C'est pour cela que la case est décochée dans le studio.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/eevee_raytracing_panel_blender.jpg"
caption: "Figure 4.9 : L'onglet Render, rubrique Raytracing cochée : Method (Screen-Trace), Resolution, et la sous-rubrique Fast GI Approximation."
title: "La rubrique Raytracing"
---
La case est dans l'en-tête de la rubrique *Raytracing*. *Method* reste sur *Screen-Trace*.

*Fast GI Approximation* reste grisée tant que *Raytracing* est décochée.
```

![Figure 4.10 : Le banc d'essai, rendu avec F12. À gauche, Raytracing décoché : les bras et la sphère chromée du nuancier paraissent sombres. À droite, Raytracing coché : le métal reflète le studio et ses voisins.](assets/images/raytracing_off_on_blender.jpg)

> [!NOTE]
> **Rappel du chapitre 3 : le verre.** La matière du verre a sa case *Raytraced Transmission* cochée (onglet *Material*, rubrique *Settings*, figure 3.13) et *Thin Wall* coché (figure 3.14). Cela ne suffit pas : il faut aussi la case *Raytracing* de la scène.

### Les échantillons : Samples
La rubrique *Sampling* règle le nombre d'échantillons, c'est-à-dire le nombre de calculs moyennés pour chaque image :
- *Viewport > Samples* (16 par défaut) règle la fluidité de la vue en mode *Rendered* ;
- *Render > Samples* (64 par défaut) règle la qualité du rendu final.

Montez à 128 pour l'image finale, si votre poste le permet : le grain disparaît dans les ombres douces, mais le calcul double.

```side-by-side
layout: "textRight"
imagePath: "assets/images/eevee_sampling_panel_blender.jpg"
caption: "Figure 4.11 : L'onglet Render, rubrique Sampling : Viewport > Samples à 16 et Render > Samples à 128."
title: "La rubrique Sampling"
---
*Viewport* et *Render* ont chacun leur champ *Samples*.

Sur un poste lent, baissez *Viewport > Samples* à 8 : la vue reste fluide, et le rendu final ne change pas.
```

### Recette · Le banc d'essai
La caméra `CAM_banc_essai` du studio cadre la lampe et le nuancier.
- **1.** `F12`. Dans la fenêtre de rendu, l'emplacement 1 reçoit l'image, *Raytracing* décoché. Notez le temps.
- **2.** Onglet *Render* : cochez *Raytracing*.
- **3.** Dans la fenêtre de rendu, choisissez l'emplacement 2, puis `F12`.
- **4.** `J` : comparez le chrome, la laque et le verre.
- **5.** *Render > Samples* à 128, puis `F12` dans l'emplacement 3. Notez le temps.
Contrôle : deux emplacements montrent la lampe sans et avec *Raytracing*, et vous connaissez le temps de rendu de votre poste à 64 et à 128 échantillons.

### La transformation de vue
L'onglet *Render*, rubrique *Color Management*, règle la façon dont les lumières calculées deviennent des couleurs d'écran. Le menu *View* propose plusieurs transformations :
- *AgX*, par défaut : un rendu photographique, qui adoucit les hautes lumières, mais désature les couleurs vives ;
- *Standard* : aucune compression ; les hautes lumières saturent vite ;
- *Khronos PBR Neutral* : conçu pour restituer fidèlement la couleur de base d'un produit. C'est le choix pour vérifier une teinte CMF.

*Exposure* éclaircit ou assombrit l'image entière, comme le diaphragme d'un appareil photo.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/color_management_view_menu_blender.jpg"
caption: "Figure 4.12 : L'onglet Render, rubrique Color Management, menu View ouvert : AgX, Khronos PBR Neutral, Standard et les autres transformations."
title: "Le menu View"
---
Ouvrez la rubrique *Color Management*, en bas de l'onglet *Render*, puis le menu *View*.

*Look* et *Exposure*, juste en dessous, ajustent le contraste et la luminosité.
```

![Figure 4.13 : Le nuancier du studio, de gauche à droite en AgX, Standard et Khronos PBR Neutral. Le rouge CMF garde sa saturation en Khronos PBR Neutral ; AgX le pâlit, Standard brûle les reflets.](assets/images/view_transform_comparison_blender.jpg)

### Consignes · Régler son fichier
À vous, pour la suite de la séance :
- gardez *Raytracing* coché ;
- choisissez un nombre d'échantillons adapté à votre poste ;
- choisissez une transformation de vue, et sachez dire pourquoi ;
- enregistrez (`Ctrl + S`).
Contrôle : le banc d'essai rend une image nette, en quelques secondes. Corrigé : la ligne « Corrigé » de la partie 1 du LISEZ-MOI : *Raytracing* coché, *Render > Samples* à 128, *View* sur *Khronos PBR Neutral*.

> [!WARNING]
> Les rubriques de l'onglet *Render* sont repliées : dépliez-les une par une. Un verre qui ne laisse rien voir, *Raytracing* coché : sa matière n'a pas *Raytraced Transmission* (figure 3.13). Un poste lent : *Viewport > Samples* à 8, et des rendus d'essai à 50 % (*Resolution Scale*, onglet *Output*, section 3).

```quiz
question: "En Material Preview, les lumières de votre scène n'éclairent pas la lampe. Pourquoi ?"
options:
  - "Les lumières sont trop faibles"
  - "Ce mode utilise une image d'environnement intégrée : Scene Lights et Scene World sont décochées"
  - "Le moteur est réglé sur Cycles"
  - "La case Raytracing est décochée"
correctIndices:
  - 1
explanation: "Material Preview sert à juger les matières sous une image intégrée à Blender. Cochez Scene Lights et Scene World, ou passez en Rendered, pour voir l'éclairage de la scène."
```

```quiz
question: "Au chapitre 3, votre ampoule laissait voir le fond de la tête. Dans le studio, après l'Append, elle ne le fait plus. Pourquoi ?"
options:
  - "L'Append a abîmé la matière du verre"
  - "La case Thin Wall s'est décochée"
  - "La case Raytracing appartient à la scène : l'Append apporte la lampe et ses matières, pas les réglages de rendu"
  - "Le studio est réglé sur Cycles"
correctIndices:
  - 2
explanation: "Raytraced Transmission et Thin Wall sont dans la matière : elles suivent la lampe. Raytracing est un réglage de la scène, dans l'onglet Render : le studio a le sien, décoché."
```

```quiz
question: "Vous devez vérifier qu'un rouge correspond au nuancier CMF. Quelle transformation de vue choisissez-vous ?"
options:
  - "AgX"
  - "Standard"
  - "Khronos PBR Neutral"
  - "False Color"
correctIndices:
  - 2
explanation: "Khronos PBR Neutral restitue fidèlement la couleur de base d'un produit. AgX désature les couleurs vives et lumineuses ; Standard brûle vite les hautes lumières."
```

## 2. Éclairage de studio et HDRI

> [!NOTE]
> Cette section part des images d'environnement de *Material Preview* (chapitre 3), de la case *Scene World* et de `F12` (section 1), et des nœuds *Texture Coordinate* et *Mapping* (chapitre 3). Elle apporte le monde de la scène, l'HDRI, puis les lumières de studio, une notion à la fois.

### Une HDRI : la lumière d'un lieu
Une **HDRI** est une photographie panoramique à 360°, qui enregistre la vraie intensité de la lumière, du ciel le plus clair à l'ombre la plus sombre. Placée dans le monde de la scène (*World*), elle éclaire la lampe et se reflète dans ses surfaces brillantes. C'est la même idée que les images de *Material Preview*, mais dans votre scène : elle sert au rendu.

Le studio a quatre mondes prêts : `Monde_Studio`, `Monde_Interieur` et `Monde_Exterieur`, trois HDRI, et `Monde_Neutre`, un gris très sombre. C'est `Monde_Studio` qui éclairait vos rendus de la section 1.

![Figure 4.14 : La lampe sous les trois HDRI du studio : Monde_Studio, Monde_Interieur (rotation 135°) et Monde_Exterieur. Chaque lieu change la couleur de la lumière, les ombres et les reflets.](assets/images/hdri_comparison_blender.jpg)

### Le sélecteur de monde
L'onglet *World* (le globe rouge) montre le monde actif. Le sélecteur, en haut de l'onglet, liste les mondes du fichier : un clic en change.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/world_browse_menu_blender.jpg"
caption: "Figure 4.15 : L'onglet World, sélecteur de monde ouvert : Monde_Exterieur, Monde_Interieur, Monde_Neutre et Monde_Studio. La lettre F signale le Fake User, qui garde chaque monde dans le fichier."
title: "Le sélecteur de monde"
---
L'icône à gauche du nom ouvre la liste des mondes, comme la liste des matières du chapitre 3.

*New* crée un monde vide. Un monde créé par erreur ne fait rien perdre : les mondes du studio restent dans la liste.
```

### Mettre en place une HDRI
Dans l'onglet *World*, rubrique *Surface*, le champ *Color* reçoit l'image : le bouton à sa gauche ouvre un menu, *Environment Texture*, puis *Open* charge le fichier de l'HDRI. *Strength* règle son intensité.

Les mondes du studio sont déjà câblés : vous ne réglerez que leur rotation et leur intensité. Blender fournit aussi ses propres HDRI, dans son dossier d'installation (`datafiles\studiolights\world`) : ce sont les images de *Material Preview*.

```side-by-side
layout: "textRight"
imagePath: "assets/images/world_surface_hdri_blender.jpg"
caption: "Figure 4.16 : L'onglet World, rubrique Surface, sur Monde_Interieur, entrées Color et Vector dépliées : sous les réglages de l'image, le Mapping, avec Location, Rotation (Z à 135°) et Scale, puis Strength."
title: "La rubrique Surface"
---
La rubrique *Surface* déroule la chaîne des nœuds du monde. La flèche à gauche de *Color* déplie l'image ; celle de *Vector*, en dessous, déplie le *Mapping*, avec ses champs *Location*, *Rotation* et *Scale*.

*Rotation Z* fait tourner l'HDRI autour de la lampe. *Strength*, en bas, règle son intensité.
```

### Tourner l'HDRI : Mapping
La rotation Z du nœud *Mapping* place le reflet principal où vous le voulez : sur la tête, le long d'un bras. Le *Mapping* est celui du chapitre 3 : il étirait le bruit du brossé ; ici, il fait tourner l'image du monde.

Les nœuds du monde se lisent dans l'espace *Shading* : en haut du Shader Editor, passez le menu *Object* sur *World*.

![Figure 4.17 : Les nœuds de Monde_Interieur dans le Shader Editor, menu World : Texture Coordinate (Generated), Mapping (Rotation Z à 135°), Environment Texture, Background, puis World Output.](assets/images/world_nodes_hdri_blender.jpg)

> [!NOTE]
> **Les licences.** Les HDRI du studio sont sous licence CC0 : tout usage est permis, y compris commercial, sans attribution obligatoire. `studio.exr` est fournie avec Blender. `artist_workshop`, d'Oliksiy Yakovlyev, et `docklands_01`, de Savva Zakharov, viennent de Poly Haven (polyhaven.com), en définition 2K. Le placage de chêne du plateau de bureau, `oak_veneer_01`, vient aussi de Poly Haven, sous la même licence.

### Recette · Trois mondes, un reflet
- **1.** Onglet *World* : choisissez `Monde_Studio`, puis `F12` dans l'emplacement 1.
- **2.** `Monde_Interieur`, puis `F12` dans l'emplacement 2. `Monde_Exterieur`, puis `F12` dans l'emplacement 3.
- **3.** Comparez avec `J`.
- **4.** Gardez l'HDRI que vous préférez. Changez sa rotation Z, dans la rubrique *Surface*, jusqu'à placer le reflet principal sur la tête.
Contrôle : vous montrez la lampe sous deux mondes, dans deux emplacements, avec un reflet placé volontairement. Puis, à vous : choisissez l'ambiance de votre future vue de situation, son intensité et sa rotation. Corrigé : la ligne « Corrigé » de la partie 2 du LISEZ-MOI : `Monde_Interieur`, rotation Z à 135°.

> [!WARNING]
> La lampe disparaît dans une HDRI très claire : baissez *Strength*. En fond, une HDRI reste moins nette qu'une photographie : 2K pour l'intérieur et l'extérieur, 1K pour le studio. Pour la vue de situation, cadrez serré ou floutez le fond avec la profondeur de champ (section 3).

```quiz
question: "Votre HDRI place le reflet principal au mauvais endroit sur la tête. Que faites-vous ?"
options:
  - "Je déplace la lampe"
  - "Je tourne l'HDRI avec la rotation Z du Mapping"
  - "Je déplace la caméra"
  - "J'augmente Strength"
correctIndices:
  - 1
explanation: "La rotation Z du Mapping fait tourner le lieu autour de la lampe : le reflet glisse sans toucher au cadrage ni à la mise en place."
```

### Partir du noir
Un éclairage de studio se construit à partir du noir. `Monde_Neutre` est un monde gris très sombre : il éteint la lumière ambiante. Chaque lumière que vous ajoutez se voit alors seule, et vous savez ce qu'elle apporte.

### Les quatre types de lumière
*Add > Light* propose quatre lumières :
- *Point* : une ampoule nue, qui éclaire dans toutes les directions ;
- *Sun* : le soleil, des rayons parallèles, une ombre nette ;
- *Spot* : un cône de lumière, comme un projecteur ;
- *Area* : une surface lumineuse, comme une boîte à lumière (*softbox*). C'est la lumière du studio produit.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_light_menu_blender.jpg"
caption: "Figure 4.18 : Le sous-menu Add > Light (Maj + A dans la vue 3D) : Point, Sun, Spot et Area."
title: "Le sous-menu Add > Light"
---
`Maj + A` dans la vue 3D, puis *Light* : les quatre types.

La lumière apparaît au curseur 3D. Placez-la ensuite avec `G`, et orientez-la avec `R`.
```

![Figure 4.19 : La lampe éclairée par une seule lumière, sur Monde_Neutre : Point, Sun, Spot, puis Area. L'Area donne l'ombre la plus douce et les reflets les plus larges.](assets/images/light_types_comparison_blender.jpg)

### Les réglages d'une lumière
L'onglet *Light* (l'ampoule verte) règle la lumière sélectionnée :
- *Power*, en watts : sa puissance (*Strength* pour *Sun*). Une *Area* neuve fait 10 W ;
- *Color*, ou *Temperature* en kelvins : cochez la case *Temperature*, décochée par défaut, puis réglez la valeur. 2700 K est chaud, comme une ampoule ; 6500 K est froid, comme un ciel couvert ;
- *Shape* et *Size*, pour une *Area* : sa forme et sa taille. Plus la source est grande, plus l'ombre et le reflet sont doux.

```side-by-side
layout: "textRight"
imagePath: "assets/images/light_properties_area_blender.jpg"
caption: "Figure 4.20 : L'onglet Light d'une Area : la case Temperature cochée et sa valeur, Power, puis Shape et Size."
title: "L'onglet Light"
---
La case *Temperature* active le réglage en kelvins ; décochée, c'est *Color* qui compte.

Une *Area* neuve mesure 1 m de côté. Pour une lampe de 450 mm, une source de 300 à 800 mm convient.
```

![Figure 4.21 : Une Area de même puissance, petite (50 mm) puis grande (1500 mm) : l'ombre portée s'adoucit et le reflet sur la tête s'élargit.](assets/images/area_size_comparison_blender.jpg)

### Recette · La principale
- **1.** Onglet *World* : `Monde_Neutre`. Passez la vue en *Rendered*.
- **2.** *Add > Light > Area*. Renommez-la `Key` (`F2`).
- **3.** Placez-la à 45° environ, au-dessus de la lampe et sur le côté, puis orientez-la vers la lampe avec `R`.
- **4.** Cochez *Temperature*. Essayez deux tailles et deux températures, par exemple *Size* `300mm` puis `800mm`, 5500 K puis 4500 K. Ajustez *Power* : environ 20 W.
Contrôle : `Key` modèle les volumes de la tête ; ni blanc brûlé, ni ombre bouchée. Corrigé : `Key_corrige`, dans la collection « Corrigé éclairage ».

### L'éclairage en trois points
Le studio photo classique utilise trois lumières :
- la principale (*key*), à 45° environ, au-dessus et sur le côté : elle modèle les volumes ;
- la secondaire (*fill*), du côté opposé, plus faible et plus grande : elle débouche les ombres ;
- le contre-jour (*rim*), derrière l'objet : il dessine le contour et détache la silhouette du fond.

Un rapport de 3 à 4 entre la principale et la secondaire est un bon départ, pas une règle.

### Trois lumières, vues de dessus
Vue de dessus (`7` du pavé numérique), les trois lumières entourent la lampe : la principale d'un côté, la secondaire de l'autre, le contre-jour derrière.

La ligne qui part de chaque lumière indique sa direction.

![Figure 4.22 : Vue de dessus du corrigé : Key à gauche, devant ; Fill à droite ; Rim derrière la lampe. La ligne qui part de chaque lumière montre sa direction.](assets/images/three_point_lighting_top_blender.jpg)

![Figure 4.23 : L'éclairage en trois points, pas à pas : Key seule, puis Key et Fill, puis les trois. Rim dessine un liseré clair sur le contour de la tête.](assets/images/three_point_steps_blender.jpg)

### Recette · Le studio en trois lumières
- **1.** Ajoutez une *Area* `Fill`, du côté opposé à `Key`, avec environ un tiers de sa puissance et une taille plus grande.
- **2.** Ajoutez une *Area* `Rim`, derrière et au-dessus de la lampe, jusqu'à voir un liseré clair sur le contour de la tête.
- **3.** Sélectionnez les trois lumières, puis `M > New Collection` : `Eclairage_studio`.
- **4.** Dans l'Outliner, fermez l'œil de deux lumières : regardez le rôle de la troisième. Puis rallumez les trois.
Contrôle : en *Rendered*, la silhouette de la lampe se détache du fond, et l'Outliner montre `Eclairage_studio` avec `Key`, `Fill` et `Rim`. Corrigé : la collection « Corrigé éclairage », avec `Monde_Neutre`.

```side-by-side
layout: "textRight"
imagePath: "assets/images/outliner_lights_collection_blender.jpg"
caption: "Figure 4.24 : L'Outliner : la collection Eclairage_studio et ses trois lumières, chacune avec son œil et son appareil photo."
title: "La collection Eclairage_studio"
---
L'œil masque une lumière dans la vue 3D. L'appareil photo l'ôte du rendu `F12`. C'est la distinction de Basics 101.

Ranger les lumières dans une collection permet de toutes les éteindre d'un clic, pour la vue de situation.
```

### Les lignes de reflet
Une *Area* longue et fine (*Shape* sur *Rectangle*) trace une ligne de lumière sur une surface brillante : ici, la tête laquée. C'est le geste du studio automobile sur une carrosserie ; on le retrouve sur un fuselage ou sur la caisse d'un train.

![Figure 4.25 : La tête laquée, sans puis avec une Area Rectangle de 1000 × 60 mm placée au-dessus : une ligne de lumière suit la forme de la tête.](assets/images/strip_light_reflection_blender.jpg)

### Consignes · Combiner
À vous :
- revenez sur `Monde_Studio`, avec une *Strength* de 0,3, lumières allumées, puis comparez avec `Monde_Neutre` ;
- gardez la combinaison que vous préférez pour la vue héros ;
- ★ une *Area* *Rectangle* longue, pour une ligne de reflet sur la tête ; une principale à 4500 K et un contre-jour à 7000 K.
Contrôle : la vue héros a son éclairage. Corrigé : `Reflet_bande_corrige`, dans la collection « Corrigé éclairage ».

> [!WARNING]
> Une lumière qui n'éclaire rien : elle pointe ailleurs ; suivez la ligne qui indique sa direction. La température ne change rien : la case *Temperature* n'est pas cochée. Tout est blanc ou tout est noir : un *Power* dix fois trop fort ou trop faible ; les valeurs dépendent de la distance, et la lampe mesure 450 mm. Le studio paraît plat : la secondaire est aussi forte que la principale. Une lumière masquée par l'œil éclaire encore au rendu `F12` : fermez aussi son appareil photo.

> [!NOTE]
> **Ailleurs.** Les mêmes gestes éclairent un siège de train, un rétroviseur ou une liseuse de cabine d'avion. Un studio automobile aligne de longues *Area* au-dessus de la voiture pour dessiner ses lignes ; un fuselage en maquette se lit mieux avec un contre-jour franc.

```quiz
question: "Dans un éclairage en trois points, quel est le rôle du contre-jour (rim) ?"
options:
  - "Éclairer la face avant de l'objet"
  - "Déboucher les ombres"
  - "Dessiner le contour et détacher la silhouette du fond"
  - "Colorer le fond"
correctIndices:
  - 2
explanation: "Le contre-jour, placé derrière l'objet, dessine un liseré clair sur son contour : la silhouette se détache du fond. La principale modèle les volumes, la secondaire débouche les ombres."
```

```quiz
question: "Pour adoucir l'ombre portée par une Area, que modifiez-vous ?"
options:
  - "Sa puissance (Power)"
  - "Sa taille (Size)"
  - "Sa température (Temperature)"
  - "Le nombre d'échantillons"
correctIndices:
  - 1
explanation: "Plus la source est grande, plus l'ombre et le reflet sont doux. La puissance change la quantité de lumière, pas la douceur de l'ombre."
```

## 3. Caméra, composition et export

> [!NOTE]
> Cette section part de la vue à travers la caméra active, `0` du pavé numérique (Basics 101), des objets *Empty* (chapitre 2), de la barre latérale `N` et du *Clip Start* de la vue (chapitre 1), de `F12` (section 1) et de la focale de 50 mm, vue à l'initiation. Elle apporte la mise en place d'une caméra, la focale, la composition, la profondeur de champ, le format de sortie et l'enregistrement de l'image.

### Placer une caméra
*Add > Camera* ajoute une caméra. `0` du pavé numérique montre la vue à travers la caméra active. Deux gestes évitent de la placer à la main :
- *View > Align View > Align Active Camera to View* (`Ctrl + Alt + 0` du pavé numérique) amène la caméra active sur votre point de vue ;
- *Lock Camera to View*, dans la barre latérale (`N`), onglet *View*, rubrique *View Lock* : tant que la case est cochée, naviguer déplace la caméra. On cadre ainsi en naviguant.

Avec plusieurs caméras, *View > Cameras > Set Active Object as Camera* (`Ctrl + 0` du pavé numérique) fait de la caméra sélectionnée la caméra active. Nommez-les : `CAM_heros`, `CAM_detail`, `CAM_situation`.

![Figure 4.26 : Deux menus de la vue 3D. À gauche, View > Cameras : Set Active Object as Camera (Ctrl + 0 du pavé) et Active Camera. À droite, View > Align View : Align Active Camera to View (Ctrl + Alt + 0 du pavé).](assets/images/view_cameras_align_menus_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/sidebar_view_lock_camera_blender.jpg"
caption: "Figure 4.27 : La barre latérale (N), onglet View, rubrique View Lock : la case Lock Camera to View cochée."
title: "Lock Camera to View"
---
Cochez *Lock Camera to View*, cadrez en naviguant, puis décochez dès que le cadrage est bon.

Tant que la case est cochée, un coup d'orbite défait le cadrage.
```

### La focale
La focale (*Focal Length*, onglet *Camera*, rubrique *Lens*) règle l'angle de vue. Au-delà des 50 mm d'usine :
- une courte focale, 24 mm, exagère la perspective et déforme les proportions ;
- une longue focale, 85 à 100 mm, avec du recul, restitue des proportions fidèles : c'est la focale de la photo de produit ;
- une caméra de *Type* *Orthographic* supprime la perspective : c'est la vue technique.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/camera_lens_panel_blender.jpg"
caption: "Figure 4.28 : L'onglet Camera, rubrique Lens : Type, Focal Length à 85 mm, puis Clip Start et End."
title: "La rubrique Lens"
---
*Focal Length* se règle en millimètres : tapez `85mm`. *Type* passe la caméra en *Orthographic*.

*Clip Start* vaut 100 mm : un objet plus proche de la caméra est coupé.
```

![Figure 4.29 : La même lampe, cadrée à la même taille avec 24, 50 puis 100 mm, la caméra reculant à chaque fois. À 24 mm, la tête paraît énorme et le socle petit ; à 100 mm, les proportions sont celles du dessin.](assets/images/focal_length_comparison_blender.jpg)

### La composition
L'onglet *Camera*, rubrique *Viewport Display*, aide à composer :
- *Composition Guides* trace des repères dans le cadre : *Thirds* (les tiers), *Center*, *Diagonal*, *Golden Ratio* ;
- *Passepartout* assombrit tout ce qui sort du cadre.

La règle des tiers place le sujet principal, ici la tête de la lampe, sur l'un des quatre points forts où les lignes se croisent.

```side-by-side
layout: "textRight"
imagePath: "assets/images/composition_guides_panel_blender.jpg"
caption: "Figure 4.30 : L'onglet Camera, rubrique Viewport Display : Passepartout coché, et la sous-rubrique Composition Guides, avec Thirds coché."
title: "Composition Guides"
---
Dépliez *Viewport Display*, puis *Composition Guides*, et cochez *Thirds*.

Les guides ne s'affichent qu'en vue caméra, et jamais au rendu.
```

![Figure 4.31 : La vue à travers CAM_heros, guides Thirds et Passepartout : la tête de la lampe sur le point fort en haut à droite.](assets/images/camera_view_thirds_blender.jpg)

### Recette · La vue héros
- **1.** *Add > Camera*. Renommez-la `CAM_heros`, puis `Ctrl + 0` du pavé numérique pour la rendre active.
- **2.** *Focal Length* : `85mm`.
- **3.** Naviguez jusqu'à une vue de trois quarts avant, un peu au-dessus de la lampe. *View > Align View > Align Active Camera to View*.
- **4.** Cochez *Lock Camera to View*, affinez le cadrage en naviguant, puis décochez.
- **5.** *Composition Guides > Thirds* : la tête sur un point fort.
Contrôle : en vue caméra, la lampe entière, câble compris, tient dans le cadre, la tête sur un point fort. Corrigé : `CAM_heros_corrige`, dans la collection « Corrigé caméras ».

### La profondeur de champ
Une vraie photo n'est nette qu'à une certaine distance : c'est la profondeur de champ. Elle attire le regard sur un détail. Dans l'onglet *Camera*, rubrique *Depth of Field* :
- *Focus on Object* désigne l'objet sur lequel faire la mise au point : un *Empty* posé sur le détail, ou une pièce de la lampe ;
- *F-Stop*, dans la sous-rubrique *Aperture*, règle le flou : plus le nombre est petit, plus le fond est flou.

En gros plan, la zone nette ne mesure que quelques millimètres : partez de 5,6 à 8. L'effet n'est crédible que si la scène est à l'échelle réelle, ce qui est le cas de la lampe.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/camera_dof_panel_blender.jpg"
caption: "Figure 4.32 : L'onglet Camera, rubrique Depth of Field cochée : Focus on Object (l'Empty Mise_au_point), puis Aperture et F-Stop à 8."
title: "La rubrique Depth of Field"
---
Cochez la case de la rubrique, puis choisissez l'objet de la mise au point dans *Focus on Object*.

Sans objet, c'est *Focus Distance* qui compte : une distance en millimètres depuis la caméra.
```

![Figure 4.33 : La vue de détail du corrigé, mise au point sur l'interrupteur. À gauche, F-Stop 1,4 : seuls quelques crans sont nets. À droite, F-Stop 8 : l'interrupteur est net, l'articulation et le bras restent flous.](assets/images/dof_comparison_blender.jpg)

### Le format de sortie
L'onglet *Output* (l'imprimante), rubrique *Format*, règle l'image produite par `F12` :
- *Resolution X* et *Y* : la taille, en pixels ;
- *%* : une réduction, pour des essais rapides ;
- le bouton des préréglages, à droite du titre, propose des formats courants.

Le ratio suit l'usage : 16:9 pour une diapositive (1920 × 1080), 1:1 pour un réseau social (1080 × 1080), un format A4 pour une impression.

```side-by-side
layout: "textRight"
imagePath: "assets/images/output_format_panel_blender.jpg"
caption: "Figure 4.34 : L'onglet Output, rubrique Format : Resolution X et Y, le pourcentage, le rapport des pixels et la cadence."
title: "La rubrique Format"
---
La résolution appartient à la scène, pas à la caméra : changez-la avant de rendre une caméra d'un autre format, puis remettez-la.

Le pourcentage (*%*) réduit l'image sans toucher à la résolution.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/format_presets_menu_blender.jpg"
caption: "Figure 4.35 : Le bouton des préréglages de la rubrique Format, ouvert : HDTV 1080p, HDTV 720p, 4K DCI, et les autres formats courants."
title: "Les préréglages de format"
---
Le bouton à droite du titre *Format* ouvre la liste des préréglages. *HDTV 1080p* donne 1920 × 1080.

Pour un carré, tapez simplement 1080 dans *Resolution X* et *Y*.
```

### Rendre et enregistrer
`F12` calcule l'image, mais n'enregistre rien sur le disque. Pour garder l'image : dans la fenêtre de rendu, *Image > Save As* (`Maj + Alt + S`). Dans la fenêtre d'enregistrement, réglez :
- *File Format* : *PNG* ;
- *Color* : *RGB*, ou *RGBA* pour un fond transparent ;
- *Color Depth* : 8 ;
- *Color Management* sur *Follow Scene*, la valeur par défaut : l'image garde la transformation de vue de la scène, comme à l'écran.

Pour un PNG sans fond, à poser sur une diapositive : cochez *Transparent*, dans l'onglet *Render*, rubrique *Film*, puis enregistrez en *RGBA*.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/render_menu_blender.jpg"
caption: "Figure 4.36 : Le menu Render de la barre du haut : Render Image (F12), Render Animation, View Render (F11)."
title: "Le menu Render"
---
*Render Image* est le même geste que `F12`. *View Render* (`F11`) rouvre la fenêtre de rendu, avec le dernier rendu.

*Render Animation* rend une suite d'images : il sert à l'un des défis.
```

![Figure 4.37 : La fenêtre Save As de l'image rendue : à droite, File Format (PNG), Color (RGB), Color Depth (8), puis la rubrique Color Management sur Follow Scene : Display, View (Khronos PBR Neutral) et Look suivent la scène. Le chemin du poste est flouté.](assets/images/image_save_as_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/eevee_film_panel_blender.jpg"
caption: "Figure 4.38 : L'onglet Render, rubrique Film : Filter Size et la case Transparent."
title: "Un fond transparent"
---
*Transparent* remplace le fond par la transparence, au rendu. Le monde éclaire toujours la lampe.

Enregistrez alors en *RGBA* : en *RGB*, la transparence serait perdue.
```

### Recette · Le détail et le premier export
- **1.** *Add > Camera* : `CAM_detail`, *Focal Length* `100mm`, sur un détail : l'interrupteur cranté et la grille d'aération, une articulation, ou l'ampoule dans la tête.
- **2.** *Add > Empty > Plain Axes* : `Mise_au_point`, posé sur ce détail. Rubrique *Depth of Field* de `CAM_detail` : cochez-la, *Focus on Object* `Mise_au_point`, *F-Stop* entre 5,6 et 8.
- **3.** Masquez la collection *Nuancier* (œil et appareil photo) : elle entre dans le cadre de la vue héros.
- **4.** `CAM_heros` active (`Ctrl + 0`). Vérifiez le format : 1920 × 1080. `F12`.
- **5.** *Image > Save As* : dossier `rendus`, à côté de votre fichier, nom `lampe_heros_<initiales>_v001.png`, *PNG*, *Color Management* sur *Follow Scene*.
- **6.** Ouvrez l'image dans l'Explorateur de Windows : elle doit être identique au rendu.
Contrôle : `CAM_heros` et `CAM_detail` existent, et un PNG bien nommé est dans `rendus`. Corrigé : `CAM_detail_corrige` et `Mise_au_point_corrige`, dans la collection « Corrigé caméras », et l'image `PRC02_ch4_corrige_heros.png`.

### Consignes · La vue de détail
À vous :
- rendez `CAM_detail` active ;
- passez la résolution à 1080 × 1080 ;
- rendez, puis enregistrez `rendus/lampe_detail_<initiales>_v001.png`.
Contrôle : deux PNG dans `rendus`, au bon nom et au bon format. Corrigé : l'image `PRC02_ch4_corrige_detail.png`.

> [!WARNING]
> La vue de détail sort en 16:9 : la résolution n'a pas été changée ; elle appartient à la scène. Un PNG aux couleurs différentes du rendu : la rubrique *Color Management* de la fenêtre d'enregistrement est passée sur *Override* ; remettez *Follow Scene*. Une profondeur de champ sans effet : *Focus on Object* est vide, ou la mise au point tombe sur le fond. Le détail lui-même est flou : *F-Stop* trop petit pour un gros plan ; remontez vers 8. Un détail coupé net par un plan invisible : la caméra est à moins de 100 mm de l'objet (*Clip Start*, figure 4.28) ; reculez-la et allongez la focale.

```quiz
question: "Pour une vue produit fidèle aux proportions du dessin, quelle focale privilégiez-vous ?"
options:
  - "Une courte focale, 24 mm, près de l'objet"
  - "La focale d'usine, 50 mm"
  - "Une longue focale, 85 à 100 mm, avec du recul"
  - "Peu importe : la focale ne change que le cadrage"
correctIndices:
  - 2
explanation: "Avec du recul, une longue focale écrase peu la perspective : les proportions restent celles du dessin. Une courte focale près de l'objet grossit ce qui est proche."
```

```quiz
question: "Votre rendu F12 est terminé. Est-il enregistré sur le disque ?"
options:
  - "Oui, dans le dossier du fichier .blend"
  - "Oui, dans le dossier rendus"
  - "Non : il faut Image > Save As dans la fenêtre de rendu"
  - "Non : il faut File > Export"
correctIndices:
  - 2
explanation: "F12 calcule l'image dans la fenêtre de rendu, sans l'enregistrer. Image > Save As (Maj + Alt + S) l'écrit sur le disque ; Color Management, sur Follow Scene, garde la transformation de vue de la scène."
```

```quiz
question: "Vous voulez un PNG sans fond, à poser sur une diapositive. Que réglez-vous ?"
options:
  - "Film > Transparent dans l'onglet Render, puis RGBA à l'enregistrement"
  - "Monde_Neutre comme monde"
  - "Strength du monde à 0"
  - "Color Depth à 16"
correctIndices:
  - 0
explanation: "Film > Transparent remplace le fond par la transparence ; seul le format RGBA la garde dans le PNG. Le monde continue d'éclairer la lampe."
```

## 4. Atelier : concept final

> [!NOTE]
> L'atelier n'apporte aucune notion nouvelle : il réinvestit les sections 1 à 3, *Pack Resources* (Basics 102) et, pour les paliers, *File > Append* et la liste des matières (chapitre 3). Comptez environ 40 minutes, puis la galerie et le bilan de la formation.

### La situation
Revue de design demain matin. Vous présentez votre concept de lampe au client en trois visuels : ils doivent faire comprendre la forme, les matières et l'usage.

Le cadre se transpose à chaque secteur : la revue d'un siège ferroviaire, d'un rétroviseur automobile ou d'une liseuse de cabine d'avion se prépare de la même façon.

### Les livrables
Trois images et un fichier :
- **V1 · Héros :** `CAM_heros`, la lampe entière en trois quarts avant, en studio, 1920 × 1080 : `lampe_heros_<initiales>_v001.png` ;
- **V2 · Détail :** `CAM_detail`, un gros plan avec profondeur de champ, 1080 × 1080 : `lampe_detail_<initiales>_v001.png` ;
- **V3 · Situation :** `CAM_situation`, la lampe dans son usage, sur le plateau de bureau, sous une HDRI, 1920 × 1080 : `lampe_situation_<initiales>_v001.png` ;
- le fichier de scène `lampe_rendu_v001.blend`, ressources empaquetées (*File > External Data > Pack Resources*).

Les noms suivent une convention : `<objet>_<vue>_<initiales>_v<version>.png`, en minuscules, sans accent ni espace, les initiales en majuscules. Exemple : `lampe_heros_MJ_v001.png`. Les images vont dans `rendus`, à côté du fichier, puis dans le dossier de la galerie que le formateur indique.

### Consignes · Le concept final, par paliers
- **Lumière.** Réglez la lumière définitive de la vue héros et du détail.
- **Situation.** Rendez visible la collection *Mise_en_situation* (œil et appareil photo), masquez *Studio* et *Nuancier*, choisissez une HDRI d'intérieur ou d'extérieur, éteignez `Eclairage_studio` si besoin. Créez `CAM_situation`, par exemple à 35 mm, à hauteur d'yeux d'une personne assise. Le plateau est en chêne plaqué, posé en projection *Box* comme les finitions du chapitre 3 : sélectionnez-le, puis ouvrez le *Shader Editor* pour lire sa matière.
- **Socle.** Les trois vues exportées et bien nommées ; le fichier empaqueté, puis enregistré.
- **★** Une version de la vue héros à fond transparent (*Film > Transparent*, *RGBA*). Une vue technique de profil, avec une caméra *Orthographic* face à la lampe et `Monde_Neutre`. La gamme : *File > Append* de la collection `Lampe_coloris_B` de `lampe_habillage_v002.blend` (dans le fichier de secours, elle est déjà là : ouvrez son œil et son appareil photo), puis une caméra `CAM_gamme` qui cadre les deux lampes : `lampe_gamme_<initiales>_v001.png`.
- **★★** La lampe allumée pour la vue de situation : un *Spot* dans la tête, *Temperature* à 2700 K, `Eclairage_studio` éteint ; sur l'ampoule, la matière fournie `Ampoule_allumee`, choisie dans la liste des matières (figure 3.6). Ou le même studio pour un autre objet : la liseuse de cabine du chapitre 2, la maquette en kit ou la rangée de sièges de l'initiation.
- **Dépôt.** Copiez vos trois PNG dans le dossier de la galerie.
Avant d'envoyer : nuancier masqué, bonne résolution pour chaque vue, noms vérifiés. Corrigé : `CAM_situation_corrige` (« Corrigé caméras »), la collection « Corrigé paliers » et les images du corrigé.

![Figure 4.39 : La vue de situation du corrigé : le plateau de bureau en chêne plaqué, le carnet et la lampe, sous Monde_Interieur (rotation 135°), vus par CAM_situation_corrige à 35 mm. Le studio et ses lumières sont masqués.](assets/images/atelier_situation_blender.jpg)

![Figure 4.40 : Les paliers du corrigé. À gauche, ★ la vue technique, caméra Orthographic ; au milieu, ★ la gamme, les deux coloris côte à côte ; à droite, ★★ la lampe allumée, un Spot de 2700 K dans la tête, sous Monde_Interieur très baissé.](assets/images/atelier_paliers_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/spot_light_panel_blender.jpg"
caption: "Figure 4.41 : L'onglet Light d'un Spot : Temperature à 2700 K, Power, Radius, puis la rubrique Beam Shape avec Angle et Blend."
title: "Palier ★★ : le Spot de la lampe"
---
Un *Spot* se règle comme une *Area* : *Temperature*, puis *Power*, environ 12 W. Placez-le dans la tête, devant l'ampoule, tourné comme la tête.

*Angle* et *Blend*, dans la rubrique *Beam Shape*, règlent l'ouverture et le bord du cône : c'est un défi, ci-dessous.
```

```resource
title: "Les images du corrigé"
description: "Les visuels attendus, en PNG : la vue héros (1920 × 1080), le détail (1080 × 1080), la situation (1920 × 1080), la variante lampe allumée du palier ★★, et l'image comparative Material Preview, EEVEE et Cycles de la section 1."
fileName: "PRC02_ch4_images_corrige.zip (8.8 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch4_images_corrige.zip"
```

> [!WARNING]
> Le nuancier apparaît dans un visuel : fermez l'œil et l'appareil photo de sa collection. Un sol qui scintille sous le plateau de bureau : la collection *Studio* est restée visible. Au palier ★, `ABS_Noir.001` apparaît après l'Append du coloris B : c'est une copie des matières partagées par les deux coloris, sans effet sur le rendu. Perdu à la fin de la section 3 ? Ouvrez le fichier de secours, enregistrez-le sous `lampe_rendu_v001.blend`, rendez visibles « Corrigé éclairage » et « Corrigé caméras », puis suivez les lignes « Corrigé » du LISEZ-MOI.

```quiz
question: "Avant d'envoyer vos visuels, que vérifiez-vous ? Plusieurs réponses sont justes."
options:
  - "Le nom de chaque fichier, selon la convention"
  - "La résolution de chaque vue"
  - "Color Management sur Follow Scene à l'enregistrement"
  - "Une focale de 50 mm sur toutes les vues"
  - "Le fichier .blend empaqueté"
correctIndices:
  - 0
  - 1
  - 2
  - 4
explanation: "Les noms, les formats, la gestion des couleurs à l'enregistrement et l'empaquetage rendent la livraison exploitable. La focale se choisit vue par vue : 85 à 100 mm pour la vue héros et le détail, plus courte pour la situation."
```

### Galerie et restitution
Chacun dépose ses visuels dans le dossier de la galerie. Le formateur les projette : d'abord les vues héros, sans commentaire.

Chacun commente ensuite sa vue de situation, ou sa vue préférée, en une minute : un choix de lumière, un choix de cadrage. Le groupe pose une question au plus. Pour finir, chacun colle un post-it vert sur le visuel d'un autre.

### Bilan de la formation
**Les six demi-journées.** Le formateur projette une vignette par demi-journée ; pour chacune, le groupe nomme un geste clé :
- prendre ses repères : la maquette en kit ;
- modéliser : la rangée de sièges et la clinique du fichier ;
- chapitre 1 : le blocage de la lampe ;
- chapitre 2 : la lampe remodelée, avec ses modificateurs et ses courbes ;
- chapitre 3 : la lampe habillée, ses matières rangées en bibliothèque ;
- chapitre 4 : un visuel de la galerie.

**Pour continuer :**
- cette application : les chapitres, les quiz et les défis ;
- les fichiers de la formation : chaque LISEZ-MOI garde ses consignes par paliers, et les collections « Corrigé » montrent le résultat attendu ;
- votre bibliothèque CMF du chapitre 3 et le studio de ce chapitre, à réutiliser pour vos projets ;
- Poly Haven, pour des HDRI et des textures sous licence CC0 ;
- le manuel officiel de Blender, en anglais, avec les mêmes libellés que l'interface.

**Questions.** Le temps qui reste sert à vos questions. Pour finir, chacun dit en une phrase ce qu'il appliquera dès la semaine prochaine.

### Pour ceux qui avancent vite
Les défis suivants apportent une notion nouvelle. Le LISEZ-MOI du studio donne leur chemin dans l'interface :
- **le Spot réglé finement :** *Angle* et *Blend*, rubrique *Beam Shape* (figure 4.41), pour un cône de lumière net ou doux sur le plateau ;
- **votre propre ampoule allumée :** la rubrique *Emission* de la matière (figure 3.15), au lieu de la matière fournie ;
- **l'éclat de l'ampoule :** un nœud *Glare*, de type *Bloom*, dans le compositeur ;
- **toutes les vues en un seul lancement :** un marqueur par caméra dans la *Timeline*, *Marker > Bind Camera to Markers*, le chemin de sortie de l'onglet *Output*, puis *Render > Render Animation* ;
- **des lumières qui suivent la lampe :** une contrainte *Damped Track* vers un *Empty* ;
- **le studio en bibliothèque :** ranger le studio et ses lumières en actifs, comme les matières du chapitre 3, pour les réutiliser d'un projet à l'autre.
