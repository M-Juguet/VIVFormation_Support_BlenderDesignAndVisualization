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
