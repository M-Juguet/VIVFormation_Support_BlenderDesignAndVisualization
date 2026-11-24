## Modélisation avancée

> [!NOTE]
> Ce défi est **facultatif** : il n'est pas prévu au programme de base. Il prolonge le chapitre 2 et s'adresse à ceux qui sont à l'aise avec lui, ou qui maîtrisent déjà ces sujets. Vous pouvez le faire après le chapitre 2, s'il vous reste du temps, ou à la place de ses parties de base. Il demande de savoir ajouter un modificateur, le régler et changer sa place dans la pile (Basics 103, section 3). Si vous le faites à la place du chapitre 2, vous pouvez reprendre le chapitre 3 avec son fichier de secours, `PRC02_ch3_lampe_a_habiller.blend`, ou avec `PRC02_ch2_lampe_modele.blend`, enregistré sous `lampe_modele_v001.blend`. C'est une option, pas une obligation.

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

![Figure D1.1 : Le banc du défi, une rangée par étape : surfaces de référence, exemples et pièces à travailler, puis le rétroviseur de l'atelier.](assets/images/modeling_challenge_overview_blender.jpg)

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

![Figure D1.2 : Trois carters de projecteur avec la même cage et la même subdivision : sans rien de plus (un savon), avec des boucles de maintien, avec un Crease de 1. À droite, la même rangée en MatCap de contrôle des reflets.](assets/images/subdivision_holding_loops_crease_blender.jpg)

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
caption: "Figure D1.3 : Une boucle de maintien, sélectionnée à 4 mm de l'arête du dessus, en Mode Édition."
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
caption: "Figure D1.4 : Le menu Edge du Mode Édition, avec Edge Crease (Maj + E)."
title: "Le menu Edge"
---
Le menu Edge réunit les commandes qui agissent sur les arêtes sélectionnées. Edge Crease y figure avec son raccourci, Maj + E. Pendant le geste, tapez la valeur voulue, de 0 à 1, puis validez avec Entrée.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/subdivision_advanced_use_creases_blender.jpg"
caption: "Figure D1.5 : Le panneau Subdivision Surface, rubrique Advanced dépliée : Use Creases est coché par défaut."
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
caption: "Figure D1.6 : Le capot du petit défi, en MatCap de contrôle des reflets : nervure molle à gauche, nervure tendue par un Crease de 0,8 à droite."
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

![Figure D1.7 : Deux trappes d'accès de 200 × 150 mm sur un fuselage de 2 m de diamètre. De profil, la trappe restée plane décolle de 3 mm à ses bords ; la trappe conformée épouse la courbe.](assets/images/shrinkwrap_principle_flat_vs_wrapped_blender.jpg)

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
caption: "Figure D1.8 : Le sous-menu Deform du menu Add Modifier, avec Shrinkwrap."
title: "Où trouver le Shrinkwrap"
---
Le Shrinkwrap est un modificateur de déformation : il déplace des sommets sans en créer. Il se trouve dans le sous-menu Deform du bouton Add Modifier. Maj + A, la souris au-dessus de l'onglet Modifiers, ouvre le même menu.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/shrinkwrap_panel_default_blender.jpg"
caption: "Figure D1.9 : Le panneau Shrinkwrap avec ses réglages par défaut : Wrap Method, Snap Mode, Target, Offset et Vertex Group."
title: "Le panneau Shrinkwrap"
---
Wrap Method choisit comment chaque sommet trouve la surface ; Nearest Surface Point, le réglage par défaut, l'envoie au point le plus proche. Snap Mode et Vertex Group servent à l'étape 3. Target désigne la surface cible, Offset l'écart entre le détail et cette surface.
```

![Figure D1.10 : La plaque conformée en Material Preview : à Offset 0, elle scintille par plaques ; à 0,2 mm, elle est nette.](assets/images/shrinkwrap_offset_z_fighting_blender.jpg)

### Recette · Donner l'épaisseur
Toujours sur la plaque :
- **1.** *Add Modifier > Generate > Solidify*. Il se range sous le *Shrinkwrap*.
- **2.** *Thickness* : `2mm` ; *Offset* : `1`. L'épaisseur part vers l'extérieur, perpendiculaire à la courbe.
- **3.** Option : faites glisser le *Solidify* au-dessus du *Shrinkwrap*, par la poignée à droite de son en-tête. L'épaisseur disparaît : ses deux faces sont posées sur le nez. Remettez-le en dessous.

### Le Solidify en dessous
Chaque modificateur travaille sur le résultat du précédent. Placé après le Shrinkwrap, le Solidify épaissit une plaque déjà courbée. Placé avant, il épaissit une plaque plane, puis le Shrinkwrap pose ses deux faces sur la même surface.

![Figure D1.11 : Solidify sous le Shrinkwrap, la plaque a 2 mm d'épaisseur (à gauche) ; Solidify au-dessus, ses deux faces sont posées sur le nez et l'épaisseur disparaît (à droite).](assets/images/shrinkwrap_solidify_stack_order_blender.jpg)

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
caption: "Figure D1.12 : Le menu Snap Mode du Shrinkwrap : On Surface, Inside, Outside, Outside Surface et Above Surface."
title: "Les choix de Snap Mode"
---
Snap Mode décide de quel côté le détail se pose. Inside ne déplace que les sommets qui sont dehors : le détail reste dans le volume. Outside ne déplace que ceux qui sont dedans : le détail ne s'enfonce jamais. Outside Surface et Above Surface gardent toujours l'Offset vers l'extérieur.
```

![Figure D1.13 : Le cadre de hublot sur le fuselage : en On Surface, ses côtés partis de l'intérieur restent cachés ; en Above Surface, tout le cadre est dehors.](assets/images/porthole_frame_fuselage_blender.jpg)

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
caption: "Figure D1.14 : Les réglages du mode Project : Limit, Subdivision Levels, Axis, Negative, Positive, Face Cull, Invert Cull et Auxiliary Target."
title: "Les réglages de Project"
---
Axis choisit l'axe de la projection ; sans axe coché, Project suit les normales du détail. Limit borne la distance de projection. Subdivision Levels sert à l'étape 4. Auxiliary Target ajoute une seconde surface cible, utile quand un détail chevauche deux pièces.
```

![Figure D1.15 : Le nez de tram vu de face : le bandeau en Project reste droit (à gauche) ; en Nearest Surface Point, il se tord vers les côtés (à droite).](assets/images/tram_nose_band_project_vs_nearest_blender.jpg)

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
caption: "Figure D1.16 : Le menu Vertex Groups (Ctrl + G) du Mode Édition, avec Assign to New Group."
title: "Créer un groupe de sommets"
---
En Mode Édition, Ctrl + G ouvre le menu des groupes de sommets. Assign to New Group crée un groupe avec les sommets sélectionnés, au poids 1. D'autres entrées apparaissent dès qu'un groupe existe : ajouter au groupe actif, retirer.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/vertex_groups_panel_weight_blender.jpg"
caption: "Figure D1.17 : L'onglet Object Data, rubrique Vertex Groups : la liste des groupes, les boutons Assign, Remove, Select et Deselect, et le champ Weight."
title: "La rubrique Vertex Groups"
---
La liste montre les groupes de l'objet ; un double-clic renomme un groupe. En Mode Édition, Assign ajoute la sélection au groupe actif avec le poids du champ Weight, et Remove l'en retire. Select et Deselect retrouvent les sommets d'un groupe.
```

![Figure D1.18 : Trois prises d'air sur le capot : sans groupe, elle s'aplatit et scintille (à gauche) ; avec le bord au poids 1 et la rangée voisine à 0,5 (au centre) ; avec un dégradé de poids, son arrière se fond dans le capot (à droite).](assets/images/hood_scoop_vertex_group_blender.jpg)

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

![Figure D1.19 : Les quatre modes sur une main courante à 12 pans, en fil de fer : Nearest Surface Point, Project, Nearest Vertex (la bande effondrée ne se voit plus) et Target Normal Project.](assets/images/shrinkwrap_four_modes_blender.jpg)

### Recette · Le Shrinkwrap et la subdivision
Sur `E4_Pratique_Cadre_8`, un cadre de hublot grossier, à 8 côtés seulement, au-dessus du fuselage `E4_Fuselage` :
- **1.** *Shrinkwrap*, *Target* `E4_Fuselage`, *Offset* `0.2mm`, *Snap Mode* *Above Surface*. Seuls ses 16 sommets sont posés : entre eux, les côtés droits s'enfoncent dans la courbe.
- **2.** *Add Modifier > Generate > Subdivision Surface*, puis montez-le au-dessus du *Shrinkwrap* : menu de son en-tête, *Move to First*. Choisissez *Simple* et *Levels Viewport* `3`. Les côtés reçoivent des sommets, que le *Shrinkwrap* pose sur la courbe : le cadre colle partout, et il garde ses 8 côtés.
- **3.** Choisissez *Catmull-Clark*, puis *Move to Last* : le lissage arrive après la pose. Le cadre s'arrondit, mais il quitte la surface par endroits et s'enfonce ailleurs.
- **4.** Retenez l'ordre : *Subdivision* au-dessus, en *Catmull-Clark* pour un cadre rond ou en *Simple* pour garder les angles ; puis *Shrinkwrap* ; puis *Solidify* (`4mm`, *Offset* `1`).
- **5.** Option : en mode *Project*, le champ *Subdivision Levels* subdivise le détail le temps du calcul. Il évite un modificateur de plus.

![Figure D1.20 : Le cadre à 8 côtés sur le fuselage : seul, il s'enfonce entre ses sommets ; avec une Subdivision Simple au-dessus du Shrinkwrap, il colle partout ; avec une Subdivision Catmull-Clark en dessous, il décolle et s'enfonce par endroits.](assets/images/shrinkwrap_subdivision_order_blender.jpg)

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
caption: "Figure D1.21 : Le panneau Boolean : les opérations Intersect, Union et Difference, l'objet de coupe et le solveur."
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
caption: "Figure D1.22 : L'onglet Object, rubrique Viewport Display dépliée : Display As réglé sur Wire."
title: "Display As"
---
Display As change seulement l'affichage dans la vue 3D. En Wire, l'objet de coupe n'est plus qu'un fil de fer : la découpe se voit au travers, et l'objet reste facile à sélectionner. Bounds le réduit à sa boîte englobante.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/object_visibility_renders_blender.jpg"
caption: "Figure D1.23 : L'onglet Object, rubrique Visibility dépliée : Renders décoché dans la ligne Show In."
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

![Figure D1.24 : Le bord haut de la découpe en MatCap de contrôle : Bevel au-dessus du Boolean, le bord reste vif (à gauche) ; Bevel en dessous, il s'arrondit (à droite).](assets/images/boolean_bevel_order_blender.jpg)

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

![Figure D1.25 : L'anneau de la ligne de joint, conformé en Project sur E5_Nez_reference, la copie du nez non découpée.](assets/images/boolean_cutter_reference_surface_blender.jpg)

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

![Figure D1.26 : La découpe de hublot en MatCap de contrôle : des traînées dans les reflets autour du trou (à gauche) ; avec Data Transfer, les bandes de reflet restent continues (à droite).](assets/images/boolean_shading_vs_data_transfer_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/matcap_reflection_check_blender.jpg"
caption: "Figure D1.27 : Le menu Viewport Shading en mode Solid : éclairage MatCap, image check_reflection_horizontal."
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
caption: "Figure D1.28 : Le sous-menu Edit du menu Add Modifier, avec Data Transfer."
title: "Où trouver Data Transfer"
---
Data Transfer copie des données d'un objet vers un autre : des normales, des couleurs, des UV. Il se trouve dans le sous-menu Edit du menu Add Modifier, avec les modificateurs qui modifient des données sans changer la forme.
```

![Figure D1.29 : Le panneau Data Transfer : la source, la rubrique Face Corner Data dépliée (Custom Normals, Mapping) et, à droite, la rubrique Topology Mapping avec la case Max Distance.](assets/images/data_transfer_panel_custom_normals_blender.jpg)

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
caption: "Figure D1.30 : Le sous-menu Normals du menu Add Modifier : Normal Edit et Weighted Normal."
title: "Le sous-menu Normals"
---
Le sous-menu Normals réunit les modificateurs qui règlent les normales sans toucher à la forme. Weighted Normal est celui du défi ; Normal Edit oriente les normales vers un point ou une direction, pour des effets plus rares.
```

![Figure D1.31 : La platine percée en MatCap de contrôle : des triangles d'ombrage barrent sa face (à gauche) ; avec Weighted Normal, la face redevient uniforme (à droite).](assets/images/weighted_normal_plate_blender.jpg)

### Data Transfer ou Weighted Normal ?
Choisissez selon la pièce :
- *Weighted Normal* pour une pièce à faces planes : platine, boîtier, carter. Il suffit d'un modificateur ;
- *Data Transfer* pour une surface courbe : il faut une surface de référence saine, à la même place et au même niveau de subdivision.

Dans les deux cas, l'ordre de fin de pile est le même : *Smooth by Angle*, puis le modificateur qui règle les normales, tout en bas.

> [!NOTE]
> Jusqu'à Blender 4.0, il fallait cocher *Auto Smooth* pour que *Data Transfer* et *Weighted Normal* agissent. Cette case n'existe plus depuis Blender 4.1 : les tutoriels plus anciens la demandent encore. Autre point : une *Subdivision* placée sous *Data Transfer* ignore les normales transférées, sauf si sa case *Use Custom Normals* est cochée (figure D1.5). Gardez *Data Transfer* tout en bas.

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

![Figure D1.32 : Le rétroviseur terminé en Material Preview, vu de l'arrière avec son miroir convexe, puis de l'avant avec son clignotant.](assets/images/side_mirror_workshop_blender.jpg)

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
caption: "Figure D1.33 : Le miroir conformé et, derrière lui, sa calotte de référence de 1 400 mm de rayon, en fil de fer."
title: "Un miroir convexe par shrinkwrap"
---
La glace est dessinée à plat ; le Shrinkwrap la pose sur une calotte de sphère, la surface de référence. Pour un miroir plus ou moins bombé, il suffit de changer le rayon de la calotte, sans toucher à la glace.
```

### Le logement du clignotant
Le logement est creusé par un objet de coupe tiré du clignotant et conformé sur la copie de référence de la coque. Data Transfer, depuis la même référence, rend aux reflets leur continuité autour du logement.

![Figure D1.34 : ★★ Le logement du clignotant en MatCap de contrôle : traînées autour du logement sans Data Transfer (à gauche), reflets continus avec (à droite).](assets/images/side_mirror_indicator_recess_blender.jpg)

> [!CAUTION]
> **Variantes ★★, sans corrigé, pour retrouver votre métier.**
> - **Ferroviaire, le cadre de vitre frontale :** sur le nez `E3_Nez`, dessinez de face le cadre d'une vitre frontale de tram, avec son joint, et posez-le avec *Project*.
> - **Aéronautique, le hublot complet :** sur `E3_Fuselage`, découpez le hublot avec un *Boolean*, posez son cadre avec un *Shrinkwrap* en *Above Surface*, puis une vitre en retrait de 8 mm.

### Pour aller plus loin
Le modificateur *Lattice* déforme d'un coup tout un ensemble de pièces avec une cage simple. Il sert à essayer une proportion, par exemple étirer tout le rétroviseur, détails compris.
