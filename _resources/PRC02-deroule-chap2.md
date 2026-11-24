# Chapitre 2 · Modélisation non destructive : déroulé formateur

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 4 sur 6, en présentiel, de 5 à 8 apprenants · Version du 19 novembre 2026, application support 1.0.0

## En bref

- **Objectif :** à la fin de la demi-journée, chaque apprenant a remplacé les volumes de son blocage par des pièces propres, qui restent modifiables. Il reflète un bras avec *Mirror*, fait de l'abat-jour une coque avec *Solidify*, arrondit et lisse ses pièces, puis répète un détail en couronne avec *Array* et un *Empty*. Il dessine une courbe de Bézier, en fait un câble, puis tire une ampoule d'un demi-profil avec *Screw*.
- **Format :** 3 h 50, dont 3 h 30 de contenu et 2 pauses de 10 minutes. Il reste 10 minutes de marge sur 4 heures. Exemple : de 9 h 00 à 12 h 50.
- **Principe :** le même qu'à l'initiation et au chapitre 1. Une notion à la fois, en cycles courts : vous la montrez en quelques minutes, ils la pratiquent en guidé, puis seuls. Personne ne passe plus de 15 minutes sans toucher la souris.
- **La règle du jour : on n'applique aucun modificateur.** Une épaisseur, un nombre de lamelles ou un profil restent des réglages jusqu'au chapitre 4. Seule l'échelle s'applique (`Ctrl + A > Scale`), et ce n'est pas la même chose. La règle du chapitre 1 continue : chaque valeur se tape avec son unité, `3mm` dans un champ, `G Y = 10mm` pendant un geste.
- **Fil rouge :** la lampe de bureau. Le blocage du chapitre 1 sert de gabarit, et chaque volume devient une pièce : des bras à deux tiges, un abat-jour en coque, une grille d'aération, une molette, un câble, une ampoule. Le fichier de fin, `lampe_modele_v001.blend`, est celui qu'ouvre le chapitre 3.
- **Trois ajouts hors du programme officiel :** le modificateur *Screw*, *Shade Auto Smooth* et le parentage. Chacun sert un point du programme ; le chapitre 3 dépend du lissage.

### L'ordre de la séance

La séance suit l'ordre de l'application, à deux détails près. Dans l'épaisseur, vous montrez *Shade Auto Smooth* avant le *Bevel*, que les apprenants découvrent seuls sur le socle ; l'application range le *Bevel* d'abord (figures 2.10, puis 2.11) pour montrer la pile complète de la tête (figure 2.12). Les quiz se font à la fin de la séquence qu'ils vérifient ; dans l'application, ils sont groupés en fin de section.

### Ce que l'on survole

Ces notions sont dans l'application. Elles ne sont pas exigées en séance, et certaines servent de défi.
- L'ordre de la pile : une remarque de 30 secondes, l'encart *NOTE* de la tête, sans manipulation. *Move to First* et *Move to Last* (figure 2.3) : cités.
- *Clipping* et *Bisect* du *Mirror* (figure 2.6) : montrés sur le capot du fichier de démos ; ils servent au défi de la chape. *Merge* : cité.
- Les poignées *Aligned* et *Free* : citées. On pratique *Vector* et *Automatic*.
- *Extrude* et *Offset* d'une courbe : cités, comme pièges.
- *Circle*, le cercle de Bézier, et les champs *Screw* et *Iterations* du *Screw* : cités ; ils servent au défi des ressorts.
- Le *Boolean* : seulement en défi (figure 2.31).
- Le défi facultatif « Modélisation avancée », dans la rubrique « Pour aller plus loin » de la barre latérale : annoncé en une phrase, sans démonstration.

### Les fichiers

| Fichier | Moment | Contenu |
|---|---|---|
| `PRC02_ch2_lampe_depart.blend` | 0:00, puis toute la séance | Le gabarit (la variante A du chapitre 1, en fil de fer, non sélectionnable), les pièces de travail dans *Lampe*, les croquis et le repère de l'ampoule. Les corrigés : collections masquées *Corrigé* et *Corrigé défis*. Enregistré aussitôt sous `lampe_modele_v001.blend` |
| `PRC02_ch2_croquis_ampoule.zip` | 2:10, si besoin | Le demi-profil de l'ampoule, déjà placé dans le fichier de départ ; pour ceux qui gardent leur propre blocage |
| `PRC02_ch2_lampe_modele.blend` | Fin de séance | La lampe terminée, noms sans suffixe : le corrigé de l'atelier et le départ du chapitre 3 |
| `PRC02_ch2_liseuse_depart.blend` | Atelier, pour ceux qui avancent vite | Le défi ★★ de la liseuse, avec son corrigé masqué *Corrigé* |
| `PRC02_ch2_defi_modelisation.blend` | Hors minutage | Le défi facultatif « Modélisation avancée » ; corrigés dans « Corrigé défi modélisation » |
| `PRC02_ch2_demos_secteurs.blend` | Moments « Ailleurs » | Votre poste seulement : un capot, une soufflante, une main courante de tram et une roue ferroviaire, déjà terminés |

L'application propose le fichier de départ en section 1, sous « Du blocage au modèle », et le croquis en section 2, sous « Profil de révolution : l'ampoule ». La lampe modélisée et la liseuse sont en section 3, sous la checklist et dans « Les défis ★★ »  ; le défi facultatif, dans la rubrique « Pour aller plus loin » de la barre latérale (Défi 1). Le fichier de démos n'est pas dans l'application : il est dans le dossier `_resources/exercices/` du dépôt, avec les autres.

> **À savoir :** chaque fichier s'ouvre sur un texte LISEZ-MOI en bas de l'écran ; `Ctrl + Espace`, la souris au-dessus, l'agrandit. Celui du fichier de départ suit la séance : une partie par séquence, de « 0 · Repères » à « 6 · Atelier », chacune avec son socle, un palier ★ et un contrôle. Il tient lieu de consignes : ce document n'a pas d'annexe et renvoie à ses parties. Les fichiers sont réglés sur EEVEE et affichent des millimètres : cette fois, pas de moteur à vérifier.

## Avant la demi-journée

### Les postes des apprenants

- [ ] L'application support 1.0.0 est installée. Une version plus ancienne propose la mise à jour à son démarrage.
- [ ] Le dossier de travail contient `PRC02_ch2_lampe_depart.blend`. À défaut, chacun le télécharge depuis l'application, en section 1, à 0:00.
- [ ] Blender 5.2 LTS s'ouvre, avec une souris à trois boutons. *Emulate Numpad* reste activé sur les portables sans pavé numérique.
- [ ] Le blocage du chapitre 1, `lampe_blocage_v001.blend`, n'est pas nécessaire : le fichier de départ le remplace. Ceux qui veulent garder le leur le peuvent ; ils auront besoin de l'archive du croquis de l'ampoule.

### Votre poste de démonstration

- **Lancez Blender en configuration d'usine** (`blender.exe --factory-startup`), avec *Resolution Scale* à 1,3, comme au chapitre 1. Pendant vos démos, tapez toujours `=` avant une unité.
- **Préparez une copie de travail du fichier de départ,** enregistrée sous un autre nom : le fichier livré reste intact.
- **Le geste des tiges, à connaître avant la séance :** `S`, `Maj + Z` deux fois, puis `0.5`. Les bras sont inclinés : avec un seul `Maj + Z`, en orientation *Global*, l'échelle suit les axes du monde, et la tige se redresse, raccourcit et quitte ses articulations. Le second `Maj + Z` prend l'axe propre du bras, comme `G Z Z` au chapitre 1 (vérifié dans Blender 5.2). Si l'application ou le LISEZ-MOI du fichier écrivent encore `S Maj + Z 0.5`, rectifiez à l'oral.
- **Ouvrez `PRC02_ch2_demos_secteurs.blend` dans une seconde fenêtre de Blender,** pour les moments « Ailleurs ». Son LISEZ-MOI dit quoi montrer dans chaque collection. C'est le premier élément coupé en cas de retard.
- **Ne cliquez jamais *Apply*** : montrez le menu de l'en-tête sans l'exécuter.
- **Gardez l'application ouverte** sur le chapitre 2, pour projeter les quiz.

### Le matériel de la salle

- Les post-it vert et rose des points de contrôle, et le minuteur.
- Le paperboard, préparé avant l'arrivée des apprenants :
  - la règle du jour : « On n'applique aucun modificateur. Seule l'échelle s'applique : `Ctrl + A > Scale`. » ;
  - la règle du chapitre 1, toujours valable : « Tapez l'unité : `3mm` dans un champ, `G Y = 10mm` pendant un geste. » ;
  - le corrigé : « collection *Corrigé*, œil fermé : on compare, on ne copie pas. Une pièce manque ? `M` vers *Lampe*, puis renommez-la sans `_corrige`. » ;
  - la checklist du modèle propre, pour l'atelier (voir sa fiche) ;
  - le fichier de fin : `lampe_modele_v001.blend` ;
  - les raccourcis du jour, complétés au fil de la séance : `S`, `Maj + Z` deux fois, `X > Faces`, `Maj + C`, `Maj + S`, `Ctrl + P`, `V`, `E`, `Ctrl + clic droit`, `Ctrl + Espace`.
- Pas de consignes imprimées : le LISEZ-MOI de chaque fichier en tient lieu.

## La demi-journée · Du blocage au modèle

Les trois sections du chapitre 2. Les apprenants repartent avec leur lampe modélisée, modifiable de bout en bout, dans `lampe_modele_v001.blend`. Dans la colonne « Modalité », les durées sont en minutes.

| Horaire | Durée | Séquence | Section | Modalité |
|---|---|---|---|---|
| 0:00 | 10 min | Lancement : du blocage au modèle | 1 | Collectif 4 + poste 6 |
| 0:10 | 25 min | Symétrie : *Mirror* | 1 | Démo 10 + guidé 10 + autonomie 4 + quiz 1 |
| 0:35 | 25 min | Épaisseur : *Solidify*, puis lissage et *Bevel* | 1 | Démo 8 + guidé 9 + autonomie 7 + quiz 1 |
| 1:00 | 10 min | Pause | | |
| 1:10 | 30 min | Répétition : la grille d'aération | 1 | Démo 10 + guidé 12 + autonomie 8 |
| 1:40 | 30 min | Courbes de Bézier : le câble | 2 | Démo 10 + guidé 10 + autonomie 8 + quiz 2 |
| 2:10 | 25 min | Profil de révolution : l'ampoule | 2 | Démo 10 + guidé 10 + autonomie 5 |
| 2:35 | 10 min | Pause | | |
| 2:45 | 50 min | Atelier · La lampe modélisée | 3 | Lancement 5 + autonomie 40 + retour 5 |
| 3:35 | 15 min | Galerie, bilan et passerelle vers le chapitre 3 | 3 | Collectif, dont quiz 2 |

### 0:00 · Lancement : du blocage au modèle (10 min)

- **Où l'on en est (collectif, 4 min) :** « Au chapitre 1, vous avez arrêté les proportions de la lampe. Aujourd'hui, chaque volume devient une pièce propre, et chaque décision reste modifiable. Au chapitre 3, ces pièces recevront leurs matières. »
- **Montrez le but :** sur votre copie, fermez l'œil de *Lampe* et ouvrez celui de *Corrigé* : la lampe terminée apparaît dans le gabarit (figure 2.28). Sélectionnez *Grille_aeration_corrige* ; onglet *Modifiers*, *Count* 18 : une demi-couronne. Remettez 36. « C'est cela, le non destructif. » Puis refermez l'œil de *Corrigé* et rouvrez celui de *Lampe*.
- **La règle du jour,** au paperboard : « On n'applique aucun modificateur. »
- **Le défi facultatif, en une phrase :** « Pour ceux qui sont à l'aise, ou qui connaissent déjà ces sujets : un défi facultatif, hors programme, dans la rubrique « Pour aller plus loin » de l'application. » Pas de démonstration.

**Ils font, sur poste (6 min),** d'après § 1 « Du blocage au modèle » et « Recette · Prendre le fichier en main » (figure 2.1) :
1. *File > Open* : `PRC02_ch2_lampe_depart.blend`. Ceux qui ne l'ont pas le téléchargent dans l'application, en section 1.
2. *File > Save As* : `lampe_modele_v001.blend`, dans le dossier de travail. Le fichier de départ reste intact.
3. Le tour de l'Outliner : *Gabarit*, le blocage en fil de fer, non sélectionnable ; *Lampe*, leurs pièces, une par volume ; *Croquis*, les images de référence et le repère de l'ampoule ; *Corrigé* et *Corrigé défis*, œil fermé. « On les ouvre pour comparer, jamais pour copier. »
4. Le LISEZ-MOI : `Ctrl + Espace`, la souris au-dessus, l'agrandit, puis le réduit. Ils lisent la partie 0, les repères.
5. Le fichier affiche des millimètres : c'est un réglage du fichier, pas une exigence. Les valeurs se tapent toujours avec leur unité.

**Ce fichier remplace le blocage du chapitre 1 :** il ne demande aucun travail préalable. Proposez-le à tous. Celui qui garde son propre blocage suit les mêmes étapes, avec des valeurs indicatives ; ses corrigés restent dans le fichier de départ, ouvert dans une seconde fenêtre de Blender.

**Point de contrôle :** la barre de titre affiche `lampe_modele_v001.blend` ; chaque écran montre le gabarit en fil de fer et les pièces en volume.

**Pièges fréquents :**
- Un clic sur le gabarit ne sélectionne rien : c'est voulu, il est verrouillé.
- Le LISEZ-MOI ne s'agrandit pas : la souris n'est pas au-dessus du texte.
- Un apprenant travaille dans le fichier de départ : *File > Save As* a été oublié. Faites-le tout de suite.

### 0:10 · Symétrie : *Mirror* (25 min)

**Un autre axe (démo 5 min, guidé 10 min).** Vous montrez, d'après § 1 « La pile de modificateurs » (figures 2.2 et 2.3), « Symétrie : le Mirror sur un autre axe » et « Recette · Des tiges doubles pour les bras » (figures 2.4 et 2.5) :
1. **La pile, en rappel (1 min).** Onglet *Modifiers*, *Add Modifier > Generate* : les premières lettres d'un nom suffisent pour le trouver. La flèche de l'en-tête d'un modificateur : *Copy to Selected*, *Move to First*, *Move to Last*, et *Apply*, montré sans clic. L'encart *WARNING* : appliquer un modificateur n'est pas appliquer l'échelle.
2. *Bras_bas* sélectionné : `Tab`, `A`, puis `S`, `Maj + Z` deux fois et `0.5`. La tige passe à 8 mm de diamètre, sans changer de longueur. « Le bras est incliné : le second `Maj + Z` prend son axe propre, comme `G Z Z` au chapitre 1. »
3. `G Y = 10mm` : la tige quitte l'axe de la lampe. `Tab`.
4. *Add Modifier > Generate > Mirror*. L'axe X est coché : décochez-le, cochez Y. Deux tiges parallèles apparaissent. « L'axe se lit dans le repère de l'objet ; le reflet se fait autour de son origine. »
5. **Ailleurs :** dans le fichier de démos, *Auto_capot* : une moitié de capot, et le *Mirror* construit l'autre. `Tab`, puis un sommet du bord central déplacé : il reste sur l'axe, c'est *Clipping*. Même méthode pour un nez de tram ou un fuselage.

**Ils font, en guidé (10 min) :** les étapes 2 à 4 sur *Bras_bas*, avec la partie 1 du LISEZ-MOI, étapes 1 et 2.

**L'origine et *Copy to Selected* (démo 5 min, autonomie 4 min).** Vous montrez, d'après l'encart *WARNING* « Le piège de l'origine » (figure 2.5, à droite) :
1. **Faites deviner.** *Bras_haut* sélectionné, `Maj + D`, puis clic droit : une copie, restée en place. Ajoutez-lui un *Mirror* sur Y seul, puis `G Y = 10mm` en Mode Objet. Une seule tige : « Où est la seconde ? » L'origine a suivi la tige, et le reflet tombe sur elle.
2. Deux solutions : décaler la géométrie en Mode Édition, comme sur *Bras_bas* ; ou choisir *Socle* dans *Mirror Object*. Montrez la seconde : la deuxième tige apparaît. Puis `X` : la copie est supprimée.
3. ***Copy to Selected*.** Sur *Bras_haut*, refaites vite les étapes 2 et 3. Puis *Bras_haut* sélectionné, `Maj + clic` sur *Bras_bas* : il devient l'objet actif. Menu de l'en-tête du *Mirror* > *Copy to Selected* : le modificateur passe sur *Bras_haut*.

**Ils font, en autonomie (4 min) :** *Bras_haut*, avec la partie 1, étape 3. ★ : le piège sur une copie, puis *Mirror Object* sur *Socle*.

**Quiz (1 min),** ensemble à l'écran : le premier quiz de la section 1, la tige déplacée en Mode Objet. Il est en fin de section dans l'application. Chacun répond pour soi, puis on commente les erreurs.

**Point de contrôle :** en vue de dessus (`7`), chaque bras montre deux tiges, symétriques par rapport à l'axe du socle. En vue de face (`1`), les tiges suivent toujours le gabarit. Dans `N > Item`, *Bras_bas* est resté à -5, 0, 165 mm. `Ctrl + S`.

**Corrigé :** *Bras_bas_corrige* et *Bras_haut_corrige*, dans *Corrigé*.

**Pièges fréquents :**
- Des tiges qui plongent dans le socle : l'axe X est resté coché.
- Le *Mirror* semble ne rien faire : `G Y` a été fait en Mode Objet. `Ctrl + Z`, puis `Tab` avant `G Y = 10mm`.
- *Copy to Selected* sans effet : l'objet actif doit porter le modificateur. *Bras_bas* se sélectionne en dernier.
- Une tige qui se redresse et quitte ses articulations : un seul `Maj + Z`, l'échelle a suivi les axes du monde. `Ctrl + Z`, puis `S`, `Maj + Z` deux fois, `0.5`.

### 0:35 · Épaisseur : *Solidify*, puis lissage et *Bevel* (25 min)

**La coque (démo 5 min, guidé 7 min).** Une seule notion : la coque ouverte et son épaisseur. Vous montrez, d'après § 1 « Épaisseur : une coque avec le Solidify » et « Recette · La coque de la tête » (figures 2.7 à 2.9), sur *Tête* :
1. `Tab`, `3`, clic sur la grande face de l'ouverture, puis `X > Faces` (figure 2.7). Il reste une surface sans épaisseur. `Tab`.
2. *Add Modifier > Generate > Solidify* (figure 2.8) : *Thickness* `1.5mm`. Faites varier *Offset* de `-1` à `1` : l'épaisseur passe de l'intérieur à l'extérieur. Remettez `-1` : la forme extérieure, validée au blocage, ne change pas. *Even Thickness* coché.
3. *Fill*, dans la rubrique *Rim*, ferme le bord de la coque : comparez, case cochée puis décochée.
4. **Ailleurs :** un carénage d'avion, une coque de rétroviseur, un panneau d'habillage intérieur de train. On dessine la surface extérieure ; le *Solidify* donne l'épaisseur.

**Ils font, en guidé (7 min) :** les étapes 1 à 3, avec la partie 2 du LISEZ-MOI, étapes 1 et 2.

**Le lissage (démo 3 min, guidé 2 min), puis la découverte du *Bevel* (autonomie 7 min).** Vous montrez, d'après § 1 « Lisser l'affichage : Shade Auto Smooth » et « Recette · Lisser la tête, le socle et les bras » (figures 2.11 et 2.12) :
1. *Tête* sélectionnée, *Object > Shade Auto Smooth*. Les 24 côtés paraissent lisses ; le bord reste net. Le modificateur *Smooth by Angle* s'ajoute en bas de la pile.
2. **L'ordre de la pile (30 secondes, sans manipulation),** l'encart *NOTE* : Blender calcule la pile de haut en bas, et l'ordre peut changer le résultat. *Smooth by Angle* fait exception : l'épingle de son en-tête le garde en dernier.

Ils font :
- **en guidé :** *Shade Auto Smooth* sur *Tête* ;
- **en autonomie, la découverte du *Bevel* sur *Socle*,** d'après § 1 « Arrondir les arêtes : le Bevel en modificateur » et « Recette · Le Bevel du socle » (figure 2.10). Annoncez-la en une phrase : « Le *Bevel* que vous connaissez en outil existe aussi en modificateur. » Partie 2 du LISEZ-MOI, étapes 4 et 5 : *Amount* `3mm`, *Segments* 3, *Limit Method* sur *Angle*, déjà réglé ; *Shade Auto Smooth* sur *Socle* ; puis sur *Bras_bas* et *Bras_haut*, sélectionnés ensemble : leurs tiges seront en métal au chapitre 3 ;
- **★ :** *Offset* à `1`, puis `-1` ; *Thickness* `1mm`, puis `3mm` ; le *Bevel* de la tête (`0.5mm`, 2 segments), prévu à l'atelier.

Passez d'abord par les postes qui découvrent le *Bevel* : c'est la seule notion nouvelle pratiquée sans démo.

**Quiz (1 min),** ensemble à l'écran : le second quiz de la section 1, l'épaisseur qui part vers l'extérieur.

**Point de contrôle :** en vue de dessous (`Ctrl + 7`), le bord de la tête montre une épaisseur régulière. Les piles se lisent, de haut en bas : *Tête* = *Solidify*, *Smooth by Angle* ; *Socle* = *Bevel*, *Smooth by Angle*. Les arêtes du dessus et du dessous du socle sont arrondies. `Ctrl + S`.

**Corrigé :** *Tête_corrige*, *Socle_corrige* et les deux bras, dans *Corrigé*. La tête du corrigé porte déjà le *Bevel* de l'atelier : sa pile compte trois modificateurs.

**Pièges fréquents :**
- `X` en Mode Objet supprime toute la tête : `Ctrl + Z`, puis `Tab`.
- L'épaisseur part vers l'extérieur : *Offset* vaut `1`, ou les normales sont inversées. *Face Orientation* (Basics 103) tranche : une face rouge regarde vers l'intérieur.
- Un arrondi à grosses facettes : *Segments* est resté à 1.
- Un socle déformé : *Amount* est trop grand. Lisez la valeur affichée dans le champ, avec son unité.
- *Amount* introuvable : l'apprenant a pris l'outil `Ctrl + B`, qui affiche *Width*. Le modificateur est dans l'onglet *Modifiers*.

### 1:00 · Pause (10 min)

### 1:10 · Répétition : la grille d'aération (30 min)

Le socle cache l'électronique de la lampe : il lui faut une grille d'aération, une couronne de lamelles sur le dessus.

**La couronne (démo 7 min, guidé 10 min).** Vous montrez, d'après § 1 « Répétition : une couronne avec un Empty » et « Recette · La grille d'aération » (figures 2.13 à 2.15) :
1. **Rappel (1 min) :** *Relative Offset* et *Constant Offset* répétaient les sièges en ligne. Pour une couronne, il faut un repère qui tourne : un *Empty*, un objet sans géométrie, comme celui qui porte un croquis.
2. `Maj + C` : le curseur revient au centre, sous l'axe du socle. `Maj + A > Mesh > Cube`, F9 : *Size* `2mm`.
3. `Tab`, `S X 6` : une lamelle de 12 mm. `G X = 76mm`, puis `G Z = 25mm` : elle se pose sur le dessus du socle, près du bord. `Tab`. L'origine reste au centre du socle. Renommez-la *Grille_aeration*.
4. `Maj + A > Empty > Plain Axes` (figure 2.13), au même endroit, puis `R Z 10`. Renommez-le *Grille_pivot*.
5. Sur la lamelle, *Add Modifier > Generate > Array (Legacy)* : l'encart *NOTE* explique les deux entrées *Array*. Décochez *Relative Offset* ; cochez *Object Offset*, dépliez sa rubrique et choisissez *Grille_pivot* (figure 2.14). *Count* 36 : « 36 fois 10°, un tour complet. »
6. **Ailleurs :** *Aero_soufflante*, dans le fichier de démos : *Count* de 18 à 20, puis l'*Empty* tourné de 18°, soit 360° divisé par 20. Évitez 24 : c'est la réponse de la molette. Les rayons d'une jante et les boulons d'une roue de bogie suivent la même règle.

**Ils font, en guidé (10 min) :** les étapes 2 à 5, avec la partie 3 du LISEZ-MOI, étapes 1 à 4.

**L'*Empty* suit la pièce (démo 3 min, guidé 2 min, autonomie 8 min).** Vous montrez, d'après § 1 « Le parentage : l'Empty suit la pièce » (figures 2.16 et 2.17) :
1. Déplacez la lamelle seule : la couronne se déforme, car l'*Empty* est resté en place. `Ctrl + Z`. « Comment la garder entière ? »
2. Clic sur *Grille_pivot*, `Maj + clic` sur *Grille_aeration* : sélectionnée en dernier, elle est active. `Ctrl + P > Object` (figure 2.16). Dans l'Outliner, l'*Empty* se range sous la lamelle. Déplacez la lamelle : la couronne suit. `Ctrl + Z`.

Ils font :
- **en guidé :** le parentage, puis un essai de déplacement, annulé avec `Ctrl + Z` (partie 3, étape 5) ;
- **en autonomie, la molette de l'interrupteur,** avec l'encart *CAUTION* « À vous : la molette de l'interrupteur » (figure 2.17) et la partie 3, étape 6. Le curseur sur l'interrupteur (`Maj + S > Cursor to Selected`) ; un cran de 1,5 × 1,5 × 6 mm, à 8 mm de l'axe ; 24 crans ; *Interrupteur_crans* et *Interrupteur_pivot*. L'angle de l'*Empty* se cherche : ne le donnez pas ;
- **★ :** 30 crans ; une demi-couronne de lamelles à l'arrière du socle.

Un repère, si un apprenant bloque sur le cran : un cube, F9 *Size* `1.5mm`, puis `Tab`, `S Z 4`, `G X = 8mm`, `Tab`. La réponse attendue pour l'*Empty* : 15°.

**Point de contrôle :** 36 lamelles régulières sur le socle et 24 crans autour de l'interrupteur. Un déplacement de *Grille_aeration* emporte toute la couronne ; `Ctrl + Z`. `Ctrl + S`.

**Corrigé :** *Grille_aeration_corrige* et *Grille_pivot_corrige* ; *Interrupteur_crans_corrige* et *Interrupteur_pivot_corrige*, tourné de 15°.

**Pièges fréquents :**
- Un cube de 2 m : F9 a été oublié ; Blender ajoute ses primitives à leur taille d'origine.
- Une spirale : *Relative Offset* est resté coché.
- Une couronne décentrée : le curseur n'était pas au bon endroit au moment d'ajouter l'*Empty*, ou la lamelle a été déplacée en Mode Objet. `Ctrl + Z`, puis `Tab` avant `G X`.
- `Ctrl + P` dans le mauvais ordre : la lamelle suit l'*Empty*. Le parent est l'objet actif, sélectionné en dernier.

### 1:40 · Courbes de Bézier : le câble (30 min)

**Points et poignées (démo 4 min, guidé 6 min).** Vous montrez, d'après § 2 « Courbe et maillage », « L'anatomie d'une courbe de Bézier » et « Recette · Tracer le câble » (figures 2.18 à 2.20) :
1. « Un maillage, ce sont des sommets, des arêtes et des faces. Une courbe, c'est quelques points de contrôle : Blender en calcule la forme lisse. »
2. Vue de dessus (`7`). `Maj + A > Curve > Bézier` (figure 2.18), F9 : *Radius* `50mm`. Sans ce réglage, la courbe mesure 2 m. Renommez-la *Câble*.
3. `Tab` : chaque point de contrôle porte deux poignées (figure 2.19). `G` sur un point, puis sur une poignée. `V` (figure 2.20) : *Vector* casse l'angle, *Automatic* l'adoucit.
4. Le point d'une extrémité sélectionné, `E` : la courbe se prolonge. `Ctrl + clic droit` pose un point sous la souris.

**Ils font, en guidé (6 min) :** un tracé de 4 ou 5 points, de l'arrière du socle (à gauche en vue de face) vers le bord de la table, avec la partie 4 du LISEZ-MOI, étapes 1 et 2.

**Le volume (démo 3 min, guidé 4 min).** Vous montrez, d'après § 2 « Donner du volume au câble » et « Recette · Le câble rond » (figures 2.22 à 2.24) :
1. Onglet *Object Data*, l'icône de courbe. Rubrique *Geometry > Bevel* (figure 2.23) : *Round*, *Depth* `2.5mm` pour un câble de 5 mm, *Resolution* 4, *Fill Caps*. « Ce *Bevel* donne une section à la courbe : rien à voir avec le modificateur. »
2. Rubrique *Shape* (figure 2.22) : *Resolution Preview U*, à monter si le câble paraît anguleux.
3. En vue de face (`1`), le câble doit reposer sur la table, au niveau du dessous du socle. S'il flotte ou s'enfonce, en Mode Objet : `N > Item`, *Location* Z `2.5mm`, son rayon.
4. Avec l'aimantation *Face* du chapitre 1 (§ 3 « L'aimantation », figure 1.18), le premier point se pose contre le flanc du socle. Les suivants restent sur la table.
5. **Ailleurs :** *Ferro_main_courante*, dans le fichier de démos : `Tab`, un point déplacé, puis *Depth* changé. Une durite, un faisceau électrique de cabine.

**Ils font, en guidé (4 min) :** le câble rond de 5 mm, posé sur la table, son premier point contre le socle (partie 4, étapes 3 et 4).

***Curve Pen* (démo 3 min, autonomie 8 min).** Vous montrez, d'après § 2 « L'outil Curve Pen » (figure 2.21) : en Mode Édition, l'outil *Curve Pen*, en bas de la barre d'outils. Un clic pose un point anguleux (*Vector*) ; un cliquer-glisser tire ses poignées et pose un point arrondi (*Aligned*). Il prolonge la courbe depuis le point d'extrémité sélectionné. Pour revenir à la sélection, reprenez l'outil du haut de la barre.

**Ils font, en autonomie (8 min) :** un second tracé avec *Curve Pen*, avec une boucle posée sur la table (partie 4, étape 5). Chacun garde le tracé qu'il préfère. ★ : *Resolution Preview U* à 24. Une astuce à souffler : `Maj + D` sur le câble, puis, sur la copie en Mode Édition, ne garder que le premier point (`X > Vertices` sur les autres) : le nouveau tracé garde son épaisseur.

**Quiz (2 min),** ensemble à l'écran : les deux quiz de la section 2, le type de poignée *Vector* et la section ronde.

**Point de contrôle :** en vue de face (`1`), le câble repose sur la table. Il est rond et lisse ; en Mode Édition, il ne compte que 4 à 6 points. `Ctrl + S`.

**Corrigé :** *Câble_corrige* : cinq points à poignées *Aligned*, à 2,5 mm du sol, le premier enfoncé dans le flanc du socle.

**Pièges fréquents :**
- Des points partis en profondeur : ils ont été posés en perspective. Travaillez en vue de dessus (`7`).
- Un câble plat : *Extrude* a été réglé à la place de *Depth*. Un câble à facettes : *Resolution* ou *Resolution Preview U* est trop basse.
- Un câble qui flotte : la courbe est apparue au curseur, resté sur l'interrupteur depuis la molette. *Location* Z `2.5mm`.
- Un câble qui s'enfonce par endroits : une poignée descend sous la table. Remontez-la en vue de face.
- Le premier point se pose sur le dessus du socle : l'aimantation a été faite en vue de dessus. Passez en vue de face (`1`).

### 2:10 · Profil de révolution : l'ampoule (25 min)

**Vous montrez (10 min),** d'après § 2 « Profil de révolution : l'ampoule » et « Recette · L'ampoule » (figures 2.25 à 2.27) :
1. **Le principe :** on dessine la moitié du profil, et Blender le fait tourner autour d'un axe. C'est la révolution des logiciels de CAO. Le croquis est déjà placé : en vue de face, à droite de la lampe, cinq points numérotés du culot au sommet.
2. Clic sur *Repere_ampoule*, dans l'Outliner (collection *Croquis*), puis `Maj + S > Cursor to Selected` (figure 2.25) : le curseur se pose à la base de l'axe.
3. `Maj + A > Curve > Bézier`, renommée *Ampoule*. `Tab`. Le point de droite : `X > Vertices`. Le point restant : `Maj + S > Selection to Cursor`, c'est le point 1, sur l'axe. Puis `V > Vector`.
4. Vue de face (`1`). *Curve Pen* : un clic sur les points 2 et 3 (le culot, anguleux), un cliquer-glisser vertical sur le point 4 (le globe), un cliquer-glisser horizontal sur le point 5 (le sommet, sur l'axe).
5. `Tab`. *Add Modifier > Generate > Screw* (figure 2.26) : *Axis* Z, *Steps* 32. Cochez *Merge* : le sommet s'aplatit, car la distance d'origine, 10 mm, soude tout ce qui passe près de l'axe (figure 2.27, à droite). Tapez `0.1mm` dans le champ à droite de la case.
6. `Tab`, une poignée déplacée : toute l'ampoule suit. Le profil reste modifiable.
7. **Ailleurs :** *Ferro_roue*, dans le fichier de démos : `Tab`, retouchez le boudin, toute la roue suit. L'optique d'un phare, le cône d'une hélice.

**Ils font :**
- **en guidé (10 min) :** les étapes 2 à 5, avec la partie 5 du LISEZ-MOI, étapes 1 à 4 ;
- **en autonomie (5 min) :** placer l'ampoule dans la tête, `N > Item` : *Location* `211mm`, `0`, `411mm` ; *Rotation* Y `150` (étape 5). Puis ★ : retoucher le profil, un globe plus rond ou un culot plus long ; comparer 16 et 48 *Steps*.

**Point de contrôle :** une ampoule lisse, fermée en haut et en bas, logée au fond de la tête. `Ctrl + S`.

**Corrigé :** *Ampoule_corrige*. Son profil est rangé du sommet vers la base, dans l'ordre où *Curve Pen* pose les points : c'est le sens qui tourne les normales vers l'extérieur.

**Pièges fréquents :**
- Un sommet aplati : la distance de *Merge* est restée à 10 mm. Tapez `0.1mm`.
- Un trou au sommet : le point 5 ne touche pas l'axe, ou *Merge* n'est pas coché. Un sommet pointu : le point 5 a été posé d'un simple clic ; ses poignées doivent être horizontales.
- Un disque à la place d'une ampoule : le mauvais axe est choisi.
- Une ampoule rouge avec *Face Orientation* : cochez *Flip*, dans la rubrique *Normals* du *Screw*.
- Le croquis n'apparaît pas : la vue est en perspective. Il ne s'affiche qu'en vue de face orthographique (`1`).

### 2:35 · Pause (10 min)

### 2:45 · Atelier · La lampe modélisée (50 min)

La fiche complète est plus bas. Le lancement dure 5 minutes, l'autonomie 40 minutes et le retour 5 minutes.

### 3:35 · Galerie, bilan et passerelle (15 min)

- **Galerie (6 min) :** chaque lampe à l'écran, sous son meilleur angle, en *Solid* avec *Cavity*. Tout le monde fait le tour des postes.
- **Trois questions (4 min) :**
  - « Pourquoi le *Mirror* n'a-t-il rien fait, quand la tige avait été déplacée en Mode Objet ? »
  - « Quel réglage donne son épaisseur à un câble ? »
  - « Que se passe-t-il si l'on déplace la lamelle sans son *Empty* ? »
- **Quiz (2 min),** ensemble à l'écran : le quiz de la section 3, quand appliquer les modificateurs. Chacun répond pour soi, puis on commente les erreurs.
- **Passerelle (2 min) :** « Au chapitre 3, chaque pièce reçoit sa matière : un plastique laqué pour la tête, un métal pour les tiges, du verre pour l'ampoule. Vos pièces sont séparées : c'est ce qui rend l'habillage simple. Si votre lampe n'est pas finie, la lampe modélisée vous attend dans l'application, en section 3. »
- **Dernier contrôle (1 min) :** chacun a enregistré `lampe_modele_v001.blend`, *Gabarit* masqué, aucun modificateur appliqué.

<!-- pagebreak -->

## Atelier · La lampe modélisée

**Fichier :** `lampe_modele_v001.blend` · **Durée :** 50 min · **De 2:45 à 3:35**

**Situation :** « Le concept a passé la revue de blocage. Préparez la maquette numérique de la revue de design. Le client demandera sûrement des retouches : tout doit rester modifiable. »

**Objectif :** terminer les pièces de la lampe, l'assembler, la contrôler, puis l'enregistrer.

**Pourquoi il fonctionne :**
- Aucune notion nouvelle : l'atelier réinvestit les sections 1 et 2, avec la méthode de § 3 « Remplacer le blocage pièce par pièce ».
- Le gabarit rend le contrôle objectif : chaque pièce se compare à son volume, en vue de face (`1`) et de profil (`3`).
- La checklist est celle d'un fichier qu'on transmet : le chapitre 3 ouvre ce fichier tel quel.
- La question du client, au retour, montre ce que vaut le non destructif.

**Le socle, en 7 étapes,** d'après § 3 « Consignes · La lampe modélisée » (figure 2.28) et la partie 6 du LISEZ-MOI :

| Étape | Ce qu'il faut faire | Gestes réinvestis |
|---|---|---|
| 1 | *Articulation_bas*, *_milieu* et *_haut* : le curseur sur chaque sphère, puis `X`. *Cylinder*, F9 : *Vertices* 32, *Radius* `15mm`, `14mm` ou `12mm`, *Depth* `36mm`. `R X 90`. *Bevel* (`2mm`, 2 segments, *Angle*) et *Shade Auto Smooth*. Renommer | `Maj + S > Cursor to Selected`, F9, *Bevel*, lissage |
| 2 | *Douille* : le curseur sur *Tête*. *Cylinder*, F9 : *Radius* `15mm`, *Depth* `20mm`, *Rotation* Y `-30`. Puis `G Z Z = 45mm` : elle glisse le long de son axe, au fond de la tête. *Bevel* (`1mm`, 2 segments) et *Shade Auto Smooth* | `G Z Z` et l'orientation *Local* (chapitre 1) |
| 3 | *Tête* : *Bevel* de `0.5mm`, 2 segments. Il se range de lui-même au-dessus de *Smooth by Angle* | *Bevel*, l'épingle de la pile |
| 4 | *Interrupteur* : *Bevel* de `0.5mm`, 2 segments, et *Shade Auto Smooth* | *Bevel*, lissage |
| 5 | *Ampoule* : la placer, si ce n'est pas fait | `N > Item` |
| 6 | *Câble* : il touche le socle et repose sur la table | Aimantation, vues orthographiques |
| 7 | La checklist, *Gabarit* masqué, puis `Ctrl + S` | Basics 103 § 4 |

**La checklist,** au paperboard et dans « Consignes · La checklist du modèle propre » (figures 2.29 et 2.30) :
- chaque pièce porte un nom clair et se range dans la collection *Lampe* ;
- les échelles valent 1 (`Ctrl + A > Scale` si besoin) ;
- *Face Orientation* ne montre aucune face rouge ;
- les modificateurs sont tous actifs, aucun n'est appliqué ;
- la silhouette suit le gabarit, en vue de face et de profil ;
- la collection *Gabarit* est masquée, et `lampe_modele_v001.blend` est enregistré (`Ctrl + S`).

**Déroulé :**
1. **Lancement (5 min).** Sur votre copie, fermez l'œil de *Lampe* et ouvrez celui de *Corrigé* : la lampe terminée, dans le gabarit (figure 2.28). Rappelez la règle du jour : rien n'est appliqué, sauf l'échelle. Montrez la checklist, puis lancez le minuteur.
2. **Autonomie (40 min).** Chacun suit la partie 6 du LISEZ-MOI. Annoncez les 10 dernières minutes : c'est le moment de la checklist et de l'enregistrement.
3. **Retour (5 min).** Un volontaire projette sa lampe et change une valeur en direct : l'épaisseur de la tête, le nombre de lamelles ou le tracé du câble. « Le client veut une tête 20 % plus grande. Combien de temps vous faut-il ? »

**Paliers :**
- **★ :** l'encart *CAUTION* « Les paliers ★ de l'atelier ». Des molettes de serrage sur les articulations : l'interrupteur, ses crans et son *Empty* sélectionnés ensemble, `Alt + D`, la copie tournée de X -90° et posée contre l'articulation. Une rainure sur le pourtour du socle : deux boucles (*Loop Cut*), puis la bande entre elles extrudée de 1 mm vers l'intérieur. Une collection par sous-ensemble, *Pied*, *Bras* et *Tête*, dans *Lampe*.
- **★★ :** les défis de la partie « Pour ceux qui avancent vite », puis le défi facultatif « Modélisation avancée ».

**Points d'observation :**
- Trois articulations de diamètres différents : des copies simples (`Maj + D`) redimensionnées en Mode Édition, ou trois cylindres. Une copie redimensionnée en Mode Objet garde une échelle différente de 1.
- `Ctrl + A` ouvre le menu d'application des transformations : rien à voir avec *Apply*, dans l'en-tête d'un modificateur. Seule l'échelle s'applique : le chapitre 3 se sert de la rotation des bras pour orienter le brossé du métal.
- Une douille qui monte à la verticale : `G Z` seul suit l'axe du monde. Le second `Z` suit l'axe de la douille.
- Un *Bevel* plus large que l'épaisseur croise la géométrie : sur la tête, 0,5 mm pour 1,5 mm d'épaisseur.
- Palier ★ : les molettes en copie liée partagent leur maillage, pas leurs modificateurs ; changer le nombre de crans de l'une ne change pas les autres. `Alt + D` sur le cran seul garde l'ancien *Empty* : les trois objets se copient ensemble.
- Palier ★ : le *Bevel* de 3 mm du socle adoucit aussi la rainure. C'est voulu ; pour une rainure plus nette, réduisez *Amount*.

**Corrigé :** la collection masquée *Corrigé* : toute la lampe, chaque nom suffixé `_corrige`, à la place des pièces de travail. Les paliers ★ et les défis ★★ : *Corrigé défis*, une sous-collection chacun, à côté de la lampe. Pour en voir un : œil de *Corrigé défis* ouvert, une pièce sélectionnée, puis `.` du pavé numérique. La lampe terminée existe aussi en fichier séparé, `PRC02_ch2_lampe_modele.blend`.

**Ce que le chapitre 3 attend :** `lampe_modele_v001.blend`, ses pièces nommées dans *Lampe*, les échelles à 1, les modificateurs actifs. Le chapitre 3 l'ouvre, l'enregistre sous `lampe_habillage_v001.blend` et vérifie cinq points : les noms, l'échelle, les normales, le lissage et le moteur EEVEE. Une lampe inachevée ne bloque personne : `PRC02_ch2_lampe_modele.blend` la remplace, comme le fichier de secours du chapitre 3, `PRC02_ch3_lampe_a_habiller.blend`.

## Le défi facultatif · Modélisation avancée

Le Défi 1 de la rubrique « Pour aller plus loin » de la barre latérale, qui prolonge ce chapitre. Un complément hors programme et hors minutage : vous n'en faites aucune démonstration. Ses figures sont numérotées D1.1 à D1.34.

**Pour qui :** ceux qui parcourent vite le contenu principal, et ceux qui maîtrisent déjà ces sujets. Le défi apprend à poser des détails sur des surfaces courbes et à garder ces surfaces propres : le quotidien du design de carrosserie, de cabine et de fuselage.

**Quand le proposer :** annoncez-le en une phrase à 0:00. Proposez-le pendant l'atelier, à qui a fini le socle et enregistré `lampe_modele_v001.blend` : le défi se fait dans un autre fichier, et la lampe du chapitre 3 n'est pas touchée. La suite se fait après la séance ; chaque étape se termine par un quiz et une comparaison avec le corrigé. Celui qui maîtrise déjà le chapitre 2 peut le faire à la place : il reprend alors le chapitre 3 avec `PRC02_ch2_lampe_modele.blend` ou avec le fichier de secours du chapitre 3.

**Le fichier :** `PRC02_ch2_defi_modelisation.blend`, en tête du défi, enregistré sous `defi_modelisation_v001.blend`. Une collection par étape ; gris clair pour les carrosseries, gris sombre pour les détails finis, orange pour les pièces à travailler. Son LISEZ-MOI résume les recettes.

| Étape | Ce qu'on apprend | Sur quelle pièce |
|---|---|---|
| 1 | Tendre une arête en subdivision : boucles de maintien, *Crease*. Facultative | Un carter de projecteur ; un capot |
| 2 | *Shrinkwrap* : *Target*, *Offset* `0.2mm`, puis *Solidify* en dessous | Une plaque sur un nez de tram |
| 3 | *Snap Mode*, le mode *Project*, le *Vertex Group* | Un cadre de hublot, un bandeau de tram, une prise d'air |
| 4 | Les quatre modes ; l'ordre *Subdivision*, *Shrinkwrap*, *Solidify* | Un cadre de hublot à 8 côtés |
| 5 | Le *Boolean* et son objet de coupe | Une découpe de hublot |
| 6 ★★ | *Data Transfer* et *Weighted Normal* | Le hublot découpé ; une platine percée |
| Atelier | Tout | Un rétroviseur extérieur |

Le palier 1, les étapes 1 à 4, dure environ 90 minutes ; le palier 2, 55 minutes ; l'atelier, 35 minutes. Huit quiz servent de points d'arrêt.

**Le corrigé :** la collection masquée « Corrigé défi modélisation », avec une sous-collection par étape, de « Corrigé étape 1 » à « Corrigé étape 6 », et « Corrigé atelier ». Les pièces corrigées sont à la place de celles à travailler : on affiche la sous-collection, puis on masque sa pièce (`H`). Les variantes ★★ de l'atelier n'ont pas de corrigé.

**L'accompagner sans y passer la séance :** renvoyez à la recette, au quiz et au corrigé de l'étape. Conseillez d'afficher seulement la collection de l'étape en cours, et la vue locale (`/` du pavé numérique). Qui connaît la subdivision commence à l'étape 2. Le groupe passe d'abord : le défi attend vos tours de postes.

**Pièges principaux :**
- Un détail qui scintille par plaques : il est exactement sur la surface. *Offset* `0.2mm`.
- Un détail qui disparaît dans la carrosserie : il partait de l'intérieur. *Snap Mode* sur *Above Surface*.
- Une épaisseur qui disparaît : le *Solidify* est au-dessus du *Shrinkwrap*.
- Un *Boolean* sans effet : l'objet de coupe est conformé sur la pièce qu'il découpe. Il doit viser la copie `_reference`.
- ★★ Des plaques et de grands triangles : *Smooth by Angle* est resté sous *Data Transfer*. Désactivez son épingle, puis *Move to Last* sur *Data Transfer*.

## Gérer l'hétérogénéité

### Le parcours « première fois »

- Les binômes et les copilotes de l'initiation restent en place.
- Tous partent du fichier de départ : aucun blocage personnel à réparer.
- Le LISEZ-MOI donne chaque geste et chaque valeur avec son unité. Les valeurs restent indicatives : chacun peut les adapter à son concept.
- Le socle de chaque séquence suffit : il couvre tous les points du programme. Les ★ restent des options.
- À chaque point de contrôle, passez d'abord par les postes des débutants.
- Les termes de l'interface restent en anglais : traduisez-les à l'oral la première fois (*Thickness*, l'épaisseur ; *Count*, le nombre de copies).
- **Un apprenant très en retard** prend la pièce qui lui manque dans *Corrigé*. Il supprime sa version, sélectionne la pièce corrigée, fait `M` vers *Lampe*, puis la renomme sans `_corrige`. Pour la grille ou la molette, il sélectionne aussi son *Empty*. Il reprend avec le groupe à la séquence suivante.

### Pour ceux qui avancent vite

- Les paliers ★ de chaque séquence, dans le LISEZ-MOI, puis ceux de l'atelier.
- **La chape (★★) :** une chape en U pour l'articulation du haut, modélisée par moitié avec *Mirror*, *Clipping* et *Bisect* (figure 2.6). Elle prend la place de la molette du haut : c'est l'une ou l'autre.
- **La tête tulipe (★★) :** le cône remplacé par un profil de Bézier, puis *Screw* et *Solidify*. La pile la plus complète du chapitre.
- **Les ressorts (★★) :** un cercle de Bézier décalé de l'axe, et un *Screw* avec une valeur de *Screw* et plusieurs *Iterations*, comme sur les lampes d'architecte. Un *Mirror* donne le second.
- **Percer la grille (★★) :** un *Boolean* en *Difference* sur le socle, avec la grille comme objet (figure 2.31). La lamelle, prolongée vers le bas sur 6 mm de haut, donne des fentes de 3 mm. La grille passe en *Wire*, *Renders* décoché. Changer *Count* change le nombre de fentes.
- **Une grille au dos de l'abat-jour (★★) :** la même couronne, sur l'axe incliné de la tête.
- Leurs solutions : *Corrigé défis*, sous-collections *Chape*, *Tulipe*, *Ressorts*, *Perçage* et *Grille tête*.
- **La liseuse de cabine (★★) :** `PRC02_ch2_liseuse_depart.blend` (figure 2.32), enregistré sous `liseuse_modele_v001.blend`. Six étapes dans son LISEZ-MOI : la platine, les vis en symétrie, le bouton moleté, le col de cygne, la tête en coque et le diffuseur. Son corrigé est dans sa collection masquée *Corrigé*. Le bouton a 16 crans : son *Empty* tourne de 22,5° autour de Y.
- Le défi facultatif « Modélisation avancée ».
- Le rôle de copilote, comme à l'initiation.

## Animer : ce qui change au chapitre 2

Les conseils de l'initiation restent valables : « Regardez, puis à vous », les touches dites à voix haute, les post-it vert et rose, la règle des 3 minutes, la souris qu'on ne prend pas. Ceux du chapitre 1 aussi : l'unité dite avec le `=`, le corrigé qu'on compare sans le copier. Ce chapitre en ajoute six :
1. **Faites vivre la règle du jour.** À chaque modificateur, ouvrez le menu de son en-tête et montrez *Apply* sans cliquer. Dites la différence à voix haute : appliquer l'échelle, oui ; appliquer un modificateur, non.
2. **Prouvez le non destructif.** En fin de séquence, changez une valeur en direct : l'épaisseur, *Count*, une poignée. Le client de l'atelier posera la même question.
3. **Annoncez le mode.** « Tab : Mode Édition. » Les pièges du jour viennent souvent d'un geste fait dans le mauvais mode : la tige décalée en Mode Objet, `X` qui supprime toute la tête, la lamelle dont l'origine quitte le centre.
4. **Dites où est le curseur 3D.** Chaque nouvelle pièce y apparaît : `Maj + C` ou `Maj + S > Cursor to Selected` avant `Maj + A`. La grille, la molette, l'ampoule et les articulations en dépendent.
5. **Laissez chercher les angles.** La règle « 360° divisé par le nombre de copies » se dit ; l'angle de la molette et celui du bouton de la liseuse se trouvent. Évitez 24 copies dans vos démos.
6. **Tenez les cycles courts.** C'est le chapitre le plus chargé de la formation : une notion, puis la souris. Si une démo déborde, coupez l'« Ailleurs » plutôt que le guidé.

## Si vous prenez du retard

Raccourcissez dans cet ordre :

| Ordre | Ce que l'on coupe | Ce que l'on garde |
|---|---|---|
| D'abord | Le fichier de démos : chaque « Ailleurs » se dit en une phrase, sans ouvrir le fichier | Le lien avec les métiers, à l'oral |
| Ensuite | Les autonomies de la répétition et du câble : la molette passe en palier ★ de l'atelier ; le second tracé du câble saute | Les cycles guidés ; la découverte du *Bevel* sur le socle, faite en guidé, pas à pas, si le temps manque |
| Ensuite | L'ampoule : démo seule. Les apprenants prennent celle du corrigé (`M` vers *Lampe*, renommée *Ampoule*) et retouchent son profil | Le principe de la révolution |
| En dernier | L'atelier : les articulations restent les sphères du blocage | La checklist et l'enregistrement |

**Ce qui ne saute jamais :** *Mirror*, *Solidify*, la grille d'aération en *Array* et le câble en Bézier, car ils portent les points du programme. Ni *Shade Auto Smooth*, dont le chapitre 3 dépend, ni l'enregistrement sous `lampe_modele_v001.blend`. Si le retard est important, `PRC02_ch2_lampe_modele.blend` garantit à tous le même départ au chapitre 3.

## Si vous êtes en avance

- **L'atelier s'enrichit :** les paliers ★, puis les défis ★★, en commençant par la chape ou la tête tulipe. La liseuse, pour qui veut un objet de son secteur.
- **Le retour s'allonge :** chacun change une valeur en direct sur sa lampe, au lieu d'un seul volontaire.
- **Le défi facultatif :** son palier 1, pour les plus à l'aise.

---

Les fichiers du chapitre se reconstruisent avec les scripts de `tool/exercices_ch2/` (`croquis_ampoule.py`, `build_lampe.py`, `build_liseuse.py`, `build_demos.py`, puis `finish_ui.py`) et de `tool/exercices_ch2_defi/` (`build_defi_modelisation.py`, puis `finish_ui_defi.py`), dans Blender 5.2 en arrière-plan. Ce document se convertit en PDF avec `tool/deroule_initiation/export_pdf.ps1 -Source _resources\PRC02-deroule-chap2.md`.
