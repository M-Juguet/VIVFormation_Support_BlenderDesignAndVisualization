# Chapitre 2 · Section 4 · Défi facultatif : modélisation avancée : plan

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 4 et travail personnel · Complément facultatif, hors programme de base · Plan rédigé le 18 novembre 2026, **validé le même jour par la session principale, par délégation du formateur**, avec quatre ajustements (décision 16) ; à confirmer par le formateur

## En bref

- **Un complément facultatif, hors programme de base :** le défi n'est pas prévu dans la formation initiale. Il ajoute des techniques de modélisation utiles en design de transport, que le chapitre 2 ne couvre pas. L'écran Programme, le titre de la section et son introduction le signalent comme facultatif.
- **Pour qui :** deux profils d'apprenants :
  - ceux qui parcourent vite les contenus de base, parce qu'ils sont à l'aise ;
  - ceux qui maîtrisent déjà ces sujets en début de formation.

  Le chapitre 2 apprend à modéliser un objet de façon non destructive, avec des modificateurs et des courbes. Ce défi apprend à **poser des détails sur des surfaces courbes** et à garder ces surfaces propres : le quotidien du design de carrosserie, de cabine et de fuselage.
- **Forme :** une section 4 du chapitre 2 dans l'application, « 4. Défi facultatif · Modélisation avancée ». Elle a sa propre ancre, `ch2_sec4_title`, et un quatrième point au programme, « Défi facultatif : modélisation avancée ». Elle se lit en autonomie : recettes, captures et quiz, avec les modules existants. Tant que le contenu de base du chapitre 2 n'est pas rédigé, le chapitre s'ouvre sur un encart qui l'annonce, puis sur le défi.
- **Moment :** au choix de l'apprenant.
  - **À la suite des parties de base,** s'il lui reste du temps : en séance, puis après la séance si besoin.
  - **À la place des parties de base,** pour l'apprenant qui veut des défis plus poussés. Il reprend alors le chapitre 3 avec un fichier de secours (voir « Quand et comment »).
- **Périmètre :** 6 étapes en 2 paliers, puis un atelier, pour environ 3 heures de travail.
  - Palier 1, le cœur, 90 minutes, faisable en séance : la surface de référence en subdivision, puis le shrinkwrap en trois étapes (à quoi il sert, trois cas d'usage, les réglages).
  - Palier 2, 55 minutes : les booléens non destructifs, puis, en ★★, des normales propres sur une surface coupée.
  - Atelier, 35 minutes : un rétroviseur extérieur automobile. Deux variantes ★★ : un cadre de vitre frontale de tram, un hublot sur un fuselage.
- **Le shrinkwrap peut s'aborder directement :** les surfaces de référence sont déjà prêtes dans le fichier. L'étape 1 est utile, mais un apprenant qui connaît la subdivision peut commencer à l'étape 2.
- **Supports :** un seul fichier, `PRC02_ch2_defi_modelisation.blend`, pour toutes les étapes et l'atelier. Les pièces viennent des trois secteurs : fuselage d'avion d'affaires, nez de tram, capot et rétroviseur automobiles.
- **Le rôle du formateur :** il ne fait aucune démonstration. Il annonce la section en une phrase, passe voir les apprenants concernés et les renvoie aux corrigés. Le minutage du chapitre 2 ne change pas.
- **Affichage :** tout fonctionne en *Solid*, en *Material Preview* et au rendu EEVEE : le défi ne touche qu'à la géométrie et aux normales. Les recettes ont été vérifiées dans Blender 5.2.1 LTS et rendues sous EEVEE. Aucune ne dépend de Cycles.
- **Corrigés :** dans le fichier de travail, dans la collection masquée « Corrigé défi modélisation », avec une sous-collection par étape et une pour l'atelier. Il n'y a aucun fichier séparé.
- **Vérification des acquis :** 8 quiz dans l'application. Il n'y a pas de grille d'autoévaluation.

## Objectifs

À la fin du défi, l'apprenant sait :
- tendre les arêtes d'une surface en subdivision, avec des boucles de maintien ou le *Crease* ;
- expliquer à quoi sert le shrinkwrap, et pourquoi il est si répandu en design de transport ;
- conformer un détail à une carrosserie ou à un fuselage, avec le mode adapté : *Nearest Surface Point*, *Project*, *Nearest Vertex* ou *Target Normal Project* ;
- régler *Snap Mode* et *Offset* pour qu'un détail reste dehors, sans scintiller ;
- limiter le shrinkwrap à une partie du détail, avec un groupe de sommets ;
- placer *Shrinkwrap*, *Subdivision* et *Solidify* dans le bon ordre ;
- découper une pièce sans la détruire, avec un *Boolean* et un objet de coupe ;
- en ★★, nettoyer l'ombrage d'une surface coupée, avec *Data Transfer* ou *Weighted Normal*.

## Prérequis : ce que l'initiation et les chapitres 1 et 2 ont déjà montré

Le défi part de ces acquis, sans les reprendre. **Il peut se faire dès le chapitre 1**, avant que le chapitre 2 soit enseigné : les acquis du chapitre 2 sont alors rappelés dans l'encart NOTE « Si vous n'avez pas encore suivi le chapitre 2 » (ci-dessous).

| Déjà vu | Origine | Où | Ce que le défi en fait |
|---|---|---|---|
| Le modificateur *Subdivision Surface*, `Ctrl + 1`, `Ctrl + 2` | Basics | Basics 103, section 3 | La surface de référence (étape 1) |
| *Loop Cut* (`Ctrl + R`), la sélection de boucle (`Alt + clic`) | Basics | Basics 103, section 2 | Les boucles de maintien ; la sélection du bord d'une prise d'air |
| La pile de modificateurs, son ordre, *Apply* | Basics | Basics 103, section 3 | L'ordre *Subdivision*, *Shrinkwrap*, *Solidify*, *Boolean*, *Bevel* |
| Le *Boolean*, cité | Basics | Basics 103, section 3 | Les découpes non destructives (étape 5) |
| La saisie d'une valeur avec son unité, `=` pendant un geste | Chapitre 1 | Section 1 | Toutes les valeurs : `0.2mm` dans un champ, `G X = 500mm` pendant un geste |
| La vue locale (`/` du pavé numérique) | Chapitre 1 | Section 2 | Isoler une pièce et sa surface de référence |
| *Solidify* : *Thickness*, *Offset* | Chapitre 2 (rappel dans l'encart) | 0:35 | L'épaisseur de chaque détail conformé |
| *Bevel* (modificateur) : *Amount*, *Segments*, *Limit Method* sur *Angle* | Chapitre 2 (rappel dans l'encart) | 0:35 | L'arrondi d'une découpe (étape 5) |
| *Shade Auto Smooth* (*Smooth by Angle*) | Chapitre 2 (rappel dans l'encart) | 0:35 | Le lissage de toutes les pièces ; il reste en bas de la pile |

Pour commencer, l'apprenant doit savoir ajouter un modificateur, le régler et changer sa place dans la pile. En cas de doute, il relit Basics 103, section 3. Quand le contenu de base du chapitre 2 sera en ligne, ses quiz serviront de test d'entrée.

**Encart NOTE « Si vous n'avez pas encore suivi le chapitre 2 »,** en tête de la section 4, juste après l'introduction. Des rappels, pas des leçons :
- *Solidify* (*Add Modifier > Generate*) donne une épaisseur à une surface : *Thickness* règle l'épaisseur ; *Offset* la place, à `-1` sous la surface, à `0` de part et d'autre, à `1` dessus.
- Le modificateur *Bevel* (*Add Modifier > Generate*) arrondit les arêtes : *Amount* règle la largeur du biseau (la propriété *Width*), *Segments* son arrondi ; *Limit Method* sur *Angle*, le réglage par défaut, ne biseaute que les arêtes vives.
- *Object > Shade Auto Smooth* lisse l'affichage sans arrondir les arêtes vives. Il ajoute le modificateur *Smooth by Angle*, qui reste toujours en bas de la pile.
- Vu au chapitre 1 : pendant un geste, `=` ouvre la saisie avec unité (`G X = 500mm`) ; `/` du pavé numérique isole la sélection (vue locale).

## Ce que le défi n'aborde pas

- ***Lattice* :** cité en une phrase, dans « Pour aller plus loin ». Il déforme d'un coup tout un ensemble de pièces, avec une cage. Le budget de 3 heures ne permet pas d'en faire une étape.
- **La contrainte *Shrinkwrap* :** elle pose un objet entier sur une surface, sans le déformer, par exemple une vis ou un écusson. Elle est citée en note à l'étape 4.
- **La retopologie :** le même principe sert à poser un maillage propre sur une forme sculptée ou scannée. Elle est citée en une phrase dans la théorie (étape 2).
- **Le reste :** *Surface Deform*, *Mesh Deform*, les Geometry Nodes, *Normal Edit*, la sculpture, les surfaces NURBS et l'import de CAO. Le défi reste en maillage, avec les modificateurs livrés avec Blender, sans extension.
- **Les matières, l'éclairage et le rendu :** ils restent aux chapitres 3 et 4. Le fichier contient seulement trois matières neutres, pour distinguer les carrosseries, les détails finis et les pièces à travailler.

### Ce qui n'est pas fidèle sous EEVEE ou en *Material Preview*, et ce que l'on fait

Le shrinkwrap, la subdivision, le booléen et les normales sont calculés avant l'affichage : le résultat est le même en *Solid*, en *Material Preview* et au rendu EEVEE. Les points ci-dessous concernent la lecture du résultat, pas la technique.

| Ce que l'on voit | Pourquoi | Ce que l'on fait | Étape |
|---|---|---|---|
| Le détail scintille par plaques, en vue comme au rendu | Il est exactement sur la surface (*Offset* à 0) : les deux surfaces se disputent l'affichage | *Offset* de 0,2 mm, ou un *Solidify* vers l'extérieur | 2 |
| Le détail disparaît dans la carrosserie | Il partait de l'intérieur : en *On Surface*, l'*Offset* s'applique dans le sens du trajet, donc vers l'intérieur | *Snap Mode* sur *Above Surface* | 3.1 |
| Des traînées et un halo d'ombrage autour d'une découpe, surtout en *Material Preview* et sous EEVEE, avec les reflets | Le booléen crée des faces longues et fines ; le lissage les interpole mal sur une surface courbe | ★★ *Data Transfer* des normales depuis la surface non coupée | 6 |
| Des triangles d'ombrage sur une platine plane, biseautée et percée | Même cause, sur une face plane | ★★ *Weighted Normal* | 6 |
| Les normales transférées donnent des plaques et de grands triangles | *Smooth by Angle*, épinglé en bas de la pile, recalcule les arêtes vives après *Data Transfer* et dérègle les normales | Désépingler *Smooth by Angle* et le placer au-dessus de *Data Transfer* ou de *Weighted Normal* | 6 |
| Le transfert ne prend que par endroits | La surface de référence n'a pas le même niveau de subdivision que la pièce : les deux surfaces ne coïncident plus | Le même niveau de subdivision pour la pièce et sa référence | 6 |
| Une rainure étroite se hérisse de grands triangles | Un *Bevel* sous le *Boolean* biseaute les longues arêtes du booléen | Pas de *Bevel* sur une ligne de joint : elle reste vive | 5 |
| L'objet de coupe apparaît au rendu | *Display As* ne change que la vue 3D | Décocher *Renders* dans *Visibility* | 5 |
| L'affichage ralentit | Booléen *Exact* sur une surface très subdivisée | Garder la subdivision au niveau 2 dans la vue ; masquer les collections des autres étapes | 5, 6 |
| Un arrondi « au rendu », sans géométrie | Le nœud *Bevel* des matières ne fonctionne que sous Cycles | Le modificateur *Bevel*, géométrique, fonctionne partout | 5 |

**Pour lire une surface :** en *Solid*, le menu *Viewport Shading* propose l'éclairage *MatCap*. Les images `check_reflection_horizontal` et `check_reflection_vertical` dessinent des bandes de reflet, comme les néons d'une cabine de contrôle qualité. Une bande cassée ou qui tremble signale un défaut. C'est une option, conseillée aux étapes 1 et 6.

**Pour les tutoriels anciens :** jusqu'à Blender 4.0, il fallait cocher *Auto Smooth* pour que *Data Transfer* et *Weighted Normal* agissent. Cette case n'existe plus depuis Blender 4.1 : les deux modificateurs agissent seuls. Un encart NOTE le dit à l'étape 6.

## Quand et comment

**L'annonce.** À l'ouverture du chapitre 2, le formateur signale le défi en une phrase : « Pour ceux qui sont à l'aise, ou qui connaissent déjà ces sujets : un défi facultatif, hors programme, en section 4 du chapitre 2 dans l'application, avec le fichier `PRC02_ch2_defi_modelisation.blend`. » Il ne fait aucune démonstration, et le minutage du chapitre 2 ne change pas.

**À la suite des parties de base.** L'apprenant suit le chapitre 2, puis ouvre le défi quand il lui reste du temps, en séance ou après. Il enregistre d'abord `lampe_modele_v001.blend` : le défi se fait dans un autre fichier, et la lampe qui part au chapitre 3 n'est pas touchée.

**À la place des parties de base.** L'apprenant qui maîtrise déjà le chapitre 2 peut faire le défi à sa place. Il n'a alors pas forcément `lampe_modele_v001.blend`, le point de départ du chapitre 3. Au choix, il reprend le chapitre 3 :
- avec le fichier de secours du chapitre 3, `PRC02_ch3_lampe_a_habiller.blend`, enregistré sous `lampe_habillage_v001.blend`, comme le prévoit le check-up du chapitre 3 ;
- ou avec le corrigé du chapitre 2, `PRC02_ch2_lampe_modele.blend`, enregistré sous `lampe_modele_v001.blend` : il suit alors le check-up du chapitre 3 comme tout le monde.

C'est une option, pas une obligation. L'encart d'introduction de la section 4 le dit en deux phrases. Ces deux fichiers seront construits avec les fichiers du chapitre 2 et du chapitre 3.

**Après la séance.** L'apprenant reprend à l'étape où il s'est arrêté. Chaque étape se termine par un point d'arrêt : un quiz de l'application et la comparaison avec le corrigé.

**Le même ordre à chaque étape :**
1. **Exemple :** une pièce terminée dans le fichier. L'apprenant l'observe, puis ouvre sa pile de modificateurs.
2. **Pratique guidée :** une recette numérotée, refaite sur une pièce à compléter, en orange.
3. **Petit défi :** une variante sans recette complète, avec son corrigé.

**Les secteurs tournent d'une étape à l'autre :** dans chaque étape, l'exemple, la pratique et le petit défi viennent de secteurs différents.

| Étape | Exemple | Pratique guidée | Petit défi |
|---|---|---|---|
| 1 | Carters de projecteur (tous secteurs) | Le même carter | Capot à ligne de caractère (auto) |
| 2 | Trappe d'accès sur un fuselage (aéro) | Plaque de numéro de rame sur un nez de tram (ferro) | Monogramme sur un capot (auto) |
| 3 | Les trois cas d'usage : cadre de hublot (aéro), bandeau sur un nez de tram (ferro), prise d'air sur un capot (auto) | Les mêmes, à compléter | Deux hublots de plus (aéro) ; ★ grille de capot (auto) |
| 4 | Les quatre modes sur une main courante à 12 pans (ferro) | Cadre à 8 côtés sur un fuselage (aéro) | Jonc d'aile (auto) |
| 5 | Logement de poignée affleurante sur une portière (auto) | Découpe de hublot dans un fuselage (aéro) | Ligne de joint d'une trappe de visite sur un nez de tram (ferro) |
| 6 ★★ | Découpe de hublot, avant et après (aéro) | La même ; platine percée (auto) | La ligne de joint du nez de tram (ferro) |
| Atelier | Rétroviseur extérieur (auto) | | Variantes ★★ : cadre de vitre frontale de tram (ferro), hublot et son cadre (aéro) |

## La progression

### Une notion nouvelle à la fois

Chaque étape introduit une seule notion. Ses réglages arrivent un par un, dans des sous-étapes. Les sous-étapes marquées ★ sont facultatives ; l'étape 6 et les variantes de l'atelier sont ★★.

| Étape | Durée | La notion nouvelle | Les réglages, dans l'ordre | Elle s'appuie sur |
|---|---|---|---|---|
| Avant de commencer | 5 min | Le fichier du défi | Collections, vue locale, option *MatCap* | Chapitre 1 |
| **Palier 1** | | | | |
| 1 · La surface de référence | 15 min | Tendre une arête en subdivision | `Ctrl + 2`, boucles de maintien (`Ctrl + R`), *Crease* (`Maj + E`) | *Subdivision Surface*, *Loop Cut* (Basics 103) |
| 2 · Le shrinkwrap | 15 min | Conformer un maillage à une surface | *Shrinkwrap*, *Target*, *Offset*, puis *Solidify* en dessous | La pile ; *Solidify* (chapitre 2) |
| 3 · Trois cas d'usage | 35 min | Un réglage par cas | 3.1 *Snap Mode* ; 3.2 *Project* (axe, *Negative* / *Positive*, *Face Cull*) ; 3.3 *Vertex Group* | Étape 2 |
| 4 · Les réglages et la pile | 20 min | Choisir le mode et l'ordre | *Nearest Vertex*, *Target Normal Project* ; *Subdivision* avant et après | Étapes 1 à 3 |
| **Palier 2** | | | | |
| 5 · Les booléens non destructifs | 30 min | Découper avec un objet de coupe | *Boolean* *Difference* ; *Display As* ; *Renders* ; ordre avec *Bevel* ; outil conformé | La pile ; *Bevel* (chapitre 2) ; étape 3 |
| 6 ★★ · Des normales propres | 25 min | Corriger l'ombrage sans toucher à la forme | *Data Transfer* (*Custom Normals*) ; *Weighted Normal* | Étape 5 |
| **Atelier** · Le rétroviseur | 35 min | Aucune : il réinvestit les étapes 1 à 6 | | Étapes 1 à 6 |

Durée totale : 180 minutes, soit environ 3 heures. Palier 1 : 90 minutes, avec l'accueil ; palier 2 : 55 minutes ; atelier : 35 minutes. Les durées sont indicatives : un apprenant à l'aise va plus vite.

### Les repères d'échelle

Le fichier est en millimètres, et toutes les pièces sont à l'échelle réelle :
- le fuselage est celui d'un avion d'affaires, de 2 m de diamètre ;
- le nez de tram mesure 1,6 m de large et 1,2 m de haut ;
- le capot mesure 1 m sur 0,8 m ;
- le rétroviseur mesure environ 250 mm de large.

Les valeurs se tapent avec leur unité. Dans un champ, on tape `0.2mm` ; pendant un geste, on tape `G X = 500mm`, avec le `=`. Pour un détail posé sur une carrosserie, l'*Offset* va de 0,1 à 0,5 mm, et l'épaisseur de 1,5 à 4 mm.

## Les recettes, étape par étape

Conventions :
- les menus sont ceux de Blender 5.2, vérifiés dans le code de l'interface ;
- les valeurs se tapent avec leur unité ;
- « la pile » désigne la liste des modificateurs, dans l'onglet *Modifiers* (la clé à molette) de l'éditeur de propriétés ;
- *Smooth by Angle*, ajouté par *Shade Auto Smooth*, porte l'épingle *Pin to Last* : il reste toujours en bas de la pile, et chaque nouveau modificateur se range au-dessus de lui.

### Les menus des modificateurs dans Blender 5.2

Le bouton *Add Modifier* de l'onglet *Modifiers* ouvre quatre catégories pour un maillage. `Maj + A`, la souris au-dessus de l'onglet, ouvre le même menu.

| Modificateur | Chemin |
|---|---|
| *Subdivision Surface*, *Solidify*, *Bevel*, *Boolean* | *Add Modifier > Generate* |
| *Shrinkwrap* ; *Lattice*, cité | *Add Modifier > Deform* |
| *Data Transfer* | *Add Modifier > Edit* |
| *Weighted Normal* ; *Normal Edit*, non utilisé | *Add Modifier > Normals* |

Dès que le menu est ouvert, il suffit de taper le nom du modificateur : la recherche démarre au clavier. Elle est conseillée aux apprenants.

### Avant de commencer (5 min)

**Nouveau :** le fichier du défi. **Déjà vu :** les collections, la vue locale.

1. Ouvrir `PRC02_ch2_defi_modelisation.blend`, puis l'enregistrer sous `defi_modelisation_v001.blend`.
2. Afficher seulement la collection de l'étape en cours (l'œil de l'Outliner). Pour travailler sur une pièce, la sélectionner avec sa surface de référence, puis `/` du pavé numérique : la vue locale. Le même raccourci ramène la vue complète.
3. Repérer les couleurs : gris clair pour les carrosseries, gris très sombre pour les détails finis, orange pour les pièces à travailler.
4. Option : *Viewport Shading > Lighting* sur *MatCap*, image `check_reflection_horizontal`, pour lire les reflets (figure 2.59). Retour : *Studio*.

**Erreurs fréquentes :**
- La vue locale n'affiche rien : aucune pièce n'était sélectionnée. `/` pour sortir, sélectionnez, puis `/` à nouveau.
- Tout est lent : toutes les collections sont affichées. Masquez celles des autres étapes.

### Palier 1

### Étape 1 · La surface de référence en subdivision (15 min)

**Nouveau :** tendre une arête dans une surface en subdivision, avec des boucles de maintien, puis avec le *Crease*. **Déjà vu :** *Subdivision Surface* (Basics 103), *Loop Cut*, la sélection de boucle.

Cette étape est facultative pour qui connaît déjà la subdivision : toutes les surfaces de référence des étapes suivantes sont prêtes dans le fichier.

**Pourquoi cette étape :** en design de transport, les carrosseries, les nez et les fuselages sont des surfaces douces et tendues. En maillage, on les obtient avec une cage légère et le modificateur *Subdivision Surface*. Le shrinkwrap a besoin de ces surfaces propres : un détail conformé épouse chaque défaut de sa cible.

**Exemple :** trois carters de projecteur de 120 × 80 × 40 mm, avec la même cage et la même *Subdivision* au niveau 2 :
- `E1_Exemple_Sans` : sans rien de plus, le carter devient un savon ;
- `E1_Exemple_Boucles` : avec des boucles de maintien à 4 mm des arêtes, les arêtes se tendent ;
- `E1_Exemple_Crease` : avec un *Crease* de 1 sur les arêtes, elles deviennent vives, sans géométrie de plus.

**1.1 · La subdivision,** sur `E1_Pratique_Boucles` (cube de 120 × 80 × 40 mm, sans modificateur).
1. En Mode Objet, `Ctrl + 2` : un modificateur *Subdivision Surface* au niveau 2 rejoint la pile. Le carter devient un savon.
2. Dans le modificateur : *Levels Viewport* 2, *Render* 2. Gardez ces valeurs : au-delà, l'affichage ralentit pour un gain invisible.

**1.2 · Les boucles de maintien,** sur la même pièce.
1. `Tab` : Mode Édition. Le savon montre sa cage, le cube.
2. `Ctrl + R`, survolez une arête verticale : l'aperçu jaune d'une boucle horizontale apparaît. Cliquez, puis glissez la boucle près du dessus, à environ 4 mm, et cliquez. Les arêtes du dessus se tendent.
3. Même geste près du dessous.
4. Même geste sur une arête horizontale de la longueur, puis de la largeur, près de chaque extrémité : quatre boucles de plus. Les arêtes verticales se tendent à leur tour.
5. `Tab` : Mode Objet.

**À retenir :** plus la boucle est proche de l'arête, plus l'arête est vive. La valeur exacte n'a pas d'importance.

**1.3 · Le *Crease*,** sur `E1_Pratique_Crease` (la même cage, déjà subdivisée).
1. `Tab`, puis `2` : sélection des arêtes.
2. `Alt + clic` sur une arête du dessus : toute la boucle du bord du dessus est sélectionnée.
3. `Maj + E`, tapez `1`, puis `Entrée` : le *Crease* de ces arêtes vaut 1, et elles deviennent vives. Le même réglage est dans le menu *Edge > Edge Crease*.
4. Option : refaites le geste avec `0.6` : l'arête s'adoucit.

**Les deux méthodes :**
- les boucles de maintien restent dans la géométrie : elles se lisent dans tous les logiciels, et elles règlent le rayon de l'arête ;
- le *Crease* est un réglage de Blender : il est rapide et se modifie à tout moment. Le modificateur le lit grâce à la case *Use Creases*, cochée par défaut, dans sa rubrique *Advanced*.

**Rendu attendu :** les deux pratiques ressemblent aux exemples `_Boucles` et `_Crease`.

**Erreurs fréquentes :**
- La boucle n'apparaît pas : la souris n'est pas sur une arête. Approchez-la d'une arête, jusqu'à l'aperçu jaune.
- Tout le carter devient vif : le *Crease* a été mis sur toutes les arêtes. `Maj + E`, puis `0` sur celles qui doivent rester douces.
- Une bosse ou un creux près d'un coin : une boucle a été glissée trop loin, jusqu'à croiser une autre boucle. `Ctrl + Z`.

**Petit défi (encart CAUTION) · Le capot à ligne de caractère (auto) :** `E1_Defi_Capot` est la cage d'un capot, déjà subdivisée. Sa nervure centrale est molle. Rendez-la vive, sans toucher au reste du capot. Solution : `Alt + clic` sur la boucle de la nervure, `Maj + E`, `0.8`. Corrigé : sous-collection « Corrigé étape 1 ».

### Étape 2 · Le shrinkwrap : à quoi il sert (15 min)

**Nouveau :** le modificateur *Shrinkwrap* et son *Offset*. **Déjà vu :** la pile, *Solidify*.

**La théorie (un `TextModule`, puis un encart IMPORTANT).**
- **Ce qu'il fait :** le *Shrinkwrap* déplace chaque sommet d'un objet jusqu'à une surface cible, comme un film rétractable chauffé sur une forme. L'objet garde son propre maillage : seuls ses sommets bougent. Tant que le modificateur n'est pas appliqué, rien n'est détruit.
- **Pourquoi il est partout en design de transport :**
  - les carrosseries, les nez de train et les fuselages sont des surfaces à double courbure, tendues et continues ;
  - les détails doivent s'y poser exactement : prises d'air, grilles, cadres de vitre, joints, logos, trappes, optiques ;
  - la carrosserie change à chaque revue de design. Un détail conformé suit chaque modification, sans être remodelé ;
  - le détail se dessine à plat, simplement et au millimètre, d'après un croquis ou un profil de CAO. Le shrinkwrap le pose ensuite sur la courbe ;
  - on ne découpe pas la carrosserie pour y loger le détail : son maillage reste propre, et ses reflets aussi.
- **Ailleurs :** le même principe sert à conformer un maillage à une surface de référence : un scan, une surface importée de la CAO, ou une forme sculptée qu'on retopologise.

**Exemple (aéro) :** sur le tronçon de fuselage `E2_Fuselage`, deux trappes d'accès de 200 × 150 mm. `E2_Exemple_Trappe_plate` est restée plane : ses bords décollent de 3 mm. `E2_Exemple_Trappe` est conformée, avec une épaisseur de 1,5 mm.

**Pratique guidée (ferro),** sur `E2_Pratique_Plaque` : une plaque de numéro de rame de 300 × 120 mm, plane, posée devant le nez de tram `E2_Nez`. Elle touche le nez en son centre ; ses bords en sont loin.

**2.1 · Conformer**
1. Sélectionnez `E2_Pratique_Plaque`. Onglet *Modifiers*, *Add Modifier > Deform > Shrinkwrap*.
2. Champ *Target* : la pipette, puis un clic sur le nez `E2_Nez`. Ou choisissez `E2_Nez` dans la liste.
3. La plaque épouse le nez. Elle garde ses sommets ; seules leurs positions changent.

**2.2 · Décoller de 0,2 mm**
1. La plaque scintille par plaques : elle est exactement sur la surface du nez, et les deux se disputent l'affichage.
2. *Offset* : tapez `0.2mm`. Le scintillement disparaît.

**2.3 · L'épaisseur**
1. *Add Modifier > Generate > Solidify*. Il se range sous le *Shrinkwrap*.
2. *Thickness* `2mm`, *Offset* `1` : l'épaisseur part vers l'extérieur, perpendiculaire à la courbe.
3. Option : faites glisser le *Solidify* au-dessus du *Shrinkwrap* (la poignée à droite de son en-tête). L'épaisseur disparaît : ses deux faces sont posées sur le nez. Remettez-le en dessous.

**2.4 · Option : la cible change, le détail suit**
1. Sélectionnez `E2_Nez`, `Tab`, puis déplacez un sommet de la cage au centre : `G Y = -30mm`.
2. La plaque suit la nouvelle forme. `Ctrl + Z` pour revenir.

**Rendu attendu :** une plaque de 2 mm d'épaisseur, posée sur le nez sans scintiller, sans bord qui décolle.

**Erreurs fréquentes :**
- Rien ne bouge : le champ *Target* est vide, ou il désigne la plaque elle-même.
- La plaque reste plane, seuls ses coins bougent : elle n'a que quatre sommets. Le shrinkwrap ne déplace que des sommets : un détail doit en avoir assez pour se courber (voir l'étape 4).
- La plaque disparaît dans le nez : l'*Offset* du *Solidify* vaut -1. Tapez `1`.
- L'épaisseur a disparu : le *Solidify* est au-dessus du *Shrinkwrap*.

**Petit défi (encart CAUTION) · Le monogramme (auto) :** posez `E2_Defi_Monogramme`, une plaque ovale de 120 × 60 mm, sur le capot `E2_Capot`, avec 2 mm d'épaisseur et sans scintillement. Corrigé : sous-collection « Corrigé étape 2 ».

**Point d'arrêt :** les quiz 1 et 2.

### Étape 3 · Trois cas d'usage (35 min)

**Nouveau :** un réglage par cas : *Snap Mode*, puis le mode *Project*, puis la limitation par groupe de sommets. **Déjà vu :** *Shrinkwrap*, *Offset*, *Solidify* en dessous.

**Exemple :** les trois pièces terminées de la collection `Etape_3_Cas_usage` : `E3_Exemple_Hublot`, `E3_Exemple_Bandeau` et `E3_Exemple_Prise`.

**3.1 · Aéro : le cadre de hublot, et *Snap Mode*,** sur `E3_Pratique_Cadre` : un cadre plat de 280 × 380 mm à l'extérieur, 210 × 310 mm à l'intérieur, aux coins arrondis. Il est à moitié enfoncé dans le fuselage `E3_Fuselage`.
1. *Add Modifier > Deform > Shrinkwrap*, *Target* `E3_Fuselage`, *Offset* `0.2mm`.
2. Une partie du cadre scintille ou disparaît. Ses sommets partaient de l'intérieur du fuselage. En *Snap Mode* *On Surface*, le réglage par défaut, l'*Offset* s'applique dans le sens du trajet du sommet : vers l'intérieur.
3. *Snap Mode* : *Above Surface*. Tout le cadre passe 0,2 mm au-dessus de la surface, d'où que partent ses sommets.
4. *Add Modifier > Generate > Solidify*, *Thickness* `4mm`, *Offset* `1`.

Les autres choix de *Snap Mode* :
- *Inside* : ne déplace que les sommets qui sont dehors ; le détail reste dans le volume ;
- *Outside* : ne déplace que les sommets qui sont dedans ; le détail ne s'enfonce jamais, et ses parties qui sont dehors ne bougent pas ;
- *Outside Surface* : comme *On Surface*, mais l'*Offset* va toujours vers l'extérieur.

**3.2 · Ferro : le bandeau sur le nez, et le mode *Project*,** sur `E3_Pratique_Bandeau` : une bande de 1 400 × 60 mm, dessinée de face, à 300 mm devant le nez `E3_Nez`.
1. *Shrinkwrap*, *Target* `E3_Nez`, *Offset* `0.2mm`. En *Nearest Surface Point*, chaque sommet va au point le plus proche : vue de face, la bande se tord vers les côtés du nez.
2. *Wrap Method* : *Project*. Cochez l'axe *Y*. La bande se projette sur le nez droit devant elle : vue de face (`1` du pavé numérique), elle garde exactement son tracé.
3. *Negative* et *Positive* : le sens de la projection, le long de l'axe. *Positive* est coché par défaut : les sommets avancent vers +Y. Option : `G Y = 1000mm` place la bande derrière le nez : elle ne le trouve plus. Cochez *Negative* : elle le retrouve. `Ctrl + Z` deux fois.
4. *Face Cull* : *Off* par défaut. *Back* ignore les faces vues de dos. Sur une carrosserie fermée, il évite qu'un sommet se pose sur la face intérieure.
5. *Add Modifier > Generate > Solidify*, *Thickness* `2mm`, *Offset* `1`.

**À retenir :** *Project* garde le dessin tel qu'on le voit dans l'axe choisi. C'est le mode des bandeaux, des logos et des grilles dessinés de face ou de dessus. Sans axe coché, il projette suivant les normales du détail.

**3.3 · Auto : la prise d'air sur le capot, et le groupe de sommets,** sur `E3_Pratique_Prise` : un bossage de 300 × 200 mm, avec une lèvre avant de 35 mm de haut, posé au-dessus du capot `E3_Capot`.
1. *Shrinkwrap*, *Target* `E3_Capot`. Toute la prise d'air s'aplatit sur le capot : chaque sommet a été conformé.
2. `Tab`, `1` : sélection des sommets. Les sommets du bord arrière et des côtés sont déjà sélectionnés dans le fichier. Sinon, `Alt + clic` sur les boucles de bord, avec `Maj` pour ajouter.
3. `Ctrl + G > Assign to New Group` : un groupe de sommets, au poids 1. Dans l'onglet *Object Data* (le triangle vert), rubrique *Vertex Groups*, double-cliquez sur son nom et tapez `Raccord`.
4. `Tab`. Dans le *Shrinkwrap*, champ *Vertex Group* : `Raccord`. Seul le bord se pose sur le capot ; la lèvre retrouve sa hauteur.
5. Option, pour un raccord plus doux : `Tab`, sélectionnez la rangée de sommets voisine du bord, réglez *Weight* à `0.5` dans la rubrique *Vertex Groups*, puis *Assign*. Le poids dose l'effet : 1, tout l'effet ; 0, aucun effet.
6. *Solidify*, *Thickness* `2mm`, *Offset* `-1`.

Les deux flèches à droite du champ *Vertex Group* inversent le groupe : le shrinkwrap agit alors partout, sauf sur le groupe.

**Rendu attendu :** un cadre de hublot de 4 mm sans scintillement ; un bandeau droit vu de face ; une prise d'air dont le bord se fond dans le capot. Comparez avec les exemples.

**Erreurs fréquentes :**
- *Project* ne fait rien : aucun axe n'est coché et les normales du détail ne regardent pas la cible ; ou bien la cible est derrière le détail et seul *Positive* est coché.
- Des sommets du bandeau restent en l'air : la projection ne rencontre pas le nez, parce que le dessin dépasse sa silhouette. Raccourcissez le dessin ; *Limit* borne la distance de projection.
- Le groupe de sommets n'a aucun effet : son nom n'est pas choisi dans le champ *Vertex Group*, ou les poids valent 0.
- La prise d'air reste plate : le groupe contient tous les sommets. `Tab`, sélectionnez la lèvre, puis *Remove* dans la rubrique *Vertex Groups*.

**Petit défi (encart CAUTION)**
- **Deux hublots de plus (aéro) :** `Maj + D`, `G X = 500mm` sur le cadre terminé, deux fois. Chaque copie garde son modificateur et reste conformée. Puis modifiez la courbure du fuselage en Mode Édition : les trois cadres suivent.
- **★ La grille de capot (auto) :** `E3_Defi_Grille` est une grille de six ouïes, dessinée à plat au-dessus du capot. Posez-la avec *Project* suivant Z, puis donnez-lui 3 mm d'épaisseur.

Corrigé : sous-collection « Corrigé étape 3 ».

**Point d'arrêt :** les quiz 3 et 4.

### Étape 4 · Les réglages et l'ordre dans la pile (20 min)

**Nouveau :** les deux derniers modes, puis la place du *Shrinkwrap* par rapport à *Subdivision*. **Déjà vu :** les étapes 1 à 3.

**Exemple (ferro) :** `E4_Exemple_Modes`, quatre bandes de 45 × 160 mm conformées sur `E4_Main_courante`, un tube volontairement grossier, à 12 pans, de 200 mm de diamètre. Une étiquette nomme le mode de chaque bande.

| Mode | Ce qu'il fait | Quand l'utiliser |
|---|---|---|
| *Nearest Surface Point* (défaut) | Chaque sommet va au point le plus proche de la surface | Le plus souvent ; détails petits devant la courbure |
| *Project* | Chaque sommet se projette suivant un axe, ou sa normale | Un dessin de face ou de dessus qui doit garder son tracé |
| *Nearest Vertex* | Chaque sommet va au sommet le plus proche de la cible | Deux maillages de même topologie, par exemple une copie retouchée qu'on recale sur l'original. Sur une cible légère, le détail s'effondre sur quelques sommets |
| *Target Normal Project* | Comme *Nearest Surface Point*, mais en suivant les normales lissées de la cible | Une cible peu dense : les sommets se répartissent plus régulièrement. Il est plus lent |

Sur la main courante à 12 pans, les chiffres du banc d'essai le montrent :
- en *Nearest Surface Point*, les 287 sommets d'une bande n'occupent que 203 positions : des sommets se superposent sur les arêtes du tube ;
- en *Target Normal Project*, aucun ;
- en *Nearest Vertex*, toute la bande s'effondre sur 6 sommets ;
- en *Project*, l'espacement reste celui du dessin, 4 mm.

**Pratique guidée (aéro),** sur `E4_Pratique_Cadre_8` : un cadre de hublot grossier, à 8 côtés seulement, au-dessus du fuselage `E4_Fuselage`.

**4.1 · Le *Shrinkwrap* seul.** *Shrinkwrap*, *Target* `E4_Fuselage`, *Offset* `0.2mm`, *Snap Mode* *Above Surface*. Seuls ses 16 sommets sont posés : entre eux, les côtés droits s'enfoncent dans la courbe.

**4.2 · *Subdivision* au-dessus.** *Add Modifier > Generate > Subdivision Surface*, puis montez-le au-dessus du *Shrinkwrap* (menu de l'en-tête, *Move to First*). Choisissez *Simple* et *Levels Viewport* `3`. Les côtés reçoivent des sommets, que le *Shrinkwrap* pose sur la courbe : le cadre colle partout, et il garde ses 8 côtés.

**4.3 · *Subdivision* en dessous.** Choisissez *Catmull-Clark*, puis *Move to Last* : le lissage arrive après la pose. Le cadre s'arrondit, mais il quitte la surface par endroits et s'enfonce ailleurs.

**4.4 · L'ordre retenu.** *Subdivision* au-dessus, en *Catmull-Clark* pour un cadre rond, ou en *Simple* pour garder les angles. Puis *Shrinkwrap*, puis *Solidify* (`4mm`, *Offset* `1`).

**4.5 · Option : la subdivision intégrée à *Project*.** En mode *Project*, le champ *Subdivision Levels* subdivise le détail le temps du calcul. Il évite un modificateur de plus.

**À retenir, l'ordre type d'un détail conformé :**
1. ce qui ajoute des sommets (*Subdivision*) ;
2. *Shrinkwrap* ;
3. ce qui donne l'épaisseur (*Solidify*) ;
4. *Smooth by Angle*, toujours en bas.

**Encart NOTE · La contrainte *Shrinkwrap* :** pour poser un objet entier sans le déformer, comme une vis, un rivet ou un écusson rigide, l'onglet *Object Constraints* propose une contrainte *Shrinkwrap*. Elle déplace l'objet, pas ses sommets.

**Erreurs fréquentes :**
- Le détail s'enfonce entre ses sommets : il n'a pas assez de sommets. *Subdivision* au-dessus du *Shrinkwrap*.
- Le détail décolle et s'enfonce par endroits : une *Subdivision* *Catmull-Clark* est sous le *Shrinkwrap*. Montez-la.
- *Move to First* est grisé : le modificateur est déjà en tête. Utilisez la poignée de l'en-tête pour le faire glisser.

**Petit défi (encart CAUTION) · Le jonc d'aile (auto) :** `E4_Defi_Jonc` est un jonc chromé de 600 × 12 mm, très léger (6 segments), au-dessus du capot `E4_Capot`. Trouvez la pile qui le rend lisse, collé au capot, avec 3 mm d'épaisseur. Solution : *Subdivision* (*Catmull-Clark*, 2), *Shrinkwrap* (*Above Surface*, `0.2mm`), *Solidify* (`3mm`). Corrigé : sous-collection « Corrigé étape 4 ».

**Point d'arrêt du palier 1 :** les quiz 5 et 6, et la comparaison avec les corrigés des étapes 1 à 4.

### Palier 2

### Étape 5 · Les booléens non destructifs (30 min)

**Nouveau :** découper une pièce avec un objet de coupe, sans la détruire. **Déjà vu :** la pile, *Bevel* et *Limit Method* (chapitre 2), *Project* (étape 3).

**Exemple (auto) :** `E5_Exemple_Porte`, un panneau de portière bombé, avec le logement d'une poignée affleurante. L'objet de coupe, `E5_Exemple_Coupe`, est affiché en fil de fer.

**Pratique guidée (aéro),** sur `E5_Pratique_Fuselage` : un tronçon de fuselage, avec sa peau de 3 mm (*Subdivision*, puis *Solidify*). L'objet de coupe `E5_Coupe_Hublot` est un pavé aux coins arrondis de 230 × 330 mm, qui traverse la peau.

**5.1 · Découper**
1. Sélectionnez `E5_Pratique_Fuselage`. *Add Modifier > Generate > Boolean*.
2. *Difference* est l'opération par défaut. Champ *Object* : `E5_Coupe_Hublot`.
3. La peau est percée, mais l'objet de coupe la cache encore.

**5.2 · Ranger l'objet de coupe**
1. Sélectionnez `E5_Coupe_Hublot`. Onglet *Object* (le carré orange), rubrique *Viewport Display*, *Display As* : *Wire*, ou *Bounds* pour une simple boîte.
2. Même onglet, rubrique *Visibility* : décochez *Renders*. *Display As* ne change que la vue 3D ; sans ce réglage, l'objet de coupe apparaîtrait au rendu.

**5.3 · La découpe reste vivante.** Déplacez l'objet de coupe : `G X = 100mm`. Le trou suit. `Ctrl + Z`. Faites-le tourner, ou changez son échelle : le trou change aussi.

**5.4 · L'ordre avec *Bevel***
1. Sur le fuselage, *Add Modifier > Generate > Bevel* : il se range sous le *Boolean*. *Amount* `1mm`, *Segments* `3`, *Limit Method* sur *Angle* (le réglage par défaut).
2. Le bord du trou s'arrondit : le biseau s'applique au résultat de la découpe.
3. Faites glisser le *Bevel* au-dessus du *Boolean* : le bord du trou redevient vif. Remettez-le en dessous.

**5.5 · Le solveur.** *Solver* : *Exact* par défaut, le plus fiable. *Float* est plus rapide, mais il échoue sur des faces qui se superposent. *Manifold* est rapide, mais il exige deux maillages fermés, sans trou.

**Rendu attendu :** un fuselage percé d'une découpe de hublot aux bords arrondis de 1 mm, sans objet de coupe visible au rendu.

**Erreurs fréquentes :**
- Rien n'est découpé : l'objet de coupe ne traverse pas la peau. Il doit la dépasser des deux côtés.
- Tout disparaît, sauf la découpe : l'opération est *Intersect*. Choisissez *Difference*.
- L'objet de coupe apparaît au rendu : *Renders* est resté coché.
- Le bord du trou est vif : le *Bevel* est au-dessus du *Boolean*.
- Des traînées d'ombrage autour du trou : c'est l'objet de l'étape 6.

**Petit défi (encart CAUTION) · La ligne de joint d'une trappe de visite (ferro) :** sur le nez `E5_Defi_Nez`, dont la peau fait 6 mm, creusez la ligne de joint d'une trappe de 300 × 200 mm : une rainure de 4 mm de large et 3 mm de profondeur. L'objet de coupe `E5_Defi_Coupe_Joint` est l'anneau de la rainure, dessiné de face, à plat.
1. Conformez-le avec *Project* suivant Y, *Offset* `0`.
2. Donnez-lui son volume : *Solidify* `6mm`, *Offset* `0`. Il déborde alors de 3 mm de chaque côté de la surface : la rainure a partout la même profondeur, même là où le nez tourne. C'est pour cela qu'on conforme l'objet de coupe.
3. Faites la découpe. Pas de *Bevel* : une ligne de joint reste vive, et un biseau sur une rainure aussi étroite la hérisse de grands triangles.

**Le piège :** conformez l'objet de coupe sur `E5_Nez_reference`, la copie du nez non découpée et masquée, et non sur le nez qu'il découpe. Sinon, le nez dépend de l'objet de coupe, qui dépend du nez : Blender détecte une dépendance circulaire, et le *Boolean* ne fait rien. Corrigé : sous-collection « Corrigé étape 5 ».

**Point d'arrêt :** le quiz 7.

### Étape 6 ★★ · Des normales propres (25 min)

**Nouveau :** corriger l'ombrage sans toucher à la forme, en remplaçant les normales. **Déjà vu :** *Shade Auto Smooth*, la découpe de l'étape 5, la surface de référence (étape 1).

**Pourquoi :** autour d'une découpe dans une surface courbe et lissée, le booléen crée des faces longues et fines. Le lissage les interpole mal : des traînées et un halo apparaissent dans les reflets. La forme est juste ; seul l'ombrage est faux. On remplace donc les normales de la zone par celles d'une surface saine.

**Exemple (aéro) :** `E6_Exemple_Brut` et `E6_Exemple_Propre`, deux découpes de hublot identiques, sans puis avec *Data Transfer*. Regardez-les en *Material Preview*, ou en *MatCap* `check_reflection_horizontal`.

**6.1 · *Data Transfer*,** sur `E6_Pratique_Fuselage` : la découpe de l'étape 5, avec ses traînées. `E6_Fuselage_reference` est le même fuselage sans découpe, au même niveau de subdivision (2), masqué et affiché en fil de fer.
1. *Add Modifier > Edit > Data Transfer*. Il se range au-dessus de *Smooth by Angle*, sous le *Bevel*.
2. *Source* : `E6_Fuselage_reference`.
3. Dépliez la rubrique *Face Corner Data* (sa flèche), cochez sa case, puis choisissez *Custom Normals*.
4. Dans la même rubrique, *Mapping* : *Nearest Face Interpolated*.
5. Dépliez la rubrique *Topology Mapping*, cochez *Max Distance* et tapez `0.3mm` : seules les faces posées sur la surface de référence reçoivent ses normales. Les flancs de la découpe gardent les leurs.
6. **Les normales en dernier :** cliquez sur l'épingle (*Pin to Last*), tout à droite de l'en-tête de *Smooth by Angle* : elle se désactive. Puis, dans le menu de l'en-tête de *Data Transfer*, *Move to Last*. *Smooth by Angle* fixe d'abord les arêtes vives, et *Data Transfer* règle ensuite les normales. Dans l'autre ordre, *Smooth by Angle* recalcule les arêtes vives après le transfert et le dérègle.
7. Les traînées disparaissent. Cochez et décochez l'œil du modificateur pour comparer.

**6.2 · *Weighted Normal*,** sur `E6_Pratique_Platine` (auto) : une platine de rétroviseur plane, biseautée, percée de quatre trous par un *Boolean*. Des triangles d'ombrage barrent sa face.
1. *Add Modifier > Normals > Weighted Normal*.
2. Cochez *Keep Sharp* : les arêtes vives restent vives.
3. Comme en 6.1 : épingle de *Smooth by Angle* désactivée, puis *Move to Last* sur *Weighted Normal*.
4. La face redevient uniforme : les grandes faces imposent leur normale aux petites.

**À retenir, l'ordre de fin de pile :** *Smooth by Angle*, puis le modificateur qui règle les normales (*Data Transfer* ou *Weighted Normal*), tout en bas.

**Lequel choisir :**
- *Weighted Normal* pour une pièce à faces planes : platine, boîtier, carter ;
- *Data Transfer* pour une surface courbe : il faut une surface de référence saine.

**Encart NOTE :**
- depuis Blender 4.1, la case *Auto Smooth* n'existe plus, et ces deux modificateurs agissent seuls. Les tutoriels plus anciens demandent encore de la cocher ;
- une *Subdivision* placée sous *Data Transfer* ignore les normales transférées, sauf si sa case *Use Custom Normals* (rubrique *Advanced*) est cochée. Gardez *Data Transfer* tout en bas.

**Rendu attendu :** autour de la découpe, les reflets sont continus, comme sur l'exemple `_Propre`. La platine est uniforme.

**Erreurs fréquentes :**
- Rien ne change : *Face Corner Data* n'est pas coché, ou la source est la pièce découpée elle-même.
- Les flancs de la découpe sont faux, comme aplatis : *Max Distance* n'est pas coché, ou *Max Distance* est trop grande.
- La surface de référence apparaît au rendu : décochez *Renders* dans sa rubrique *Visibility*.
- La surface de référence a été déplacée : les normales ne correspondent plus. Elle doit rester à la même place que la pièce.
- Des plaques et de grands triangles apparaissent : *Smooth by Angle* est resté sous *Data Transfer*. Voir 6.1, point 6.
- Le transfert ne prend que par endroits : la référence n'a pas le même niveau de subdivision que la pièce, et les deux surfaces ne coïncident plus.

**Petit défi (encart CAUTION) · La ligne de joint du nez de tram (ferro) :** nettoyez l'ombrage autour de la ligne de joint du petit défi de l'étape 5, avec *Data Transfer* depuis `E5_Nez_reference`. Corrigé : sous-collection « Corrigé étape 6 ».

**Point d'arrêt :** le quiz 8.

### Atelier · Le rétroviseur extérieur (35 min)

**Nouveau :** rien. L'atelier réinvestit les étapes 1 à 6 sur un objet complet.

**L'objet :** un rétroviseur extérieur automobile d'environ 250 mm de large, dans la collection `Atelier_Retroviseur`. Toutes les pièces sont là, sans modificateur :
- `Retro_Coque` : la cage de la coque, ouverte à l'arrière, avec ses boucles de maintien au bord de l'ouverture ;
- `Retro_Miroir` : la glace, plane ;
- `Retro_Miroir_reference` : une calotte de sphère de 1 400 mm de rayon, en fil de fer, absente du rendu. Le miroir côté passager est convexe : il élargit le champ de vision ;
- `Retro_Clignotant` : le répétiteur de clignotant, dessiné de face, devant la coque ;
- `Retro_Pied` et `Retro_Platine` : le pied et la platine de fixation sur la portière ;
- `Retro_Coupe_Platine` : quatre cylindres, pour trois vis et le passage du câble.

**Les consignes, par paliers** (valeurs indicatives) :
1. **La coque (étape 1) :** `Ctrl + 2` ; puis *Solidify* `2.5mm`, *Offset* `-1`, *Even Thickness* coché. Vérifiez au *MatCap* que l'ouverture reste tendue.
2. **Le miroir (étapes 2 et 3) :** *Shrinkwrap* sur `Retro_Miroir_reference`. La glace se bombe d'environ 4 mm. Puis *Solidify* `2mm`, *Offset* `-1`.
3. **Le clignotant (étape 3) :** *Shrinkwrap* en *Project*, axe Y, *Above Surface*, `0.2mm`, sur `Retro_Coque`. Puis *Solidify* `1.5mm`, *Offset* `1`.
4. **Le pied (chapitre 2) :** *Bevel*, *Amount* `4mm`, 3 segments, puis *Shade Auto Smooth*.
5. **La platine (étape 5) :** *Boolean* *Difference* avec `Retro_Coupe_Platine`, en *Wire* et sans rendu ; puis *Bevel*, *Amount* `0.8mm`, 3 segments, *Angle*.
6. **★★ La platine propre (étape 6) :** *Weighted Normal*, *Keep Sharp*, sous *Smooth by Angle*.
7. **★★ Le logement du clignotant (étapes 5 et 6) :**
   - une copie de référence de la coque : `Maj + D`, clic droit, nommée `Retro_Coque_reference`, sans *Solidify*, masquée, sans rendu ;
   - un objet de coupe tiré du clignotant (`Maj + D`), conformé sur cette référence, avec un *Solidify* `3mm`, *Offset* `0` : il creuse un logement de 1,5 mm ;
   - le clignotant vise lui aussi la référence, et descend dans le logement : *Offset* `-0.6mm` ;
   - enfin *Data Transfer* depuis la référence, sous *Smooth by Angle*.

**Variantes ★★, sans corrigé obligatoire,** pour retrouver son métier :
- **Ferro, le cadre de vitre frontale :** sur le nez `E3_Nez`, dessinez de face le cadre d'une vitre frontale de tram, avec son joint, et posez-le avec *Project*.
- **Aéro, le hublot complet :** sur `E3_Fuselage`, découpez le hublot (*Boolean*), posez son cadre (*Shrinkwrap*, *Above Surface*), puis une vitre en retrait de 8 mm.

**Rendu attendu :** le rétroviseur complet, sans scintillement ni traînée, avec un miroir bombé et une platine percée. Corrigé : sous-collection « Corrigé atelier », avec `Retro_*_corrige` et le logement ★★.

**Pour aller plus loin (une phrase) :** le modificateur *Lattice* déforme d'un coup un ensemble de pièces avec une cage simple. Il sert à essayer une proportion, par exemple étirer tout le rétroviseur, détails compris.

## Les quiz de vérification des acquis

Huit quiz, au format du module de quiz de l'application (`question`, `options`, `correctIndices` à partir de 0, `explanation`). Chacun se place à la fin de l'étape indiquée. Ils peuvent aussi se faire ensemble à l'écran.

| N° | Placé après | Question | Options (la bonne en gras) | Explication |
|---|---|---|---|---|
| 1 | Étape 1 | « Sur une pièce en subdivision, vous voulez une arête vive, sans ajouter de géométrie. Que faites-vous ? » | **Un Crease de 1 sur l'arête (Maj + E)** ; monter Levels Viewport ; une boucle de maintien ; appliquer la subdivision | « Le *Crease* tend l'arête par un réglage, sans géométrie de plus. Une boucle de maintien marche aussi, mais elle ajoute des arêtes. Monter le niveau ne tend rien : la pièce reste aussi molle, en plus fin. » |
| 2 | Étape 2 | « Votre plaque, posée par Shrinkwrap sur le nez du tram, scintille par plaques. Que faites-vous ? » | **Régler Offset à 0,2 mm** ; monter la subdivision du nez ; passer en Nearest Vertex ; appliquer le modificateur | « La plaque est exactement sur la surface, et les deux se disputent l'affichage. Un *Offset* de quelques dixièmes de millimètre la décolle, sans que l'œil le voie. » |
| 3 | Étape 3 | « Un bandeau dessiné de face doit garder exactement son tracé vu de face, une fois posé sur le nez. Quel mode choisissez-vous ? » | Nearest Surface Point ; **Project, avec l'axe Y** ; Nearest Vertex ; Target Normal Project | « *Project* déplace chaque sommet le long de l'axe choisi : vu dans cet axe, le dessin ne bouge pas. Les autres modes vont au point le plus proche, et le tracé se tord là où la surface tourne. » |
| 4 | Étape 3 | « Sur la prise d'air, à quoi sert le groupe de sommets choisi dans le champ Vertex Group ? » | **À limiter le Shrinkwrap aux sommets du groupe, selon leur poids** ; à choisir la surface cible ; à donner l'épaisseur ; à masquer la prise d'air au rendu | « Seuls les sommets du groupe sont conformés, d'autant plus que leur poids est proche de 1. Le bord se pose sur le capot ; la lèvre, hors du groupe, garde sa hauteur. » |
| 5 | Étape 4 | « Un cadre à 8 côtés, conformé sur le fuselage, s'enfonce dans la courbe entre ses sommets. Que faites-vous ? » | **Ajouter une Subdivision au-dessus du Shrinkwrap** ; ajouter une Subdivision en dessous ; monter l'Offset à 10 mm ; passer en Nearest Vertex | « Le *Shrinkwrap* ne déplace que des sommets. Une *Subdivision* placée avant lui en ajoute, et il les pose tous sur la courbe. Placée après, elle lisse le résultat et le décolle de la surface. » |
| 6 | Étape 4 | « Dans quel ordre empilez-vous les modificateurs d'un détail conformé ? » | Solidify, Shrinkwrap, Subdivision ; **Subdivision, Shrinkwrap, Solidify** ; Shrinkwrap, Solidify, Subdivision ; l'ordre ne change rien | « D'abord ce qui ajoute des sommets, puis la pose, puis l'épaisseur. Un *Solidify* placé avant le *Shrinkwrap* voit ses deux faces posées sur la surface : l'épaisseur disparaît. » |
| 7 | Étape 5 | « Votre objet de coupe est conformé par Shrinkwrap sur le nez même qu'il découpe. Le Boolean ne fait rien. Pourquoi ? » | Le solveur Exact ne gère pas le Shrinkwrap ; **Le nez dépend de l'objet de coupe, qui dépend du nez : la dépendance est circulaire** ; l'objet de coupe est en Wire ; il faut appliquer le Shrinkwrap | « Blender ne peut pas calculer une pièce qui dépend d'elle-même. Conformez l'objet de coupe sur une copie du nez non découpée, la surface de référence. » |
| 8 | Étape 6 | « Une platine plane, biseautée et percée montre des triangles d'ombrage. Quel modificateur les corrige le plus simplement ? » | Data Transfer ; **Weighted Normal** ; Subdivision Surface ; Triangulate | « *Weighted Normal* donne aux petites faces la normale des grandes faces voisines : la face plane redevient uniforme. *Data Transfer* demande une surface de référence ; il sert surtout sur les surfaces courbes. » |

Les quiz 1 à 6 forment le point d'arrêt du palier 1, les quiz 7 et 8 celui du palier 2.

## Fichiers d'exercice

Ce défi est livré avec son fichier, construit par un script rejouable dans `tool/exercices_ch2_defi/`.

### Où trouver le corrigé, exercice par exercice

La convention est commune aux chapitres 2 à 4 :
- le corrigé est dans le fichier de travail, dans une collection masquée (œil fermé) dont le nom commence par « Corrigé » ;
- le LISEZ-MOI indique en une ligne où le trouver.

Le défi a un seul fichier de travail, pour les étapes et l'atelier. **Aucun fichier séparé n'est justifié :**
- tout le résultat tient dans des collections ;
- le défi ne règle ni le rendu ni le monde ;
- il n'utilise aucune image ;
- il ne sert de point de départ à aucun chapitre ;
- l'atelier est léger : un seul fichier simplifie le téléchargement.

| Exercice | Moment | Fichier de travail | Où se trouve le corrigé |
|---|---|---|---|
| Avant de commencer | À la suite des parties de base, ou à leur place | `PRC02_ch2_defi_modelisation.blend`, enregistré sous `defi_modelisation_v001.blend` | Sans objet |
| Étape 1 · Surface de référence | En séance ou après | Le même | Sous-collection « Corrigé étape 1 » de la collection masquée « Corrigé défi modélisation » |
| Étape 2 · Shrinkwrap | En séance ou après | Le même | « Corrigé étape 2 » |
| Étape 3 · Trois cas d'usage | En séance ou après | Le même | « Corrigé étape 3 » |
| Étape 4 · Réglages et pile | En séance ou après | Le même | « Corrigé étape 4 » |
| Étape 5 · Booléens | En séance ou après | Le même | « Corrigé étape 5 » |
| Étape 6 ★★ · Normales | En séance ou après | Le même | « Corrigé étape 6 » |
| Atelier · Rétroviseur | En séance ou après | Le même | « Corrigé atelier » ; les variantes ★★ n'ont pas de corrigé |

Les pièces du corrigé sont à la même place que les pièces à travailler, et utilisent les mêmes surfaces de référence. Pour comparer, affichez la sous-collection du corrigé, puis masquez votre pièce (`H`).

### Fichier 6 · `PRC02_ch2_defi_modelisation.blend`

Le numéro suit les fichiers 1 à 5 du plan du chapitre 2.

**Rôle :** le banc du défi. Pour chaque étape, il contient les surfaces de référence, une pièce d'exemple terminée, les pièces à compléter et leur corrigé masqué. Il contient aussi le rétroviseur de l'atelier.

**Règles communes :**
- Blender 5.2 LTS ; construction par script en arrière-plan (`blender.exe -b --factory-startup`), script rejouable dans `tool/exercices_ch2_defi/` ;
- unités *Metric*, *Length* en *Millimeters*, *Unit Scale* 1,0 ; moteur EEVEE ;
- aucun chemin absolu ni nom d'utilisateur, même dans le tampon d'un navigateur de fichiers ; aucun texte d'extension tierce ; `save_version` à 0 ; contrôle par décompression du fichier (zstd en plusieurs trames) ;
- aucune image : il n'y a rien à empaqueter ;
- pièces sans couche UV ;
- *Shade Auto Smooth* sur toutes les pièces lisses ;
- les surfaces de référence partagent leur maillage d'une étape à l'autre (copies liées) : le fichier reste léger.

**Matières,** pour la lecture seulement, avec la même couleur en *Solid* (*Viewport Display*) :
- `Carrosserie` : gris clair #CCCCCC, *Roughness* 0,3 ;
- `Detail` : gris très sombre #1A1A1C, *Roughness* 0,4 ;
- `Pratique` : orange #D9662A, *Roughness* 0,35, pour les pièces à travailler ;
- `Miroir` : #E6E6EA, *Metallic* 1, *Roughness* 0,02.

**Surfaces de référence,** en cage légère avec *Subdivision* au niveau 2, y compris les copies de référence de *Data Transfer* : la pièce et sa référence doivent coïncider.
- `Fuselage_ref` : un tronçon de cylindre de 1 000 mm de rayon, 900 mm de long, sur 100° d'arc, axe X ;
- `Nez_ref` : un nez de tram de 1 600 × 1 200 mm, à double courbure, tourné vers -Y ;
- `Capot_ref` : un capot de 1 000 × 800 mm, bombé dans les deux sens ;
- `Main_courante_ref` : un tube à 12 pans, Ø 200 × 250 mm, sans subdivision.

**Collections visibles,** une par étape, une rangée par étape. Chaque rangée a un titre en objet texte, avec la matière `Detail`.

| Collection | Objet | Forme et dimensions | Matière, état |
|---|---|---|---|
| `Etape_1_Subdivision` | `E1_Exemple_Sans`, `_Boucles`, `_Crease` | Carters de 120 × 80 × 40 mm, *Subdivision* 2 ; boucles à 4 mm ; *Crease* 1 sur les 12 arêtes | `Detail`, terminés |
| | `E1_Pratique_Boucles` | Cube de 120 × 80 × 40 mm, sans modificateur | `Pratique` |
| | `E1_Pratique_Crease` | Le même cube, *Subdivision* 2 | `Pratique` |
| | `E1_Defi_Capot` | Cage d'un capot de 600 × 400 mm avec une nervure centrale, *Subdivision* 2 | `Pratique` |
| `Etape_2_Shrinkwrap` | `E2_Fuselage`, `E2_Nez`, `E2_Capot` | Copies liées des surfaces de référence | `Carrosserie` |
| | `E2_Exemple_Trappe_plate`, `E2_Exemple_Trappe` | Plaques de 200 × 150 mm, grille 20 × 15 ; la seconde conformée, *Offset* 0,2 mm, *Solidify* 1,5 mm | `Detail` |
| | `E2_Pratique_Plaque` | Plaque de 300 × 120 mm, grille 30 × 12, tangente au nez | `Pratique` |
| | `E2_Defi_Monogramme` | Ovale de 120 × 60 mm, maillé en grille | `Pratique` |
| `Etape_3_Cas_usage` | `E3_Fuselage`, `E3_Nez`, `E3_Capot` | Copies liées | `Carrosserie` |
| | `E3_Exemple_Hublot`, `_Bandeau`, `_Prise` | Les trois cas terminés | `Detail` |
| | `E3_Pratique_Cadre` | Cadre de 280 × 380 mm, intérieur 210 × 310 mm, coins arrondis, dense, à moitié dans le fuselage | `Pratique` |
| | `E3_Pratique_Bandeau` | Bande de 1 400 × 60 mm, grille 70 × 3, dans le plan XZ, 300 mm devant le nez | `Pratique` |
| | `E3_Pratique_Prise` | Bossage de 300 × 200 mm, lèvre de 35 mm, grille 16 × 10 ; bord arrière et côtés sélectionnés en Mode Édition | `Pratique` |
| | `E3_Defi_Grille` | Six ouïes de 180 × 12 mm, à plat au-dessus du capot | `Pratique` |
| `Etape_4_Reglages` | `E4_Main_courante`, `E4_Fuselage`, `E4_Capot` | Copies liées | `Carrosserie` |
| | `E4_Exemple_Modes` | Quatre bandes de 45 × 160 mm, grille 6 × 40, une par mode, chacune étiquetée | `Detail` |
| | `E4_Pratique_Cadre_8` | Cadre octogonal de Ø 340 × 240 mm, 8 côtés, au-dessus du fuselage | `Pratique` |
| | `E4_Defi_Jonc` | Bande de 600 × 12 mm, 6 segments, au-dessus du capot | `Pratique` |
| `Etape_5_Booleens` | `E5_Exemple_Porte`, `E5_Exemple_Coupe` | Panneau de portière bombé de 900 × 500 mm, peau de 3 mm ; logement de poignée de 180 × 40 × 15 mm, *Bevel* 1 mm | `Carrosserie`, terminé ; coupe en *Wire*, sans rendu |
| | `E5_Pratique_Fuselage`, `E5_Coupe_Hublot` | Fuselage, *Subdivision* puis *Solidify* 3 mm ; pavé de 230 × 330 × 200 mm aux coins arrondis | `Carrosserie` ; coupe en `Pratique` |
| | `E5_Defi_Nez`, `E5_Nez_reference`, `E5_Defi_Coupe_Joint` | Nez avec peau de 6 mm (*Subdivision*, puis *Solidify*) ; sa référence masquée, au même niveau de subdivision ; anneau plat de la ligne de joint, 300 × 200 mm, 4 mm de large, dessiné de face | `Carrosserie` ; référence en *Wire*, sans rendu ; coupe en `Pratique` |
| `Etape_6_Normales` | `E6_Exemple_Brut`, `E6_Exemple_Propre` | Fuselage découpé, sans et avec *Data Transfer* | `Carrosserie`, terminés |
| | `E6_Pratique_Fuselage`, `E6_Fuselage_reference` | Fuselage découpé, avec *Bevel* ; référence au même niveau de subdivision, masquée, en *Wire*, sans rendu | `Carrosserie` |
| | `E6_Pratique_Platine` | Platine de 120 × 90 × 8 mm, quatre trous (*Boolean*), *Bevel* 0,8 mm | `Detail` |
| `Atelier_Retroviseur` | `Retro_Coque`, `Retro_Miroir`, `Retro_Miroir_reference`, `Retro_Clignotant`, `Retro_Pied`, `Retro_Platine`, `Retro_Coupe_Platine` | Voir l'atelier ; aucun modificateur | `Carrosserie`, `Miroir`, `Pratique`, `Detail` ; référence et coupe en *Wire*, sans rendu |

**Collection masquée « Corrigé défi modélisation » :** une sous-collection par étape, de « Corrigé étape 1 » à « Corrigé étape 6 », et « Corrigé atelier ».
- Chaque sous-collection contient la copie terminée de chaque pièce *Pratique* et *Defi* de son étape, à la même place. Les objets portent le suffixe `_corrige`.
- Les valeurs sont celles des recettes de ce plan, rendues sous EEVEE.
- « Corrigé atelier » contient le rétroviseur terminé, y compris les paliers ★★ (logement du clignotant, *Weighted Normal*), et sa `Retro_Coque_reference_corrige`.
- Les objets d'exemple ne sont pas des corrigés : ils restent visibles et s'observent librement.

**Vue d'ouverture :**
- espace *Layout*, vue 3D en *Solid*, éclairage *Studio*, couleur des matières, contour des objets ;
- seule la collection `Etape_1_Subdivision` est affichée, pour un premier affichage rapide ;
- `E1_Pratique_Boucles` est sélectionné ;
- le LISEZ-MOI est en bas, dans un *Text Editor*.

**Texte du LISEZ-MOI :**

```
LISEZ-MOI : survolez cette zone et appuyez sur Ctrl + Espace pour l'agrandir (même raccourci pour revenir).

PRC02 · Chapitre 2 · Défi facultatif, hors programme : modélisation avancée
Enregistrez ce fichier sous defi_modelisation_v001.blend. Suivez la section 4 du chapitre 2 dans l'application.
Corrigés : collection « Corrigé défi modélisation » (œil fermé), une sous-collection par étape et une pour l'atelier.
Les corrigés sont à la place de vos pièces : affichez-les, puis masquez votre pièce (H) pour comparer.
Affichez seulement la collection de l'étape en cours. Vue locale : / du pavé numérique.
Couleurs : gris clair = carrosserie, gris sombre = détail fini, orange = pièce à travailler.
Valeurs indicatives, à taper avec leur unité : 0.2mm dans un champ, G X = 500mm pendant un geste.

PALIER 1
1 · Subdivision : Ctrl + 2. Boucles de maintien : Ctrl + R près des arêtes. Crease : Maj + E, 1.
    Les surfaces de référence sont prêtes : vous pouvez commencer à l'étape 2.
2 · Shrinkwrap : Add Modifier > Deform > Shrinkwrap, Target. Offset 0.2mm. Solidify EN DESSOUS.
3 · Hublot : Snap Mode = Above Surface. Bandeau : Project, axe Y. Prise d'air : Vertex Group « Raccord ».
4 · Les 4 modes : voir les étiquettes. Ordre : Subdivision, puis Shrinkwrap, puis Solidify.

PALIER 2
5 · Boolean, Difference. Objet de coupe : Display As = Wire, Renders décoché. Bevel SOUS le Boolean.
    Un objet de coupe se conforme sur la copie « _reference », jamais sur la pièce qu'il découpe.
6 ★★ · Data Transfer : Face Corner Data > Custom Normals ; Topology Mapping > Max Distance 0.3mm. Platine : Weighted Normal.
    Smooth by Angle : cliquez sur son épingle (Pin to Last), puis Data Transfer (ou Weighted Normal) > Move to Last.

ATELIER · Le rétroviseur : collection Atelier_Retroviseur. Consignes par paliers dans l'application.
Variantes ★★ : cadre de vitre frontale sur E3_Nez, hublot complet sur E3_Fuselage.
```

**Corrigé attendu, contrôles :**
- chaque pièce *Pratique* et *Defi* a son double terminé, suffixé `_corrige` ;
- le rendu EEVEE de chaque corrigé correspond au « Rendu attendu » de sa recette ;
- aucun corrigé ne scintille, et aucune dépendance circulaire n'est signalée à l'ouverture ;
- le miroir de l'atelier se bombe de 3 à 5 mm ;
- le fichier s'ouvre seul, sans chemin absolu ni nom d'utilisateur (contrôle par décompression).

**Dans l'application :** un module ressource en tête de la section 4. Le fichier `.blend` se distribue seul : il ne contient aucune image.

## Captures Blender à prévoir

Une capture pour chaque menu, bouton ou panneau cité. Les numéros suivent ceux du chapitre 2, qui s'arrête à 2.32. Le menu *Add Modifier* et ses sous-menus *Generate* (2.2) et *Deform* sont ici capturés à part, pour que la section se lise seule. Côte à côte : environ 600 × 400 px ; pleine largeur pour les comparaisons.

**Ordre de production :** les figures du palier 1 d'abord (2.33 à 2.52), puis le palier 2 et l'atelier.

**État au 18 novembre 2026 :** les 34 figures sont produites dans `assets/images/`, par les scripts de `tool/exercices_ch2_defi/` :
- `captures_brutes.py` prend les captures dans une fenêtre Blender séparée ;
- `captures_clics.py` déplie les rubriques repliées par des clics simulés ;
- `recadrer.py` recadre et assemble les figures.

La 2.35 montre une boucle déjà sélectionnée, pas son glissement : `loopcut_slide` ne se pilote pas par script.

| Figure | Fichier | Ce qu'elle montre | Format |
|---|---|---|---|
| 2.33 | `modeling_challenge_overview_blender.jpg` | Le banc du défi : les rangées des étapes et le rétroviseur | Pleine largeur |
| 2.34 | `subdivision_holding_loops_crease_blender.jpg` | Les trois carters : sans rien, boucles de maintien, *Crease* | Pleine largeur |
| 2.35 | `loop_cut_holding_loop_blender.jpg` | Une boucle de maintien, sélectionnée à 4 mm d'une arête, en Mode Édition | Côte à côte |
| 2.36 | `edge_menu_edge_crease_blender.jpg` | Le menu *Edge* en Mode Édition, avec *Edge Crease* | Côte à côte |
| 2.37 | `subdivision_advanced_use_creases_blender.jpg` | Le panneau *Subdivision Surface* : *Levels Viewport*, *Render*, rubrique *Advanced* ouverte, *Use Creases*, *Use Custom Normals* | Côte à côte |
| 2.38 | `crease_hood_character_line_blender.jpg` | Le capot à ligne de caractère, avant et après le *Crease* | Côte à côte |
| 2.39 | `shrinkwrap_principle_flat_vs_wrapped_blender.jpg` | La trappe plate qui décolle, et la trappe conformée, sur le fuselage | Pleine largeur |
| 2.40 | `add_modifier_deform_menu_blender.jpg` | *Add Modifier > Deform*, *Shrinkwrap* en surbrillance | Côte à côte |
| 2.41 | `shrinkwrap_panel_default_blender.jpg` | Le panneau *Shrinkwrap* : *Wrap Method*, *Snap Mode*, *Target*, *Offset*, *Vertex Group* | Côte à côte |
| 2.42 | `shrinkwrap_offset_z_fighting_blender.jpg` | Le scintillement à *Offset* 0, puis la plaque nette à 0,2 mm | Pleine largeur |
| 2.43 | `shrinkwrap_solidify_stack_order_blender.jpg` | La pile *Shrinkwrap* puis *Solidify*, et l'inverse, avec l'épaisseur perdue | Pleine largeur (image large, lisible à 0,6) |
| 2.44 | `shrinkwrap_snap_mode_menu_blender.jpg` | Le menu *Snap Mode* : *On Surface*, *Inside*, *Outside*, *Outside Surface*, *Above Surface* | Côte à côte |
| 2.45 | `porthole_frame_fuselage_blender.jpg` | Le cadre de hublot, en *On Surface* (à moitié caché) puis en *Above Surface* | Pleine largeur |
| 2.46 | `shrinkwrap_project_panel_blender.jpg` | Les réglages de *Project* : *Limit*, *Subdivision Levels*, *Axis*, *Negative*, *Positive*, *Face Cull*, *Invert Cull*, *Auxiliary Target* | Côte à côte |
| 2.47 | `tram_nose_band_project_vs_nearest_blender.jpg` | Vu de face : le bandeau en *Project*, droit, et en *Nearest Surface Point*, tordu | Pleine largeur |
| 2.48 | `vertex_group_menu_ctrl_g_blender.jpg` | Le menu `Ctrl + G` en Mode Édition, *Assign to New Group* | Côte à côte |
| 2.49 | `vertex_groups_panel_weight_blender.jpg` | L'onglet *Object Data*, rubrique *Vertex Groups* : la liste, *Weight*, *Assign*, *Remove* | Côte à côte |
| 2.50 | `hood_scoop_vertex_group_blender.jpg` | Les trois prises d'air : sans groupe (aplatie), groupe au poids 1, groupe dégradé | Pleine largeur |
| 2.51 | `shrinkwrap_four_modes_blender.jpg` | Les quatre bandes sur la main courante à 12 pans, en fil de fer | Pleine largeur |
| 2.52 | `shrinkwrap_subdivision_order_blender.jpg` | Le cadre à 8 côtés : seul, *Subdivision* au-dessus, *Subdivision* en dessous | Pleine largeur |
| 2.53 | `boolean_panel_difference_solver_blender.jpg` | Le panneau *Boolean* : *Intersect*, *Union*, *Difference* ; *Object* ; *Solver* | Côte à côte |
| 2.54 | `object_viewport_display_as_blender.jpg` | Onglet *Object*, rubrique *Viewport Display*, *Display As* | Côte à côte |
| 2.55 | `object_visibility_renders_blender.jpg` | Onglet *Object*, rubrique *Visibility*, *Renders* décoché | Côte à côte |
| 2.56 | `boolean_bevel_order_blender.jpg` | La découpe de hublot, bord vif (*Bevel* au-dessus) puis arrondi (*Bevel* en dessous) | Pleine largeur |
| 2.57 | `boolean_cutter_reference_surface_blender.jpg` | L'objet de coupe de la ligne de joint, conformé sur la référence masquée, et l'Outliner | Pleine largeur (image large, lisible à 0,6) |
| 2.58 | `boolean_shading_vs_data_transfer_blender.jpg` | La découpe en *MatCap* de contrôle : traînées, puis reflets propres | Pleine largeur |
| 2.59 | `matcap_reflection_check_blender.jpg` | Option : *Viewport Shading*, *MatCap*, `check_reflection_horizontal` | Côte à côte |
| 2.60 | `add_modifier_edit_menu_blender.jpg` | *Add Modifier > Edit*, *Data Transfer* | Côte à côte |
| 2.61 | `data_transfer_panel_custom_normals_blender.jpg` | Le panneau *Data Transfer* : *Source*, rubrique *Face Corner Data* dépliée (*Custom Normals*, *Mapping*), et la rubrique *Topology Mapping* (*Max Distance*) | Pleine largeur |
| 2.62 | `add_modifier_normals_menu_blender.jpg` | *Add Modifier > Normals* : *Normal Edit*, *Weighted Normal* | Côte à côte |
| 2.63 | `weighted_normal_plate_blender.jpg` | La platine percée, sans puis avec *Weighted Normal* | Pleine largeur |
| 2.64 | `side_mirror_workshop_blender.jpg` | Le rétroviseur terminé, vu de l'arrière et de l'avant | Pleine largeur |
| 2.65 | `side_mirror_convex_reference_blender.jpg` | Le miroir et sa calotte de référence en fil de fer | Côte à côte |
| 2.66 | `side_mirror_indicator_recess_blender.jpg` | ★★ Le logement du clignotant, sans puis avec *Data Transfer* | Pleine largeur (image large, lisible à 0,6) |

**Méthode :** celle des chapitres précédents. *Resolution Scale* à 1,25, onglets d'extensions tierces hors champ, interface en anglais. Les menus et les panneaux se capturent dans une fenêtre Blender courte, lancée à part avec `--factory-startup`, jamais dans la session du formateur. Les comparaisons se rendent sous EEVEE, avec l'image *studio* de *Material Preview*.

## Comment le défi s'insère dans l'application

- **Le texte source :** un fichier `_resources/PRC02-SU-26v01_chap2_modelisation_non_destructive.md`, au format de `writer_guide.md`. Pour l'instant, il contient l'encart d'attente, puis la section `## 4. Défi facultatif · Modélisation avancée`. Les sections 1 à 3 viendront s'insérer avant elle.
- **Le registre :** dans `lib/core/data/course_data.dart`, chapitre 2, un quatrième point : `ChapterPoint(label: 'Défi facultatif : modélisation avancée', targetModuleId: 'ch2_sec4_title')`. Les trois premiers points restent. Leurs ancres n'existent pas encore : un clic ouvre le chapitre en haut, sans erreur (vérifié dans `chapter_scaffold.dart`).
- **Le badge « En préparation » :** `isInPreparation` vaut `modules.isEmpty`. Dès que `chapter2Modules` contient le défi, le chapitre s'ouvre, mais le badge disparaît du tableau de bord et du Programme. **Solution retenue, la plus simple qui reste juste :**
  - un champ `baseContentPending` (booléen, `false` par défaut) dans `CourseChapter`, mis à `true` pour le chapitre 2 ;
  - un accesseur `showsPreparationBadge`, qui vaut `isInPreparation || baseContentPending` ;
  - `dashboard_screen.dart` et `program_screen.dart` l'utilisent pour le badge, à la place de `isInPreparation`. `chapter_scaffold.dart` garde `isInPreparation` : le chapitre s'ouvre et affiche le défi.

  Le badge « En préparation » reste donc tant que le contenu de base manque. Il suffira de retirer `baseContentPending: true` quand il sera rédigé.
- **Les modules,** dans `chapter2Modules` de `lib/core/data/mock_chapters_data.dart`. Aucun nouveau type de module n'est nécessaire.

| Contenu | Module | Identifiants |
|---|---|---|
| Titre du chapitre | `TitleModule` | `ch2_title`, « Modélisation non destructive : modificateurs et courbes » |
| L'encart d'attente : « Le contenu de base de ce chapitre arrivera avec une prochaine mise à jour. Le défi facultatif est déjà disponible pour ceux qui veulent aller plus loin. » | `InfoModule` de type `info` (NOTE) | `ch2_info_base_a_venir` |
| Titre de la section | `TitleModule` | `ch2_sec4_title`, « 4. Défi facultatif · Modélisation avancée » |
| Statut facultatif, pour qui, quand, prérequis, reprise au chapitre 3 | `InfoModule` de type `info` (NOTE) | `ch2_sec4_info_intro` |
| Rappels pour qui n'a pas suivi le chapitre 2 | `InfoModule` de type `info` (NOTE) | `ch2_sec4_info_rappels` |
| Le fichier | `ResourceModule` | `ch2_sec4_res1`, `PRC02_ch2_defi_modelisation.blend` |
| Ce qui n'est pas fidèle sous EEVEE ou en *Material Preview* | `InfoModule` de type `objective` (IMPORTANT) | `ch2_sec4_info_eevee` |
| La théorie du shrinkwrap | `TextModule`, puis `InfoModule` de type `objective` | `ch2_sec4_e2_txt1`, `ch2_sec4_e2_obj1` |
| Chaque étape : notion, exemple | `TextModule` avec sous-titre (« Étape 1 · La surface de référence ») | `ch2_sec4_e1_txt1`… |
| Chaque menu ou panneau | `SideBySideModule` | `ch2_sec4_e1_side1`… |
| Chaque recette | `ListModule` numéroté (« Recette · … ») | `ch2_sec4_e1_list1`… |
| Comparaisons | `FullMediaModule` | `ch2_sec4_e1_media1`… |
| Rendu attendu, à retenir | `TextModule` | |
| Erreurs fréquentes | `InfoModule` de type `warning` | `ch2_sec4_e1_warn1`… |
| Notes (*Snap Mode*, contrainte, *Auto Smooth*) | `InfoModule` de type `info` | |
| Petits défis, atelier, variantes | `InfoModule` de type `challenge` (CAUTION) | `ch2_sec4_e1_chal1`… |
| Quiz | `QuizModule` | `ch2_sec4_quiz1` à `quiz8` |

- **Les paliers :** un `TextModule` court ouvre chaque palier : « Palier 1 · Surfaces et shrinkwrap », « Palier 2 · Découpes et normales », puis « Atelier · Le rétroviseur ». Il rappelle la durée et le point d'arrêt.
- **Les signets et la recherche** reprennent les modules automatiquement, comme pour les autres sections.
- **Le style :** vouvoiement, phrases courtes, réglages présentés comme des options et des valeurs de départ, aucun emoji, aucune grille d'autoévaluation.

## Coordination avec le chapitre 2 et les autres plans

Ce plan ne modifie aucun plan existant. Les points ci-dessous sont à reporter par la session principale.

1. **Le menu *Array* dans Blender 5.2.1.** *Add Modifier > Generate* propose deux entrées : *Array*, un nouvel actif en Geometry Nodes, et *Array (Legacy)*, le modificateur classique. Le plan du chapitre 2 décrit le modificateur classique (*Relative Offset*, *Object Offset*, *Count*). Son contenu devra nommer *Array (Legacy)*, ou décrire le nouvel actif. Ce défi n'utilise pas *Array*.
2. **L'annonce du défi.** Quand le contenu de base du chapitre 2 sera rédigé, son ouverture et sa rubrique « Les défis pour ceux qui avancent vite » pourront renvoyer à la section 4 en une phrase. Le défi ★★ « Percer la grille » du chapitre 2 prépare l'étape 5.
3. **La reprise au chapitre 3.** Elle s'appuie sur `PRC02_ch3_lampe_a_habiller.blend` et sur `PRC02_ch2_lampe_modele.blend`, prévus par les plans des chapitres 2 et 3 mais pas encore construits.
4. **Les figures.** Le défi numérote ses figures de 2.33 à 2.66, à la suite des 32 figures du chapitre 2.
5. **Le badge du chapitre 2.** Le champ `baseContentPending` est à retirer quand les sections 1 à 3 seront en ligne.
6. **Le chapitre 4.** Le défi ne touche ni à la lampe, ni à l'éclairage, ni au rendu. Le rétroviseur peut devenir un autre objet à mettre en scène au chapitre 4, comme la liseuse ; ce n'est pas prévu à ce stade.
7. **Les fichiers construits par script, tous chapitres.** *Shade Auto Smooth* lie le groupe *Smooth by Angle* depuis le dossier d'installation de Blender : le fichier garde un chemin absolu vers `C:\Program Files\…`. Les scripts des fichiers du chapitre 2 (la lampe utilise *Shade Auto Smooth* partout) et du chapitre 3 doivent rendre ce groupe local et retirer la bibliothèque, comme `tool/exercices_ch2_defi/build_defi_modelisation.py`. Le contrôle par décompression le détecte.
8. **L'ordre des normales au chapitre 2.** Si le contenu de base du chapitre 2 ou ses défis utilisent un jour *Weighted Normal* ou *Data Transfer*, la même règle vaut : *Smooth by Angle* désépinglé, au-dessus d'eux.

## Contrôle face aux critères du découpage

| Critère | Comment le plan y répond |
|---|---|
| 1 · Durée | Hors minutage : le défi ne prend aucune minute au chapitre 2, et le formateur ne fait aucune démonstration. L'apprenant le fait à la suite des parties de base, s'il lui reste du temps, ou à leur place ; le reste se fait après la séance. |
| 2 · Périmètre | Complément facultatif, hors programme de base, signalé comme tel sur l'écran Programme, dans le titre de la section et dans son introduction. Il prolonge le point 1 du programme (modificateurs), dans l'ancre `ch2_sec4_title`. Ni *Append*, ni *Link*, ni matière à régler, ni lumière, ni caméra. |
| 3 · Pas de redite | *Subdivision Surface*, *Loop Cut*, la pile, *Solidify*, *Bevel*, *Shade Auto Smooth* et la vue locale sont réemployés, pas réexpliqués (tableau des prérequis). Les acquis du chapitre 2 sont seulement rappelés, en quatre lignes, pour qui fait le défi avant ce chapitre. |
| 4 · Continuité | Le défi se fait dans son propre fichier : `lampe_modele_v001.blend` n'est pas touché. L'apprenant qui remplace les parties de base reprend le chapitre 3 avec `PRC02_ch3_lampe_a_habiller.blend` ou `PRC02_ch2_lampe_modele.blend`. |
| 5 · Fichiers | Un seul fichier de travail, pour les étapes et l'atelier. Les corrigés sont dans la collection masquée « Corrigé défi modélisation », signalée en une ligne dans le LISEZ-MOI. Aucun fichier séparé. Le fichier s'ouvre seul : aucune image, aucun chemin. |
| 7 · Progression | Les prérequis sont distingués selon leur origine (Basics, chapitre 1, chapitre 2). Le défi peut se faire dès le chapitre 1 : les acquis du chapitre 2 dont il se sert (*Solidify*, *Bevel*, *Shade Auto Smooth*) sont rappelés dans l'encart « Si vous n'avez pas encore suivi le chapitre 2 ». Les surfaces de référence sont prêtes : on peut entrer à l'étape 2. Une notion par étape, des réglages introduits un par un. Chaque étape suit le même ordre : exemple, pratique guidée, petit défi. Un point d'arrêt et des quiz à la fin de chaque palier. L'atelier n'introduit rien de nouveau. Les sous-étapes difficiles sont marquées ★ ; l'étape 6 et les variantes sont ★★. |

## Points techniques vérifiés dans Blender 5.2.1 LTS

Vérifiés le 18 novembre 2026, dans un Blender lancé en arrière-plan (`-b --factory-startup`), sans toucher à la session du formateur. Les comparaisons ont été rendues sous EEVEE, sous l'image *studio*, à l'échelle réelle. Les rendus de contrôle sont dans le dossier de notes partagé.

- **Libellés et valeurs par défaut :**
  - *Shrinkwrap* : *Wrap Method* *Nearest Surface Point* (défaut), *Project*, *Nearest Vertex*, *Target Normal Project* ; *Snap Mode* *On Surface* (défaut), *Inside*, *Outside*, *Outside Surface*, *Above Surface* ; *Offset* 0 ; en *Project* : *Limit*, *Subdivision Levels*, axes *X*, *Y*, *Z*, *Negative* (décoché), *Positive* (coché), *Face Cull* *Off* / *Front* / *Back*, *Invert Cull*, *Auxiliary Target* ; *Vertex Group* et son bouton *Invert*.
  - *Subdivision Surface* : *Use Creases* coché, *Use Custom Normals* décoché, *Quality* 3, dans la rubrique *Advanced*.
  - *Boolean* : *Difference* par défaut, *Operand Type* *Object*, *Solver* *Exact* (défaut), *Float*, *Manifold* ; *Self Intersection*, *Hole Tolerant*.
  - *Data Transfer* : *Object Transform* coché ; *Face Corner Data* ; types *Custom Normals*, *Colors*, *UVs* ; rubrique *Face Corner Data* : *Mapping* *Nearest Face Interpolated* ; rubrique *Topology Mapping* : case *Max Distance* (propriété `use_max_distance`, nommée « Only Neighbor Geometry » dans l'API) ; *Mix Mode* *Replace*, *Mix Factor* 1.
  - *Weighted Normal* : *Weighting Mode* *Face Area*, *Weight* 50, *Threshold* 0,01, *Keep Sharp* et *Face Influence* décochés.
  - *Display As* : *Bounds*, *Wire*, *Solid*, *Textured*.
- **Les menus :** *Add Modifier* propose *Edit*, *Generate*, *Deform*, *Normals* et *Physics* pour un maillage (`properties_data_modifier.py`). `Maj + A` au-dessus de l'onglet *Modifiers* ouvre le même menu. *Generate* contient *Array* (actif) et *Array (Legacy)*.
- **Les raccourcis** (`blender_default.py`) : `Ctrl + 0` à `Ctrl + 5` règlent la subdivision et ajoutent le modificateur au besoin ; `Maj + E` : *Edge Crease* ; `Ctrl + R` : *Loop Cut and Slide* ; `Ctrl + G` en Mode Édition : menu *Vertex Groups*, avec *Assign to New Group* ; `/` : vue locale.
- **Le scintillement :** une plaque conformée à *Offset* 0 scintille au rendu EEVEE ; à 0,2 mm, elle est nette.
- **La plaque plate :** une plaque de 150 mm de haut, tangente à un fuselage de 1 m de rayon, décolle de 3,3 mm à ses bords.
- ***Snap Mode*, avec *Offset* 0,2 mm :**
  - une plaque partie de l'extérieur finit au même endroit en *On Surface*, *Outside Surface* et *Above Surface* ;
  - partie de l'intérieur, elle finit 0,2 mm **sous** la surface en *On Surface*, et 0,2 mm au-dessus en *Outside*, *Outside Surface* et *Above Surface* ;
  - *Outside* ne déplace pas une plaque déjà dehors ; *Inside* ne déplace pas une plaque déjà dedans.
- ***Solidify* et *Shrinkwrap* :** placé en dessous, le *Solidify* donne bien 1,5 mm d'épaisseur, perpendiculaire à la courbe. Placé au-dessus, l'épaisseur tombe à 0,2 mm : ses deux faces sont posées.
- ***Project* :** une bande partie derrière la cible ne bouge pas avec *Positive* seul ; avec *Negative* coché, elle se pose. Vue de face, la bande projetée garde son tracé ; en *Nearest Surface Point*, elle se tord vers les côtés du nez.
- **Les quatre modes,** une bande de 287 sommets sur un tube à 12 pans : 203 positions distinctes en *Nearest Surface Point*, 287 en *Target Normal Project* et en *Project*, 6 en *Nearest Vertex*.
- **Le groupe de sommets :** sans groupe, la prise d'air s'aplatit et scintille sur le capot ; avec le groupe au poids 1, elle garde sa lèvre, avec une marche ; avec un dégradé, son arrière se fond dans le capot.
- **L'ordre avec *Subdivision* :** un cadre à 8 côtés seul s'enfonce entre ses sommets ; *Simple* au-dessus, il colle partout ; *Catmull-Clark* en dessous, il décolle et s'enfonce par endroits.
- **Le booléen :** *Bevel* sous le *Boolean* arrondit le bord du trou ; au-dessus, le bord reste vif. Sur une surface courbe et lissée, la découpe montre des traînées d'ombrage au rendu EEVEE.
- **La dépendance circulaire :** un objet de coupe conformé sur la pièce qu'il découpe provoque « Detected 2 dependency cycles », et le *Boolean* n'a aucun effet. Conformé sur une copie de référence, tout fonctionne.
- ***Data Transfer* :** depuis la surface non coupée, avec *Max Distance* à 0,3 mm, les traînées disparaissent au rendu EEVEE, et les flancs de la découpe gardent leur ombrage.
  - *Smooth by Angle* placé **sous** *Data Transfer* (épinglé en bas, le réglage par défaut) : sur la ligne de joint, plaques et grands triangles. Placé **au-dessus**, épingle décochée : rendu propre. Même règle pour *Weighted Normal*.
  - Une référence au niveau de subdivision 3, pour une pièce au niveau 2 : le transfert ne prend que par endroits. Au même niveau : rendu propre.
- ***Weighted Normal* :** sur une platine biseautée et percée, les triangles d'ombrage disparaissent, avec *Keep Sharp*.
- **La ligne de joint :** une rainure de 4 mm sur 3 mm de profondeur, creusée par un anneau conformé (*Project*, *Solidify* `6mm`, *Offset* 0), est nette. Un *Bevel* de 0,5 mm sous le *Boolean* la hérisse de grands triangles.
- ***Shade Auto Smooth* lie une bibliothèque :** l'opérateur ne copie pas le groupe de nœuds *Smooth by Angle* : il le **lie** depuis `geometry_nodes_essentials.blend`, dans le dossier d'installation de Blender. Le fichier garde alors un chemin absolu vers `C:\Program Files\…`. Le script de construction rend le groupe local et retire la bibliothèque ; le contrôle par décompression ne trouve plus aucun chemin. Pour un apprenant, c'est sans conséquence : son Blender retrouve ses propres actifs.
- **La sélection enregistrée :** les 37 sommets de bord de `E3_Pratique_Prise` restent sélectionnés à l'ouverture, en sélection par sommets.
- **Le rétroviseur :** la glace conformée sur une calotte de 1 400 mm de rayon se bombe d'environ 4 mm (3,7 mm mesurés sans épaisseur). Le clignotant projeté suivant Y se pose entièrement sur la coque.
- **Les MatCaps** `check_reflection_horizontal` et `check_reflection_vertical` sont livrés avec Blender 5.2.

À vérifier pendant la construction du fichier :
- le libellé « Face Cull » est confirmé à l'écran (capture 2.46) ;
- le libellé du biseau dans le panneau *Bevel* : *Amount*, relevé dans le catalogue de traduction de Blender 5.2.1 (aucune capture de ce panneau dans le défi), pour la propriété *Width* ;
- l'épingle *Pin to Last* est une icône, tout à droite de l'en-tête de *Smooth by Angle* (vu sur une capture de la pile) ;
- le temps d'affichage en *Material Preview* avec toutes les collections, sur le poste le plus modeste.

## Décisions, 18 novembre 2026

Décisions prises par la session principale, par délégation du formateur, le 18 novembre 2026 :
1. **Statut :** « Défi facultatif : modélisation avancée », hors programme de base, comme le défi procédural du chapitre 3. Public : ceux qui vont vite et ceux qui maîtrisent déjà ces sujets ; à la suite des parties de base ou à leur place. Aucune démonstration du formateur ; le minutage du chapitre 2 ne change pas.
2. **Périmètre :** deux paliers, environ 3 heures, une notion par étape. Palier 1 : la surface de référence en subdivision, puis le shrinkwrap en trois étapes (théorie, trois cas d'usage, réglages). Palier 2 : les booléens non destructifs, puis les normales propres en ★★. Les surfaces de référence sont prêtes, pour aborder le shrinkwrap directement.
3. **Atelier :** un rétroviseur extérieur automobile ; deux variantes ★★ sans corrigé obligatoire, le cadre de vitre frontale d'un tram et un hublot sur un fuselage.
4. **Affichage :** section 4 du chapitre 2, ancre `ch2_sec4_title`, précédée d'un encart d'attente ; point au programme « Défi facultatif : modélisation avancée ».
5. **Fichiers :** aussi peu que possible ; les corrigés dans des collections masquées « Corrigé… ».

Décisions mineures prises par cette session, **par délégation, à confirmer par le formateur :**
6. ***Lattice* :** cité seulement, dans « Pour aller plus loin ». Une étape ★ dépasserait le budget de 3 heures.
7. **Un seul fichier,** pour les étapes et l'atelier.
8. **Les secteurs tournent dans chaque étape** (tableau de « Quand et comment ») ; les surfaces de référence sont partagées par copies liées.
9. **Trois matières neutres** et une matière de miroir, pour la lecture ; les pièces à travailler sont en orange.
10. **Les corrigés sont à la même place** que les pièces à travailler, pour partager les mêmes surfaces de référence.
11. **Le badge « En préparation »** reste sur le chapitre 2, grâce au champ `baseContentPending`, tant que le contenu de base manque.
12. **Huit quiz :** six pour le palier 1, deux pour le palier 2.
13. **La reprise au chapitre 3** pour qui remplace les parties de base : `PRC02_ch3_lampe_a_habiller.blend`, ou `PRC02_ch2_lampe_modele.blend`.
14. **Le petit défi de l'étape 5 est une ligne de joint,** et non un phare encastré : un logement de phare de 40 mm ne se creuse pas dans une peau de quelques millimètres. La ligne de joint montre en plus pourquoi on conforme un objet de coupe : sa profondeur reste la même sur toute la courbe.
15. **Les normales en dernier :** à l'étape 6 et dans l'atelier, *Smooth by Angle* est désépinglé et placé au-dessus de *Data Transfer* ou de *Weighted Normal*. C'est un geste de plus, mais sans lui le transfert se dérègle (vérifié au rendu).
16. **Un défi autonome, utilisable dès le chapitre 1 (relecture de la session principale, 18 novembre 2026) :** l'encart NOTE « Si vous n'avez pas encore suivi le chapitre 2 » rappelle *Solidify*, le modificateur *Bevel* (*Amount*), *Shade Auto Smooth*, la saisie avec `=` et la vue locale. Les prérequis sont distingués selon leur origine. Le plan est validé par délégation, avec ces quatre ajustements : défi autonome, libellé *Amount*, palier 1 en priorité, aucun fichier hors du dépôt.
