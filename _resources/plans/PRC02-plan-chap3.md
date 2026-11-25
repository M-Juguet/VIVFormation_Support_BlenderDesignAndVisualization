# Chapitre 3 · Matières et finitions réalistes sans dépliage UV : plan

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 5 · En présentiel, de 5 à 8 apprenants · Plan validé le 18 novembre 2026, décisions du formateur intégrées le même jour · Mise à jour du 25 novembre 2026 : un lot de textures PBR sur le socle, dans le fil rouge (voir « Décisions du formateur, 25 novembre 2026 »)

## En bref

- **Objectif du chapitre :** créer des matières réalistes avec le Principled BSDF (métal, plastique, verre), appliquer des finitions CMF par projection triplanaire et organiser ses matières dans la bibliothèque d'actifs.
- **À la fin de la demi-journée, l'apprenant sait :**
  - régler une matière de métal, de plastique ou de verre avec le Principled BSDF ;
  - ajouter une finition brossée, grainée ou structurée, puis poser un lot de textures PBR, sans dépliage UV ;
  - ranger ses matières en actifs dans l'Asset Browser, et récupérer une matière d'un autre fichier avec *File > Append*.
- **Format :** 3 h 30 de contenu et 2 pauses de 10 minutes, soit 3 h 50. Il reste 10 minutes de marge sur 4 heures. Exemple : de 9 h 00 à 12 h 50.
- **Principe :** comme à l'initiation, une démo de 10 minutes au plus, un geste guidé, puis une pratique autonome sur la lampe. Les apprenants ne passent jamais plus de 15 minutes sans toucher la souris.
- **Fil rouge :** la lampe modélisée au chapitre 2 (`lampe_modele_v001.blend`). Elle repart habillée, en deux coloris, avec ses matières rangées en bibliothèque. C'est le point de départ du chapitre 4.
- **Affichage :** tout le chapitre se fait en vue *Material Preview*. Cette vue calcule les matières avec EEVEE, sous une image d'environnement intégrée à Blender : c'est suffisant pour juger une matière. L'éclairage de la scène, le mode *Rendered* et les réglages d'EEVEE restent au chapitre 4. Seule exception, décidée par le formateur : la case *Raytracing*, cochée pour le verre avec une seule phrase d'explication.
- **Une montée en douceur :** la section 1 se fait entièrement dans l'onglet *Material*, que les apprenants connaissent depuis Basics 101. Le Shader Editor et les nœuds n'arrivent qu'en section 2, quand les textures les rendent nécessaires, et un nœud à la fois.
- **De l'autonomie dans chaque section :** c'est le chapitre le plus abstrait. Les apprenants pratiquent seuls environ 50 minutes, dont 6 en section 3 et 16 dans l'atelier de 20 minutes.
- **Les corrigés :** selon la convention commune aux chapitres 2 à 4, chaque corrigé se trouve dans le fichier de travail, dans une collection masquée dont le nom commence par « Corrigé ». Un seul fichier séparé, justifié : la lampe habillée, point de départ du chapitre 4.

## La progression

### Ce que le chapitre approfondit

| Déjà vu | Où | Ce que le chapitre 3 en fait |
|---|---|---|
| L'éditeur de propriétés et ses onglets, dont *Material* | Basics 101 | Le lieu de toute la section 1 |
| Les modes d'affichage, *Material Preview* montré une fois | Basics 101 ; initiation, demi-journée 1 (Pack Resources) | La vue de travail de tout le chapitre |
| Les workspaces, dont *Shading* | Basics 101 ; initiation, demi-journée 1 | Le poste de travail des nœuds, en section 2 |
| `Maj + A`, `G`, `X` dans la vue 3D | Initiation | Les mêmes touches dans le Shader Editor |
| Le compteur d'utilisateurs, les données partagées | Basics 102 § 3 ; initiation, demi-journée 2 | Une matière partagée par plusieurs pièces ; une copie indépendante pour une finition ou un coloris |
| L'échelle appliquée (`Ctrl + A > Scale`) | Basics 103 ; clinique, patient 2 | La condition d'une projection régulière |
| *Pack Resources* | Basics 102 § 4 ; initiation, demi-journée 1 | Empaqueter les images de finition |
| Append et Link, cités en une phrase | Basics 102 § 4 ; initiation, demi-journée 1 | Append mis en pratique avec le nuancier ; Link reste cité en une phrase, sa manipulation devient un défi |
| La vue locale (`/`), le menu *Viewport Shading* | Chapitre 1 | Isoler l'ampoule ; choisir l'image d'environnement |
| *Duplicate Collection*, les variantes | Chapitre 1 | Le second coloris de l'atelier |
| *Shade Auto Smooth*, les modificateurs non appliqués | Chapitre 2 | Des surfaces lisses, qui reflètent proprement |
| La lampe en pièces séparées et nommées | Chapitre 2 | L'objet à habiller |

### Une notion nouvelle à la fois

Chaque ligne passe de la démonstration à la pratique guidée, puis à la pratique autonome, avant la suivante.

| Séquence | La notion nouvelle | Elle s'appuie sur |
|---|---|---|
| Ouverture | Aucune : un check-up | Basics 103, chapitre 2 |
| Une matière dans Blender | La matière : la créer, la nommer, la partager | L'onglet *Material*, le compteur d'utilisateurs |
| Métal et plastique | *Metallic* et *Roughness*, puis *Coat* | La matière, *Base Color* |
| Le verre | La transmission et ses deux interrupteurs | *Roughness*, l'onglet *Render* |
| Le Shader Editor | Le nœud et le lien | La matière de la section 1, l'espace *Shading*, `Maj + A` |
| Finitions procédurales | Les coordonnées *Object*, puis le relief *Bump*, puis l'étirement *Mapping* | Le nœud et le lien |
| Projection triplanaire | L'image projetée en *Box* | La même chaîne ; l'échelle appliquée |
| Lot PBR sur le socle | Plusieurs cartes sur un seul *Mapping*, puis le *Normal Map* ; le bouclier (*Fake User*) | La projection *Box*, *Non-Color*, la copie d'une matière ; Pack Resources |
| Ranger en actifs | L'actif et le catalogue, puis le glisser-déposer d'une vignette | Les matières, le sélecteur de type d'éditeur, la barre latérale |
| Réutiliser | *File > Append* mis en pratique ; Link cité en une phrase | Append et Link cités à l'initiation, la fenêtre d'ouverture de fichiers, l'actif |
| Atelier | Aucune | Chapitre 1, initiation, sections 1 à 3 |

## Minutage

| Horaire | Durée | Séquence | Section | Modalité |
|---|---|---|---|---|
| 0:00 | 15 min | Ouverture et check-up du modèle | | Collectif 5 min + contrôle sur poste 10 min |
| 0:15 | 20 min | Une matière dans Blender | 1 | Démo 7 min + guidée 13 min |
| 0:35 | 30 min | Métal et plastique | 1 | Démo 8 min + guidée 7 min + autonomie 10 min ; *Coat* : démo 2 min + guidée 3 min |
| 1:05 | 10 min | Pause | | |
| 1:15 | 16 min | Le verre | 1 | Démo 7 min + guidée 9 min ; le verre dépoli ou fumé devient un défi ★ |
| 1:31 | 15 min | Le Shader Editor : la matière en nœuds | 2 | Démo 6 min + guidée 9 min |
| 1:46 | 25 min | Finitions procédurales sans UV | 2 | Trois étapes démo + guidée (19 min) + autonomie 6 min |
| 2:11 | 21 min | Projection triplanaire d'images | 2 | Démo 8 min + guidée 9 min + autonomie 3 min + quiz 1 min |
| 2:32 | 12 min | Un lot de textures PBR sur le socle | 2 | Démo Poly Haven 2 min + démo 3 min + guidée 5 min + *Pack Resources* 1 min + quiz 1 min |
| 2:44 | 10 min | Pause | | |
| 2:54 | 18 min | Ranger ses matières en actifs | 3 | Démo 7 min + guidée 7 min + autonomie 4 min ; la description d'un actif devient un défi ★ |
| 3:12 | 12 min | Réutiliser : récupérer une matière par Append | 3 | Démo 5 min + guidée 7 min |
| 3:24 | 20 min | Atelier · Le second coloris | | Lancement 2 min + autonomie 16 min + revue 2 min |
| 3:44 | 6 min | Tour des postes, bilan et passerelle | | Collectif, une question orale |
| 3:50 | | Fin | | |

Répartition : section 1, 66 minutes ; section 2, 73 minutes ; section 3, 30 minutes ; ouverture 15 minutes, atelier 20 minutes et bilan 6 minutes. Total : 210 minutes de contenu. La première pause tombe à la même heure qu'à l'initiation, la seconde à 2:44. Le déroulé formateur détaille chaque séquence ; les 12 minutes du lot PBR sont reprises comme le décrit « Décisions du formateur, 25 novembre 2026 ».

Pratique autonome : environ 45 minutes, soit 10 en section 1, 10 en section 2, 4 en section 3 et 16 dans l'atelier ; la recette guidée du lot PBR s'y ajoute.

## Avant la demi-journée

### Les postes des apprenants

- [ ] Le fichier de fin du chapitre 2, `lampe_modele_v001.blend`, est dans le dossier de travail.
- [ ] Les fichiers du chapitre 3 sont copiés : la lampe à habiller, les finitions triplanaires, le dossier `textures_cmf` et le dossier `PRC02_bibliotheque_CMF`, avec son fichier `blender_assets.cats.txt` (voir « Fichiers d'exercice »).
- [ ] Les préférences des postes ne sont pas modifiées : le parcours principal n'en a pas besoin.
- [ ] *Material Preview* reste fluide avec la case *Raytracing* cochée. À tester sur chaque modèle de poste : c'est le réglage le plus exigeant du chapitre.

### Votre poste de démonstration

- Blender lancé en configuration d'usine (`blender.exe --factory-startup`), comme à l'initiation.
- *Resolution Scale* à 1,3 pour le vidéoprojecteur.
- La lampe à habiller, le nuancier `PRC02_ch3_nuancier_cmf.blend` et `PRC02_ch3_finitions_triplanaires.blend` prêts à ouvrir.
- La lampe habillée `PRC02_ch3_lampe_habillage.blend` prête à ouvrir, pour l'ouverture. Les corrigés des exercices sont dans les collections masquées de la lampe à habiller et des finitions triplanaires : vous les projetez aux points de contrôle.
- Option, pour la démo de 3:10 : la bibliothèque `PRC02_bibliotheque_CMF` déclarée dans vos propres préférences.

### Le matériel de la salle

- Les post-it vert et rose des points de contrôle.
- Le paperboard des raccourcis du jour. Section 1 : `/`. Section 2 : `Maj + A`, `G`, `X` et `Origine` dans le Shader Editor, `Ctrl + A > Scale`. Section 3 : `N`.
- Le minuteur.

## Ouverture · 0:00 (15 min)

**Où l'on en est (5 min, collectif) :**
- Le parcours de la lampe : bloquée au chapitre 1, modélisée au chapitre 2, habillée aujourd'hui, mise en scène au chapitre 4.
- Projetez la lampe habillée, `PRC02_ch3_lampe_habillage.blend` : la lampe en *Material Preview*, dans ses deux coloris. « Ce soir, votre lampe ressemble à celle-ci, et ses matières sont rangées pour vos prochains projets. »
- Le mot CMF : *Color, Material, Finish*. C'est le métier qui choisit les teintes, les matières et les finitions d'un produit : la sellerie d'un train, la planche de bord d'une voiture, l'habillage d'une cabine d'avion.

**Le check-up du modèle (10 min, sur poste) :** chacun ouvre `lampe_modele_v001.blend` et l'enregistre sous `lampe_habillage_v001.blend`. Puis il vérifie cinq points déjà vus :
1. chaque pièce porte un nom clair dans la collection *Lampe* ;
2. l'échelle est appliquée : *Scale* à 1 dans `N > Item`, sinon `Ctrl + A > Scale` ;
3. les normales sont tournées vers l'extérieur (*Face Orientation*) ;
4. aucune pièce courbe ne montre de facettes, en particulier les tiges des bras et les articulations, qui seront en métal : sinon *Object > Shade Auto Smooth* (chapitre 2) ;
5. le moteur de rendu est EEVEE, dans l'onglet *Render* (le fichier du chapitre 1 était réglé sur Cycles).

Un modèle incomplet ou abîmé ? L'apprenant ouvre le fichier de secours `PRC02_ch3_lampe_a_habiller.blend` et l'enregistre sous `lampe_habillage_v001.blend`.

**Point de contrôle :** un post-it vert sur chaque écran. Les cinq points sont bons ou le fichier de secours est ouvert.

**Points d'observation :**
- Le check-up reprend la clinique du fichier de l'initiation : renvoyez aux patients 1 et 2.
- Ne laissez personne réparer un modèle plus de 5 minutes : le fichier de secours existe pour cela.

## Section 1 · Principled BSDF : métal, plastique, verre

Ancre `ch3_sec1_title` · 70 minutes, de 0:15 à 1:35, pause comprise · Espace de travail *Layout*

**Prérequis déjà vus :** l'éditeur de propriétés et ses onglets (Basics 101) ; *Material Preview* (Basics 101, initiation) ; le compteur d'utilisateurs (initiation, demi-journée 2) ; l'onglet *Render* (initiation, chasse aux réglages) ; la vue locale et le menu *Viewport Shading* (chapitre 1).

**Ce que la section apporte :** la matière et son Principled BSDF, réglés uniquement depuis l'onglet *Material* ; les réglages qui distinguent un métal, un plastique, une laque et un verre ; les deux interrupteurs du verre sous EEVEE. Aucun nœud n'est encore montré : l'onglet *Material* affiche les mêmes réglages sous forme de liste (vérifié dans Blender 5.2.1).

### Notions prévues dans l'application

| Sous-titre prévu | Contenu | Figures |
|---|---|---|
| Où l'on en est | Le parcours de la lampe, ce que l'on construit, les prérequis (encart NOTE) | 3.1 |
| Voir les matières : Material Preview | *Solid* n'affiche pas les matières ; *Material Preview* les calcule avec EEVEE sous une image d'environnement intégrée. En option : choisir l'image *studio*, la faire tourner. | 3.2, 3.3 |
| Créer et nommer une matière | Onglet *Material*, bouton *New*, nom ; une convention : `Matière_Finition_Teinte` | 3.4 |
| Le Principled BSDF | Le réglage *Surface* de l'onglet : un seul modèle pour presque toutes les matières ; *Base Color* | 3.5 |
| Une matière pour plusieurs pièces | La liste des matières existantes, à gauche du nom ; le compteur d'utilisateurs. Astuce : `Ctrl + L > Link Materials` | 3.6, 3.17 |
| Métal ou non : Metallic | 0 ou 1, rarement entre les deux ; la couleur d'un métal se règle dans *Base Color* | 3.7 |
| Du poli au mat : Roughness | De 0, le miroir, à 1, le mat | 3.7 |
| Laque et vernis : Coat | Un vernis transparent par-dessus : carrosserie, livrée de train, carénage peint | 3.8 |
| Des valeurs de départ | Liste indicative (ci-dessous) | |
| Le verre : Transmission | *Transmission Weight*, *Roughness* pour le dépoli, IOR, teinte | 3.9 |
| Voir à travers le verre | Les deux interrupteurs : *Raytracing* (onglet *Render*) et *Raytraced Transmission* (onglet *Material*, rubrique *Settings*). Une seule phrase sur *Raytracing* : « Sans elle, le verre ne réfracte pas ; le chapitre 4 explique ce réglage. » | 3.10, 3.11, 3.12 |
| Un verre fin : Thin Wall | Paroi fine sans déformation : ampoule, vitre, pare-brise | 3.13 |
| Une matière qui éclaire : Emission (encart NOTE) | Un voyant, un écran, un filament. Pratique en défi ; la lampe s'éclaire au chapitre 4. | 3.14 |
| Ce qu'EEVEE simplifie (encart NOTE) | *Anisotropic*, le nœud *Bevel* et *Thin Film* ne fonctionnent que sous Cycles. Le brossé se simule à la section 2 ; les arrondis viennent de la géométrie. | |
| Option : deux matières sur une pièce | Deux emplacements (*slots*) sur la tête, puis *Material Offset* de son Solidify : l'intérieur prend la seconde matière | 3.15, 3.16 |

**Exemples multisectoriels à citer :** une jante en aluminium, une main courante en inox, un carénage en aluminium ; une planche de bord en plastique, une tablette de siège ; un pare-brise, un hublot, un feu arrière en polycarbonate.

**Valeurs de départ (indicatives) :** voir le tableau des matières de la bibliothèque, fiche B. En résumé :

| Matière | Metallic | Roughness | Autres réglages |
|---|---|---|---|
| Aluminium, inox, chrome, laiton | 1 | de 0,03 (chrome) à 0,4 (satiné) | La teinte du métal dans *Base Color* |
| Plastique brillant, mat | 0 | de 0,15 à 0,6 | |
| Caoutchouc, PVC | 0 | 0,7 à 0,85 | *Base Color* presque noire, jamais 0 |
| Laque | 0 | 0,4 | *Coat Weight* 1, *Coat Roughness* 0,03 |
| Verre clair, dépoli | 0 | 0 ; 0,4 | *Transmission Weight* 1, IOR 1,5, *Thin Wall* pour une paroi fine |
| Polycarbonate teinté | 0 | 0,05 | *Transmission Weight* 1, IOR 1,58, *Base Color* teintée |

### 0:15 · Une matière dans Blender (20 min)

**Nouveau :** la matière. **Déjà vu :** l'onglet *Material* (la sphère à damier de Basics 101), le compteur d'utilisateurs.

**Vous montrez (7 min),** sur la lampe à habiller, dans l'espace *Layout* :
- En *Solid*, aucune matière ne s'affiche. Le bouton *Material Preview* : Blender calcule les matières avec EEVEE.
- Le socle sélectionné : onglet *Material*, *New*. Renommer la matière `Peinture_Vert`. La rubrique *Surface* indique *Principled BSDF* et liste ses réglages. « Aujourd'hui, un seul : *Base Color*. » Changer la teinte.
- La tête sélectionnée : la liste des matières, à gauche du bouton *New*, puis `Peinture_Vert`. Le compteur affiche 2. Changer la teinte : les deux pièces changent. « Vous avez déjà vu ça : les roues de la maquette. »

**Ils font (13 min),** sur leur lampe :
1. passer en *Material Preview* ;
2. créer la peinture du socle, la nommer et choisir une teinte ;
3. la donner à la tête par la liste des matières ;
4. créer `ABS_Noir` sur l'interrupteur, puis la donner à la grille d'aération ;
5. vérifier le compteur de chaque matière.

**Point de contrôle :** socle et tête de la même teinte, interrupteur et grille en noir ; le compteur affiche 2 pour chaque matière.

**Points d'observation :**
- La première bascule en *Material Preview* fige l'écran quelques secondes : Blender prépare ses shaders. Prévenez avant.
- *New* sur un objet qui a déjà une matière crée `Material.001` : renommez tout de suite.
- La grille d'aération a un *Empty* enfant (chapitre 2) : c'est la grille elle-même qu'il faut sélectionner.
- Astuce pour les plus rapides : `Ctrl + L > Link Materials` donne la matière de l'objet actif à toute la sélection.

### 0:35 · Métal et plastique (30 min)

**Nouveau :** *Metallic* et *Roughness*, puis *Coat*. **Déjà vu :** la matière, *Base Color*.

**Vous montrez (8 min),** sur le nuancier `PRC02_ch3_nuancier_cmf.blend` :
- *Metallic* : 0 pour un plastique, une peinture ou un verre ; 1 pour un métal. Une valeur intermédiaire ne correspond à aucune matière réelle.
- La couleur d'un métal se règle dans *Base Color* : gris clair pour l'aluminium, jaune doré pour le laiton.
- *Roughness* : la grille des pastilles, du poli miroir au mat.
- Option : dans le menu *Viewport Shading* (vu au chapitre 1), choisir l'image *studio* et la faire tourner. Les reflets glissent : c'est ainsi qu'on juge une finition.

**Ils font, guidé (7 min) :** `Alu_Naturel` sur *Bras_bas* : *Metallic* 1, *Roughness* 0,3, *Base Color* gris très clair. Puis la même matière sur *Bras_haut*, par la liste.

**Ils font, en autonomie (10 min),** d'après le cahier CMF de la lampe :
- `Chrome` sur les trois articulations ;
- `PVC_Mat_Noir` sur le câble ;
- la *Roughness* de `ABS_Noir`, à 0,15.

**Coat (5 min) :**
- **Vous montrez (2 min) :** sur `Peinture_Vert`, dépliez la rubrique *Coat* : *Weight* 1, *Roughness* 0,03. La peinture devient une laque.
- **Ils font (3 min) :** la même chose sur leur peinture. L'atelier réinvestira ce réglage.

**Point de contrôle :** vue de face en *Material Preview*. On distingue au premier regard le métal (reflets nets, colorés par l'environnement), la laque (reflet net sur la teinte) et le plastique mat.

**Points d'observation :**
- *Metallic* à 0,5 : la pièce paraît sale. Revenez à 0 ou à 1.
- *Base Color* en noir pur : la pièce perd tout modelé. Gardez un gris très sombre.
- Des reflets en escalier sur une tige : *Shade Auto Smooth* manque (point 4 du check-up).
- Le câble est une courbe : son onglet *Material* fonctionne comme celui d'un maillage.

### 1:05 · Pause (10 min)

### 1:15 · Le verre (16 min)

**Nouveau :** la transmission et ses deux interrupteurs. **Déjà vu :** *Roughness*, l'onglet *Render*, la vue locale.

**Vous montrez (7 min) :**
- `Verre_Clair` sur l'ampoule : dépliez *Transmission*, *Weight* 1 ; *Roughness* 0. L'ampoule montre le paysage de l'image d'environnement, pas le fond de la tête. Faites deviner pourquoi.
- Les deux interrupteurs : onglet *Render*, case *Raytracing* ; onglet *Material*, rubrique *Settings*, case *Raytraced Transmission*. Pour *Raytracing*, une seule phrase : « Sans elle, le verre ne réfracte pas ; le chapitre 4 explique ce réglage. »
- L'ampoule du chapitre 2 est un volume plein : elle déforme comme une boule de cristal. La case *Thin Wall*, en haut de la liste, en fait une paroi fine, comme une ampoule, une vitre ou un pare-brise.
- *Roughness* 0,4 : un verre dépoli. Une *Base Color* teintée : un verre fumé, un feu arrière. L'IOR se cite seulement : 1,5 pour le verre, 1,58 pour le polycarbonate.

**Ils font, guidé (9 min) :**
1. isoler l'ampoule et la tête en vue locale (`/`) ;
2. créer `Verre_Clair` et cocher les deux interrupteurs ;
3. cocher *Thin Wall*.

**Ils font, en autonomie (4 min) :** essayer un verre dépoli ou teinté, puis garder celui qui convient à leur lampe.

**Point de contrôle :** en vue de dessous, le fond de la tête se voit à travers l'ampoule, sans déformation.

**Points d'observation :**
- Une seule case cochée : rien ne change. Il faut les deux.
- La case *Raytracing* n'apparaît pas : le moteur est resté sur Cycles (point 5 du check-up).
- L'ampoule est une courbe avec un modificateur Screw : son onglet *Material* fonctionne comme celui d'un maillage.
- Un poste devient lent : décochez *Raytracing* le temps des autres séquences, puis recochez-la avant d'enregistrer.

### Quiz de la section 1

1. « Une pièce en aluminium ressemble à du plastique gris. Quel réglage corriger ? » *Metallic* à 1 ; leurres : *Roughness* à 0, une *Base Color* plus claire, *Coat Weight* à 1.
2. « Votre ampoule montre le paysage de l'environnement, mais pas la tête placée derrière elle. Que faut-il activer ? » Les deux : *Raytracing* dans l'onglet *Render* et *Raytraced Transmission* dans la matière ; leurres : l'une ou l'autre seule, *Thin Wall*.
3. Option : « Quel réglage ajoute un vernis brillant par-dessus une teinte ? » *Coat* ; leurres : *Metallic*, *Roughness* à 0, *Specular Tint*.

### Défi fil rouge de la section 1 (encart CAUTION)

Habillez toute la lampe d'après le cahier CMF : laque du socle et de la tête, aluminium des bras, chrome des articulations, plastique de l'interrupteur, de la grille et du câble, verre de l'ampoule. Nommez chaque matière. Les teintes et les valeurs sont indicatives : composez votre propre gamme.

## Section 2 · Finitions CMF en projection triplanaire

Ancre `ch3_sec2_title` · 73 minutes, de 1:31 à 2:44 · Espace de travail *Shading*

**Prérequis déjà vus :** les matières de la section 1 et les réglages du Principled ; l'espace *Shading* (Basics 101) ; `Maj + A`, `G` et `X` dans la vue 3D (initiation) ; le compteur d'utilisateurs (initiation) ; `Ctrl + A > Scale` (Basics 103) ; *Pack Resources* et la fenêtre d'ouverture de fichiers (initiation, demi-journée 1).

**Ce que la section apporte :** le Shader Editor, le nœud et le lien ; une texture procédurale ; les coordonnées *Object* ; le relief par *Bump* ; l'étirement par *Mapping* ; l'image projetée en *Box* et l'espace colorimétrique *Non-Color* ; enfin un lot de textures PBR, ses cartes sur un seul *Mapping* et le *Normal Map*. Les nœuds sont introduits un par un : on part de la matière déjà réglée, que l'on retrouve sous forme de nœud, puis chaque étape ajoute un seul nœud.

### Notions prévues dans l'application

| Sous-titre prévu | Contenu | Figures |
|---|---|---|
| Pourquoi pas de dépliage UV | Le dépliage UV sert à poser une image à un endroit précis. Une finition uniforme (grain, brossé, structure) s'applique en 3D, sans dépliage, comme les cartes d'un lot de textures. | |
| Le Shader Editor : la même matière, vue en nœuds | L'espace *Shading* ; le nœud *Principled BSDF* porte les mêmes réglages que l'onglet *Material* ; le nœud *Material Output* ; entrées à gauche, sorties à droite ; le lien | 3.18, 3.19 |
| Se déplacer et agir dans le Shader Editor | Molette pour zoomer, clic molette pour déplacer la vue, `Origine` pour tout voir ; `G` et `X` comme dans la vue 3D | |
| Ajouter un nœud et le relier | `Maj + A` ; glisser d'une sortie vers une entrée ; glisser un lien hors de son entrée pour le défaire | 3.20, 3.21 |
| Une texture procédurale : Noise | Une texture calculée, sans image, sans raccord ; *Scale* compte les motifs par mètre | 3.21 |
| Les coordonnées de texture | Le nœud *Texture Coordinate* : *Generated* étire la texture selon la boîte de l'objet ; *Object* garde la même taille partout ; *UV* n'est pas utilisé ici | 3.22 |
| Du motif au relief : Bump | *Height* vers *Normal* du Principled ; *Strength* adaptée à un petit objet | 3.23 |
| Étirer pour brosser : Mapping | *Scale* du nœud *Mapping*, dans l'axe de la pièce | 3.24 |
| Une image projetée sur trois axes : Box | *Image Texture*, menu *Projection*, *Box*, puis *Blend* pour fondre les raccords | 3.25 à 3.28 |
| Les images de données : Non-Color | Une image de relief n'est pas une couleur : *Color Space* sur *Non-Color* ; une image de couleur reste en *sRGB* | 3.29 |
| L'échelle appliquée, condition de la projection | Une échelle non appliquée étire la texture : `Ctrl + A > Scale` | 3.30 |
| Un lot de textures PBR | Plusieurs cartes d'un même échantillon : `diff` (*sRGB*), `rough`, `nor_gl`, `disp` (*Non-Color*) | |
| Où trouver des lots : Poly Haven | Licence CC0, taille réelle, définition 1K, cartes en JPG ; démo du formateur ; ressource `PRC02_ch3_textures_pbr.zip` | |
| Toutes les cartes en projection Box | Un seul *Texture Coordinate* (*Object*) et un seul *Mapping* ; *Scale* compte les répétitions par mètre | 3.33 |
| La carte de normales : Normal Map | `Maj + A > Displacement > Normal Map`, entre l'image et *Normal* ; il fonctionne en *Box*, sans dépliage UV ; `nor_gl` et non `nor_dx` | 3.31, 3.34 |
| Garder une matière : le bouclier | *Fake User* garde une matière qu'aucune pièce ne porte ; le bouton de copie, juste à droite | 3.32 |
| Le même socle, plusieurs lots | Noyer, béton lisse, palissandre verni | 3.35 |
| Option : Node Wrangler | Extension livrée avec Blender, désactivée par défaut ; `Ctrl + T` ajoute *Texture Coordinate* et *Mapping* ; `Ctrl + Maj + T` charge un lot, à repasser en *Object* et en *Box* | 3.36, 3.37 |
| Empaqueter les images | *File > External Data > Pack Resources*, vu à l'initiation, une fois pour toutes les images | 3.38 |

**Exemples multisectoriels à citer :** un accoudoir en cuir grainé (aéronautique), une coque de rétroviseur grainée (automobile), une main courante en inox brossé et un marchepied en tôle larmée (ferroviaire), une pièce en fibre de carbone.

**La chaîne construite pas à pas :** *Texture Coordinate* (*Object*) → *Mapping* → texture → *Bump* → entrée *Normal* du Principled. La section change seulement la texture : procédurale d'abord, image ensuite. Le lot PBR garde le même *Mapping* et multiplie les images : `diff` → *Base Color*, `rough` → *Roughness*, `nor_gl` → *Normal Map* → *Normal*.

### 1:31 · Le Shader Editor : la matière en nœuds (15 min)

**Nouveau :** le nœud et le lien. **Déjà vu :** l'espace *Shading*, `Maj + A`, `G`, `X`, la matière `Alu_Naturel`.

**Vous montrez (6 min) :**
- L'onglet *Shading* : la vue 3D en *Material Preview* en haut, le Shader Editor en bas, l'éditeur de propriétés à droite.
- Un bras sélectionné : le Shader Editor montre deux nœuds, *Principled BSDF* relié à *Material Output*. « C'est la matière `Alu_Naturel`, vue autrement. » Changez *Roughness* dans le nœud : l'onglet *Material* suit.
- Lire un nœud : les entrées à gauche, les sorties à droite, le lien entre les deux. *Material Output* reçoit ce que l'objet affiche.
- Se déplacer : la molette zoome, le clic molette déplace la vue, `Origine` montre tous les nœuds. `G` déplace un nœud, `X` le supprime, comme dans la vue 3D.
- `Maj + A > Texture > Noise Texture`. Glisser de sa sortie *Color* vers l'entrée *Base Color* : le bras se couvre de nuages gris. Glisser le lien hors de *Base Color* : il disparaît, le bras redevient uni.

**Ils font, guidé (9 min),** sur un bras de leur lampe :
1. passer dans l'espace *Shading* et retrouver les deux nœuds ;
2. changer *Roughness* dans le nœud, puis vérifier l'onglet *Material* ;
3. `Origine` pour tout voir ;
4. ajouter *Noise Texture* et relier *Color* à *Base Color* ;
5. défaire ce lien, sans supprimer le nœud : il resservira.

**Point de contrôle :** chaque bras a montré des nuages gris, puis il est redevenu uni. Le nœud *Noise Texture* reste dans l'éditeur.

**Points d'observation :**
- Le Shader Editor est vide : l'objet actif n'a pas de matière, ou ce n'est pas le bon objet.
- La vue 3D de l'espace *Shading* a ses propres réglages : son image d'environnement peut différer de celle de l'espace *Layout*.

### 1:46 · Finitions procédurales sans UV (25 min)

**Nouveau :** trois nœuds, l'un après l'autre : *Texture Coordinate*, *Bump*, *Mapping*. **Déjà vu :** le nœud et le lien, *Noise Texture*.

**Étape 1 · Les coordonnées (démo 3 min + guidée 3 min).** Reliez de nouveau *Noise* à *Base Color* : le motif est étiré sur la longueur du bras. `Maj + A > Input > Texture Coordinate`, sortie *Object* vers l'entrée *Vector* du *Noise* : le motif garde la même taille partout. La lampe est petite : *Scale* du *Noise* passe de 5 à 1000, soit environ un motif par millimètre.

**Étape 2 · Le relief (démo 3 min + guidée 4 min).** Défaites le lien vers *Base Color*. `Maj + A > Displacement > Bump` : *Factor* du *Noise* vers *Height*, *Normal* du *Bump* vers *Normal* du Principled. Le motif devient un relief. *Strength* passe de 1 à 0,2 ; *Distance* garde sa valeur : la force par défaut est trop forte pour un si petit objet.

**Étape 3 · Le brossé (démo 2 min + guidée 4 min).** `Maj + A > Utilities > Vector > Mapping`, entre *Texture Coordinate* et *Noise*. *Scale* Z à 0,02 : le grain s'étire en fines rayures dans l'axe du bras. *Strength* du *Bump* à 0,15. Renommez la matière `Alu_Brosse`.

**Ils font, en autonomie (6 min) :** la même chaîne, sans *Mapping*, sur `ABS_Noir` : un grain fin pour l'interrupteur et la grille (*Noise Scale* 1500, *Strength* 0,05). Les plus rapides microbillent les articulations.

**Point de contrôle :** sur chaque tige, les rayures suivent la longueur du bras ; le grain de l'interrupteur est régulier.

**Points d'observation :**
- Rien ne se voit : *Scale* du *Noise* est resté trop faible, un seul motif couvre la pièce.
- Un relief qui scintille : *Strength* trop forte. Divisez-la par deux.
- Les rayures sont en travers : l'axe étiré dans *Mapping* n'est pas le bon. Les axes *Object* sont ceux de la pièce : la rotation des bras n'est pas appliquée au chapitre 2, c'est voulu.

### 2:11 · Projection triplanaire d'images (21 min)

**Nouveau :** l'image projetée en *Box*, avec son espace colorimétrique. **Déjà vu :** la chaîne de l'étape précédente, le compteur d'utilisateurs, `Ctrl + A > Scale`, *Pack Resources*.

**Vous montrez (8 min),** sur `PRC02_ch3_finitions_triplanaires.blend` :
- L'accoudoir n'a pas de dépliage UV. Le nœud *Image Texture* et l'image de cuir grainé, reliés sans coordonnées : rien de lisible. Avec *Object* et la projection *Flat* : l'image coule sur les flancs.
- Le menu *Projection*, *Box* : l'image est projetée sur trois axes, d'où le nom de projection triplanaire. Les raccords se voient à 45°. *Blend* à 0,25 les fond.
- *Color Space* sur *Non-Color* : une image de relief est une donnée, pas une couleur. Une image de couleur, comme celle du carbone, reste en *sRGB*.
- Le piège : l'accoudoir jumeau, dont l'échelle n'est pas appliquée. Le grain s'étire. `Ctrl + A > Scale` le remet d'aplomb : c'est le patient 2 de la clinique.

**Ils font, guidé (9 min),** sur le socle de leur lampe :
1. rendre la laque du socle indépendante : un clic sur son compteur, puis la renommer `Structure_Vert`. Même teinte, autre finition : c'est une décision CMF ;
2. *Coat Weight* à 0, *Roughness* à 0,6 ;
3. ajouter *Image Texture*, *Open*, puis `textures_cmf/grain_structure.png` ; *Non-Color* ; projection *Box*, *Blend* 0,25 ;
4. relier *Texture Coordinate* (*Object*), *Mapping* (*Scale* 50 sur les trois axes), l'image, *Bump* (*Strength* 0,2) et *Normal*.

**Ils font, en autonomie (3 min) :**
- faire le tour du socle et régler *Blend* et *Scale* jusqu'à ne plus voir de raccord ;
- enregistrer. *Pack Resources* attend la fin du lot PBR.

**Point de contrôle :** au tour du socle, aucun raccord visible.

**Points d'observation :**
- Le grain paraît coloré ou trop contrasté : *Color Space* est resté en *sRGB*.
- Le grain du socle est une image de hauteur, en niveaux de gris : il passe par un *Bump*. Une carte de normales passe par un *Normal Map*, en projection *Box*, sans dépliage UV : c'est la séquence suivante.
- Le grain apparaît aussi sur la tête : la laque n'a pas été rendue indépendante avant la modification. `Ctrl + Z`, puis le compteur.

### 2:32 · Un lot de textures PBR sur le socle (12 min)

**Nouveau :** plusieurs cartes sur un seul *Mapping*, le nœud *Normal Map*, le bouclier (*Fake User*). **Déjà vu :** la projection *Box* et *Non-Color* (séquence précédente), la copie d'une matière, *Pack Resources*.

**Vous montrez le téléchargement (2 min),** dans un navigateur : la page `https://polyhaven.com/a/walnut_veneer_02`, sa licence CC0 et sa taille réelle (« 1m wide ») ; la définition passée de 4K à 1K ; la flèche de *Download*, qui liste les cartes (*Diffuse*, *Rough*, *Normal (GL)*, *Displacement*) en EXR, JPG ou PNG. Le dossier `textures_pbr` contient déjà les trois lots.

**Vous montrez la chaîne (3 min),** sur le socle de votre copie : le bouclier de `Structure_Vert`, le bouton de copie, la copie `Bois_Noyer` ; dans le nœud *Image Texture* de la copie, la carte `diff` (*sRGB*) vers *Base Color*, le *Bump* supprimé, *Scale* du *Mapping* à 2 ; `Maj + D` et la carte `rough` (*Non-Color*) vers *Roughness* ; `Maj + D` et la carte `nor_gl` (*Non-Color*), puis `Maj + A > Displacement > Normal Map` vers *Normal*.

**Ils font, guidé (5 min),** d'après « Recette · Un lot PBR sur le socle » : les étapes 1 à 4.

**Ils font, seuls (1 min) :** *Pack Resources*, une fois pour toutes les images, puis enregistrer. Le béton ou le palissandre se posent pendant l'atelier ou après la séance.

**Quiz (1 min) :** le nœud entre la carte de normales et *Normal*.

**Point de contrôle :** le socle porte le veinage du noyer, net et sans raccord ; `Structure_Vert` reste dans la liste, son bouclier activé.

**Points d'observation :**
- Le socle devient bleu violet : la carte de normales est reliée à *Base Color*.
- Des creux en bosse : la carte `nor_dx` au lieu de `nor_gl`.
- Un bois délavé : `diff` en *Non-Color* ; un socle trop brillant ou trop mat : `rough` en *sRGB*.
- Une carte décalée : son entrée *Vector* n'est pas reliée au *Mapping*, car `Maj + D` ne copie pas ce lien.
- Le bouclier oublié : `Structure_Vert` disparaît à la réouverture du fichier.

### Quiz de la section 2

1. « Pourquoi relier la sortie Object du nœud Texture Coordinate ? » Pour que le motif garde la même taille sur toute la pièce, quelle que soit sa forme ; leurres : pour déplier les UV, pour accélérer l'affichage, pour colorer la texture.
2. « Le grain paraît étiré sur une seule pièce. Quelle est la cause la plus probable ? » Une échelle non appliquée ; leurres : un *Blend* trop faible, une image en *sRGB*, une *Roughness* trop forte.
3. « Quel nœud se place entre la carte de normales d'un lot PBR et l'entrée Normal du Principled ? » *Normal Map* ; leurres : *Bump*, *Mapping*, *Displacement*. Ce quiz remplace le 25 novembre 2026 celui du *Bump*, qui écartait à tort *Normal Map* « faute de dépliage UV ».

### Défi fil rouge de la section 2 (encart CAUTION)

Donnez à la lampe ses finitions : aluminium brossé dans l'axe des bras, grain fin sur l'interrupteur et la grille, socle en lot PBR, sans raccord. Gardez la peinture structurée par son bouclier, puis empaquetez les images.

## Section 3 · Bibliothèque d'actifs (Asset Browser)

Ancre `ch3_sec3_title` · 32 minutes, de 2:50 à 3:22

**Prérequis déjà vus :** les matières des sections 1 et 2 ; la liste des matières et le compteur d'utilisateurs (section 1) ; le sélecteur de type d'éditeur, l'Outliner (Basics 101) ; la barre latérale `N` (initiation) ; Append et Link cités en une phrase, la fenêtre d'ouverture de fichiers (initiation, demi-journée 1) ; *Pack Resources*.

**Ce que la section apporte :** l'actif et le catalogue ; l'Asset Browser et sa bibliothèque *Current File* ; le glisser-déposer d'une vignette sur une pièce ; *File > Append*, enfin mis en pratique. Link reste cité en une phrase, comme à l'initiation : sa manipulation devient un défi ★. La bibliothèque déclarée dans les préférences reste une option : le parcours principal ne modifie pas les préférences des postes.

### Notions prévues dans l'application

| Sous-titre prévu | Contenu | Figures |
|---|---|---|
| Pourquoi une bibliothèque | Une gamme CMF partagée par l'équipe : on réutilise au lieu de recréer | |
| Faire d'une matière un actif | Clic droit sur le nom de la matière, *Mark as Asset* ; ou l'Outliner, en mode *Blender File*. La vignette se crée seule. | 3.31 |
| L'Asset Browser | Le sélecteur de type d'éditeur ; la bibliothèque *Current File* | 3.32, 3.33 |
| Ranger en catalogues | Le bouton `+`, le renommage, le glisser-déposer des vignettes. Les catalogues s'enregistrent dans un fichier `blender_assets.cats.txt`, à côté du `.blend` : il voyage avec lui. | 3.34 |
| Décrire un actif | La barre latérale (`N`) : description, auteur, étiquettes (*Tags*), aperçu | 3.35 |
| Appliquer un actif par glisser-déposer | Une vignette de *Current File* déposée sur une pièce : le même résultat que la liste des matières, en un geste | 3.38 |
| Récupérer une matière : File > Append | Un fichier `.blend` s'ouvre comme un dossier : *Collection*, *Material*, *Object*… La matière arrive modifiable, avec ses images ; elle garde son statut d'actif. | 3.40, 3.41 |
| Link, en une phrase (encart NOTE) | « Link lie la matière en lecture seule ; on l'utilise pour partager une bibliothèque d'équipe. » *Pack*, nouveau dans Blender 5, se cite de même : il lie, puis empaquette. Manipulation : défi ★. | 3.42 |
| Option : déclarer une bibliothèque | *Edit > Preferences > File Paths > Asset Libraries*, bouton `+` ; la bibliothèque apparaît dans le sélecteur de l'Asset Browser ; le menu *Import Method* | 3.36, 3.37, 3.39 |

**Exemples multisectoriels à citer :** la gamme de teintes d'un constructeur automobile, la charte des intérieurs d'une compagnie aérienne, les matières homologuées d'un aménagement ferroviaire.

### 2:54 · Ranger ses matières en actifs (18 min)

**Nouveau :** l'actif et le catalogue, puis le glisser-déposer d'une vignette. **Déjà vu :** le sélecteur de type d'éditeur, la barre latérale, la liste des matières.

**Vous montrez (7 min),** sur la lampe :
- Clic droit sur le nom de la matière `Alu_Brosse`, *Mark as Asset* : une vignette se calcule.
- La Timeline changée en *Asset Browser* avec le sélecteur de type d'éditeur. La bibliothèque *Current File* : les actifs du fichier ouvert.
- Un catalogue *Métaux* avec le bouton `+`, puis la vignette de l'aluminium glissée dessus.
- La barre latérale (`N`) : une description, par exemple « Aluminium brossé. Bras de lampe ; convient aussi à une main courante ou à une jante. »
- La douille est encore nue. Glissez sur elle la vignette de `Chrome` : elle prend la matière en un geste, comme avec la liste des matières. « Un essai : la douille recevra mieux tout à l'heure. »
- Enregistrer. Les catalogues partent dans un fichier `blender_assets.cats.txt`, posé à côté du `.blend` : « Copiez toujours les deux ensemble. »

**Ils font, guidé (7 min) :**
1. marquer comme actifs `Alu_Brosse`, `Chrome` et `Peinture_Vert` ;
2. créer trois catalogues : *Métaux*, *Plastiques et peintures*, *Verres* ;
3. ranger ces trois actifs dans leur catalogue ;
4. glisser la vignette de `Chrome` sur la douille.

**Ils font, en autonomie (4 min) :**
- marquer et ranger seuls les autres matières, jusqu'à la dernière : `ABS_Noir`, `PVC_Mat_Noir`, `Verre_Clair`, et la matière du socle (`Bois_Noyer`…) dans un quatrième catalogue, *Bois et minéraux* ;
- enregistrer. Décrire un actif devient un défi ★.

**Point de contrôle :** dans l'Asset Browser, bibliothèque *Current File*, chaque matière de la lampe est rangée dans un catalogue ; *Métaux* montre l'aluminium brossé et le chrome. La douille est chromée.

**Points d'observation :**
- *Mark as Asset* lancé depuis le menu *Object* marque la pièce, pas sa matière. `Ctrl + Z`.
- Une vignette noire : relancez *Generate Preview* dans la barre latérale.
- La vignette lâchée à côté de la pièce ne fait rien : il faut relâcher le bouton avec le pointeur sur la pièce.
- Les catalogues ont disparu après une copie du fichier : le `blender_assets.cats.txt` est resté dans l'ancien dossier (vérifié dans Blender 5.2.1). Les actifs, eux, sont toujours là.

### 3:12 · Réutiliser : récupérer une matière par Append (12 min)

**Nouveau :** *File > Append*, mis en pratique ; Link, cité en une phrase. **Déjà vu :** Append et Link cités à l'initiation, la fenêtre d'ouverture de fichiers, l'actif et le glisser-déposer.

**Vous montrez (5 min) :**
- Le nuancier, ouvert sur votre poste avant la séquence : « La gamme CMF de la classe. » Revenez à la lampe par *File > Open Recent*.
- *File > Append*, dossier `PRC02_bibliotheque_CMF`, puis double-clic sur `PRC02_ch3_nuancier_cmf.blend` : le fichier s'ouvre comme un dossier, avec *Collection*, *Material*, *Object*… Dossier *Material*, `Alu_Naturel`, bouton *Append*.
- La matière est dans la liste des matières, modifiable. Elle garde son statut d'actif : sa vignette apparaît dans *Current File* (vérifié dans Blender 5.2.1). Glissez-la sur la douille : elle remplace l'essai en chrome.
- Link, en une phrase : « Link lie la matière en lecture seule ; on l'utilise pour partager une bibliothèque d'équipe. » Le fichier qui part au chapitre 4 n'en contient aucune.
- Le chapitre 4 reprendra *File > Append* pour amener la lampe dans son studio.
- Option (1 min) : sur votre poste, la bibliothèque déclarée dans les préférences apparaît dans le sélecteur de l'Asset Browser, et ses vignettes se glissent directement sur une pièce. Le menu *Import Method* s'ouvre, et *Pack*, nouveau dans Blender 5, se cite en une phrase : il lie, puis empaquette. « C'est l'usage d'une équipe. Aujourd'hui, nous ne touchons pas aux préférences des postes. »

**Ils font, guidé (7 min) :**
1. *File > Append*, le nuancier, dossier *Material*, `Alu_Naturel` ;
2. glisser sa vignette sur la douille, ou la choisir dans la liste des matières ;
3. ranger l'actif dans *Métaux* ;
4. enregistrer.

**Point de contrôle :** la douille porte `Alu_Naturel`, et ses réglages ne sont pas grisés. Aucune matière liée ne reste dans le fichier.

**Points d'observation :**
- Pas de dossier *Material* : l'apprenant est resté dans le dossier `PRC02_bibliotheque_CMF`. Double-clic sur le fichier `.blend`.
- La matière s'appelle `Alu_Naturel.001` : l'aluminium des bras n'a pas été renommé `Alu_Brosse` en section 2. Renommez les deux.
- Des réglages grisés : la matière a été liée par *File > Link*. `Ctrl + Z`, puis *File > Append*.

### Quiz de la section 3

1. « Vous voulez récupérer une matière d'un autre fichier, sans toucher aux préférences de Blender. Quel chemin suivez-vous ? » *File > Append*, puis le dossier *Material* du fichier ; leurres : *File > Open*, *File > Import*, *Edit > Preferences > File Paths*.
2. « Que fait Link, par rapport à Append ? » Il lie la matière en lecture seule, sans la copier ; leurres : il copie la matière et ses images, il marque la matière comme actif, il empaquette le fichier source.
3. Option : « Où retrouver les actifs du fichier ouvert dans l'Asset Browser ? » La bibliothèque *Current File* ; leurres : *Essentials*, *User Library*, le menu *File > Recover*.

### Défi fil rouge de la section 3 (encart CAUTION)

Faites des matières de votre lampe des actifs, rangés en catalogues et décrits. Habillez ensuite la douille avec une matière du nuancier, récupérée par *File > Append*.

## Atelier · Le second coloris · 3:24 (20 min)

**Situation :** « La revue de design demande une seconde proposition de couleurs, le coloris B. »

**Objectif :** décliner la lampe dans un second coloris, sans toucher au premier.

**Gestes :** aucun nouveau. *Duplicate Collection* (chapitre 1) ; le compteur d'utilisateurs pour rendre une matière indépendante (initiation, section 2) ; *Base Color*, *Metallic*, *Roughness*, *Coat* et le verre (section 1) ; *Mark as Asset*, les catalogues, le glisser-déposer et *File > Append* (section 3) ; l'enregistrement avec le bouton `+` (initiation).

**Déroulé :**
1. **Lancement (2 min).** « Dupliquez la collection *Lampe*, renommez la copie `Lampe_coloris_B` et décalez-la de 750 mm sur X (`G X = 750mm`) : avec moins, le câble de la copie traverserait le socle de l'original. Attention : la copie partage les matières de l'original. » Si un apprenant manque d'idée, proposez le coloris B du corrigé : une version claire pour un bureau d'études, avec structure et laque blanches, bras anodisés noirs, articulations en laiton et verre dépoli.
2. **Autonomie (16 min).** Chacun compose son coloris B sur la copie, pièce par pièce. La collection *Lampe* garde le coloris A et son nom : le chapitre 4 l'importe sous ce nom. Passez voir chaque poste au moins une fois.
3. **Revue (2 min).** Chacun change une teinte du coloris B, vérifie que le coloris A ne bouge pas, puis enregistre sous `lampe_habillage_v002.blend` avec le bouton `+`.

**Paliers :**
- **Socle :** le coloris B change au moins quatre matières, dont une peinture et un métal. Chaque matière changée est rendue indépendante, puis renommée (`Laque_Blanche`…). Le coloris A ne bouge pas. Pour le socle : `Structure_Vert`, gardée par son bouclier, copiée en `Structure_Blanche`, ou un autre lot PBR.
- **★ :** toutes les pièces du coloris B suivent une gamme cohérente. Ses nouvelles matières sont des actifs, rangés dans les catalogues. Une matière au moins vient du nuancier par *File > Append*, par exemple `Laiton`.
- **★★ :** un coloris C « premium » : laiton, carbone en projection triplanaire, verre fumé.

**Point de contrôle :** deux lampes côte à côte. Changer une teinte du coloris B ne change rien au coloris A.

**Points d'observation :**
- Les deux lampes changent ensemble : la matière est encore partagée. Un clic sur le compteur la rend indépendante. *Duplicate Collection* copie les objets et les maillages, mais pas les matières (vérifié dans Blender 5.2.1).
- Une copie garde ses nœuds : l'aluminium brossé rendu indépendant, puis teinté en noir, reste brossé. Faites-le remarquer, c'est la section 2 réinvestie.
- Un verre créé avec *New*, au lieu d'une copie de `Verre_Clair`, ne montre que l'image d'environnement : il faut recocher *Raytraced Transmission* et *Thin Wall*.

## Tour des postes, bilan et passerelle · 3:44 (6 min)

- **Tour des postes (2 min) :** les écrans en *Material Preview*, les deux coloris côte à côte, chaque socle avec son lot.
- **Une question (1 min) :** « Pourquoi l'ampoule ne montrait-elle que l'image d'environnement ? »
- **Quiz (1 min) :** *Link* face à *Append*, puis « Append ou Link, pour envoyer votre fichier à un client ? »
- **Passerelle (2 min) :** « Au chapitre 4, la lampe sort de la vue de travail. Vous l'amènerez dans un studio par Append, vous l'éclairerez, vous la cadrerez et vous en tirerez des visuels. » Vérifiez que chacun a enregistré `lampe_habillage_v002.blend`, images empaquetées.
- **Pour aller plus loin :** les quiz du chapitre 3 dans l'application et les défis ci-dessous.

## Le fil rouge

### La lampe au début du chapitre

Le chapitre part de `lampe_modele_v001.blend`, le fichier de fin du chapitre 2. D'après le plan validé du chapitre 2, il contient :
- la collection *Lampe*, en millimètres, avec le moteur EEVEE, sans matière ni lumière ;
- des pièces séparées et nommées : *Socle*, *Grille_aeration* (couronne de lamelles sur le socle, avec son *Empty*), *Interrupteur* (molette crantée, avec son *Empty*), *Articulation_bas*, *_milieu* et *_haut*, *Bras_bas* et *Bras_haut* (deux tiges chacun, par Mirror), *Tête* (coque en Solidify), *Douille* (pièce séparée, au fond de la tête), *Ampoule* (courbe et Screw, volume plein), *Câble* (courbe) ;
- des échelles appliquées et des modificateurs actifs, non appliqués : les matières se posent sans les appliquer ;
- *Shade Auto Smooth* sur le socle et la tête.

Le check-up de l'ouverture complète ce dernier point sur les bras et les articulations, si besoin (voir « Coordination »).

### Le cahier CMF de la lampe

Valeurs et teintes indicatives : l'apprenant compose sa propre gamme. Le détail des réglages est dans le tableau des matières (fiche B).

| Pièce | Coloris A, collection *Lampe* | Séquence | Coloris B du corrigé |
|---|---|---|---|
| *Socle* | `Structure_Vert` : peinture structurée, même teinte que la tête, gardée par son bouclier ; puis un lot PBR, au choix : `Bois_Noyer` (recette), `Beton_Lisse` ou `Palissandre_Verni` | Une matière ; triplanaire ; lot PBR | `Structure_Blanche` |
| *Tête* | `Peinture_Vert` : laque (*Coat*) | Une matière ; *Coat* | `Laque_Blanche` |
| *Grille_aeration*, *Interrupteur* | `ABS_Noir`, grainé | Une matière ; procédural | `ABS_Noir` |
| *Bras_bas*, *Bras_haut* | `Alu_Brosse` | Métal ; procédural | `Alu_Anodise_Noir` brossé |
| *Articulation_bas*, *_milieu*, *_haut* | `Chrome` | Métal | `Laiton` |
| *Câble* | `PVC_Mat_Noir` | Métal et plastique | `PVC_Mat_Noir` |
| *Ampoule* | `Verre_Clair`, *Thin Wall* | Le verre | `Verre_Depoli` |
| *Douille* (pièce séparée au chapitre 2) | `Alu_Naturel`, récupéré du nuancier par *File > Append* | Section 3 : essai en `Chrome` par glisser-déposer, puis Append | `Laiton` |
| Intérieur de la tête (option) | Blanc mat, par *Material Offset* du Solidify | Défi | |

L'ampoule n'éclaire pas dans ce chapitre. La lumière de la lampe appartient au chapitre 4 ; l'émission de la matière y est un palier ★★.

### Ce que l'apprenant a en main en fin de chapitre

Le fichier `lampe_habillage_v002.blend`, point de départ du chapitre 4 :
- la collection *Lampe*, habillée dans le coloris A, et la collection `Lampe_coloris_B` ;
- des matières nommées, marquées comme actifs et rangées en catalogues ; le fichier `blender_assets.cats.txt`, à côté du `.blend`, garde ces catalogues ;
- des images de finition et les cartes du lot PBR empaquetées, aucune matière liée : le fichier s'ouvre seul, et un Append de la collection *Lampe* emporte ses matières ;
- un verre dont la matière a *Raytraced Transmission* et *Thin Wall* cochées ;
- EEVEE comme moteur, avec la case *Raytracing* cochée ;
- aucune lumière ni caméra réglée : c'est le travail du chapitre 4.

Il garde aussi pour la suite ses propres actifs, réutilisables dans un autre projet par *File > Append*, et la bibliothèque CMF déclarée dans ses préférences, s'il a relevé ce défi.

Le fichier `PRC02_ch3_lampe_habillage.blend` montre cet état attendu (fiche A2), avec un socle en peinture structurée : il précède le lot PBR et reste un exemple.

## Fichiers d'exercice

La session principale construit ces fichiers avec le MCP Blender, d'après les fiches ci-dessous. Ce plan n'en crée aucun.

### Où trouver le corrigé, exercice par exercice

La convention est commune aux chapitres 2 à 4. Le corrigé de chaque exercice et de l'atelier se trouve dans le fichier de travail, dans une collection masquée (œil fermé) dont le nom commence par « Corrigé ». Le LISEZ-MOI indique en une ligne où le trouver. Un fichier séparé n'existe que s'il est justifié.

| Exercice ou atelier | Moment du minutage | Fichier de travail | Où se trouve le corrigé |
|---|---|---|---|
| Check-up du modèle | 0:00 à 0:15 | `lampe_modele_v001.blend`, enregistré sous `lampe_habillage_v001.blend` ; secours : `PRC02_ch3_lampe_a_habiller.blend` | Pas de corrigé : la collection *Lampe* du fichier de secours est le modèle vérifié |
| Habillage en coloris A : matières, métal, plastique, verre | 0:15 à 1:35 | `lampe_habillage_v001.blend` | Collection masquée *Corrigé coloris A* de `PRC02_ch3_lampe_a_habiller.blend` : chaque matière y est réglée |
| Démo « Métal et plastique » | 0:35 | `PRC02_ch3_nuancier_cmf.blend` | Sans objet : le nuancier est un fichier de référence, complet dès le départ |
| Shader Editor et finitions procédurales | 1:35 à 2:15 | `lampe_habillage_v001.blend` | *Corrigé coloris A* : les bras en `Alu_Brosse_corrige`, l'interrupteur et la grille en `ABS_Noir_corrige`, avec leurs chaînes de nœuds |
| Projection triplanaire sur le socle | 2:11 à 2:32 | `lampe_habillage_v001.blend` | *Corrigé coloris A* : le socle en `Structure_Vert_corrige` |
| Projection triplanaire : démo et défi ★★ | 2:11 ; défis | `PRC02_ch3_finitions_triplanaires.blend` | Collection masquée *Corrigé* du même fichier |
| Lot de textures PBR sur le socle | 2:32 à 2:44 | `lampe_habillage_v001.blend` ; cartes : `PRC02_ch3_textures_pbr.zip` | Collection masquée *Corrigé socle PBR* de `PRC02_ch3_lampe_a_habiller.blend` : *Socle_PBR* en `Bois_Noyer_corrige`, devant la lampe du coloris A |
| Rangement en actifs | 2:54 à 3:12 | `lampe_habillage_v001.blend` | La bibliothèque elle-même, `PRC02_bibliotheque_CMF/` : actifs, catalogues, descriptions et étiquettes, dans la forme attendue |
| Récupérer une matière par Append | 3:12 à 3:24 | `lampe_habillage_v001.blend` ; source : `PRC02_ch3_nuancier_cmf.blend` | *Corrigé coloris A* : la douille en `Alu_Naturel_corrige` |
| Atelier · Le second coloris | 3:24 à 3:44 | `lampe_habillage_v001.blend`, enregistré sous `lampe_habillage_v002.blend` | Collection masquée *Corrigé coloris B* de `PRC02_ch3_lampe_a_habiller.blend` |
| Fin du chapitre | 3:50 | `lampe_habillage_v002.blend` | Fichier séparé `PRC02_ch3_lampe_habillage.blend` (fiche A2), justifié ci-dessous |

**Un seul fichier séparé : `PRC02_ch3_lampe_habillage.blend`.** Il est justifié deux fois :
- il sert de point de départ au chapitre suivant : c'est l'état attendu de `lampe_habillage_v002.blend`, avec les collections *Lampe* et `Lampe_coloris_B` sous leurs vrais noms. Le chapitre 4 en tire son fichier de secours `PRC02_ch4_lampe_en_studio.blend`, par le même Append que les apprenants. C'est le rôle que joue `PRC02_ch2_lampe_modele.blend` pour le chapitre 3 ;
- une partie du résultat ne tient pas dans une collection : la case *Raytracing* de la scène, et les catalogues de la lampe.

**Les apprenants qui gardent leur propre lampe,** soit le parcours principal, n'ont pas le corrigé dans leur fichier. Ils le voient sur l'écran du formateur à chaque point de contrôle, ou dans `PRC02_ch3_lampe_a_habiller.blend` ouvert dans une seconde fenêtre de Blender.

### Les fiches de construction

| Fiche | Fichier | Moment du minutage |
|---|---|---|
| A | `PRC02_ch3_lampe_a_habiller.blend` | Ouverture (fichier de secours) ; démos des sections 1 et 2 ; corrigés de la lampe |
| A2 | `PRC02_ch3_lampe_habillage.blend`, avec son `blender_assets.cats.txt` | Ouverture (le but du jour) ; fin du chapitre ; source du fichier de secours du chapitre 4 |
| B | `PRC02_bibliotheque_CMF/` : `PRC02_ch3_nuancier_cmf.blend` et `blender_assets.cats.txt` | Démo « Métal et plastique » ; section 3, dont le corrigé du rangement ; atelier ; défis |
| C | `PRC02_ch3_finitions_triplanaires.blend` | Démo « Projection triplanaire » ; défi ★★ |
| D | `textures_cmf/` : cinq images PNG | Séquence « Projection triplanaire » ; empaquetées dans A, A2, B et C |
| E | `textures_pbr/` : trois lots CC0 de Poly Haven, en 1K | Séquence « Un lot de textures PBR » ; le noyer empaqueté dans A (*Corrigé socle PBR*) |

Le mémo des matières imprimé (ancienne fiche E) est reporté : plus tard, hors de ce plan. La lettre E désigne depuis le 25 novembre 2026 les lots de textures PBR.

**Dans l'application, proposition :** quatre modules ressource. `PRC02_ch3_lampe_a_habiller.blend` en section 1 ; `PRC02_ch3_finitions_triplanaires.blend` et `textures_cmf.zip` en section 2 ; `PRC02_bibliotheque_CMF.zip` en section 3. La bibliothèque se distribue en zip, car le fichier de catalogues doit accompagner le `.blend`. Le fichier de la fiche A2 reste au formateur et à la session du chapitre 4 : s'il est distribué, c'est en zip avec son fichier de catalogues.

### Règles communes

- Blender 5.2 LTS. Construction par script en arrière-plan, puis retouche de l'interface dans une fenêtre courte, comme les fichiers de l'initiation (`tool/exercices_initiation/`). Scripts rejouables dans `tool/exercices_ch3/`.
- Unités : *Metric*, *Length* en *Millimeters*, *Unit Scale* 1,0. Toutes les dimensions ci-dessous sont en mètres ; les millimètres sont rappelés entre parenthèses.
- Moteur de rendu : EEVEE.
- Images empaquetées (*Pack Resources*), chemins relatifs, aucun chemin absolu (contrôle par décompression, comme pour le fichier du chapitre 1), aucun texte d'extension tierce, `save_version` à 0 pour éviter le `.blend1`.
- Un texte `LISEZ-MOI` dans un éditeur de texte en bas de l'écran, de 151 px de haut, retour à la ligne actif, comme les fichiers de l'initiation.
- Pièces de démonstration sans dépliage UV : supprimer les couches UV créées avec les primitives.
- Corrigés : une collection masquée (œil fermé) dont le nom commence par « Corrigé ». Ses objets **et ses matières** portent le suffixe `_corrige`, comme les objets des corrigés du chapitre 2 : un apprenant qui crée `Peinture_Vert` dans le fichier de secours n'obtient pas `Peinture_Vert.001`, et ne modifie pas le corrigé par erreur. Les matières des corrigés ne sont pas marquées comme actifs : la bibliothèque *Current File* reste vide au début de la section 3.
- Catalogues : un fichier ordinaire enregistre ses catalogues dans un fichier `blender_assets.cats.txt` posé à côté de lui, pas dans le `.blend` (vérifié dans Blender 5.2.1). Les fichiers qui contiennent des actifs rangés (A2, B) se livrent donc dans un dossier, ou un zip, avec ce fichier. La fiche A n'en a pas besoin.

### Fiche A · `PRC02_ch3_lampe_a_habiller.blend`

**Rôle :** le fichier de départ propre, avec la lampe remodelée, pour commencer sans le travail du chapitre 2. Il sert aussi aux démos du formateur et porte les corrigés de la lampe : coloris A pour les sections 1 à 3, coloris B pour l'atelier.

**Source :** la collection *Lampe* de `PRC02_ch2_lampe_modele.blend`, le corrigé du chapitre 2, reprise telle quelle par Append (modificateurs actifs, noms, *Empty*). Ce fichier se construit donc après celui du chapitre 2.

**État de départ de la scène :**
- Collection *Lampe*, visible, sans aucune matière (aucun emplacement). Cotes du corrigé du chapitre 2, rappelées à titre indicatif :

| Objet | Dimensions indicatives | Modificateurs |
|---|---|---|
| *Socle* | Ø 0,180 × 0,025 m (180 × 25 mm) | Bevel, Smooth by Angle |
| *Grille_aeration* et son *Empty* | 36 lamelles de 0,012 × 0,002 × 0,002 m sur le dessus du socle | Array (*Object Offset*) |
| *Interrupteur* et son *Empty* | Ø 0,016 × 0,006 m, 24 crans | Array (*Object Offset*) |
| *Articulation_bas*, *_milieu*, *_haut* | Ø 0,030, 0,028 et 0,024 m, cylindres couchés sur Y | Bevel |
| *Bras_bas* | Deux tiges Ø 0,008 × 0,260 m | Mirror (Y) |
| *Bras_haut* | Deux tiges Ø 0,007 × 0,220 m | Mirror (Y) |
| *Tête* | Ø 0,120 × 0,110 m, coque de 0,0015 m | Solidify, Bevel, Smooth by Angle |
| *Douille* | Ø 0,030 × 0,020 m, au fond de la tête | Bevel, Smooth by Angle |
| *Ampoule* | Ø 0,050 × 0,085 m environ | Screw (sur une courbe) |
| *Câble* | Ø 0,005 m (*Bevel Depth* 0,0025) | Aucun (courbe) |

  Hauteur totale : 0,450 m environ.
- À ajouter si le corrigé du chapitre 2 ne l'a pas : *Shade Auto Smooth* sur *Bras_bas*, *Bras_haut*, les trois articulations et l'interrupteur. La rotation des bras n'est pas appliquée : leur axe Z local suit la tige, ce que le brossé utilise.
- Collection *Corrigé coloris A*, masquée (œil fermé) : une copie de la lampe décalée de X + 0,75 m, objets suffixés `_A`, avec les matières du coloris A (cahier CMF ci-dessus), toutes suffixées `_corrige` : `Peinture_Vert_corrige`, `Structure_Vert_corrige`, `ABS_Noir_corrige`, `Alu_Brosse_corrige`, `Chrome_corrige`, `PVC_Mat_Noir_corrige`, `Verre_Clair_corrige`, `Alu_Naturel_corrige`. Valeurs et chaînes de nœuds : celles de la fiche A2. C'est le résultat attendu des sections 1 à 3 sur la lampe. Les matières ne sont pas marquées comme actifs : le corrigé du rangement est la bibliothèque (fiche B).
- Collection *Corrigé coloris B*, masquée : une copie décalée de X + 1,50 m, soit 0,75 m de plus que le coloris A, comme dans la consigne de l'atelier, objets suffixés `_B`, avec les matières du coloris B, suffixées `_corrige` elles aussi. `ABS_Noir_corrige` et `PVC_Mat_Noir_corrige` restent partagées avec le coloris A, comme dans le résultat attendu. C'est le corrigé de l'atelier.
- Image empaquetée : `grain_structure.png` (fiche D).
- Scène : EEVEE, *Raytracing* **décoché**, comme dans les fichiers des apprenants : la démo du verre en a besoin. Le formateur la coche pendant la séquence.

**Vue d'ouverture :** espace *Layout* ; vue 3D en *Solid*, comme le fichier de fin du chapitre 2 ; perspective de trois quarts avant gauche, la lampe cadrée ; l'éditeur de propriétés sur l'onglet *Material* ; le LISEZ-MOI en bas.

**Texte du LISEZ-MOI :**

```
PRC02 · Chapitre 3 · Habiller la lampe
Enregistrez ce fichier sous lampe_habillage_v001.blend.
Corrigés : collections « Corrigé coloris A » (sections 1 à 3) et « Corrigé coloris B » (atelier), œil fermé dans l'Outliner.
Valeurs indicatives : composez votre propre gamme.

SECTION 1 · Les matières (onglet Material, vue Material Preview)
Socle
- Socle et tête : une peinture partagée. Interrupteur et grille : ABS noir partagé.
- Bras : aluminium, Metallic 1, Roughness 0,3. Articulations : chrome, Metallic 1, Roughness 0,03.
- Câble : PVC noir, Roughness 0,7.
- Ampoule : Transmission > Weight 1, Roughness 0, Thin Wall coché.
  Onglet Render > Raytracing ; onglet Material > Settings > Raytraced Transmission.
★  Coat > Weight 1 sur la peinture : une laque. Un verre dépoli : Roughness 0,4.
★★ Intérieur blanc de la tête : un second emplacement de matière, puis Solidify > Materials > Material Offset 1.

SECTION 2 · Les finitions (espace Shading)
Socle
- Bras brossés : Texture Coordinate (Object) > Mapping (Scale Z 0,02) > Noise Texture (Scale 1000)
  > Bump (Strength 0,15) > Normal du Principled.
- Socle : rendez sa matière indépendante (compteur), Coat 0, Roughness 0,6.
  Image Texture : textures_cmf/grain_structure.png, Non-Color, Box, Blend 0,25.
  Mapping Scale 50, Bump Strength 0,2.
- File > External Data > Pack Resources, puis enregistrez.
★  ABS grainé : Noise Scale 1500, Bump Strength 0,05.
★★ Articulations microbillées : Noise Scale 2000, Bump Strength 0,03, Roughness 0,5.

SECTION 3 · La bibliothèque
Socle
- Mark as Asset sur toutes vos matières ; catalogues Métaux, Plastiques et peintures, Verres.
- Glissez la vignette de Chrome sur la douille.
- File > Append > PRC02_bibliotheque_CMF > PRC02_ch3_nuancier_cmf.blend > Material > Alu_Naturel,
  puis glissez-la sur la douille.
- Gardez le fichier blender_assets.cats.txt à côté de votre fichier : il contient vos catalogues.
- Corrigé du rangement : la bibliothèque PRC02_bibliotheque_CMF elle-même.
★  Une description et des étiquettes pour chaque actif.
   File > Link d'une matière du nuancier : elle arrive grisée, en lecture seule. Puis Ctrl + Z.
★★ Edit > Preferences > File Paths > Asset Libraries > + : déclarez PRC02_bibliotheque_CMF,
   puis glissez une vignette de la bibliothèque sur une pièce.

ATELIER · Le coloris B
Socle
- Duplicate Collection sur Lampe ; renommez la copie Lampe_coloris_B ; G X = 750mm.
- Changez au moins quatre matières, dont une peinture et un métal :
  rendez-les d'abord indépendantes (compteur), puis renommez-les.
- Le coloris A ne doit pas bouger.
★  Une gamme complète, rangée en actifs ; une matière récupérée du nuancier par File > Append.
★★ Un coloris C premium : laiton, carbone, verre fumé.
Enregistrez sous lampe_habillage_v002.blend (bouton +).
```

**Corrigé attendu :** les collections *Corrigé coloris A* (sections 1 à 3) et *Corrigé coloris B* (atelier). Contrôles : chaque pièce a une matière nommée ; `Alu_Brosse_corrige` montre des rayures dans l'axe des tiges ; le socle n'a aucun raccord visible ; l'ampoule laisse voir le fond de la tête une fois *Raytracing* cochée.

**Les matières de la lampe,** dans les corrigés (suffixe `_corrige`) et dans la fiche A2 (sans suffixe) :

| Matière | Pièces | Réglages |
|---|---|---|
| `Peinture_Vert` | *Tête* | #2F5D3A, *Roughness* 0,4, *Coat* *Weight* 1, *Roughness* 0,03 |
| `Structure_Vert` | *Socle* | Copie de `Peinture_Vert` : *Coat Weight* 0, *Roughness* 0,6 ; `grain_structure.png` (*Non-Color*, *Box*, *Blend* 0,25), *Mapping* *Scale* 50, *Bump* *Strength* 0,2 |
| `ABS_Noir` | *Interrupteur*, *Grille_aeration* | #1A1A1A, *Roughness* 0,15 ; grain : *Texture Coordinate* (*Object*), *Noise* *Scale* 1500, *Bump* *Strength* 0,05, sans *Mapping* |
| `Alu_Brosse` | *Bras_bas*, *Bras_haut* | Chaîne du brossé de la fiche B |
| `Chrome` | Les trois articulations | Fiche B |
| `PVC_Mat_Noir` | *Câble* | Fiche B |
| `Verre_Clair` | *Ampoule* | *Transmission Weight* 1, *Roughness* 0, *Thin Wall*, *Raytraced Transmission* |
| `Alu_Naturel` | *Douille* | Copiée du nuancier (fiche B) |
| Coloris B : `Structure_Blanche`, `Laque_Blanche` (*Coat* 1), `Alu_Anodise_Noir` (copie de `Alu_Brosse`, #2A2A2C, brossé), `Laiton` (récupéré du nuancier) sur les articulations et la douille, `Verre_Depoli` (*Roughness* 0,4) | Les pièces du coloris B | `ABS_Noir` et `PVC_Mat_Noir` restent partagées avec le coloris A |

### Fiche A2 · `PRC02_ch3_lampe_habillage.blend` : la lampe habillée

**Rôle :** l'état attendu de `lampe_habillage_v002.blend`, sous les vrais noms. C'est le seul fichier séparé du chapitre, pour deux raisons :
- il sert de point de départ au chapitre 4 : la session du chapitre 4 en tire `PRC02_ch4_lampe_en_studio.blend`, par un Append de la collection *Lampe*, comme les apprenants. C'est le rôle de `PRC02_ch2_lampe_modele.blend` pour le chapitre 3 ;
- une partie du résultat ne tient pas dans une collection : la case *Raytracing* de la scène, et les catalogues.

Le formateur l'ouvre aussi à l'ouverture du chapitre, pour montrer le but du jour.

**Source :** le contenu des collections *Corrigé coloris A* et *B* de la fiche A, sans suffixes :
- collection *Lampe* : le coloris A, à l'origine, noms des pièces du chapitre 2 ;
- collection `Lampe_coloris_B` : le coloris B, décalé de X + 0,75 m comme dans la consigne de l'atelier, noms d'objets laissés tels que *Duplicate Collection* les donne (`Socle.001`…) ;
- matières du tableau ci-dessus, sans suffixe, toutes marquées comme actifs, vignettes générées ; catalogues *Métaux*, *Plastiques et peintures* et *Verres* ; description de `Alu_Brosse` ;
- EEVEE, case *Raytracing* cochée ; images empaquetées ; aucune matière liée.

**Livraison :** avec son `blender_assets.cats.txt`, dans un dossier ou un zip. Sans ce fichier, les actifs restent mais perdent leur rangement ; l'Append du chapitre 4 n'est pas touché.

**Vue d'ouverture :** espace *Layout* ; vue 3D en *Material Preview*, image *studio*, les deux lampes cadrées côte à côte, de trois quarts avant ; la Timeline remplacée par l'Asset Browser, bibliothèque *Current File*, catalogue *Métaux* ouvert ; un LISEZ-MOI de deux lignes :

```
PRC02 · Chapitre 3 · La lampe habillée
Le résultat attendu en fin de chapitre (lampe_habillage_v002.blend) : coloris A dans la collection Lampe, coloris B dans Lampe_coloris_B.
```

### Fiche B · `PRC02_bibliotheque_CMF/`

**Rôle :** le nuancier du formateur et la bibliothèque CMF de la classe. Le dossier contient `PRC02_ch3_nuancier_cmf.blend` et son fichier de catalogues `blender_assets.cats.txt`. Il se distribue en zip.

**État de départ de la scène :**
- Scène : EEVEE, *Raytracing* coché (les verres doivent se lire).
- Collection *Support* : un plan de 1,00 × 0,70 m à Z = 0, matière `Support_Gris` (gris moyen, *Roughness* 0,8), non marquée comme actif.
- Collection *Grille_Metallic_Roughness*, au fond du plan : 12 pastilles en deux rangées. Rangée avant : *Metallic* 0, gris moyen ; rangée arrière : *Metallic* 1, gris clair. Colonnes : *Roughness* 0, 0,1, 0,2, 0,4, 0,6 et 1. Matières `Grille_M0_R00` à `Grille_M1_R10`, non marquées comme actifs. Étiquettes en objets texte : « Metallic 0 », « Metallic 1 » en début de rangée, la valeur de *Roughness* au-dessus de chaque colonne. Cette grille sert à la figure 3.7.
- Collection *Nuancier* : une pastille par matière de la bibliothèque, une rangée par catalogue, l'étiquette du catalogue en début de rangée et le nom de la matière sous chaque pastille.
  - Pastille : une plaquette CMF de 0,050 × 0,080 × 0,004 m (50 × 80 × 4 mm), modificateur Bevel de 0,0015 m à 3 segments, *Shade Auto Smooth*, inclinée de 25° autour de X vers la vue.
  - Pour les verres, une bille de Ø 0,030 m devant la plaquette : la transmission se lit mieux sur un volume.
  - Pas de 0,070 m entre pastilles, de 0,120 m entre rangées.
  - Étiquettes : objets texte de 0,006 m de haut, matière `Etiquette` (gris très sombre, mate), non marquée comme actif.
- Images empaquetées : les cinq images de la fiche D.

**Les matières de la bibliothèque,** toutes marquées comme actifs, avec l'auteur « VIV Formation », la licence « CC0 1.0 », une vignette générée et les étiquettes indiquées. Couleurs en hexadécimal sRGB, comme dans le sélecteur de couleur de Blender.

| Catalogue | Matière | Base Color | Metallic | Roughness | Autres réglages | Étiquettes |
|---|---|---|---|---|---|---|
| Métaux | `Alu_Naturel` | #E6E7E8 | 1 | 0,3 | | aluminium, automobile, aéronautique |
| Métaux | `Alu_Brosse` | #E6E7E8 | 1 | 0,3 | Chaîne du brossé : *Mapping* Scale (1, 1, 0,02), *Noise* Scale 1000, Detail 4, *Bump* Strength 0,15 | aluminium, brossé, ferroviaire |
| Métaux | `Alu_Microbille` | #D9DADB | 1 | 0,5 | *Noise* Scale 2000, *Bump* Strength 0,03 | aluminium, microbillé |
| Métaux | `Alu_Anodise_Bronze` | #8C6A4A | 1 | 0,35 | | aluminium, anodisé |
| Métaux | `Alu_Anodise_Noir` | #2A2A2C | 1 | 0,35 | | aluminium, anodisé |
| Métaux | `Inox_Poli` | #C8C8C6 | 1 | 0,08 | | inox, ferroviaire |
| Métaux | `Chrome` | #C4C5C5 | 1 | 0,03 | | chrome, automobile |
| Métaux | `Laiton` | #E0C27A | 1 | 0,25 | | laiton |
| Métaux | `Titane_Satine` | #A9A49C | 1 | 0,4 | | titane, aéronautique |
| Plastiques | `ABS_Brillant_Noir` | #1A1A1A | 0 | 0,15 | | ABS, brillant |
| Plastiques | `ABS_Graine_Noir` | #1A1A1A | 0 | 0,45 | *Noise* Scale 1500, *Bump* Strength 0,05 | ABS, grainé, automobile |
| Plastiques | `PP_Mat_Gris` | #6E7072 | 0 | 0,6 | | polypropylène, mat |
| Plastiques | `PVC_Mat_Noir` | #161616 | 0 | 0,7 | | PVC, câble |
| Plastiques | `Caoutchouc_Noir` | #121212 | 0 | 0,85 | | caoutchouc, joint |
| Peintures | `Laque_Rouge` | #A3161A | 0 | 0,4 | *Coat* Weight 1, Roughness 0,03 | laque, automobile |
| Peintures | `Laque_Blanche` | #EDEDE8 | 0 | 0,4 | *Coat* Weight 1, Roughness 0,03 | laque, ferroviaire |
| Peintures | `Peinture_Structuree_Gris` | #4A4D50 | 0 | 0,6 | `grain_structure.png`, *Non-Color*, *Box*, *Blend* 0,25, *Mapping* Scale 50, *Bump* Strength 0,2 | structurée, ferroviaire |
| Peintures | `Peinture_Metallisee_Bleu` | #1C3F7A | 1 | 0,35 | Paillettes : *Voronoi Texture* Scale 3000 vers *Bump* (Strength 0,02) sur *Normal* seulement ; *Coat* Weight 1, Roughness 0,02 | métallisée, automobile |
| Verres | `Verre_Clair` | #FFFFFF | 0 | 0 | *Transmission* Weight 1, IOR 1,5, *Thin Wall* ; *Raytraced Transmission* | verre, vitrage |
| Verres | `Verre_Depoli` | #FFFFFF | 0 | 0,4 | Idem | verre, dépoli |
| Verres | `Verre_Fume` | #5A5A5A | 0 | 0,02 | Idem | verre, teinté, aéronautique |
| Verres | `Polycarbonate_Rouge` | #C0141A | 0 | 0,05 | *Transmission* Weight 1, IOR 1,58, sans *Thin Wall* ; *Raytraced Transmission* | polycarbonate, feu, automobile |
| Finitions texturées | `Cuir_Graine_Noir` | #1E1B19 | 0 | 0,55 | `grain_cuir.png`, *Non-Color*, *Box*, *Blend* 0,3, *Mapping* Scale 25, *Bump* Strength 0,3 | cuir, sellerie, aéronautique |
| Finitions texturées | `Carbone_Serge` | image | 0 | 0,25 | `carbone_serge_couleur.png` (*sRGB*) vers *Base Color* ; `carbone_serge_relief.png` (*Non-Color*) vers *Bump* (Strength 0,1) ; *Box*, *Blend* 0,2, *Mapping* Scale 62,5 ; *Coat* Weight 1, Roughness 0,02 | carbone, aéronautique, automobile |
| Finitions texturées | `Tole_Larmee` | #9A9C9E | 1 | 0,35 | `tole_larmee.png`, *Non-Color*, *Box*, *Blend* 0,1, *Mapping* Scale 8,33, *Bump* Strength 0,8 | tôle, marchepied, ferroviaire |

Chaque matière porte une description d'une phrase : son usage et ses secteurs. Exemple : « Aluminium brossé. Main courante, jante, bras de lampe. » Toutes les chaînes partent de *Texture Coordinate*, sortie *Object*. Les valeurs de *Scale* et de *Strength* ont été calées sur des pièces de la taille de la lampe, en *Material Preview* ; elles se retouchent à l'œil.

**Catalogues** (`blender_assets.cats.txt`, version 1, un UUID par ligne) : *Métaux*, *Plastiques*, *Peintures*, *Verres*, *Finitions texturées*.

**Vue d'ouverture :** espace *Layout* ; vue 3D en *Material Preview* avec l'image *studio*, vue de trois quarts plongeante sur le nuancier et la grille ; l'éditeur de propriétés sur l'onglet *Material* ; un LISEZ-MOI en bas :

```
PRC02 · Bibliothèque CMF
Pour récupérer une matière dans votre fichier : File > Append > PRC02_ch3_nuancier_cmf.blend > Material.
La matière arrive modifiable, avec ses images.
Option, pour parcourir cette gamme dans l'Asset Browser de tous vos fichiers :
Edit > Preferences > File Paths > Asset Libraries > + > choisissez le dossier PRC02_bibliotheque_CMF.
Toutes les valeurs sont indicatives. Les images sont créées par VIV Formation et libres de droits (CC0).
```

### Fiche C · `PRC02_ch3_finitions_triplanaires.blend`

**Rôle :** la démo de la projection triplanaire, sur des pièces des trois secteurs, et le défi ★★ des apprenants rapides.

**État de départ de la scène :**
- Scène : EEVEE, *Raytracing* coché.
- Collection *Pièces*, visible. Aucune pièce n'a de dépliage UV.

| Objet | Secteur | Forme et dimensions | Position | Matière de départ |
|---|---|---|---|---|
| *Accoudoir* | Aéronautique | Pavé de 0,300 × 0,060 × 0,050 m, Bevel 0,008 m à 4 segments, *Shade Auto Smooth*, échelle appliquée | (−0,35 ; 0 ; 0,025) | `Cuir_Graine_Noir`, à compléter |
| *Accoudoir_jumeau* | Aéronautique | Même aspect, mais construit en 0,150 × 0,060 × 0,050 m avec une échelle X de 2,0 **non appliquée** | (−0,35 ; 0,15 ; 0,025) | La même matière, partagée |
| *Coque_retroviseur* | Automobile | Demi-ellipsoïde de 0,220 × 0,120 × 0,140 m (une UV Sphere coupée en deux, échelle appliquée), Solidify 0,0025 m, *Shade Auto Smooth* | (0 ; 0 ; 0,07) | `Grainage_Retroviseur` (#1A1A1A, *Roughness* 0,45, image `grain_structure.png`), à compléter |
| *Marchepied* | Ferroviaire | Pavé de 0,600 × 0,300 × 0,020 m, Bevel 0,003 m | (0,45 ; 0 ; 0,01) | `Tole_Larmee`, à compléter |
| *Panneau_carbone* | Aéronautique, automobile | Plan de 0,300 × 0,200 m subdivisé, Simple Deform (*Bend*, 45°), Solidify 0,003 m | (0,45 ; 0,35 ; 0,05) | `Carbone_Serge`, à compléter |

- « À compléter » : la matière n'a que son Principled réglé (teinte, *Metallic*, *Roughness*) et un nœud *Image Texture* déjà chargé avec son image, non relié. La démo gagne ainsi le temps de chercher le fichier.
- Collection *Corrigé*, masquée : une copie de chaque pièce, suffixée `_corrige`, décalée de Y − 0,60 m. Chaque copie porte sa propre matière, suffixée `_corrige` elle aussi (`Cuir_Graine_Noir_corrige`…), avec la chaîne complète : valeurs de la fiche B ; pour la coque, celles du LISEZ-MOI ci-dessous (*Mapping* *Scale* 100, *Bump* *Strength* 0,1, *Blend* 0,3). La copie de l'accoudoir jumeau a son échelle appliquée. C'est le corrigé de la démo et du défi ★★.
- Images empaquetées : `grain_cuir.png`, `grain_structure.png`, `tole_larmee.png`, `carbone_serge_couleur.png`, `carbone_serge_relief.png`.

**Vue d'ouverture :** espace *Shading* ; *Accoudoir* sélectionné, sa matière visible dans le Shader Editor ; vue 3D en *Material Preview* avec l'image *studio*, de trois quarts, les cinq pièces cadrées ; le LISEZ-MOI en bas.

**Texte du LISEZ-MOI :**

```
PRC02 · Chapitre 3 · Finitions triplanaires (défi)
Aucune pièce n'a de dépliage UV. Corrigé : collection « Corrigé » (œil fermé).

Socle · L'accoudoir
- Texture Coordinate (Object) > Mapping (Scale 25) > Image Texture (grain_cuir) > Bump (Strength 0,3) > Normal.
- Image Texture : Non-Color, projection Box, Blend 0,3.
- L'accoudoir jumeau a un grain étiré : trouvez pourquoi, puis soignez-le.
★  La coque de rétroviseur
- Même chaîne avec grain_structure (Mapping Scale 100, Bump Strength 0,1).
- Réglez Blend jusqu'à ne plus voir de raccord sur les flancs courbes.
★★ Le marchepied et le panneau carbone
- Tôle larmée : relief marqué, Bump Strength 0,8, Mapping Scale 8,33.
- Carbone : deux images. La couleur (sRGB) va dans Base Color, le relief (Non-Color) dans Bump.
  Ajoutez un vernis : Coat Weight 1.
```

**Corrigé attendu :** la collection *Corrigé*. Contrôles : grain régulier sur les deux accoudoirs une fois l'échelle appliquée ; aucun raccord visible sur la coque à *Blend* 0,3 ; la tôle larmée montre des larmes en relief ; le carbone garde son motif tissé sur la courbure du panneau.

### Fiche D · `textures_cmf/`

**Rôle :** les images de finition des fiches A, A2, B et C, et le dossier ouvert par les apprenants en séquence « Projection triplanaire ».

**Règles :**
- Images créées par script, sans aucune source extérieure : elles sont libres de droits (CC0) par construction. Le script reste dans `tool/exercices_ch3/`.
- 1024 × 1024 px, PNG 8 bits.
- Raccordables sur les quatre bords : bruit filtré par transformée de Fourier, ou motif périodique. Contrôle : l'image répétée en 2 × 2 ne montre aucune couture.

| Fichier | Contenu | Espace colorimétrique | Taille d'une tuile | *Mapping Scale* |
|---|---|---|---|---|
| `grain_structure.png` | Relief de peinture structurée : des bosses douces, environ 25 par tuile, contraste moyen, en niveaux de gris | *Non-Color* | 0,020 m (20 mm) | 50 |
| `grain_cuir.png` | Grain de cuir : environ 40 cellules de Voronoi par tuile, creux sur les bords des cellules, plus un bruit fin | *Non-Color* | 0,040 m (40 mm) | 25 |
| `carbone_serge_couleur.png` | Sergé 2 × 2, 8 mèches par tuile, du noir au gris très sombre, reflet léger au centre de chaque mèche | *sRGB* | 0,016 m (16 mm) | 62,5 |
| `carbone_serge_relief.png` | Le même sergé en hauteur : mèches bombées, creux aux croisements | *Non-Color* | 0,016 m (16 mm) | 62,5 |
| `tole_larmee.png` | Tôle larmée : larmes en relief, alternées à + 45° et − 45°, 4 × 4 par tuile, fond plat noir, larmes blanches à bords doux | *Non-Color* | 0,120 m (120 mm) | 8,33 |

### Fiche E · `textures_pbr/` : les lots de textures PBR

**Rôle :** les cartes du lot PBR du socle (séquence de 2:32), distribuées dans `_resources/exercices/PRC02_ch3_textures_pbr.zip` (6,7 Mo), et le corrigé *Corrigé socle PBR* de la fiche A.

**Source :** trois lots CC0 de Poly Haven, téléchargés une fois le 25 novembre 2026, avec l'accord du formateur, en 1K et en JPG, depuis l'API publique ; empreintes MD5 contrôlées. Les cartes restent hors du dépôt, dans `tool/exercices_ch3/textures_pbr/` ; le script `tool/exercices_ch3/textures_pbr.py` écrit le zip, son LISEZ-MOI, et relit chaque fichier décompressé à la recherche de chemins absolus.

| Lot | Matière du chapitre | Taille réelle | *Mapping Scale* sur le socle | Cartes |
|---|---|---|---|---|
| `walnut_veneer_02` (noyer, recette) | `Bois_Noyer` | 1 m | 2 | `diff` *sRGB* ; `rough`, `nor_gl`, `disp` *Non-Color* |
| `granular_concrete` (béton lisse) | `Beton_Lisse` | 2,4 m | 4 | idem |
| `rosewood_veneer1` (palissandre verni) | `Palissandre_Verni` | 2,43 m | 3 | idem |

**La chaîne :** un seul *Texture Coordinate* (*Object*), un seul *Mapping*, trois *Image Texture* en *Box*, *Blend* 0,25 : `diff` → *Base Color* ; `rough` → *Roughness* ; `nor_gl` → *Normal Map* (*Strength* 1) → *Normal*. *Metallic* 0, sans *Coat*. Recette dans `tool/exercices_ch3/matieres.py` (`LOTS_PBR`, `pbr`).

**Contrôle :** rendu EEVEE du corrigé (`rendus_controle.py`, rendus `a_corrige_socle_pbr…`) ; la carte de normales donne bien un relief en projection *Box*, sans couche UV (comparaison avec *Strength* 0).

## Captures Blender à prévoir

Une capture pour chaque menu, bouton, panneau ou nœud cité : 54 figures, toutes produites. Les figures 3.31 à 3.37 (lot PBR du socle) datent du 25 novembre 2026 : les suivantes ont été renumérotées d'autant. La figure 3.54, la planche CMF, vient de `tool/exercices_cmf/`. Les légendes ci-dessous sont celles du texte. L'échelle est celle de l'affichage dans l'application (colonne de 715 px : une figure pleine largeur tient dans 715 × 450 px, une figure côte à côte dans 345 × 300 px). Toutes les figures qui montrent l'interface s'affichent à 0,5 au moins ; le script `tool/exercices_ch3/echelles.py` les recalcule. Les figures 3.3 et 3.13 portent les noms de fichier prévus par le plan du chapitre 4 : une seule capture sert aux deux chapitres.

| Figure | Fichier | Ce qu'elle montre | Format | Taille (px) | Échelle dans l'application |
|---|---|---|---|---|---|
| 3.1 | `lamp_cmf_target_blender.jpg` | Le but du chapitre : la lampe habillée en deux coloris, en Material Preview. À gauche, le coloris A (laque verte, aluminium brossé, chrome) ; à droite, le coloris B de l'atelier. | Pleine largeur | 828 × 356 | 0,86 |
| 3.2 | `material_preview_button_blender.jpg` | Les boutons de mode d'affichage, en haut à droite de la vue 3D (agrandis dans le médaillon) : Material Preview est actif. La lampe n'a pas encore de matière : elle reste blanche. | Côte à côte | 593 × 593 | 0,51 |
| 3.3 | `material_preview_popover_blender.jpg` | Le menu Viewport Shading en Material Preview : l'image d'environnement, sa rotation, World Opacity, et les cases Scene Lights et Scene World. | Côte à côte | 320 × 333 | 0,90 |
| 3.4 | `material_tab_new_blender.jpg` | L'onglet Material d'une pièce sans matière : la liste des emplacements, vide, et le bouton New. | Côte à côte | 542 × 190 | 0,64 |
| 3.5 | `material_tab_surface_blender.jpg` | La rubrique Surface d'une nouvelle matière : Principled BSDF, puis Base Color, Metallic, Roughness, IOR, Alpha, Thin Wall, Normal, et les rubriques repliées. | Côte à côte | 542 × 590 | 0,51 |
| 3.6 | `material_browse_list_blender.jpg` | La liste des matières existantes, ouverte à gauche du nom. Le chiffre 2 à droite du nom : deux pièces partagent Peinture_Vert. | Côte à côte | 540 × 342 | 0,64 |
| 3.7 | `link_materials_menu_blender.jpg` | Astuce : Ctrl + L dans la vue 3D ouvre le menu Link/Transfer Data ; Link Materials donne la matière de l'objet actif à toute la sélection. | Côte à côte | 501 × 544 | 0,55 |
| 3.8 | `metallic_roughness_grid_blender.jpg` | La grille du nuancier, en Material Preview. Rangée arrière : Metallic 1 ; rangée avant : Metallic 0. De gauche à droite : Roughness 0, 0,1, 0,2, 0,4, 0,6 et 1. | Pleine largeur | 920 × 213 | 0,78 |
| 3.9 | `principled_coat_panel_blender.jpg` | À gauche, la rubrique Coat dépliée sur Peinture_Vert : Weight 1, Roughness 0,03. À droite, la tête prend un reflet net de laque. | Pleine largeur | 1156 × 720 | 0,62 |
| 3.10 | `principled_transmission_blender.jpg` | La rubrique Transmission dépliée sur Verre_Clair : Weight 1. Roughness est à 0 et Thin Wall est coché. | Côte à côte | 542 × 598 | 0,50 |
| 3.11 | `glass_raytracing_comparison_blender.jpg` | L'ampoule vue par l'ouverture de la tête. À gauche, sans les deux cases : une boule sombre qui reflète l'environnement. Au milieu, avec les deux cases : le verre réfracte, comme une boule de cristal. À droite, avec Thin Wall en plus : une paroi fine, qui laisse voir la douille sans la déformer. | Pleine largeur | 1200 × 327 | 0,60 |
| 3.12 | `render_raytracing_checkbox_blender.jpg` | L'onglet Render : le moteur EEVEE et la case Raytracing, cochée. | Côte à côte | 542 × 590 | 0,51 |
| 3.13 | `material_settings_transmission_blender.jpg` | L'onglet Material, rubrique Settings : Render Method, la case Raytraced Transmission cochée, et Thickness. | Côte à côte | 542 × 390 | 0,64 |
| 3.14 | `principled_thin_wall_blender.jpg` | La case Thin Wall cochée, dans la rubrique Surface de Verre_Clair. | Côte à côte | 542 × 530 | 0,57 |
| 3.15 | `principled_emission_panel_blender.jpg` | Défi : la rubrique Emission dépliée, Color vert et Strength 6. En dessous, l'interrupteur devient un voyant. | Côte à côte | 528 × 353 | 0,65 |
| 3.16 | `material_slots_two_blender.jpg` | Option : deux emplacements de matière sur la tête, Peinture_Vert et Blanc_Interieur. L'intérieur de l'abat-jour devient blanc. | Pleine largeur | 1166 × 600 | 0,61 |
| 3.17 | `solidify_material_offset_blender.jpg` | Option : le modificateur Solidify de la tête, rubrique Materials : Material Offset à 1. | Côte à côte | 542 × 530 | 0,57 |
| 3.18 | `shading_workspace_blender.jpg` | L'espace de travail Shading : le navigateur de fichiers en haut à gauche (flouté ici), la vue 3D en Material Preview, le Shader Editor en bas, l'Outliner et l'éditeur de propriétés à droite. | Pleine largeur | 1200 × 720 | 0,60 |
| 3.19 | `principled_node_vs_tab_blender.jpg` | À gauche, la matière Alu_Naturel en nœuds : Principled BSDF relié à Material Output. À droite, l'onglet Material affiche les mêmes valeurs. | Pleine largeur | 1132 × 683 | 0,63 |
| 3.20 | `shader_editor_add_menu_blender.jpg` | Maj + A dans le Shader Editor : le menu Add, puis son sous-menu Texture, avec Noise Texture et Image Texture. | Côte à côte | 498 × 374 | 0,69 |
| 3.21 | `node_link_noise_base_color_blender.jpg` | Une Noise Texture reliée par sa sortie Color à l'entrée Base Color. À droite, la tige se couvre de nuages gris, étirés sur toute sa longueur. | Pleine largeur | 1150 × 723 | 0,62 |
| 3.22 | `texture_coordinate_node_blender.jpg` | Étape 1 : Texture Coordinate, sortie Object, reliée à l'entrée Vector du Noise (Scale 1000). À droite, le motif devient fin et régulier sur toute la tige. | Pleine largeur | 1200 × 558 | 0,60 |
| 3.23 | `noise_bump_chain_blender.jpg` | Étape 2 : la sortie Factor du Noise va dans Height du Bump, la sortie Normal du Bump va dans Normal du Principled. Strength est à 0,2. À droite, le motif devient un relief. | Pleine largeur | 1200 × 634 | 0,60 |
| 3.24 | `brushed_aluminium_blender.jpg` | Étape 3 : le nœud Mapping, Scale (1, 1, 0,02), entre Texture Coordinate et Noise ; Strength du Bump à 0,15. À droite, les rayures suivent la longueur de la tige. | Pleine largeur | 1196 × 560 | 0,60 |
| 3.25 | `image_texture_projection_menu_blender.jpg` | Le nœud Image Texture et son menu de projection : Flat, Box, Sphere, Tube. | Côte à côte | 262 × 254 | 1,18 |
| 3.26 | `image_texture_box_node_blender.jpg` | Le nœud Image Texture réglé : projection Box, Blend 0,3, Color Space Non-Color. | Côte à côte | 262 × 254 | 1,18 |
| 3.27 | `leather_chain_armrest_blender.jpg` | La chaîne du cuir grainé : Texture Coordinate (Object), Mapping (Scale 25), Image Texture en Box avec Blend 0,3 et Non-Color, Bump (Strength 0,3), dont la sortie va dans Normal du Principled. | Pleine largeur | 1050 × 539 | 0,68 |
| 3.28 | `box_blend_comparison_blender.jpg` | Une image contrastée (la tôle larmée) projetée en Box sur une coque de rétroviseur, au raccord de deux projections. À gauche, Blend 0 : les larmes sont coupées net. À droite, Blend 0,2 : la transition se fond. | Pleine largeur | 808 × 260 | 0,88 |
| 3.29 | `image_color_space_menu_blender.jpg` | Le menu Color Space du nœud Image Texture : Non-Color pour une image de relief, sRGB pour une image de couleur. | Côte à côte | 262 × 304 | 0,99 |
| 3.30 | `texture_scale_not_applied_blender.jpg` | Les deux accoudoirs du fichier de démonstration. À gauche, l'accoudoir du fond a une échelle X de 2 non appliquée : son grain s'étire en longueur. À droite, après Ctrl + A > Scale : les deux grains sont identiques. | Pleine largeur | 1200 × 380 | 0,60 |
| 3.31 | `shader_add_normal_map_blender.jpg` | Maj + A > Displacement, dans le Shader Editor : Normal Map, sous Bump et Displacement. | Côte à côte | 245 × 150 | 1,41 |
| 3.32 | `material_fake_user_shield_blender.jpg` | L'onglet Material du socle : le bouclier de Structure_Vert, activé (en bleu), puis le bouton de copie (New Material). | Côte à côte | 542 × 190 | 0,64 |
| 3.33 | `pbr_chain_overview_blender.jpg` | La chaîne du lot : Texture Coordinate (Object) et un seul Mapping (Scale 2), trois Image Texture en Box (Blend 0,25), puis Base Color, Roughness et, par le Normal Map, Normal. | Pleine largeur | 886 × 673 | 0,67 |
| 3.34 | `pbr_maps_closeup_blender.jpg` | Deux cartes du lot, en gros plan. À gauche, la couleur, en sRGB. À droite, les normales, en Non-Color, reliées au Normal Map. La rugosité se règle comme les normales. | Pleine largeur | 998 × 436 | 0,72 |
| 3.35 | `pbr_socle_lots_comparison_blender.jpg` | Le même socle, quatre finitions, en Material Preview : la peinture structurée, le noyer (Scale 2), le béton lisse (Scale 4) et le palissandre verni (Scale 3). | Pleine largeur | 762 × 168 | 0,94 |
| 3.36 | `preferences_node_wrangler_blender.jpg` | Option : Edit > Preferences > Add-ons, l'extension Node Wrangler, livrée avec Blender. | Côte à côte | 600 × 276 | 0,57 |
| 3.37 | `node_wrangler_principled_setup_blender.jpg` | Option : la chaîne créée par Ctrl + Maj + T avec les cartes diff, rough et nor_gl du noyer. Les images arrivent en projection Flat, et Texture Coordinate est relié par sa sortie UV (agrandie dans le médaillon). | Pleine largeur | 989 × 581 | 0,72 |
| 3.38 | `file_external_data_pack_blender.jpg` | File > External Data : Pack Resources range les images dans le fichier .blend. | Côte à côte | 280 × 293 | 1,02 |
| 3.39 | `cmf_swatch_library_blender.jpg` | Le nuancier de la bibliothèque CMF, en Material Preview : une rangée par catalogue (métaux, plastiques, peintures, verres, finitions texturées), et la grille Metallic / Roughness au fond. | Pleine largeur | 934 × 794 | 0,57 |
| 3.40 | `material_mark_as_asset_blender.jpg` | Le clic droit sur le nom de la matière, dans l'onglet Material : Mark as Asset. | Côte à côte | 594 × 242 | 0,58 |
| 3.41 | `asset_browser_editor_type_blender.jpg` | Le sélecteur de type d'éditeur, ouvert sur la zone du bas : Asset Browser se trouve dans la colonne Data. | Pleine largeur | 950 × 284 | 0,75 |
| 3.42 | `asset_browser_overview_blender.jpg` | L'Asset Browser, bibliothèque Current File : les catalogues à gauche, les vignettes du catalogue Métaux au centre, et la barre latérale de l'actif sélectionné à droite. | Pleine largeur | 1011 × 430 | 0,71 |
| 3.43 | `asset_catalog_new_blender.jpg` | La liste des catalogues : le bouton + pour en créer un, et les trois catalogues de la lampe. Unassigned regroupe les actifs sans catalogue. | Côte à côte | 298 × 195 | 1,16 |
| 3.44 | `asset_metadata_sidebar_blender.jpg` | La barre latérale de l'Asset Browser pour Alu_Brosse : Description, License, Author, et la vignette (Preview). | Côte à côte | 297 × 393 | 0,76 |
| 3.45 | `asset_drag_drop_material_blender.jpg` | La vignette Chrome, glissée de la bibliothèque Current File sur la douille. Blender affiche la pièce visée : « Drop Chrome on Douille ». | Pleine largeur | 1010 × 620 | 0,71 |
| 3.46 | `file_menu_link_append_blender.jpg` | Le menu File : Link… et Append…, juste au-dessus de Data Previews. | Côte à côte | 263 × 566 | 0,53 |
| 3.47 | `file_append_blend_folders_blender.jpg` | La fenêtre File > Append, à l'intérieur du fichier du nuancier : ses dossiers Collection, Material, Object… Le chemin du poste est flouté. | Pleine largeur | 1025 × 430 | 0,70 |
| 3.48 | `preferences_asset_libraries_blender.jpg` | Option : Edit > Preferences > Asset Libraries, la bibliothèque CMF ajoutée, avec son chemin (Path, flouté) et sa méthode d'import (Import Method : Pack). | Pleine largeur | 993 × 314 | 0,72 |
| 3.49 | `asset_library_selector_blender.jpg` | Option : le menu des bibliothèques de l'Asset Browser : All Libraries, Current File, Essentials, User Library et la bibliothèque CMF déclarée. | Côte à côte | 296 × 234 | 1,17 |
| 3.50 | `asset_import_method_menu_blender.jpg` | Option : Import Settings, dans l'en-tête de l'Asset Browser : Import Method propose Follow Asset or Preferences, Link, Append et Pack. | Côte à côte | 430 × 200 | 0,80 |
| 3.51 | `outliner_collection_menu_blender.jpg` | Le clic droit sur la collection Lampe, dans l'Outliner : Duplicate Collection. | Côte à côte | 317 × 277 | 1,08 |
| 3.52 | `lamp_two_colorways_blender.jpg` | L'atelier terminé : le coloris A dans la collection Lampe, le coloris B dans Lampe_coloris_B, décalé de 750 mm. | Pleine largeur | 752 × 288 | 0,95 |
| 3.53 | `linked_material_readonly_blender.jpg` | Défi : une matière liée par File > Link. Son nom porte l'icône de lien, et ses réglages sont grisés : elle se modifie dans son fichier source. | Côte à côte | 542 × 530 | 0,57 |

**Méthode :** celle du chapitre 1 (note de passation) : *Resolution Scale* à 1,25, onglets d'extensions tierces hors champ, chemins personnels floutés dans le navigateur de fichiers de l'espace *Shading*. Les vues en *Material Preview* se capturent dans une fenêtre Blender courte, lancée à part, en ouvrant un fichier `.blend` pour éviter l'écran d'accueil ; la comparaison 3.10 a déjà été prototypée ainsi.

## Si vous prenez du retard

Raccourcissez dans cet ordre :

| Ordre | Ce que l'on raccourcit | Gain |
|---|---|---|
| D'abord | *Coat* en démo seulement ; l'option de la bibliothèque déclarée ; la démo du téléchargement sur Poly Haven | 6 min |
| Ensuite | L'autonomie du procédural (grain de l'ABS) ; l'autonomie de la projection réduite à l'enregistrement ; le lot PBR réduit à la couleur et aux normales | 10 min |
| En dernier | L'atelier réduit à son palier Socle, en 10 minutes ; la suite après la séance, avec le LISEZ-MOI et la collection *Corrigé coloris B* | 10 min |

Un apprenant qui décroche reprend avec le groupe sur la pièce de l'exercice en cours : chaque exercice porte sur ses propres pièces (les bras, le socle, la douille). Il finit les pièces sautées après la séance, avec la collection *Corrigé coloris A*.

À ne jamais sauter : *Material Preview* et le Principled (*Metallic*, *Roughness*) ; le verre et ses deux interrupteurs ; le Shader Editor et la chaîne du brossé ; la projection *Box* sur le socle ; le lot PBR et son *Normal Map* ; *Mark as Asset* et *File > Append* ; l'enregistrement final, images empaquetées.

## Pour ceux qui avancent vite

**★**
- Le verre dépoli et le verre fumé.
- La description d'un actif.
- Un autre lot sur le socle, béton ou palissandre ; la carte `disp` dans un *Bump* chaîné au *Normal Map* ; un lot chargé par `Ctrl + Maj + T` de *Node Wrangler*, repassé en *Object* et en *Box*.
- L'intérieur blanc de la tête : un second emplacement de matière et *Material Offset* du Solidify.
- `Ctrl + L > Link Materials`, pour donner une matière à plusieurs pièces d'un coup.
- *Emission* : un voyant lumineux sur l'interrupteur.
- *File > Link* d'une matière du nuancier : elle arrive grisée, en lecture seule. Puis `Ctrl + Z`.
- La bibliothèque CMF déclarée dans ses préférences : glisser une vignette de la gamme sur une pièce, puis essayer le menu *Import Method* (*Append*, *Append (Reuse Data)*, *Link*, *Pack*).

**★★**
- **Automobile :** la peinture métallisée de la bibliothèque, décortiquée, puis reproduite.
- **Aéronautique :** l'accoudoir en cuir grainé et le panneau carbone, sur le fichier des finitions triplanaires.
- **Ferroviaire :** le marchepied en tôle larmée, puis la rangée de sièges de l'initiation (`PRC02_init_rangee_sieges.blend`) habillée avec la bibliothèque.
- **Marquage :** un logo projeté par un objet *Empty*, sans dépliage UV.
- **Sa propre bibliothèque :** déclarer son dossier de travail, puis habiller un objet dans un nouveau fichier.

## Coordination avec les chapitres 2 et 4

Les plans `PRC02-plan-chap2.md` et `PRC02-plan-chap4.md`, en attente de validation, ont été relus le 18 novembre 2026, ainsi que leurs notes de passation. Ce plan s'y aligne sur ces points :
- le fichier d'entrée `lampe_modele_v001.blend`, le corrigé `PRC02_ch2_lampe_modele.blend` et la liste des pièces ;
- le nom de sortie `lampe_habillage_v00N.blend`, que le plan du chapitre 2 supposait déjà, avant `lampe_rendu_v001.blend` au chapitre 4 ;
- la collection *Lampe*, que le chapitre 4 importe par *File > Append* : elle garde son nom et porte le coloris A ;
- les matières attendues par le chapitre 4 : métal brossé ou chromé pour les bras, plastique laqué pour la tête, verre pour l'ampoule ;
- les seules images d'environnement de *Material Preview* : le monde de la scène et les HDRI restent au chapitre 4 ;
- *File > Append* pratiqué au chapitre 3 sur une matière, réinvesti au chapitre 4 sur la collection *Lampe*, sans nouvelle explication ;
- Link cité en une phrase au chapitre 3, comme à l'initiation : le chapitre 4 ne doit pas supposer qu'il a été manipulé ;
- le fichier de secours du chapitre 4, `PRC02_ch4_lampe_en_studio.blend`, construit à partir de `PRC02_ch3_lampe_habillage.blend` (fiche A2) ;
- la convention des corrigés, commune aux chapitres 2 à 4 : une collection masquée dont le nom commence par « Corrigé », dans le fichier de travail ; objets suffixés `_corrige`, comme au chapitre 2, et ici matières aussi ;
- les noms gardés tels quels pour le chapitre 4 : `lampe_habillage_v002.blend`, les collections *Lampe* et `Lampe_coloris_B`, les noms des matières. Aucun n'a changé avec les décisions du 18 novembre.

### Incohérences et décisions

1. **La case Raytracing. Décidé le 18 novembre 2026.** Le chapitre 3 coche *Raytracing* et *Raytraced Transmission* pour le verre, avec une seule phrase : « Sans elle, le verre ne réfracte pas ; le chapitre 4 explique ce réglage. » Le chapitre 4 l'explique en détail et garde son exercice, qui fonctionne toujours : la case ne suit pas un Append, et le studio du chapitre 4 l'a décochée.
2. **L'ampoule à paroi mince.** Le plan du chapitre 2 prévoit que le chapitre 3 ajoute un Solidify à l'ampoule. Ce n'est plus utile : la case *Thin Wall* de Blender 5.2 suffit. Rien à changer au chapitre 2.
3. **Le lissage des bras et des articulations.** Le plan du chapitre 2 met *Shade Auto Smooth* sur le socle et la tête seulement. Les tiges et les articulations, en métal au chapitre 3, montreraient des reflets en escalier. Deux solutions : le chapitre 2 l'ajoute sur ces pièces, ou le check-up du chapitre 3 le fait faire (c'est ce que prévoit ce plan, sans notion nouvelle).
4. ***Shade Auto Smooth* dépend du chapitre 2.** Le plan du chapitre 2 le classe parmi ses ajouts hors programme, encore à valider. S'il est retiré, le chapitre 3 devra l'introduire au check-up, et ce ne serait plus un rappel.
5. **L'émission de l'ampoule.** Le chapitre 4 en fait un palier ★★ « si le chapitre 3 a vu la matière émissive ». Ce plan la présente dans un encart NOTE et un défi ★, sans pratique pour tous.
6. **Les coloris.** Le palier ★ du chapitre 4 prévoit deux coloris de la vue héros. Le coloris B existe déjà à la fin du chapitre 3, dans `Lampe_coloris_B` : le chapitre 4 peut l'importer par Append au lieu de le recréer.
7. **Les captures partagées.** `material_preview_popover_blender.jpg` et `material_settings_transmission_blender.jpg` figurent dans les deux plans. Le chapitre 3 les produit ; le chapitre 4 les réutilise.
8. **Une phrase des Basics.** Basics 101, § 4, annonce que les modes d'affichage seront exploités « au chapitre 4 ». Le chapitre 3 utilise *Material Preview* tout du long. Les Basics étant déjà livrés, aucune retouche n'est prévue : le formateur peut le dire en une phrase à l'ouverture (« le chapitre 3 commence à exploiter *Material Preview*, le chapitre 4 ira jusqu'au rendu »).
9. **Le moteur du fichier du chapitre 1.** `PRC02_ch1_blocage_lampe.blend` est réglé sur Cycles ; les plans des chapitres 2 et 4 le signalent aussi. Le check-up du chapitre 3 le vérifie.
10. **La grille d'aération.** Le plan du chapitre 2 (version de 00:52) modélise *Grille_aeration*, une couronne de 36 lamelles sur le socle. Le plan du chapitre 4 (version de 00:51) écrit « pas de grille d'aération ». Le chapitre 3 suit le chapitre 2 et habille la grille en `ABS_Noir`. Le chapitre 4 est à resynchroniser.
11. **La matière de la douille.** Le cahier CMF du chapitre 2 suggère du plastique ou de la céramique. Le chapitre 3 retient `Alu_Naturel`, récupéré du nuancier par Append, puis `Laiton` pour le coloris B. Les valeurs du chapitre 2 étant indicatives, rien à changer.
12. **Les catalogues hors du `.blend`.** Les catalogues d'un fichier ordinaire vivent dans un `blender_assets.cats.txt` posé à côté de lui (vérifié dans Blender 5.2.1). Sans effet sur l'Append du chapitre 4, qui emporte les matières. Mais tout fichier qui contient des actifs rangés doit voyager avec ce fichier, dans un dossier ou un zip : ici la bibliothèque et la lampe habillée.
13. **Les corrigés.** Selon la convention commune, ils sont dans des collections masquées : *Corrigé coloris A* et *Corrigé coloris B* (fiche A), *Corrigé* (fiche C) ; le corrigé du rangement en actifs est la bibliothèque elle-même. Le seul fichier séparé, `PRC02_ch3_lampe_habillage.blend`, est l'état attendu de `lampe_habillage_v002.blend` : le chapitre 4 en tire son fichier de secours. Les matières des corrigés portent le suffixe `_corrige`, pour ne pas entrer en conflit avec celles que l'apprenant crée dans le fichier de secours. Si le chapitre 4 reprend une lampe depuis un corrigé, il prend la fiche A2, dont les noms sont sans suffixe.

## Contrôle face aux critères du découpage

| Critère | Comment le plan y répond |
|---|---|
| 1 · Durée | 210 minutes de contenu et 20 minutes de pause : fin à 3:50, sous les 4 heures. Section 3 ramenée à 32 minutes, atelier porté à 20 minutes. |
| 2 · Périmètre | Les trois ancres `ch3_sec1_title` à `ch3_sec3_title` et les trois points du programme. Append est pratiqué ici ; Link est cité en une phrase, sa manipulation en défi ★. EEVEE, l'éclairage et la caméra restent au chapitre 4, sauf la case *Raytracing*, cochée pour le verre en une phrase (décision du 18 novembre). |
| 3 · Pas de redite | *Material Preview*, Pack Resources, Append et Link, le compteur d'utilisateurs et *Duplicate Collection* sont réinvestis, pas réexpliqués (tableau « Ce que le chapitre approfondit »). |
| 4 · Continuité | Entrée : `lampe_modele_v001.blend`. Sortie : `lampe_habillage_v002.blend`, collection *Lampe* pour l'Append du chapitre 4. Fichier de départ propre : fiche A. Fichier de fin propre, source du secours du chapitre 4 : fiche A2. |
| 5 · Fichiers et ateliers | Chaque exercice et l'atelier ont un fichier de travail et un corrigé en collection masquée « Corrigé… », signalé en une ligne dans le LISEZ-MOI (tableau en tête de « Fichiers d'exercice »). Un seul fichier séparé, justifié. Tous s'ouvrent seuls : images empaquetées, catalogues livrés avec leur `.blend`. Consignes par paliers dans chaque LISEZ-MOI ; défis ★ et ★★. Aucune modification des préférences des postes, ni des fichiers déjà livrés. |
| 6 · Chapitre 4 | Sans objet pour ce chapitre. Le plan laisse au chapitre 4 un fichier prêt à importer, et la lampe habillée comme source de son fichier de secours. |
| 7 · Progression | Une notion nouvelle par séquence, ou par étape dans « Finitions procédurales » ; démo, puis guidé, puis autonome, y compris en section 3. Environ 50 minutes de pratique autonome. Les nœuds n'arrivent qu'en section 2, à partir d'une matière déjà connue. L'atelier de 20 minutes ne réinvestit que des gestes vus. Prérequis et apports de chaque section en tête de section ; ouverture « Où l'on en est ». |

## Points techniques vérifiés dans Blender 5.2.1 LTS

Vérifiés le 18 novembre 2026, dans un Blender lancé à part, sans toucher à la session du formateur.

- **Principled BSDF :** les entrées utiles sont *Base Color*, *Metallic*, *Roughness*, *IOR*, *Alpha*, *Thin Wall* (nouvelle), *Normal*, *Specular IOR Level*, *Transmission Weight*, *Coat* (*Weight*, *Roughness*, *IOR*, *Tint*, *Normal*), *Sheen*, *Emission* (*Color*, *Strength*). Valeurs par défaut : *Roughness* 0,5, IOR 1,5.
- **L'onglet Material** affiche tous ces réglages sans passer par les nœuds : rubrique *Surface* (*Base Color*, *Metallic*, *Roughness*, *IOR*, *Alpha*, *Thin Wall*, *Normal*, puis les rubriques *Diffuse*, *Subsurface*, *Specular*, *Transmission*, *Coat*, *Sheen*, *Emission*, *Thin Film*), puis *Volume*, *Displacement*, *Thickness* et *Settings*.
- **Le verre sous EEVEE :** par défaut, le *Raytracing* de la scène et le *Raytraced Transmission* de la matière sont désactivés. Le verre ne montre alors que l'image d'environnement, en rendu comme en *Material Preview*. Il faut les deux cases. *Thin Wall* fonctionne sous EEVEE : la paroi devient fine et ne déforme plus.
- **Bump :** *Strength* 1 et *Distance* 0,001 par défaut ; *Distance* est un nombre sans unité, en mètres. Sur une tige de 8 mm, 0,001 donne un relief bruité, 0,0002 un brossé net. *Noise Texture* : *Scale* 5 par défaut.
- **Limites d'EEVEE (manuel) :** *Anisotropic*, le nœud *Bevel* et *Thin Film* ne fonctionnent que sous Cycles. La projection *Box* répète toujours l'image (*Repeat*).
- **Projection :** le nœud *Image Texture* propose *Flat*, *Box*, *Sphere* et *Tube*, avec *Blend* pour *Box* (0 par défaut). Aucun nœud « triplanaire » dédié, ni dans Blender ni dans la bibliothèque *Essentials*.
- **Material Preview :** huit images d'environnement intégrées (*city*, *courtyard*, *forest* par défaut, *interior*, *night*, *studio*, *sunrise*, *sunset*) ; options *Scene Lights* et *Scene World*.
- **Asset Browser :** méthodes d'import *Link*, *Append*, *Append (Reuse Data)* et *Pack*, plus *Follow Preferences* dans l'en-tête. *Mark as Asset* se trouve dans le menu *Assets* de l'Outliner et dans *Object > Asset*. La vue 3D n'a pas d'étagère d'actifs pour les matières : seulement pour les pinceaux.
- **Essentials :** la bibliothèque livrée avec Blender ne contient aucune matière. La bibliothèque CMF du chapitre est donc à créer.
- **Copies :** par défaut, `Maj + D` et *Duplicate Collection* copient les objets et les maillages, mais partagent les matières (préférence *Duplicate Data > Material* décochée).
- **Catalogues :** un fichier qui n'appartient à aucune bibliothèque enregistre ses catalogues dans un fichier `blender_assets.cats.txt` créé à côté de lui, pas dans le `.blend`. Testé dans une fenêtre Blender : un catalogue créé dans *Current File*, puis le fichier enregistré.
- **File > Append :** garde par défaut le statut d'actif, la description et les étiquettes d'une matière (option *clear_asset_data* décochée). La matière récupérée apparaît donc dans *Current File*.
- **Solidify :** rubrique *Materials*, *Material Offset* et *Rim*, pour un intérieur d'une autre matière.
- **Node Wrangler :** livré avec Blender, désactivé par défaut.

À vérifier pendant la construction des fichiers :
- le clic droit sur le nom d'une matière propose bien *Mark as Asset* ;
- le glisser-déposer d'une vignette de *Current File* sur une pièce lui donne bien la matière ;
- le catalogue où apparaît une matière récupérée du nuancier par Append, puisque l'identifiant de son catalogue d'origine est inconnu dans le fichier de la lampe ;
- la génération des vignettes d'actifs dans une construction en arrière-plan, sinon dans la fenêtre courte ;
- une image empaquetée dans la bibliothèque reste empaquetée après un Append ;
- les valeurs des images (fiche D) une fois les images créées : *Mapping Scale* et *Strength* se retouchent à l'œil ;
- la connexion faite par `Ctrl + T` de Node Wrangler (sortie *UV* ou *Generated*), à reconnecter sur *Object* si besoin ;
- *Shade Auto Smooth* sur une courbe avec Screw (l'ampoule) et sur le câble.

## Décisions du formateur, 18 novembre 2026

1. **Raytracing :** la case est cochée dès le chapitre 3, pour le verre, avec une seule phrase. Le chapitre 4 l'explique en détail.
2. **Atelier :** le second coloris est gardé, et passe de 12 à 20 minutes.
3. **Bibliothèque :** la déclaration dans les préférences devient une option. Le parcours principal passe par *File > Append*, sans modifier les préférences des postes.
4. **Mémo imprimé :** reporté, hors de ce plan.
5. **Plus d'autonomie :** Link réduit à une phrase, sa manipulation en défi ★, *Pack* cité de même ; les 8 minutes gagnées à 3:10 passent à l'atelier ; une partie de la pratique guidée de la section 3 devient autonome ; le quiz de la section 3 ne porte plus sur la manipulation de Link ni sur la bibliothèque déclarée.
6. **Corrigés :** la convention commune aux chapitres 2 à 4. Le corrigé est dans le fichier de travail, en collection masquée dont le nom commence par « Corrigé », et le LISEZ-MOI le signale en une ligne. Un fichier séparé n'existe que s'il est justifié : ici, seulement la lampe habillée, point de départ du chapitre 4. Les fichiers déjà livrés (Basics, initiation, chapitre 1) ne sont pas retouchés.

## Décisions de production, 19 novembre 2026

Prises par délégation pendant la production des fichiers, du texte et des captures, à confirmer par le formateur.

1. **Le relief se règle avec *Strength*, pas avec *Distance*.** Dans Blender 5.2, le champ *Distance* du nœud *Bump* affiche trois décimales : 0,0002 s'y lit « 0.000 », ce qui égarerait un débutant. *Distance* garde sa valeur par défaut (0,001) et *Strength* porte le réglage, avec le même rendu : brossé 0,15, peinture structurée 0,2, grain de l'ABS 0,05, microbillé 0,03, cuir 0,3, coque 0,1, carbone 0,1, tôle larmée 0,8. Le message pédagogique ne change pas : la valeur par défaut est trop forte pour un si petit objet. Les fichiers, les LISEZ-MOI et le texte suivent ces valeurs.
2. **Les préférences des bibliothèques :** dans Blender 5.2, la section est *Edit > Preferences > Asset Libraries*, et non *File Paths*. Le texte, les LISEZ-MOI et la figure 3.42 suivent.
3. **La méthode d'import :** le menu *Import Settings* de l'Asset Browser propose *Follow Asset or Preferences*, *Link*, *Append* et *Pack*. Une bibliothèque déclarée importe en *Pack* par défaut (vérifié dans Blender 5.2.1). Le texte le dit dans l'option « déclarer une bibliothèque », et conseille *Append* pour une matière à modifier.
4. **Les images de finition font 512 × 512 px**, et non 1024 : la projection *Box* en *Material Preview* n'en demande pas plus, et les fichiers restent légers (0,2 à 0,8 Mo).
5. **Les livrables en zip :** `PRC02_ch3_textures_cmf.zip` (le dossier `textures_cmf`), `PRC02_bibliotheque_CMF.zip` (le nuancier et son fichier de catalogues) et `PRC02_ch3_lampe_habillage.zip` (la lampe habillée et son fichier de catalogues). La lampe à habiller et les finitions triplanaires se distribuent seules.
6. **La grille *Metallic* / *Roughness*** est faite de sphères de 44 mm, plus lisibles que des plaquettes ; les plaquettes du nuancier sont couchées à 25° de l'horizontale, pour refléter le haut clair de l'image d'environnement. Le support mesure 1,05 × 0,95 m.
7. **La figure de *Blend*** (3.28) montre la tôle larmée projetée sur une coque de rétroviseur, cadrée serré sur le raccord, et non le socle : sur la peinture structurée, le raccord se lit à peine.
8. **Le panneau carbone** est construit debout dans son repère local, puis couché par sa rotation : le *Bend* du *Simple Deform* sur l'axe Y ne courbe pas un plan couché en XY (vérifié).
9. **Dans le fichier de démonstration des finitions,** le LISEZ-MOI occupe la zone du navigateur de fichiers de l'espace *Shading* : ce navigateur aurait enregistré le chemin absolu du dossier.

## Décisions du formateur, 25 novembre 2026

1. **Une erreur corrigée.** Le support, le déroulé et ce plan écartaient le nœud *Normal Map* « faute de dépliage UV ». C'est faux : une carte de normales en espace tangent, projetée en *Box* (coordonnées *Object*), donne un relief sans couche UV, en EEVEE comme en Cycles (test du formateur dans Blender 5.2.1, confirmé par le rendu de contrôle du corrigé). Le quiz qui en faisait un leurre est remplacé.
2. **Un lot de textures PBR dans le fil rouge, pour tous,** sur le socle, juste après la peinture structurée qui en pose les notions : séquence de 2:32, 12 minutes. Le formateur juge ces lots essentiels, voire majoritaires, dans le travail avec des designers CMF.
3. **Les lots :** trois lots CC0 de Poly Haven en 1K, téléchargés une fois avec son accord (fiche E) : le noyer de la recette, un béton lisse et un palissandre verni. Le formateur montre le téléchargement sur polyhaven.com. Pas de marbre : Poly Haven n'en propose pas en plaque sans joints.
4. **Le socle du coloris A garde le lot PBR.** `Structure_Vert` reste dans le fichier par son bouclier (*Fake User*) et sert au coloris B. La figure 3.1, la lampe habillée (fiche A2) et les fichiers du chapitre 4 gardent le socle en peinture structurée : ils deviennent des exemples.
5. **Le minutage :** les 12 minutes sont reprises ainsi : le verre dépoli ou fumé devient un défi ★ (−4) ; *Pack Resources* passe après le lot, une seule fois (−3) ; le quiz du *Bump* devient celui du lot (−1) ; la description d'un actif devient un défi ★ (−2) ; le bilan garde une question orale (−2). Seconde pause à 2:44.
6. **Le corrigé** va dans `PRC02_ch3_lampe_a_habiller.blend`, fichier déjà livré, avec l'accord du formateur : collection masquée *Corrigé socle PBR* (*Socle_PBR*, `Bois_Noyer_corrige`), une ligne et la recette dans le LISEZ-MOI. Les corrigés A et B et les paliers ★ du LISEZ-MOI restent tels quels (paliers à revoir plus tard). Le fichier passe à 1,9 Mo ; il est reconstruit par `build_lampe.py a`, puis `finish_ui.py`. À cette occasion, le reste d'un ancien chemin absolu, laissé dans le tampon du chemin de `grain_structure.png`, a disparu (`matieres.image` écrase désormais tout le tampon).
