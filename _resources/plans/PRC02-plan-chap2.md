# Chapitre 2 · Modélisation non destructive : plan de la demi-journée

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 4 sur 6, en présentiel, de 5 à 8 apprenants · Plan du 18 novembre 2026, **validé** par le formateur le même jour, avec ses décisions (dernière partie)

Ce plan suit le découpage validé (`PRC02-decoupage-formation.md`) et ses critères de contrôle. Les libellés cités ont été vérifiés dans Blender 5.2.1. Les valeurs de la lampe, des défis et de la liseuse ont été éprouvées sur des prototypes construits en arrière-plan.

## En bref

- **Objectif du chapitre** (déclaré dans l'application) : modéliser un objet industriel de façon non destructive avec les modificateurs de symétrie, d'épaisseur et de répétition, et dessiner profils et détails organiques avec les courbes de Bézier.
- **À la fin de la demi-journée, l'apprenant sait :**
  - refléter une pièce avec *Mirror*, sur l'axe de son choix ;
  - donner une épaisseur régulière à une coque avec *Solidify* ;
  - arrondir les arêtes avec *Bevel* et lisser l'affichage avec *Shade Auto Smooth* ;
  - répéter un détail en couronne avec *Array* et un *Empty* ;
  - dessiner une courbe de Bézier et régler ses poignées ;
  - faire d'une courbe un câble, ou une pièce de révolution avec *Screw* ;
  - garder un modèle modifiable de bout en bout, prêt à recevoir ses matières.
- **Format :** 3 h 30 de contenu et 2 pauses de 10 minutes, soit 3 h 50. Il reste 10 minutes de marge sur 4 heures. Exemple : de 9 h 00 à 12 h 50.
- **Principe :** le même qu'à l'initiation. Une seule notion nouvelle à la fois, montrée en quelques minutes, puis pratiquée en guidé, puis réinvestie en autonomie. Les apprenants ne passent jamais plus de 15 minutes sans toucher la souris.
- **Fil rouge :** la lampe de bureau du chapitre 1. Son blocage sert de gabarit : chaque volume est remplacé par une pièce propre. La répartition suit le découpage : symétrie pour le pied, épaisseur pour l'abat-jour, répétition pour une grille d'aération, courbes de Bézier pour le câble et le profil de l'ampoule.
- **Règle du jour :** « On n'applique aucun modificateur. » Une épaisseur, un nombre de lamelles ou un profil doivent rester modifiables jusqu'au chapitre 4.
- **Fichiers :** un seul fichier de travail pour la lampe. Le corrigé de chaque séquence, de l'atelier et des défis s'y trouve, dans une collection masquée dont le nom commence par « Corrigé » (tableau en tête de la partie « Les fichiers d'exercice »).

### Ce qui est acquis, ce que l'on approfondit

L'initiation a présenté les modificateurs (Basics 103 § 3) et les a mis en œuvre dans la rangée de sièges. Le chapitre 1 a apporté les unités, l'aimantation, les orientations et la mesure. Ce chapitre ne les répète pas : il les pousse plus loin, sur une vraie pièce.

| Notion | Déjà vu | Approfondi ici |
|---|---|---|
| La pile de modificateurs | Onglet *Modifiers*, ordre, affichage, *Apply* | *Copy to Selected* ; ne pas appliquer ; l'ordre, en simple remarque |
| *Mirror* | Axe X, origine sur l'axe du couloir (sièges) | Un autre axe ; le reflet autour de l'origine ; *Mirror Object* |
| *Solidify* | Une démo sur un plan | Une coque ouverte : *Offset*, *Even Thickness*, *Fill Rim* |
| *Bevel* (modificateur) | Le *Bevel* en outil (`Ctrl + B`) ; le modificateur cité, en palier ★ des sièges seulement | Nouveau pour la plupart : découvert sur le socle, en autonomie ; *Amount*, *Segments*, *Limit Method* sur *Angle* |
| *Array* | *Relative Offset* et *Constant Offset* (sièges) | *Object Offset* avec un *Empty* : la répétition en couronne |
| Courbes de Bézier | Rien | Tout : points, poignées, *Curve Pen*, épaisseur, révolution |
| Aimantation, orientation *Local*, mesure | Chapitre 1 § 3 | Réutilisées pour poser les pièces |

**Trois ajouts hors programme, retenus par le formateur.** Le programme officiel ne les cite pas, mais chacun sert directement l'un de ses points :
- le modificateur ***Screw*** : il fait tourner un profil de Bézier autour d'un axe. C'est la façon la plus simple de tirer une pièce d'un profil, comme la révolution en CAO ;
- ***Shade Auto Smooth*** (menu *Object*) : il lisse l'affichage des faces courbes sans arrondir les arêtes vives. Sans lui, une coque à 24 côtés paraît facettée. Le chapitre 3 en dépend : ses métaux montreraient chaque facette ;
- le **parentage** (`Ctrl + P > Object`) : un seul geste, pour que l'*Empty* d'une répétition en couronne suive sa pièce.

### Ce que l'on survole

Ces notions sont présentées dans l'application. Elles ne sont ni pratiquées ni exigées en séance ; certaines servent de défi.
- *Clipping* et *Bisect* du *Mirror* : utiles pour modéliser la moitié d'une forme qui traverse le plan de symétrie. Elles servent le défi de la chape.
- *Fit Type > Fit Length* de l'*Array*.
- Le mode *Complex* du *Solidify*.
- L'outil *Draw* (tracé à main levée) et le mode *Object* du *Bevel* de courbe (balayer un profil le long d'un chemin).
- *Object > Convert > Mesh* : figer une courbe en maillage, pour un export.
- Le *Boolean* : déjà cité à l'initiation, il revient seulement en défi.

## Minutage

| Horaire | Durée | Séquence | Section | Modalité |
|---|---|---|---|---|
| 0:00 | 10 min | Lancement : du blocage au modèle | | Collectif + prise en main du fichier |
| 0:10 | 25 min | Symétrie : *Mirror* | 1 | Démo 10 min + guidé 10 min + autonomie 5 min |
| 0:35 | 25 min | Épaisseur : *Solidify*, puis lissage et *Bevel* | 1 | Démo 8 min + guidé 9 min + autonomie 8 min |
| 1:00 | 10 min | Pause | | |
| 1:10 | 30 min | Répétition : la grille d'aération | 1 | Démo 10 min + guidé 12 min + autonomie 8 min |
| 1:40 | 30 min | Courbes de Bézier : le câble | 2 | Démo 10 min + guidé 10 min + autonomie 10 min |
| 2:10 | 25 min | Profil de révolution : l'ampoule | 2 | Démo 10 min + guidé 10 min + autonomie 5 min |
| 2:35 | 10 min | Pause | | |
| 2:45 | 50 min | Atelier : la lampe modélisée | 3 | Lancement 5 min + autonomie 40 min + retour 5 min |
| 3:35 | 15 min | Galerie, bilan et passerelle vers le chapitre 3 | 3 | Collectif |

Sur 3 h 30 : 48 minutes de démonstration, 51 minutes de pratique guidée, 76 minutes en autonomie et 35 minutes en collectif. Dans chaque séquence, les démos sont découpées en cycles courts : une notion, montrée puis pratiquée, avant la suivante.

### 0:00 · Lancement : du blocage au modèle (10 min)

- **Où l'on en est :** « Au chapitre 1, vous avez arrêté les proportions de la lampe. Aujourd'hui, chaque volume devient une pièce propre, et chaque décision reste modifiable. Au chapitre 3, ces pièces recevront leurs matières. »
- **Montrez le but :** ouvrez l'œil de la collection *Corrigé*, à côté du gabarit en fil de fer. Changez une valeur en direct, par exemple le nombre de lamelles de la grille d'aération : c'est cela, le non destructif. Refermez l'œil.
- **Ils ouvrent `PRC02_ch2_lampe_depart.blend`** (fichier 1, plus bas). Ils y trouvent :
  - la collection *Gabarit* : le blocage de la variante A, en fil de fer et non sélectionnable ;
  - la collection *Lampe* : une copie de travail, une pièce par volume, nommée sans suffixe (*Socle*, *Bras_bas*, *Tête*…) ;
  - la collection *Croquis* : les croquis de face et de profil, le demi-profil de l'ampoule et son repère.
- **Ils l'enregistrent aussitôt** sous `lampe_modele_v001.blend` (*File > Save As*), puis font `Ctrl + S` à chaque point de contrôle. Le fichier de départ reste intact.
- **Ce fichier remplace le travail du chapitre 1.** Il permet de commencer en cas d'absence, de retard ou de fichier perdu. Ceux qui veulent garder leur propre blocage le peuvent ; les valeurs du LISEZ-MOI deviennent alors indicatives.
- **En cas de retard pendant la demi-journée,** l'apprenant prend la pièce qui lui manque dans la collection *Corrigé* : il supprime sa propre version, fait `M` vers *Lampe*, puis renomme la pièce sans `_corrige`. Une pièce qui a un *Empty* se déplace avec lui.

**Point de contrôle :** chaque écran montre le gabarit en fil de fer et la copie en volume. L'unité affichée est le millimètre.

## Section 1 · Modificateurs : symétrie, épaisseur, répétition

Ancre : `ch2_sec1_title`.

### Prérequis et nouveautés

| Prérequis, déjà vus | Où |
|---|---|
| Mode Édition, sélection des sommets, arêtes et faces | Basics 103 § 1 ; initiation, demi-journée 2 |
| `G`, `R`, `S` avec un axe et une valeur ; `Maj + Z` pour exclure un axe | Basics 102 § 1 ; chapitre 1 § 3 |
| `Maj + A`, le panneau F9, `X` pour supprimer un objet | Basics 102 § 2 |
| Le curseur 3D : `Maj + C`, `Maj + S > Cursor to Selected` | Initiation, demi-journée 1 ; clinique, patient 5 |
| L'onglet *Modifiers*, la pile, l'ordre, l'affichage, *Apply* | Basics 103 § 3 |
| *Mirror* sur X, *Array* en *Relative* et *Constant Offset* | Initiation, activité B |
| *Solidify* (une démo) ; le *Bevel* en outil (`Ctrl + B`, segments à la molette) | Initiation, demi-journée 2 ; activité B |
| Normales, *Face Orientation*, échelle appliquée | Basics 103 § 4 ; clinique |
| Saisie d'une valeur avec son unité ; affichage en millimètres, recommandé et non exigé | Chapitre 1 § 1 |

| Nouveau, dans l'ordre d'introduction | Séquence |
|---|---|
| 1. *Mirror* sur un autre axe, et le reflet autour de l'origine | Symétrie, cycle A |
| 2. *Mirror Object* et *Copy to Selected* | Symétrie, cycle B |
| 3. Supprimer une face en Mode Édition (`X > Faces`) ; *Solidify* sur une coque ouverte | Épaisseur, cycle A |
| 4. *Shade Auto Smooth* | Épaisseur, cycle B (démo, puis guidé) |
| 5. Le *Bevel* en modificateur : *Amount*, *Segments*, *Limit Method* | Épaisseur, cycle B (découverte en autonomie, sur le socle) |
| 6. L'*Empty* (`Maj + A > Empty`) et l'*Array* en *Object Offset* | Répétition, cycle A |
| 7. Le parentage (`Ctrl + P > Object`) | Répétition, cycle B |

### Notions

- **La pile :** *Add Modifier > Generate* ; le menu de l'en-tête d'un modificateur (*Apply*, *Duplicate*, *Copy to Selected*, *Move to First*, *Move to Last*). L'ordre d'évaluation, de haut en bas, est rappelé en simple remarque, sans manipulation. La différence entre **appliquer un modificateur** et **appliquer l'échelle** (`Ctrl + A > Scale`), que les débutants confondent.
- ***Mirror* :** l'axe se lit dans le repère de l'objet ; le reflet se fait autour de l'origine ; *Mirror Object* reflète autour d'un autre objet.
- ***Solidify* :** *Thickness* ; *Offset* (-1, 0 ou 1) pour épaissir vers l'intérieur, de part et d'autre ou vers l'extérieur ; le rôle des normales ; *Even Thickness* ; *Fill Rim*.
- **Lissage et *Bevel* :** *Object > Shade Auto Smooth* ajoute en bas de la pile le modificateur *Smooth by Angle*, épinglé en dernière position. Le *Bevel* en outil (`Ctrl + B`), connu depuis l'initiation, existe aussi en modificateur : le même arrondi, qui reste modifiable. *Amount*, *Segments*, *Limit Method* sur *Angle* (le réglage d'usine).
- ***Array* en couronne :** *Object Offset* avec un *Empty* tourné de 360° divisé par le nombre de copies ; l'*Empty* rendu enfant de la pièce répétée.

**Dans l'application**, la section suivra la même progression : la pile, puis symétrie, épaisseur (avec le lissage et le *Bevel*) et répétition. Chaque modificateur aura une capture de son panneau, un exemple sur la lampe et un exemple dans les transports.

### 0:10 · Symétrie : *Mirror* (25 min)

**Cycle A : un autre axe (démo 5 min, guidé 10 min).**

Vous montrez, sur *Bras_bas* :
1. `Tab`, `A`, `S Maj + Z 0.5` : la tige passe à 8 mm de diamètre. Puis `G Y = 10mm` : elle quitte l'axe de la lampe. `Tab`.
2. *Add Modifier > Generate > Mirror*. Par défaut, l'axe X est coché : décochez-le et cochez Y. Le bras devient une paire de tiges parallèles.
3. **Ailleurs :** on modélise ainsi une moitié de capot, de nez de tram ou de fuselage.

Ils font, en guidé : les étapes 1 et 2 sur *Bras_bas*.

**Cycle B : l'origine, *Mirror Object* et *Copy to Selected* (démo 5 min, autonomie 5 min).**

Vous montrez :
1. **Le piège :** sur une copie, `G Y = 10mm` en Mode Objet. Le *Mirror* semble ne rien faire : il reflète autour de l'origine de l'objet, qui a suivi la tige. Deux solutions : décaler la géométrie en Mode Édition, comme au cycle A, ou choisir le *Socle* comme *Mirror Object*.
2. *Copy to Selected* : *Bras_haut* sélectionné, *Bras_bas* actif, menu de l'en-tête du *Mirror*. Le modificateur passe sur *Bras_haut*.

Ils font, en autonomie : le même résultat sur *Bras_haut*, avec *Copy to Selected* et un décalage de 10 mm en Mode Édition.

**Point de contrôle :** en vue de dessus (`7`), chaque bras montre deux tiges, symétriques par rapport à l'axe du socle. Dans `N > Item`, la position de *Bras_bas* n'a pas changé.

**Corrigé :** collection masquée *Corrigé*, *Bras_bas_corrige* et *Bras_haut_corrige*.

**Points d'observation :**
- Des tiges qui plongent dans le socle : l'axe X est resté coché.
- `G Y` fait en Mode Objet : c'est le piège du cycle B.
- *Copy to Selected* sans effet : l'objet actif doit être celui qui porte le modificateur.

### 0:35 · Épaisseur : *Solidify*, puis lissage et *Bevel* (25 min)

**Cycle A : la coque (démo 5 min, guidé 7 min).** Une seule notion : la coque ouverte et son épaisseur.

Vous montrez, sur *Tête* :
1. `Tab`, `3`, clic sur la grande face de l'ouverture, puis `X > Faces`. Il reste une surface sans épaisseur. `Tab`.
2. *Add Modifier > Generate > Solidify* : *Thickness* `1.5mm`. Faites varier *Offset* de -1 à 1 : l'épaisseur passe de l'intérieur à l'extérieur. Remettez -1. Cochez *Even Thickness*. Montrez *Fill Rim*, qui ferme le bord.
3. **Ailleurs :** un carénage d'avion, une coque de rétroviseur, un panneau d'habillage intérieur de train.

Ils font, en guidé : les étapes 1 et 2 sur *Tête*.

**Cycle B : le lissage (démo 3 min, guidé 2 min), puis la découverte du *Bevel* (autonomie 8 min).**

Vous montrez : *Object > Shade Auto Smooth* sur *Tête*. Les 24 côtés de la coque paraissent lisses, les arêtes vives restent nettes. Le modificateur *Smooth by Angle* s'ajoute en bas de la pile.

> **NOTE · L'ordre de la pile (30 secondes, sans manipulation).** La pile de la tête compte maintenant deux modificateurs. Blender les calcule de haut en bas : chacun travaille sur le résultat du précédent. Changer l'ordre peut donc changer le résultat ; Basics 103 § 3 l'a montré. *Smooth by Angle* fait exception : l'épingle de son en-tête le garde en dernière position, même si l'on ajoute un modificateur après lui (figure 2.12).

Ils font :
- **en guidé :** *Shade Auto Smooth* sur *Tête* ;
- **en autonomie, découverte du *Bevel* sur *Socle*,** avec les valeurs du LISEZ-MOI et la figure 2.10. Annoncez-le en une phrase : « Le *Bevel* que vous connaissez en outil existe aussi en modificateur. » *Add Modifier > Generate > Bevel* : *Amount* `3mm`, *Segments* 3, *Limit Method* sur *Angle* (déjà réglé). Puis *Shade Auto Smooth* sur *Socle*. Enfin, *Shade Auto Smooth* sur *Bras_bas* et *Bras_haut*, sélectionnés ensemble : leurs tiges seront en métal au chapitre 3, et un métal montre la moindre facette ;
- **★ :** essayer 1 mm puis 3 mm d'épaisseur sur la tête ; ajouter dès maintenant le *Bevel* de la tête, prévu à l'atelier.

Passez d'abord par les postes qui découvrent le *Bevel* : c'est la seule notion nouvelle pratiquée sans démo.

**Point de contrôle :** en vue de dessous, le bord de la tête montre une épaisseur régulière. Les piles se lisent, de haut en bas : *Tête* = *Solidify*, *Smooth by Angle* ; *Socle* = *Bevel*, *Smooth by Angle*. Les arêtes du socle sont arrondies.

**Corrigé :** collection masquée *Corrigé*, *Tête_corrige* et *Socle_corrige*. La tête du corrigé porte en plus le *Bevel* ajouté à l'atelier.

**Points d'observation :**
- L'épaisseur part vers l'extérieur : les normales sont inversées, ou *Offset* vaut 1. *Face Orientation* tranche la question.
- `X` en Mode Objet supprime tout l'objet : `Ctrl + Z`.
- Un arrondi à grosses facettes : *Segments* est resté à 1.
- Un socle déformé : *Amount* est trop grand. Lisez la valeur affichée dans le champ, avec son unité.

### 1:00 · Pause (10 min)

### 1:10 · Répétition : la grille d'aération (30 min)

Le socle cache l'électronique de la lampe : il lui faut une grille d'aération. Elle prend la forme d'une couronne de lamelles sur le dessus du socle.

**Cycle A : la couronne (démo 7 min, guidé 10 min).**

Vous montrez :
1. **Rappel (1 min) :** *Relative Offset* et *Constant Offset*, vus avec les sièges, répètent en ligne. Pour répéter en couronne, il faut un repère qui tourne : un *Empty*, un objet sans géométrie, comme celui qui porte une image de référence.
2. `Maj + C` : le curseur 3D revient au centre, sous l'axe du socle. `Maj + A > Mesh > Cube`, F9 : *Size* `2mm`. `Tab`, puis `S X 6` : une lamelle de 12 mm. `G X = 76mm`, puis `G Z = 25mm` : elle se pose sur le dessus du socle, près du bord. `Tab`. L'origine de la lamelle reste au centre du socle. Renommez-la *Grille_aeration*.
3. `Maj + A > Empty > Plain Axes`, au même endroit, puis `R Z 10`. Renommez-le *Grille_pivot*.
4. Sur la lamelle : *Add Modifier > Generate > Array (Legacy)*. Décochez *Relative Offset*, cochez *Object Offset* et choisissez *Grille_pivot*. *Count* 36 : les lamelles font le tour du socle.
5. **Ailleurs :** les aubes d'une soufflante, les rayons d'une jante, les boulons d'une roue de bogie.

> **NOTE · Deux entrées *Array*.** Blender 5.2 propose aussi *Array*, un nouvel outil en Geometry Nodes ; ce chapitre utilise le modificateur classique, *Array (Legacy)*, qui accepte un *Empty* en *Object Offset*.

Ils font, en guidé : les étapes 2 à 4.

**Cycle B : l'*Empty* suit la pièce (démo 3 min, guidé 2 min, autonomie 8 min).**

Vous montrez : déplacez la lamelle seule. La couronne se déforme, car l'*Empty* est resté en place. `Ctrl + Z`. Sélectionnez *Grille_pivot*, puis *Grille_aeration* en dernier, et `Ctrl + P > Object` : l'*Empty* suit désormais la lamelle.

Ils font :
- **en guidé :** le parentage de *Grille_pivot*, puis un essai de déplacement, annulé avec `Ctrl + Z` ;
- **en autonomie :** la même méthode sur *Interrupteur*, qui devient une molette crantée. Le curseur va sur l'interrupteur (`Maj + S > Cursor to Selected`) ; un cran de 1,5 × 1,5 × 6 mm se place à 8 mm de l'axe ; l'*Empty* tourne de 15° pour 24 crans. Les apprenants trouvent seuls cette valeur. Les objets s'appellent *Interrupteur_crans* et *Interrupteur_pivot*.

**Point de contrôle :** 36 lamelles régulières sur le socle, et 24 crans autour de l'interrupteur. Un déplacement de la lamelle emporte toute la couronne.

**Corrigé :** collection masquée *Corrigé*, *Grille_aeration_corrige* et *Interrupteur_crans_corrige*, avec leurs *Empty*.

**Points d'observation :**
- Un cube de 2 m : F9 a été oublié. Blender ajoute ses primitives à leur taille d'origine, en mètres.
- Une spirale : *Relative Offset* est resté coché.
- Une couronne décentrée : le curseur 3D n'était pas au bon endroit au moment d'ajouter l'*Empty*.
- `Ctrl + P` dans le mauvais ordre : la lamelle devient l'enfant de l'*Empty*. L'objet actif, sélectionné en dernier, devient le parent.

## Section 2 · Courbes de Bézier : profils et détails

Ancre : `ch2_sec2_title`.

### Prérequis et nouveautés

| Prérequis, déjà vus | Où |
|---|---|
| Mode Édition, `E` pour extruder, `G` avec un axe | Basics 103 § 1 et 2 |
| Les vues orthographiques `1` et `7` | Basics 101 § 4 |
| `Maj + A`, F9, `Maj + S > Cursor to Selected`, `N > Item` | Basics 102 ; clinique ; chapitre 1 § 2 |
| L'aimantation sur *Face* | Chapitre 1 § 3 |
| L'onglet *Object Data* (pour une image de référence) | Chapitre 1 § 1 |
| La pile de modificateurs, *Merge* (*By Distance*) | Section 1 ; clinique, patient 3 |

| Nouveau, dans l'ordre d'introduction | Séquence |
|---|---|
| 1. L'objet courbe : points de contrôle, poignées et leurs types (`V`) ; `E` et `Ctrl + clic droit` sur une courbe | Câble, cycle A |
| 2. La rubrique *Geometry* de la courbe : *Bevel*, *Depth*, *Resolution*, *Fill Caps* | Câble, cycle B |
| 3. L'outil *Curve Pen* : un clic pour un angle, un cliquer-glisser pour une courbe | Câble, cycle C |
| 4. `Maj + S > Selection to Cursor` ; le modificateur *Screw* et sa *Merge Distance* | Ampoule |

### Notions

- **Courbe et maillage :** une courbe est définie par quelques points de contrôle ; Blender en calcule la forme lisse. Sa finesse se règle après coup : la courbe est non destructive par nature.
- **Anatomie d'un point :** le point de contrôle et ses deux poignées. Les types de poignée, avec `V` : *Automatic*, *Vector*, *Aligned* et *Free*.
- **Dessiner :** *Add > Curve > Bézier* ; en Mode Édition, `E` prolonge la courbe depuis un point, `Ctrl + clic droit` ajoute un point sous la souris. L'outil *Curve Pen* de la barre d'outils pose un point anguleux d'un clic et un point arrondi d'un cliquer-glisser, comme en dessin vectoriel.
- **Donner du volume :** onglet *Object Data* de la courbe. Rubrique *Shape* : *Resolution Preview U*. Rubrique *Geometry* : *Bevel* en mode *Round*, avec *Depth*, *Resolution* et *Fill Caps*. *Extrude* et *Offset*, voisins, sont seulement cités.
- **Profil de révolution :** le modificateur *Screw* (*Axis*, *Angle* 360°, *Steps*, *Merge Vertices*, *Merge Distance*), sur une courbe ou un maillage.

**Dans l'application**, la section commencera par l'anatomie d'une courbe, avec une capture annotée. Viendront ensuite le dessin, le volume, puis la révolution.

### 1:40 · Courbes de Bézier : le câble (30 min)

**Cycle A : points et poignées (démo 4 min, guidé 6 min).**

Vous montrez :
1. Vue de dessus (`7`). `Maj + A > Curve > Bézier`, F9 : *Radius* `50mm`. Sans ce réglage, la courbe mesure 2 m. Renommez-la *Câble*.
2. `Tab` : les points et leurs poignées. Déplacez un point, puis une poignée. `V` : *Vector* casse l'angle, *Automatic* l'adoucit.
3. `E` sur le dernier point prolonge la courbe ; `Ctrl + clic droit` pose un point sous la souris.

Ils font, en guidé : un tracé de 4 ou 5 points, de l'arrière du socle (à gauche en vue de face) vers le bord de la table.

**Cycle B : le volume (démo 3 min, guidé 4 min).**

Vous montrez :
1. Onglet *Object Data* (icône de courbe), rubrique *Geometry > Bevel* : *Round*, *Depth* `2.5mm` (un câble de 5 mm), *Resolution* 4, *Fill Caps*. Rubrique *Shape* : montez *Resolution Preview U* si le câble paraît anguleux.
2. Avec l'aimantation *Face* du chapitre 1, posez le premier point contre le flanc du socle ; les suivants reposent sur la table.
3. **Ailleurs :** une main courante ou une barre de maintien de tram, une durite, un faisceau électrique.

Ils font, en guidé : le câble rond de 5 mm, son premier point contre le socle.

**Cycle C : *Curve Pen* (démo 3 min, autonomie 10 min).**

Vous montrez : l'outil *Curve Pen*, dans la barre d'outils du Mode Édition. Un clic pose un point anguleux ; un cliquer-glisser tire ses poignées et pose un point arrondi.

Ils font, en autonomie : un second tracé du câble avec *Curve Pen*, avec une boucle posée sur la table. Chacun garde le tracé qu'il préfère.

**Point de contrôle :** en vue de face, le câble repose sur la table. Il est rond et lisse ; en Mode Édition, il ne compte que 4 à 6 points.

**Corrigé :** collection masquée *Corrigé*, *Câble_corrige*.

**Points d'observation :**
- Des points posés en perspective partent en profondeur : travaillez en vue orthographique de dessus.
- Un câble plat : *Extrude* a été réglé à la place de *Depth*.
- Un câble à facettes : *Resolution* ou *Resolution Preview U* est trop basse.
- Un câble qui s'enfonce dans la table : une poignée descend sous le plan. Remontez-la en vue de face.

### 2:10 · Profil de révolution : l'ampoule (25 min)

**Vous montrez (10 min) :**
1. **Le principe :** on dessine la moitié du profil, et Blender le fait tourner autour d'un axe. C'est la révolution des logiciels de CAO.
2. Clic sur *Repere_ampoule*, à droite de la lampe, puis `Maj + S > Cursor to Selected` : le curseur se pose sur l'axe de l'ampoule, à sa base.
3. `Maj + A > Curve > Bézier`, renommée *Ampoule*. `Tab`. Supprimez le point de droite (`X > Vertices`). Sélectionnez celui qui reste, puis `Maj + S > Selection to Cursor` : c'est le point 1 du croquis, sur l'axe. `V > Vector`.
4. Vue de face (`1`). Avec *Curve Pen* : un clic sur les points 2 et 3 du croquis (le culot, anguleux), un cliquer-glisser vertical sur le point 4 (le globe), un cliquer-glisser horizontal sur le point 5 (le sommet, sur l'axe).
5. `Tab`. *Add Modifier > Generate > Screw* : *Axis* Z, *Steps* 32, *Merge Vertices* coché, *Merge Distance* `0.1mm`. L'ampoule apparaît.
6. `Tab`, puis déplacez une poignée du profil : toute l'ampoule suit. C'est un profil qui reste modifiable.
7. **Ailleurs :** le profil d'une roue ferroviaire, l'optique d'un phare, le cône d'une hélice.

**Ils font :**
- **guidé (10 min) :** les étapes 2 à 5 ;
- **en autonomie (5 min) :** retoucher le profil (un globe plus rond, un culot plus long), comparer 16 et 48 *Steps*, puis placer l'ampoule dans la tête avec `N > Item` : *Location* 211, 0, 411 mm ; *Rotation* Y 150°.

**Point de contrôle :** une ampoule lisse, fermée en haut et en bas, logée au fond de la tête.

**Corrigé :** collection masquée *Corrigé*, *Ampoule_corrige*.

**Points d'observation :**
- Un sommet aplati : *Merge Distance* vaut 10 mm par défaut. Tout ce qui passe à moins de 10 mm de l'axe est soudé. Ramenez-la à 0,1 mm.
- Un trou au sommet : le dernier point ne touche pas l'axe, ou *Merge Vertices* n'est pas coché.
- Un disque à la place d'une ampoule : le mauvais axe est choisi.
- Un sommet pointu : le point 5 a été posé d'un simple clic. Ses poignées doivent être horizontales.

> **À tester lors de la construction des fichiers :**
> - l'enchaînement de l'étape 4 : *Curve Pen* prolonge-t-il bien la courbe depuis le point 1 sélectionné ? Sinon, `Ctrl + clic droit` pour les points 2 à 4, puis *Curve Pen* pour le point 5 ;
> - une valeur tapée pendant un geste : point tranché au plan du chapitre 1. Un nombre seul suit l'unité affichée, et une unité n'est lue qu'après `=`, la saisie avancée. Les valeurs à taper pendant un geste s'écrivent donc avec `=` et leur unité (`G X = 76mm`). Ainsi, chacun suit, que son fichier affiche des mètres ou des millimètres.

### 2:35 · Pause (10 min)

## Section 3 · Atelier : concept d'objet industriel

Ancre : `ch2_sec3_title`.

### Prérequis et nouveautés

| Prérequis, déjà vus | Où |
|---|---|
| Tous les gestes des sections 1 et 2, dont le *Bevel* en modificateur et *Shade Auto Smooth* | Ce chapitre |
| `Maj + D` et `Alt + D` ; copie liée et maillage partagé | Basics 102 ; initiation, activités A et C |
| L'orientation *Local* et `G Z Z` | Chapitre 1 § 3 |
| La checklist du modèle propre | Basics 103 § 4 ; clinique |
| Les collections, le nommage, l'enregistrement par versions | Basics 102 § 4 ; initiation, demi-journée 1 |

**Nouveau :** aucune notion. L'atelier réinvestit les sections 1 et 2, avec une méthode de travail : remplacer pièce par pièce les volumes du blocage, en les comparant au gabarit.

### Notions

- Remplacer un volume du blocage par une pièce propre, à sa place et à ses cotes.
- Comparer la pièce au gabarit, sous les vues de face et de profil.
- Tenir un fichier propre : des noms clairs, l'échelle appliquée, les normales vérifiées, les modificateurs non appliqués.
- Enregistrer la version de fin : `lampe_modele_v001.blend`.

**Dans l'application**, la section présentera la méthode, la checklist du modèle propre, et un défi fil rouge (encart *CAUTION*) avec des cotes indicatives.

### 2:45 · Atelier : la lampe modélisée (50 min)

**Situation :** « Le concept a passé la revue de blocage. Préparez la maquette numérique de la revue de design. Le client demandera sûrement des retouches : tout doit rester modifiable. »

**Objectif :** terminer les pièces de la lampe, l'assembler, la contrôler, puis l'enregistrer.

**Déroulé :**
1. **Lancement (5 min).** Ouvrez l'œil de la collection *Corrigé*, à côté du gabarit. Rappelez la règle du jour : rien n'est appliqué, sauf l'échelle. Lancez le minuteur.
2. **Autonomie (40 min).** Chacun suit la partie « Atelier » du LISEZ-MOI. Annoncez les 10 dernières minutes : c'est le moment de la checklist et de l'enregistrement.
3. **Retour (5 min).** Un volontaire projette sa lampe et change une valeur en direct : l'épaisseur de la tête, le nombre de lamelles ou le tracé du câble. Question : « Le client veut une tête 20 % plus grande. Combien de temps vous faut-il ? »

**Le socle de l'atelier :**

| Pièce | Ce qu'il reste à faire | Gestes réinvestis |
|---|---|---|
| *Articulation_bas*, *_milieu*, *_haut* | Remplacer chaque sphère par un cylindre couché sur Y, au même diamètre, de 36 mm de long | `Maj + S > Cursor to Selected`, `Maj + A` et F9, `R X 90`, `X`, *Bevel*, *Shade Auto Smooth* |
| *Douille* | Un cylindre de 30 mm de diamètre et 20 mm de long, au fond de la tête | `Maj + S > Cursor to Selected` sur *Tête*, F9 (*Rotation* Y -30°), puis `G Z Z = 45mm` : le long de son propre axe ; *Bevel*, *Shade Auto Smooth* |
| *Tête* | Arrondir le bord de l'ouverture : *Bevel* de 0,5 mm. Il se place de lui-même au-dessus de *Smooth by Angle* | *Bevel*, vu sur le socle |
| *Interrupteur* | *Bevel* de 0,5 mm et *Shade Auto Smooth* | *Bevel*, *Shade Auto Smooth* |
| *Ampoule* | La placer, si ce n'est pas fait | `N > Item` |
| *Câble* | Vérifier qu'il touche le socle et repose sur la table | Aimantation, vues orthographiques |
| Tout | La checklist, puis l'enregistrement | Basics 103 § 4 |

La checklist, au tableau et à la fin du LISEZ-MOI :
- chaque pièce porte un nom clair et se range dans la collection *Lampe* ;
- les échelles valent 1 (`Ctrl + A > Scale` si besoin) ;
- *Face Orientation* ne montre aucune face rouge ;
- les modificateurs sont tous actifs, aucun n'est appliqué ;
- la silhouette suit le gabarit, sous les vues de face et de profil ;
- la collection *Gabarit* est masquée ; le fichier `lampe_modele_v001.blend` est enregistré (`Ctrl + S`).

**Paliers :**
- **★ :** des molettes de serrage sur les articulations, en copies liées de la molette de l'interrupteur (`Alt + D`) ; une rainure décorative sur le pourtour du socle (*Loop Cut*, puis *Extrude* vers l'intérieur) ; une collection par sous-ensemble (*Pied*, *Bras*, *Tête*), dans *Lampe*.
- **★★ :** voir « Les défis pour ceux qui avancent vite ».

**Points d'observation :**
- Trois articulations de diamètres différents : des copies simples (`Maj + D`), redimensionnées en Mode Édition. Une copie liée mise à l'échelle en Mode Objet garderait une échelle non appliquée.
- `Ctrl + A` ouvre le menu d'application des transformations. Rien à voir avec *Apply* dans l'en-tête d'un modificateur.
- Un *Bevel* plus large que l'épaisseur croise la géométrie : sur la tête, 0,5 mm pour 1,5 mm d'épaisseur.
- Palier ★ : les molettes en copie liée partagent leur maillage, pas leurs modificateurs. Changer le nombre de crans sur l'une ne change pas les autres.
- Palier ★ : `Alt + D` sur le cran seul, et la copie garde l'ancien *Empty*. Sélectionnez la molette, ses crans et son *Empty* ensemble avant de copier.
- Palier ★ : le *Bevel* de 3 mm du socle adoucit aussi la rainure. C'est voulu ; pour une rainure plus nette, réduisez *Amount*.

**Corrigé :** la collection masquée *Corrigé* ; celui des paliers ★ et des défis ★★ est dans la collection masquée *Corrigé défis*. La lampe terminée existe aussi en fichier séparé, `PRC02_ch2_lampe_modele.blend`, parce que le chapitre 3 en part.

### 3:35 · Galerie, bilan et passerelle vers le chapitre 3 (15 min)

- **Galerie (6 min) :** chaque lampe à l'écran, sous son meilleur angle, en *Solid* avec *Cavity*. Tout le monde fait le tour des postes.
- **Trois questions (4 min) :**
  - « Pourquoi le *Mirror* n'a-t-il rien fait, quand la tige avait été déplacée en Mode Objet ? »
  - « Quel réglage donne son épaisseur à un câble ? »
  - « Que se passe-t-il si l'on déplace la lamelle sans son *Empty* ? »
- **Vérification des acquis (3 min) :** un quiz du chapitre dans l'application, fait ensemble à l'écran. Chacun répond pour soi, puis on commente les erreurs.
- **Passerelle (2 min) :** « Au chapitre 3, chaque pièce reçoit sa matière : un plastique laqué pour la tête, un métal pour les tiges, du verre pour l'ampoule. Vos pièces sont séparées : c'est ce qui rend l'habillage simple. »

## Les quiz prévus dans l'application

Cinq quiz, dans la lignée des quatre du chapitre 1. Chacun vérifie un acquis dont dépend la suite. La règle de l'*Array* (360° divisé par le nombre de copies) est déjà vérifiée en séance : les apprenants trouvent seuls l'angle de la molette. Le parentage l'est par le point de contrôle de la répétition.

| Section | Question | Bonne réponse | Pièges proposés | Ce qu'il garantit pour la suite |
|---|---|---|---|---|
| 1 | La tige a été déplacée en Mode Objet, puis un *Mirror* sur Y lui a été ajouté. Rien ne semble changer : pourquoi ? | Le reflet se fait autour de l'origine de l'objet | Le *Mirror* ne marche qu'en X ; l'échelle n'est pas appliquée ; il faut appliquer le modificateur | Lire l'origine et les axes d'une pièce : le brossé du chapitre 3 suit les axes des bras |
| 1 | L'épaisseur de la coque part vers l'extérieur. Que changer ? | Le signe d'*Offset*, ou les normales | *Thickness* à 0 ; *Fill Rim* ; *Even Thickness* | Distinguer l'intérieur et l'extérieur d'une coque : le chapitre 3 peut y poser deux matières |
| 2 | Quel type de poignée change d'un coup un point de courbe en angle vif ? | *Vector* | *Automatic* ; *Aligned* ; aucun, il faut ajouter un point | Retoucher un profil sans le redessiner : l'ampoule, le câble, les défis |
| 2 | Quel réglage donne une section ronde à une courbe ? | *Bevel* en mode *Round*, avec *Depth* | *Extrude* ; *Offset* ; *Resolution Preview U* | Une courbe sans *Depth* n'a pas de volume : elle ne reçoit pas de matière au chapitre 3 et n'apparaît pas au rendu du chapitre 4 |
| 3 | Quand appliquer les modificateurs de la lampe ? | Le plus tard possible, par exemple pour un export : les matières du chapitre 3 se posent sans les appliquer | Dès que la pièce est finie ; avant d'enregistrer ; avant d'appliquer l'échelle | Le chapitre 3 habille les pièces telles quelles ; le client peut encore demander des retouches |

## Le fil rouge

### La lampe de bureau, du blocage au modèle (retenue)

Le découpage validé et le chapitre 1 l'annoncent : « le blocage sert de gabarit au chapitre 2 ». Le formateur a confirmé la lampe jusqu'au chapitre 4. Les bras passent à deux tiges : c'est une évolution du concept bloqué au chapitre 1, qui n'avait qu'un bras plein, retenue elle aussi.

**Au début du chapitre, l'apprenant a en main :**
- son blocage `lampe_blocage_v001.blend` (chapitre 1), ou le fichier de départ `PRC02_ch2_lampe_depart.blend`, qui ne demande aucun travail préalable ;
- les gestes de l'initiation et du chapitre 1 : Mode Édition, *Extrude*, *Bevel* en outil, la pile de modificateurs, la saisie d'une valeur avec son unité, l'aimantation, l'orientation *Local*, la mesure.

**À la fin du chapitre, il a en main** le fichier `lampe_modele_v001.blend`. C'est le point de départ du chapitre 3 :

| Objet | Type | Modificateurs, de haut en bas | Matière probable au chapitre 3 |
|---|---|---|---|
| *Socle* | Maillage | *Bevel*, *Smooth by Angle* | Métal peint ou plastique lesté |
| *Grille_aeration* et *Grille_pivot* | Maillage, *Empty* enfant | *Array* (*Object Offset*) | Plastique ou métal, d'une autre teinte que le socle |
| *Interrupteur*, *Interrupteur_crans* et *Interrupteur_pivot* | Maillages, *Empty* enfant | *Bevel*, *Smooth by Angle* ; *Array* sur les crans | Plastique |
| *Articulation_bas*, *_milieu*, *_haut* | Maillages | *Bevel*, *Smooth by Angle* | Plastique ou métal |
| *Bras_bas*, *Bras_haut* | Maillages | *Mirror*, *Smooth by Angle* | Métal (chromé ou brossé) |
| *Tête* | Maillage | *Solidify*, *Bevel*, *Smooth by Angle* | Plastique laqué dehors, réflecteur dedans |
| *Douille* | Maillage | *Bevel*, *Smooth by Angle* | Plastique ou céramique |
| *Ampoule* | Courbe | *Screw* | Verre |
| *Câble* | Courbe | Aucun (*Bevel* de la courbe) | Plastique souple |

Le fichier est en millimètres, avec le moteur EEVEE. Il ne contient ni matière ni lumière. La collection *Gabarit* y est masquée. Les molettes des articulations, palier ★, n'y sont pas forcément.

### Le défi ★★ : la liseuse de cabine

Pour ceux qui avancent vite, la même méthode sur un objet des transports : une liseuse à col de cygne, fixée à la paroi au-dessus de l'accoudoir, comme en voiture de première classe ou en cabine d'affaires. Elle réunit toutes les notions du chapitre :
- une platine arrondie (*Bevel*) et ses deux vis (*Mirror*, avec *Mirror Object*) ;
- un bouton moleté (*Array* en couronne) ;
- un col de cygne (courbe de Bézier avec *Depth*) ;
- une tête en coque (*Solidify*) et son diffuseur (profil de Bézier et *Screw*).

Elle a son propre fichier de travail, avec son corrigé dans une collection masquée (fichier 4). Le plan du chapitre 4 la propose comme autre objet à mettre en scène.

### Écarté : le projecteur multisecteur

Un projecteur au choix (phare de tram, phare automobile, phare d'atterrissage) aurait remplacé la lampe. Le formateur ne l'a pas retenu : il rompait avec le chapitre 1, déjà publié, et changeait l'objet des chapitres 3 et 4. Son intérêt, l'ancrage dans le métier de chacun, passe par la liseuse et par les moments « Ailleurs » des démos.

## Les fichiers d'exercice : spécifications de construction

Les fichiers sont construits par la session principale, avec le MCP Blender. Cette partie suffit à les construire.

### Tableau des fichiers et des corrigés

Convention commune aux chapitres 2 à 4 :
- le corrigé de chaque exercice et de l'atelier se trouve dans le fichier de travail, dans une collection masquée (œil fermé) dont le nom commence par « Corrigé » ;
- le LISEZ-MOI dit en une ligne où le trouver ;
- un fichier séparé n'existe que s'il est justifié.

| Exercice ou atelier | Moment | Fichier de travail | Où se trouve le corrigé |
|---|---|---|---|
| Prise en main du fichier | 0:00 | `PRC02_ch2_lampe_depart.blend`, enregistré aussitôt sous `lampe_modele_v001.blend` | Sans objet : pas de production |
| Symétrie : les tiges doubles | 0:10 | `lampe_modele_v001.blend` | Collection masquée *Corrigé* : *Bras_bas_corrige*, *Bras_haut_corrige* |
| Épaisseur : la coque, le lissage, le *Bevel* du socle | 0:35 | `lampe_modele_v001.blend` | Collection masquée *Corrigé* : *Tête_corrige*, *Socle_corrige*, les deux bras. La tête du corrigé porte en plus le *Bevel* de l'atelier |
| Répétition : la grille d'aération et la molette | 1:10 | `lampe_modele_v001.blend` | Collection masquée *Corrigé* : *Grille_aeration_corrige*, *Interrupteur_crans_corrige* et leurs *Empty* |
| Courbes de Bézier : le câble | 1:40 | `lampe_modele_v001.blend` | Collection masquée *Corrigé* : *Câble_corrige* |
| Profil de révolution : l'ampoule | 2:10 | `lampe_modele_v001.blend` | Collection masquée *Corrigé* : *Ampoule_corrige* |
| Atelier : la lampe modélisée | 2:45 | `lampe_modele_v001.blend` | Collection masquée *Corrigé* : toute la lampe. Aussi en fichier séparé, `PRC02_ch2_lampe_modele.blend`. **Raison :** il sert de point de départ et de secours au chapitre 3 (`PRC02_ch3_lampe_a_habiller.blend` en est tiré) |
| Atelier, paliers ★ et défis ★★ sur la lampe | 2:45, pour ceux qui avancent vite | `lampe_modele_v001.blend` | Collection masquée *Corrigé défis*, une sous-collection par palier ou défi |
| Défi ★★ : la liseuse de cabine | 2:45, pour ceux qui avancent vite | `PRC02_ch2_liseuse_depart.blend` | Collection masquée *Corrigé* du même fichier |

- **Un seul fichier de travail pour la lampe.** `lampe_modele_v001.blend` est le fichier de départ enregistré sous le nom de l'apprenant ; il emporte toutes les collections de corrigé. Un apprenant en retard y prend la pièce qui lui manque : il supprime sa propre version s'il en a une, fait `M` vers *Lampe*, puis renomme la pièce sans `_corrige`. Une pièce qui a un *Empty* se déplace avec lui.
- **Les paliers ★ des séquences** (30 crans, comparer les *Steps*…) ne changent que des valeurs : ils n'ont pas de corrigé à part.
- **Aucun autre fichier séparé.** Tous les résultats du chapitre tiennent dans une collection : pas de réglage de rendu, de monde ni d'image exportée à montrer.
- **Hors tableau :** `croquis_ampoule_profil.png` (fichier 3) est une ressource du fichier de départ. `PRC02_ch2_demos_secteurs.blend` (fichier 5) sert aux démos du formateur ; ce n'est pas un exercice, et il s'ouvre déjà sur ses résultats.

### Conventions communes

- Blender 5.2 LTS. Construction en arrière-plan (`blender.exe -b --factory-startup`) ou par le MCP Blender, sans toucher au fichier ouvert par le formateur.
- Scène : *Unit System* Metric, *Length* Millimeters, *Unit Scale* 1,0 ; moteur EEVEE (`BLENDER_EEVEE`). Les dimensions ci-dessous sont en **mètres** (unités internes). Les LISEZ-MOI les donnent en millimètres, l'unité affichée.
- Ressources empaquetées, chemins relatifs, aucun chemin absolu caché (voir la note de passation sur `ImagePackedFile.filepath`), aucun texte d'extension (*Geo-Scatter*). `preferences.filepaths.save_version = 0` avant d'enregistrer, pour éviter le `.blend1`.
- Source du gabarit : la collection *Variante A* de `_resources/exercices/PRC02_ch1_blocage_lampe.blend`, lue sans être modifiée. Les fichiers déjà livrés (Basics, initiation, chapitre 1) ne sont pas retouchés.
- Un texte LISEZ-MOI s'ouvre en bas de l'écran, comme dans les fichiers de l'initiation (`finish_ui.py`).
- Scripts rejouables dans `tool/exercices_ch2/`. Le même script construit la lampe du corrigé pour le fichier 1 (noms suffixés) et pour le fichier 2 (noms simples).
- **Ordre de construction :** le fichier 3 (le croquis, empaqueté dans le fichier 1), puis 1, 2 et 4. Le fichier 5 vient en dernier : c'est aussi le premier élément coupé en cas de retard.

### Fichier 1 · `PRC02_ch2_lampe_depart.blend`

**Moment :** toute la demi-journée. C'est le fichier de travail, enregistré par chaque apprenant sous `lampe_modele_v001.blend` dès le lancement. C'est aussi le fichier de départ propre : il ne demande pas le travail du chapitre 1. Il porte les corrigés de toutes les séquences, de l'atelier et des défis sur la lampe.

**Collections, dans l'ordre de l'Outliner :**

| Collection | État à l'ouverture | Contenu |
|---|---|---|
| *Gabarit* | Visible, objets non sélectionnables (`hide_select`), affichés en fil de fer (*Display As* *Wire*) | Les 8 objets de la variante A, noms d'origine : *Socle_A*, *Interrupteur_A*, *Articulation_bas_A*, *Bras_bas_A*, *Articulation_milieu_A*, *Bras_haut_A*, *Articulation_haut_A*, *Tête_A* |
| *Lampe* | Visible, sélectionnable | Les copies de travail, maillages indépendants, affichage normal : *Socle*, *Interrupteur*, *Articulation_bas*, *Articulation_milieu*, *Articulation_haut*, *Bras_bas*, *Bras_haut*, *Tête*. Aucun modificateur |
| *Croquis* | Visible | *Croquis_face* et *Croquis_profil*, repris du chapitre 1 ; *Croquis_ampoule* et *Repere_ampoule* (ci-dessous) |
| *Corrigé* | Œil fermé, repliée | La lampe terminée (tableau du fichier 2), à la même place que la copie de travail, chaque nom suffixé `_corrige` : *Socle_corrige*, *Grille_aeration_corrige*… |
| *Corrigé défis* | Œil fermé, repliée | Les paliers ★ de l'atelier et cinq défis ★★, une sous-collection chacun, à côté de la lampe (ci-dessous) |

**Les objets de la variante A** (repris tels quels, échelle 1, sans modificateur) :

| Objet | Forme | Dimensions (m) | Position (m) | Rotation |
|---|---|---|---|---|
| *Socle_A* | Cylindre, 32 côtés | Ø 0.180 × 0.025 | (0, 0, 0.0125) | 0 |
| *Interrupteur_A* | Cylindre, 16 côtés | Ø 0.016 × 0.006 | (0.055, 0, 0.028) | 0 |
| *Articulation_bas_A* | Sphère UV | Ø 0.030 | (-0.040, 0, 0.040) | 0 |
| *Bras_bas_A* | Cylindre, 16 côtés | Ø 0.016 × 0.2596 | (-0.005, 0, 0.165) | Y 15,64° (0.273 rad) |
| *Articulation_milieu_A* | Sphère UV | Ø 0.028 | (0.030, 0, 0.290) | 0 |
| *Bras_haut_A* | Cylindre, 16 côtés | Ø 0.014 × 0.2202 | (0.115, 0, 0.360) | Y 50,53° (0.882 rad) |
| *Articulation_haut_A* | Sphère UV | Ø 0.024 | (0.200, 0, 0.430) | 0 |
| *Tête_A* | Tronc de cône, 24 côtés, fermé | Ø 0.120 (z local -0.055) à Ø 0.044 (z local +0.055), longueur 0.110 | (0.2335, 0, 0.372) | Y -30° |

Les copies de *Lampe* ont exactement les mêmes formes, positions et rotations.

**Les repères de l'ampoule :**
- *Croquis_ampoule* : *Empty* image (*Reference*), image `croquis_ampoule_profil.png` empaquetée. Position (0.500, 0, 0.040), rotation X 90° (face à la vue de face), *Size* 0.120. *Opacity* 0,5 ; *Depth* *Back* ; *Show In* *Orthographic* et *Only Axis Aligned*, comme les croquis du chapitre 1.
- *Repere_ampoule* : *Empty* *Plain Axes*, taille 0.010, position (0.500, 0, 0). Il marque la base de l'axe de révolution.

**Vue d'ouverture :** espace *Layout*. Vue 3D en perspective, trois quarts avant droit, un peu en hauteur : toute la lampe et le repère de l'ampoule sont cadrés (direction de visée de (0.75, -0.95, 0.55) vers (0.15, 0, 0.21) environ). Mode *Solid* : *Lighting* *Studio*, *Color* *Random*, *Cavity* activé. *Clip Start* de la vue à 1 mm. Outliner : *Gabarit*, *Lampe* et *Croquis* dépliées ; *Corrigé* et *Corrigé défis* repliées. Éditeur de propriétés sur l'onglet *Modifiers*, *Bras_bas* actif. Texte LISEZ-MOI en bas.

#### La collection *Corrigé défis*

**Moment :** l'atelier, pour ceux qui avancent vite. Le formateur l'ouvre aussi pour anticiper les questions des paliers ★ et des défis ★★.

**Construction :**
- Six sous-collections, chacune une copie complète de la lampe du fichier 2 (*Duplicate Collection*).
- Les copies sont disposées en deux rangées, à côté de la lampe de travail, espacées de 0.8 m.
- Chaque copie porte le suffixe de son défi, pour éviter les `.001` : `_paliers`, `_chape`, `_tulipe`, `_ressorts`, `_percage`, `_grille_tete` (`Socle_paliers`, `Bras_bas_ressorts`…).
- Les pièces ajoutées portent le suffixe `_corrige`, pour qu'un apprenant qui les crée garde un nom simple : *Molette_bas_corrige*…, *Chape_corrige*, *Tête_tulipe_corrige*, *Ressort_corrige*, *Grille_tete_corrige*.
- Ces pièces sont en orange (*Object Color* #E8913A), le reste en gris clair (#C8C8C8).

| Sous-collection | Décalage (m) | Ce qui change, en coordonnées de la lampe avant décalage |
|---|---|---|
| *Paliers* (★) | (0.8, 0, 0) | **Molettes :** trois copies liées de *Interrupteur*, *Interrupteur_crans* et *Interrupteur_pivot*, sélectionnés ensemble puis `Alt + D` (vérifié : l'*Array* et le parent suivent la copie). Chaque jeu tourne de X -90° et se centre sur la face +Y d'une articulation : (-0.040, 0.021, 0.040), (0.030, 0.021, 0.290), (0.200, 0.021, 0.430). Noms : *Molette_bas_corrige*, *_milieu*, *_haut*, avec leurs crans et leur pivot. **Rainure :** sur le flanc du socle, deux boucles à z = 0.0115 et 0.0135, la bande entre elles extrudée de 0.001 vers l'axe. **Sous-collections :** *Pied* (*Socle*, la grille, l'interrupteur et ses crans, *Câble*), *Bras* (les articulations, leurs molettes, *Bras_bas*, *Bras_haut*), *Tête* (*Tête*, *Douille*, *Ampoule*) |
| *Chape* (★★) | (1.6, 0, 0) | *Chape_corrige* : un profil en L dans le plan YZ, points (y ; z) relatifs à l'origine : (0 ; 0.0165), (0.021 ; 0.0165), (0.021 ; -0.003), (0.018 ; -0.003), (0.018 ; 0.0135), (0 ; 0.0135), extrudé en X de -0.013 à 0.013. Origine au centre d'*Articulation_haut*, (0.200, 0, 0.430). *Mirror* Y avec *Clipping* et *Bisect* ; *Bevel* (0.0005, 2) ; *Smooth by Angle*. Une chape en U renversé coiffe l'articulation ; elle ne touche ni la tête ni les tiges |
| *Tulipe* (★★) | (2.4, 0, 0) | *Tête* supprimée. *Tête_tulipe_corrige* : courbe de Bézier à l'origine et à la rotation de la tête. Points (local) : (0, 0, 0.055) *Vector* ; (0.022, 0, 0.055) *Vector* ; (0.026, 0, 0.025) *Automatic* ; (0.050, 0, -0.025) *Automatic* ; (0.064, 0, -0.055) *Vector*. *Screw* (Z, 32, *Merge Distance* 0.0001) ; *Solidify* (0.0015, -1, *Even*) ; *Smooth by Angle*. L'épaisseur part bien vers l'intérieur (vérifié : rayon extérieur maximal 64 mm). Douille et ampoule restent en place |
| *Ressorts* (★★) | (0.8, 0.8, 0) | *Ressort_corrige* : cercle de Bézier de 4 points *Automatic*, rayon 0.00075, dans le plan XZ, centré en (0.005, 0, 0). Origine (-0.0179, 0.025, 0.1188), rotation Y 15,64°, le long de *Bras_bas*. *Screw* (*Axis* Z, *Angle* 360°, *Screw* 0.006, *Iterations* 16, *Steps* 16) ; *Mirror* Y, *Mirror Object* *Bras_bas_ressorts*. Deux ressorts de 97 mm, Ø 11,5 mm, de part et d'autre des tiges, sans les toucher |
| *Perçage* (★★) | (1.6, 0.8, 0) | La lamelle de *Grille_aeration_percage* prolongée en Z : 0.006 de haut, de z = 0.022 à 0.028. *Display As* *Wire*, désactivée au rendu. Sur *Socle_percage* : *Boolean*, *Difference*, objet *Grille_aeration_percage*, *Solver* *Exact* (réglage d'usine). Il se range entre *Bevel* et *Smooth by Angle*. Résultat vérifié : 36 fentes de 3 mm de profondeur |
| *Grille tête* (★★) | (2.4, 0.8, 0) | *Grille_tete_corrige* : origine et rotation de la tête ; une lamelle de 0.0015 × 0.0015 × 0.012, tournée de -19,07° autour de Y local (la pente du cône), centrée en (0.0306, 0, 0.030) local, à moitié enfoncée dans le flanc. *Grille_tete_pivot_corrige* : *Empty* enfant, rotation locale Z 15°. *Array* : *Object Offset*, *Count* 24. La couronne suit l'axe incliné de la tête, loin de l'articulation et des tiges |

**Points à connaître :**
- La molette du haut et la chape occupent la même place : un apprenant choisit l'une ou l'autre.
- Le *Boolean* utilise la couronne calculée par l'*Array* : changer le nombre de lamelles change le nombre de fentes.
- Pour voir un défi : œil de *Corrigé défis* ouvert, puis sélection d'une pièce et touche `.` du pavé numérique pour la cadrer.

### Fichier 2 · Le corrigé, et `PRC02_ch2_lampe_modele.blend` (fichier séparé, départ du chapitre 3)

**Moment :** le corrigé sert au lancement, à chaque point de contrôle et à l'atelier, dans la collection *Corrigé* du fichier 1. Le même contenu, sans suffixe, forme `PRC02_ch2_lampe_modele.blend`. **Raison d'un fichier séparé :** c'est le point de départ et le fichier de secours du chapitre 3, dont le fichier `PRC02_ch3_lampe_a_habiller.blend` est tiré.

| Objet | Construction | Dimensions et position (m) | Modificateurs, de haut en bas |
|---|---|---|---|
| *Socle* | Copie de *Socle_A* | Comme *Socle_A* | *Bevel* (*Amount* 0.003, soit `width` en Python, *Segments* 3, *Limit Method* *Angle* 30°) ; *Smooth by Angle* (par *Shade Auto Smooth*) |
| *Grille_aeration* | Cube de 0.002, mis à l'échelle X 6 en Mode Édition : lamelle de 0.012 × 0.002 × 0.002, centrée en (0.076, 0, 0.025) par rapport à l'origine | Origine en (0, 0, 0) | *Array* : *Relative Offset* décoché, *Object Offset* *Grille_pivot*, *Count* 36 |
| *Grille_pivot* | *Empty* *Plain Axes*, taille 0.010 | (0, 0, 0), rotation Z 10°, enfant de *Grille_aeration* | |
| *Interrupteur* | Copie d'*Interrupteur_A* | Comme *Interrupteur_A* | *Bevel* (0.0005, 2, *Angle*) ; *Smooth by Angle* |
| *Interrupteur_crans* | Cran de 0.0015 × 0.0015 × 0.006, centré en (0.008, 0, 0) par rapport à l'origine | Origine en (0.055, 0, 0.028) | *Array* : *Object Offset* *Interrupteur_pivot*, *Count* 24 |
| *Interrupteur_pivot* | *Empty* *Plain Axes*, taille 0.005 | (0.055, 0, 0.028), rotation Z 15°, enfant d'*Interrupteur_crans* | |
| *Articulation_bas* | Cylindre, 32 côtés, Ø 0.030 × 0.036 | (-0.040, 0, 0.040), rotation X 90° | *Bevel* (0.002, 2, *Angle*) ; *Smooth by Angle* |
| *Articulation_milieu* | Cylindre, 32 côtés, Ø 0.028 × 0.036 | (0.030, 0, 0.290), rotation X 90° | Idem |
| *Articulation_haut* | Cylindre, 32 côtés, Ø 0.024 × 0.036 | (0.200, 0, 0.430), rotation X 90° | Idem |
| *Bras_bas* | Copie de *Bras_bas_A* ; en Mode Édition, X et Y × 0.5 (Ø 0.008), puis Y + 0.010 | Position et rotation de *Bras_bas_A* | *Mirror* (axe Y seul) ; *Smooth by Angle* |
| *Bras_haut* | Copie de *Bras_haut_A* ; X et Y × 0.5 (Ø 0.007), puis Y + 0.010 | Position et rotation de *Bras_haut_A* | Idem |
| *Tête* | Copie de *Tête_A*, grande face (z local -0.055) supprimée | Comme *Tête_A* | *Solidify* (*Thickness* 0.0015, *Offset* -1, *Even Thickness*) ; *Bevel* (0.0005, 2, *Angle*) ; *Smooth by Angle* |
| *Douille* | Cylindre, 32 côtés, Ø 0.030 × 0.020 | (0.2110, 0, 0.4110), rotation Y -30° (à 0.045 du centre de la tête, sur son axe, vers le fond) | *Bevel* (0.001, 2, *Angle*) ; *Smooth by Angle* |
| *Ampoule* | Courbe 3D, une spline de Bézier. Points (repère local, m) : 1 (0, 0, 0) *Vector* ; 2 (0.0135, 0, 0.004) *Vector* ; 3 (0.0135, 0, 0.025) *Vector* ; 4 (0.025, 0, 0.055) *Automatic* ; 5 (0, 0, 0.080) *Aligned*, poignées horizontales en (±0.012, 0, 0.080) | Origine en (0.2110, 0, 0.4110), rotation Y 150° | *Screw* (*Axis* Z, *Angle* 360°, *Steps* et *Render Steps* 32, *Merge Vertices*, *Merge Distance* 0.0001) |
| *Câble* | Courbe 3D, une spline de Bézier. Points : (-0.0895, 0, 0.010), (-0.140, 0.004, 0.0025), (-0.200, 0.050, 0.0025), (-0.265, 0.030, 0.0025), (-0.330, -0.020, 0.0025). Poignées *Aligned* : la première horizontale selon -X, les autres horizontales (même z que leur point) | Origine en (0, 0, 0) | Aucun. *Geometry* : *Bevel* *Round*, *Depth* 0.0025, *Resolution* 4, *Fill Caps* ; *Shape* : *Resolution Preview U* 24 |

**L'ordre des piles :** *Smooth by Angle* est épinglé en dernière position (*Pin to Last*, posé par *Shade Auto Smooth*). Un *Bevel* ajouté après lui se range au-dessus de lui : c'est vérifié dans Blender 5.2.1.

**Contrôles faits sur le prototype :** aucune interpénétration visible. Les lamelles (rayon 0.070 à 0.082) passent à côté de l'interrupteur (rayon 0.047 à 0.063). Le câble repose sur la table (point le plus bas à z = 0.00001). L'ampoule reste à 45 mm en retrait de l'ouverture de la tête. Avec la *Merge Distance* d'usine (0.01), le sommet de l'ampoule s'aplatit : il faut 0.0001. Quelques contacts sont voulus et restent cachés :
- la douille traverse le fond de la coque sur 1,5 mm, là où elle est fixée ;
- le culot de l'ampoule entre dans la douille ;
- le premier point du câble entre dans le socle ;
- les lamelles et les crans sont à moitié enfoncés ;
- les tiges des bras se rejoignent dans les articulations.

**`PRC02_ch2_lampe_modele.blend` :** collections *Lampe* (les objets ci-dessus, sans suffixe), *Gabarit* (œil fermé) et *Croquis* (œil fermé). Ni *Corrigé* ni *Corrigé défis*. Vue d'ouverture : celle du fichier 1, en *Solid*, *Color* *Object*, *Cavity* activé. LISEZ-MOI court : « La lampe modélisée au chapitre 2 : le corrigé de l'atelier, et le point de départ du chapitre 3. Les modificateurs sont actifs : ne les appliquez pas. »

### Fichier 3 · `croquis_ampoule_profil.png`

**Moment :** profil de l'ampoule (2:10). Empaqueté dans le fichier 1.

- 1200 × 1200 px, fond blanc. Échelle : 10 px par millimètre.
- L'axe de révolution, en trait mixte rouge, sur la colonne x = 600, de z = -10 à z = +90 mm. La base de l'ampoule (z = 0) se trouve à la ligne y = 1000 depuis le haut ; le centre de l'image correspond donc à z = 40 mm, ce qui place l'axe sur x = 0.500 m dans la scène.
- Le demi-profil droit en trait noir de 4 px, d'après les points du corrigé (rayon et hauteur en mm) : 1 (0, 0), 2 (13,5 ; 4), 3 (13,5 ; 25), 4 (25 ; 55), 5 (0 ; 80). La moitié gauche en gris clair pointillé, pour l'allure.
- Les points numérotés 1 à 5 en pastilles. Deux cotes : Ø 50 et 80.
- Production possible : un rendu Freestyle, comme les croquis du chapitre 1, ou un SVG exporté en PNG par Edge sans interface, comme le mémo de navigation.

### Fichier 4 · `PRC02_ch2_liseuse_depart.blend` (défi ★★)

**Moment :** l'atelier (2:45), pour ceux qui ont fini le socle et les paliers ★. Mêmes réglages de scène que le fichier 1. Le corrigé est dans la collection masquée *Corrigé* du même fichier.

**Repère :** la paroi de la cabine est le plan y = 0 ; la cabine est du côté des y négatifs ; z monte.

| Collection | État à l'ouverture | Objets |
|---|---|---|
| *Contexte* | Visible, non sélectionnable, affichage normal | *Paroi* : plan de 0.50 × 0.40, centre (0, 0, 0.20), rotation X 90°. *Accoudoir* : pavé de 0.50 × 0.15 × 0.05 (X × Y × Z), centre (0, -0.075, 0.025) |
| *Gabarit_liseuse* | Visible, fil de fer, non sélectionnable | *Platine_G*, *Bouton_G* et *Tête_G* : mêmes formes et positions que les copies de travail ci-dessous. *Col_G* : la courbe du col de cygne du corrigé, sans épaisseur |
| *Liseuse* | Visible, sélectionnable | Copies de travail, sans modificateur : *Platine* (pavé de 0.070 × 0.008 × 0.040, centre (0, -0.004, 0.150)) ; *Bouton* (cylindre de 32 côtés, Ø 0.010 × 0.004, centre (0.020, -0.010, 0.140), rotation X 90°) ; *Tête_liseuse* (cône fermé de 32 côtés : rayon 0.020 en bas, 0.012 en haut, hauteur 0.045 ; centre (0, -0.2635, 0.167), rotation X -36,87°). Deux repères *Plain Axes* de taille 0.005 : *Repere_col* en (0, -0.004, 0.150), départ du col, et *Repere_diffuseur* en (0.150, -0.200, 0.300), un endroit libre pour dessiner le profil du diffuseur |
| *Corrigé* | Œil fermé, repliée | La liseuse terminée (tableau ci-dessous), à la même place, chaque nom suffixé `_corrige` |

**Le corrigé de la liseuse :**

| Objet | Construction | Position (m) | Modificateurs, de haut en bas |
|---|---|---|---|
| *Platine_corrige* | Pavé de 0.070 × 0.008 × 0.040 | (0, -0.004, 0.150) | *Bevel* (0.002, 2, *Angle*) ; *Smooth by Angle* |
| *Vis_corrige* | Cylindre de 16 côtés, Ø 0.005 × 0.002 | (0.027, -0.009, 0.160), rotation X 90° | *Mirror* (X seul, *Mirror Object* *Platine_corrige*) ; *Smooth by Angle* |
| *Bouton_corrige* | Cylindre de 32 côtés, Ø 0.010 × 0.004 | (0.020, -0.010, 0.140), rotation X 90° | *Bevel* (0.0003, 2, *Angle*) ; *Smooth by Angle* |
| *Bouton_crans_corrige* | Cran de 0.001 × 0.004 × 0.001 (X × Y × Z), centré en (0.005, 0, 0) par rapport à l'origine | Origine (0.020, -0.010, 0.140), rotation 0 | *Array* : *Object Offset* *Bouton_pivot_corrige*, *Count* 16 |
| *Bouton_pivot_corrige* | *Empty* *Plain Axes*, taille 0.004 | (0.020, -0.010, 0.140), rotation Y 22,5°, enfant de *Bouton_crans_corrige* | |
| *Col_de_cygne_corrige* | Courbe 3D, une spline de Bézier. Points : 1 (0, -0.004, 0.150) *Aligned*, poignées (0, 0.010, 0.150) et (0, -0.040, 0.150) ; 2 (0, -0.090, 0.215) *Automatic* ; 3 (0, -0.180, 0.225) *Automatic* ; 4 (0, -0.250, 0.185) *Aligned*, poignées (0, -0.226, 0.217) et (0, -0.262, 0.169) | Origine (0, 0, 0) | Aucun. *Bevel* *Round*, *Depth* 0.004, *Resolution* 4, *Fill Caps* ; *Resolution Preview U* 24 |
| *Tête_liseuse_corrige* | Cône de 32 côtés : rayon 0.020 en bas (z local -0.0225), 0.012 en haut ; grande face supprimée | (0, -0.2635, 0.167), rotation X -36,87° : l'ouverture regarde vers l'accoudoir, dans l'axe de la fin du col | *Solidify* (0.0015, *Offset* -1, *Even Thickness*) ; *Smooth by Angle* |
| *Diffuseur_corrige* | Courbe 3D, une spline de Bézier. Points (repère local) : 1 (0, 0, 0) *Vector* ; 2 (0.0175, 0, 0) *Vector* ; 3 (0, 0, -0.004) *Aligned*, poignées (±0.010, 0, -0.004) | (0, -0.2761, 0.1502), rotation X -36,87° | *Screw* (*Axis* Z, *Steps* et *Render Steps* 32, *Merge Vertices*, *Merge Distance* 0.0001) |

**Contrôles faits sur le prototype :** aucune interpénétration. Contacts voulus : le col entre dans la platine et aboutit au dos de la tête ; les vis et le bouton sont posés sur la face avant de la platine. Le diffuseur (rayon 17,5 mm) reste dans l'ouverture (rayon intérieur 18,2 mm à cette hauteur). Le bord de la tête passe à 87 mm au-dessus de l'accoudoir.

**Vue d'ouverture :** perspective, œil (0.30, -0.55, 0.32), cible (0, -0.13, 0.17). *Solid*, *Color* *Random*, *Cavity*. *Platine* active, onglet *Modifiers*. LISEZ-MOI en bas :

```
LISEZ-MOI · Défi ★★ · La liseuse de cabine
Une liseuse à col de cygne, fixée à la paroi au-dessus de l'accoudoir.
Même méthode que la lampe : chaque volume du gabarit devient une pièce propre.
Valeurs indicatives. N'appliquez aucun modificateur.
Corrigé : collection « Corrigé », masquée (œil fermé dans l'Outliner).
D'abord : File > Save As, sous liseuse_modele_v001.blend.

1. Platine : Bevel (Amount 2 mm, Segments 2), puis Shade Auto Smooth.
2. Vis : Add > Mesh > Cylinder (Vertices 16, Radius 2.5 mm, Depth 2 mm), R X 90.
   N > Item : Location 27, -9, 160 mm. Mirror : axe X seul, Mirror Object = Platine.
3. Bouton : 16 crans de 1 x 4 x 1 mm, à 5 mm de l'axe. Le bouton est couché :
   l'Empty tourne autour de Y. De combien ?
4. Col de cygne : Cursor to Selected sur Repere_col. Add > Curve > Bézier, Tab,
   supprimez un point, Selection to Cursor sur l'autre. Vue de droite (3), Curve Pen :
   3 points jusqu'au dos de la tête. Geometry > Bevel : Round, Depth 4 mm, Fill Caps.
5. Tête_liseuse : X > Faces sur la grande face, Solidify 1.5 mm, Shade Auto Smooth.
6. Diffuseur : sur Repere_diffuseur, comme l'ampoule, un demi-profil en vue de face :
   l'axe, le bord à 17.5 mm, un dôme de 4 mm. Screw : Axis Z, Merge Distance 0.1 mm.
   N > Item : Location 0, -276.1, 150.2 mm ; Rotation X -36.87°.
Contrôle : le col part de la platine et entre dans le dos de la tête ;
rien ne traverse la paroi ni l'accoudoir. Ctrl + S.
```

### Fichier 5 · `PRC02_ch2_demos_secteurs.blend` (léger)

**Moment :** les moments « Ailleurs » des démos (1 minute chacun). Poste du formateur seulement ; il sert aussi à certaines figures. Ce n'est pas un exercice : il s'ouvre déjà sur ses résultats et n'a pas de corrigé. Il reste léger : des formes simples, sans détail ni matière. C'est le premier élément coupé en cas de retard.

| Collection | Contenu | Dimensions indicatives (m) |
|---|---|---|
| *Auto_capot* | Une moitié de capot (plan subdivisé et galbé), avec *Mirror* X, *Clipping* et *Bisect* | 1.2 × 0.9 |
| *Aero_soufflante* | Un moyeu, une aube et un *Empty* : *Array* en couronne de 18 aubes | Ø 1.2 |
| *Ferro_main_courante* | Deux poteaux et une main courante de tram en courbe de Bézier, *Bevel* *Depth* 0.016 | 1.5 de long, Ø 0.032 |
| *Ferro_roue* | Le demi-profil d'une roue ferroviaire (bandage, boudin, toile) en Bézier, avec *Screw* | Ø 0.84 |

Les quatre collections sont alignées sur X, espacées de 2 m. Vue d'ouverture : la première collection, en *Solid* avec *Cavity*.

### Le LISEZ-MOI du fichier 1 : consignes par paliers

Texte destiné aux apprenants, en millimètres. Une partie par séquence ; chaque partie a un socle, un palier ★ et un contrôle.

```
LISEZ-MOI · Chapitre 2 · Du blocage au modèle
Les valeurs sont indicatives : adaptez-les à votre concept.
Ctrl + Espace agrandit ce texte. Règle du jour : n'appliquez aucun modificateur.
D'abord : File > Save As, sous lampe_modele_v001.blend. Puis Ctrl + S à chaque contrôle.

0 · REPÈRES
Gabarit : le blocage, en fil de fer. Lampe : vos pièces.
Corrigé : collection « Corrigé », masquée (œil fermé) ; défis : « Corrigé défis ».
Une pièce vous manque ? Prenez-la dans « Corrigé » : M vers Lampe, puis renommez-la.

1 · SYMÉTRIE (Bras_bas, Bras_haut)
1. Bras_bas : Tab, A, S Maj+Z 0.5, G Y = 10mm, Tab.
2. Modifiers > Add Modifier > Generate > Mirror : décochez X, cochez Y.
3. Bras_haut : Tab, A, S Maj+Z 0.5, G Y = 10mm, Tab. Puis Bras_haut sélectionné,
   Bras_bas actif : menu du Mirror > Copy to Selected.
★ Sur une copie, G Y = 10mm en Mode Objet : que fait le Mirror ? Réglez Mirror Object sur Socle.
Contrôle : vue de dessus (7), deux tiges par bras.

2 · ÉPAISSEUR (Tête, Socle, Bras)
1. Tête : Tab, 3, clic sur la grande face de l'ouverture, X > Faces, Tab.
2. Add Modifier > Generate > Solidify : Thickness 1.5 mm, Offset -1, Even Thickness.
3. Object > Shade Auto Smooth.
4. À vous, sur Socle : Add Modifier > Generate > Bevel.
   Amount 3 mm, Segments 3, Limit Method Angle (déjà réglé). Puis Shade Auto Smooth.
5. Bras_bas et Bras_haut, sélectionnés ensemble : Object > Shade Auto Smooth.
★ Offset à 1, puis -1 ; Thickness 1 mm, puis 3 mm.
  Tête : Bevel (Amount 0.5 mm, Segments 2), prévu à l'atelier.
Contrôle : pile de la tête = Solidify, Smooth by Angle ;
pile du socle = Bevel, Smooth by Angle.

3 · RÉPÉTITION (grille d'aération, interrupteur)
1. Maj + C. Add > Mesh > Cube, F9 : Size 2 mm. Renommez : Grille_aeration.
2. Tab, S X 6, G X = 76mm, G Z = 25mm, Tab.
3. Add > Empty > Plain Axes, R Z 10. Renommez : Grille_pivot.
4. Grille_aeration : Add Modifier > Generate > Array (Legacy).
   Décochez Relative Offset, cochez Object Offset > Grille_pivot. Count 36.
5. Clic sur Grille_pivot, Maj + clic sur Grille_aeration, Ctrl + P > Object.
6. À vous : Interrupteur devient une molette de 24 crans (1,5 x 1,5 x 6 mm, à 8 mm de l'axe).
   Nommez Interrupteur_crans et Interrupteur_pivot. Quelle rotation pour l'Empty ?
★ 30 crans ; une demi-couronne de lamelles à l'arrière du socle.
Contrôle : déplacez Grille_aeration, la couronne suit. Ctrl + Z.

4 · LE CÂBLE
1. Vue de dessus (7). Add > Curve > Bézier, F9 : Radius 50 mm. Renommez : Câble.
2. Tab. E sur un point d'extrémité, ou Ctrl + clic droit : 4 à 5 points,
   de l'arrière du socle vers le bord de la table. V : Vector ou Automatic.
3. Object Data > Geometry > Bevel : Round, Depth 2.5 mm, Fill Caps.
4. Aimantation Face : le premier point contre le flanc du socle.
5. À vous : retracez le câble avec l'outil Curve Pen, avec une boucle.
★ Shape > Resolution Preview U à 24.
Contrôle : vue de face (1), le câble repose sur la table.

5 · L'AMPOULE
1. Clic sur Repere_ampoule, Maj + S > Cursor to Selected.
2. Add > Curve > Bézier. Renommez : Ampoule. Tab. X > Vertices sur le point de droite.
   Point restant : Maj + S > Selection to Cursor, puis V > Vector.
3. Vue de face (1), outil Curve Pen : clic sur les points 2 et 3,
   cliquer-glisser vertical sur le point 4, cliquer-glisser horizontal sur le point 5.
4. Tab. Add Modifier > Generate > Screw : Axis Z, Steps 32,
   Merge Vertices coché, Merge Distance 0.1 mm.
5. N > Item : Location 211, 0, 411 mm ; Rotation Y 150°.
★ Retouchez une poignée : l'ampoule suit. Comparez Steps 16 et 48.
Contrôle : une ampoule lisse et fermée, au fond de la tête.

6 · ATELIER
1. Articulations : Cursor to Selected sur chaque sphère, X pour la supprimer,
   Add > Mesh > Cylinder (F9 : Vertices 32, Radius 15, 14 ou 12 mm, Depth 36 mm),
   R X 90. Bevel (2 mm, 2 segments, Angle) et Shade Auto Smooth. Renommez.
2. Douille : Cursor to Selected sur Tête, Add > Mesh > Cylinder
   (F9 : Radius 15 mm, Depth 20 mm, Rotation Y -30°), puis G Z Z = 45mm (le long de son axe).
   Bevel (1 mm, 2 segments) et Shade Auto Smooth.
3. Tête : Bevel (Amount 0.5 mm, Segments 2). Il se range au-dessus de Smooth by Angle.
4. Interrupteur : Bevel (Amount 0.5 mm, Segments 2) et Shade Auto Smooth.
5. Checklist : noms clairs ; échelles à 1 ; aucune face rouge (Face Orientation) ;
   modificateurs actifs ; silhouette conforme au gabarit (vues 1 et 3).
6. Masquez Gabarit. Ctrl + S : lampe_modele_v001.blend.
★ Molettes sur les articulations (Alt + D de la molette, de ses crans et de son Empty) ;
  rainure du socle ; sous-collections Pied, Bras, Tête.
★★ Voir les défis du chapitre dans l'application ; solutions dans « Corrigé défis ».
   La liseuse a son propre fichier, avec son corrigé.
```

## Les captures Blender à prévoir

Une capture par menu, bouton ou panneau cité. Les figures sont numérotées « Figure 2.N » sur tout le chapitre. La disposition suit les tailles lisibles dans l'application : environ 600 × 400 px pour le côte à côte ; pleine largeur pour les captures larges ou riches en texte.

| N° | Section | Sujet | Disposition | Fichier prévu |
|---|---|---|---|---|
| 2.1 | 1 | Le gabarit en fil de fer et la copie de travail en volume | Pleine largeur | `gabarit_wire_lamp_blender.jpg` |
| 2.2 | 1 | Le menu *Add Modifier*, sous-menu *Generate* ouvert | Côte à côte | `add_modifier_generate_menu_blender.jpg` |
| 2.3 | 1 | Le menu de l'en-tête d'un modificateur : *Apply*, *Duplicate*, *Copy to Selected*, *Move to First*, *Move to Last* | Côte à côte | `modifier_header_menu_blender.jpg` |
| 2.4 | 1 | Le panneau *Mirror* : axes, *Bisect*, *Flip*, *Mirror Object*, *Clipping*, *Merge* | Côte à côte | `mirror_modifier_panel_blender.jpg` |
| 2.5 | 1 | Les tiges doubles, et le piège de l'origine (avant et après) | Pleine largeur | `mirror_arm_rods_blender.jpg` |
| 2.6 | 1 | *Clipping* et *Bisect* sur une moitié de capot (survolé) | Côte à côte | `mirror_clipping_bisect_blender.jpg` |
| 2.7 | 1 | Le menu *Delete* (`X`) en Mode Édition, sur *Faces* | Côte à côte | `delete_menu_faces_blender.jpg` |
| 2.8 | 1 | Le panneau *Solidify* : *Thickness*, *Offset*, *Even Thickness*, *Fill Rim* | Côte à côte | `solidify_modifier_panel_blender.jpg` |
| 2.9 | 1 | La coque de la tête, vue de dessous : l'épaisseur du bord | Côte à côte | `solidify_lamp_head_blender.jpg` |
| 2.10 | 1 | Le panneau *Bevel* : *Amount*, *Segments*, *Limit Method* sur *Angle* (la figure de la découverte en autonomie) | Côte à côte | `bevel_modifier_angle_blender.jpg` |
| 2.11 | 1 | Le menu *Object* avec *Shade Auto Smooth* | Côte à côte | `object_menu_shade_auto_smooth_blender.jpg` |
| 2.12 | 1 | La pile de la tête : *Solidify*, *Bevel*, *Smooth by Angle* et l'épingle de son en-tête ; facettes avant, lisse après | Pleine largeur | `modifier_stack_head_blender.jpg` |
| 2.13 | 1 | Le menu *Add > Empty* | Côte à côte | `add_empty_menu_blender.jpg` |
| 2.14 | 1 | Le panneau du modificateur ajouté par *Array (Legacy)*, nommé *Array* dans la pile : *Relative Offset* décoché, *Object Offset* sur l'*Empty*, *Count* | Côte à côte | `array_object_offset_panel_blender.jpg` |
| 2.15 | 1 | La grille d'aération en couronne sur le socle, et son *Empty* tourné de 10° | Côte à côte | `radial_array_vent_grille_blender.jpg` |
| 2.16 | 1 | Le menu *Set Parent To* (`Ctrl + P`) | Côte à côte | `parent_menu_blender.jpg` |
| 2.17 | 1 | La molette crantée de l'interrupteur | Côte à côte | `radial_array_knob_blender.jpg` |
| 2.18 | 2 | Le menu *Add > Curve* | Côte à côte | `add_curve_menu_blender.jpg` |
| 2.19 | 2 | L'anatomie d'une courbe de Bézier en Mode Édition : points et poignées | Pleine largeur | `bezier_anatomy_blender.jpg` |
| 2.20 | 2 | Le menu *Set Handle Type* (`V`) | Côte à côte | `handle_type_menu_blender.jpg` |
| 2.21 | 2 | La barre d'outils en Mode Édition de courbe, *Curve Pen* actif | Côte à côte | `curve_pen_toolbar_blender.jpg` |
| 2.22 | 2 | L'onglet *Object Data* d'une courbe, rubrique *Shape* | Côte à côte | `curve_shape_panel_blender.jpg` |
| 2.23 | 2 | La rubrique *Geometry* : *Bevel* (*Round*, *Depth*, *Resolution*, *Fill Caps*) | Côte à côte | `curve_geometry_bevel_panel_blender.jpg` |
| 2.24 | 2 | Le câble posé, de l'arrière du socle à la table | Pleine largeur | `cable_bezier_lamp_blender.jpg` |
| 2.25 | 2 | Le menu `Maj + S`, avec *Cursor to Selected* et *Selection to Cursor* | Côte à côte | `snap_pie_menu_blender.jpg` |
| 2.26 | 2 | Le panneau *Screw* : *Angle*, *Screw*, *Iterations*, *Steps*, *Axis*, *Merge Vertices*, *Merge Distance* | Côte à côte | `screw_modifier_panel_blender.jpg` |
| 2.27 | 2 | Le demi-profil de l'ampoule et l'ampoule obtenue ; à côté, le sommet aplati par une *Merge Distance* de 10 mm | Pleine largeur | `bulb_profile_screw_blender.jpg` |
| 2.28 | 3 | La lampe modélisée, superposée au gabarit en fil de fer | Pleine largeur | `lamp_model_vs_gabarit_blender.jpg` |
| 2.29 | 3 | L'Outliner du fichier final : collections, pièces et icônes des modificateurs | Côte à côte | `outliner_lamp_model_blender.jpg` |
| 2.30 | 3 | La lampe modélisée, en *Solid* avec *Cavity* | Pleine largeur | `lamp_model_final_blender.jpg` |
| 2.31 | 3 | Défi : le panneau *Boolean* en *Difference*, avec la grille comme objet | Côte à côte | `boolean_difference_panel_blender.jpg` |
| 2.32 | 3 | Défi : la liseuse de cabine finie, sur sa paroi | Côte à côte | `reading_light_challenge_blender.jpg` |

L'aimantation, *Face Orientation* et le menu `Ctrl + A` ont déjà leurs captures au chapitre 1 et dans Basics 103 : le texte y renverra. Les captures se prennent de préférence sur la collection *Corrigé* du fichier 1.

## Ce qui peut sauter en cas de retard

Raccourcissez dans cet ordre :

| Ordre | Ce que l'on coupe | Ce que l'on garde |
|---|---|---|
| D'abord | Le fichier de démos `PRC02_ch2_demos_secteurs.blend` : chaque moment « Ailleurs » se dit en une phrase, sans ouvrir le fichier | Le lien avec les métiers, à l'oral |
| Ensuite | Les autonomies de la répétition et du câble : la molette de l'interrupteur passe en palier ★ de l'atelier ; le second tracé du câble saute | Les cycles guidés ; la découverte du *Bevel* sur le socle, faite en guidé, pas à pas, si le temps manque |
| Ensuite | L'ampoule : démo seule. Les apprenants prennent celle du corrigé (`M` vers *Lampe*, puis renommée *Ampoule*) et retouchent son profil | Le principe de la révolution |
| En dernier | L'atelier : les articulations restent les sphères du blocage | La checklist et l'enregistrement |

Ce qui ne saute jamais : *Mirror*, *Solidify*, la grille d'aération en *Array* et le câble en Bézier. Ils portent les points du programme officiel. Un apprenant en retard prend la pièce qui lui manque dans la collection *Corrigé* (`M` vers *Lampe*). Si le retard est important, `PRC02_ch2_lampe_modele.blend` garantit à tous le même point de départ au chapitre 3.

## Les défis pour ceux qui avancent vite

- Les paliers ★ de chaque séquence et de l'atelier, dans le LISEZ-MOI. Ceux de l'atelier ont leur solution dans la collection masquée *Corrigé défis*, sous-collection *Paliers*.
- **La chape (★★) :** une chape en U pour l'articulation du haut, modélisée par moitié avec *Mirror*, *Clipping* et *Bisect* (présentés dans l'application). Elle prend la place de la molette du haut.
- **La tête tulipe (★★) :** remplacer le cône par un profil de Bézier, puis *Screw* et *Solidify*. La pile la plus complète du chapitre.
- **Les ressorts (★★) :** un cercle de Bézier, décalé de l'axe, et un *Screw* avec une valeur de *Screw* non nulle et plusieurs *Iterations* donnent un ressort, comme ceux des lampes d'architecte. Un *Mirror* donne le second.
- **Percer la grille (★★) :** un *Boolean* en mode *Difference* sur le socle, avec l'objet des lamelles comme outil. Prolongez d'abord la lamelle vers le bas, sur 6 mm de haut : les fentes font alors 3 mm de profondeur. Les lamelles deviennent de vraies fentes, et le perçage reste non destructif.
- **Une grille au dos de l'abat-jour (★★) :** la même couronne, sur l'axe incliné de la tête.
- **La liseuse de cabine (★★) :** la même méthode sur un objet des transports, avec son fichier de travail et son corrigé masqué (fichier 4).
- Le rôle de copilote, comme à l'initiation.

Les solutions des cinq premiers défis ★★ sont dans la collection masquée *Corrigé défis* du fichier de travail, une sous-collection par défi.

## Gérer l'hétérogénéité

- Les binômes et les copilotes de l'initiation restent en place.
- Le LISEZ-MOI donne chaque geste au chiffre près. Les valeurs restent indicatives : on peut les adapter à son concept.
- Le socle de l'atelier suffit : il couvre tous les points du programme.
- À chaque point de contrôle, passez d'abord par les postes des débutants, avec les post-it vert et rose de l'initiation.
- Un apprenant perdu prend la pièce qui lui manque dans la collection *Corrigé* : il rattrape le groupe sans refaire ce qu'il a manqué.
- Les termes de l'interface restent en anglais : traduisez-les à l'oral la première fois.

## Coordination avec les chapitres 3 et 4

Ce plan a été relu face au découpage validé (`PRC02-decoupage-formation.md`, critères 1 à 7 et décisions du 18 novembre) et aux plans des chapitres 3 et 4 (`PRC02-plan-chap3.md`, `PRC02-plan-chap4.md`), dans leur version du 18 novembre.

**Contrôle des critères du découpage :**

| Critère | Où le plan y répond |
|---|---|
| 1. Durée | 3 h 30 de contenu, 3 h 50 avec les pauses. L'ajustement de l'épaisseur garde ses 25 minutes |
| 2. Périmètre | Les trois ancres ; ni *Append* ni *Link* ; ni matière, ni lumière, ni caméra. Le *Boolean* reste un défi |
| 3. Pas de redite | Tableau « Ce qui est acquis, ce que l'on approfondit ». Le *Bevel* en modificateur s'appuie sur le *Bevel* en outil de l'initiation |
| 4. Continuité | Départ : la variante A du chapitre 1, ou le fichier 1 sans travail préalable. Fin : `lampe_modele_v001.blend`. En cours de séance, un apprenant en retard prend la pièce manquante dans la collection *Corrigé* |
| 5. Fichiers et ateliers | Tableau des fichiers et des corrigés, en tête de la partie « Les fichiers d'exercice ». Corrigés dans des collections masquées « Corrigé » et « Corrigé défis » ; un seul fichier séparé, justifié : `PRC02_ch2_lampe_modele.blend`, départ du chapitre 3. Ressources empaquetées ; LISEZ-MOI par paliers, qui disent où trouver le corrigé |
| 6. Chapitre 4 | Sans objet |
| 7. Progression | Prérequis et nouveautés de chaque section. Une notion par cycle : le cycle A de l'épaisseur n'introduit plus que la coque ; le *Bevel* en modificateur est déclaré nouveau, découvert seul sur le socle ; l'ordre de la pile devient une remarque. L'atelier n'apporte aucune notion nouvelle. Cinq quiz, sur les acquis dont dépend la suite |

**Ce qui est aligné avec le chapitre 4 :**
- **Les pièces attendues :** socle, bras, articulations, abat-jour, grille d'aération, câble, interrupteur et ampoule. Le gros plan sur une articulation, l'interrupteur ou l'ampoule trouve ses sujets.
- **L'état de la lampe :** une seule collection *Lampe*, à l'échelle réelle (millimètres, *Unit Scale* 1,0), échelle appliquée, modificateurs actifs.
- **Le nommage :** `lampe_blocage_v001.blend` (chapitre 1), `lampe_modele_v001.blend` (chapitre 2), `lampe_habillage_v002.blend` (chapitre 3), `lampe_rendu_v001.blend` (chapitre 4).
- **La lampe allumée** (palier ★★ du chapitre 4) : l'ampoule est un objet séparé, logé au fond de l'abat-jour.
- **La liseuse de cabine :** le défi ★★ du chapitre 2, que le chapitre 4 propose de mettre en scène, a son fichier de travail, corrigé compris.

**Ce qui est aligné avec le chapitre 3 :**
- **Le fichier d'entrée et les pièces :** `lampe_modele_v001.blend`, le corrigé `PRC02_ch2_lampe_modele.blend` (base de son fichier de secours `PRC02_ch3_lampe_a_habiller.blend`), et la liste des pièces de son cahier CMF. La *Douille* est bien une pièce séparée.
- **La convention des corrigés,** commune aux chapitres 2 à 4 : une collection masquée dont le nom commence par « Corrigé », dans le fichier de travail ; un fichier séparé seulement s'il est justifié. Au chapitre 2, le seul fichier séparé est `PRC02_ch2_lampe_modele.blend`, parce que le chapitre 3 en part.
- **Les rotations des bras ne sont pas appliquées :** le chapitre 3 s'en sert pour orienter le brossé de l'aluminium.
- **L'abat-jour est une seule coque *Solidify* :** le chapitre 3 propose en option un intérieur blanc par le *Material Offset* du *Solidify*.
- **L'ampoule est un volume plein**, tiré d'une courbe : le chapitre 3 en fait une paroi fine avec la case *Thin Wall* du *Principled BSDF*. Aucun *Solidify* n'est nécessaire.
- **Le lissage :** *Shade Auto Smooth* est retenu. Il est posé sur le socle, la tête et les bras pendant la séquence de l'épaisseur, puis sur les articulations, l'interrupteur et la douille à l'atelier. L'ampoule (*Smooth Shading* coché par défaut dans le *Screw*) et le câble (courbe lisse par défaut) n'en ont pas besoin. Le check-up du chapitre 3 reste une sécurité.
- **Le moteur de rendu :** le fichier du chapitre 1 est réglé sur Cycles et contient un texte caché laissé par une extension (*Geo-Scatter*). Les fichiers du chapitre 2 seront réglés sur EEVEE et nettoyés.

**Pour le chapitre 4, un point d'attention et non une incohérence :** le *Clip Start* d'une caméra vaut 0,1 m par défaut. Un gros plan pris à moins de 100 mm de la lampe serait coupé. Avec les focales prévues (85 à 100 mm, avec du recul), le cas ne devrait pas se présenter.

**Phrases périmées dans les plans voisins** (à corriger par leurs sessions, ce plan n'y touche pas) :
- **Chapitre 4,** liste des pièces de la lampe et tableau « Ce que le plan du chapitre 2 confirme » : les molettes des articulations sont un palier ★. Elles ne sont pas dans `PRC02_ch2_lampe_modele.blend`, seulement dans la collection *Corrigé défis* du fichier de travail.
- **Chapitre 4,** même tableau et point de vigilance « La répétition du chapitre 2 » : le socle porte bien, pour tous, une grille d'aération en couronne, en plus des crans de l'interrupteur. « Pas de grille d'aération » et « les ouïes ne sont qu'un défi » ne sont plus vrais. Le découpage et le plan du chapitre 2 sont d'accord.
- **Chapitre 3,** partie sur ce que le chapitre reçoit (« *Shade Auto Smooth* sur le socle et la tête ») et question 3 de ses points ouverts : le lissage couvre aussi les bras, les articulations, l'interrupteur et la douille. Son check-up reste utile, comme sécurité.

## Décisions du formateur (18 novembre 2026)

1. **Le fil rouge :** la lampe jusqu'au bout. La liseuse de cabine, de train ou d'avion, devient un défi ★★, avec son fichier de travail et son corrigé masqué. Le projecteur multisecteur n'est pas retenu.
2. **Les trois ajouts hors programme sont retenus :** le modificateur *Screw*, *Shade Auto Smooth* et le parentage. Le chapitre 3 dépend de *Shade Auto Smooth*.
3. **Les bras à deux tiges sont retenus.**
4. **Le fichier de démos multisecteurs est gardé, léger.** C'est le premier élément coupé en cas de retard.
5. **Cinq quiz au lieu de sept,** dans la lignée des quatre du chapitre 1. Sont retirés : l'angle de l'*Empty*, déjà vérifié en autonomie, et l'ordre de sélection du parentage, vérifié au point de contrôle.
6. **L'épaisseur, cycle A :** il ne garde que la suppression d'une face et le *Solidify*. Le *Bevel* en modificateur se découvre sur le socle, en autonomie, au cycle B ; il est déclaré comme nouveauté. Le *Bevel* de la tête passe à l'atelier. L'ordre de la pile devient une remarque du formateur (encart *NOTE*). Le minutage reste à 25 minutes, et le total à 3 h 30.
7. **Les corrigés,** selon la convention commune aux chapitres 2 à 4 : dans le fichier de travail, une collection masquée dont le nom commence par « Corrigé » (*Corrigé*, *Corrigé défis*), signalée en une ligne dans le LISEZ-MOI. Un fichier séparé n'existe que s'il est justifié : ici, seul `PRC02_ch2_lampe_modele.blend`, départ et secours du chapitre 3. Un tableau récapitule, pour chaque exercice et l'atelier, le fichier de travail et l'endroit du corrigé. Les fichiers déjà livrés (Basics, initiation, chapitre 1) ne sont pas retouchés.

**Encore à tester lors de la construction :** l'enchaînement *Curve Pen* depuis un point sélectionné, et l'unité d'une valeur tapée pendant un geste (encadré de la séquence de l'ampoule).
