## 1. Modificateurs : symétrie, épaisseur, répétition

> [!NOTE]
> Ce chapitre part du principe que vous savez passer en Mode Édition, ajouter un modificateur et le régler. Si besoin, Basics 103 (section 3) reprend la pile de modificateurs pas à pas. Le chapitre 1 a présenté la saisie d'une valeur avec son unité, l'aimantation et l'orientation *Local* : ils servent ici sans être redits. Les captures et les libellés correspondent à Blender 5.2 LTS, avec l'interface en anglais.

### Du blocage au modèle
Au chapitre 1, vous avez arrêté les proportions de la lampe de bureau avec des volumes simples. Dans ce chapitre, chaque volume devient une pièce propre : un bras à deux tiges, un abat-jour en coque, une grille d'aération, un câble, une ampoule.

La méthode est **non destructive** : chaque décision reste modifiable. L'épaisseur de l'abat-jour, le nombre de lamelles ou le tracé du câble sont des réglages, pas des formes figées. Si le client demande une retouche, vous changez une valeur, sans rien reconstruire.

> [!IMPORTANT]
> **La règle du chapitre : n'appliquez aucun modificateur.** Un modificateur appliqué transforme son résultat en géométrie figée. Gardez-les actifs jusqu'au chapitre 4 : le chapitre 3 pose ses matières sur les pièces telles quelles.

```resource
title: "Fichier d'exercice : la lampe, du blocage au modèle"
description: "Le fichier de travail du chapitre : le blocage du chapitre 1 en gabarit, une copie de travail par volume, les croquis, et le texte LISEZ-MOI avec les consignes de chaque partie. Les corrigés sont dans les collections masquées « Corrigé » et « Corrigé défis ». Enregistrez-le sous lampe_modele_v001.blend avant de commencer."
fileName: "PRC02_ch2_lampe_depart.blend (0.3 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch2_lampe_depart.blend"
```

### Recette · Prendre le fichier en main
Ce fichier ne demande aucun travail préalable : il remplace votre blocage du chapitre 1. Si vous préférez garder le vôtre, c'est possible ; les valeurs données deviennent alors indicatives.
- **1.** Ouvrez `PRC02_ch2_lampe_depart.blend`, puis enregistrez-le aussitôt sous `lampe_modele_v001.blend` (*File > Save As*). Le fichier de départ reste intact.
- **2.** Repérez les collections dans l'Outliner : *Gabarit*, le blocage en fil de fer, non sélectionnable ; *Lampe*, vos pièces, une par volume ; *Croquis*, les images de référence.
- **3.** Les corrigés sont rangés dans les collections *Corrigé* et *Corrigé défis*, masquées : cliquez sur leur œil pour les afficher.
- **4.** Le texte LISEZ-MOI, en bas de l'écran, résume chaque partie. `Ctrl + Espace` au-dessus de lui l'agrandit.
- **5.** Faites `Ctrl + S` à chaque contrôle.
Le fichier affiche des millimètres. Toutes les valeurs du chapitre sont indicatives : adaptez-les à votre concept.

![Figure 2.1 : Le fichier de départ : le gabarit du chapitre 1 en fil de fer, et la copie de travail en volume, une pièce par volume.](assets/images/gabarit_wire_lamp_blender.jpg)

> [!TIP]
> Une pièce vous manque, ou vous avez pris du retard ? Prenez-la dans la collection *Corrigé* : supprimez votre version, sélectionnez la pièce corrigée, faites `M` vers *Lampe*, puis renommez-la sans `_corrige`. Une pièce qui a un *Empty* se déplace avec lui.

### La pile de modificateurs
Un modificateur transforme l'affichage d'un objet sans toucher à sa géométrie. Ils s'ajoutent dans l'éditeur de propriétés, onglet *Modifiers* (la clé), avec *Add Modifier*. Ce chapitre utilise surtout le sous-menu *Generate* : *Mirror*, *Solidify*, *Bevel*, *Array (Legacy)* et *Screw*.

Les modificateurs d'un objet forment une pile. Blender la calcule de haut en bas : chacun travaille sur le résultat du précédent. Dans ce chapitre, l'ordre se règle presque toujours tout seul ; vous le verrez en remarque avec l'abat-jour.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_modifier_generate_menu_blender.jpg"
caption: "Figure 2.2 : Le sous-menu Generate du menu Add Modifier, présenté ici en deux colonnes."
title: "Le sous-menu Generate"
---
Les modificateurs qui créent de la géométrie sont rangés dans *Add Modifier > Generate*. Le menu s'ouvre sur sa liste complète : tapez les premières lettres d'un nom pour le trouver plus vite.

Deux entrées portent le nom *Array* : ce chapitre utilise *Array (Legacy)*, le modificateur classique (partie Répétition).
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/modifier_header_menu_blender.jpg"
caption: "Figure 2.3 : Le menu de l'en-tête d'un modificateur : Apply, Duplicate, Copy to Selected, Move to First, Move to Last."
title: "Le menu de l'en-tête"
---
La petite flèche de l'en-tête d'un modificateur ouvre son menu. *Copy to Selected* copie le modificateur sur les autres objets sélectionnés ; vous vous en servirez pour les bras. *Move to First* et *Move to Last* le déplacent dans la pile.

*Apply* fige le résultat : la règle du chapitre est de ne pas s'en servir.
```

> [!WARNING]
> Ne confondez pas **appliquer un modificateur** (*Apply*, dans son en-tête) et **appliquer l'échelle** (`Ctrl + A > Scale`, dans la vue 3D). Le premier fige le résultat du modificateur. Le second ramène l'échelle de l'objet à 1 sans changer sa forme : c'est un geste de fichier propre, que vous pouvez faire à tout moment.

### Symétrie : le Mirror sur un autre axe
Le *Mirror* reflète la géométrie d'un objet. Vous l'avez vu sur l'axe X avec la rangée de sièges. Deux points comptent ici :
- l'axe se lit dans le repère de l'objet ;
- le reflet se fait autour de l'origine de l'objet, ou autour d'un autre objet choisi dans *Mirror Object*.

Sur la lampe, le *Mirror* transforme chaque bras plein en une paire de tiges parallèles, de part et d'autre de l'axe de la lampe.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/mirror_modifier_panel_blender.jpg"
caption: "Figure 2.4 : Le panneau Mirror du bras : seul l'axe Y est coché ; Bisect, Flip, Mirror Object, Clipping et Merge gardent leurs réglages d'origine."
title: "Le panneau Mirror"
---
Par défaut, le *Mirror* reflète sur X. Pour les bras, décochez X et cochez Y : les tiges se répartissent de part et d'autre de l'axe de la lampe.

*Mirror Object* change le centre du reflet. *Merge* soude les sommets qui se touchent sur le plan de symétrie.
```

### Recette · Des tiges doubles pour les bras
Sur *Bras_bas*, puis sur *Bras_haut* :
- **1.** Sélectionnez *Bras_bas*. `Tab`, `A`, puis `S Maj + Z 0.5` : la tige passe à 8 mm de diamètre, sans changer de longueur.
- **2.** `G Y = 10mm` : la tige quitte l'axe de la lampe. `Tab`.
- **3.** *Add Modifier > Generate > Mirror*. Décochez X, cochez Y : deux tiges parallèles apparaissent.
- **4.** Sur *Bras_haut*, refaites les étapes 1 et 2.
- **5.** Sélectionnez *Bras_haut*, puis *Bras_bas* en dernier : il devient l'objet actif. Dans le menu de l'en-tête du *Mirror*, choisissez *Copy to Selected*.
Contrôle : en vue de dessus (`7`), chaque bras montre deux tiges, symétriques par rapport à l'axe du socle. Corrigé : *Bras_bas_corrige* et *Bras_haut_corrige*, dans la collection *Corrigé*.

![Figure 2.5 : Vue de dessus. À gauche, la tige décalée de 10 mm en Mode Édition : le Mirror donne deux tiges. À droite, la même tige déplacée en Mode Objet : le reflet se fait autour de l'origine, qui a suivi la tige, et le Mirror semble ne rien faire.](assets/images/mirror_arm_rods_blender.jpg)

> [!WARNING]
> **Le piège de l'origine.** Si vous déplacez la tige en Mode Objet, son origine la suit : le reflet se fait autour d'elle, et le *Mirror* semble ne rien faire. Deux solutions : décaler la géométrie en Mode Édition, comme dans la recette, ou choisir le *Socle* dans *Mirror Object*.
> D'autres signes : des tiges qui plongent dans le socle (l'axe X est resté coché) ; *Copy to Selected* sans effet (l'objet actif doit être celui qui porte le modificateur).

> [!NOTE]
> **Ailleurs.** On modélise de la même façon une moitié de capot automobile, de nez de tram ou de fuselage : le *Mirror* construit l'autre moitié, et chaque retouche se fait des deux côtés à la fois.

```side-by-side
layout: "textRight"
imagePath: "assets/images/mirror_clipping_bisect_blender.jpg"
caption: "Figure 2.6 : Une moitié de capot en Mode Édition, avec Mirror X, Clipping et Bisect : la moitié reflétée suit chaque retouche."
title: "Pour aller plus loin : Clipping et Bisect"
---
Quand une forme traverse le plan de symétrie, deux cases du *Mirror* aident. *Clipping* retient sur le plan les sommets du milieu : ils ne peuvent plus le traverser. *Bisect* coupe ce qui dépasse de l'autre côté.

Elles ne sont pas nécessaires pour la lampe. Le défi de la chape (section 3) s'en sert.
```

### Épaisseur : une coque avec le Solidify
L'abat-jour du blocage est un cône plein. Pour en faire une coque, on enlève sa grande face, puis le modificateur *Solidify* lui donne une épaisseur régulière, qui reste réglable.

Ses réglages principaux :
- *Thickness* : l'épaisseur ;
- *Offset* : le côté de l'épaisseur, de `-1` (vers l'intérieur) à `1` (vers l'extérieur), `0` la répartissant de part et d'autre ;
- *Even Thickness* : une épaisseur constante, même dans les angles ;
- *Fill* (rubrique *Rim*) : ferme le bord de la coque.

Le côté intérieur ou extérieur se lit d'après les normales des faces : si elles sont inversées, l'épaisseur part du mauvais côté.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/delete_menu_faces_blender.jpg"
caption: "Figure 2.7 : Le menu Delete (X) en Mode Édition, la grande face de la tête sélectionnée."
title: "Supprimer une face"
---
En Mode Édition, `X` ouvre le menu *Delete*. *Faces* supprime seulement la face sélectionnée : ses arêtes et ses sommets restent, et la surface s'ouvre.

En Mode Objet, `X` supprime l'objet entier. En cas d'erreur, `Ctrl + Z`.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/solidify_modifier_panel_blender.jpg"
caption: "Figure 2.8 : Le panneau Solidify de la tête : Thickness 1,5 mm, Offset -1, Even Thickness et Fill cochés."
title: "Le panneau Solidify"
---
*Thickness* et *Offset* suffisent dans la plupart des cas. Faites varier *Offset* de -1 à 1 : l'épaisseur passe de l'intérieur à l'extérieur de la coque.

Avec `-1`, la forme extérieure de l'abat-jour ne change pas : c'est celle que vous avez validée au blocage.
```

### Recette · La coque de la tête
Sur *Tête* :
- **1.** `Tab`, puis `3` pour sélectionner des faces. Cliquez sur la grande face de l'ouverture.
- **2.** `X > Faces` : il reste une surface sans épaisseur. `Tab`.
- **3.** *Add Modifier > Generate > Solidify* : *Thickness* `1.5mm`, *Offset* `-1`, *Even Thickness* coché.
- **4.** Option : cochez *Fill* pour fermer le bord, et comparez.
Contrôle : en vue de dessous, le bord de la tête montre une épaisseur régulière. Corrigé : *Tête_corrige*, dans la collection *Corrigé*.

![Figure 2.9 : La tête vue de dessous : une coque ouverte. À droite, le bord en gros plan : la tranche de 1,5 mm.](assets/images/solidify_lamp_head_blender.jpg)

> [!WARNING]
> L'épaisseur part vers l'extérieur ? *Offset* vaut `1`, ou les normales sont inversées. L'affichage *Face Orientation* (Basics 103) tranche la question : une face rouge regarde vers l'intérieur.

> [!NOTE]
> **Ailleurs.** Un carénage d'avion, une coque de rétroviseur, un panneau d'habillage intérieur de train : on dessine la surface extérieure, et le *Solidify* donne l'épaisseur de la pièce. Changer l'épaisseur ne demande aucune reconstruction.

### Arrondir les arêtes : le Bevel en modificateur
Vous connaissez le *Bevel* en outil (`Ctrl + B`), qui biseaute les arêtes sélectionnées en Mode Édition. Il existe aussi en modificateur : le même arrondi, qui reste modifiable. Une arête parfaitement vive n'existe pas dans un objet fabriqué : un léger arrondi accroche la lumière et rend la pièce crédible.

C'est une notion nouvelle, que vous découvrez seul sur le socle. Trois réglages suffisent :
- *Amount* : la largeur de l'arrondi ;
- *Segments* : le nombre de facettes de l'arrondi ;
- *Limit Method* sur *Angle*, le réglage d'origine : seules les arêtes plus vives que l'angle donné sont arrondies.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/bevel_modifier_angle_blender.jpg"
caption: "Figure 2.10 : Le panneau Bevel du socle : Amount 3 mm, Segments 3, Limit Method sur Angle (30°)."
title: "Le panneau Bevel"
---
Le champ *Amount* donne la largeur de l'arrondi. Avec *Limit Method* sur *Angle*, les arêtes du dessus et du dessous du socle sont arrondies, mais pas les arêtes douces de son pourtour.

Le *Bevel* en outil (`Ctrl + B`) affiche, lui, *Width* pour la même notion.
```

### Recette · Le Bevel du socle
Sur *Socle*, en autonomie, avec la figure 2.10 :
- **1.** *Add Modifier > Generate > Bevel*.
- **2.** *Amount* `3mm`, *Segments* 3. *Limit Method* est déjà sur *Angle*.
- **3.** Tournez autour du socle : les arêtes du dessus et du dessous sont arrondies.
Contrôle : les arêtes du socle sont arrondies, sans déformation. Corrigé : *Socle_corrige*.

> [!WARNING]
> Un arrondi à grosses facettes : *Segments* est resté à 1. Un socle déformé : *Amount* est trop grand ; lisez la valeur affichée dans le champ, avec son unité.

### Lisser l'affichage : Shade Auto Smooth
Une coque à 24 côtés paraît facettée. *Object > Shade Auto Smooth* lisse l'affichage des faces courbes, sans arrondir les arêtes vives : la coque paraît lisse, et son bord reste net. La géométrie ne change pas.

Ce lissage compte pour la suite : au chapitre 3, un métal ou un plastique laqué montre la moindre facette.

```side-by-side
layout: "textRight"
imagePath: "assets/images/object_menu_shade_auto_smooth_blender.jpg"
caption: "Figure 2.11 : Le menu Object, avec Shade Smooth, Shade Auto Smooth et Shade Flat."
title: "Le menu Object"
---
*Shade Auto Smooth* se trouve dans le menu *Object* de la vue 3D, entre *Shade Smooth* et *Shade Flat*. Il s'applique à tous les objets sélectionnés en une fois.

Il ajoute au bas de la pile un modificateur, *Smooth by Angle* : les faces qui forment un angle de moins de 30° sont lissées.
```

### Recette · Lisser la tête, le socle et les bras
- **1.** Sélectionnez *Tête*, puis *Object > Shade Auto Smooth*.
- **2.** Faites de même sur *Socle*.
- **3.** Sélectionnez *Bras_bas* et *Bras_haut* ensemble, puis *Object > Shade Auto Smooth* : leurs tiges seront en métal au chapitre 3.
- **4.** Option : sur *Tête*, ajoutez dès maintenant un *Bevel* de `0.5mm`, 2 segments. Il est prévu à l'atelier.
Contrôle : les piles se lisent, de haut en bas : *Tête* = *Solidify*, *Smooth by Angle* ; *Socle* = *Bevel*, *Smooth by Angle*.

![Figure 2.12 : La tête sans lissage, puis avec Shade Auto Smooth. En bas, sa pile : Solidify, Bevel, puis Smooth by Angle, avec l'épingle à droite de son en-tête.](assets/images/modifier_stack_head_blender.jpg)

> [!NOTE]
> **L'ordre de la pile.** La pile de la tête compte maintenant plusieurs modificateurs. Blender les calcule de haut en bas : changer leur ordre peut changer le résultat (Basics 103, section 3). *Smooth by Angle* fait exception : l'épingle de son en-tête le garde en dernière position, même si vous ajoutez un modificateur après lui. Le *Bevel* de la tête se range donc de lui-même au-dessus.

### Répétition : une couronne avec un Empty
Le socle cache l'électronique de la lampe : il lui faut une grille d'aération, une couronne de lamelles sur le dessus. Avec les sièges, *Relative Offset* et *Constant Offset* répétaient en ligne. Pour répéter en couronne, l'*Array* a besoin d'un repère qui tourne : un *Empty*.

Un *Empty* est un objet sans géométrie, comme celui qui porte une image de référence. Avec *Object Offset*, chaque copie reprend l'écart entre l'objet et l'*Empty* : position, rotation et échelle. Tourné de 10°, l'*Empty* fait tourner chaque lamelle de 10° par rapport à la précédente. Pour faire le tour complet, la rotation vaut 360° divisé par le nombre de copies.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_empty_menu_blender.jpg"
caption: "Figure 2.13 : Le sous-menu Empty du menu Add (Maj + A), avec Plain Axes en tête."
title: "Ajouter un Empty"
---
`Maj + A > Empty` propose plusieurs formes d'affichage. Elles ne changent rien au rôle de l'*Empty* : choisissez *Plain Axes*, de simples axes.

Comme toute nouvelle pièce, l'*Empty* apparaît au curseur 3D : placez d'abord le curseur au bon endroit.
```

> [!NOTE]
> **Deux entrées Array.** Blender 5.2 propose aussi *Array*, un nouvel outil en Geometry Nodes ; ce chapitre utilise le modificateur classique, *Array (Legacy)*, qui accepte un *Empty* en *Object Offset*. Une fois ajouté, il s'appelle simplement *Array* dans la pile.

```side-by-side
layout: "textRight"
imagePath: "assets/images/array_object_offset_panel_blender.jpg"
caption: "Figure 2.14 : Le panneau du modificateur ajouté par Array (Legacy) : Relative Offset décoché, Object Offset coché sur l'Empty, Count 36."
title: "L'Array en Object Offset"
---
Trois réglages : décochez *Relative Offset*, cochez *Object Offset* et choisissez l'*Empty* dans son champ *Object*. *Count* donne le nombre de copies.

La rubrique *Object Offset* se déplie avec la petite flèche, à gauche de sa case.
```

### Recette · La grille d'aération
- **1.** `Maj + C` : le curseur 3D revient au centre, sous l'axe du socle.
- **2.** `Maj + A > Mesh > Cube`, puis F9 : *Size* `2mm`. Sans ce réglage, le cube mesure 2 m.
- **3.** `Tab`, `S X 6` : une lamelle de 12 mm. `G X = 76mm`, puis `G Z = 25mm` : elle se pose sur le dessus du socle, près du bord. `Tab`. L'origine reste au centre du socle. Renommez la lamelle *Grille_aeration*.
- **4.** `Maj + A > Empty > Plain Axes`, au même endroit, puis `R Z 10`. Renommez-le *Grille_pivot*.
- **5.** Sur la lamelle : *Add Modifier > Generate > Array (Legacy)*. Décochez *Relative Offset*, cochez *Object Offset* et choisissez *Grille_pivot*. *Count* 36 : les lamelles font le tour du socle.
Corrigé : *Grille_aeration_corrige* et son *Empty*, dans la collection *Corrigé*.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/radial_array_vent_grille_blender.jpg"
caption: "Figure 2.15 : Le socle en vue de dessus : 36 lamelles en couronne, et l'Empty Grille_pivot, agrandi pour la figure, tourné de 10°."
title: "La couronne de lamelles"
---
L'*Empty* est au centre du socle, comme l'origine de la lamelle. Chaque lamelle est tournée de 10° par rapport à la précédente : 36 copies font le tour complet.

Changez *Count*, ou la rotation de l'*Empty* : la couronne se met à jour aussitôt.
```

> [!WARNING]
> Un cube de 2 m : F9 a été oublié ; Blender ajoute ses primitives à leur taille d'origine. Une spirale : *Relative Offset* est resté coché. Une couronne décentrée : le curseur 3D n'était pas au centre au moment d'ajouter l'*Empty*.

### Le parentage : l'Empty suit la pièce
Déplacez la lamelle seule : la couronne se déforme, car l'*Empty* est resté en place. `Ctrl + Z`. Pour que l'*Empty* suive la lamelle, faites-en son enfant : c'est le **parentage**.

Sélectionnez d'abord l'enfant, *Grille_pivot*, puis le parent, *Grille_aeration*, en dernier : il devient l'objet actif. `Ctrl + P > Object`. Désormais, déplacer ou tourner la lamelle emporte l'*Empty*, et la couronne garde sa forme.

```side-by-side
layout: "textRight"
imagePath: "assets/images/parent_menu_blender.jpg"
caption: "Figure 2.16 : Le menu Set Parent To (Ctrl + P), l'Empty puis la lamelle sélectionnés."
title: "Le menu Set Parent To"
---
`Ctrl + P` ouvre le menu *Set Parent To*. Choisissez *Object* : l'enfant garde sa place et suit désormais son parent.

Dans l'Outliner, l'*Empty* se range sous la lamelle.
```

> [!WARNING]
> L'ordre de sélection compte : l'objet actif, sélectionné en dernier, devient le parent. Dans le mauvais ordre, c'est la lamelle qui suit l'*Empty*. `Ctrl + Z`, puis recommencez.

> [!CAUTION]
> **À vous : la molette de l'interrupteur.** Faites de l'interrupteur une molette crantée, avec la même méthode. Placez le curseur sur l'interrupteur (`Maj + S > Cursor to Selected`). Un cran de 1,5 × 1,5 × 6 mm se place à 8 mm de l'axe ; la molette compte 24 crans. Nommez les objets *Interrupteur_crans* et *Interrupteur_pivot*. De combien l'*Empty* doit-il tourner ? Le corrigé est dans la collection *Corrigé*.
> Palier ★ : 30 crans ; une demi-couronne de lamelles à l'arrière du socle.
> Contrôle : déplacez *Grille_aeration*, la couronne suit ; puis `Ctrl + Z`.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/radial_array_knob_blender.jpg"
caption: "Figure 2.17 : La molette crantée de l'interrupteur : un seul cran, répété en couronne autour de l'axe."
title: "La molette crantée"
---
Les crans sont à moitié enfoncés dans le bord de l'interrupteur : la molette paraît taillée dans la masse.

Un seul cran est modélisé. Pour un bouton plus fin, changez *Count*, puis la rotation de l'*Empty*.
```

> [!NOTE]
> **Ailleurs.** Les aubes d'une soufflante de réacteur, les rayons d'une jante, les boulons d'une roue de bogie : une pièce, un *Empty* et un *Array* en couronne. Le nombre d'éléments reste un réglage jusqu'au bout du projet.

```quiz
question: "La tige a été déplacée en Mode Objet, puis un Mirror sur Y lui a été ajouté. Rien ne semble changer : pourquoi ?"
options:
  - "Le Mirror ne fonctionne que sur l'axe X"
  - "Le reflet se fait autour de l'origine de l'objet, qui a suivi la tige"
  - "L'échelle de l'objet n'est pas appliquée"
  - "Il faut d'abord appliquer le modificateur"
correctIndices:
  - 1
explanation: "Le **Mirror** reflète autour de l'origine de l'objet. En Mode Objet, l'origine suit la tige : le reflet tombe sur la tige elle-même. Décalez la géométrie en Mode Édition, ou choisissez un **Mirror Object**. Au chapitre 3, le brossé des bras suit lui aussi leurs axes : savoir lire l'origine et les axes d'une pièce sert encore."
```

```quiz
question: "L'épaisseur de la coque part vers l'extérieur alors que vous la voulez à l'intérieur. Que changez-vous ?"
options:
  - "Thickness, à 0"
  - "La case Fill de la rubrique Rim"
  - "Le signe d'Offset, ou le sens des normales"
  - "La case Even Thickness"
correctIndices:
  - 2
explanation: "**Offset** place l'épaisseur d'un côté ou de l'autre de la surface, d'après le sens des normales. Avec des normales inversées, -1 part vers l'extérieur. Distinguer l'intérieur et l'extérieur d'une coque sert au chapitre 3, qui peut y poser deux matières."
```

## 2. Courbes de Bézier : profils et détails

### Courbe et maillage
Un maillage est fait de sommets, d'arêtes et de faces. Une courbe est définie par quelques points de contrôle seulement : Blender en calcule la forme lisse. Sa finesse se règle après coup, et sa forme se retouche en déplaçant un point ou une poignée. La courbe est non destructive par nature.

Elle sert à deux choses dans ce chapitre : le câble de la lampe, une courbe à laquelle on donne une épaisseur ronde, et le profil de l'ampoule, que l'on fait tourner autour d'un axe.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_curve_menu_blender.jpg"
caption: "Figure 2.18 : Le sous-menu Curve du menu Add."
title: "Ajouter une courbe"
---
`Maj + A > Curve > Bézier` ajoute une courbe de deux points. Comme pour les primitives, F9 règle sa taille : *Radius* `50mm`. Sans ce réglage, la courbe mesure 2 m.

*Circle* ajoute un cercle de Bézier fermé, à quatre points.
```

### L'anatomie d'une courbe de Bézier
En Mode Édition (`Tab`), chaque **point de contrôle** porte deux **poignées**. La direction des poignées donne la tangente de la courbe au point ; leur longueur règle la tension de la courbe.

Le type des poignées change le comportement du point. Il se choisit avec `V` :
- *Automatic* : Blender règle les poignées pour une courbe douce ;
- *Vector* : chaque poignée vise le point voisin, et le point devient un angle vif ;
- *Aligned* : les deux poignées restent alignées, mais leur longueur est libre ;
- *Free* : chaque poignée se règle seule, et le point peut faire un angle.

![Figure 2.19 : Une courbe de Bézier en Mode Édition : chaque point de contrôle porte deux poignées, et leur type règle la forme de la courbe autour du point.](assets/images/bezier_anatomy_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/handle_type_menu_blender.jpg"
caption: "Figure 2.20 : Le menu Set Handle Type (V)."
title: "Changer le type d'un point"
---
Sélectionnez un ou plusieurs points, puis `V` : le menu *Set Handle Type* s'ouvre sous la souris.

*Vector* casse la courbe en un angle vif ; *Automatic* l'adoucit. Déplacer une poignée *Automatic* la fait passer en *Aligned*.
```

### Recette · Tracer le câble
- **1.** Vue de dessus (`7`). `Maj + A > Curve > Bézier`, puis F9 : *Radius* `50mm`. Renommez la courbe *Câble*.
- **2.** `Tab` : les points et leurs poignées apparaissent. Déplacez un point, puis une poignée, avec `G`.
- **3.** Sélectionnez le point d'une extrémité, puis `E` : la courbe se prolonge. `Ctrl + clic droit` pose un nouveau point sous la souris.
- **4.** Tracez 4 ou 5 points, de l'arrière du socle (à gauche en vue de face) jusqu'au bord de la table.
- **5.** Réglez les types avec `V` : *Vector* pour un angle, *Automatic* pour une courbe.
Travaillez en vue orthographique : en perspective, les points posés partent en profondeur.

### L'outil Curve Pen
En Mode Édition, l'outil *Curve Pen* de la barre d'outils dessine comme un logiciel de dessin vectoriel. Un clic pose un point anguleux (*Vector*). Un cliquer-glisser tire ses poignées et pose un point arrondi (*Aligned*).

Il prolonge la courbe depuis le point d'extrémité sélectionné. Vous gardez ensuite le tracé que vous préférez : celui du `E` et du `Ctrl + clic droit`, ou celui du *Curve Pen*.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/curve_pen_toolbar_blender.jpg"
caption: "Figure 2.21 : L'outil Curve Pen, actif dans la barre d'outils du Mode Édition, et ses réglages dans l'en-tête."
title: "L'outil Curve Pen"
---
L'outil se trouve en bas de la barre d'outils, en Mode Édition d'une courbe. Son en-tête affiche *Extrude Handle Type* sur *Vector* : c'est le type d'un point posé d'un simple clic.

Pour revenir à la sélection, reprenez l'outil du haut de la barre.
```

### Donner du volume au câble
Une courbe n'a pas de volume : elle n'apparaît pas au rendu. Son épaisseur se règle dans l'éditeur de propriétés, onglet *Object Data* (l'icône de courbe) :
- rubrique *Shape* : *Resolution Preview U*, la finesse de la courbe dans la vue ;
- rubrique *Geometry*, sous-rubrique *Bevel* : *Round* pour une section ronde, *Depth* pour son rayon, *Resolution* pour sa finesse, *Fill Caps* pour fermer les extrémités.

*Extrude* et *Offset*, juste au-dessus, servent à d'autres usages : *Extrude* donne un ruban plat.

```side-by-side
layout: "textRight"
imagePath: "assets/images/curve_shape_panel_blender.jpg"
caption: "Figure 2.22 : L'onglet Object Data du câble, rubrique Shape : Resolution Preview U à 24."
title: "La rubrique Shape"
---
*Resolution Preview U* règle le nombre de segments calculés entre deux points de contrôle. Montez-le si le câble paraît anguleux.

Le réglage ne change que la finesse du calcul : les points de contrôle restent les mêmes.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/curve_geometry_bevel_panel_blender.jpg"
caption: "Figure 2.23 : La rubrique Geometry, sous-rubrique Bevel : Round, Depth 2,5 mm, Resolution 4, Fill Caps."
title: "La sous-rubrique Bevel"
---
*Depth* est le rayon de la section : `2.5mm` donne un câble de 5 mm de diamètre. *Fill Caps* ferme ses deux extrémités.

Ce *Bevel* de courbe n'a rien à voir avec le modificateur *Bevel* : il donne une section à la courbe.
```

### Recette · Le câble rond
- **1.** Sélectionnez *Câble*. Onglet *Object Data*, rubrique *Geometry > Bevel* : *Round*, *Depth* `2.5mm`, *Resolution* 4, *Fill Caps* coché.
- **2.** Activez l'aimantation sur *Face* (chapitre 1), puis posez le premier point contre le flanc du socle. Les suivants reposent sur la table.
- **3.** À vous : retracez le câble avec l'outil *Curve Pen*, avec une boucle posée sur la table. Gardez le tracé que vous préférez.
- **4.** Option : rubrique *Shape*, *Resolution Preview U* à 24.
Contrôle : en vue de face (`1`), le câble repose sur la table. Il est rond et lisse ; en Mode Édition, il ne compte que 4 à 6 points. Corrigé : *Câble_corrige*.

![Figure 2.24 : Le câble posé : il part de l'arrière du socle et repose sur la table.](assets/images/cable_bezier_lamp_blender.jpg)

> [!WARNING]
> Un câble plat : *Extrude* a été réglé à la place de *Depth*. Un câble à facettes : *Resolution* ou *Resolution Preview U* est trop basse. Un câble qui s'enfonce dans la table : une poignée descend sous le plan ; remontez-la en vue de face.

> [!NOTE]
> **Ailleurs.** Une main courante ou une barre de maintien de tram, une durite de moteur, un faisceau électrique en cabine : un tracé de quelques points et une section ronde. Le tracé se retouche à tout moment.

```quiz
question: "Quel type de poignée change d'un coup un point de courbe en angle vif ?"
options:
  - "Automatic"
  - "Aligned"
  - "Aucun : il faut ajouter un point"
  - "Vector"
correctIndices:
  - 3
explanation: "Avec **Vector**, chaque poignée vise le point voisin : le point devient un angle vif. **Automatic** l'adoucit. Retoucher un point sans redessiner la courbe sert pour l'ampoule, le câble et les défis."
```

```quiz
question: "Quel réglage donne une section ronde à une courbe ?"
options:
  - "Bevel en mode Round, avec une valeur de Depth"
  - "Extrude"
  - "Offset"
  - "Resolution Preview U"
correctIndices:
  - 0
explanation: "Dans **Geometry > Bevel**, le mode **Round** et la valeur de **Depth** donnent une section ronde. **Extrude** donne un ruban plat. Une courbe sans **Depth** n'a pas de volume : elle ne reçoit pas de matière au chapitre 3 et n'apparaît pas au rendu du chapitre 4."
```

### Profil de révolution : l'ampoule
Pour une pièce de révolution, on dessine la moitié de son profil, et Blender le fait tourner autour d'un axe : c'est la révolution des logiciels de CAO. Le modificateur *Screw* s'en charge, sur une courbe comme sur un maillage. Le profil reste modifiable : une poignée déplacée change toute la pièce.

Le profil de l'ampoule est donné par un croquis, déjà placé dans le fichier (collection *Croquis*). Il se voit en vue de face, à droite de la lampe. Ses cinq points sont numérotés, du culot au sommet.

```resource
title: "Croquis : le demi-profil de l'ampoule"
description: "Le croquis du demi-profil, avec ses cinq points numérotés et ses cotes (Ø 50, hauteur 80 mm). Il est déjà placé dans le fichier d'exercice ; cette copie sert si vous travaillez dans votre propre fichier du chapitre 1."
fileName: "PRC02_ch2_croquis_ampoule.zip (43 Ko)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch2_croquis_ampoule.zip"
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/snap_pie_menu_blender.jpg"
caption: "Figure 2.25 : Le menu circulaire Snap (Maj + S), avec Cursor to Selected et Selection to Cursor."
title: "Le curseur et la sélection"
---
`Maj + S` ouvre un menu circulaire. *Cursor to Selected* pose le curseur 3D sur la sélection ; *Selection to Cursor* fait l'inverse : il amène la sélection sur le curseur.

Ici, le curseur se pose sur le repère de l'ampoule, puis le premier point du profil le rejoint : il est exactement sur l'axe.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/screw_modifier_panel_blender.jpg"
caption: "Figure 2.26 : Le panneau Screw de l'ampoule : Angle 360°, Axis Z, Steps 32, Merge coché à 0,1 mm."
title: "Le panneau Screw"
---
*Axis* donne l'axe de révolution, dans le repère de l'objet. *Steps* règle le nombre de facettes du tour. *Merge* soude les sommets proches de l'axe : le champ à côté de la case est la distance de soudure.

*Screw* et *Iterations* font un ressort, en décalant chaque tour : c'est l'un des défis de la section 3.
```

### Recette · L'ampoule
- **1.** Cliquez sur *Repere_ampoule*, à droite de la lampe, puis `Maj + S > Cursor to Selected` : le curseur se pose à la base de l'axe de l'ampoule.
- **2.** `Maj + A > Curve > Bézier`, renommée *Ampoule*. `Tab`. Sélectionnez le point de droite et supprimez-le (`X > Vertices`).
- **3.** Sélectionnez le point restant, puis `Maj + S > Selection to Cursor` : c'est le point 1 du croquis, sur l'axe. `V > Vector`.
- **4.** Vue de face (`1`). Avec *Curve Pen* : un clic sur les points 2 et 3 du croquis (le culot, anguleux), un cliquer-glisser vertical sur le point 4 (le globe), un cliquer-glisser horizontal sur le point 5 (le sommet, sur l'axe).
- **5.** `Tab`. *Add Modifier > Generate > Screw* : *Axis* Z, *Steps* 32, *Merge* coché, distance `0.1mm`. L'ampoule apparaît.
- **6.** Placez-la dans la tête : `N > Item`, *Location* `211mm`, `0`, `411mm`, *Rotation* Y `150`.
Contrôle : une ampoule lisse, fermée en haut et en bas, logée au fond de la tête. Corrigé : *Ampoule_corrige*.

![Figure 2.27 : Le demi-profil de l'ampoule, posé sur son croquis ; l'ampoule obtenue par le Screw ; à droite, le sommet aplati par une distance de soudure de 10 mm, le réglage d'origine.](assets/images/bulb_profile_screw_blender.jpg)

> [!WARNING]
> **La distance de soudure.** Par défaut, *Merge* soude tout ce qui passe à moins de 10 mm de l'axe : sur une ampoule de 50 mm, le sommet s'aplatit. Ramenez la distance à `0.1mm`.
> Autres signes : un trou au sommet (le point 5 ne touche pas l'axe, ou *Merge* n'est pas coché) ; un disque à la place d'une ampoule (le mauvais axe) ; un sommet pointu (le point 5 posé d'un simple clic, ses poignées doivent être horizontales) ; une ampoule rouge avec *Face Orientation* (cochez *Flip*, dans la rubrique *Normals* du *Screw*).

> [!TIP]
> Option ★ : retouchez une poignée du profil, l'ampoule suit. Comparez 16 et 48 *Steps* : à cette taille, 32 suffisent.

> [!NOTE]
> **Ailleurs.** Le profil d'une roue ferroviaire, avec sa table de roulement et son boudin ; l'optique d'un phare ; le cône d'une hélice. On dessine une moitié du profil, et la pièce reste modifiable par ses quelques points.

## 3. Atelier : concept d'objet industriel

### Remplacer le blocage pièce par pièce
**La situation.** Le concept de lampe a passé la revue de blocage. Vous préparez la maquette numérique de la revue de design. Le client demandera sûrement des retouches : tout doit rester modifiable.

L'atelier n'apporte aucune notion nouvelle : il réinvestit les sections 1 et 2. La méthode est toujours la même. Vous remplacez un volume du blocage par une pièce propre, à sa place et à ses cotes, puis vous la comparez au gabarit, en vue de face (`1`) et de profil (`3`). Comptez environ 40 minutes.

### Consignes · La lampe modélisée
Les valeurs sont indicatives ; elles sont aussi dans la partie « Atelier » du LISEZ-MOI.
- **Articulations.** Placez le curseur sur chaque sphère (`Maj + S > Cursor to Selected`), supprimez-la (`X`), puis `Maj + A > Mesh > Cylinder`, F9 : *Vertices* 32, *Radius* `15mm`, `14mm` ou `12mm`, *Depth* `36mm`. `R X 90` : le cylindre se couche sur Y. *Bevel* (`2mm`, 2 segments, *Angle*) et *Shade Auto Smooth*. Renommez *Articulation_bas*, *_milieu* et *_haut*.
- **Douille.** Curseur sur *Tête*, puis `Maj + A > Mesh > Cylinder`, F9 : *Radius* `15mm`, *Depth* `20mm`, *Rotation* Y `-30`. Puis `G Z Z = 45mm` : elle glisse le long de son propre axe, au fond de la tête. *Bevel* (`1mm`, 2 segments) et *Shade Auto Smooth*.
- **Tête.** Un *Bevel* de `0.5mm`, 2 segments, sur le bord de l'ouverture. Il se range de lui-même au-dessus de *Smooth by Angle*.
- **Interrupteur.** Un *Bevel* de `0.5mm`, 2 segments, et *Shade Auto Smooth*.
- **Ampoule.** Placez-la, si ce n'est pas fait : `N > Item`.
- **Câble.** Vérifiez qu'il touche le socle et repose sur la table.
- **Tout.** La checklist, puis l'enregistrement.
Un *Bevel* plus large que l'épaisseur croise la géométrie : sur la tête, 0,5 mm pour 1,5 mm d'épaisseur.

> [!WARNING]
> Trois articulations de diamètres différents : faites des copies simples (`Maj + D`) et redimensionnez-les en Mode Édition, ou ajoutez trois cylindres. Une copie redimensionnée en Mode Objet garderait une échelle différente de 1. Et `Ctrl + A` ouvre le menu d'application des transformations : rien à voir avec *Apply*, dans l'en-tête d'un modificateur.

![Figure 2.28 : La lampe modélisée, superposée au gabarit en fil de fer, en vue de face et en perspective.](assets/images/lamp_model_vs_gabarit_blender.jpg)

### Consignes · La checklist du modèle propre
Avant d'enregistrer, vérifiez :
- chaque pièce porte un nom clair et se range dans la collection *Lampe* ;
- les échelles valent 1 (`Ctrl + A > Scale` si besoin) ;
- *Face Orientation* ne montre aucune face rouge ;
- les modificateurs sont tous actifs, aucun n'est appliqué ;
- la silhouette suit le gabarit, en vue de face et de profil ;
- la collection *Gabarit* est masquée, et le fichier `lampe_modele_v001.blend` est enregistré (`Ctrl + S`).
Corrigé : la collection *Corrigé* contient toute la lampe terminée.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/outliner_lamp_model_blender.jpg"
caption: "Figure 2.29 : L'Outliner de la lampe modélisée : une pièce par objet, et l'icône de clé des modificateurs."
title: "Un fichier lisible"
---
Dans l'Outliner, chaque pièce a son nom. La petite clé à droite d'un nom signale ses modificateurs : un clic sur la flèche de l'objet les déplie.

Des pièces séparées et bien nommées rendent l'habillage du chapitre 3 simple : une matière par pièce.
```

![Figure 2.30 : La lampe modélisée, en Solid avec Cavity.](assets/images/lamp_model_final_blender.jpg)

```resource
title: "La lampe modélisée : départ du chapitre 3"
description: "La lampe terminée, sans suffixe, modificateurs actifs : le corrigé de l'atelier, et le point de départ du chapitre 3. Si vous n'avez pas fini, enregistrez-le sous lampe_modele_v001.blend et reprenez le chapitre 3 avec lui."
fileName: "PRC02_ch2_lampe_modele.blend (0.3 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch2_lampe_modele.blend"
```

> [!CAUTION]
> **Les paliers ★ de l'atelier**, pour ceux qui ont fini le socle :
> - des molettes de serrage sur les articulations : sélectionnez l'interrupteur, ses crans et son *Empty* ensemble, puis `Alt + D` ; tournez la copie de X -90° et posez-la contre l'articulation ;
> - une rainure décorative sur le pourtour du socle : deux boucles (*Loop Cut*), puis la bande entre elles extrudée de 1 mm vers l'intérieur ;
> - une collection par sous-ensemble, *Pied*, *Bras* et *Tête*, dans *Lampe*.
>
> Les solutions sont dans la collection *Corrigé défis*, sous-collection *Paliers*. Les copies liées partagent leur maillage, pas leurs modificateurs : changer le nombre de crans de l'une ne change pas les autres.

### Les défis ★★
Pour ceux qui avancent vite, cinq défis sur la lampe. Leurs solutions sont dans la collection *Corrigé défis*, une sous-collection par défi. Pour en voir un, ouvrez l'œil de la collection, sélectionnez une pièce, puis `.` du pavé numérique pour la cadrer.
- **La chape** : une chape en U pour l'articulation du haut, modélisée par moitié avec *Mirror*, *Clipping* et *Bisect* (figure 2.6). Elle prend la place de la molette du haut.
- **La tête tulipe** : remplacez le cône par un profil de Bézier, puis *Screw* et *Solidify*. C'est la pile la plus complète du chapitre.
- **Les ressorts** : un cercle de Bézier décalé de l'axe, et un *Screw* avec une valeur de *Screw* et plusieurs *Iterations*, comme sur les lampes d'architecte. Un *Mirror* donne le second.
- **Percer la grille** : un *Boolean* en *Difference* sur le socle, avec la grille comme objet. Prolongez d'abord la lamelle vers le bas, sur 6 mm de haut : les fentes font alors 3 mm de profondeur.
- **Une grille au dos de l'abat-jour** : la même couronne, sur l'axe incliné de la tête.

```side-by-side
layout: "textRight"
imagePath: "assets/images/boolean_difference_panel_blender.jpg"
caption: "Figure 2.31 : Défi : le panneau Boolean du socle, en Difference, avec la grille d'aération comme objet."
title: "Percer la grille"
---
Le *Boolean* en *Difference* retire du socle le volume de la grille. Il utilise la couronne calculée par l'*Array* : changer le nombre de lamelles change le nombre de fentes.

Dans l'onglet *Object* de la grille, réglez *Display As* sur *Wire* (rubrique *Viewport Display*) et décochez *Renders* (rubrique *Visibility*) : elle ne sert plus que d'outil. Les figures 2.54 et 2.55 de la section 4 montrent ces deux rubriques.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/reading_light_challenge_blender.jpg"
caption: "Figure 2.32 : Défi : la liseuse de cabine finie, sur sa paroi, au-dessus de l'accoudoir."
title: "Défi ★★ : la liseuse de cabine"
---
La même méthode sur un objet des transports : une liseuse à col de cygne, fixée à la paroi, comme en voiture de première classe ou en cabine d'affaires.

Elle réunit toutes les notions du chapitre : une platine arrondie et ses vis en symétrie, un bouton moleté, un col de cygne en courbe, une tête en coque et son diffuseur de révolution.
```

```resource
title: "Défi ★★ : la liseuse de cabine"
description: "Le fichier du défi : la paroi et l'accoudoir, le gabarit de la liseuse en fil de fer, les pièces à travailler et un LISEZ-MOI par étapes. Le corrigé est dans la collection masquée « Corrigé ». Enregistrez le fichier sous liseuse_modele_v001.blend avant de commencer."
fileName: "PRC02_ch2_liseuse_depart.blend (0.1 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch2_liseuse_depart.blend"
```

```quiz
question: "Quand appliquer les modificateurs de la lampe ?"
options:
  - "Dès que la pièce est finie"
  - "Avant d'enregistrer le fichier"
  - "Avant d'appliquer l'échelle"
  - "Le plus tard possible, par exemple pour un export : les matières du chapitre 3 se posent sans les appliquer"
correctIndices:
  - 3
explanation: "Un modificateur appliqué ne se règle plus. Gardez-les actifs : le chapitre 3 habille les pièces telles quelles, et le client peut encore demander des retouches. On n'applique qu'au dernier moment, par exemple pour exporter vers un autre logiciel."
```

> [!NOTE]
> Pour aller plus loin, la section 4 propose un défi facultatif de modélisation avancée : surfaces tendues, détails conformés avec le *Shrinkwrap* et découpes avec le *Boolean*, sur des pièces des trois secteurs.

## 4. Défi facultatif · Modélisation avancée

> [!NOTE]
> Ce défi est **facultatif** : il n'est pas prévu au programme de base. Il s'adresse à ceux qui avancent vite dans les contenus de base, et à ceux qui maîtrisent déjà ces sujets. Vous pouvez le faire à la suite des parties de base, s'il vous reste du temps, ou à leur place. Il demande de savoir ajouter un modificateur, le régler et changer sa place dans la pile (Basics 103, section 3). Si vous le faites à la place des parties de base, vous pouvez reprendre le chapitre 3 avec son fichier de secours, `PRC02_ch3_lampe_a_habiller.blend`, ou avec `PRC02_ch2_lampe_modele.blend`, enregistré sous `lampe_modele_v001.blend`. C'est une option, pas une obligation.

> [!NOTE]
> **Si vous n'avez pas encore suivi le chapitre 2**, voici les quelques réglages dont le défi se sert :
> - *Solidify* (*Add Modifier > Generate*) donne une épaisseur à une surface. *Thickness* règle l'épaisseur ; *Offset* la place : à `-1` sous la surface, à `0` de part et d'autre, à `1` dessus.
> - Le modificateur *Bevel* (*Add Modifier > Generate*) arrondit les arêtes. *Amount* règle la largeur du biseau (la propriété *Width*), *Segments* son arrondi. *Limit Method* sur *Angle*, le réglage par défaut, ne biseaute que les arêtes vives.
> - *Object > Shade Auto Smooth* lisse l'affichage sans arrondir les arêtes vives. Il ajoute le modificateur *Smooth by Angle*, qui reste toujours en bas de la pile.
> - Vu au chapitre 1 : pendant un geste, `=` ouvre la saisie avec unité (`G X = 500mm`) ; `/` du pavé numérique isole la sélection (vue locale).

### Ce que vous allez apprendre
Les carrosseries, les nez de train et les fuselages sont des surfaces courbes et tendues. Ce défi apprend à y poser des détails proprement, et à garder ces surfaces propres. À la fin, vous saurez :
- tendre les arêtes d'une surface en subdivision ;
- conformer un détail à une surface courbe avec le modificateur *Shrinkwrap*, dans le mode adapté ;
- régler l'écart et le côté d'un détail, et limiter le shrinkwrap à une partie du détail ;
- placer *Subdivision*, *Shrinkwrap* et *Solidify* dans le bon ordre ;
- découper une pièce sans la détruire, avec un *Boolean* ;
- en ★★, nettoyer l'ombrage autour d'une découpe.

Le défi dure environ 3 heures, en deux paliers et un atelier. Chaque étape suit le même ordre : une pièce d'exemple à observer, une recette guidée, puis un petit défi. Les exemples viennent des trois secteurs : un fuselage d'avion d'affaires, un nez de tram, un capot et un rétroviseur automobiles.

```resource
title: "Fichier d'exercice : défi de modélisation avancée"
description: "Toutes les pièces du défi, rangées en une collection par étape, avec leurs surfaces de référence, les exemples terminés et le rétroviseur de l'atelier. Les corrigés sont dans la collection masquée « Corrigé défi modélisation ». Enregistrez le fichier sous defi_modelisation_v001.blend avant de commencer."
fileName: "PRC02_ch2_defi_modelisation.blend (0.2 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch2_defi_modelisation.blend"
```

![Figure 2.33 : Le banc du défi, une rangée par étape : surfaces de référence, exemples et pièces à travailler, puis le rétroviseur de l'atelier.](assets/images/modeling_challenge_overview_blender.jpg)

> [!WARNING]
> Tout le défi fonctionne en *Solid*, en *Material Preview* et au rendu EEVEE : il ne touche qu'à la géométrie et aux normales, et aucune recette ne dépend de Cycles. Quelques effets peuvent toutefois surprendre à la lecture :
> - un détail posé exactement sur la surface scintille par plaques : décollez-le de 0,2 mm (étape 2) ;
> - un détail parti de l'intérieur de la carrosserie peut y disparaître : réglez *Snap Mode* (étape 3) ;
> - une découpe dans une surface courbe montre des traînées dans les reflets : c'est un défaut d'ombrage, pas de forme (étape 6) ;
> - un objet de coupe reste visible au rendu tant que *Renders* est coché (étape 5).

### Avant de commencer
Ouvrez le fichier et repérez-vous en cinq minutes. Les pièces sont à l'échelle réelle, en millimètres. Les couleurs vous guident : gris clair pour les carrosseries, gris très sombre pour les détails finis, orange pour les pièces à travailler.

### Recette · Prendre le fichier en main
Quatre gestes avant la première étape :
- **1.** Ouvrez `PRC02_ch2_defi_modelisation.blend`, puis enregistrez-le sous `defi_modelisation_v001.blend`.
- **2.** Dans l'Outliner, affichez seulement la collection de l'étape en cours (l'œil). Moins de pièces affichées, c'est un affichage plus fluide.
- **3.** Pour travailler sur une pièce, sélectionnez-la avec sa surface de référence, puis appuyez sur `/` du pavé numérique : la vue locale. Le même raccourci ramène la vue complète.
- **4.** Les corrigés sont à la place de vos pièces, dans la collection masquée « Corrigé défi modélisation ». Pour comparer, affichez la sous-collection de l'étape, puis masquez votre pièce avec `H`.
Le texte LISEZ-MOI, en bas de l'écran, résume les recettes. `Ctrl + Espace` au-dessus de lui l'agrandit.

### Palier 1 · Surfaces et shrinkwrap
Le premier palier dure environ 90 minutes, et il se fait en séance. Il part de la surface de référence, puis présente le shrinkwrap en trois étapes : à quoi il sert, trois cas d'usage, puis les réglages et l'ordre dans la pile. Point d'arrêt : les quiz 1 à 6.

### Étape 1 · La surface de référence en subdivision
**Nouveau :** tendre une arête dans une surface en subdivision. **Déjà vu :** le modificateur *Subdivision Surface* et *Loop Cut* (Basics 103).

En design de transport, une carrosserie ou un fuselage est une surface douce et tendue. En maillage, on l'obtient avec une cage légère et le modificateur *Subdivision Surface*. Le shrinkwrap a besoin de ces surfaces propres : un détail conformé épouse chaque défaut de sa cible.

Cette étape est facultative si vous connaissez déjà la subdivision : toutes les surfaces de référence des étapes suivantes sont prêtes dans le fichier.

![Figure 2.34 : Trois carters de projecteur avec la même cage et la même subdivision : sans rien de plus (un savon), avec des boucles de maintien, avec un Crease de 1. À droite, la même rangée en MatCap de contrôle des reflets.](assets/images/subdivision_holding_loops_crease_blender.jpg)

### Recette · Subdivision et boucles de maintien
Sur `E1_Pratique_Boucles`, un cube de 120 × 80 × 40 mm, sans modificateur :
- **1.** En Mode Objet, `Ctrl + 2` : un modificateur *Subdivision Surface* au niveau 2 rejoint la pile. Le carter devient un savon. Gardez *Levels Viewport* et *Render* à 2 : au-delà, l'affichage ralentit pour un gain invisible.
- **2.** `Tab` : Mode Édition. La cage du carter apparaît.
- **3.** `Ctrl + R`, puis survolez une arête verticale : l'aperçu jaune d'une boucle horizontale apparaît. Cliquez, glissez la boucle près du dessus, à environ 4 mm, puis cliquez. Les arêtes du dessus se tendent.
- **4.** Même geste près du dessous, puis près des extrémités de la longueur et de la largeur : six boucles en tout. Les arêtes verticales se tendent à leur tour.
- **5.** `Tab` : retour au Mode Objet.
Plus la boucle est proche de l'arête, plus l'arête est vive. La valeur exacte n'a pas d'importance.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/loop_cut_holding_loop_blender.jpg"
caption: "Figure 2.35 : Une boucle de maintien, sélectionnée à 4 mm de l'arête du dessus, en Mode Édition."
title: "Une boucle de maintien"
---
La boucle sélectionnée, en jaune, court tout autour du carter, à 4 mm du dessus. La subdivision arrondit toujours l'arête, mais sur une bande étroite : l'arête paraît vive et reste douce aux reflets. Une boucle placée au milieu de la face ne tendrait rien.
```

### Recette · Le Crease
Sur `E1_Pratique_Crease`, la même cage, déjà subdivisée :
- **1.** `Tab`, puis `2` : la sélection des arêtes.
- **2.** `Alt + clic` sur une arête du dessus : toute la boucle du bord du dessus est sélectionnée.
- **3.** `Maj + E`, tapez `1`, puis `Entrée`. Le *Crease* de ces arêtes vaut 1 : elles deviennent vives, sans géométrie de plus.
- **4.** Option : refaites le geste avec `0.6`. L'arête s'adoucit.
Le même réglage se trouve dans le menu *Edge > Edge Crease* du Mode Édition.

```side-by-side
layout: "textRight"
imagePath: "assets/images/edge_menu_edge_crease_blender.jpg"
caption: "Figure 2.36 : Le menu Edge du Mode Édition, avec Edge Crease (Maj + E)."
title: "Le menu Edge"
---
Le menu Edge réunit les commandes qui agissent sur les arêtes sélectionnées. Edge Crease y figure avec son raccourci, Maj + E. Pendant le geste, tapez la valeur voulue, de 0 à 1, puis validez avec Entrée.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/subdivision_advanced_use_creases_blender.jpg"
caption: "Figure 2.37 : Le panneau Subdivision Surface, rubrique Advanced dépliée : Use Creases est coché par défaut."
title: "Le Crease et le modificateur"
---
Le modificateur lit le Crease grâce à la case Use Creases, cochée par défaut, dans sa rubrique Advanced. Si une arête creasée reste molle, vérifiez cette case. La case Use Custom Normals servira à l'étape 6.
```

### Boucles de maintien ou Crease ?
Les deux méthodes tendent une arête, chacune à sa façon :
- les boucles de maintien restent dans la géométrie : elles se lisent dans tous les logiciels, et leur distance règle le rayon de l'arête ;
- le *Crease* est un réglage de Blender : il est rapide, et il se modifie à tout moment, sans toucher à la cage.

Beaucoup de designers combinent les deux : des boucles pour les grandes lignes, un *Crease* pour une nervure qu'on veut ajuster.

> [!WARNING]
> **Erreurs fréquentes**
> - La boucle n'apparaît pas : la souris n'est pas sur une arête. Approchez-la jusqu'à voir l'aperçu jaune.
> - Tout le carter devient vif : le *Crease* a été posé sur toutes les arêtes. `Maj + E`, puis `0` sur celles qui doivent rester douces.
> - Une bosse près d'un coin : une boucle a été glissée trop loin, jusqu'à croiser une autre boucle. `Ctrl + Z`.

```side-by-side
layout: "textRight"
imagePath: "assets/images/crease_hood_character_line_blender.jpg"
caption: "Figure 2.38 : Le capot du petit défi, en MatCap de contrôle des reflets : nervure molle à gauche, nervure tendue par un Crease de 0,8 à droite."
title: "Le capot à ligne de caractère"
---
Une ligne de caractère est une arête tendue qui court sur un capot ou un flanc. Elle accroche la lumière et donne sa tension au dessin. En MatCap de contrôle, les bandes de reflet se cassent net sur une nervure tendue ; elles s'arrondissent sur une nervure molle.
```

> [!CAUTION]
> **Petit défi · Le capot à ligne de caractère (automobile).** `E1_Defi_Capot` est la cage d'un capot de 600 × 400 mm, déjà subdivisée. Sa nervure centrale est molle. Rendez-la vive, sans toucher au reste du capot. Le corrigé est dans la sous-collection « Corrigé étape 1 ».

```quiz
question: "Sur une pièce en subdivision, vous voulez une arête vive, sans ajouter de géométrie. Que faites-vous ?"
options:
  - "Un Crease de 1 sur l'arête (Maj + E)"
  - "Monter Levels Viewport"
  - "Une boucle de maintien près de l'arête"
  - "Appliquer la subdivision"
correctIndices:
  - 0
explanation: "Le **Crease** tend l'arête par un simple réglage, sans géométrie de plus. Une boucle de maintien marche aussi, mais elle ajoute des arêtes. Monter le niveau ne tend rien : la pièce reste aussi molle, en plus fin."
```

### Étape 2 · Le shrinkwrap : à quoi il sert
**Nouveau :** le modificateur *Shrinkwrap* et son *Offset*. **Déjà vu :** la pile de modificateurs, *Solidify*.

Le *Shrinkwrap* déplace chaque sommet d'un objet jusqu'à une surface cible, comme un film rétractable chauffé sur une forme. L'objet garde son propre maillage : seuls ses sommets bougent. Tant que le modificateur n'est pas appliqué, rien n'est détruit.

### Pourquoi il est partout en design de transport
Le shrinkwrap répond à un besoin de tous les jours :
- les carrosseries, les nez de train et les fuselages sont des surfaces à double courbure, tendues et continues ;
- les détails doivent s'y poser exactement : prises d'air, grilles, cadres de vitre, joints, logos, trappes, optiques ;
- la carrosserie change à chaque revue de design : un détail conformé suit chaque modification, sans être remodelé ;
- le détail se dessine à plat, simplement et au millimètre, d'après un croquis ou un profil de CAO. Le shrinkwrap le pose ensuite sur la courbe ;
- on ne découpe pas la carrosserie pour y loger le détail : son maillage reste propre, et ses reflets aussi.

Le même principe sert à conformer un maillage à une surface de référence : un scan, une surface importée de la CAO, ou une forme sculptée qu'on retopologise.

![Figure 2.39 : Deux trappes d'accès de 200 × 150 mm sur un fuselage de 2 m de diamètre. De profil, la trappe restée plane décolle de 3 mm à ses bords ; la trappe conformée épouse la courbe.](assets/images/shrinkwrap_principle_flat_vs_wrapped_blender.jpg)

### Recette · Conformer et décoller
Sur `E2_Pratique_Plaque`, une plaque de numéro de rame de 300 × 120 mm, posée devant le nez de tram `E2_Nez` :
- **1.** Sélectionnez la plaque. Dans l'onglet *Modifiers* (la clé à molette), *Add Modifier > Deform > Shrinkwrap*.
- **2.** Champ *Target* : la pipette, puis un clic sur le nez. Vous pouvez aussi choisir `E2_Nez` dans la liste.
- **3.** La plaque épouse le nez. Elle garde ses sommets ; seules leurs positions changent.
- **4.** La plaque scintille par plaques : elle est exactement sur la surface du nez, et les deux se disputent l'affichage. Champ *Offset* : tapez `0.2mm`. Le scintillement disparaît.
Dès que le menu *Add Modifier* est ouvert, vous pouvez aussi taper le nom du modificateur : la recherche démarre au clavier.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_modifier_deform_menu_blender.jpg"
caption: "Figure 2.40 : Le sous-menu Deform du menu Add Modifier, avec Shrinkwrap."
title: "Où trouver le Shrinkwrap"
---
Le Shrinkwrap est un modificateur de déformation : il déplace des sommets sans en créer. Il se trouve dans le sous-menu Deform du bouton Add Modifier. Maj + A, la souris au-dessus de l'onglet Modifiers, ouvre le même menu.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/shrinkwrap_panel_default_blender.jpg"
caption: "Figure 2.41 : Le panneau Shrinkwrap avec ses réglages par défaut : Wrap Method, Snap Mode, Target, Offset et Vertex Group."
title: "Le panneau Shrinkwrap"
---
Wrap Method choisit comment chaque sommet trouve la surface ; Nearest Surface Point, le réglage par défaut, l'envoie au point le plus proche. Snap Mode et Vertex Group servent à l'étape 3. Target désigne la surface cible, Offset l'écart entre le détail et cette surface.
```

![Figure 2.42 : La plaque conformée en Material Preview : à Offset 0, elle scintille par plaques ; à 0,2 mm, elle est nette.](assets/images/shrinkwrap_offset_z_fighting_blender.jpg)

### Recette · Donner l'épaisseur
Toujours sur la plaque :
- **1.** *Add Modifier > Generate > Solidify*. Il se range sous le *Shrinkwrap*.
- **2.** *Thickness* : `2mm` ; *Offset* : `1`. L'épaisseur part vers l'extérieur, perpendiculaire à la courbe.
- **3.** Option : faites glisser le *Solidify* au-dessus du *Shrinkwrap*, par la poignée à droite de son en-tête. L'épaisseur disparaît : ses deux faces sont posées sur le nez. Remettez-le en dessous.

### Le Solidify en dessous
Chaque modificateur travaille sur le résultat du précédent. Placé après le Shrinkwrap, le Solidify épaissit une plaque déjà courbée. Placé avant, il épaissit une plaque plane, puis le Shrinkwrap pose ses deux faces sur la même surface.

![Figure 2.43 : Solidify sous le Shrinkwrap, la plaque a 2 mm d'épaisseur (à gauche) ; Solidify au-dessus, ses deux faces sont posées sur le nez et l'épaisseur disparaît (à droite).](assets/images/shrinkwrap_solidify_stack_order_blender.jpg)

### Option : la cible change, le détail suit
Sélectionnez le nez `E2_Nez`, `Tab`, puis déplacez un sommet de la cage au centre : `G Y = -30mm`. La plaque suit la nouvelle forme, sans rien refaire. `Ctrl + Z` pour revenir. C'est tout l'intérêt du shrinkwrap pendant les revues de design.

Rendu attendu : une plaque de 2 mm d'épaisseur, posée sur le nez sans scintiller, sans bord qui décolle.

> [!WARNING]
> **Erreurs fréquentes**
> - Rien ne bouge : le champ *Target* est vide, ou il désigne la plaque elle-même.
> - La plaque reste plane, seuls ses coins bougent : elle n'a que quatre sommets. Le shrinkwrap ne déplace que des sommets ; un détail doit en avoir assez pour se courber (étape 4).
> - La plaque disparaît dans le nez : l'*Offset* du *Solidify* vaut -1. Tapez `1`.
> - L'épaisseur a disparu : le *Solidify* est au-dessus du *Shrinkwrap*.

> [!CAUTION]
> **Petit défi · Le monogramme (automobile).** Posez `E2_Defi_Monogramme`, une plaque ovale de 120 × 60 mm, sur le capot `E2_Capot`, avec 2 mm d'épaisseur et sans scintillement. Le corrigé est dans la sous-collection « Corrigé étape 2 ».

```quiz
question: "Votre plaque, posée par Shrinkwrap sur le nez du tram, scintille par plaques. Que faites-vous ?"
options:
  - "Régler Offset à 0,2 mm"
  - "Monter la subdivision du nez"
  - "Passer en Nearest Vertex"
  - "Appliquer le modificateur"
correctIndices:
  - 0
explanation: "La plaque est exactement sur la surface, et les deux surfaces se disputent l'affichage. Un **Offset** de quelques dixièmes de millimètre la décolle, sans que l'œil le voie."
```

### Étape 3 · Trois cas d'usage
**Nouveau :** un réglage par cas : *Snap Mode*, puis le mode *Project*, puis la limitation par groupe de sommets. **Déjà vu :** *Shrinkwrap*, *Offset*, *Solidify* en dessous.

La collection `Etape_3_Cas_usage` montre les trois cas terminés : `E3_Exemple_Hublot` sur le fuselage, `E3_Exemple_Bandeau` sur le nez de tram et `E3_Exemple_Prise` sur le capot. Observez-les, puis ouvrez leur pile.

### Recette · Aéronautique : le cadre de hublot
Sur `E3_Pratique_Cadre`, un cadre plat de 280 × 380 mm, à moitié enfoncé dans le fuselage `E3_Fuselage` :
- **1.** *Add Modifier > Deform > Shrinkwrap*, *Target* `E3_Fuselage`, *Offset* `0.2mm`.
- **2.** Une partie du cadre scintille ou disparaît. Ses sommets partaient de l'intérieur du fuselage. Or en *Snap Mode* *On Surface*, le réglage par défaut, l'*Offset* s'applique dans le sens du trajet du sommet : vers l'intérieur.
- **3.** *Snap Mode* : *Above Surface*. Tout le cadre passe 0,2 mm au-dessus de la surface, d'où que partent ses sommets.
- **4.** *Add Modifier > Generate > Solidify*, *Thickness* `4mm`, *Offset* `1`.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/shrinkwrap_snap_mode_menu_blender.jpg"
caption: "Figure 2.44 : Le menu Snap Mode du Shrinkwrap : On Surface, Inside, Outside, Outside Surface et Above Surface."
title: "Les choix de Snap Mode"
---
Snap Mode décide de quel côté le détail se pose. Inside ne déplace que les sommets qui sont dehors : le détail reste dans le volume. Outside ne déplace que ceux qui sont dedans : le détail ne s'enfonce jamais. Outside Surface et Above Surface gardent toujours l'Offset vers l'extérieur.
```

![Figure 2.45 : Le cadre de hublot sur le fuselage : en On Surface, ses côtés partis de l'intérieur restent cachés ; en Above Surface, tout le cadre est dehors.](assets/images/porthole_frame_fuselage_blender.jpg)

### Recette · Ferroviaire : le bandeau sur le nez
Sur `E3_Pratique_Bandeau`, une bande de 1 400 × 60 mm dessinée de face, à 300 mm devant le nez `E3_Nez` :
- **1.** *Shrinkwrap*, *Target* `E3_Nez`, *Offset* `0.2mm`. En *Nearest Surface Point*, chaque sommet va au point le plus proche : vue de face, la bande se tord vers les côtés du nez.
- **2.** *Wrap Method* : *Project*, puis cochez l'axe *Y*. La bande se projette sur le nez droit devant elle. Vue de face (`1` du pavé numérique), elle garde exactement son tracé.
- **3.** *Negative* et *Positive* règlent le sens de la projection le long de l'axe ; *Positive* est coché par défaut. Option : `G Y = 1000mm` place la bande derrière le nez, et elle ne le trouve plus. Cochez *Negative* : elle le retrouve. `Ctrl + Z` deux fois.
- **4.** *Face Cull* vaut *Off* par défaut. Sur *Back*, il ignore les faces vues de dos : sur une carrosserie fermée, un sommet ne se pose pas sur la face intérieure.
- **5.** *Add Modifier > Generate > Solidify*, *Thickness* `2mm`, *Offset* `1`.

```side-by-side
layout: "textRight"
imagePath: "assets/images/shrinkwrap_project_panel_blender.jpg"
caption: "Figure 2.46 : Les réglages du mode Project : Limit, Subdivision Levels, Axis, Negative, Positive, Face Cull, Invert Cull et Auxiliary Target."
title: "Les réglages de Project"
---
Axis choisit l'axe de la projection ; sans axe coché, Project suit les normales du détail. Limit borne la distance de projection. Subdivision Levels sert à l'étape 4. Auxiliary Target ajoute une seconde surface cible, utile quand un détail chevauche deux pièces.
```

![Figure 2.47 : Le nez de tram vu de face : le bandeau en Project reste droit (à gauche) ; en Nearest Surface Point, il se tord vers les côtés (à droite).](assets/images/tram_nose_band_project_vs_nearest_blender.jpg)

> [!TIP]
> *Project* garde le dessin tel qu'on le voit dans l'axe choisi. C'est le mode des bandeaux de livrée, des logos et des grilles dessinés de face ou de dessus, d'après un croquis.

### Recette · Automobile : la prise d'air sur le capot
Sur `E3_Pratique_Prise`, un bossage de 300 × 200 mm avec une lèvre avant de 35 mm de haut, posé au-dessus du capot `E3_Capot` :
- **1.** *Shrinkwrap*, *Target* `E3_Capot`. Toute la prise d'air s'aplatit sur le capot : chaque sommet a été conformé.
- **2.** `Tab`, puis `1` : la sélection des sommets. Les sommets du bord arrière et des côtés sont déjà sélectionnés dans le fichier. Sinon, `Alt + clic` sur les boucles du bord, avec `Maj` pour ajouter.
- **3.** `Ctrl + G > Assign to New Group` : un groupe de sommets, au poids 1. Dans l'onglet *Object Data* (le triangle vert), rubrique *Vertex Groups*, double-cliquez sur son nom et tapez `Raccord`.
- **4.** `Tab`. Dans le *Shrinkwrap*, champ *Vertex Group* : `Raccord`. Seul le bord se pose sur le capot ; la lèvre retrouve sa hauteur.
- **5.** Option, pour un raccord plus doux : `Tab`, sélectionnez la rangée de sommets voisine du bord, réglez *Weight* à `0.5` dans la rubrique *Vertex Groups*, puis cliquez sur *Assign*. Le poids dose l'effet : à 1, tout l'effet ; à 0, aucun effet.
- **6.** *Solidify*, *Thickness* `2mm`, *Offset* `-1`.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/vertex_group_menu_ctrl_g_blender.jpg"
caption: "Figure 2.48 : Le menu Vertex Groups (Ctrl + G) du Mode Édition, avec Assign to New Group."
title: "Créer un groupe de sommets"
---
En Mode Édition, Ctrl + G ouvre le menu des groupes de sommets. Assign to New Group crée un groupe avec les sommets sélectionnés, au poids 1. D'autres entrées apparaissent dès qu'un groupe existe : ajouter au groupe actif, retirer.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/vertex_groups_panel_weight_blender.jpg"
caption: "Figure 2.49 : L'onglet Object Data, rubrique Vertex Groups : la liste des groupes, les boutons Assign, Remove, Select et Deselect, et le champ Weight."
title: "La rubrique Vertex Groups"
---
La liste montre les groupes de l'objet ; un double-clic renomme un groupe. En Mode Édition, Assign ajoute la sélection au groupe actif avec le poids du champ Weight, et Remove l'en retire. Select et Deselect retrouvent les sommets d'un groupe.
```

![Figure 2.50 : Trois prises d'air sur le capot : sans groupe, elle s'aplatit et scintille (à gauche) ; avec le bord au poids 1 et la rangée voisine à 0,5 (au centre) ; avec un dégradé de poids, son arrière se fond dans le capot (à droite).](assets/images/hood_scoop_vertex_group_blender.jpg)

> [!NOTE]
> Les deux flèches à droite du champ *Vertex Group* inversent le groupe : le shrinkwrap agit alors partout, sauf sur le groupe.

Rendu attendu : un cadre de hublot de 4 mm sans scintillement, un bandeau droit vu de face, une prise d'air dont le bord se fond dans le capot. Comparez avec les exemples, puis avec la sous-collection « Corrigé étape 3 ».

> [!WARNING]
> **Erreurs fréquentes**
> - *Project* ne fait rien : aucun axe n'est coché et les normales du détail ne regardent pas la cible ; ou bien la cible est derrière le détail et seul *Positive* est coché.
> - Des sommets du bandeau restent en l'air : la projection ne rencontre pas le nez, parce que le dessin dépasse sa silhouette. Raccourcissez le dessin.
> - Le groupe de sommets n'a aucun effet : son nom n'est pas choisi dans le champ *Vertex Group*, ou les poids valent 0.
> - La prise d'air reste plate : le groupe contient tous les sommets. `Tab`, sélectionnez la lèvre, puis cliquez sur *Remove*.

> [!CAUTION]
> **Petit défi · Deux hublots de plus (aéronautique).** Sur le cadre terminé : `Maj + D`, puis `G X = 500mm`, deux fois. Chaque copie garde son modificateur et reste conformée. Modifiez ensuite la courbure du fuselage en Mode Édition : les trois cadres suivent.
>
> **★ La grille de capot (automobile).** `E3_Defi_Grille` est une grille de six ouïes, dessinée à plat au-dessus du capot. Posez-la avec *Project* suivant Z, puis donnez-lui 3 mm d'épaisseur. Le corrigé est dans la sous-collection « Corrigé étape 3 ».

```quiz
question: "Un bandeau dessiné de face doit garder exactement son tracé vu de face, une fois posé sur le nez. Quel mode choisissez-vous ?"
options:
  - "Nearest Surface Point"
  - "Project, avec l'axe Y"
  - "Nearest Vertex"
  - "Target Normal Project"
correctIndices:
  - 1
explanation: "**Project** déplace chaque sommet le long de l'axe choisi : vu dans cet axe, le dessin ne bouge pas. Les autres modes vont au point le plus proche, et le tracé se tord là où la surface tourne."
```

```quiz
question: "Sur la prise d'air, à quoi sert le groupe de sommets choisi dans le champ Vertex Group ?"
options:
  - "À limiter le Shrinkwrap aux sommets du groupe, selon leur poids"
  - "À choisir la surface cible"
  - "À donner l'épaisseur"
  - "À masquer la prise d'air au rendu"
correctIndices:
  - 0
explanation: "Seuls les sommets du groupe sont conformés, d'autant plus que leur **poids** est proche de 1. Le bord se pose sur le capot ; la lèvre, hors du groupe, garde sa hauteur."
```

### Étape 4 · Les réglages et l'ordre dans la pile
**Nouveau :** les deux derniers modes, puis la place du *Shrinkwrap* par rapport à *Subdivision*. **Déjà vu :** les étapes 1 à 3.

### Les quatre modes du Shrinkwrap
`E4_Exemple_Modes` montre quatre bandes conformées sur une main courante volontairement grossière, à 12 pans. Chaque mode a son usage :
- *Nearest Surface Point*, le réglage par défaut : chaque sommet va au point le plus proche. C'est le mode le plus courant, pour des détails petits devant la courbure.
- *Project* : chaque sommet se projette suivant un axe, ou suivant sa normale. Il garde le tracé d'un dessin.
- *Nearest Vertex* : chaque sommet va au sommet le plus proche de la cible. Il sert à recaler un maillage sur un autre de même topologie, par exemple une copie retouchée sur l'original. Sur une cible légère, le détail s'effondre sur quelques sommets.
- *Target Normal Project* : comme *Nearest Surface Point*, mais en suivant les normales lissées de la cible. Les sommets se répartissent plus régulièrement sur une cible peu dense. Il est plus lent.

Sur la main courante, les 287 sommets d'une bande n'occupent que 203 positions en *Nearest Surface Point* : des sommets se superposent sur les arêtes du tube. En *Target Normal Project* et en *Project*, ils restent tous distincts. En *Nearest Vertex*, la bande s'effondre sur 6 sommets.

![Figure 2.51 : Les quatre modes sur une main courante à 12 pans, en fil de fer : Nearest Surface Point, Project, Nearest Vertex (la bande effondrée ne se voit plus) et Target Normal Project.](assets/images/shrinkwrap_four_modes_blender.jpg)

### Recette · Le Shrinkwrap et la subdivision
Sur `E4_Pratique_Cadre_8`, un cadre de hublot grossier, à 8 côtés seulement, au-dessus du fuselage `E4_Fuselage` :
- **1.** *Shrinkwrap*, *Target* `E4_Fuselage`, *Offset* `0.2mm`, *Snap Mode* *Above Surface*. Seuls ses 16 sommets sont posés : entre eux, les côtés droits s'enfoncent dans la courbe.
- **2.** *Add Modifier > Generate > Subdivision Surface*, puis montez-le au-dessus du *Shrinkwrap* : menu de son en-tête, *Move to First*. Choisissez *Simple* et *Levels Viewport* `3`. Les côtés reçoivent des sommets, que le *Shrinkwrap* pose sur la courbe : le cadre colle partout, et il garde ses 8 côtés.
- **3.** Choisissez *Catmull-Clark*, puis *Move to Last* : le lissage arrive après la pose. Le cadre s'arrondit, mais il quitte la surface par endroits et s'enfonce ailleurs.
- **4.** Retenez l'ordre : *Subdivision* au-dessus, en *Catmull-Clark* pour un cadre rond ou en *Simple* pour garder les angles ; puis *Shrinkwrap* ; puis *Solidify* (`4mm`, *Offset* `1`).
- **5.** Option : en mode *Project*, le champ *Subdivision Levels* subdivise le détail le temps du calcul. Il évite un modificateur de plus.

![Figure 2.52 : Le cadre à 8 côtés sur le fuselage : seul, il s'enfonce entre ses sommets ; avec une Subdivision Simple au-dessus du Shrinkwrap, il colle partout ; avec une Subdivision Catmull-Clark en dessous, il décolle et s'enfonce par endroits.](assets/images/shrinkwrap_subdivision_order_blender.jpg)

> [!TIP]
> L'ordre type d'un détail conformé : d'abord ce qui ajoute des sommets (*Subdivision*), puis *Shrinkwrap*, puis ce qui donne l'épaisseur (*Solidify*). *Smooth by Angle* reste toujours en bas.

> [!NOTE]
> Pour poser un objet entier sans le déformer, comme une vis, un rivet ou un écusson rigide, l'onglet *Object Constraints* propose une contrainte *Shrinkwrap*. Elle déplace l'objet, pas ses sommets.

> [!WARNING]
> **Erreurs fréquentes**
> - Le détail s'enfonce entre ses sommets : il n'a pas assez de sommets. Placez une *Subdivision* au-dessus du *Shrinkwrap*.
> - Le détail décolle et s'enfonce par endroits : une *Subdivision* *Catmull-Clark* est sous le *Shrinkwrap*. Montez-la.
> - *Move to First* est grisé : le modificateur est déjà en tête de la pile.

> [!CAUTION]
> **Petit défi · Le jonc d'aile (automobile).** `E4_Defi_Jonc` est un jonc chromé de 600 × 12 mm, très léger (6 segments), au-dessus du capot `E4_Capot`. Trouvez la pile qui le rend lisse, collé au capot, avec 3 mm d'épaisseur. Le corrigé est dans la sous-collection « Corrigé étape 4 ».

```quiz
question: "Un cadre à 8 côtés, conformé sur le fuselage, s'enfonce dans la courbe entre ses sommets. Que faites-vous ?"
options:
  - "Ajouter une Subdivision au-dessus du Shrinkwrap"
  - "Ajouter une Subdivision en dessous du Shrinkwrap"
  - "Monter l'Offset à 10 mm"
  - "Passer en Nearest Vertex"
correctIndices:
  - 0
explanation: "Le Shrinkwrap ne déplace que des sommets. Une **Subdivision placée avant lui** en ajoute, et il les pose tous sur la courbe. Placée après, elle lisse le résultat et le décolle de la surface."
```

```quiz
question: "Dans quel ordre empilez-vous les modificateurs d'un détail conformé, de haut en bas ?"
options:
  - "Solidify, Shrinkwrap, Subdivision"
  - "Subdivision, Shrinkwrap, Solidify"
  - "Shrinkwrap, Solidify, Subdivision"
  - "L'ordre ne change rien"
correctIndices:
  - 1
explanation: "D'abord ce qui ajoute des sommets, puis la pose, puis l'épaisseur. Un **Solidify** placé avant le Shrinkwrap voit ses deux faces posées sur la surface : l'épaisseur disparaît."
```

### Palier 2 · Découpes et normales
Le second palier dure environ 55 minutes. Il découpe des pièces sans les détruire, puis, en ★★, il nettoie l'ombrage autour des découpes. Point d'arrêt : les quiz 7 et 8.

### Étape 5 · Les booléens non destructifs
**Nouveau :** découper une pièce avec un objet de coupe, sans la détruire. **Déjà vu :** la pile, le modificateur *Bevel*, le mode *Project* (étape 3).

L'exemple `E5_Exemple_Porte` est un panneau de portière bombé, avec le logement d'une poignée affleurante. Son objet de coupe, `E5_Exemple_Coupe`, est affiché en fil de fer. Déplacez-le : le logement suit.

### Recette · Découper le hublot
Sur `E5_Pratique_Fuselage`, un tronçon de fuselage avec sa peau de 3 mm. L'objet de coupe `E5_Coupe_Hublot` est un pavé aux coins arrondis de 230 × 330 mm, qui traverse la peau :
- **1.** Sélectionnez le fuselage. *Add Modifier > Generate > Boolean*.
- **2.** *Difference* est l'opération par défaut. Champ *Object* : `E5_Coupe_Hublot`.
- **3.** La peau est percée, mais l'objet de coupe la cache encore.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/boolean_panel_difference_solver_blender.jpg"
caption: "Figure 2.53 : Le panneau Boolean : les opérations Intersect, Union et Difference, l'objet de coupe et le solveur."
title: "Le panneau Boolean"
---
Difference retire le volume de l'objet de coupe ; Union l'ajoute ; Intersect ne garde que la partie commune. Operand Type permet de couper avec toute une collection. Solver vaut Exact par défaut : c'est le plus fiable.
```

### Recette · Ranger l'objet de coupe
Sélectionnez `E5_Coupe_Hublot`, puis ouvrez l'onglet *Object* (le carré orange) :
- **1.** Rubrique *Viewport Display*, *Display As* : *Wire*, ou *Bounds* pour une simple boîte.
- **2.** Rubrique *Visibility* : décochez *Renders*. *Display As* ne change que la vue 3D ; sans ce réglage, l'objet de coupe apparaîtrait au rendu.
- **3.** Déplacez l'objet de coupe : `G X = 100mm`. Le trou suit. `Ctrl + Z`. Faites-le tourner ou changez son échelle : le trou change aussi. La découpe reste vivante.

```side-by-side
layout: "textRight"
imagePath: "assets/images/object_viewport_display_as_blender.jpg"
caption: "Figure 2.54 : L'onglet Object, rubrique Viewport Display dépliée : Display As réglé sur Wire."
title: "Display As"
---
Display As change seulement l'affichage dans la vue 3D. En Wire, l'objet de coupe n'est plus qu'un fil de fer : la découpe se voit au travers, et l'objet reste facile à sélectionner. Bounds le réduit à sa boîte englobante.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/object_visibility_renders_blender.jpg"
caption: "Figure 2.55 : L'onglet Object, rubrique Visibility dépliée : Renders décoché dans la ligne Show In."
title: "Absent du rendu"
---
La ligne Show In décide où l'objet apparaît. Décochez Renders pour l'objet de coupe : il reste visible dans la vue, mais ne figure plus au rendu ni dans les images exportées au chapitre 4.
```

### Recette · L'ordre avec le Bevel
Sur le fuselage percé :
- **1.** *Add Modifier > Generate > Bevel* : il se range sous le *Boolean*. *Amount* : `1mm` ; *Segments* : `3` ; *Limit Method* sur *Angle*, le réglage par défaut.
- **2.** Le bord du trou s'arrondit : le biseau s'applique au résultat de la découpe.
- **3.** Faites glisser le *Bevel* au-dessus du *Boolean* : le bord du trou redevient vif. Remettez-le en dessous.
Le champ *Solver* propose aussi *Float*, plus rapide mais fragile sur des faces superposées, et *Manifold*, rapide mais qui exige deux maillages fermés, sans trou.

![Figure 2.56 : Le bord haut de la découpe en MatCap de contrôle : Bevel au-dessus du Boolean, le bord reste vif (à gauche) ; Bevel en dessous, il s'arrondit (à droite).](assets/images/boolean_bevel_order_blender.jpg)

Rendu attendu : un fuselage percé d'une découpe de hublot aux bords arrondis de 1 mm, sans objet de coupe visible au rendu.

> [!WARNING]
> **Erreurs fréquentes**
> - Rien n'est découpé : l'objet de coupe ne traverse pas la peau. Il doit la dépasser des deux côtés.
> - Tout disparaît, sauf la découpe : l'opération est *Intersect*. Choisissez *Difference*.
> - L'objet de coupe apparaît au rendu : *Renders* est resté coché.
> - Le bord du trou est vif : le *Bevel* est au-dessus du *Boolean*.
> - Des traînées d'ombrage autour du trou : c'est l'objet de l'étape 6.

> [!CAUTION]
> **Petit défi · La ligne de joint d'une trappe de visite (ferroviaire).** Sur le nez `E5_Defi_Nez`, dont la peau fait 6 mm, creusez la ligne de joint d'une trappe de 300 × 200 mm : une rainure de 4 mm de large et 3 mm de profondeur. L'objet de coupe `E5_Defi_Coupe_Joint` est l'anneau de la rainure, dessiné de face, à plat. Conformez-le avec *Project* suivant Y, *Offset* `0`, puis donnez-lui son volume : *Solidify* `6mm`, *Offset* `0`. Il déborde de 3 mm de chaque côté de la surface : la rainure a partout la même profondeur, même là où le nez tourne. Faites ensuite la découpe, sans *Bevel* : une ligne de joint reste vive. Le corrigé est dans la sous-collection « Corrigé étape 5 ».

### Le piège de la dépendance circulaire
Conformez l'objet de coupe sur E5_Nez_reference, la copie du nez masquée et non découpée, jamais sur le nez qu'il découpe. Sinon, le nez dépend de l'objet de coupe, qui dépend du nez : Blender ne peut pas calculer une pièce qui dépend d'elle-même, et le Boolean ne fait rien.

![Figure 2.57 : L'anneau de la ligne de joint, conformé en Project sur E5_Nez_reference, la copie du nez non découpée.](assets/images/boolean_cutter_reference_surface_blender.jpg)

```quiz
question: "Votre objet de coupe est conformé par Shrinkwrap sur le nez même qu'il découpe. Le Boolean ne fait rien. Pourquoi ?"
options:
  - "Le solveur Exact ne gère pas le Shrinkwrap"
  - "Le nez dépend de l'objet de coupe, qui dépend du nez : la dépendance est circulaire"
  - "L'objet de coupe est affiché en Wire"
  - "Il faut appliquer le Shrinkwrap"
correctIndices:
  - 1
explanation: "Blender ne peut pas calculer une pièce qui dépend d'elle-même. Conformez l'objet de coupe sur une copie du nez non découpée : la **surface de référence**."
```

### Étape 6 ★★ · Des normales propres
**Nouveau :** corriger l'ombrage sans toucher à la forme, en remplaçant les normales. **Déjà vu :** *Shade Auto Smooth*, la découpe de l'étape 5, la surface de référence.

Autour d'une découpe dans une surface courbe et lissée, le booléen crée des faces longues et fines. Le lissage les interpole mal : des traînées et un halo apparaissent dans les reflets. La forme est juste ; seul l'ombrage est faux. On remplace donc les normales de la zone par celles d'une surface saine.

![Figure 2.58 : La découpe de hublot en MatCap de contrôle : des traînées dans les reflets autour du trou (à gauche) ; avec Data Transfer, les bandes de reflet restent continues (à droite).](assets/images/boolean_shading_vs_data_transfer_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/matcap_reflection_check_blender.jpg"
caption: "Figure 2.59 : Le menu Viewport Shading en mode Solid : éclairage MatCap, image check_reflection_horizontal."
title: "Lire les reflets"
---
Option conseillée pour cette étape : dans le menu Viewport Shading, en Solid, choisissez l'éclairage MatCap, puis l'image check_reflection_horizontal. Elle dessine des bandes de reflet, comme les néons d'une cabine de contrôle qualité. Une bande cassée ou qui tremble signale un défaut. Retour : Studio.
```

### Recette · Data Transfer
Sur `E6_Pratique_Fuselage`, la découpe de l'étape 5, avec ses traînées. `E6_Fuselage_reference` est le même fuselage sans découpe, au même niveau de subdivision, masqué :
- **1.** *Add Modifier > Edit > Data Transfer*. Il se range au-dessus de *Smooth by Angle*, sous le *Bevel*.
- **2.** *Source* : `E6_Fuselage_reference`.
- **3.** Dépliez la rubrique *Face Corner Data* (sa flèche), cochez sa case, puis choisissez *Custom Normals*. Dans la même rubrique, *Mapping* : *Nearest Face Interpolated*.
- **4.** Dépliez la rubrique *Topology Mapping*, cochez *Max Distance* et tapez `0.3mm` : seules les faces posées sur la surface de référence reçoivent ses normales. Les flancs de la découpe gardent les leurs.
- **5.** Les normales en dernier : cliquez sur l'épingle (*Pin to Last*), tout à droite de l'en-tête de *Smooth by Angle*. Puis, dans le menu de l'en-tête de *Data Transfer*, *Move to Last*.
- **6.** Les traînées disparaissent. Cochez et décochez l'écran du modificateur dans son en-tête pour comparer.

```side-by-side
layout: "textRight"
imagePath: "assets/images/add_modifier_edit_menu_blender.jpg"
caption: "Figure 2.60 : Le sous-menu Edit du menu Add Modifier, avec Data Transfer."
title: "Où trouver Data Transfer"
---
Data Transfer copie des données d'un objet vers un autre : des normales, des couleurs, des UV. Il se trouve dans le sous-menu Edit du menu Add Modifier, avec les modificateurs qui modifient des données sans changer la forme.
```

![Figure 2.61 : Le panneau Data Transfer : la source, la rubrique Face Corner Data dépliée (Custom Normals, Mapping) et, à droite, la rubrique Topology Mapping avec la case Max Distance.](assets/images/data_transfer_panel_custom_normals_blender.jpg)

> [!IMPORTANT]
> **Pourquoi les normales en dernier ?** *Smooth by Angle* décide quelles arêtes restent vives. Placé sous *Data Transfer*, il recalcule ces arêtes après le transfert et le dérègle : des plaques et de grands triangles apparaissent. Placé au-dessus, il fixe d'abord les arêtes vives, puis *Data Transfer* règle les normales. La surface de référence doit aussi avoir le même niveau de subdivision que la pièce : sinon, les deux surfaces ne coïncident plus, et le transfert ne prend que par endroits.

### Recette · Weighted Normal
Sur `E6_Pratique_Platine`, une platine de rétroviseur plane, biseautée et percée de quatre trous par un *Boolean*. Des triangles d'ombrage barrent sa face :
- **1.** *Add Modifier > Normals > Weighted Normal*.
- **2.** Cochez *Keep Sharp* : les arêtes vives restent vives.
- **3.** Comme pour *Data Transfer* : épingle de *Smooth by Angle* désactivée, puis *Move to Last* sur *Weighted Normal*.
- **4.** La face redevient uniforme : les grandes faces imposent leur normale aux petites.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_modifier_normals_menu_blender.jpg"
caption: "Figure 2.62 : Le sous-menu Normals du menu Add Modifier : Normal Edit et Weighted Normal."
title: "Le sous-menu Normals"
---
Le sous-menu Normals réunit les modificateurs qui règlent les normales sans toucher à la forme. Weighted Normal est celui du défi ; Normal Edit oriente les normales vers un point ou une direction, pour des effets plus rares.
```

![Figure 2.63 : La platine percée en MatCap de contrôle : des triangles d'ombrage barrent sa face (à gauche) ; avec Weighted Normal, la face redevient uniforme (à droite).](assets/images/weighted_normal_plate_blender.jpg)

### Data Transfer ou Weighted Normal ?
Choisissez selon la pièce :
- *Weighted Normal* pour une pièce à faces planes : platine, boîtier, carter. Il suffit d'un modificateur ;
- *Data Transfer* pour une surface courbe : il faut une surface de référence saine, à la même place et au même niveau de subdivision.

Dans les deux cas, l'ordre de fin de pile est le même : *Smooth by Angle*, puis le modificateur qui règle les normales, tout en bas.

> [!NOTE]
> Jusqu'à Blender 4.0, il fallait cocher *Auto Smooth* pour que *Data Transfer* et *Weighted Normal* agissent. Cette case n'existe plus depuis Blender 4.1 : les tutoriels plus anciens la demandent encore. Autre point : une *Subdivision* placée sous *Data Transfer* ignore les normales transférées, sauf si sa case *Use Custom Normals* est cochée (figure 2.37). Gardez *Data Transfer* tout en bas.

> [!WARNING]
> **Erreurs fréquentes**
> - Rien ne change : *Face Corner Data* n'est pas coché, ou la source est la pièce découpée elle-même.
> - Les flancs de la découpe sont faux, comme aplatis : *Max Distance* n'est pas coché, ou sa valeur est trop grande.
> - Des plaques et de grands triangles apparaissent : *Smooth by Angle* est resté sous *Data Transfer*.
> - Le transfert ne prend que par endroits : la référence n'a pas le même niveau de subdivision que la pièce.
> - La surface de référence a été déplacée : les normales ne correspondent plus. Elle doit rester à la même place que la pièce.

> [!CAUTION]
> **Petit défi · La ligne de joint du nez de tram (ferroviaire).** Nettoyez l'ombrage autour de la ligne de joint du petit défi de l'étape 5, avec *Data Transfer* depuis `E5_Nez_reference`. Le corrigé est dans la sous-collection « Corrigé étape 6 ».

```quiz
question: "Une platine plane, biseautée et percée montre des triangles d'ombrage. Quel modificateur les corrige le plus simplement ?"
options:
  - "Data Transfer"
  - "Weighted Normal"
  - "Subdivision Surface"
  - "Triangulate"
correctIndices:
  - 1
explanation: "**Weighted Normal** donne aux petites faces la normale des grandes faces voisines : la face plane redevient uniforme. Data Transfer demande une surface de référence ; il sert surtout sur les surfaces courbes."
```

### Atelier · Le rétroviseur extérieur
L'atelier dure environ 35 minutes. Il n'apporte aucune notion nouvelle : il réinvestit les étapes 1 à 6 sur un objet complet, un rétroviseur automobile d'environ 250 mm de large. Toutes ses pièces sont dans la collection `Atelier_Retroviseur`, sans modificateur :
- `Retro_Coque` : la cage de la coque, ouverte à l'arrière, avec ses boucles de maintien au bord de l'ouverture ;
- `Retro_Miroir` : la glace, plane ;
- `Retro_Miroir_reference` : une calotte de sphère de 1 400 mm de rayon, en fil de fer et absente du rendu. Le miroir côté passager est convexe : il élargit le champ de vision ;
- `Retro_Clignotant` : le répétiteur de clignotant, dessiné de face, devant la coque ;
- `Retro_Pied` et `Retro_Platine` : le pied et la platine de fixation sur la portière ;
- `Retro_Coupe_Platine` : quatre cylindres, pour trois vis et le passage du câble.

![Figure 2.64 : Le rétroviseur terminé en Material Preview, vu de l'arrière avec son miroir convexe, puis de l'avant avec son clignotant.](assets/images/side_mirror_workshop_blender.jpg)

### Consignes · Le rétroviseur, par paliers
Les valeurs sont indicatives : adaptez-les à votre dessin.
- **1. La coque (étape 1).** `Ctrl + 2`, puis *Solidify* : *Thickness* `2.5mm`, *Offset* `-1`, *Even Thickness* coché. Vérifiez en MatCap de contrôle que l'ouverture reste tendue.
- **2. Le miroir (étapes 2 et 3).** *Shrinkwrap* sur `Retro_Miroir_reference` : la glace se bombe d'environ 4 mm. Puis *Solidify* `2mm`, *Offset* `-1`.
- **3. Le clignotant (étape 3).** *Shrinkwrap* en *Project*, axe Y, *Snap Mode* *Above Surface*, *Offset* `0.2mm`, sur `Retro_Coque`. Puis *Solidify* `1.5mm`, *Offset* `1`.
- **4. Le pied.** *Bevel*, *Amount* `4mm`, 3 segments, puis *Shade Auto Smooth*.
- **5. La platine (étape 5).** *Boolean* *Difference* avec `Retro_Coupe_Platine`, en *Wire* et sans rendu ; puis *Bevel*, *Amount* `0.8mm`, 3 segments, *Limit Method* sur *Angle*.
- **6. ★★ La platine propre (étape 6).** *Weighted Normal*, *Keep Sharp*, sous *Smooth by Angle*.
- **7. ★★ Le logement du clignotant (étapes 5 et 6).** Faites une copie de référence de la coque : `Maj + D`, clic droit, renommée `Retro_Coque_reference`, sans *Solidify*, masquée, sans rendu. Tirez du clignotant un objet de coupe (`Maj + D`), conformé sur cette référence, avec un *Solidify* `3mm`, *Offset* `0` : il creuse un logement de 1,5 mm. Le clignotant vise lui aussi la référence et descend dans le logement : *Offset* `-0.6mm`. Enfin, *Data Transfer* depuis la référence, sous *Smooth by Angle*.
Le corrigé est dans la sous-collection « Corrigé atelier », paliers ★★ compris.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/side_mirror_convex_reference_blender.jpg"
caption: "Figure 2.65 : Le miroir conformé et, derrière lui, sa calotte de référence de 1 400 mm de rayon, en fil de fer."
title: "Un miroir convexe par shrinkwrap"
---
La glace est dessinée à plat ; le Shrinkwrap la pose sur une calotte de sphère, la surface de référence. Pour un miroir plus ou moins bombé, il suffit de changer le rayon de la calotte, sans toucher à la glace.
```

### Le logement du clignotant
Le logement est creusé par un objet de coupe tiré du clignotant et conformé sur la copie de référence de la coque. Data Transfer, depuis la même référence, rend aux reflets leur continuité autour du logement.

![Figure 2.66 : ★★ Le logement du clignotant en MatCap de contrôle : traînées autour du logement sans Data Transfer (à gauche), reflets continus avec (à droite).](assets/images/side_mirror_indicator_recess_blender.jpg)

> [!CAUTION]
> **Variantes ★★, sans corrigé, pour retrouver votre métier.**
> - **Ferroviaire, le cadre de vitre frontale :** sur le nez `E3_Nez`, dessinez de face le cadre d'une vitre frontale de tram, avec son joint, et posez-le avec *Project*.
> - **Aéronautique, le hublot complet :** sur `E3_Fuselage`, découpez le hublot avec un *Boolean*, posez son cadre avec un *Shrinkwrap* en *Above Surface*, puis une vitre en retrait de 8 mm.

### Pour aller plus loin
Le modificateur *Lattice* déforme d'un coup tout un ensemble de pièces avec une cage simple. Il sert à essayer une proportion, par exemple étirer tout le rétroviseur, détails compris.
