# Chapitre 1 · Environnement de travail et blocage de volumes : plan de la demi-journée

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 3 sur 6, en présentiel, de 5 à 8 apprenants · Plan du 18 novembre 2026, **validé** par le formateur le même jour, avec ses décisions (dernière partie)

Ce plan suit le découpage validé (`PRC02-decoupage-formation.md`) et ses critères de contrôle. Il cale sur une demi-journée le contenu du chapitre 1, déjà rédigé et validé (`PRC02-SU-26v01_chap1_blocage_environnement.md`), sans le modifier. Les libellés et les valeurs cités ont été vérifiés dans Blender 5.2.1 (partie « Points vérifiés »).

## En bref

- **Objectif du chapitre** (déclaré dans l'application) : configurer un environnement de travail adapté au design produit, puis explorer rapidement volumes et silhouettes par blocage de formes, avec les outils de transformation et d'édition interactive.
- **À la fin de la demi-journée, l'apprenant sait :**
  - saisir une cote avec son unité, dans un champ ou pendant un geste, quelle que soit l'unité affichée ;
  - régler l'affichage de la vue pour lire une forme, et caler un volume sur un croquis ;
  - bloquer un objet avec des primitives, à ses cotes ;
  - incliner et déplacer une pièce selon ses propres axes ;
  - poser une pièce sur une autre avec l'aimantation, puis contrôler une cote ;
  - biseauter et extruder au millimètre ;
  - décliner et comparer des variantes par leur silhouette.
- **Format :** 3 h 30 de contenu et 2 pauses de 10 minutes, soit 3 h 50. Il reste 10 minutes de marge sur 4 heures. Exemple : de 9 h 00 à 12 h 50.
- **Principe :** le même qu'à l'initiation. Une notion à la fois, montrée en quelques minutes, puis pratiquée en guidé, puis réinvestie en autonomie. Les apprenants ne passent jamais plus de 15 minutes sans toucher la souris.
- **La règle du jour : tapez l'unité.** Dans un champ, `25mm` est toujours compris. Pendant un geste, on tape d'abord `=` : `G Z = 25mm`. Ces deux gestes fonctionnent que la scène affiche des mètres ou des millimètres. L'affichage en millimètres reste une option, recommandée pour le design produit.
- **Fil rouge :** la lampe de bureau, que les apprenants ont vue à l'initiation. Ils en bloquent leur propre version sur les croquis, puis deux variantes. Le fichier de fin, `lampe_blocage_v001.blend`, est celui que le chapitre 2 attend.
- **Fichiers :** un seul fichier de travail, déjà livré et non modifié : `PRC02_ch1_blocage_lampe.blend`. Son corrigé est fait de ses trois collections masquées *Variante A*, *B* et *C*. Aucun nouveau fichier.
- **Moteur de rendu :** le fichier livré est encore réglé sur Cycles ; sa correction en EEVEE est prévue en fin de projet. D'ici là, chacun vérifie le moteur à 0:25 et choisit EEVEE si besoin.

## La progression

### Ce que le chapitre approfondit

| Déjà vu | Où | Ce que le chapitre 1 en fait |
|---|---|---|
| La barre latérale `N`, onglet *Item*, et le champ *Location* | Initiation, demi-journée 1 (la balise) | Des cotes saisies avec leur unité ; le champ *Dimensions* |
| `Maj + A` et le panneau F9 | Basics 102 § 2 ; initiation, demi-journée 1 | Des primitives réglées à leurs cotes, avec peu de segments |
| `G`, `R`, `S` avec un axe et une valeur | Basics 102 § 1 ; initiation | Une valeur avec son unité (`=`) ; l'axe propre de l'objet (`G Z Z`) |
| Les vues `1`, `3`, `7` et `5` | Basics 101 § 4 ; défi des vues | Le calage sur les croquis ; la Quad View |
| Les modes d'affichage et la flèche de leurs options | Basics 101 § 4 | Le menu *Viewport Shading* : lire les volumes, juger la silhouette |
| L'Outliner, l'œil, les collections, `M` | Basics 101 et 102 ; activité A | La collection active ; une collection par variante ; *Duplicate Collection* |
| *Save As* et le bouton `+` | Basics 102 § 4 ; initiation, demi-journée 1 | Un fichier de travail enregistré sous son nom dès l'ouverture |
| `Ctrl + A > Scale` | Basics 103 § 4 ; clinique, patient 2 | Après une cote saisie dans *Dimensions* ; avant un biseau |
| Le Mode Édition, `Alt + clic`, *Extrude*, *Bevel* | Basics 103 § 1 et 2 ; initiation, demi-journée 2 | Le biseau mesuré ; les variantes de l'extrusion (`Alt + E`) |
| Le moteur EEVEE, nommé dans la chasse aux réglages | Initiation, demi-journée 1 | Le vérifier dans l'onglet *Render* du fichier de la lampe |

### Une notion nouvelle à la fois

Chaque notion passe par la démonstration, la pratique guidée, puis la pratique autonome. La dernière colonne dit où elle est réinvestie seule.

| Notion nouvelle | Démo et pratique guidée | Pratique autonome |
|---|---|---|
| Une valeur avec son unité dans un champ (`180mm`) | 0:10 · Les cotes et leur unité | 1:27 · Les grands volumes |
| Un nombre seul s'entend dans l'unité affichée ; `=` pour taper une unité pendant un geste | 0:10 · Les cotes et leur unité | 1:27 ; 2:45 ; 3:00 ; atelier |
| L'unité d'affichage (*Length*), une option recommandée | 0:10 · Les cotes et leur unité | Au choix de chacun |
| Le menu *Viewport Shading* (*Random*, *Cavity*, *MatCap*) | 0:30 · Lire la forme | 0:30, fin de séquence ; atelier |
| *Clip Start* | 0:30 · Lire la forme | 2:07, gros plans sur les articulations |
| La Quad View | 0:30 · Lire la forme | Atelier (comparer les pistes) |
| L'image de référence et ses réglages | 0:45 · Images de référence | 0:45, placement du croquis de profil |
| Les *Quick Favorites* ; les options de navigation et de saisie | 0:57 · À votre main | 0:57, essai libre ; ensuite, au choix |
| La méthode en quatre temps ; l'encombrement | 1:15 · Méthode et encombrement | Atelier |
| Le champ *Dimensions* | 1:15 · Méthode et encombrement | 3:00 (bras allongé) ; atelier |
| `H`, `Alt + H` | 1:15 · Méthode et encombrement | Toute la suite |
| La collection active | 1:27 · Les grands volumes | Atelier |
| La vue locale (`/`) | 1:27 · Les grands volumes | 1:27, fin de séquence ; 2:45 |
| L'orientation *Local* et `G Z Z` | 1:52 · Orienter : la tête | 3:00 (variante B) ; atelier (variante C) |
| L'aimantation : cible, point de base, `Ctrl` | 2:07 · Aimanter et mesurer (*Face Center*) | 2:07 : articulation du haut ; pose sur une surface avec *Face* ; atelier |
| L'outil *Measure* ; *Edge Length* | 2:07 · Aimanter et mesurer | Atelier (contrôle de la piste retenue) |
| Le biseau mesuré : *Width* avec son unité, *Profile*, *Clamp Overlap* | 2:45 · Éditer avec précision | 2:45, congé du bord inférieur |
| *Extrude Manifold*, *Extrude Faces Along Normals* | 2:45 · Éditer avec précision | 2:45, le bandeau |
| *Duplicate Collection* | 3:00 · Variantes et silhouette | Atelier (variante C) |
| Le réglage « ombre chinoise » du mode *Solid* | 3:00 · Variantes et silhouette | Atelier (comparaison des pistes) |

La section 1 compte beaucoup de notions, mais chacune tient en un réglage : une case, un champ ou un menu. La charge réelle se concentre dans la section 3.

### L'ordre de la séance

La séance suit l'ordre de l'application, avec une exception, validée par le formateur. Les deux dernières notions de la section 2, *Comparer des variantes* et *Juger la silhouette*, passent après la section 3. C'est l'ordre de la méthode en quatre temps du chapitre lui-même : on pose l'encombrement, on place les grands volumes, on ajuste les proportions, puis seulement on compare et on itère. Les outils de la section 3 servent à l'étape « ajuster ». Les variantes arrivent donc quand la lampe est complète, juste avant l'atelier.

Le quiz de la section 2 se fait en conséquence après ceux de la section 3.

### Ce que l'on survole

Ces notions sont présentées dans l'application. Elles ne sont pas exigées en séance ; certaines servent de défi.
- *Unit Scale* : une phrase, celle de l'encart *WARNING* de l'application.
- *Save Startup File* et *Load Factory Settings* : le sous-menu est montré, sans clic. Sur les postes de la salle, partagés, on n'enregistre pas de fichier de démarrage.
- Les orientations *Normal*, *View*, *Cursor*, *Gimbal* et *Parent* : citées.
- Plusieurs cibles d'aimantation à la fois (`Maj + clic`), la touche `B` pendant le geste : une astuce, et un défi.
- L'édition proportionnelle (`O`), `G G` et `Alt + S` : une minute de démonstration, puis des défis ★★.
- Le biseau d'un sommet (`Ctrl + Maj + B`) et *Extrude Individual Faces* : cités, puis défis.
- *Background* (l'image toujours derrière) : cité à côté de *Reference*.

## Minutage

| Horaire | Durée | Séquence | Section | Modalité |
|---|---|---|---|---|
| 0:00 | 10 min | Ouverture : où l'on en est | | Collectif 7 min + poste 3 min |
| 0:10 | 15 min | Les cotes et leur unité | 1 | Démo 5 + guidé 8 + quiz 2 |
| 0:25 | 5 min | Le fichier du fil rouge | 1 | Guidé 5 |
| 0:30 | 15 min | Lire la forme : affichage, *Clip Start*, Quad View | 1 | Démo 5 + guidé 8 + autonomie 2 |
| 0:45 | 12 min | Images de référence | 1 | Démo 4 + guidé 3 + autonomie 5 |
| 0:57 | 8 min | À votre main : *Quick Favorites*, navigation, saisie | 1 | Démo 4 + guidé 2 + autonomie 2 |
| 1:05 | 10 min | Pause | | |
| 1:15 | 12 min | La méthode et l'encombrement | 2 | Démo 4 + guidé 8 |
| 1:27 | 25 min | Les grands volumes | 2 | Démo 6 + guidé 8 + autonomie 11 |
| 1:52 | 15 min | Orienter : la tête | 3 | Démo 5 + guidé 8 + quiz 2 |
| 2:07 | 28 min | Aimanter et mesurer : les articulations | 3 | Démo 9 + guidé 13 + autonomie 5 + quiz 1 |
| 2:35 | 10 min | Pause | | |
| 2:45 | 15 min | Éditer avec précision : biseau et extrusions | 3 | Démo 6 + guidé 6 + autonomie 3 |
| 3:00 | 15 min | Variantes et silhouette | 2 | Démo 5 + guidé 9 + quiz 1 |
| 3:15 | 25 min | Atelier : trois pistes pour une revue de concept | | Lancement 2 + autonomie 20 + revue 3 |
| 3:40 | 10 min | Galerie, bilan et passerelle vers le chapitre 2 | | Collectif |
| 3:50 | | Fin | | |

Sur 3 h 30 : 53 minutes de démonstration, 78 minutes de pratique guidée, 48 minutes en autonomie, 6 minutes de quiz et 25 minutes en collectif. Par section : 55 minutes pour la section 1, 52 pour la section 2 (dont les variantes), 58 pour la section 3. Les pauses tombent aux mêmes heures qu'à l'initiation et au chapitre 2.

## Avant la demi-journée

### Les postes des apprenants

- [ ] Le dossier de travail contient `PRC02_ch1_blocage_lampe.blend` et les deux croquis, `croquis_lampe_face.png` et `croquis_lampe_profil.png`. Les croquis seront téléchargeables depuis l'application à la prochaine mise à jour du contenu. D'ici là, distribuez-les vous-même avec le fichier : clé USB, dossier partagé ou adresse `raw.githubusercontent.com` du dépôt, comme les fichiers de l'initiation.
- [ ] Blender 5.2 LTS s'ouvre, avec une souris à trois boutons ; *Emulate Numpad* reste activé sur les portables sans pavé numérique.
- [ ] Les *Quick Favorites* et les options que les apprenants essaieront s'enregistrent dans les préférences du poste. C'est voulu : ce sont leurs options. Prévenez seulement le gestionnaire des postes si la salle est partagée.

### Votre poste de démonstration

- Blender lancé en configuration d'usine (`blender.exe --factory-startup`), comme à l'initiation. Votre écran correspond alors à celui des apprenants, et vos préférences ne sont pas touchées.
- *Resolution Scale* à 1,3 pour le vidéoprojecteur.
- `PRC02_ch1_blocage_lampe.blend` prêt à ouvrir. Préparez aussi une copie de travail, enregistrée sous un autre nom, pour vos démonstrations : le fichier livré reste intact.
- **Ne cliquez pas sur *Save Startup File*** pendant la démo du fichier de démarrage. Par prudence, montrez le sous-menu sans l'exécuter : le fichier de démarrage de votre configuration habituelle reste ainsi intact.

### Le matériel de la salle

- Les post-it vert et rose des points de contrôle.
- Le minuteur.
- Le paperboard, préparé avant l'arrivée des apprenants :
  - **la règle du jour :** « Tapez l'unité. Dans un champ : `25mm`. Pendant un geste : `=`, puis `25mm`. » ;
  - **le corrigé :** « collections *Variante A*, *B* et *C*, œil fermé » ;
  - **le fichier de fin :** `lampe_blocage_v001.blend`, moteur EEVEE ;
  - **les raccourcis du jour,** complétés au fil de la séance : `N`, `Ctrl + Alt + Q`, `Q`, `H` et `Alt + H`, `/`, `,`, `G Z Z`, `Ctrl` pendant un geste, `Maj + Tab`, `Ctrl + B`, `Alt + E`.
- Les consignes par paliers (partie « Les consignes par paliers »), projetées ou imprimées. Le fichier livré n'a pas de texte LISEZ-MOI : elles en tiennent lieu.

## Ouverture · 0:00 (10 min)

**Où l'on en est (7 min, collectif) :**
- « L'initiation vous a donné les gestes de base. Aujourd'hui commence la formation proprement dite. » Rappelez le parcours de la lampe : bloquée aujourd'hui, modélisée au chapitre 2, habillée au chapitre 3, mise en scène et exportée au chapitre 4.
- **Montrez le but :** ouvrez votre copie de `PRC02_ch1_blocage_lampe.blend` et les yeux des trois variantes. Passez-les en ombres chinoises (réglage de la séquence 3:00). « À midi, vous aurez votre lampe, en trois pistes comme celles-ci, et vous en défendrez une. »
- **Le mot du jour :** le blocage, ou *greyboxing*, c'est la maquette en mousse du designer. On juge les proportions avant le détail.
- **Annoncez la règle :** les réglages de la première partie sont des options. Chacun garde ce qui l'aide. Une seule habitude compte : taper l'unité.

**Sur poste (3 min) :** chacun lance Blender et ferme l'écran d'accueil. La scène d'usine, avec son cube, sert à la première séquence.

**Point de contrôle :** sur chaque écran, la scène d'usine.

## Section 1 · Un environnement adapté au design produit

Ancre `ch1_sec1_title` · 55 minutes, de 0:10 à 1:05.

### Prérequis et nouveautés

| Prérequis, déjà vus | Où |
|---|---|
| L'éditeur de propriétés et ses onglets, dont *Scene* et *Render* | Basics 101 ; chasse aux réglages |
| La barre latérale `N`, onglet *Item* | Initiation, demi-journée 1 |
| `G` avec un axe et une valeur | Basics 102 § 1 ; initiation, demi-journée 1 |
| Les vues `1`, `3`, `7`, `5` et `Ctrl` pour la vue opposée | Basics 101 § 4 ; défi des vues |
| Les quatre modes d'affichage et la flèche de leurs options | Basics 101 § 4 |
| L'Outliner et l'œil | Basics 101 ; activité A |
| *File > Open*, *Save As* ; *Edit > Preferences* (*Emulate Numpad*) | Basics 102 § 4 ; initiation |

| Nouveau, dans l'ordre d'introduction | Séquence |
|---|---|
| 1. Une valeur avec son unité dans un champ | Les cotes et leur unité |
| 2. Un nombre seul s'entend dans l'unité affichée ; `=` pour taper une unité pendant un geste | Les cotes et leur unité |
| 3. L'unité d'affichage : *Scene > Units > Length*, une option recommandée | Les cotes et leur unité |
| 4. Le menu *Viewport Shading* : *Lighting*, *Color*, *Cavity*, *Outline* | Lire la forme, cycle A |
| 5. *Clip Start* | Lire la forme, cycle B |
| 6. La Quad View | Lire la forme, cycle C |
| 7. L'image de référence : *Add > Image > Reference*, et ses réglages dans *Object Data* | Images de référence |
| 8. Les *Quick Favorites* ; les options de navigation et de saisie | À votre main |

### 0:10 · Les cotes et leur unité (15 min)

**Vous montrez (5 min),** dans la scène d'usine, qui affiche des mètres :
1. Le cube sélectionné, `N`, onglet *Item* : *Dimensions* 2 m.
2. **Dans un champ, l'unité est toujours comprise.** Dans *Dimensions* X, tapez `180mm` : le champ affiche 0,18 m. Puis `3.5cm`, puis `1m 20mm`.
3. **Pendant un geste, c'est différent.** `G Z 25` : le cube monte de 25 m. « Un nombre seul s'entend dans l'unité affichée. » `Ctrl + Z`. Faites deviner : « Et `G Z 25mm` ? » Essayez : 25 m encore, les lettres sont ignorées. `Ctrl + Z`. Puis `G Z`, `=`, `25mm`, Entrée : 25 mm. « La touche `=` ouvre la saisie avancée, qui comprend les unités. Le `*` du pavé numérique fait de même. »
4. **Une option, recommandée pour le design produit :** onglet *Scene*, rubrique *Units*, champ *Length* sur *Millimeters*. Le même cube affiche 180 mm, et `G Z 25` monterait de 25 mm. *Unit Scale* reste à 1,000 : une phrase, celle de l'encart *WARNING*. « Je travaille souvent en mètres moi-même : les deux se valent, tant que vous tapez l'unité. »
5. **Ailleurs :** une planche de bord ou un phare se cote en millimètres ; l'implantation d'un tram en mètres. Chacun garde l'affichage de son métier.

**Ils font, en guidé (8 min),** dans la scène d'usine :
1. Le cube devient une galette de socle : *Dimensions* `180mm`, `180mm`, `25mm`.
2. `G Z`, `=`, `12.5mm`, Entrée : elle repose sur le sol.
3. `Ctrl + A > Scale` : l'échelle revient à 1, les cotes restent.
4. En option, *Length* sur *Millimeters* : les mêmes cotes, lues en millimètres. Chacun garde l'affichage qu'il préfère.

**Quiz (2 min), ensemble à l'écran :** le quiz de la section 1, dans sa version révisée (partie « Les quiz retenus »).

**Point de contrôle :** dans `N > Item`, *Dimensions* 180 × 180 × 25 mm (0,18 × 0,18 × 0,025 m), *Location* Z 12,5 mm (0,0125 m), *Scale* 1.

**Points d'observation :**
- La galette s'envole à 12,5 m : le `=` a été oublié, dans une scène en mètres. `Ctrl + Z`.
- `=` sans effet : le pavé numérique fait l'affaire (`*`). Sur un clavier français, `=` est la touche à gauche de la touche d'effacement.
- Un champ qui refuse une valeur : une virgule a été tapée au lieu d'un point (`3,5cm` au lieu de `3.5cm`).

**Corrigé :** les valeurs du point de contrôle. La scène d'usine n'est pas enregistrée.

### 0:25 · Le fichier du fil rouge (5 min)

**Ils font, en guidé, pas à pas :**
1. *File > Open* : `PRC02_ch1_blocage_lampe.blend`. *Don't Save* pour la scène d'usine.
2. *File > Save As* : `lampe_blocage_v001.blend`, dans le dossier de travail. Le fichier livré reste intact.
3. Onglet *Render* : vérifiez que *Render Engine* indique **EEVEE** ; choisissez-le si besoin. « La formation travaille avec EEVEE, le moteur de la chasse aux réglages. En mode *Solid*, rien ne change à l'écran ; le chapitre 4 en dira plus. » Tant que le fichier livré n'est pas corrigé, il est réglé sur Cycles et ce geste est nécessaire.
4. Onglet *Scene*, *Units* : ce fichier affiche des millimètres. C'est un réglage du fichier, pas une exigence : chacun peut repasser en mètres. Les consignes donnent toujours l'unité.
5. Le tour du fichier : la vue de face montre le croquis ; dans l'Outliner, la collection *Croquis*, puis *Variante A*, *B* et *C*, l'œil fermé. « Ce sont trois blocages terminés : votre corrigé. On les ouvre pour comparer, jamais pour copier. »
6. `Ctrl + S`.

**Point de contrôle :** la barre de titre affiche `lampe_blocage_v001.blend` ; *Render Engine* indique EEVEE.

### 0:30 · Lire la forme : affichage, *Clip Start*, Quad View (15 min)

Chacun ouvre l'œil de *Variante A*, qui sert de sujet pendant cette séquence.

**Cycle A : le menu *Viewport Shading* (démo 2 min, guidé 3 min).** Vous montrez la flèche à droite des quatre modes d'affichage, puis *Lighting* (*Studio*, *MatCap*, *Flat*), *Color* (*Random*, déjà choisi dans ce fichier), *Cavity* et *Outline*. Ils font : *Cavity* activé, un essai de *MatCap*, puis retour à *Studio*. « Regardez la jonction entre le socle et le bras. »

**Cycle B : *Clip Start* (démo 2 min, guidé 3 min).** En perspective (`5`), sélectionnez *Interrupteur_A*, cadrez-le (`.` du pavé numérique) et zoomez au plus près. Le fichier est déjà réglé à 1 mm : tapez `10mm`, la valeur d'usine, dans `N`, onglet *View*, champ *Clip Start*. L'interrupteur se coupe. Revenez à `1mm`. Ils font le même essai.

**Cycle C : la Quad View (démo 1 min, guidé 2 min).** `Ctrl + Alt + Q` : trois vues orthographiques et une perspective. Ils l'ouvrent, déplacent un objet de la variante et le voient bouger dans les quatre vues, `Ctrl + Z`, puis `Ctrl + Alt + Q` pour revenir.

**En autonomie (2 min) :** chacun choisit l'affichage qui l'aide le plus pour la suite, puis referme l'œil de *Variante A*.

**Point de contrôle :** *Clip Start* à 1 mm ; *Variante A* masquée ; une seule vue 3D.

**Points d'observation :**
- *Clip Start* sans effet visible : la vue est restée orthographique. Passez en perspective (`5`).
- Une Quad View qui ne se referme pas : la souris n'était pas au-dessus de la vue 3D.
- Un apprenant qui modifie un objet de la variante : `Ctrl + Z`. Le corrigé doit rester juste.

### 0:45 · Images de référence (12 min)

**Vous montrez (4 min) :**
1. En vue de face (`1`), le croquis s'affiche ; en tournant la vue, il disparaît. Sélectionnez *Croquis_face* dans l'Outliner : c'est un *Empty*, un objet sans géométrie qui porte une image.
2. Onglet *Object Data* : *Opacity*, *Depth* (*Front*, *Back*), *Show In* (*Perspective*, *Only Axis Aligned*).
3. Comment on en place une : vue de droite (`3`), *Add > Image > Reference*, puis l'image. Elle arrive face à la vue, au curseur 3D, et mesure 5 m de large. *Background* la garde toujours derrière. On peut aussi faire glisser l'image depuis l'Explorateur Windows.
4. **Ailleurs :** les vues de face et de profil d'un nez de tram, d'un rétroviseur, d'une cabine d'avion d'affaires.

**Ils font, en guidé (3 min),** sur *Croquis_face* : *Opacity* à 0,2 puis 0,5 ; *Depth* sur *Front* puis *Back* ; *Perspective* coché puis décoché dans *Show In*.

**Ils font, en autonomie (5 min) : replacer le croquis de profil.** Ils masquent *Croquis_profil* (œil), puis le replacent eux-mêmes avec les valeurs des consignes :
- vue de droite (`3`), *Add > Image > Reference*, `croquis_lampe_profil.png` ;
- *Object Data* : *Size* `560mm` ; *Opacity* 0,5 ; *Depth* *Back* ; *Show In* : *Perspective* décoché, *Only Axis Aligned* coché ;
- `N > Item`, *Location* : X `-300mm`, Z `222mm`.

Ils rouvrent l'œil de *Croquis_profil* pour comparer, puis suppriment le leur (`X`). Le blocage s'appuie sur celui du fichier.

**Point de contrôle :** les deux images se superposent exactement, puis il ne reste que *Croquis_profil*, visible.

**Corrigé :** l'objet *Croquis_profil* du fichier.

**Points d'observation :**
- Une image immense : *Size* vaut encore 5 m.
- Une image couchée : elle a été ajoutée en vue de face ou en perspective. Supprimez-la et recommencez en vue de droite.
- Le fichier image introuvable : les croquis n'ont pas été copiés dans le dossier de travail. Solution de repli : réglages seulement, sans replacement.

### 0:57 · À votre main : *Quick Favorites*, navigation, saisie (8 min)

Annoncez-le : « Tout ce qui suit est une option. »

**Vous montrez (4 min) :**
1. Menu *View > Area*, clic droit sur *Toggle Quad View*, *Add to Quick Favorites*. La touche `Q` ouvre le menu sous la souris.
2. *Edit > Preferences > Navigation* : *Orbit Around Selection*, *Zoom to Mouse Position* et la case *Depth* de la ligne *Auto*.
3. *Edit > Preferences > Input*, rubrique *Keyboard*, sous *Emulate Numpad* : *Default to Advanced Numeric Input*. Cochée, elle rend le `=` inutile : `G Z 25mm` marche directement.
4. *File > Defaults* : *Save Startup File* et *Load Factory Settings*. Montrez-les sans cliquer. « Chez vous, ou pour une équipe, un fichier de démarrage commun garde la même unité pour tous. »

**Ils font :**
- **en guidé (2 min) :** *Toggle Quad View* dans les *Quick Favorites*, puis `Q` ;
- **en autonomie (2 min) :** une option de navigation ou de saisie à essayer, à garder ou non.

**Point de contrôle :** `Q` ouvre un menu qui contient au moins une entrée.

**Points d'observation :**
- Votre écran ne garde pas les options des apprenants : il tourne en configuration d'usine. Pendant vos démos, tapez donc toujours `=` avant une unité.
- Un apprenant qui a cliqué *Save Startup File* : rien de grave sur son poste. Prévenez seulement le gestionnaire des postes.

### 1:05 · Pause (10 min)

## Section 2 · Explorer un concept par blocage de volumes

Ancre `ch1_sec2_title` · 37 minutes de 1:15 à 1:52, puis 15 minutes de 3:00 à 3:15 (voir « L'ordre de la séance »).

### Prérequis et nouveautés

| Prérequis, déjà vus | Où |
|---|---|
| `Maj + A`, F9, `X` | Basics 102 § 2 ; initiation, demi-journée 1 |
| `G`, `R` avec un axe et une valeur ; `Maj + C` pour ramener le curseur | Initiation, demi-journée 1 |
| Renommer (double-clic dans l'Outliner, `F2`) ; `M > New Collection` | Basics 102 § 4 ; initiation, demi-journée 1 |
| `Ctrl + A > Scale` | Basics 103 § 4 ; clinique, patient 2 |
| La saisie avec unité, les croquis, le menu *Viewport Shading* | Section 1 |

| Nouveau, dans l'ordre d'introduction | Séquence |
|---|---|
| 1. La méthode en quatre temps ; l'encombrement | Méthode et encombrement |
| 2. Le champ *Dimensions* | Méthode et encombrement |
| 3. `H`, `Alt + H` | Méthode et encombrement |
| 4. La collection active, qui reçoit les nouveaux objets | Les grands volumes, cycle A |
| 5. La vue locale (`/`) | Les grands volumes, cycle B |
| 6. *Duplicate Collection* | Variantes et silhouette, cycle A |
| 7. Le réglage « ombre chinoise » : *Flat*, *Custom* noir, fond *Custom* clair | Variantes et silhouette, cycle B |

### 1:15 · La méthode et l'encombrement (12 min)

**Vous montrez (4 min) :**
1. Au paperboard, la méthode en quatre temps : l'encombrement, les grands volumes, les proportions, la silhouette. « Se tromper vite coûte peu. »
2. `Maj + A > Mesh > Cube` : 2 m de côté. Dans `N > Item`, *Dimensions* : `420mm`, `180mm`, `450mm`. Les champs *Scale* changent en conséquence. Une phrase : cette échelle se remet à 1 avec `Ctrl + A > Scale` avant certaines opérations, comme le biseau de la section 3.
3. *Location* : X `120mm`, Z `225mm`. Renommez le cube *Encombrement*.
4. Vues de face et de droite : le croquis tient dans le cube. `H` le masque, `Alt + H` le réaffiche.
5. **Ailleurs :** l'enveloppe d'un siège d'avion, d'un rétroviseur, d'un pupitre de conduite.

**Ils font, en guidé (8 min) :** les étapes 2 à 4.

**Point de contrôle :** vues `1` et `3`, le croquis tient dans l'encombrement. *Encombrement* est rangé dans *Scene Collection*, puis masqué avec `H`.

**Corrigé :** les valeurs ci-dessus. La lampe de *Variante A* tient dans cet encombrement : elle s'étend de -90 à 313 mm en X et de 0 à 442 mm en Z.

**Points d'observation :**
- Un cube qui déborde du croquis : `Location` a été oubliée.
- `Alt + H` ne fait pas réapparaître les variantes : c'est normal, elles sont masquées par l'œil de leur collection.

### 1:27 · Les grands volumes (25 min)

**Cycle A : le socle et le bras du bas (démo 4 min, guidé 8 min).**

Vous montrez :
1. **La collection active.** Dans l'Outliner, clic droit sur *Scene Collection > New Collection*, renommez-la *Lampe*, puis cliquez-la : elle est surlignée. Chaque nouvel objet s'y range.
2. *Socle* : `Maj + A > Mesh > Cylinder`, F9 : *Vertices* 32, *Radius* `90mm`, *Depth* `25mm`. Puis `G Z`, `=`, `12.5mm`. « Peu de segments suffisent pour un blocage. »
3. *Bras_bas* : *Cylinder*, F9 : *Vertices* 16, *Radius* `8mm`, *Depth* `260mm`. `R Y 15.6`, puis en vue de face (`1`), `G` pour le poser sur le croquis. Repère : *Location* -5, 0, 165 mm.

Ils font, en guidé : *Lampe* active, puis *Socle* et *Bras_bas*, nommés.

**Cycle B : la vue locale (démo 2 min), puis l'autonomie (11 min).**

Vous montrez : *Bras_bas* sélectionné, `/` du pavé numérique. Seul le bras reste à l'écran ; `/` ramène la vue complète.

Ils font, en autonomie, avec les consignes :
- *Interrupteur* : *Cylinder*, *Vertices* 16, *Radius* `8mm`, *Depth* `6mm`, *Location* `55mm`, `0`, `28mm` ;
- *Bras_haut* : *Cylinder*, *Vertices* 16, *Radius* `7mm`, *Depth* `220mm`, `R Y 50.5`, posé sur le croquis (repère : 115, 0, 360 mm) ;
- une vérification de chaque pièce en vue locale, puis `Ctrl + S`.

**Point de contrôle :** en vue de face, les quatre volumes suivent le croquis. Dans `N > Item`, *Socle* mesure 180 × 180 × 25 mm. Les quatre pièces sont rangées dans *Lampe*.

**Corrigé :** collection masquée *Variante A* : *Socle_A*, *Interrupteur_A*, *Bras_bas_A*, *Bras_haut_A*.

**Points d'observation :**
- Une pièce rangée dans *Scene Collection* ou dans *Croquis* : la collection active n'était pas *Lampe*. `M > Lampe`.
- Un cylindre de 2 m : F9 a été oublié, ou le panneau s'est refermé après un autre geste.
- Une pièce géante ou minuscule : une valeur tapée sans unité. Lisez l'unité affichée dans le champ.
- Une pièce qui n'apparaît pas à l'origine : le curseur 3D a été déplacé. `Maj + C`.
- Un bras incliné dans le mauvais sens : `R Y -15.6` au lieu de `15.6`. Dans Blender 5.2, `R Y 15.6` donne bien +15,6° dans le champ *Rotation* Y.
- Un bras posé de face mais décalé en profondeur : la règle de l'activité A, deux vues orthographiques avant de valider.

## Section 3 · Transformer et éditer avec précision

Ancre `ch1_sec3_title` · 58 minutes, de 1:52 à 3:00, pause comprise.

### Prérequis et nouveautés

| Prérequis, déjà vus | Où |
|---|---|
| `G`, `R`, `S` avec un axe ; `Maj + Z` pour exclure un axe | Basics 102 § 1 ; initiation |
| Le Mode Édition, `1`, `2`, `3`, `Alt + clic` | Basics 103 § 1 ; initiation, demi-journée 2 |
| `E`, `I`, `Ctrl + B` avec la molette et F9 | Basics 103 § 2 ; exercices d'édition ; activité B |
| *Alt + E > Extrude Individual Faces* (palier ★★ des sièges) | Initiation, activité B |
| L'échelle appliquée | Basics 103 § 4 ; clinique |
| La saisie avec unité et `=` ; `Dimensions` ; la vue locale | Sections 1 et 2 |

| Nouveau, dans l'ordre d'introduction | Séquence |
|---|---|
| 1. Le menu *Transform Orientation* et le menu circulaire `,` ; *Global* et *Local* ; `G Z Z` | Orienter : la tête |
| 2. L'aimantation : *Snap Target*, *Snap Base*, `Ctrl` pendant le geste, `Maj + Tab` | Aimanter et mesurer, cycle A |
| 3. L'outil *Measure* ; *Edge Length* | Aimanter et mesurer, cycle B |
| 4. Le biseau mesuré : *Width* avec son unité, *Segments*, *Profile Shape*, *Clamp Overlap* | Éditer avec précision, cycle A |
| 5. *Extrude Manifold* et *Extrude Faces Along Normals* | Éditer avec précision, cycle B |

La section approfondit Basics 103 sans le reprendre : les outils d'édition sont connus, on apprend à les doser au millimètre et à les orienter.

### 1:52 · Orienter : la tête (15 min)

**Vous montrez (5 min) :**
1. *Tête* : `Maj + A > Mesh > Cone`, F9 : *Vertices* 24, *Radius 1* `60mm`, *Radius 2* `22mm`, *Depth* `110mm`. `R Y -30` : la tête s'incline vers le plan de travail.
2. L'outil *Move* de la barre d'outils : le gizmo suit les axes du monde, *Global*. Menu *Transform Orientation* de l'en-tête, ou `,` : *Local*. Le gizmo s'incline avec la tête.
3. Retour en *Global*, puis `G Z Z` : le second `Z` suit l'axe propre de la tête. Elle avance ou recule sans glisser de côté.
4. **Ailleurs :** un rétroviseur incliné, un volet d'aile, un pare-brise de cabine.

**Ils font, en guidé (8 min) :**
1. la tête, avec les valeurs de la démo ;
2. en vue de face, `G` pour la placer près du haut de *Bras_haut* ;
3. `G Z Z` pour l'avancer jusqu'à ce que le petit bout touche le bras. Repère : *Location* 233,5, 0, 372 mm.

**Quiz (2 min), ensemble à l'écran :** le premier quiz de la section 3, `G Z Z`.

**Point de contrôle :** la tête inclinée de 30°, son petit bout contre le haut du bras, son ouverture tournée vers la table. `Ctrl + S`.

**Corrigé :** *Tête_A*, dans la collection masquée *Variante A*.

**Points d'observation :**
- `G Z` seul fait monter la tête à la verticale : c'est l'axe du monde. Le second `Z` change d'axe.
- Une tête tournée vers le haut : `R Y 30` au lieu de `-30`.
- Le gizmo reste droit : l'outil actif n'est pas *Move*, ou l'orientation est restée *Global*.

### 2:07 · Aimanter et mesurer : les articulations (28 min)

**Cycle A : l'aimantation (démo 6 min, guidé 8 min, autonomie 5 min, quiz 1 min).**

Vous montrez :
1. L'icône d'aimant de l'en-tête et `Maj + Tab`. Au quotidien, `Ctrl` pendant le geste suffit.
2. Le menu à droite de l'aimant : *Snap Base* sur *Center*, *Snap Target* sur *Face Center*. Citez aussi *Face* : l'objet se pose sur une surface. Ils l'essaieront en autonomie, et le câble du chapitre 2 s'en servira.
3. *Articulation_bas* : `Maj + A > Mesh > UV Sphere`, F9 : *Segments* 16, *Ring Count* 8, *Radius* `15mm`. `G`, puis `Ctrl` en survolant le bout inférieur de *Bras_bas* : la sphère se centre sur la face du bout.
4. Une astuce : `Maj + clic` dans *Snap Target* ajoute une cible ; `B` pendant le geste choisit le point de base.
5. **Ailleurs :** poser une roue sur son moyeu, un siège sur son rail, un feu dans son logement.

Ils font :
- **en guidé :** *Articulation_bas* (*Radius* `15mm`), puis *Articulation_milieu* (*Radius* `14mm`), au bout supérieur de *Bras_bas* ;
- **en autonomie :**
  - *Articulation_haut* (*Radius* `12mm`), au bout supérieur de *Bras_haut*, puis un contrôle de la tête : elle touche l'articulation. Si besoin, `G Z Z`. Un gros plan sur une articulation rappelle *Clip Start* ;
  - **une pose sur une surface (1 min environ) :** vue de dessus (`7`), *Snap Target* sur *Face*, *Snap Base* sur *Closest*. *Interrupteur* sélectionné, `G`, puis `Ctrl` au-dessus du dessus du socle : l'interrupteur s'y pose. C'est ainsi que le chapitre 2 pose le câble.

**Quiz (1 min), ensemble à l'écran :** le second quiz de la section 3, la touche `Ctrl`.

**Cycle B : mesurer (démo 3 min, guidé 5 min).**

Vous montrez :
1. En vue de face, l'outil *Measure* de la barre d'outils. Cliquez-glissez d'un bord à l'autre du dessus du socle en maintenant `Ctrl` : 180 mm.
2. En Mode Édition, le menu *Mesh Edit Mode*, à droite d'*Overlays* : *Measurement > Edge Length*.

Ils font, en guidé :
1. le diamètre du socle (180 mm) ;
2. la hauteur totale, du dessous du socle au sommet de l'articulation du haut (environ 442 mm) ;
3. *Bras_bas* en Mode Édition, *Edge Length* coché, une arête verticale sélectionnée : 260 mm.

**Point de contrôle :** les trois articulations sont centrées sur les bouts des bras ; l'interrupteur repose sur le socle. La règle donne 180 mm et environ 440 mm. `Ctrl + S`.

**Corrigé :** *Articulation_bas_A*, *_milieu_A* et *_haut_A*, dans la collection masquée *Variante A*. Elles sont aux bouts exacts des bras : (-40, 0, 40), (30, 0, 290) et (200, 0, 430) mm. *Interrupteur_A* repose sur le socle, son centre à 28 mm de haut.

**Points d'observation :**
- La sphère se pose sur un sommet ou sur le bord : *Snap Target* est resté sur *Vertex* (réglage du fichier livré) ou *Snap Base* sur *Closest*.
- L'interrupteur s'enfonce à moitié dans le socle : *Snap Base* est resté sur *Center*, c'est son centre qui s'est posé. Passez sur *Closest*.
- Tout s'accroche, même sans `Ctrl` : l'aimant de l'en-tête est allumé. `Maj + Tab`.
- Une règle qui tombe dans le vide : `Ctrl` a été relâché trop tôt.
- Aucune longueur ne s'affiche : *Edge Length* ne montre que les arêtes sélectionnées, en Mode Édition.

### 2:35 · Pause (10 min)

### 2:45 · Éditer avec précision : biseau et extrusions (15 min)

Le travail se fait sur une **pièce d'essai**, pas sur la lampe. L'encart *IMPORTANT* de l'application le dit : un biseau posé trop tôt alourdit chaque correction. « Ces outils serviront dès que les proportions seront arrêtées. »

**Préparation (en guidé, 1 min) :** *Socle* sélectionné, `Maj + D`, `X`, `=`, `-400mm`, Entrée. Puis `/` : la copie seule, en vue locale. `Tab`.

**Cycle A : le biseau mesuré (démo 3 min, guidé 2 min, autonomie 2 min).**

Vous montrez : mode arête (`2`), `Alt + clic` sur l'arête du haut, `Ctrl + B`, un petit mouvement de souris, clic. Puis F9 : *Width* `4mm` ; *Segments* 1, un chanfrein, puis 4, un congé ; *Profile Shape* 0,5, un arc de cercle ; *Clamp Overlap*. Une phrase sur l'encart *WARNING* : sur une échelle non appliquée, le biseau est irrégulier. Citez `Ctrl + Maj + B`, le biseau d'un sommet.

Ils font :
- **en guidé :** le même biseau, puis le passage d'un chanfrein à un congé dans F9 ;
- **en autonomie :** un congé de `2mm` sur l'arête du dessous.

**Cycle B : les extrusions (démo 2 min, guidé 3 min, autonomie 1 min).**

Vous montrez le menu `Alt + E` et ses trois variantes :
- *Extrude Faces Along Normals* sur l'anneau de faces du flanc : un bandeau ;
- *Extrude Individual Faces* : citée, les accoudoirs des sièges ;
- *Extrude Manifold*, vers l'intérieur : une encoche pour la sortie du câble, sans faces parasites.

Ils font :
- **en guidé :** l'encoche. Mode face (`3`), quatre faces du flanc arrière, `Alt + E > Extrude Manifold`, `=`, `-5mm`, Entrée ;
- **en autonomie :** le bandeau. `Alt + clic` sur une arête verticale du flanc, `Alt + E > Extrude Faces Along Normals`, `=`, `2mm`, Entrée.

**Survol (1 min, démo seule) :** l'édition proportionnelle (`O`), `G G` et `Alt + S`. Ils sont dans l'application et dans les défis.

**Pour finir :** `Tab`, `/`, puis `X` : la pièce d'essai est supprimée. Elle ne doit pas partir dans les variantes.

**Point de contrôle :** avant la suppression, F9 affiche le dernier réglage ; la pièce d'essai montre son congé de 4 mm, son encoche de 5 mm et son bandeau.

**Corrigé :** pas de collection dans le fichier livré, et pas de fichier corrigé (décision du formateur). Le résultat se lit dans F9, et la figure 1.21 de l'application montre le biseau de 4 mm à 4 segments sur le socle.

**Points d'observation :**
- Un biseau qui part de travers ou s'arrête net : *Clamp Overlap* le limite, ou l'arête choisie n'est pas la boucle entière.
- Une encoche qui ressort au lieu de rentrer : la valeur était positive. `Ctrl + Z`, puis `-5mm`.
- Une extrusion de plusieurs mètres : le `=` a été oublié, dans une scène en mètres. `Ctrl + Z`.
- La copie a été faite en Mode Édition : `Maj + D` a dupliqué la géométrie dans le socle lui-même. `Ctrl + Z`, `Tab`, et recommencez en Mode Objet.

## Section 2, suite · Comparer des variantes

### 3:00 · Variantes et silhouette (15 min)

**Cycle A : *Duplicate Collection* (démo 3 min, guidé 6 min).**

Vous montrez :
1. Clic droit sur la collection *Lampe* dans l'Outliner, *Duplicate Collection*. La copie s'appelle *Lampe.001*, ses pièces *Socle.001*, *Bras_bas.001*… Renommez la collection *Lampe_B*.
2. Clic droit sur *Lampe_B* > *Select Objects*, puis `G X`, `=`, `550mm`, Entrée.
3. Une variante : *Bras_haut.001* plus long. *Dimensions* Z `300mm`, puis `G Z Z`, `=`, `40mm`, Entrée : le bas du bras revient sur son articulation. `Ctrl + A > Scale`.
4. *Articulation_haut.001* : `G` avec `Ctrl` sur le nouveau bout du bras (*Face Center*, *Center*). *Tête.001* : `G` pour la rapprocher, puis `G Z Z`.
5. **Ailleurs :** trois pistes de calandre, de nez de train ou de winglet, côte à côte.

Ils font, en guidé : la même variante B.

**Cycle B : juger la silhouette (démo 2 min, guidé 3 min).**

Vous montrez : menu *Viewport Shading*, *Lighting* sur *Flat*, *Color* sur *Custom* avec du noir, *Background* sur *Custom* avec un fond clair. Les deux lampes deviennent des ombres chinoises. Vues `1`, `3` et `7`.

Ils font, en guidé : le même réglage, puis les trois vues. « Laquelle se lit le mieux ? »

**Quiz (1 min), ensemble à l'écran :** le quiz de la section 2, la silhouette.

**Point de contrôle :** deux lampes côte à côte, en ombres chinoises ; la variante B a un bras plus long. `Ctrl + S`.

**Corrigé :** la collection masquée *Variante B*, qui allonge elle aussi le bras supérieur (300 mm, avec une inclinaison un peu plus forte).

**Points d'observation :**
- *Duplicate Linked* choisi au lieu de *Duplicate Collection* : changer le bras de B change aussi celui de la lampe. `Ctrl + Z`.
- Le bras de B ne touche plus son articulation du bas : `G Z Z` a été oublié, ou fait dans le mauvais sens.
- Des objets restés à la place de l'original : ils n'étaient pas sélectionnés, par exemple masqués avec `H`.
- L'aimantation pose l'articulation sur le bord : *Snap Target* est resté sur *Face* depuis la pose de l'interrupteur. Revenez à *Face Center* et *Center*.

## Atelier · Trois pistes pour une revue de concept · 3:15 (25 min)

**Situation :** « Revue de concept demain matin. Présentez trois pistes de lampe, en silhouette, et défendez celle que vous retenez. »

**Nouveau :** aucune notion. L'atelier réinvestit les trois sections.

**Déroulé :**
1. **Lancement (2 min).** Ouvrez l'œil de *Variante C* : une tête cylindrique. « La vôtre peut être différente : socle carré, tête plus large, bras plus court. » Lancez le minuteur.
2. **Autonomie (20 min).** Chacun suit la partie « Atelier » des consignes. Annoncez les 5 dernières minutes : c'est le moment de choisir et d'enregistrer.
3. **Revue (3 min).** Deux volontaires projettent leurs trois silhouettes. Question : « Laquelle retenez-vous, et pourquoi ? »

**Le socle de l'atelier :**

| Étape | Ce qu'il faut faire | Gestes réinvestis |
|---|---|---|
| 1 | *Duplicate Collection* de *Lampe*, renommée *Lampe_C*, puis `G X = 1100mm` | *Duplicate Collection*, *Select Objects*, saisie avec unité |
| 2 | Une autre piste. Exemple : *Tête.002* supprimée, puis un cylindre de 24 côtés, *Radius* `50mm`, *Depth* `120mm`, `R Y -30`, posé contre l'articulation et avancé avec `G Z Z` | Primitives et F9, orientation *Local*, aimantation |
| 3 | Les trois pistes comparées en ombres chinoises, sous les vues de face, de droite et de dessus | Réglage silhouette, Quad View |
| 4 | Un contrôle de la piste retenue : diamètre du socle, hauteur totale | *Measure* |
| 5 | La piste retenue visible, les deux autres masquées (œil) ; l'échelle appliquée sur les pièces redimensionnées ; `Ctrl + S` | Outliner, `Ctrl + A > Scale` |

**Paliers :**
- **★ :** renommer les pièces des variantes sans `.001`, par exemple *Socle_B* ; une copie de l'encombrement (`Alt + H`, `Maj + D`, `X = 550mm`) pour voir si la variante B le dépasse ; une quatrième piste.
- **★★ :** voir « Pour ceux qui avancent vite ».

**Points d'observation :**
- Une troisième piste identique à la deuxième : la copie a été faite à partir de *Lampe_B*. C'est possible, mais le décalage est alors de 550 mm depuis B.
- Une silhouette qui ne dit rien : la vue est restée en perspective. Passez en orthographique.
- Un apprenant qui modifie *Variante C* au lieu de sa propre lampe : `Ctrl + Z`, et refermez l'œil des variantes du corrigé.

**Corrigé :** les collections masquées *Variante A*, *B* et *C*. *Variante C* remplace la tête conique par une tête cylindrique (100 mm de diamètre, 120 mm de long).

## Galerie, bilan et passerelle · 3:40 (10 min)

- **Galerie (4 min) :** chaque écran montre ses trois pistes en ombres chinoises, en vue de face. Tout le monde fait le tour des postes.
- **Trois questions (3 min) :**
  - « Pendant un déplacement, comment taper 25 mm, quelle que soit l'unité affichée ? »
  - « Comment avancer la tête dans son propre axe ? »
  - « Quel réglage transforme vos lampes en ombres chinoises ? »
- **Passerelle (2 min) :** « Au chapitre 2, chaque volume devient une pièce propre : un abat-jour creux, des bras à deux tiges, un câble. Votre blocage sert de gabarit. Si votre fichier vous manque, un fichier de départ vous attend. »
- **Dernier contrôle (1 min) :** chacun a enregistré `lampe_blocage_v001.blend`, moteur EEVEE.

## Les quiz retenus

Les quatre quiz du chapitre sont retenus. Chacun se fait ensemble à l'écran, à la fin de la séquence qui l'a préparé : chacun répond pour soi, puis on commente les erreurs.

| Section | Question | Moment | Ce qu'il garantit pour la suite |
|---|---|---|---|
| 1 | Version révisée : « Votre scène affiche des mètres. Pendant le déplacement, que tapez-vous pour monter une pièce de 25 mm ? » `G Z = 25mm` ou `G Z 0.025` | 0:23 | Le chapitre 2 donne toutes ses valeurs en millimètres |
| 3 | La tête est inclinée, l'orientation *Global* est active : comment la déplacer le long de son propre axe Z ? `G Z Z` | 2:05 | La douille du chapitre 2 se place par `G Z Z` |
| 3 | Quelle touche maintenir pour aimanter le temps du geste ? `Ctrl` | 2:26 | Le câble du chapitre 2 se pose par aimantation sur *Face* |
| 2 | Quel réglage du mode *Solid* est le plus parlant pour juger une silhouette ? *Flat*, couleur sombre, fond clair | 3:14 | L'atelier compare les pistes de cette façon |

Le quiz de la section 1 sera remplacé dans l'application par sa version révisée (partie « Ajustements retenus du contenu »). Tant que la mise à jour n'est pas faite, le quiz actuel, *Length* ou *Unit Scale*, se fait au même moment, et vous posez la question révisée à l'oral.

Le support ne contient aucune grille d'autoévaluation : dans l'application, les acquis se vérifient seulement par ces quiz. Les autres gestes dont la suite dépend n'ont pas de quiz ; vous les observez en séance, aux points de contrôle : la vue locale (utilisée de nouveau au chapitre 3), *Duplicate Collection* (le second coloris du chapitre 3), *Clip Start* et la barre latérale (la caméra du chapitre 4).

## Les consignes par paliers

Le fichier livré n'a pas de texte LISEZ-MOI. Ces consignes en tiennent lieu : projetez-les ou imprimez-les. Chaque valeur porte son unité : elles fonctionnent avec un affichage en mètres comme en millimètres.

```
CONSIGNES · Chapitre 1 · Le blocage de la lampe
Les valeurs sont indicatives : adaptez-les à votre concept.
Tapez toujours l'unité. Dans un champ : 25mm.
Pendant un geste : = d'abord, puis la valeur (G Z = 25mm). Sans =, l'unité est ignorée.
Corrigé : collections Variante A, B et C, œil fermé. On compare, on ne copie pas.

1 · LES COTES (scène d'usine, non enregistrée)
1. N > Item > Dimensions : 180mm, 180mm, 25mm.
2. G Z = 12.5mm, Entrée.
3. Ctrl + A > Scale.
4. Option : Scene > Units > Length : Millimeters.
Contrôle : 180 x 180 x 25 mm ; Location Z 12,5 mm ; Scale 1.

2 · LE FICHIER
1. File > Open : PRC02_ch1_blocage_lampe.blend (Don't Save).
2. File > Save As : lampe_blocage_v001.blend. Puis Ctrl + S à chaque contrôle.
3. Render > Render Engine : vérifiez EEVEE, choisissez-le si besoin.

3 · L'AFFICHAGE (œil de Variante A ouvert, puis refermé)
1. Viewport Shading : Color Random, Cavity. Essayez MatCap.
2. En perspective (5) : N > View > Clip Start 10mm, puis 1mm.
3. Ctrl + Alt + Q, puis de nouveau Ctrl + Alt + Q.

4 · LE CROQUIS DE PROFIL
1. Croquis_face : Object Data > Opacity, Depth, Show In. Essayez.
2. Masquez Croquis_profil (œil). Vue de droite (3).
3. Add > Image > Reference : croquis_lampe_profil.png.
4. Object Data : Size 560mm ; Opacity 0.5 ; Depth Back ;
   Show In : Perspective décoché, Only Axis Aligned coché.
5. N > Item > Location : X -300mm, Z 222mm.
6. Rouvrez Croquis_profil : les deux coïncident. Supprimez le vôtre (X).

5 · À VOTRE MAIN (options)
Clic droit > Add to Quick Favorites, puis Q.
Edit > Preferences > Navigation ; Input > Default to Advanced Numeric Input.

6 · L'ENCOMBREMENT
1. Maj + A > Mesh > Cube. Renommez : Encombrement.
2. Dimensions : 420mm, 180mm, 450mm. Location : X 120mm, Z 225mm.
3. Vues 1 et 3 : le croquis tient dedans. H pour le masquer.

7 · LES GRANDS VOLUMES
1. Outliner : clic droit sur Scene Collection > New Collection.
   Renommez-la Lampe, puis cliquez-la : elle reçoit les nouveaux objets.
2. Socle : Cylinder, F9 : Vertices 32, Radius 90mm, Depth 25mm. G Z = 12.5mm.
3. Bras_bas : Cylinder, F9 : Vertices 16, Radius 8mm, Depth 260mm.
   R Y 15.6, puis G sur le croquis (repère : -5, 0, 165 mm).
4. À vous :
   Interrupteur : Cylinder, Vertices 16, Radius 8mm, Depth 6mm.
     Location 55mm, 0, 28mm.
   Bras_haut : Cylinder, Vertices 16, Radius 7mm, Depth 220mm.
     R Y 50.5 (repère : 115, 0, 360 mm).
5. / (pavé numérique) : vérifiez une pièce seule, puis / pour revenir.
Contrôle : vue de face (1), les volumes suivent le croquis.

8 · LA TÊTE (orientation Local)
1. Cone, F9 : Vertices 24, Radius 1 60mm, Radius 2 22mm, Depth 110mm. R Y -30.
2. Vue de face : G près du haut de Bras_haut.
3. G Z Z : avancez-la dans son axe jusqu'au bras (repère : 233.5, 0, 372 mm).

9 · LES ARTICULATIONS (aimantation) ET LA MESURE
1. Menu de l'aimant : Snap Base Center ; Snap Target Face Center.
2. UV Sphere, F9 : Segments 16, Ring Count 8, Radius 15mm.
   G, puis Ctrl au-dessus du bout bas de Bras_bas. Renommez : Articulation_bas.
3. Articulation_milieu (Radius 14mm) : bout haut de Bras_bas.
4. À vous : Articulation_haut (Radius 12mm) : bout haut de Bras_haut.
5. À vous : vue de dessus (7), Snap Target Face, Snap Base Closest.
   Interrupteur : G, puis Ctrl au-dessus du socle : il se pose dessus.
6. Outil Measure, Ctrl : socle 180 mm ; hauteur totale environ 442 mm.
Contrôle : les articulations coiffent les bouts des bras.

10 · BISEAU ET EXTRUSIONS (pièce d'essai, supprimée à la fin)
1. Socle : Maj + D, X, = -400mm, Entrée. / puis Tab.
2. Mode arête (2), Alt + clic sur l'arête du haut, Ctrl + B, clic.
   F9 : Width 4mm ; Segments 1, puis 4 ; Profile 0.5.
3. À vous : un congé de 2mm sur l'arête du bas (Width dans F9).
4. Mode face (3), 4 faces du flanc arrière :
   Alt + E > Extrude Manifold, = -5mm, Entrée.
5. À vous : Alt + clic sur une arête verticale du flanc,
   Alt + E > Extrude Faces Along Normals, = 2mm, Entrée.
6. Tab, /, puis X : supprimez la pièce d'essai.

11 · LA VARIANTE B ET LA SILHOUETTE
1. Clic droit sur Lampe > Duplicate Collection. Renommez : Lampe_B.
2. Clic droit sur Lampe_B > Select Objects. G X = 550mm.
3. Bras_haut.001 : Dimensions Z 300mm, puis G Z Z = 40mm. Ctrl + A > Scale.
4. Snap Target Face Center, Snap Base Center.
   Articulation_haut.001 : G + Ctrl sur le nouveau bout. Tête.001 : G, puis G Z Z.
5. Viewport Shading : Lighting Flat ; Color Custom, noir ;
   Background Custom, clair. Vues 1, 3 et 7.

12 · ATELIER
1. Duplicate Collection de Lampe : Lampe_C. Select Objects, G X = 1100mm.
2. Une autre piste. Exemple : supprimez Tête.002, puis Cylinder,
   Vertices 24, Radius 50mm, Depth 120mm, R Y -30, G et G Z Z.
3. Comparez les trois silhouettes (vues 1, 3, 7 ou Quad View).
4. Mesurez la piste retenue (Measure).
5. Laissez-la visible, masquez les deux autres. Ctrl + S.
★ Renommez les pièces sans .001 ; copiez l'Encombrement (Alt + H, Maj + D, X = 550mm)
  pour voir si la variante B le dépasse ; une quatrième piste.
★★ Voir les défis du chapitre dans l'application.
```

## Le fil rouge : ce que l'apprenant a en main

**Au début de la demi-journée :** les gestes de l'initiation, et le souvenir de la lampe, vue au défi des vues et à la passerelle de fin d'initiation. Aucun fichier n'est attendu : `PRC02_ch1_blocage_lampe.blend` est le point de départ propre.

**À la fin, le fichier `lampe_blocage_v001.blend`,** moteur EEVEE. Il affiche des millimètres, réglage du fichier livré, sauf si l'apprenant a choisi les mètres :

| Collection | État | Contenu |
|---|---|---|
| *Lampe* | Visible si c'est la piste retenue | *Socle*, *Interrupteur*, *Bras_bas*, *Bras_haut*, *Articulation_bas*, *_milieu*, *_haut*, *Tête* |
| *Lampe_B* | Masquée, sauf si retenue | La même lampe, bras supérieur allongé, décalée de 550 mm en X ; pièces en `.001` |
| *Lampe_C* | Masquée, sauf si retenue | La piste de l'atelier, décalée de 1100 mm en X ; pièces en `.002` |
| *Croquis* | Visible | *Croquis_face* et *Croquis_profil*, tels que livrés |
| *Variante A*, *B*, *C* | Masquées | Le corrigé, tel que livré |
| *Scene Collection* | | *Encombrement*, masqué avec `H` |

**Ce que le chapitre 2 en attend :** le plan du chapitre 2 part de son propre fichier, `PRC02_ch2_lampe_depart.blend`, dont le gabarit est la *Variante A*. Il cite `lampe_blocage_v001.blend` comme le blocage de l'apprenant. Il suppose acquis la saisie d'une valeur avec son unité, l'aimantation (cible *Face*), l'orientation *Local* et `G Z Z`, la mesure et l'onglet *Object Data* d'une image de référence. Tout cela est pratiqué ici et ne saute jamais.

## Les fichiers

### Tableau des exercices et des corrigés

| Exercice ou atelier | Moment | Fichier de travail | Où se trouve le corrigé |
|---|---|---|---|
| Les cotes et leur unité | 0:10 | La scène d'usine, non enregistrée | Les valeurs du point de contrôle, dans `N > Item` |
| Prise en main du fichier | 0:25 | `PRC02_ch1_blocage_lampe.blend`, enregistré aussitôt sous `lampe_blocage_v001.blend` | Sans objet : pas de production. Contrôle : nom du fichier, moteur EEVEE |
| Lire la forme | 0:30 | `lampe_blocage_v001.blend` | Les réglages d'ouverture du fichier livré : *Random*, *Clip Start* 1 mm |
| Images de référence | 0:45 | `lampe_blocage_v001.blend` | L'objet *Croquis_profil* du fichier, masqué pendant l'exercice |
| *Quick Favorites*, navigation et saisie | 0:57 | Les préférences du poste | Sans objet : options |
| L'encombrement | 1:15 | `lampe_blocage_v001.blend` | Les valeurs du plan ; la *Variante A* tient dedans |
| Les grands volumes | 1:27 | `lampe_blocage_v001.blend` | Collection masquée *Variante A* : *Socle_A*, *Interrupteur_A*, *Bras_bas_A*, *Bras_haut_A* |
| La tête | 1:52 | `lampe_blocage_v001.blend` | Collection masquée *Variante A* : *Tête_A* |
| Les articulations, la pose sur une surface et la mesure | 2:07 | `lampe_blocage_v001.blend` | Collection masquée *Variante A* : les trois articulations, *Interrupteur_A* ; les cotes du plan |
| Biseau et extrusions | 2:45 | `lampe_blocage_v001.blend`, sur une pièce d'essai supprimée ensuite | Le panneau F9 et la figure 1.21 de l'application |
| La variante B et la silhouette | 3:00 | `lampe_blocage_v001.blend` | Collection masquée *Variante B* |
| Atelier : trois pistes | 3:15 | `lampe_blocage_v001.blend` | Collections masquées *Variante A*, *B* et *C* |
| Défis ★★ | 3:15, pour ceux qui avancent vite | `lampe_blocage_v001.blend` | Pas de corrigé dans le fichier : le formateur valide à l'écran |

### Le fichier livré, tel qu'il est

`PRC02_ch1_blocage_lampe.blend` (225 978 octets) est livré et ne sera pas modifié par ce plan. Le plan s'appuie sur lui tel qu'il est, lu en arrière-plan dans Blender 5.2.1 :

- **Collections :** *Variante A*, *B*, *C*, masquées dans la vue (œil fermé), et *Croquis*, visible. *Scene Collection* est la collection active, et aucun objet n'est sélectionné.
- **Variante A**, à l'origine : *Socle_A* (cylindre de 32 côtés, Ø 180 × 25 mm), *Interrupteur_A* (Ø 16 × 6 mm), *Bras_bas_A* (Ø 16 × 259,6 mm, Y 15,64°), *Bras_haut_A* (Ø 14 × 220,2 mm, Y 50,53°), trois articulations en sphères UV (Ø 30, 28 et 24 mm), *Tête_A* (tronc de cône de 24 côtés, Ø 120 à 44 mm, 110 mm de long, Y -30°). Échelles à 1, aucun modificateur.
- **Variante B**, à 550 mm en X : le bras supérieur passe à 300 mm et à 53,13°, l'articulation du haut et la tête montent.
- **Variante C**, à 1100 mm en X : la tête devient un cylindre de 24 côtés, Ø 100 × 120 mm.
- **Croquis :** *Croquis_face* (position 111, 200, 222 mm) et *Croquis_profil* (-300, 0, 222 mm), images empaquetées, *Size* 560 mm, *Opacity* 0,5, *Depth* *Back*, affichées seulement en vue orthographique alignée.
- **Scène :** affichage en millimètres, *Unit Scale* 1,0 ; **moteur Cycles** ; aimantation éteinte, cible *Vertex*, base *Closest* ; orientation *Global*.
- **Vue d'ouverture** (*Layout*) : vue de face orthographique, centrée sur le croquis ; *Solid*, *Color* *Random*, *Outline* ; *Clip Start* 1 mm. L'éditeur de propriétés est sur l'onglet *Scene*.
- **Aucun texte LISEZ-MOI.** Seul un texte caché, `.Geo-Scatter: Per BlendFile Properties`, laissé par une extension du formateur : sans effet, invisible pour les apprenants.

Ce que cela change pour la séance :
- **Le corrigé** porte le nom *Variante A*, *B*, *C*, et non « Corrigé… ». Le découpage l'accepte pour les fichiers déjà livrés. Le paperboard et les consignes le disent, à la place du LISEZ-MOI.
- **Le moteur :** la correction du fichier en EEVEE est prévue en fin de projet. D'ici là, la vérification de 0:25 est nécessaire ; ensuite, elle devient un simple contrôle.
- **Les unités :** l'affichage en millimètres est un réglage du fichier, pas une exigence envers l'apprenant. La séquence des cotes se fait dans la scène d'usine, en mètres, et les consignes donnent toujours l'unité.
- ***Clip Start*** est déjà réglé : la séquence remet d'abord la valeur d'usine pour montrer le problème.
- **Les croquis sont déjà placés.** L'exercice de 0:45 fait replacer celui de profil, et celui du fichier sert de corrigé. La nouvelle formulation de l'encart *CAUTION* le dira (partie « Ajustements retenus du contenu »).

### Les croquis

`croquis_lampe_face.png` et `croquis_lampe_profil.png` (dans `_resources/exercices/`) sont les images déjà empaquetées dans le fichier. L'exercice de 0:45 en a besoin. Ils seront téléchargeables depuis l'application à la prochaine mise à jour du contenu, faite par la session principale. D'ici là, le formateur les distribue lui-même avec le fichier.

### Pas de nouveau fichier

Aucun fichier ne manque vraiment :
- le parcours principal tient entièrement dans le fichier livré, dont les trois variantes font office de corrigé ;
- le point de départ propre exigé par le critère 4 est le fichier livré lui-même : la demi-journée précédente, l'initiation, ne produit rien dont ce chapitre dépende ;
- le chapitre 2 a déjà son propre fichier de départ.

**La séquence « Biseau et extrusions »** n'a pas de corrigé dans le fichier livré. Le formateur a décidé de ne pas lui créer de fichier : le résultat se lit dans le panneau F9 (*Width*, *Segments*, *Profile*), la figure 1.21 de l'application le montre, et la pièce d'essai est supprimée à la fin. L'option `PRC02_ch1_piece_essai.blend`, proposée dans la première version de ce plan, **n'est pas retenue**.

## Si vous prenez du retard

Raccourcissez dans cet ordre :

| Ordre | Ce que l'on coupe | Ce que l'on garde |
|---|---|---|
| D'abord | *À votre main* : démo de 2 minutes, sans essai ; les apprenants y reviennent avec l'application. L'option *Length* se montre sans essai | La mention des options |
| Ensuite | Images de référence : réglages sur *Croquis_face* seulement, sans replacer le croquis de profil | L'onglet *Object Data* d'une image, dont le chapitre 2 se sert |
| Ensuite | L'encombrement : vous le montrez, les apprenants ne le font pas | *Dimensions* et `H`, repris à la variante B |
| Ensuite | Les extrusions : démo seule ; le biseau reste en guidé | Le biseau mesuré, point du programme |
| En dernier | L'atelier : deux pistes au lieu de trois (A et B), comparées en silhouette | Le choix de la piste et l'enregistrement |

**Ce qui ne saute jamais :** la saisie d'une valeur avec son unité, dans un champ et pendant un geste ; la vérification du moteur EEVEE et l'enregistrement sous `lampe_blocage_v001.blend` ; le menu *Viewport Shading* ; *Clip Start* ; la vue locale ; l'orientation *Local* et `G Z Z` ; l'aimantation, avec la pose sur une surface (*Face*) ; la mesure ; *Duplicate Collection*. Les chapitres 2 à 4 s'en servent.

**Un apprenant très en retard** ouvre l'œil de *Variante A*, fait *Duplicate Collection*, renomme la copie *Lampe*, puis referme l'œil de *Variante A*. Il reprend avec le groupe à la séquence suivante, et le corrigé reste intact.

## Pour ceux qui avancent vite

- Les paliers ★ de l'atelier, dans les consignes.
- **Un socle bombé (★★) :** sur une variante, `I` trois fois sur le dessus du socle, puis la face centrale, `O` et `G Z = 8mm` : l'édition proportionnelle galbe le dessus. La molette règle l'influence, `Maj + O` le profil.
- **Une coupe qui glisse (★★) :** `G G` sur un anneau du socle bombé ; `Alt + S` sur les faces de la tête pour la gonfler.
- **Un socle carré aux coins arrondis (★★) :** un cube à 180 × 180 × 25 mm, l'échelle appliquée, puis `Ctrl + Maj + B` sur les sommets du dessus.
- **Caler un croquis à l'œil (★★) :** replacer le croquis de profil sans les valeurs, en ajustant *Size* jusqu'à ce que le socle dessiné mesure 180 mm, contrôlé avec l'outil *Measure*.
- **Plusieurs cibles d'aimantation (★) :** *Vertex* et *Face Center* ensemble (`Maj + clic`), et `B` pendant le geste.
- **Un objet de votre secteur (★★) :** la même méthode en quatre temps sur un rétroviseur, une liseuse de cabine ou une poignée de maintien de tram. Pas de corrigé : vous le validez à l'écran.
- Le rôle de copilote, comme à l'initiation.

## Gérer l'hétérogénéité

- Les binômes et les copilotes de l'initiation restent en place.
- Les consignes donnent chaque geste au millimètre près, unité comprise. Les valeurs restent indicatives : chacun peut les adapter à son concept.
- Chacun garde l'unité d'affichage qu'il préfère : les consignes marchent avec les deux.
- Le socle de chaque séquence suffit : il couvre tous les points du programme.
- À chaque point de contrôle, passez d'abord par les postes des débutants, avec les post-it vert et rose.
- La règle du jour est au paperboard dès 0:10 : « Tapez l'unité ; pendant un geste, `=` d'abord. »
- Les termes de l'interface restent en anglais : traduisez-les à l'oral la première fois.

## Coordination avec les chapitres 2 à 4

**Contrôle des critères du découpage :**

| Critère | Où le plan y répond |
|---|---|
| 1. Durée | 3 h 30 de contenu, 3 h 50 avec les pauses, 10 minutes de marge |
| 2. Périmètre | Les trois ancres `ch1_sec1_title` à `ch1_sec3_title`. Ni *Append* ni *Link* ; ni matière, ni éclairage, ni caméra. EEVEE est seulement vérifié dans l'onglet *Render*, sans réglage |
| 3. Pas de redite | Tableau « Ce que le chapitre approfondit ». *Extrude* et *Bevel* sont repris au millimètre et dans leurs variantes, pas réexpliqués |
| 4. Continuité | Départ : la lampe vue à l'initiation, et le fichier livré, qui ne demande rien. Fin : `lampe_blocage_v001.blend`, le nom prévu par les chapitres 2 à 4 |
| 5. Fichiers et ateliers | Tableau des exercices et des corrigés. Un seul fichier, livré et non modifié, dont les variantes masquées font office de corrigé. Consignes par paliers, avec des défis. La pièce d'essai n'a pas de fichier corrigé, par décision du formateur |
| 6. Chapitre 4 | Sans objet |
| 7. Progression | Tableaux des prérequis et des nouveautés ; une notion par cycle ; chaque notion démontrée, guidée puis réinvestie seule ; un atelier sans notion nouvelle ; quatre quiz en fin de séquence ; une ouverture qui rappelle le parcours |

**Ce que les chapitres suivants attendent, et où le plan le garantit :**

| Attendu | Chapitre | Moment |
|---|---|---|
| La saisie d'une valeur avec son unité | 2 | 0:10, puis toute la séance |
| L'onglet *Object Data* d'une image de référence | 2 | 0:45 |
| `N > Item`, le curseur 3D à l'origine | 2 | 1:15 et 1:27 |
| L'aimantation, dont la cible *Face* | 2 | 2:07 (*Face Center* en guidé, *Face* en autonomie) |
| L'orientation *Local* et `G Z Z` | 2 | 1:52, 3:00, atelier |
| La vue locale ; le menu *Viewport Shading* | 3 | 1:27 et 2:45 ; 0:30 et 3:00 |
| *Duplicate Collection* et les variantes | 3 | 3:00 et atelier |
| *Clip Start* de la vue ; la barre latérale `N` | 4 | 0:30 |
| Le fichier `lampe_blocage_v001.blend` | 2 | 0:25 (*Save As*), fin de l'atelier (dernier `Ctrl + S`), contrôle à 3:49 |
| Le moteur EEVEE | 3 et 4 | 0:25 |

**À signaler aux plans voisins (non modifiés ici) :**
- **Chapitre 2, les valeurs tapées pendant un geste.** Son LISEZ-MOI tape des nombres seuls pendant les gestes (`G Y 10`, `G X 76`, `G Z 25`, `G Z Z 45`). Ils sont justes dans son fichier, qui affiche des millimètres. Un apprenant qui repasse en mètres déplacerait de 10 m. Pour suivre le bémol du formateur, ces valeurs peuvent s'écrire `G Y = 10mm`. Les valeurs tapées dans les champs (`1.5mm`, `3mm`) sont justes dans tous les cas.
- **Chapitre 2, le point « encore à tester »** sur l'unité d'une valeur tapée pendant un geste : il est tranché (partie « Points vérifiés »).

## Ajustements retenus du contenu du chapitre 1

Le contenu validé n'a pas été modifié par ce plan. Le formateur a retenu ces retouches ; la session principale les applique.

1. **Un encart *TIP* sur la saisie des unités,** au § 1, après la phrase sur `35mm`. Le test dans Blender 5.2.1 a montré que, pendant un geste, l'unité n'est comprise qu'après `=`. Formulation proposée :
   > Dans un champ, l'unité tapée est toujours comprise. Pendant un geste, un nombre seul s'entend dans l'unité affichée : `G Z 25` monte de 25 m dans une scène en mètres, de 25 mm dans une scène en millimètres. Pour taper une unité pendant le geste, appuyez d'abord sur `=` : `G Z = 25mm` monte de 25 mm dans les deux cas. Sans `=`, l'unité est ignorée.
2. **Le défi fil rouge (encart *CAUTION*).** Nouvelle formulation pour la phrase sur les croquis : « Les croquis sont déjà en place dans le fichier d'exercice : masquez celui de profil et replacez-le vous-même pour vous entraîner. »
3. **Le quiz de la section 1,** révisé dans l'esprit du bémol. Proposition :
   - question : « Votre scène affiche des mètres. Pendant le déplacement, que tapez-vous pour monter une pièce de 25 mm ? » ;
   - options : `G Z 25mm` ; `G Z = 25mm` ; `G Z 0.025` ; `G Z 25` ;
   - bonnes réponses : la deuxième et la troisième ;
   - explication : « Pendant un geste, Blender ne lit l'unité qu'en saisie avancée, ouverte par `=` : `G Z = 25mm`. Sans `=`, les lettres sont ignorées, et `G Z 25mm` monte de 25 m, comme `G Z 25`. `G Z 0.025` marche aussi : un nombre seul s'entend dans l'unité affichée, ici le mètre. Dans un champ, en revanche, `25mm` est toujours compris. »
4. **Non retenu :** la phrase sur Cycles dans la description du module ressource. Le moteur du fichier livré sera corrigé en EEVEE lors des corrections de fin de projet.

## Points vérifiés dans Blender 5.2.1

- **La saisie pendant un geste** (test par simulation de touches, dans une fenêtre Blender séparée) :

  | Affichage | Saisie | Résultat |
  |---|---|---|
  | Mètres | `G Z 25` | 25 m |
  | Mètres | `G Z 25mm` | 25 m : les lettres sont ignorées |
  | Mètres | `G Z = 25mm`, ou `*` du pavé numérique à la place de `=` | 25 mm |
  | Mètres | `G Z 0.025` | 25 mm |
  | Millimètres | `G Z 25` | 25 mm |
  | Millimètres | `G Z 1` | 1 mm |
  | Millimètres | `G Z = 1m` | 1 m |
  | Mètres, option *Default to Advanced Numeric Input* cochée | `G Z 25mm` | 25 mm |

  Le manuel de Blender le confirme : les unités et les expressions demandent la saisie avancée (`=` ou `*` du pavé numérique). Dans un champ, l'unité est toujours comprise. Le test de `=` a été fait avec la touche simulée ; sur un clavier français, vérifiez-le une fois sur un poste de la salle.
- **`R Y 15.6`** donne +15,6° dans le champ *Rotation* Y : le sens attendu pour le bras du bas.
- ***Add > Image > Reference*** en vue de droite : l'image arrive face à la vue (rotation 90°, 0°, 90°), au curseur 3D, avec *Size* 5 m, *Depth* *Default*, visible en perspective, sans opacité. D'où les réglages de l'exercice de 0:45.
- **La pose sur une surface :** en vue de dessus, *Snap Target* *Face* et *Snap Base* *Closest*, l'interrupteur déplacé au-dessus du socle se pose dessus (centre à 28 mm). Avec *Snap Base* *Center*, son centre se pose sur la face (25 mm) : il s'enfonce à moitié.
- **Le menu d'aimantation :** *Snap Target* propose *Increment*, *Grid*, *Vertex*, *Edge*, *Face*, *Volume*, *Edge Center*, *Edge Perpendicular*, *Face Center*, puis *Face Project* et *Face Nearest* pour les éléments individuels ; *Snap Base* propose *Closest*, *Center*, *Median*, *Active*.
- **Les libellés du réglage silhouette :** *Color* et *Background* proposent bien *Custom* dans Blender 5.2.
- ***Extrude Manifold*** sur 4 faces du flanc d'un cylindre de Ø 180 × 25 mm, enfoncées de 5 mm : le volume reste fermé (aucune arête non manifold).
- **Les cotes des consignes** reproduisent la variante A, arrondies au millimètre : les bouts des bras tombent, à quelques dixièmes de millimètre près, sur les centres des articulations du corrigé (vérifié par calcul à partir des valeurs lues dans le fichier).

## Décisions du formateur (18 novembre 2026)

1. **Le plan est validé,** avec les recommandations de la relecture.
2. **L'ordre de la séance :** les variantes et la silhouette passent après la section 3. Validé.
3. **Les millimètres sont une recommandation, pas un prérequis.** L'essentiel est de saisir une valeur avec son unité, quel que soit l'affichage. Régler *Length* sur *Millimeters* est une option recommandée pour le design produit ; le formateur garde le plus souvent les mètres. Les consignes, les points de contrôle et le paperboard donnent toujours l'unité. Le fichier livré reste en millimètres : c'est un réglage du fichier.
4. **Les unités se règlent dans la scène d'usine,** comme une option.
5. **Le replacement du croquis de profil est validé.** Les deux PNG seront téléchargeables depuis l'application à la prochaine mise à jour du contenu, par la session principale ; d'ici là, le formateur les distribue.
6. **La pièce d'essai n'a pas de fichier corrigé.** L'option `PRC02_ch1_piece_essai.blend` n'est pas retenue.
7. **La pose avec la cible *Face* est ajoutée** à l'autonomie de 2:07, pendant une minute environ : l'interrupteur posé sur le dessus du socle.
8. **Les ajustements du contenu :** l'encart sur la saisie des unités, formulé pour les deux affichages, et la nouvelle formulation de l'encart sur les croquis sont retenus ; le quiz de la section 1 est révisé ; la phrase sur Cycles ne l'est pas. Le fichier livré sera corrigé en EEVEE en fin de projet ; d'ici là, la séquence de 0:25 vérifie le moteur.

**Un point qui précise le bémol, établi après la décision :** pendant un geste, `G Z 25mm` ne suffit pas. Sans `=`, Blender ignore l'unité et monte de 25 m dans une scène en mètres. Le plan écrit donc `G Z = 25mm` partout, et présente l'option *Default to Advanced Numeric Input* à 0:57 pour qui veut se passer du `=`.
