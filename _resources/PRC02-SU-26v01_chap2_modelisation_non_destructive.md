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
- **1.** Sélectionnez *Bras_bas*. `Tab`, `A`, puis `S`, `Maj + Z` deux fois et `0.5` : la tige passe à 8 mm de diamètre, sans changer de longueur. Le bras est incliné : le second `Maj + Z` prend son axe propre, comme `G Z Z` au chapitre 1. Avec un seul, la tige se redresserait et quitterait ses articulations.
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

Dans l'onglet *Object* de la grille, réglez *Display As* sur *Wire* (rubrique *Viewport Display*) et décochez *Renders* (rubrique *Visibility*) : elle ne sert plus que d'outil. Les figures D1.22 et D1.23 du défi « Modélisation avancée » (rubrique « Pour aller plus loin ») montrent ces deux rubriques.
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
> **Pour aller plus loin :** le défi « Modélisation avancée », dans la rubrique « Pour aller plus loin » de la barre latérale : surfaces tendues, détails conformés avec le *Shrinkwrap* et découpes avec le *Boolean*, sur des pièces des trois secteurs. Il est facultatif et hors programme : gardez-le pour quand ce chapitre vous paraît acquis.
