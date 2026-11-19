## 1. Principled BSDF : métal, plastique, verre

> [!NOTE]
> Ce chapitre part de la lampe modélisée au chapitre 2. Il réutilise l'onglet *Material* et le mode *Material Preview* (Basics 101), le compteur d'utilisateurs d'une donnée partagée (initiation) et la vue locale (chapitre 1) : ils servent ici sans être redits. Les captures et les libellés correspondent à Blender 5.2 LTS, avec l'interface en anglais. Pour ceux qui connaissent déjà ces sujets, la section 4 propose un défi facultatif sur les matières procédurales.

### Où l'on en est
La lampe de bureau a été bloquée au chapitre 1, puis modélisée au chapitre 2. Dans ce chapitre, vous l'habillez : une matière par pièce, des finitions réalistes, puis une bibliothèque pour réutiliser vos matières. Au chapitre 4, vous la mettrez en scène et vous en tirerez des visuels.

Le mot **CMF** signifie *Color, Material, Finish* : la couleur, la matière et la finition. C'est le métier qui choisit les teintes, les matières et les finitions d'un produit : la sellerie d'un train, la planche de bord d'une voiture, l'habillage d'une cabine d'avion.

À la fin de la demi-journée, vous savez :
- régler une matière de métal, de plastique ou de verre avec le Principled BSDF ;
- ajouter une finition brossée, grainée ou structurée, sans dépliage UV ;
- ranger vos matières en actifs dans l'Asset Browser, et récupérer une matière d'un autre fichier avec *File > Append*.

![Figure 3.1 : Le but du chapitre : la lampe habillée en deux coloris, en Material Preview. À gauche, le coloris A (laque verte, aluminium brossé, chrome) ; à droite, le coloris B de l'atelier.](assets/images/lamp_cmf_target_blender.jpg)

```resource
title: "Fichier d'exercice : la lampe à habiller"
description: "Le fichier de secours du chapitre : la lampe modélisée au chapitre 2, sans matière, et le texte LISEZ-MOI avec les consignes de chaque partie. Les corrigés sont dans les collections masquées « Corrigé coloris A » (sections 1 à 3) et « Corrigé coloris B » (atelier) ; leurs matières portent le suffixe _corrige. Enregistrez-le sous lampe_habillage_v001.blend avant de commencer."
fileName: "PRC02_ch3_lampe_a_habiller.blend (0.2 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch3_lampe_a_habiller.blend"
```

### Recette · Prendre le fichier en main
Partez de votre lampe du chapitre 2. Ouvrez-la, puis vérifiez cinq points déjà vus (2 à 6) : une matière se pose mieux sur un modèle propre.
- **1.** Ouvrez `lampe_modele_v001.blend`, puis enregistrez-le aussitôt sous `lampe_habillage_v001.blend` (*File > Save As*).
- **2.** Chaque pièce porte un nom clair dans la collection *Lampe*.
- **3.** L'échelle est appliquée : *Scale* à 1 dans `N > Item`. Sinon, `Ctrl + A > Scale`.
- **4.** Les normales regardent vers l'extérieur : aucune face rouge en *Face Orientation*.
- **5.** Aucune pièce courbe ne montre de facettes, en particulier les tiges des bras et les articulations, qui seront en métal. Sinon, *Object > Shade Auto Smooth*.
- **6.** Le moteur de rendu est EEVEE, dans l'onglet *Render* : le fichier du chapitre 1 était réglé sur Cycles.
Un modèle incomplet ou abîmé ? Ouvrez le fichier de secours `PRC02_ch3_lampe_a_habiller.blend` et enregistrez-le sous `lampe_habillage_v001.blend`. Ne passez pas plus de cinq minutes à réparer un modèle : le fichier de secours est fait pour cela.

> [!TIP]
> Vous avez gardé votre propre lampe ? Le corrigé n'est pas dans votre fichier : il est dans `PRC02_ch3_lampe_a_habiller.blend`. Ouvrez-le dans une seconde fenêtre de Blender, puis cliquez sur l'œil de la collection *Corrigé coloris A* pour l'afficher.

### Voir les matières : Material Preview
En mode *Solid*, la vue 3D n'affiche pas les matières : elle montre seulement les formes. Le mode *Material Preview* calcule les matières avec EEVEE, sous une image d'environnement intégrée à Blender. C'est suffisant pour juger une matière : tout ce chapitre se fait dans ce mode.

L'éclairage de la scène, le mode *Rendered* et les réglages d'EEVEE appartiennent au chapitre 4.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/material_preview_button_blender.jpg"
caption: "Figure 3.2 : Les boutons de mode d'affichage, en haut à droite de la vue 3D (agrandis dans le médaillon) : Material Preview est actif. La lampe n'a pas encore de matière : elle reste blanche."
title: "Le bouton Material Preview"
---
Les boutons de mode d'affichage se trouvent en haut à droite de la vue 3D. *Material Preview* est celui qui suit *Solid*.

La première bascule fige l'écran quelques secondes : Blender prépare ses calculs de matières. C'est normal, et cela ne se reproduit pas ensuite.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/material_preview_popover_blender.jpg"
caption: "Figure 3.3 : Le menu Viewport Shading en Material Preview : l'image d'environnement, sa rotation, World Opacity, et les cases Scene Lights et Scene World."
title: "Option : choisir l'image d'environnement"
---
La petite flèche à droite des boutons ouvre le menu *Viewport Shading*, vu au chapitre 1. En *Material Preview*, il propose une vignette : un clic dessus ouvre la liste des images d'environnement intégrées, comme *studio* ou *city*.

*Rotation* fait tourner l'image autour de la lampe : les reflets glissent sur les pièces. C'est ainsi qu'on juge une finition. *Scene Lights* et *Scene World* restent décochées : elles serviront au chapitre 4.
```

### Créer et nommer une matière
Une matière se crée dans l'éditeur de propriétés, onglet *Material* (la sphère rouge). Le bouton *New* crée une matière et la donne à l'objet actif. Nommez-la tout de suite, par un double-clic sur son nom.

Une convention simple aide à s'y retrouver : la matière, puis la finition ou la teinte. Par exemple `Alu_Brosse`, `ABS_Noir` ou `Peinture_Vert`.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/material_tab_new_blender.jpg"
caption: "Figure 3.4 : L'onglet Material d'une pièce sans matière : la liste des emplacements, vide, et le bouton New."
title: "Le bouton New"
---
Tant qu'une pièce n'a pas de matière, l'onglet *Material* montre une liste vide et le bouton *New*.

*New* sur une pièce qui a déjà une matière en crée une nouvelle, nommée `Material.001` : renommez-la aussitôt.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/material_tab_surface_blender.jpg"
caption: "Figure 3.5 : La rubrique Surface d'une nouvelle matière : Principled BSDF, puis Base Color, Metallic, Roughness, IOR, Alpha, Thin Wall, Normal, et les rubriques repliées."
title: "Le Principled BSDF"
---
La rubrique *Surface* indique *Principled BSDF* : c'est le modèle de surface de Blender. Un seul modèle suffit pour presque toutes les matières : métal, plastique, peinture, verre.

*Base Color* règle la teinte. Les rubriques repliées (*Coat*, *Transmission*, *Emission*…) s'ouvrent d'un clic sur leur nom : chacune ajoute une propriété à la matière.
```

### Une matière pour plusieurs pièces
Une matière est une donnée, comme un maillage : plusieurs pièces peuvent la partager. Vous avez déjà vu ce principe avec les roues de la maquette, à l'initiation. Changer une matière partagée change toutes les pièces qui l'utilisent.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/material_browse_list_blender.jpg"
caption: "Figure 3.6 : La liste des matières existantes, ouverte à gauche du nom. Le chiffre 2 à droite du nom : deux pièces partagent Peinture_Vert."
title: "La liste des matières et le compteur"
---
L'icône à gauche du nom de la matière ouvre la liste des matières du fichier. Choisir une matière dans cette liste la donne à l'objet actif.

Le chiffre à droite du nom compte les pièces qui partagent la matière. Un clic sur ce chiffre crée une copie indépendante : vous vous en servirez pour une finition ou un coloris.
```

### Recette · Une peinture et un plastique partagés
Sur votre lampe, dans l'espace *Layout* :
- **1.** Passez la vue 3D en *Material Preview*.
- **2.** Sélectionnez le *Socle*. Onglet *Material*, *New*. Renommez la matière `Peinture_Vert` et choisissez une teinte dans *Base Color*.
- **3.** Sélectionnez la *Tête*. Dans la liste des matières, choisissez `Peinture_Vert` : le compteur affiche 2.
- **4.** Sélectionnez l'*Interrupteur*. *New*, puis renommez la matière `ABS_Noir` et choisissez un gris très sombre.
- **5.** Donnez `ABS_Noir` aux crans de l'interrupteur (*Interrupteur_crans*) et à la grille d'aération (*Grille_aeration*), par la liste.
Contrôle : socle et tête de la même teinte, interrupteur et grille en gris très sombre. Le compteur affiche 2 pour `Peinture_Vert` et 3 pour `ABS_Noir`. Corrigé : la collection *Corrigé coloris A*.

> [!WARNING]
> La grille d'aération a un *Empty* enfant, *Grille_pivot* : c'est la grille elle-même, *Grille_aeration*, qu'il faut sélectionner. Un *Empty* n'a pas d'onglet *Material*.

```side-by-side
layout: "textRight"
imagePath: "assets/images/link_materials_menu_blender.jpg"
caption: "Figure 3.7 : Astuce : Ctrl + L dans la vue 3D ouvre le menu Link/Transfer Data ; Link Materials donne la matière de l'objet actif à toute la sélection."
title: "Astuce : plusieurs pièces d'un coup"
---
Sélectionnez les pièces à habiller, puis en dernier celle qui porte la bonne matière : elle devient l'objet actif. `Ctrl + L > Link Materials` donne sa matière à toute la sélection.

C'est un raccourci : la liste des matières suffit pour ce chapitre.
```

### Métal ou non : Metallic
*Metallic* dit si la matière est un métal. Réglez-le à 0 pour un plastique, une peinture ou un verre, et à 1 pour un métal. Une valeur intermédiaire ne correspond à aucune matière réelle : la pièce paraît sale.

La couleur d'un métal se règle dans *Base Color* : gris clair pour l'aluminium, jaune doré pour le laiton.

### Du poli au mat : Roughness
*Roughness* règle la netteté des reflets : de 0, le miroir, à 1, le mat. Un chrome est autour de 0,03, un aluminium satiné autour de 0,3, un plastique mat autour de 0,6.

![Figure 3.8 : La grille du nuancier, en Material Preview. Rangée arrière : Metallic 1 ; rangée avant : Metallic 0. De gauche à droite : Roughness 0, 0,1, 0,2, 0,4, 0,6 et 1.](assets/images/metallic_roughness_grid_blender.jpg)

### Des valeurs de départ
Ces valeurs sont indicatives : composez votre propre gamme. Elles sont aussi dans le nuancier de la bibliothèque CMF (section 3).
- **Aluminium, inox, chrome, laiton :** *Metallic* 1, *Roughness* de 0,03 (chrome) à 0,4 (satiné), la teinte du métal dans *Base Color*.
- **Plastique brillant ou mat :** *Metallic* 0, *Roughness* de 0,15 à 0,6.
- **Caoutchouc, PVC :** *Metallic* 0, *Roughness* de 0,7 à 0,85, *Base Color* presque noire, jamais noire pure.
- **Laque :** *Metallic* 0, *Roughness* 0,4, *Coat Weight* 1, *Coat Roughness* 0,03.
- **Verre clair ou dépoli :** *Metallic* 0, *Roughness* 0 ou 0,4, *Transmission Weight* 1, IOR 1,5, *Thin Wall* pour une paroi fine.
- **Polycarbonate teinté :** *Metallic* 0, *Roughness* 0,05, *Transmission Weight* 1, IOR 1,58, *Base Color* teintée.

### Recette · L'aluminium des bras
Sur *Bras_bas*, puis *Bras_haut* :
- **1.** Sélectionnez *Bras_bas*. *New*, puis renommez la matière `Alu_Naturel`.
- **2.** *Metallic* à 1, *Roughness* à 0,3, *Base Color* gris très clair.
- **3.** Sélectionnez *Bras_haut* et choisissez `Alu_Naturel` dans la liste des matières.
Contrôle : les deux bras reflètent l'image d'environnement, avec des reflets un peu flous.

### Consignes · Le chrome, le câble et le plastique
À vous, d'après les valeurs de départ :
- `Chrome` sur les trois articulations ;
- `PVC_Mat_Noir` sur le câble ;
- la *Roughness* de `ABS_Noir`, à 0,15.
Contrôle : vue de face, en *Material Preview*. On distingue au premier regard le métal, aux reflets nets et colorés par l'environnement, et le plastique.

> [!WARNING]
> Des reflets en escalier sur une tige : *Shade Auto Smooth* manque (point 5 de la prise en main). Une pièce qui perd tout modelé : sa *Base Color* est noire pure ; gardez un gris très sombre. Le câble est une courbe : son onglet *Material* fonctionne comme celui d'un maillage.

### Laque et vernis : Coat
La rubrique *Coat* ajoute un vernis transparent par-dessus la teinte : une carrosserie, une livrée de train, un carénage peint. La peinture devient une laque.

### La rubrique Coat
Sur `Peinture_Vert`, dépliez la rubrique *Coat* : *Weight* à 1, *Roughness* à 0,03.

*Weight* règle la présence du vernis, *Roughness* sa netteté. Le reflet du vernis reste net, même si la peinture dessous est un peu mate.

![Figure 3.9 : À gauche, la rubrique Coat dépliée sur Peinture_Vert : Weight 1, Roughness 0,03. À droite, la tête prend un reflet net de laque.](assets/images/principled_coat_panel_blender.jpg)

### Le verre : Transmission
La rubrique *Transmission* laisse passer la lumière à travers la matière : *Weight* à 1 donne un verre. *Roughness* à 0 donne un verre clair, à 0,4 un verre dépoli. Une *Base Color* teintée donne un verre fumé ou un feu arrière.

L'IOR, l'indice de réfraction, dévie la lumière : 1,5 pour le verre, 1,58 pour le polycarbonate. Vous n'avez pas à le changer.

```side-by-side
layout: "textRight"
imagePath: "assets/images/principled_transmission_blender.jpg"
caption: "Figure 3.10 : La rubrique Transmission dépliée sur Verre_Clair : Weight 1. Roughness est à 0 et Thin Wall est coché."
title: "La rubrique Transmission"
---
Dépliez *Transmission* et réglez *Weight* à 1. Mettez *Roughness* à 0 pour un verre clair.

Si votre ampoule ne montre alors que le paysage de l'image d'environnement, c'est normal : il manque deux réglages, présentés juste après.
```

### Voir à travers le verre : deux interrupteurs
Sous EEVEE, un verre ne montre ce qui se trouve derrière lui que si deux cases sont cochées :
- la case *Raytracing*, dans l'onglet *Render* : sans elle, le verre ne réfracte pas ; le chapitre 4 explique ce réglage ;
- la case *Raytraced Transmission*, dans l'onglet *Material*, rubrique *Settings*.

Une seule case cochée ne change rien : il faut les deux.

![Figure 3.11 : L'ampoule vue par l'ouverture de la tête. À gauche, sans les deux cases : une boule sombre qui reflète l'environnement. Au milieu, avec les deux cases : le verre réfracte, comme une boule de cristal. À droite, avec Thin Wall en plus : une paroi fine, qui laisse voir la douille sans la déformer.](assets/images/glass_raytracing_comparison_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/render_raytracing_checkbox_blender.jpg"
caption: "Figure 3.12 : L'onglet Render : le moteur EEVEE et la case Raytracing, cochée."
title: "La case Raytracing"
---
L'onglet *Render* (l'appareil photo) montre le moteur de rendu, EEVEE, et ses rubriques. Cochez la case de la rubrique *Raytracing*.

Sans elle, le verre ne réfracte pas ; le chapitre 4 explique ce réglage. C'est la seule case de l'onglet *Render* de ce chapitre.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/material_settings_transmission_blender.jpg"
caption: "Figure 3.13 : L'onglet Material, rubrique Settings : Render Method, la case Raytraced Transmission cochée, et Thickness."
title: "La case Raytraced Transmission"
---
Dans l'onglet *Material*, faites défiler jusqu'à la rubrique *Settings*. Cochez *Raytraced Transmission*.

Cette case appartient à la matière : chaque matière de verre a la sienne.
```

### Un verre fin : Thin Wall
L'ampoule du chapitre 2 est un volume plein : avec la transmission, elle déforme ce qui est derrière elle, comme une boule de cristal. La case *Thin Wall*, en haut de la rubrique *Surface*, en fait une paroi fine : une ampoule, une vitre, un pare-brise.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/principled_thin_wall_blender.jpg"
caption: "Figure 3.14 : La case Thin Wall cochée, dans la rubrique Surface de Verre_Clair."
title: "La case Thin Wall"
---
*Thin Wall* se trouve sous *Alpha*. Cochée, elle traite la surface comme une paroi mince : plus de déformation.

Un polycarbonate en volume plein, comme un feu arrière, garde la case décochée.
```

### Recette · Le verre de l'ampoule
- **1.** Sélectionnez l'*Ampoule* et la *Tête*, puis isolez-les en vue locale (`/`).
- **2.** Sélectionnez l'*Ampoule*. *New*, puis renommez la matière `Verre_Clair`. *Transmission > Weight* à 1, *Roughness* à 0.
- **3.** Onglet *Render* : cochez *Raytracing*. Onglet *Material*, rubrique *Settings* : cochez *Raytraced Transmission*.
- **4.** Cochez *Thin Wall*.
- **5.** `/` pour quitter la vue locale.
Contrôle : en vue de dessous, la douille se voit à travers l'ampoule, sans déformation. Puis, à vous : essayez un verre dépoli (*Roughness* 0,4) ou fumé (*Base Color* grise), et gardez celui qui convient à votre lampe.

> [!WARNING]
> La case *Raytracing* n'apparaît pas : le moteur est resté sur Cycles (point 6 de la prise en main). Un poste devient lent : décochez *Raytracing* le temps des autres parties, puis recochez-la avant d'enregistrer. L'ampoule est une courbe avec un modificateur *Screw* : son onglet *Material* fonctionne comme celui d'un maillage.

> [!NOTE]
> **Une matière qui éclaire : Emission.** La rubrique *Emission* fait briller une matière : un voyant, un écran, un filament. *Color* règle la teinte, *Strength* l'intensité. Elle est proposée ici en défi : la lumière de la lampe appartient au chapitre 4.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/principled_emission_panel_blender.jpg"
caption: "Figure 3.15 : Défi : la rubrique Emission dépliée, Color vert et Strength 6. En dessous, l'interrupteur devient un voyant."
title: "Défi : un voyant lumineux"
---
Sur une copie de la matière de l'interrupteur, dépliez *Emission* : une couleur vive dans *Color*, puis *Strength* autour de 5.

En *Material Preview*, la pièce brille, mais elle n'éclaire pas encore ce qui l'entoure : l'éclairage est le travail du chapitre 4.
```

> [!NOTE]
> **Ce qu'EEVEE simplifie.** Trois réglages ne fonctionnent que sous Cycles, l'autre moteur de Blender : *Anisotropic* (rubrique *Specular*), le nœud *Bevel* et *Thin Film*. Le brossé se simule autrement, à la section 2 ; les arrondis viennent de la géométrie, avec le *Bevel* du chapitre 2.

### Option : deux matières sur une pièce
Une pièce peut porter plusieurs matières. Le bouton `+` à droite de la liste ajoute un emplacement (*slot*) ; donnez-lui une seconde matière, par exemple un blanc mat.

Sur la tête, le *Solidify* sait où poser cette seconde matière : sur l'intérieur de la coque (figure suivante).

![Figure 3.16 : Option : deux emplacements de matière sur la tête, Peinture_Vert et Blanc_Interieur. L'intérieur de l'abat-jour devient blanc.](assets/images/material_slots_two_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/solidify_material_offset_blender.jpg"
caption: "Figure 3.17 : Option : le modificateur Solidify de la tête, rubrique Materials : Material Offset à 1."
title: "Option : Material Offset du Solidify"
---
Dans l'onglet *Modifiers*, dépliez la rubrique *Materials* du *Solidify*. *Material Offset* à 1 donne à la face intérieure l'emplacement suivant : le blanc.

*Rim* fait de même pour la tranche de la coque.
```

> [!NOTE]
> **Ailleurs.** Les mêmes réglages habillent une jante en aluminium ou une planche de bord en plastique grainé (automobile), une main courante en inox ou une tablette de siège (ferroviaire), un carénage peint ou un hublot en polycarbonate (aéronautique).

```quiz
question: "Une pièce en aluminium ressemble à du plastique gris. Quel réglage corriger ?"
options:
  - "Metallic, à 1"
  - "Roughness, à 0"
  - "Une Base Color plus claire"
  - "Coat Weight, à 1"
correctIndices:
  - 0
explanation: "Metallic décide si la matière est un métal : 0 pour un plastique, 1 pour un métal. La teinte du métal se règle ensuite dans Base Color, et la netteté de ses reflets dans Roughness."
```

```quiz
question: "Votre ampoule montre le paysage de l'image d'environnement, mais pas la tête placée derrière elle. Que faut-il activer ?"
options:
  - "La case Raytracing de l'onglet Render seulement"
  - "La case Raytraced Transmission de la matière seulement"
  - "Les deux : Raytracing dans l'onglet Render et Raytraced Transmission dans la matière"
  - "La case Thin Wall"
correctIndices:
  - 2
explanation: "Sous EEVEE, le verre ne montre ce qui est derrière lui qu'avec les deux cases cochées. Thin Wall évite ensuite la déformation d'un volume plein."
```

```quiz
question: "Quel réglage ajoute un vernis brillant par-dessus une teinte ?"
options:
  - "Metallic"
  - "Roughness, à 0"
  - "Coat"
  - "Specular Tint"
correctIndices:
  - 2
explanation: "La rubrique Coat ajoute un vernis transparent : Weight 1 et une Roughness basse donnent une laque, comme sur une carrosserie."
```

> [!CAUTION]
> **Défi fil rouge.** Habillez toute la lampe d'après ces valeurs : laque du socle et de la tête, aluminium des bras, chrome des articulations, plastique de l'interrupteur, de la grille et du câble, verre de l'ampoule. Nommez chaque matière. Les teintes sont indicatives : composez votre propre gamme. Comparez avec la collection *Corrigé coloris A*.

## 2. Finitions CMF en projection triplanaire

> [!NOTE]
> Cette section part des matières de la section 1. Elle utilise l'espace de travail *Shading* (Basics 101), `Maj + A`, `G` et `X` comme dans la vue 3D, et `Ctrl + A > Scale` (Basics 103). Elle apporte le Shader Editor : on y retrouve d'abord la matière déjà réglée, puis chaque étape ajoute un seul nœud.

### Pourquoi pas de dépliage UV
Le dépliage UV sert à poser une image à un endroit précis : un logo, une étiquette, un marquage. Une finition uniforme, comme un grain, un brossé ou une peinture structurée, n'en a pas besoin : elle s'applique en 3D, directement d'après la position de la surface.

Ce chapitre ne déplie donc aucune pièce. C'est la méthode la plus rapide pour habiller un produit en revue de design.

### Le Shader Editor : la même matière, vue en nœuds
L'onglet *Shading*, en haut de la fenêtre, ouvre un espace de travail prévu pour les matières. La vue 3D est en *Material Preview*, et le Shader Editor occupe le bas de l'écran. L'éditeur de propriétés reste à droite.

Sélectionnez un bras : le Shader Editor montre sa matière sous forme de **nœuds**. Le nœud *Principled BSDF* porte les mêmes réglages que l'onglet *Material*. Le nœud *Material Output* reçoit ce que l'objet affiche.

![Figure 3.18 : L'espace de travail Shading : le navigateur de fichiers en haut à gauche (flouté ici), la vue 3D en Material Preview, le Shader Editor en bas, l'Outliner et l'éditeur de propriétés à droite.](assets/images/shading_workspace_blender.jpg)

### Un nœud, des entrées, des sorties
Un nœud a ses entrées à gauche et ses sorties à droite. Un **lien** relie la sortie d'un nœud à l'entrée d'un autre : ici, la sortie *BSDF* du Principled va dans l'entrée *Surface* de *Material Output*.

Changez *Roughness* dans le nœud : l'onglet *Material* suit. C'est la même matière, vue autrement.

![Figure 3.19 : À gauche, la matière Alu_Naturel en nœuds : Principled BSDF relié à Material Output. À droite, l'onglet Material affiche les mêmes valeurs.](assets/images/principled_node_vs_tab_blender.jpg)

### Se déplacer et agir dans le Shader Editor
Le Shader Editor se manie comme la vue 3D :
- la molette zoome, le clic molette déplace la vue ;
- `Origine` cadre tous les nœuds ;
- `G` déplace un nœud, `X` le supprime ;
- `Maj + A` ouvre le menu d'ajout.

Le Shader Editor est vide ? L'objet actif n'a pas de matière, ou ce n'est pas le bon objet.

### Ajouter un nœud et le relier
`Maj + A` ajoute un nœud, comme un objet dans la vue 3D. Pour relier deux nœuds, glissez d'une sortie vers une entrée. Pour défaire un lien, glissez-le hors de son entrée.

Une **texture procédurale** est calculée par Blender, sans image : elle n'a ni raccord ni limite de taille. La *Noise Texture* donne un bruit, comme des nuages. Son réglage *Scale* compte les motifs par mètre.

```side-by-side
layout: "textRight"
imagePath: "assets/images/shader_editor_add_menu_blender.jpg"
caption: "Figure 3.20 : Maj + A dans le Shader Editor : le menu Add, puis son sous-menu Texture, avec Noise Texture et Image Texture."
title: "Le menu Add du Shader Editor"
---
Le menu *Add* range les nœuds par familles : *Input*, *Shader*, *Displacement*, *Texture*, *Utilities*… Ce chapitre utilise *Texture*, *Input*, *Displacement* et *Utilities*.

Comme dans la vue 3D, tapez les premières lettres d'un nom pour le trouver plus vite.
```

![Figure 3.21 : Une Noise Texture reliée par sa sortie Color à l'entrée Base Color. À droite, la tige se couvre de nuages gris, étirés sur toute sa longueur.](assets/images/node_link_noise_base_color_blender.jpg)

### Recette · La matière en nœuds
Sur un bras de votre lampe :
- **1.** Passez dans l'espace *Shading*. Sélectionnez *Bras_bas* : le Shader Editor montre deux nœuds.
- **2.** Changez *Roughness* dans le nœud *Principled BSDF*, puis vérifiez l'onglet *Material* : il a suivi.
- **3.** Survolez le Shader Editor et faites `Origine` pour cadrer tous les nœuds.
- **4.** `Maj + A > Texture > Noise Texture`. Glissez sa sortie *Color* vers l'entrée *Base Color* du Principled : le bras se couvre de nuages.
- **5.** Glissez le lien hors de *Base Color* : le bras redevient uni. Gardez le nœud *Noise Texture* : il resservira.
Contrôle : chaque bras a montré des nuages gris, puis il est redevenu uni.

### Étape 1 · Les coordonnées : Texture Coordinate
Par défaut, une texture suit la boîte de l'objet (*Generated*) : sur un bras long et fin, le motif est étiré. Le nœud *Texture Coordinate*, sortie *Object*, garde la même taille de motif partout, quelle que soit la forme de la pièce.

La lampe est petite : *Scale* du *Noise* passe de 5 à 1000, soit environ un motif par millimètre.

![Figure 3.22 : Étape 1 : Texture Coordinate, sortie Object, reliée à l'entrée Vector du Noise (Scale 1000). À droite, le motif devient fin et régulier sur toute la tige.](assets/images/texture_coordinate_node_blender.jpg)

### Étape 2 · Du motif au relief : Bump
Le nœud *Bump* transforme un motif en relief, sans toucher à la géométrie : il agit sur la façon dont la surface reflète la lumière. Sa sortie *Normal* se relie à l'entrée *Normal* du Principled.

Sa force par défaut, *Strength* 1, est trop forte pour une pièce de quelques millimètres : le relief scintille. Baissez *Strength* à 0,2 et laissez *Distance* à sa valeur.

![Figure 3.23 : Étape 2 : la sortie Factor du Noise va dans Height du Bump, la sortie Normal du Bump va dans Normal du Principled. Strength est à 0,2. À droite, le motif devient un relief.](assets/images/noise_bump_chain_blender.jpg)

### Étape 3 · Étirer pour brosser : Mapping
Le nœud *Mapping*, placé entre *Texture Coordinate* et la texture, étire le motif. Avec *Scale* Z à 0,02, le grain s'allonge cinquante fois dans l'axe Z de la pièce : il devient des rayures fines. C'est un aluminium brossé.

Sur les bras, l'axe Z de chaque pièce suit la tige : leur rotation n'a pas été appliquée au chapitre 2, et c'est voulu.

![Figure 3.24 : Étape 3 : le nœud Mapping, Scale (1, 1, 0,02), entre Texture Coordinate et Noise ; Strength du Bump à 0,15. À droite, les rayures suivent la longueur de la tige.](assets/images/brushed_aluminium_blender.jpg)

### Recette · L'aluminium brossé
Sur `Alu_Naturel`, l'aluminium des bras, une étape à la fois :
- **1.** Reliez de nouveau la sortie *Color* du *Noise* à *Base Color* : le motif est étiré sur la longueur du bras.
- **2.** `Maj + A > Input > Texture Coordinate`. Reliez sa sortie *Object* à l'entrée *Vector* du *Noise*. Réglez *Scale* du *Noise* à 1000.
- **3.** Défaites le lien vers *Base Color*. `Maj + A > Displacement > Bump`. Reliez la sortie *Factor* du *Noise* à *Height*, puis la sortie *Normal* du *Bump* à l'entrée *Normal* du Principled. *Strength* à 0,2.
- **4.** `Maj + A > Utilities > Vector > Mapping`. Placez-le entre *Texture Coordinate* et *Noise*, reliez *Object* à son entrée *Vector* et sa sortie *Vector* au *Noise*. *Scale* Z à 0,02.
- **5.** *Strength* du *Bump* à 0,15. Renommez la matière `Alu_Brosse`.
Contrôle : sur chaque tige, les rayures suivent la longueur du bras. Corrigé : `Alu_Brosse_corrige`, dans la collection *Corrigé coloris A*.

### Consignes · Le grain de l'ABS
À vous : la même chaîne, sans *Mapping*, sur `ABS_Noir`. Un grain fin pour l'interrupteur et la grille : *Noise* *Scale* 1500, *Bump* *Strength* 0,05.

Pour ceux qui ont fini : microbillez les articulations, avec *Noise* *Scale* 2000, *Strength* 0,03 et *Roughness* 0,5.

> [!WARNING]
> Rien ne se voit : *Scale* du *Noise* est resté trop faible, un seul motif couvre la pièce. Un relief qui scintille : *Strength* est trop forte ; divisez-la par deux. Des rayures en travers : l'axe étiré dans *Mapping* n'est pas le bon ; essayez X ou Y.

### Une image projetée sur trois axes : Box
Une texture procédurale ne sait pas tout faire : un cuir, une tôle larmée ou une fibre de carbone se dessinent mieux en image. Sans dépliage UV, le nœud *Image Texture* projette l'image en 3D.

Son menu de projection propose :
- *Flat* : l'image est projetée d'un seul côté ; elle coule sur les flancs ;
- *Box* : l'image est projetée sur trois axes, d'où le nom de **projection triplanaire**. Chaque face prend la projection qui lui fait face ;
- *Blend* (avec *Box*) : fond les raccords entre les trois projections. À 0, les raccords se voient à 45° ; vers 0,25, ils se fondent et ne se remarquent plus sur une finition fine.

```resource
title: "Les images de finition (textures CMF)"
description: "Le dossier textures_cmf : cinq images raccordables, créées par VIV Formation et libres de droits (CC0). Quatre images de relief, à régler en Non-Color : grain_structure, grain_cuir, carbone_serge_relief, tole_larmee. Une image de couleur, en sRGB : carbone_serge_couleur. Décompressez le dossier à côté de votre fichier de travail."
fileName: "PRC02_ch3_textures_cmf.zip (0.2 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch3_textures_cmf.zip"
```

```resource
title: "Fichier de démonstration : les finitions triplanaires"
description: "Cinq pièces sans dépliage UV, une par secteur : deux accoudoirs en cuir grainé, une coque de rétroviseur grainée, un marchepied en tôle larmée et un panneau en fibre de carbone. Chaque matière a son Principled réglé et son image déjà chargée : à vous de compléter la chaîne. Le corrigé est dans la collection masquée « Corrigé ». Enregistrez-le sous finitions_v001.blend avant de commencer."
fileName: "PRC02_ch3_finitions_triplanaires.blend (0.4 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch3_finitions_triplanaires.blend"
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/image_texture_projection_menu_blender.jpg"
caption: "Figure 3.25 : Le nœud Image Texture et son menu de projection : Flat, Box, Sphere, Tube."
title: "Le menu de projection"
---
Le menu de projection est la deuxième liste du nœud *Image Texture*, sous *Linear*. Il est sur *Flat* par défaut.

Choisissez *Box* : un réglage *Blend* apparaît juste en dessous.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/image_texture_box_node_blender.jpg"
caption: "Figure 3.26 : Le nœud Image Texture réglé : projection Box, Blend 0,3, Color Space Non-Color."
title: "Le nœud réglé"
---
Le nœud réglé : *Box*, *Blend* entre 0,25 et 0,3, *Color Space* en *Non-Color*.

L'image elle-même se charge avec le bouton *Open* du nœud, puis le dossier `textures_cmf`.
```

![Figure 3.27 : La chaîne du cuir grainé : Texture Coordinate (Object), Mapping (Scale 25), Image Texture en Box avec Blend 0,3 et Non-Color, Bump (Strength 0,3), dont la sortie va dans Normal du Principled.](assets/images/leather_chain_armrest_blender.jpg)

![Figure 3.28 : Une image contrastée (la tôle larmée) projetée en Box sur une coque de rétroviseur, au raccord de deux projections. À gauche, Blend 0 : les larmes sont coupées net. À droite, Blend 0,2 : la transition se fond.](assets/images/box_blend_comparison_blender.jpg)

### Les images de données : Non-Color
Une image de relief n'est pas une couleur : c'est une donnée, une hauteur par pixel. Réglez son *Color Space* sur *Non-Color* : Blender lit alors ses valeurs telles quelles. Une image de couleur, comme celle du carbone, garde son réglage d'origine, *sRGB*.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/image_color_space_menu_blender.jpg"
caption: "Figure 3.29 : Le menu Color Space du nœud Image Texture : Non-Color pour une image de relief, sRGB pour une image de couleur."
title: "Le menu Color Space"
---
*Color Space* se règle dans le nœud *Image Texture*, sous la liste des réglages de l'image.

Un grain qui paraît trop contrasté, ou un peu coloré : il est resté en *sRGB*.
```

### L'échelle appliquée, condition de la projection
La projection suit les coordonnées *Object* de la pièce. Si l'échelle de la pièce n'est pas appliquée, ses coordonnées le sont aussi : la texture s'étire dans le même sens. `Ctrl + A > Scale` remet le grain d'aplomb, sans changer la forme. C'est le patient 2 de la clinique du fichier, à l'initiation.

![Figure 3.30 : Les deux accoudoirs du fichier de démonstration. À gauche, l'accoudoir du fond a une échelle X de 2 non appliquée : son grain s'étire en longueur. À droite, après Ctrl + A > Scale : les deux grains sont identiques.](assets/images/texture_scale_not_applied_blender.jpg)

### Recette · La peinture structurée du socle
Sur le socle de votre lampe :
- **1.** Rendez la laque du socle indépendante : un clic sur le compteur de `Peinture_Vert`, puis renommez la copie `Structure_Vert`. Même teinte, autre finition : c'est une décision CMF.
- **2.** *Coat Weight* à 0, *Roughness* à 0,6.
- **3.** `Maj + A > Texture > Image Texture`. Bouton *Open*, puis `textures_cmf/grain_structure.png`. *Color Space* : *Non-Color*. Projection *Box*, *Blend* 0,25.
- **4.** Reliez *Texture Coordinate* (*Object*), puis un *Mapping* (*Scale* 50 sur les trois axes), l'image, un *Bump* (*Strength* 0,2) et l'entrée *Normal* du Principled.
Contrôle : le socle est grainé, la tête reste laquée et lisse. Corrigé : `Structure_Vert_corrige`.

### Consignes · Sans raccord, puis empaqueter
À vous :
- faites le tour du socle, et réglez *Blend* et *Scale* jusqu'à ne plus voir de raccord ;
- empaquetez les images dans le fichier (*File > External Data > Pack Resources*), comme à l'initiation ;
- enregistrez.
Contrôle : aucun raccord visible au tour du socle. Après *Pack Resources*, le fichier ne dépend plus du dossier `textures_cmf`.

```side-by-side
layout: "textRight"
imagePath: "assets/images/file_external_data_pack_blender.jpg"
caption: "Figure 3.31 : File > External Data : Pack Resources range les images dans le fichier .blend."
title: "Pack Resources"
---
*Pack Resources* copie les images utilisées dans le fichier `.blend`. Le fichier s'ouvre alors seul, sur un autre poste ou au chapitre 4.

*Automatically Pack Resources* le fait à chaque enregistrement : c'est une option.
```

> [!WARNING]
> Le grain apparaît aussi sur la tête : la laque n'a pas été rendue indépendante avant la modification. `Ctrl + Z`, puis un clic sur le compteur. Le nœud *Normal Map* ne convient pas ici : il a besoin d'un dépliage UV. Le nœud *Bump* suffit.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/preferences_node_wrangler_blender.jpg"
caption: "Figure 3.32 : Option : Edit > Preferences > Add-ons, l'extension Node Wrangler, livrée avec Blender."
title: "Option : Node Wrangler"
---
L'extension *Node Wrangler* est livrée avec Blender, mais désactivée. Cochez-la dans *Edit > Preferences > Add-ons* (cherchez « node wrangler »).

Sur un nœud de texture sélectionné, `Ctrl + T` ajoute alors *Texture Coordinate* et *Mapping* d'un coup. Vérifiez la sortie reliée : remettez-la sur *Object* si besoin.
```

> [!NOTE]
> **Ailleurs.** La projection *Box* habille un accoudoir en cuir grainé ou un panneau en fibre de carbone (aéronautique), une coque de rétroviseur grainée (automobile), une main courante en inox brossé ou un marchepied en tôle larmée (ferroviaire). Le fichier de démonstration propose ces pièces.

```quiz
question: "Pourquoi relier la sortie Object du nœud Texture Coordinate ?"
options:
  - "Pour que le motif garde la même taille sur toute la pièce, quelle que soit sa forme"
  - "Pour déplier les UV"
  - "Pour accélérer l'affichage"
  - "Pour colorer la texture"
correctIndices:
  - 0
explanation: "La sortie Object suit les coordonnées de la pièce, en mètres : la taille du motif ne dépend plus de la forme. Generated, la sortie par défaut, étire le motif selon la boîte de l'objet."
```

```quiz
question: "Le grain paraît étiré sur une seule pièce. Quelle est la cause la plus probable ?"
options:
  - "Un Blend trop faible"
  - "Une échelle non appliquée"
  - "Une image en sRGB"
  - "Une Roughness trop forte"
correctIndices:
  - 1
explanation: "La projection suit les coordonnées Object : une échelle non appliquée les étire, et la texture avec elles. Ctrl + A > Scale remet le grain d'aplomb."
```

```quiz
question: "Quel nœud transforme une image de grain en relief, sans dépliage UV ?"
options:
  - "Normal Map"
  - "Mapping"
  - "Bump"
  - "Displacement"
correctIndices:
  - 2
explanation: "Le Bump lit une hauteur et perturbe la normale de la surface. Le Normal Map a besoin d'un dépliage UV ; le Mapping étire ou déplace une texture ; le Displacement déplace la géométrie."
```

> [!CAUTION]
> **Défi fil rouge.** Donnez à la lampe ses finitions : aluminium brossé dans l'axe des bras, socle en peinture structurée, grain fin sur l'interrupteur et la grille. Vérifiez qu'aucun raccord ne se voit, puis empaquetez les images. Pour aller plus loin, le fichier `PRC02_ch3_finitions_triplanaires.blend` propose un accoudoir en cuir, une coque de rétroviseur, un marchepied en tôle larmée et un panneau en carbone, avec des consignes par paliers dans son LISEZ-MOI.

## 3. Bibliothèque d'actifs (Asset Browser)

> [!NOTE]
> Cette section part des matières des sections 1 et 2. Elle utilise le sélecteur de type d'éditeur et l'Outliner (Basics 101), la barre latérale `N`, la fenêtre d'ouverture de fichiers, et *File > Append*, cité à l'initiation. Elle apporte l'actif, le catalogue et l'Asset Browser, puis met *File > Append* en pratique.

### Pourquoi une bibliothèque
Une équipe CMF réutilise ses matières d'un projet à l'autre : la gamme de teintes d'un constructeur automobile, la charte des intérieurs d'une compagnie aérienne, les matières homologuées d'un aménagement ferroviaire. Recréer chaque matière à la main fait perdre du temps et crée des écarts.

Blender range ces matières en **actifs** (*assets*). L'**Asset Browser** les montre en vignettes, rangées en **catalogues**. La bibliothèque CMF de la formation en propose vingt-cinq.

![Figure 3.33 : Le nuancier de la bibliothèque CMF, en Material Preview : une rangée par catalogue (métaux, plastiques, peintures, verres, finitions texturées), et la grille Metallic / Roughness au fond.](assets/images/cmf_swatch_library_blender.jpg)

### Faire d'une matière un actif
Un clic droit sur le nom de la matière, dans l'onglet *Material*, ouvre un menu : *Mark as Asset*. La matière devient un actif, et Blender calcule sa vignette.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/material_mark_as_asset_blender.jpg"
caption: "Figure 3.34 : Le clic droit sur le nom de la matière, dans l'onglet Material : Mark as Asset."
title: "Mark as Asset"
---
Faites le clic droit sur le nom de la matière, pas sur la vue 3D : *Mark as Asset* lancé depuis le menu *Object* marquerait la pièce, pas sa matière.

*Clear Asset*, juste en dessous, retire le statut d'actif.
```

### L'Asset Browser
L'Asset Browser est un éditeur, comme le Shader Editor. Changez un éditeur existant avec le sélecteur de type d'éditeur, en haut à gauche de la zone : par exemple la zone du LISEZ-MOI, en bas de l'écran.

Le menu à gauche de l'Asset Browser choisit la bibliothèque. *Current File* montre les actifs du fichier ouvert.

### Le sélecteur de type d'éditeur
Le sélecteur de type d'éditeur est la première icône de l'en-tête d'une zone. *Asset Browser* se trouve dans la colonne *Data*.

Agrandissez la zone en tirant sa bordure : les vignettes ont besoin de place.

![Figure 3.35 : Le sélecteur de type d'éditeur, ouvert sur la zone du bas : Asset Browser se trouve dans la colonne Data.](assets/images/asset_browser_editor_type_blender.jpg)

![Figure 3.36 : L'Asset Browser, bibliothèque Current File : les catalogues à gauche, les vignettes du catalogue Métaux au centre, et la barre latérale de l'actif sélectionné à droite.](assets/images/asset_browser_overview_blender.jpg)

### Ranger en catalogues
Un catalogue range les actifs, comme un dossier. Le bouton `+`, en haut de la liste des catalogues, en crée un ; un double-clic le renomme. Glissez ensuite une vignette sur un catalogue pour l'y ranger.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/asset_catalog_new_blender.jpg"
caption: "Figure 3.37 : La liste des catalogues : le bouton + pour en créer un, et les trois catalogues de la lampe. Unassigned regroupe les actifs sans catalogue."
title: "Les catalogues"
---
Trois catalogues suffisent pour la lampe : *Métaux*, *Plastiques et peintures*, *Verres*.

*Unassigned* montre les actifs qui ne sont rangés nulle part.
```

> [!IMPORTANT]
> **Les catalogues sont enregistrés à côté de votre fichier,** dans un fichier `blender_assets.cats.txt`, pas dans le `.blend` (vérifié dans Blender 5.2). Copiez toujours les deux ensemble. Sans lui, vos actifs restent, mais leur rangement est perdu.

### Décrire un actif
La barre latérale de l'Asset Browser (`N`) montre l'actif sélectionné : son nom, sa description, sa licence, son auteur, ses étiquettes (*Tags*) et sa vignette. Une description d'une phrase aide toute l'équipe : l'usage de la matière et ses secteurs.

```side-by-side
layout: "textRight"
imagePath: "assets/images/asset_metadata_sidebar_blender.jpg"
caption: "Figure 3.38 : La barre latérale de l'Asset Browser pour Alu_Brosse : Description, License, Author, et la vignette (Preview)."
title: "La barre latérale"
---
Exemple de description : « Aluminium brossé. Bras de lampe ; convient aussi à une main courante ou à une jante. »

Une vignette noire ? Relancez son calcul avec le bouton à droite de l'aperçu (*Generate Preview*).
```

### Appliquer un actif par glisser-déposer
Une vignette se glisse sur une pièce de la vue 3D : la pièce prend la matière, en un geste. C'est le même résultat que la liste des matières. Relâchez le bouton avec le pointeur sur la pièce : Blender affiche alors la pièce visée.

![Figure 3.39 : La vignette Chrome, glissée de la bibliothèque Current File sur la douille. Blender affiche la pièce visée : « Drop Chrome on Douille ».](assets/images/asset_drag_drop_material_blender.jpg)

### Recette · Ranger les matières de la lampe
- **1.** Clic droit sur le nom de `Alu_Brosse`, *Mark as Asset*. Faites de même pour `Chrome` et `Peinture_Vert`.
- **2.** Changez la zone du LISEZ-MOI en *Asset Browser*, avec le sélecteur de type d'éditeur. Agrandissez-la. Bibliothèque : *Current File*.
- **3.** Créez trois catalogues : *Métaux*, *Plastiques et peintures*, *Verres*.
- **4.** Rangez les trois actifs dans leur catalogue.
- **5.** La douille est encore nue : glissez sur elle la vignette de `Chrome`. C'est un essai : elle recevra l'aluminium du nuancier un peu plus loin.
Contrôle : le catalogue *Métaux* montre l'aluminium brossé et le chrome ; la douille est chromée.

### Consignes · Jusqu'à la dernière matière
À vous :
- marquez et rangez seuls les autres matières : `Structure_Vert`, `ABS_Noir`, `PVC_Mat_Noir`, `Verre_Clair` ;
- décrivez un actif, au choix ;
- enregistrez, et vérifiez que `blender_assets.cats.txt` est apparu à côté de votre fichier.
Contrôle : dans *Current File*, chaque matière de la lampe est rangée dans un catalogue. Corrigé du rangement : la bibliothèque CMF elle-même, présentée juste après.

### Récupérer une matière : File > Append
La bibliothèque CMF de la formation est un fichier `.blend` comme un autre. *File > Append* copie une matière de ce fichier dans le vôtre, sans toucher aux préférences de Blender.

Dans la fenêtre d'*Append*, un fichier `.blend` s'ouvre comme un dossier : il contient des dossiers *Collection*, *Material*, *Object*… Entrez dans *Material*, choisissez la matière, puis *Append*. La matière arrive modifiable, avec ses images, et elle garde son statut d'actif : sa vignette apparaît dans *Current File* (vérifié dans Blender 5.2).

```resource
title: "La bibliothèque CMF"
description: "Le dossier PRC02_bibliotheque_CMF : le nuancier PRC02_ch3_nuancier_cmf.blend et son fichier de catalogues. Vingt-cinq matières rangées en cinq catalogues (métaux, plastiques, peintures, verres, finitions texturées), avec leur description, leur licence CC0 et leurs étiquettes. Décompressez le dossier sans séparer ses deux fichiers."
fileName: "PRC02_bibliotheque_CMF.zip (0.8 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_bibliotheque_CMF.zip"
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/file_menu_link_append_blender.jpg"
caption: "Figure 3.40 : Le menu File : Link… et Append…, juste au-dessus de Data Previews."
title: "Link et Append, dans le menu File"
---
*Append* copie la donnée dans votre fichier : elle devient la vôtre, modifiable.

*Link*, juste au-dessus, lie la donnée en lecture seule : on l'utilise pour partager une bibliothèque d'équipe. Le fichier qui part au chapitre 4 n'en contient aucune.
```

### Un fichier .blend s'ouvre comme un dossier
Double-cliquez sur le fichier `PRC02_ch3_nuancier_cmf.blend` : ses dossiers de données apparaissent. Les matières sont dans *Material*.

Le chapitre 4 reprendra ce geste, dans le dossier *Collection*, pour amener la lampe dans son studio.

![Figure 3.41 : La fenêtre File > Append, à l'intérieur du fichier du nuancier : ses dossiers Collection, Material, Object… Le chemin du poste est flouté.](assets/images/file_append_blend_folders_blender.jpg)

### Recette · L'aluminium de la douille
- **1.** *File > Append*. Allez dans le dossier `PRC02_bibliotheque_CMF`, double-cliquez sur `PRC02_ch3_nuancier_cmf.blend`, puis sur *Material*.
- **2.** Choisissez `Alu_Naturel`, puis *Append*.
- **3.** Dans l'Asset Browser, *Current File* : glissez la vignette de `Alu_Naturel` sur la douille. Ou choisissez-la dans la liste des matières.
- **4.** Rangez l'actif dans *Métaux*, puis enregistrez.
Contrôle : la douille est en aluminium naturel, et les réglages de sa matière ne sont pas grisés. Aucune matière liée ne reste dans le fichier.

> [!WARNING]
> Pas de dossier *Material* : vous êtes dans le dossier `PRC02_bibliotheque_CMF`, pas dans le fichier ; double-cliquez sur le `.blend`. La matière s'appelle `Alu_Naturel.001` : l'aluminium des bras n'a pas été renommé `Alu_Brosse` en section 2 ; renommez les deux. Des réglages grisés : la matière a été liée par *File > Link* ; `Ctrl + Z`, puis *File > Append*.

### Option : déclarer une bibliothèque
Pour parcourir la bibliothèque CMF dans l'Asset Browser de tous vos fichiers, déclarez son dossier dans les préférences : *Edit > Preferences > Asset Libraries*, bouton `+`, puis le dossier `PRC02_bibliotheque_CMF`. C'est l'usage d'une équipe. En formation, ce réglage n'est pas nécessaire : *File > Append* suffit.

### Option : la section Asset Libraries
La section *Asset Libraries* des préférences liste les bibliothèques. Le bouton `+` en ajoute une ; *Path* indique son dossier.

*Import Method* vaut *Pack* par défaut dans Blender 5.2 : la matière est liée, et sa source rangée dans votre fichier. Pour une matière à modifier, préférez *Append*.

![Figure 3.42 : Option : Edit > Preferences > Asset Libraries, la bibliothèque CMF ajoutée, avec son chemin (Path, flouté) et sa méthode d'import (Import Method : Pack).](assets/images/preferences_asset_libraries_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/asset_library_selector_blender.jpg"
caption: "Figure 3.43 : Option : le menu des bibliothèques de l'Asset Browser : All Libraries, Current File, Essentials, User Library et la bibliothèque CMF déclarée."
title: "Option : choisir la bibliothèque"
---
Une fois déclarée, la bibliothèque apparaît dans le menu à gauche de l'Asset Browser. Ses catalogues et ses vignettes s'affichent.

*Essentials*, livrée avec Blender, ne contient aucune matière : la bibliothèque CMF est faite pour cela.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/asset_import_method_menu_blender.jpg"
caption: "Figure 3.44 : Option : Import Settings, dans l'en-tête de l'Asset Browser : Import Method propose Follow Asset or Preferences, Link, Append et Pack."
title: "Option : la méthode d'import"
---
*Import Settings* choisit ce que fait une vignette glissée depuis une bibliothèque déclarée. *Append* copie la matière ; *Link* la lie en lecture seule ; *Pack*, nouveau dans Blender 5, la lie puis range sa source dans votre fichier.

*Follow Asset or Preferences* applique le réglage de la bibliothèque.
```

> [!NOTE]
> **Ailleurs.** Une bibliothèque d'actifs sert à toute une équipe : la gamme de teintes d'un constructeur automobile, la charte des intérieurs d'une compagnie aérienne, les matières homologuées (feu, fumée) d'un aménagement ferroviaire. Chacun puise dans la même gamme, et les visuels restent cohérents d'un projet à l'autre.

```quiz
question: "Vous voulez récupérer une matière d'un autre fichier, sans toucher aux préférences de Blender. Quel chemin suivez-vous ?"
options:
  - "File > Open, puis le fichier"
  - "File > Append, puis le dossier Material du fichier"
  - "File > Import"
  - "Edit > Preferences > Asset Libraries"
correctIndices:
  - 1
explanation: "File > Append ouvre le fichier .blend comme un dossier : le dossier Material contient ses matières. La matière arrive copiée, modifiable. Déclarer une bibliothèque dans les préférences est une option."
```

```quiz
question: "Que fait Link, par rapport à Append ?"
options:
  - "Il copie la matière et ses images"
  - "Il lie la matière en lecture seule, sans la copier"
  - "Il marque la matière comme actif"
  - "Il empaquette le fichier source"
correctIndices:
  - 1
explanation: "Link lie la matière en lecture seule : on l'utilise pour partager une bibliothèque d'équipe, qui se modifie dans son fichier source. Append copie la matière : elle devient la vôtre."
```

```quiz
question: "Où retrouver les actifs du fichier ouvert dans l'Asset Browser ?"
options:
  - "Dans la bibliothèque Essentials"
  - "Dans la bibliothèque User Library"
  - "Dans la bibliothèque Current File"
  - "Dans le menu File > Recover"
correctIndices:
  - 2
explanation: "Current File montre les actifs du fichier ouvert, rangés dans ses catalogues. Essentials est livrée avec Blender ; User Library est un dossier de votre poste."
```

> [!CAUTION]
> **Défi fil rouge.** Faites des matières de votre lampe des actifs, rangés en catalogues et décrits. Habillez ensuite la douille avec une matière du nuancier, récupérée par *File > Append*.

### Atelier · Le second coloris
**La situation.** La revue de design demande une seconde proposition de couleurs, le coloris B. Vous déclinez la lampe dans un second coloris, sans toucher au premier.

L'atelier n'apporte aucune notion nouvelle : il réinvestit *Duplicate Collection* (chapitre 1), le compteur d'utilisateurs, les réglages du Principled (section 1), les nœuds de la section 2 et la bibliothèque (section 3). Comptez environ 20 minutes.

Si vous manquez d'idée, voici le coloris B du corrigé : une version claire pour un bureau d'études, avec structure et laque blanches, bras anodisés noirs, articulations et douille en laiton, et verre dépoli.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/outliner_collection_menu_blender.jpg"
caption: "Figure 3.45 : Le clic droit sur la collection Lampe, dans l'Outliner : Duplicate Collection."
title: "Duplicate Collection"
---
Un clic droit sur la collection *Lampe*, dans l'Outliner, puis *Duplicate Collection* : la collection est copiée avec ses pièces.

Attention : la copie partage les matières de l'original. Rendez chaque matière indépendante, par un clic sur son compteur, avant de la changer.
```

### Consignes · Le coloris B, par paliers
- **Lancement.** Dupliquez la collection *Lampe*, renommez la copie `Lampe_coloris_B`, puis décalez-la de 750 mm sur X : sélectionnez ses pièces (clic droit sur la collection, *Select Objects*), puis `G X = 750mm`. Avec moins, le câble de la copie traverserait le socle de l'original.
- **Socle.** Le coloris B change au moins quatre matières, dont une peinture et un métal. Rendez chaque matière indépendante, puis renommez-la, par exemple `Laque_Blanche`. Le coloris A ne bouge pas.
- **★** Toutes les pièces du coloris B suivent une gamme cohérente. Ses nouvelles matières sont des actifs, rangés dans les catalogues. Une matière au moins vient du nuancier, par *File > Append* : par exemple `Laiton`.
- **★★** Un coloris C « premium » : laiton, carbone en projection triplanaire, verre fumé.
- **Revue.** Changez une teinte du coloris B : le coloris A ne doit pas bouger. Puis enregistrez sous `lampe_habillage_v002.blend`, avec le bouton `+` de *File > Save As*.
La collection *Lampe* garde le coloris A et son nom : le chapitre 4 l'importe sous ce nom. Corrigé : la collection *Corrigé coloris B*.

> [!WARNING]
> Les deux lampes changent ensemble : la matière est encore partagée. Un clic sur son compteur la rend indépendante. *Duplicate Collection* copie les objets et les maillages, mais pas les matières (vérifié dans Blender 5.2). Une copie de matière garde ses nœuds : l'aluminium brossé, rendu indépendant puis teinté en noir, reste brossé. Un verre créé avec *New*, au lieu d'une copie de `Verre_Clair`, ne montre que l'image d'environnement : recochez *Raytraced Transmission* et *Thin Wall*.

![Figure 3.46 : L'atelier terminé : le coloris A dans la collection Lampe, le coloris B dans Lampe_coloris_B, décalé de 750 mm.](assets/images/lamp_two_colorways_blender.jpg)

```resource
title: "La lampe habillée : fin du chapitre 3"
description: "L'état attendu de lampe_habillage_v002.blend : le coloris A dans la collection Lampe, le coloris B dans Lampe_coloris_B, les matières rangées en actifs dans leurs catalogues. C'est aussi un point de départ possible du chapitre 4. Décompressez le dossier sans séparer le .blend de son fichier de catalogues."
fileName: "PRC02_ch3_lampe_habillage.zip (0.4 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch3_lampe_habillage.zip"
```

### Pour ceux qui avancent vite
Les défis ★ :
- le verre dépoli et le verre fumé ;
- l'intérieur blanc de la tête : un second emplacement de matière et *Material Offset* du *Solidify* (figures 3.16 et 3.17) ;
- *Emission* : un voyant lumineux sur l'interrupteur (figure 3.15) ;
- *File > Link* d'une matière du nuancier : elle arrive grisée, en lecture seule (figure 3.47), puis `Ctrl + Z` ;
- la bibliothèque CMF déclarée dans vos préférences : glissez une vignette de la gamme sur une pièce, puis essayez le menu *Import Method*.

Les défis ★★ :
- **Automobile :** la peinture métallisée de la bibliothèque, décortiquée dans le Shader Editor, puis reproduite ;
- **Aéronautique :** l'accoudoir en cuir grainé et le panneau carbone, sur le fichier des finitions triplanaires ;
- **Ferroviaire :** le marchepied en tôle larmée, puis la rangée de sièges de l'initiation (`PRC02_init_rangee_sieges.blend`) habillée avec la bibliothèque ;
- **Votre bibliothèque :** déclarez votre dossier de travail comme bibliothèque, puis habillez un objet dans un nouveau fichier.

Pour aller plus loin, la section 4 propose le « Défi facultatif : matières procédurales ».

```side-by-side
layout: "textRight"
imagePath: "assets/images/linked_material_readonly_blender.jpg"
caption: "Figure 3.47 : Défi : une matière liée par File > Link. Son nom porte l'icône de lien, et ses réglages sont grisés : elle se modifie dans son fichier source."
title: "Défi : une matière liée"
---
Une matière liée appartient à son fichier source : elle s'affiche, mais ne se modifie pas ici. Si la bibliothèque change, la matière suit à la prochaine ouverture.

C'est l'intérêt de *Link* pour une équipe, et sa limite pour un fichier envoyé seul : préférez alors *Append*.
```

## 4. Défi facultatif · Matières procédurales

> [!NOTE]
> **Un complément facultatif, hors programme de base.** Cette section ajoute des connaissances utiles que la formation initiale ne prévoit pas. Elle s'adresse à ceux qui sont à l'aise avec les sections 1 à 3, ou qui connaissent déjà ces sujets.
>
> Faites-la à la suite des parties de base, s'il vous reste du temps, ou à leur place, pour un complément et des défis plus poussés. Elle part des acquis de la section 2 : le Shader Editor, *Texture Coordinate*, *Bump* et *Mapping*. En cas de doute, les trois quiz de la section 2 servent de test d'entrée.
>
> Vous faites ce défi à la place de l'atelier ? Pour le chapitre 4, repartez de son fichier de secours, de la lampe habillée (`PRC02_ch3_lampe_habillage.zip`) ou de votre propre lampe, gardée dans la collection *Lampe* et enregistrée sous `lampe_habillage_v002.blend`. C'est une option, pas une obligation.

### Ce que vous allez construire
Le chapitre a couvert les cas courants : des matières simples, un grain, un brossé, des images projetées. Ici, vous construisez vous-même des matières **procédurales** plus riches : Blender les calcule, sans image et sans dépliage UV.

Le défi compte sept étapes, en deux paliers :
- palier 1 : lire les textures de bruit, remapper les valeurs, masquer et superposer, mettre en relief ;
- palier 2 : user une pièce, construire un motif régulier, regrouper une chaîne de nœuds.

Comptez environ 3 heures. Chaque étape suit le même ordre : un exemple terminé à observer, une recette guidée, puis un petit défi. Un quiz clôt chaque étape.

![Figure 3.48 : Le banc d'échantillons du défi, terminé : une rangée par étape, des bruits aux groupes de nœuds, et la lampe usée du défi final.](assets/images/procedural_challenge_overview_blender.jpg)

```resource
title: "Le banc d'échantillons du défi"
description: "Une rangée de pièces par étape, des trois secteurs : un exemple terminé, les pièces à compléter, et une copie de la lampe pour le défi final. Corrigés : collection « Corrigé défi procédural », œil fermé, une sous-collection par étape."
fileName: "PRC02_ch3_defi_procedural.blend (0.5 Mo)"
downloadUrl: "https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/PRC02_ch3_defi_procedural.blend"
```

> [!IMPORTANT]
> **Tout fonctionne sous EEVEE.** Quelques nœuds ne marchent que sous Cycles : *Geometry > Pointiness*, le nœud *Bevel*, *Random Per Island* et *Anisotropic* du Principled. Ce défi les remplace par des alternatives vérifiées sous EEVEE et en *Material Preview* : la normale de la pièce pour repérer les arêtes, le nœud *Ambient Occlusion* pour les creux, un relief étiré pour le brossé.

### Les menus utiles du Shader Editor
Le menu `Maj + A` range les nœuds par familles (figure 3.20). Ce défi en utilise six :
- *Input* : *Texture Coordinate*, *Ambient Occlusion* ;
- *Texture* : *Noise*, *Voronoi*, *Wave*, *Gabor*, *Gradient*, *Checker* ;
- *Color* : *Color Ramp*, *Mix Color* ;
- *Utilities > Math* : *Map Range*, *Math*, *Mix* ;
- *Utilities > Vector* : *Mapping*, *Separate XYZ*, *Vector Math* ;
- *Displacement* : *Bump*.

La recherche va souvent plus vite : `Maj + A`, puis tapez le nom du nœud, ou celui d'une opération de *Math*, comme « Ping-Pong ».

![Figure 3.49 : Quatre sous-menus de Maj + A dans Blender 5.2 : Color, Utilities > Math, Utilities > Vector et Displacement.](assets/images/shader_add_submenus_blender.jpg)

### Les repères d'échelle
Toutes les recettes partent de *Texture Coordinate*, sortie *Object* : la texture se mesure en mètres, quelle que soit la pièce.
- *Noise* et *Voronoi* : *Scale* donne à peu près le nombre de motifs par mètre. Avec *Scale* 100, un motif tous les 10 mm environ.
- *Wave* : une bande tous les 0,314 / *Scale* mètre. Avec *Scale* 40, une bande tous les 7,9 mm.
- *Bump* : comme dans la section 2, le relief se règle avec *Strength*, entre 0 et 1, et *Distance* garde sa valeur.

Toutes les valeurs sont des points de départ, vérifiés sous EEVEE : retouchez-les à l'œil.

### Avant de commencer
Ouvrez `PRC02_ch3_defi_procedural.blend`, puis enregistrez-le sous `defi_procedural_v001.blend`. Le fichier s'ouvre dans l'espace *Shading*, sur les rangées des étapes 1 et 2.

Dans l'Outliner, gardez visible seulement la collection de l'étape en cours. *Material Preview* calcule chaque matière visible : moins il y en a, plus l'affichage reste fluide.

### Voir le résultat d'un nœud : l'aperçu
`Ctrl + Maj + clic` sur un nœud relie sa sortie directement à l'entrée *Surface* du *Material Output*. La pièce affiche alors la valeur brute du nœud : en niveaux de gris, du noir pour 0 au blanc pour 1, ou en couleurs pour une sortie *Color*.

Un nouveau `Ctrl + Maj + clic` sur le même nœud passe à sa sortie suivante. `Ctrl + Maj + clic` sur le *Principled BSDF* rétablit la matière. Ce geste est natif dans Blender 5.2 : Node Wrangler n'est pas nécessaire.

![Figure 3.50 : L'aperçu par Ctrl + Maj + clic : la sortie Factor du Noise reliée directement à Surface. Le Principled BSDF reste en place, sans lien. À droite, la plaquette en niveaux de gris.](assets/images/node_preview_ctrl_shift_click_blender.jpg)

> [!WARNING]
> Le blanc de l'aperçu paraît gris clair : c'est la transformation de vue *AgX*, réglée par défaut. Lisez les contrastes, pas les valeurs. La pièce reste grise et sans reflet ? L'aperçu n'a pas été annulé : `Ctrl + Maj + clic` sur le *Principled BSDF*.

### Palier 1 · Lire et combiner
Le palier 1 compte quatre étapes, pour environ 80 minutes : lire les textures de bruit, remapper les valeurs, masquer et superposer, puis mettre en relief. Les quiz 1 à 5 en vérifient les acquis.

### Étape 1 · Lire les textures de bruit
**Nouveau :** les réglages d'une texture procédurale, puis trois textures de plus. **Déjà vu :** *Noise Texture*, *Scale*, *Texture Coordinate* (*Object*), l'aperçu. Comptez 20 minutes.

**Exemple :** les quatre plaquettes `E1_Exemple_Noise`, `_Voronoi`, `_Wave` et `_Gabor`, chacune en aperçu de sa texture. Observez-les, puis entrez dans leurs nœuds.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/noise_texture_node_blender.jpg"
caption: "Figure 3.51 : Le nœud Noise Texture et le menu de son type : fBM par défaut, Multifractal, Ridged Multifractal, Hybrid Multifractal, Hetero Terrain."
title: "Les réglages du Noise"
---
- *Scale* : la taille du motif.
- *Detail* : le nombre de couches de bruit superposées.
- *Roughness* : le poids des couches fines.
- *Lacunarity* : l'écart de taille d'une couche à la suivante.
- *Distortion* : un motif tordu.
- Le menu du type : *Ridged Multifractal* donne des veines.
```

### Recette · Le Noise, réglage par réglage
Sur la plaquette `E1_Pratique`, une ligne à la fois :
- **1.** `Maj + A > Input > Texture Coordinate`, puis `Maj + A > Texture > Noise Texture`. Reliez *Object* à *Vector*. Aperçu sur la sortie *Factor* : la plaquette paraît uniforme.
- **2.** *Scale* 100 : des nuages doux, environ huit sur la largeur.
- **3.** *Detail* 8, *Roughness* 0,7 : un grain plus fin, plus riche.
- **4.** *Detail* 2, *Distortion* 2 : des tourbillons.
- **5.** Le type *Ridged Multifractal*, *Scale* 60, *Detail* 4, *Distortion* 0 : des veines nettes, pour un plastique marbré ou une pierre.
La sortie *Color* donne des nuages de couleurs pastel : elle sert rarement.

![Figure 3.52 : Le Noise sur une plaquette de 80 mm : Scale 5 par défaut, Scale 100, Detail 8, Distortion 2, puis Ridged Multifractal.](assets/images/noise_settings_comparison_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/voronoi_texture_node_blender.jpg"
caption: "Figure 3.53 : Le nœud Voronoi Texture et le menu de ses réglages : F1, F2, Smooth F1, Distance to Edge, N-Sphere Radius."
title: "Le Voronoi : des cellules"
---
Le *Voronoi* découpe l'espace en cellules.
- *F1*, sortie *Distance* : une tache sombre au centre de chaque cellule.
- *Distance to Edge* : de fins sillons sombres entre les cellules. C'est la base du cuir et des craquelures.
- Sortie *Color* : une couleur au hasard par cellule.
- *Randomness* : le désordre des cellules ; à 0, une grille parfaite.
```

### Recette · Le Voronoi
Sur `E1_Pratique`, remplacez le *Noise* par `Maj + A > Texture > Voronoi Texture`, relié de la même façon :
- **1.** *Scale* 100, aperçu sur *Distance* : des taches sombres au centre des cellules.
- **2.** Le réglage *Distance to Edge* : des sillons entre les cellules.
- **3.** Aperçu sur la sortie *Color* : une couleur par cellule. Elle sert à faire varier légèrement chaque cellule.

![Figure 3.54 : Le Voronoi à Scale 100 : F1, Distance to Edge, puis la sortie Color.](assets/images/voronoi_comparison_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/wave_texture_node_blender.jpg"
caption: "Figure 3.55 : Le nœud Wave Texture : Bands ou Rings, la direction, le profil Sine, puis Scale, Distortion et Detail."
title: "Le Wave : des bandes"
---
Le *Wave* dessine des bandes régulières.
- *Bands* : des bandes droites ; *Rings* : des anneaux.
- La direction : *X*, *Y*, *Z* ou *Diagonal*.
- Le profil : *Sine*, *Saw* ou *Triangle*.
- *Distortion* et *Detail* ondulent les bandes.
```

### Recette · Le Wave
Sur `E1_Pratique`, `Maj + A > Texture > Wave Texture`, *Scale* 40 :
- **1.** *Bands*, direction *X*, profil *Sine* : des bandes droites, une tous les 7,9 mm.
- **2.** *Distortion* 4, *Detail* 4 : des bandes ondulées.
- **3.** *Rings*, direction *Z* : des cercles concentriques, comme l'usinage d'un bouton ou d'un enjoliveur.

![Figure 3.56 : Le Wave à Scale 40 : des bandes, des bandes ondulées, puis des anneaux.](assets/images/wave_comparison_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/gabor_texture_node_blender.jpg"
caption: "Figure 3.57 : Le nœud Gabor Texture : le type 2D ou 3D, Scale, Frequency, Anisotropy et Orientation."
title: "Le Gabor : des stries"
---
Le *Gabor* dessine des stries orientées, comme un brossé.
- *Frequency* : des stries plus ou moins serrées.
- *Anisotropy* : à 1, des stries nettes ; à 0, un motif sans direction.
- *Orientation* : l'angle des stries, en radians ; 0,785 vaut 45°, 1,571 vaut 90°.
- Le type *2D* ne lit que X et Y : gardez-le pour les faces planes et horizontales.
```

### Recette · Le Gabor
Sur `E1_Pratique`, `Maj + A > Texture > Gabor Texture`, *Scale* 100, type *2D*. Aperçu sur *Value* :
- **1.** Les réglages par défaut : des stries fines, orientées à 45°.
- **2.** *Frequency* 6 : des stries plus serrées.
- **3.** *Frequency* 2, *Anisotropy* 0 : le motif devient vermiculé.
- **4.** *Frequency* 6, *Anisotropy* 1, *Orientation* 1,571 (90°) : des stries serrées dans l'axe X.
Contrôle : la plaquette montre des stries fines dans l'axe X ; avec *Orientation* 0, elles suivent l'axe Y. Corrigé : `E1_Pratique_corrige`.

![Figure 3.58 : Le Gabor à Scale 100 : par défaut, Frequency 6, puis Anisotropy 0.](assets/images/gabor_comparison_blender.jpg)

> [!WARNING]
> Une plaquette presque uniforme : *Scale* est resté à 5, sa valeur par défaut ; un seul motif couvre 20 cm. Un motif étiré ou qui glisse avec la pièce : *Texture Coordinate* n'est pas relié. Un dégradé de couleurs : l'aperçu montre la sortie *Color* ; refaites `Ctrl + Maj + clic` pour passer à *Factor* ou *Distance*. Un *Gabor* étiré sur les flancs : le type *2D* ne lit que X et Y.

> [!CAUTION]
> **Petit défi.** Reproduisez ces trois plaquettes cibles, sur `E1_Defi_A`, `_B` et `_C`, d'après la figure 3.59 : A, des cellules séparées par des sillons, comme le cuir d'un accoudoir d'avion ; B, les cercles d'usinage d'un bouton de commande automobile ; C, le brossé fin et serré d'une main courante de train, dans l'axe X. Corrigés : sous-collection « Corrigé étape 1 ».

![Figure 3.59 : Le petit défi de l'étape 1 : les plaquettes cibles A, B et C, de gauche à droite.](assets/images/step1_target_tiles_blender.jpg)

```quiz
question: "Une Noise Texture, reliée en coordonnées Object, couvre une plaquette de 80 mm d'une teinte presque uniforme. Que faites-vous ?"
options:
  - "Augmenter Scale, vers 100"
  - "Augmenter Detail"
  - "Augmenter Distortion"
  - "Passer le type en Ridged Multifractal"
correctIndices:
  - 0
explanation: "Avec les coordonnées Object, Scale compte à peu près les motifs par mètre. À 5, sa valeur par défaut, un seul motif couvre 20 cm."
```

```quiz
question: "Quelle texture et quel réglage donnent des cellules séparées par de fins sillons, comme un grain de cuir ?"
options:
  - "Voronoi, réglage F1"
  - "Voronoi, réglage Distance to Edge"
  - "Wave, type Rings"
  - "Noise, type Ridged Multifractal"
correctIndices:
  - 1
explanation: "Distance to Edge mesure la distance au bord de chaque cellule : les bords deviennent des sillons sombres. F1 marque au contraire le centre des cellules."
```

### Étape 2 · Remapper les valeurs
**Nouveau :** transformer une valeur en une autre, avec trois nœuds, l'un après l'autre : *Color Ramp*, *Map Range*, puis *Math*. **Déjà vu :** *Noise*, l'aperçu. Comptez 20 minutes.

**Exemple :** `E2_Exemple_Coque`, une coque de siège ferroviaire en plastique recyclé moucheté.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/color_ramp_node_blender.jpg"
caption: "Figure 3.60 : Le nœud Color Ramp et le menu de son interpolation : Ease, Cardinal, Linear, B-Spline, Constant."
title: "Le Color Ramp"
---
Le *Color Ramp* (`Maj + A > Color`) change une valeur en couleur, d'après ses curseurs.
- Rapprochez deux curseurs : le contraste monte.
- Les boutons `+` et `−` ajoutent et retirent un curseur.
- L'interpolation *Constant* donne des aplats francs, sans dégradé.
- La flèche, à côté des boutons, propose *Flip Color Ramp* pour inverser les curseurs.
```

### Recette · Le moucheté
Sur la plaquette `E2_Pratique_Mouchete` :
- **1.** *Texture Coordinate* (*Object*), puis *Noise* (*Scale* 100). Sortie *Factor* vers `Maj + A > Color > Color Ramp`. Aperçu sur *Color*.
- **2.** Curseur noir à 0,45, curseur blanc à 0,55 : des taches nettes.
- **3.** Interpolation *Constant*, noir à 0, blanc à 0,5 : deux tons francs.
- **4.** *Noise* : *Scale* 1500, *Detail* 0. *Color Ramp* : curseur 0 en #2B2D2F (anthracite), curseur 0,74 en #D8D6D0 (blanc cassé).
- **5.** Reliez *Color* à *Base Color*, puis rétablissez le Principled (`Ctrl + Maj + clic`). *Roughness* 0,5.
Contrôle : de fines mouchetures claires, environ une pour vingt, sur un fond anthracite. Avec le curseur clair à 0,70, elles deviennent trop denses ; à 0,62, la pièce paraît granitée.

![Figure 3.61 : Le bruit brut, puis contrasté par deux curseurs rapprochés, puis en interpolation Constant.](assets/images/color_ramp_comparison_blender.jpg)

![Figure 3.62 : La chaîne du moucheté : Texture Coordinate, Noise (Scale 1500, Detail 0), Color Ramp en Constant, Base Color. À droite, la coque de siège.](assets/images/speckled_plastic_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/map_range_node_blender.jpg"
caption: "Figure 3.63 : Le nœud Map Range : From Min et From Max, To Min et To Max, la case Clamp et le menu d'interpolation."
title: "Le Map Range"
---
Le *Map Range* (`Maj + A > Utilities > Math`) fait passer une plage de valeurs à une autre.
- *From Min* et *From Max* : les valeurs qui entrent.
- *To Min* et *To Max* : celles qui sortent, par exemple de vraies valeurs de *Roughness*.
- *Clamp* empêche de sortir de cette plage.
```

### Recette · La brillance irrégulière
Sur `E2_Pratique_Planche`, une plaquette noire de planche de bord automobile (#151515) :
- **1.** *Texture Coordinate* (*Object*), puis *Noise*, *Scale* 40, *Detail* 3.
- **2.** `Maj + A > Utilities > Math > Map Range`. Reliez *Factor* à *Value*.
- **3.** *From Min* 0,35, *From Max* 0,65, *To Min* 0,08, *To Max* 0,35. *Clamp* reste coché.
- **4.** Reliez *Result* à *Roughness*.
Contrôle : des reflets nets par endroits, voilés ailleurs, comme sur un plastique injecté. Faites tourner l'image d'environnement pour les voir (menu *Viewport Shading*, section 1).

![Figure 3.64 : La chaîne de la brillance irrégulière : Noise, Map Range (0,35 à 0,65 vers 0,08 à 0,35), Roughness. À droite, la planche de bord.](assets/images/uneven_gloss_dashboard_blender.jpg)

### Recette · Un seuil en chiffres : Math
Sur `E2_Pratique_Mouchete`, à côté du *Color Ramp*, sans toucher au Principled :
- **1.** `Maj + A > Utilities > Math > Math`. Choisissez l'opération *Greater Than*.
- **2.** Reliez la sortie *Factor* du *Noise* à sa première entrée. *Threshold* 0,74.
- **3.** Aperçu sur *Value* : les mêmes mouchetures, en blanc sur noir.
*Greater Than* rend 1 au-dessus du seuil, 0 en dessous. Le *Color Ramp* se règle à l'œil ; *Map Range* et *Math* se règlent en chiffres, et leurs chiffres pourront devenir les paramètres d'un groupe (étape 7). Corrigés : `E2_Pratique_Mouchete_corrige` et `E2_Pratique_Planche_corrige`.

![Figure 3.65 : Le nœud Math et le menu de ses opérations : Add, Multiply, Power, Absolute, Minimum, Maximum, Less Than, Greater Than, Floor… La liste continue plus bas, avec Floored Modulo et Ping-Pong.](assets/images/math_node_operations_blender.jpg)

> [!WARNING]
> Le masque est inversé : les curseurs du *Color Ramp* sont dans le mauvais ordre ; utilisez *Flip Color Ramp*. *Map Range* ne change rien : les valeurs *From* et *To* ont été confondues. *Math* rend une pièce blanche : l'opération est restée sur *Add*, sa valeur par défaut.

> [!CAUTION]
> **Petit défi.** Des mouchetures en deux couleurs, pour une coque de siège ferroviaire, sur `E2_Defi`. Ajoutez un troisième curseur avec le bouton `+` : à 0,82, en #9B6B43 (terre cuite). Entre 0,74 et 0,82, les mouchetures restent claires ; au-dessus, elles sont terre cuite, et plus rares. Corrigé : `E2_Defi_corrige`.

```quiz
question: "Vous voulez que la Roughness varie entre 0,08 et 0,35 selon un bruit. Quel nœud règle ces deux valeurs en chiffres ?"
options:
  - "Color Ramp"
  - "Map Range"
  - "Mix Color"
  - "Bump"
correctIndices:
  - 1
explanation: "Map Range fait passer les valeurs de From Min et From Max à To Min et To Max. Ici, To Min 0,08 et To Max 0,35 sont de vraies valeurs de Roughness."
```

### Étape 3 · Masques et couches
**Nouveau :** un masque qui choisit entre deux couches, puis la superposition de deux masques. **Déjà vu :** *Color Ramp*, *Map Range*, *Math*. Comptez 20 minutes.

**Exemple :** `E3_Exemple_Main_courante`, une main courante en laiton patiné, celle d'une voiture-bar ou d'un train historique. Le même masque pilote trois entrées du Principled.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/mix_color_and_float_nodes_blender.jpg"
caption: "Figure 3.66 : Le nœud Mix Color (Factor, A, B et le menu de mélange), puis le nœud Mix en Float."
title: "Les nœuds Mix"
---
Un *Mix* choisit entre *A* et *B* selon son *Factor* : 0 donne *A*, 1 donne *B*. Le masque se branche sur *Factor*.
- *Mix Color* (`Maj + A > Color`) mélange deux couleurs.
- *Mix* (`Maj + A > Utilities > Math`) mélange deux nombres, en type *Float*.
Le type se change en haut du nœud.
```

### Recette · Un masque, trois Mix
Sur `E3_Pratique_Main_courante`, un tube de Ø 32 × 300 mm en laiton neuf, couché sur X. Sa rotation n'est pas appliquée : son axe local Z suit le tube.
- **1.** *Texture Coordinate* (*Object*), puis *Noise* : *Scale* 40, *Detail* 6, *Roughness* 0,6.
- **2.** *Color Ramp* : noir à 0,50, blanc à 0,60. Aperçu : les taches blanches sont la patine. C'est le masque.
- **3.** `Maj + A > Color > Mix Color` : *A* #E0C27A (laiton), *B* #3A3B2C (patine). Masque vers *Factor*, *Result* vers *Base Color*.
- **4.** `Maj + A > Utilities > Math > Mix`, en *Float* : *A* 1, *B* 0. Masque vers *Factor*, *Result* vers *Metallic*.
- **5.** Un second *Mix* en *Float* : *A* 0,25, *B* 0,7. Masque vers *Factor*, *Result* vers *Roughness*.
Contrôle : un laiton poli et brillant, avec des taches sombres, mates et non métalliques.

```side-by-side
layout: "textRight"
imagePath: "assets/images/separate_xyz_node_blender.jpg"
caption: "Figure 3.67 : Le nœud Separate XYZ : une entrée Vector, trois sorties X, Y et Z."
title: "Separate XYZ"
---
*Separate XYZ* (`Maj + A > Utilities > Vector`) sépare un vecteur en trois nombres. Sur les coordonnées *Object*, la sortie *Z* donne la position le long de l'axe local Z de la pièce : ici, la longueur du tube.
```

### Recette · Superposer deux masques
La patine ne reste qu'aux extrémités, là où les mains ne passent pas :
- **6.** *Texture Coordinate* (*Object*), puis `Maj + A > Utilities > Vector > Separate XYZ`.
- **7.** *Math*, opération *Absolute*, sur la sortie *Z*.
- **8.** *Map Range* : *From Min* 0,08, *From Max* 0,14. Aperçu : noir au centre, blanc aux deux bouts.
- **9.** *Math*, opération *Multiply* : le masque de patine (étape 2) fois le masque des extrémités (étape 8). Reliez son résultat aux trois *Factor* des *Mix*.
Contrôle : de la patine aux deux extrémités seulement ; au centre, le laiton reste poli. Corrigé : `E3_Pratique_Main_courante_corrige`.

![Figure 3.68 : La chaîne du laiton patiné : le masque de patine (Noise, Color Ramp) multiplié par le masque des extrémités (Separate XYZ, Absolute, Map Range), puis trois Mix vers Base Color, Metallic et Roughness.](assets/images/one_mask_three_mixes_blender.jpg)

![Figure 3.69 : La main courante patinée partout, puis seulement aux extrémités.](assets/images/patina_handrail_comparison_blender.jpg)

> [!NOTE]
> Multiplier deux masques garde ce qu'ils ont en commun ; *Maximum* les additionne ; *Subtract* retire l'un de l'autre. On peut aussi mélanger deux Principled avec *Mix Shader*, mais un seul Principled, dont on mélange les entrées, reste plus léger et plus simple à régler.

> [!WARNING]
> La patine ne se voit pas : le masque n'est relié qu'à *Base Color*, et le laiton garde ses reflets métalliques. Reliez aussi *Metallic* et *Roughness*. La patine est partout et le laiton nulle part : *A* et *B* sont inversés. La patine se trouve au centre : échangez *From Min* et *From Max* du masque des extrémités.

> [!CAUTION]
> **Petit défi.** Une main courante de quai en inox (#C8C8C6, *Metallic* 1, *Roughness* 0,15), entartrée de calcaire blanc (#D9D4C7, *Metallic* 0, *Roughness* 0,8), sur `E3_Defi_Main_courante`. Les nœuds sont les mêmes : seules les valeurs changent. Corrigé : `E3_Defi_Main_courante_corrige`.

```quiz
question: "Sur la main courante patinée, un même masque pilote les entrées du Principled. Lesquelles faut-il relier pour passer du laiton à la patine ?"
options:
  - "Base Color"
  - "Metallic"
  - "Roughness"
  - "IOR"
correctIndices:
  - 0
  - 1
  - 2
explanation: "La patine change la teinte, n'est plus métallique et devient mate : Base Color, Metallic et Roughness suivent le même masque, par trois Mix."
```

### Étape 4 · Le relief procédural
**Nouveau :** enchaîner des reliefs, et donner son propre relief au vernis. **Déjà vu :** *Bump* (section 2), le masque de l'étape 3, *Coat* (section 1). Comptez 15 minutes.

**Exemple :** `E4_Exemple_Coque`, une coque de rétroviseur en laque rouge, avec une légère peau d'orange.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/bump_node_settings_blender.jpg"
caption: "Figure 3.70 : Le nœud Bump : la case Invert, Strength, Distance, Filter Width, puis les entrées Height et Normal."
title: "Le Bump, entrée par entrée"
---
- *Strength* : la force du relief, de 0 à 1 ; c'est elle que l'on règle.
- *Distance* : garde sa valeur.
- *Filter Width* : garde sa valeur par défaut, 0,1.
- *Invert* : les bosses deviennent des creux.
- L'entrée *Normal* reçoit un autre relief : c'est ce qui permet d'en enchaîner deux.
```

### Recette · Deux reliefs chaînés
Sur `E4_Pratique_Boitier`, un boîtier d'avionique en aluminium (#D9DADB, *Metallic* 1, *Roughness* 0,45) :
- **1.** *Texture Coordinate* (*Object*), puis un *Noise* A : *Scale* 2000, *Detail* 0. Sa sortie *Factor* vers *Height* d'un *Bump* A, *Strength* 0,1.
- **2.** Un *Noise* B : *Scale* 150, *Detail* 4. Sa sortie *Factor* vers *Height* d'un *Bump* B, *Strength* 0,2.
- **3.** La sortie *Normal* du *Bump* A vers l'entrée *Normal* du *Bump* B.
- **4.** La sortie *Normal* du *Bump* B vers *Normal* du Principled.
Contrôle : un grain microbillé et des ondulations douces, un aspect martelé. Le dernier *Bump* de la chaîne va au Principled. Corrigé : `E4_Pratique_Boitier_corrige`.

![Figure 3.71 : Deux Bump chaînés : le Bump A (grain fin) entre dans l'entrée Normal du Bump B (ondulations), qui va au Principled. À droite, le boîtier martelé.](assets/images/chained_bump_nodes_blender.jpg)

### Le relief du vernis : Coat Normal
Le vernis a son propre relief : l'entrée *Normal* de la rubrique *Coat*. Une peau d'orange se voit dans le reflet du vernis, pas dans la teinte : son *Bump* va donc dans *Coat Normal*.

![Figure 3.72 : La peau d'orange : Noise (Scale 600, Detail 1), Bump (Strength 0,15), puis l'entrée Normal de la rubrique Coat, dépliée, du Principled BSDF.](assets/images/principled_coat_normal_blender.jpg)

### Recette · La peau d'orange
Sur `E4_Pratique_Coque`, une coque de rétroviseur en laque rouge (#A3161A, *Roughness* 0,4, *Coat Weight* 1, *Coat Roughness* 0,03) :
- **1.** *Texture Coordinate* (*Object*), puis *Noise* : *Scale* 600, *Detail* 1.
- **2.** *Factor* vers *Height* d'un *Bump*, *Strength* 0,15.
- **3.** Dépliez la rubrique *Coat* du Principled. La sortie *Normal* du *Bump* va dans son entrée *Normal*.
Contrôle : les reflets du vernis ondulent légèrement, comme sur une carrosserie. Avec *Strength* 0,3, le défaut devient visible, comme une retouche ; à 0,05, il disparaît presque. Corrigé : `E4_Pratique_Coque_corrige`.

![Figure 3.73 : Le reflet sur la coque laquée : lisse, puis avec la peau d'orange à Strength 0,15, puis à 0,3.](assets/images/orange_peel_comparison_blender.jpg)

### Recette · Un masque en relief
Sur la main courante patinée de l'étape 3 : le masque de patine vers *Height* d'un nouveau *Bump*, *Strength* 0,1, puis vers *Normal* du Principled. La patine forme une couche en léger relief. La case *Invert* du *Bump* la met en creux. Corrigé : `E4_Relief_Main_courante_corrige`.

> [!NOTE]
> Le nœud *Normal Map* lit des images de normales, qui demandent un dépliage UV. Avec des textures procédurales, *Bump* suffit.

> [!WARNING]
> Seul le grain fin se voit : la sortie *Normal* du *Bump* A n'entre pas dans le *Bump* B. Un relief qui scintille : *Strength* est trop forte ; divisez-la par deux. La peau d'orange trouble la teinte, mais le vernis reste lisse : elle est branchée sur *Normal* et non sur *Coat Normal*.

> [!CAUTION]
> **Petit défi.** Une peinture métallisée automobile, sur `E4_Defi_Coque` (#1C3F7A, *Metallic* 1). Gardez la peau d'orange sur *Coat Normal*. Ajoutez des paillettes sous le vernis : *Voronoi* (*Scale* 3000), sortie *Distance*, vers un *Bump* (*Strength* 0,1), puis vers *Normal*. Comparez avec `Peinture_Metallisee_Bleu` du nuancier, récupérée par *File > Append* (section 3). Corrigé : `E4_Defi_Coque_corrige`.

```quiz
question: "La peau d'orange d'une laque se voit dans le reflet du vernis. Où branchez-vous son Bump ?"
options:
  - "Dans l'entrée Normal du Principled"
  - "Dans l'entrée Normal de la rubrique Coat"
  - "Dans Base Color"
  - "Dans Displacement du Material Output"
correctIndices:
  - 1
explanation: "Le vernis a son propre relief, Coat Normal. Branché sur Normal, le relief trouble la teinte, mais le vernis reste lisse."
```

### Palier 2 · Usure, motifs, groupes
Le palier 2 compte trois étapes, pour environ 95 minutes : user une pièce, construire un motif régulier, puis regrouper une chaîne de nœuds. Les quiz 6 à 9 en vérifient les acquis.

### Étape 5 · L'usure
**Nouveau :** des masques tirés de la forme de la pièce : la normale, puis l'occlusion. Les rayures et les traces de doigts réemploient des nœuds connus. **Déjà vu :** *Separate XYZ*, *Math*, *Color Ramp*, *Mix*, *Mapping*, *Coat*. Comptez 30 minutes.

**Exemple :** `E5_Exemple_Coffret`, un coffret électrique de quai, peint en vert, aux arêtes usées et sali au pied.

### Pourquoi la normale repère les arêtes
La normale est la direction vers laquelle regarde la surface. Sur le socle, elle pointe vers le haut sur le dessus, vers le côté sur le flanc, et entre les deux dans le biseau. En gardant seulement l'entre-deux, on obtient un liseré sur les arêtes.

Cette méthode demande une pièce biseautée par le modificateur *Bevel*, d'au moins 3 segments, puis lissée par *Shade Auto Smooth* (chapitre 2). L'usure n'est jamais plus large que le biseau.

### Recette · Les bords usés
Sur `E5_Pratique_Socle`, un cylindre de Ø 180 × 25 mm, biseauté de 3 mm, peint en #2F5D3A :
- **1.** `Maj + A > Input > Texture Coordinate`. Sa sortie **Normal** vers *Separate XYZ*.
- **2.** La sortie *Z* vers *Math*, opération *Absolute*.
- **3.** *Color Ramp* à trois curseurs : noir à 0,10, blanc à 0,50 (bouton `+`), noir à 0,90. Aperçu : un liseré blanc sur les arêtes du dessus et du dessous.
- **4.** *Texture Coordinate* (*Object*) vers un *Noise* : *Scale* 400, *Detail* 8, *Roughness* 0,7.
- **5.** *Math*, opération *Multiply* : le *Color Ramp* fois le *Noise*.
- **6.** *Map Range* : *From Min* 0,30, *From Max* 0,40. C'est le masque d'usure.
- **7.** *Mix Color* : *A* #2F5D3A (peinture), *B* #B8B9BA (métal). Masque vers *Factor*, *Result* vers *Base Color*.
- **8.** Le masque vers *Metallic*. Un *Map Range* (*To Min* 0,45, *To Max* 0,30) vers *Roughness*.
Contrôle : un liseré métallique irrégulier sur les arêtes. Corrigé : `E5_Pratique_Socle_corrige`.

![Figure 3.74 : La chaîne des bords usés : Texture Coordinate (Normal), Separate XYZ, Absolute, Color Ramp à trois curseurs, multiplié par un Noise, puis Map Range, vers Mix Color, Metallic et Roughness.](assets/images/edge_wear_normal_chain_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/vector_math_node_blender.jpg"
caption: "Figure 3.75 : Le nœud Vector Math, ici en Absolute ; son menu propose aussi Dot Product."
title: "Option : Vector Math"
---
*Vector Math* (`Maj + A > Utilities > Vector`) calcule sur des vecteurs entiers. *Absolute* rend les trois composantes positives d'un coup ; *Dot Product* compare deux directions (étape 7).
```

### Consignes · ★ Une pièce prismatique
Sur un boîtier, toutes les arêtes doivent s'user, verticales comprises :
- la normale passe par *Vector Math* (*Absolute*), puis *Separate XYZ* ;
- deux *Math* *Maximum* gardent la plus grande des trois composantes ;
- un *Color Ramp* : blanc à 0,80, noir à 0,97.
N'utilisez pas cette variante sur un cylindre : son flanc s'userait par bandes (figure 3.76, à droite).

![Figure 3.76 : Le masque des arêtes en aperçu sur le socle, le socle usé, puis le boîtier usé par la variante prismatique, et le faux positif de cette variante sur un cylindre.](assets/images/edge_wear_mask_comparison_blender.jpg)

> [!WARNING]
> Rien ne s'use : la pièce n'a pas de biseau, ou elle n'est pas lissée. L'usure est trop fine : élargissez le *Bevel* du modificateur ; le shader ne peut pas aller au-delà. Toute une surface s'use : la pièce est bombée, comme la tête de la lampe ou une coque ; la méthode ne convient qu'aux pièces à faces planes ou cylindriques. L'usure est sur le flanc et pas sur le dessus : la rotation de la pièce a été appliquée ; prenez la sortie *X* ou *Y* de *Separate XYZ*.

```side-by-side
layout: "textRight"
imagePath: "assets/images/ambient_occlusion_node_blender.jpg"
caption: "Figure 3.77 : Le nœud Ambient Occlusion : les sorties Color et AO, les entrées Distance et Normal, les réglages Samples, Inside et Only Local."
title: "Ambient Occlusion"
---
Le nœud *Ambient Occlusion* (`Maj + A > Input`) mesure si la surface est entourée de géométrie : sa sortie *AO* vaut 1 à découvert et baisse dans les creux.

Sous EEVEE, il se calcule à partir de l'image affichée : il change un peu quand on tourne autour, et ne tient compte que de ce qui est à l'écran. *Only Local* n'y est pas pris en charge.
```

### Recette · La saleté dans les creux
Sur `E5_Pratique_Marchepied`, une plaque de 200 × 200 mm à trois nervures, en aluminium (#9A9C9E, *Metallic* 1, *Roughness* 0,35) :
- **1.** `Maj + A > Input > Ambient Occlusion`. *Distance* `20mm` ; *Inside* et *Only Local* restent décochés.
- **2.** Sortie *AO* vers un *Color Ramp* : blanc à 0,85, noir à 0,99. Aperçu : un trait sombre au pied des nervures.
- **3.** *Texture Coordinate* (*Object*), puis *Noise* (*Scale* 200, *Detail* 6), puis un *Color Ramp* : noir à 0,35, blanc à 0,65.
- **4.** *Math* *Multiply* des deux rampes : le masque de saleté.
- **5.** *Mix Color* : *A* #9A9C9E, *B* #3B342C, vers *Base Color*. Un *Mix* en *Float* (*A* 1, *B* 0) vers *Metallic*. Un *Map Range* (*To Min* 0,35, *To Max* 0,9) vers *Roughness*.
Contrôle : une crasse mate et irrégulière au pied des nervures. Corrigé : `E5_Pratique_Marchepied_corrige`.

![Figure 3.78 : Le marchepied : l'occlusion brute, presque blanche ; la même, resserrée par le Color Ramp ; puis la saleté.](assets/images/dirt_crevices_comparison_blender.jpg)

> [!WARNING]
> Rien ne se voit : la rampe est restée entre 0 et 1. Sous EEVEE, les valeurs de l'occlusion restent très proches de 1 : resserrez-la entre 0,85 et 0,99. Toute la pièce s'assombrit, avec des halos : *Distance* est trop grande ; gardez l'ordre de grandeur du creux. La saleté se met sur les arêtes : *Inside* est coché.

### Recette · Les rayures
Sur `E5_Pratique_Main_courante`, un tube inox (#C8C8C6, *Metallic* 1) d'axe local Z. C'est le brossé de la section 2, avec un seuil :
- **1.** *Texture Coordinate* (*Object*), puis *Mapping* : *Scale* X 1, Y 1, Z 0,02.
- **2.** *Noise* : *Scale* 2000, *Detail* 2.
- **3.** *Color Ramp* : noir à 0,68, blanc à 0,70. Aperçu : de rares traits blancs dans la longueur.
- **4.** *Map Range* (*To Min* 0,05, *To Max* 0,5) vers *Roughness*.
Contrôle : de fines rayures mates dans la longueur, visibles dans les reflets. Corrigé : `E5_Pratique_Main_courante_corrige`.

![Figure 3.79 : Le masque des rayures en aperçu, puis la main courante en inox rayé.](assets/images/scratches_handrail_blender.jpg)

### Recette · Les traces de doigts
Sur `E5_Pratique_Console`, une console noir piano de planche de bord (#0A0A0A, *Roughness* 0,3, *Coat Weight* 1, *Coat Roughness* 0,02) :
- **1.** *Texture Coordinate* (*Object*), puis *Noise* : *Scale* 25, *Detail* 6, *Roughness* 0,7, *Distortion* 0,3.
- **2.** *Map Range* : *From Min* 0,55, *From Max* 0,75, *To Min* 0,02, *To Max* 0,4.
- **3.** *Result* vers **Coat Roughness**, dans la rubrique *Coat* du Principled.
Contrôle : des halos voilés dans le reflet du vernis. Une trace de doigt ne change pas la couleur : seulement la brillance du vernis. Corrigé : `E5_Pratique_Console_corrige`.

![Figure 3.80 : La console noir piano, neuve, puis avec des traces de doigts dans le reflet du vernis.](assets/images/fingerprints_piano_black_blender.jpg)

> [!WARNING]
> Les rayures sont en travers : l'axe étiré dans *Mapping* n'est pas le bon. Il y en a trop : montez les deux curseurs, par exemple à 0,72 et 0,74. Les traces sont branchées sur *Base Color* : la pièce devient grise par plaques. Elles sont branchées sur *Roughness* : sous un vernis brillant, elles ne se voient presque pas. Elles ne se voient qu'à un endroit : il faut un reflet ; faites tourner l'image d'environnement.

> [!CAUTION]
> **Petit défi.** `E5_Defi_Coffret`, un coffret de quai de 200 × 120 × 80 mm posé sur sa plinthe `E5_Defi_Plinthe`. Usez ses arêtes avec la variante prismatique, puis salissez son pied, avec deux couches successives : un premier *Mix Color* passe de la peinture au métal, un second passe de ce résultat à la saleté. Salissez aussi la plinthe. Corrigés : `E5_Defi_Coffret_corrige` et `E5_Defi_Plinthe_corrige`.

```quiz
question: "Sous EEVEE, comment repérer les arêtes d'une pièce biseautée pour les user ?"
options:
  - "Avec Geometry > Pointiness"
  - "Avec le nœud Bevel"
  - "Avec la normale de la pièce, triée par un Color Ramp"
  - "Avec Ambient Occlusion, case Inside cochée"
correctIndices:
  - 2
explanation: "Pointiness et le nœud Bevel ne fonctionnent que sous Cycles. Sous EEVEE, Inside ne donne presque rien à cette échelle. Dans un biseau lissé, la normale passe d'une direction à l'autre : c'est elle que l'on trie."
```

```quiz
question: "Votre masque de saleté, tiré du nœud Ambient Occlusion, ne montre presque rien. Que faites-vous ?"
options:
  - "Cocher Only Local"
  - "Resserrer le Color Ramp près de 1, par exemple de 0,85 à 0,99"
  - "Passer Distance à 1 m"
  - "Augmenter Detail du bruit"
correctIndices:
  - 1
explanation: "Sous EEVEE, les valeurs de l'occlusion restent très proches de 1 : il faut une rampe très serrée. Only Local n'est pas pris en charge, et une grande Distance assombrit toute la pièce."
```

### Étape 6 · Les motifs
**Nouveau :** un motif régulier, construit à partir des coordonnées. Les sous-notions arrivent une par une : la grille, puis le perçage, puis le croisement de deux motifs. **Déjà vu :** *Voronoi*, *Wave*, *Math*, *Mix*, *Bump*, *Alpha* (section 1). Comptez 40 minutes.

**Exemple :** `E6_Exemple_Dalle`, une dalle à pastilles en relief, comme un plancher antidérapant ou une dalle podotactile de quai : *Voronoi* en **2D**, *Scale* 125, *Randomness* **0**, sortie *Distance* vers un *Color Ramp* (blanc à 0,28, noir à 0,32), puis un *Bump* (*Strength* 0,5). Avec *Randomness* 0, les cellules forment une grille parfaite : des pastilles de Ø 4,8 mm au pas de 8 mm.

![Figure 3.81 : Les motifs de l'étape 6 : la dalle à pastilles, la tôle perforée, le cuir grainé, le tissu de siège, puis, en défi, le moletage et le carbone sergé.](assets/images/procedural_patterns_overview_blender.jpg)

### Recette · La tôle perforée
Sur `E6_Pratique_Grille`, une plaque de 120 × 80 × 1,5 mm posée au-dessus d'un fond orange : une grille de haut-parleur automobile ou un plafond perforé de voiture ferroviaire (#B8B9BA, *Metallic* 1, *Roughness* 0,35).
- **1.** *Texture Coordinate* (*Object*), puis *Voronoi* : type **2D**, *Scale* 250, *Randomness* 0.
- **2.** Sortie *Distance* vers *Math*, opération *Greater Than*, *Threshold* 0,3.
- **3.** *Value* vers **Alpha** du Principled.
Contrôle : des trous ronds de Ø 2,4 mm au pas de 4 mm ; on voit le fond à travers, et l'ombre est percée. *Render Method* reste sur *Dithered*, sa valeur par défaut (figure 3.13). Corrigé : `E6_Pratique_Grille_corrige`.

![Figure 3.82 : La chaîne de la tôle perforée : Voronoi 2D (Scale 250, Randomness 0), Greater Than 0,3, Alpha. À droite, la grille au-dessus de son fond orange.](assets/images/perforated_sheet_alpha_blender.jpg)

> [!TIP]
> Deux formules pour régler la tôle en millimètres : *Scale* = 1000 / pas en mm ; seuil = diamètre / (2 × pas). L'étape 7 les range dans un groupe.

> [!WARNING]
> Les trous manquent ou n'ont pas tous la même taille : le *Voronoi* est en 3D, et le plan coupe la grille entre deux rangées de points ; passez-le en 2D. Les trous sont en désordre : *Randomness* est resté à 1. Il ne reste que des pastilles qui flottent : l'opération est *Less Than*. Les trous sont étirés sur une plaque dressée : le type 2D ne lit que X et Y ; ajoutez un *Mapping*, *Rotation* X 90°.

### Recette · Le cuir grainé
Sur `E6_Pratique_Accoudoir`, un accoudoir d'avion de 300 × 60 × 50 mm (#1E1B19, *Roughness* 0,55) :
- **1.** *Texture Coordinate* (*Object*), puis *Voronoi* : type 3D, *Scale* 500, *Distance to Edge*.
- **2.** *Distance* vers un *Color Ramp* : noir à 0, blanc à 0,08.
- **3.** *Color* vers *Height* d'un *Bump*, *Strength* 0,2, puis vers *Normal*.
Contrôle : un grain fin et régulier, des cellules de 2 mm aux sillons creusés. La section 2 utilisait une image ; ici, tout est calculé, sans aucun raccord. Option : *Detail* 2 rend le grain irrégulier. Corrigé : `E6_Pratique_Accoudoir_corrige`.

![Figure 3.83 : La chaîne du cuir : Voronoi (Distance to Edge, Scale 500), Color Ramp, Bump. À droite, l'accoudoir grainé.](assets/images/leather_grain_procedural_blender.jpg)

```side-by-side
layout: "textLeft"
imagePath: "assets/images/checker_texture_node_blender.jpg"
caption: "Figure 3.84 : Le nœud Checker Texture : Color1, Color2, Scale, et les sorties Color et Factor."
title: "Le Checker : un damier"
---
Le *Checker* (`Maj + A > Texture`) dessine un damier : sa sortie *Factor* vaut 0 sur une case, 1 sur la suivante. Il sert ici de masque, pour alterner deux motifs case par case.
```

### Recette · Le tissu de siège
Sur `E6_Pratique_Assise`, un échantillon d'assise ferroviaire de 120 × 120 × 40 mm :
- **1.** *Texture Coordinate* (*Object*), puis `Maj + A > Texture > Checker Texture`, *Scale* 500. Sa sortie *Factor* vers *Factor* d'un *Mix* en *Float*.
- **2.** Un *Wave* A : *Bands*, direction *X*, *Scale* 157. Sa sortie *Factor* vers *A* du *Mix*.
- **3.** Un *Wave* B : *Bands*, direction *Y*, *Scale* 157. Sa sortie *Factor* vers *B* du *Mix*.
- **4.** *Result* vers *Height* d'un *Bump* (*Strength* 0,4), puis vers *Normal*.
- **5.** Le même *Result* vers *Factor* d'un *Mix Color* : *A* #141C30, *B* #2E3D63, vers *Base Color*.
- **6.** Principled : *Roughness* 0,8, *Sheen Weight* 0,5.
La règle : le *Scale* des *Wave* vaut 0,314 fois celui du *Checker* ; on obtient une bosse de fil par case. Contrôle : une armure toile bleu marine, aux fils de 2 mm. Corrigé : `E6_Pratique_Assise_corrige`.

![Figure 3.85 : La chaîne du tissu : un Checker (Scale 500) choisit, case par case, entre deux Wave (Scale 157) en X et en Y ; le résultat va au Bump et à Mix Color.](assets/images/seat_fabric_weave_blender.jpg)

> [!WARNING]
> Les fils sont décalés ou moirés : la règle des 0,314 n'est pas respectée. Un moiré à distance : les fils sont trop fins pour l'écran ; il disparaît de près. Un tissu trop brillant : *Roughness* est trop basse ; un tissu reste mat. *Sheen* n'est qu'approché sous EEVEE : le relief du tissage fait l'essentiel.

```side-by-side
layout: "textRight"
imagePath: "assets/images/gradient_texture_radial_blender.jpg"
caption: "Figure 3.86 : Le nœud Gradient Texture et le menu de son type, avec Radial."
title: "Le Gradient en Radial"
---
Le *Gradient Texture* (`Maj + A > Texture`) en type *Radial* donne l'angle autour de l'axe Z, de 0 à 1 sur un tour. Sur une pièce de révolution, il permet de « dérouler » la surface : c'est l'indice du moletage.
```

### Consignes · ★ Deux motifs avancés
Deux défis facultatifs, avec leur recette complète. Essayez d'abord avec l'indice.
- **Le moletage**, sur `E6_Defi_Molette`, un bouton de commande de Ø 30 × 40 mm d'axe local Z, pour l'automobile ou un cockpit (#C8C8C6, *Metallic* 1, *Roughness* 0,35). Indice : on déroule le cylindre. *Gradient Texture* (*Radial*) fois 60 dents donne u ; *Separate XYZ*, sortie *Z*, fois 636,6, soit 60 / (2π × 0,015), donne v. Calculez u + v et u − v, passez chacun dans un *Math* *Ping-Pong* (*Scale* 0,5), gardez le *Minimum* des deux, puis un *Bump* (*Strength* 0,3).
- **Le carbone sergé 2/2**, sur `E6_Defi_Panneau`, un panneau galbé de 300 × 200 mm (*Roughness* 0,3, *Coat Weight* 1). Indice : on numérote les cases. *Separate XYZ* ; X et Y fois 250, puis *Floor* : le numéro de colonne et de rangée. Leur somme, *Floored Modulo* 4, puis *Less Than* 2 : le masque du sergé. Deux *Wave* (*Scale* 78,5, en X et en Y) choisis par ce masque dans un *Mix* en *Float*, vers un *Bump* (*Strength* 0,1). Le masque choisit aussi la teinte : *Mix Color*, *A* #0B0B0C, *B* #26262A.
Contrôle : des pointes de diamant de 1,6 mm sans couture ; un sergé en diagonale aux mèches de 4 mm. Le nombre de dents doit être entier, sinon une couture apparaît. Sur une pièce très galbée, le carbone s'étire : préférez alors l'image en projection *Box* de la section 2. Corrigés : `E6_Defi_Molette_corrige` et `E6_Defi_Panneau_corrige`.

![Figure 3.87 : La chaîne du moletage : Gradient Radial et Separate XYZ donnent u et v ; Add, Subtract, deux Ping-Pong et Minimum dessinent les pointes ; puis Bump.](assets/images/knurling_procedural_blender.jpg)

![Figure 3.88 : La chaîne du carbone sergé : les numéros de case (Multiply, Floor, Add, Floored Modulo, Less Than) choisissent entre deux Wave, vers Bump et Mix Color.](assets/images/carbon_twill_procedural_blender.jpg)

```quiz
question: "Pour percer une tôle sans modéliser les trous, sur quelle entrée du Principled branchez-vous le masque ?"
options:
  - "Transmission Weight"
  - "Normal"
  - "Alpha"
  - "Coat Weight"
correctIndices:
  - 2
explanation: "Alpha à 0 rend la surface invisible : on voit au travers, et l'ombre est percée. Transmission ferait un verre, pas un trou."
```

### Étape 7 · Les groupes de nœuds
**Nouveau :** le groupe de nœuds et ses paramètres exposés. **Déjà vu :** la chaîne des bords usés (étape 5), *Map Range* et *Math* (étape 2), le compteur d'utilisateurs, *Mark as Asset* (section 3). Comptez 25 minutes.

**Exemple :** `E7_Exemple_Grain`. Sa matière contient un seul nœud de groupe, `PRC_Grain_Fin`, qui regroupe un *Noise* et un *Bump*. Il a deux entrées, *Échelle* et *Relief*, et une sortie *Normal*. `Tab` entre dans le groupe, `Tab` en sort.

### Préparer : des chiffres à la place des curseurs
Les curseurs d'un *Color Ramp* ne peuvent pas devenir des paramètres d'un groupe. Sur `E7_Pratique_Socle`, le socle de l'étape 5 avec sa chaîne des bords usés, remplacez le *Color Ramp* à trois curseurs par trois nœuds :
- *Math* *Ping-Pong*, *Scale* 0,5 ;
- *Math* *Multiply*, par 2 ;
- *Map Range*, *From Min* 0,2, *From Max* 1.

L'aperçu montre le même liseré : c'est le même calcul, écrit en chiffres.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/node_make_group_menu_blender.jpg"
caption: "Figure 3.89 : Le menu Node du Shader Editor : Make Group (Ctrl + G) et Ungroup."
title: "Make Group"
---
Sélectionnez des nœuds, puis `Ctrl + G` ou *Node > Make Group* : ils deviennent un seul nœud de groupe. `Tab` entre dans le groupe et en sort ; `Ctrl + Alt + G` défait le groupe.
```

### Recette · Créer le groupe et exposer ses paramètres
Sur `E7_Pratique_Socle` :
- **1.** Sélectionnez les nœuds du masque, de *Texture Coordinate* au dernier *Map Range*, sans le Principled ni les *Mix*. `Ctrl + G`.
- **2.** `Tab` : l'intérieur du groupe, avec *Group Input* à gauche et *Group Output* à droite. Le lien qui sortait de la sélection est devenu la sortie du groupe.
- **3.** Ajoutez un *Math* *Subtract* dont la première valeur vaut 1. Glissez la prise vide de *Group Input* vers sa seconde entrée : c'est le paramètre *Largeur*. Reliez son résultat à *From Min* du premier *Map Range*.
- **4.** Exposez de même *Quantité*, le seuil du dernier *Map Range* : *From Min* = 0,7 − *Quantité*, *From Max* = *From Min* + 0,1, avec deux *Math*. Puis *Échelle du bruit*, le *Scale* du *Noise*.
- **5.** Barre latérale (`N`), onglet *Group* : nommez le groupe `PRC_Usure_Bords`. Dans la liste des entrées et des sorties, renommez chaque prise. *Largeur* : 0,8 par défaut ; *Quantité* : 0,4 ; toutes deux entre 0 et 1, au sous-type *Factor*. *Échelle du bruit* : 400. La sortie : *Masque*.
- **6.** `Tab` pour sortir. Sur le nœud de groupe, *Largeur* et *Quantité* se règlent comme des réglages de Blender.
Contrôle : le socle s'use comme à l'étape 5, et *Largeur* et *Quantité* se règlent sans entrer dans le groupe. Avec les valeurs par défaut, le groupe refait exactement la chaîne de l'étape 5. Corrigé : `E7_Pratique_Socle_corrige`, avec le groupe `PRC_Usure_Bords_corrige`.

![Figure 3.90 : L'intérieur du groupe PRC_Usure_Bords : Group Input à gauche, avec Largeur, Quantité et Échelle du bruit, plus l'entrée Axe du petit défi ; le masque calculé en chiffres ; Group Output à droite.](assets/images/node_group_inside_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/node_group_sidebar_interface_blender.jpg"
caption: "Figure 3.91 : La barre latérale du Shader Editor, onglet Group : le nom du groupe, sa description, la liste des entrées et des sorties, et les réglages de la prise Largeur."
title: "L'onglet Group"
---
L'onglet *Group* de la barre latérale (`N`) décrit le groupe ouvert : son nom, sa description, puis la liste de ses entrées et de ses sorties.

Le bouton `+` ajoute une entrée, une sortie ou un panneau. Sous la liste, la prise sélectionnée se règle : valeur par défaut, minimum, maximum et sous-type.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_menu_group_list_blender.jpg"
caption: "Figure 3.92 : Maj + A > Group : New Group, puis les groupes du fichier."
title: "Réutiliser un groupe"
---
Sur une autre pièce, `Maj + A > Group` liste tous les groupes du fichier. Choisissez `PRC_Usure_Bords`, puis reliez *Masque* à un *Mix Color* et à *Metallic*, comme à l'étape 5.

Les groupes suffixés « _corrige » sont ceux du corrigé.
```

![Figure 3.93 : Le groupe en service sur le socle : un seul nœud, avec ses paramètres Largeur, Quantité et Échelle du bruit, relié à Mix Color et Metallic.](assets/images/node_group_in_use_blender.jpg)

> [!WARNING]
> Le groupe sort un shader : le Principled était dans la sélection ; `Ctrl + Z`, puis resélectionnez sans lui. Le groupe ne rend rien : rien n'est relié au *Group Output*. Un paramètre accepte des valeurs absurdes : son minimum et son maximum n'ont pas été réglés. Modifier le groupe change toutes les pièces qui l'utilisent : c'est voulu, comme une matière partagée ; pour une variante, rendez le groupe indépendant par son compteur.

### Option : ranger et partager
- `Ctrl + J` encadre les nœuds sélectionnés dans un *Frame*. Son nom se règle dans la barre latérale, onglet *Node*, champ *Label*.
- `Maj + clic droit` glissé sur un lien ajoute un *Reroute*, pour plier les liens. `Ctrl + clic droit` glissé coupe des liens.
- Dans l'Outliner, en mode *Blender File*, rubrique *Node Groups* : clic droit sur le groupe, puis *Mark as Asset*. Le groupe rejoint la bibliothèque, comme les matières de la section 3.

![Figure 3.94 : Option : les nœuds du masque d'usure encadrés dans un Frame intitulé « Masque d'usure » ; à droite, son Label dans l'onglet Node de la barre latérale.](assets/images/node_frame_label_blender.jpg)

```side-by-side
layout: "textRight"
imagePath: "assets/images/node_group_mark_as_asset_blender.jpg"
caption: "Figure 3.95 : Option : l'Outliner en mode Blender File, rubrique Node Groups, et le clic droit sur le groupe, avec Mark as Asset."
title: "Option : le groupe en actif"
---
Marqué comme actif, le groupe se range dans un catalogue de la bibliothèque, comme une matière. On le retrouve dans un autre fichier par *File > Append*, dossier *NodeTree*.
```

### Consignes · Petit défi et défi final
- **★ Un axe au choix.** Ajoutez une entrée *Axe* (*Vector*, par défaut 0, 0, 1). Remplacez *Separate XYZ* (Z) par *Vector Math* *Dot Product*, entre la normale et *Axe*. Le même groupe use alors une pièce couchée sur Y, même si sa rotation a été appliquée.
- **★★ La tôle perforée en millimètres.** Un groupe `PRC_Tole_Perforee`, avec deux entrées, *Pas (mm)* (4) et *Diamètre (mm)* (2,4), et une sortie *Alpha*. À l'intérieur : *Math* *Divide* (1000 / *Pas*) vers *Scale* du *Voronoi* 2D ; *Math* *Divide* (*Diamètre* / *Pas*), puis *Multiply* 0,5, vers *Threshold* du *Greater Than*. Le designer règle des millimètres, pas des échelles.
- **Le défi final · La lampe d'atelier.** Rendez visible la collection `Lampe_defi`, une copie de la lampe en coloris A, puis donnez-lui dix ans de service : `PRC_Usure_Bords` sur le socle, qui laisse voir l'aluminium, et sur les articulations, dont le chrome s'use jusqu'au laiton ; la saleté au pied des lamelles de la grille, avec *Distance* `5mm` ; les rayures sur les bras ; les traces de doigts sur la laque de la tête, par son *Coat Roughness*. Pas d'usure des bords sur la tête : elle est bombée.
Corrigés : sous-collection « Corrigé étape 7 » : le groupe `PRC_Usure_Bords_corrige`, avec son entrée *Axe* ; `E7_Grille_mm_corrige`, avec `PRC_Tole_Perforee_corrige` ; et `Lampe_defi_corrige`.

![Figure 3.96 : Le défi final : la lampe neuve, la lampe d'atelier, puis son socle vu de près, à l'arête usée jusqu'à l'aluminium.](assets/images/workshop_lamp_wear_blender.jpg)

```quiz
question: "Pourquoi remplacer le Color Ramp par Map Range et Math avant de créer le groupe ?"
options:
  - "Un Color Ramp ne fonctionne pas dans un groupe"
  - "Les curseurs d'un Color Ramp ne peuvent pas devenir des paramètres du groupe"
  - "Map Range est plus rapide sous EEVEE"
  - "Ctrl + G supprime les Color Ramp"
correctIndices:
  - 1
explanation: "Un groupe expose des entrées de nœuds. Les curseurs d'un Color Ramp n'en sont pas, alors que From Min ou Threshold en sont."
```
