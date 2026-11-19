# Chapitre 1 · Environnement et blocage de volumes : déroulé formateur

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 3 sur 6, en présentiel, de 5 à 8 apprenants · Version du 19 novembre 2026, application support 1.0.0

## En bref

- **Objectif :** à la fin de la demi-journée, chaque apprenant saisit une cote avec son unité, cale un volume sur un croquis et bloque sa lampe avec des primitives, à ses cotes. Il incline et avance une pièce dans son propre axe, pose une pièce sur une autre par aimantation et contrôle une cote. Il biseaute et extrude au millimètre, puis compare trois pistes par leur silhouette.
- **Format :** 3 h 50, dont 3 h 30 de contenu et 2 pauses de 10 minutes. Il reste 10 minutes de marge sur 4 heures. Exemple : de 9 h 00 à 12 h 50. Les pauses tombent aux mêmes heures qu'à l'initiation.
- **Principe :** le même qu'à l'initiation. Une notion à la fois : vous la montrez en quelques minutes, ils la pratiquent en guidé, puis seuls. Personne ne passe plus de 15 minutes sans toucher la souris.
- **La règle du jour : tapez l'unité.** Dans un champ, `25mm` est toujours compris. Pendant un geste, on tape d'abord `=` : `G Z = 25mm`. Ces deux gestes marchent, que la scène affiche des mètres ou des millimètres. L'affichage en millimètres reste une option, recommandée pour le design produit.
- **Fil rouge :** la lampe de bureau, déjà vue à l'initiation. Chacun en bloque sa version sur les croquis, puis deux variantes. Le fichier de fin, `lampe_blocage_v001.blend`, est celui que cite le chapitre 2.

### L'ordre de la séance

La séance suit l'ordre de l'application, sauf pour la fin de la section 2 : *Comparer des variantes* et *Juger la silhouette* passent après la section 3. C'est l'ordre de la méthode en quatre temps que le chapitre enseigne : l'encombrement, les grands volumes, les proportions, puis la comparaison. Les outils de la section 3 servent à ajuster les proportions ; les variantes arrivent quand la lampe est complète, juste avant l'atelier. Le quiz de la section 2 se fait donc après ceux de la section 3.

### Ce que l'on survole

Ces notions sont dans l'application. Elles ne sont pas exigées en séance, et certaines servent de défi.
- *Unit Scale* : une phrase, celle de l'encart *WARNING*.
- *Save Startup File* et *Load Factory Settings* : le sous-menu est montré, sans clic. Sur les postes partagés de la salle, on n'enregistre pas de fichier de démarrage.
- Les orientations *Normal*, *View*, *Cursor*, *Gimbal* et *Parent* : citées.
- Plusieurs cibles d'aimantation (`Maj + clic`) et la touche `B` pendant le geste : une astuce, puis un défi.
- L'édition proportionnelle (`O`), `G G` et `Alt + S` : une minute de démonstration, puis des défis.
- Le biseau d'un sommet (`Ctrl + Maj + B`) et *Extrude Individual Faces* : cités.
- *Background*, l'image toujours derrière : citée à côté de *Reference*.

### Les fichiers

| Fichier | Moment | Contenu |
|---|---|---|
| `PRC02_ch1_blocage_lampe.blend` | 0:25, puis toute la séance | Les croquis de face et de profil, déjà placés ; trois blocages terminés, masqués, dans les collections *Variante A*, *B* et *C* : c'est le corrigé |
| `PRC02_ch1_croquis_lampe.zip` | 0:45 | Les deux croquis en PNG, pour replacer celui de profil |
| Les consignes par paliers | Toute la séance | En annexe de ce document, à projeter ou à imprimer |

L'application propose le fichier en section 2, après « Une méthode en quatre temps », et l'archive des croquis en section 1, sous les réglages de l'image de référence.

> **À savoir :** le fichier livré n'a pas de texte LISEZ-MOI : les consignes de l'annexe en tiennent lieu. Son corrigé s'appelle *Variante A*, *B* et *C*, et non « Corrigé ». Il est encore réglé sur le moteur Cycles : chacun vérifie le moteur à 0:25. Ce réglage sera corrigé en fin de projet.

## Avant la demi-journée

### Les postes des apprenants

- [ ] L'application support 1.0.0 est installée. Une version plus ancienne propose la mise à jour à son démarrage.
- [ ] Le dossier de travail contient `PRC02_ch1_blocage_lampe.blend` et les deux croquis décompressés, `croquis_lampe_face.png` et `croquis_lampe_profil.png`. À défaut, chacun les télécharge depuis l'application à 0:25.
- [ ] Blender 5.2 LTS s'ouvre, avec une souris à trois boutons. *Emulate Numpad* reste activé sur les portables sans pavé numérique.
- [ ] Sur un poste de la salle, `G Z`, `=`, `25mm`, Entrée monte bien un objet de 25 mm. Le geste a été vérifié dans Blender par simulation de touches, pas encore sur un clavier français.
- [ ] Les *Quick Favorites* et les options essayées à 0:57 s'enregistrent dans les préférences du poste. C'est voulu : ce sont leurs options. Prévenez seulement le gestionnaire des postes si la salle est partagée.

### Votre poste de démonstration

- **Lancez Blender en configuration d'usine** (`blender.exe --factory-startup`), comme à l'initiation : votre écran correspond à celui des apprenants, et vos préférences ne sont pas touchées. En contrepartie, votre Blender ne garde pas les options de 0:57 : pendant vos démos, tapez toujours `=` avant une unité.
- **Agrandissez l'interface** pour le vidéoprojecteur : *Resolution Scale* à 1,3.
- **Préparez une copie de travail du fichier,** enregistrée sous un autre nom, pour vos démonstrations : le fichier livré reste intact.
- **Ne cliquez pas sur *Save Startup File*** pendant la démo de 0:57 : montrez le sous-menu sans l'exécuter.
- **Gardez l'application ouverte** sur le chapitre 1, pour projeter les quiz.

### Le matériel de la salle

- Les post-it vert et rose des points de contrôle, et le minuteur.
- Le paperboard, préparé avant l'arrivée des apprenants :
  - la règle du jour : « Tapez l'unité. Dans un champ : `25mm`. Pendant un geste : `=`, puis `25mm`. » ;
  - le corrigé : « collections *Variante A*, *B* et *C*, œil fermé : on compare, on ne copie pas » ;
  - le fichier de fin : `lampe_blocage_v001.blend`, moteur EEVEE ;
  - les raccourcis du jour, complétés au fil de la séance : `N`, `Ctrl + Alt + Q`, `Q`, `H` et `Alt + H`, `/`, `,`, `G Z Z`, `Ctrl` pendant un geste, `Maj + Tab`, `Ctrl + B`, `Alt + E`.
- Les consignes de l'annexe, projetées ou imprimées, une par apprenant.

## La demi-journée · Du réglage au blocage

Les trois sections du chapitre 1. Les apprenants repartent avec leur lampe bloquée, en trois pistes, dans `lampe_blocage_v001.blend`. Dans la colonne « Modalité », les durées sont en minutes.

| Horaire | Durée | Séquence | Section | Modalité |
|---|---|---|---|---|
| 0:00 | 10 min | Ouverture : où l'on en est | | Collectif 7 + poste 3 |
| 0:10 | 15 min | Les cotes et leur unité | 1 | Démo 5 + guidé 8 + quiz 2 |
| 0:25 | 5 min | Le fichier du fil rouge | 1 | Guidé |
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
| 3:15 | 25 min | Atelier · Trois pistes pour une revue de concept | | Lancement 2 + autonomie 20 + revue 3 |
| 3:40 | 10 min | Galerie, bilan et passerelle vers le chapitre 2 | | Collectif |

### 0:00 · Ouverture : où l'on en est (10 min)

- **Le parcours de la lampe (collectif, 7 min) :** « L'initiation vous a donné les gestes de base. Aujourd'hui commence la formation proprement dite. » La lampe est bloquée aujourd'hui, modélisée au chapitre 2, habillée au chapitre 3, mise en scène et exportée au chapitre 4.
- **Montrez le but :** sur votre copie du fichier, ouvrez l'œil des trois variantes et passez-les en ombres chinoises, avec le réglage de 3:00. « À la fin de la demi-journée, vous aurez votre lampe, en trois pistes comme celles-ci, et vous en défendrez une. »
- **Le mot du jour :** le blocage, ou *greyboxing*, c'est la maquette en mousse du designer. On juge les proportions avant le détail.
- **La règle :** les réglages de la première heure sont des options ; chacun garde ce qui l'aide. Une seule habitude compte : taper l'unité.
- **Sur poste (3 min) :** chacun lance Blender et ferme l'écran d'accueil. La scène d'usine et son cube servent à la première séquence.

**Point de contrôle :** sur chaque écran, la scène d'usine.

### 0:10 · Les cotes et leur unité (15 min)

**Vous montrez (5 min),** d'après § 1 « Choisir l'unité d'affichage » (figure 1.1), dans la scène d'usine, qui affiche des mètres :
1. Le cube sélectionné, `N`, onglet *Item* : *Dimensions* 2 m.
2. **Dans un champ, l'unité est toujours comprise.** Dans *Dimensions* X, tapez `180mm` : le champ affiche 0,18 m. Puis `3.5cm`, puis `1m 20mm`.
3. **Pendant un geste, c'est différent.** `G Z 25` : le cube monte de 25 m. « Un nombre seul s'entend dans l'unité affichée. » `Ctrl + Z`. Faites deviner : « Et `G Z 25mm` ? » Essayez : 25 m encore, les lettres sont ignorées. `Ctrl + Z`. Puis `G Z`, `=`, `25mm`, Entrée : 25 mm. « La touche `=` ouvre la saisie avancée, qui comprend les unités. Le `*` du pavé numérique fait de même. »
4. **Une option, recommandée pour le design produit :** onglet *Scene*, rubrique *Units*, *Length* sur *Millimeters*. Le cube affiche 180 mm, et `G Z 25` monterait de 25 mm. *Unit Scale* reste à 1 : une phrase, celle de l'encart *WARNING*. « Les mètres se valent aussi, tant que vous tapez l'unité. »
5. **Ailleurs :** une planche de bord ou un phare se cote en millimètres, l'implantation d'un tram en mètres. Chacun garde l'affichage de son métier.

**Ils font, en guidé (8 min),** dans la scène d'usine :
1. Le cube devient une galette de socle : *Dimensions* `180mm`, `180mm`, `25mm`.
2. `G Z`, `=`, `12.5mm`, Entrée : elle repose sur le sol.
3. `Ctrl + A > Scale` : l'échelle revient à 1, les cotes restent.
4. En option, *Length* sur *Millimeters*.

**Quiz (2 min),** ensemble à l'écran : le quiz de la section 1, sur la saisie de 25 mm pendant un déplacement. Chacun répond pour soi, puis on commente les erreurs.

**Point de contrôle :** dans `N > Item`, *Dimensions* 180 × 180 × 25 mm (0,18 × 0,18 × 0,025 m), *Location* Z 12,5 mm, *Scale* 1.

**Pièges fréquents :**
- La galette s'envole à 12,5 m : le `=` a été oublié, dans une scène en mètres. `Ctrl + Z`.
- `=` sans effet : le `*` du pavé numérique fait l'affaire. Sur un clavier français, `=` est la touche à gauche de la touche d'effacement.
- Un champ qui refuse la valeur : une virgule a été tapée au lieu d'un point (`3,5cm` au lieu de `3.5cm`).

### 0:25 · Le fichier du fil rouge (5 min)

**Ils font, pas à pas :**
1. *File > Open* : `PRC02_ch1_blocage_lampe.blend` ; *Don't Save* pour la scène d'usine. Ceux qui n'ont pas le fichier le téléchargent dans l'application, en section 2.
2. *File > Save As* : `lampe_blocage_v001.blend`, dans le dossier de travail. Le fichier livré reste intact.
3. Onglet *Render* : *Render Engine* doit indiquer **EEVEE** ; choisissez-le si besoin. « La formation travaille avec EEVEE. En mode *Solid*, rien ne change à l'écran ; le chapitre 4 en dira plus. » Le fichier livré est encore réglé sur Cycles : ce geste est nécessaire.
4. Onglet *Scene*, rubrique *Units* : ce fichier affiche des millimètres. C'est un réglage du fichier, pas une exigence : chacun peut repasser en mètres. Les consignes donnent toujours l'unité.
5. Le tour du fichier : la vue de face montre le croquis. Dans l'Outliner, la collection *Croquis*, puis *Variante A*, *B* et *C*, l'œil fermé : « Trois blocages terminés, votre corrigé. On les ouvre pour comparer, jamais pour copier. »
6. `Ctrl + S`.

**Point de contrôle :** la barre de titre affiche `lampe_blocage_v001.blend` ; *Render Engine* indique EEVEE.

### 0:30 · Lire la forme : affichage, *Clip Start*, Quad View (15 min)

D'après § 1 « Lire la forme dans la vue 3D », « Voir de près les petits objets » et « Voir sous tous les angles avec la Quad View » (figures 1.2, 1.3 et 1.6). Chacun ouvre l'œil de *Variante A*, qui sert de sujet.

**Le menu *Viewport Shading* (démo 2 min, guidé 3 min).** Vous montrez la flèche à droite des quatre modes d'affichage, puis *Lighting* (*Studio*, *MatCap*, *Flat*), *Color* (*Random*, déjà choisi dans ce fichier), *Cavity* et *Outline*. Ils font : *Cavity* activé, un essai de *MatCap*, puis retour à *Studio*. « Regardez la jonction entre le socle et le bras. »

***Clip Start* (démo 2 min, guidé 3 min).** En perspective (`5`), sélectionnez *Interrupteur_A*, cadrez-le (`.` du pavé numérique) et zoomez au plus près. Le fichier est réglé à 1 mm : tapez `10mm`, la valeur d'usine, dans `N`, onglet *View*, champ *Clip Start*. L'interrupteur se coupe. Revenez à `1mm`. Ils font le même essai.

**La Quad View (démo 1 min, guidé 2 min).** `Ctrl + Alt + Q` : trois vues orthographiques et une perspective. Ils l'ouvrent, déplacent un objet de la variante et le voient bouger dans les quatre vues, puis `Ctrl + Z` et de nouveau `Ctrl + Alt + Q` pour revenir.

**En autonomie (2 min) :** chacun choisit l'affichage qui l'aide le plus pour la suite, puis referme l'œil de *Variante A*.

**Point de contrôle :** *Clip Start* à 1 mm ; *Variante A* masquée ; une seule vue 3D.

**Pièges fréquents :**
- *Clip Start* sans effet visible : la vue est restée orthographique. Passez en perspective (`5`).
- Une Quad View qui ne se referme pas : la souris n'était pas au-dessus de la vue 3D.
- Un objet de la variante modifié : `Ctrl + Z`. Le corrigé doit rester juste.

### 0:45 · Images de référence (12 min)

**Vous montrez (4 min),** d'après § 1 « Travailler avec des images de référence » (figures 1.4 et 1.5) :
1. En vue de face (`1`), le croquis s'affiche ; en tournant la vue, il disparaît. Sélectionnez *Croquis_face* dans l'Outliner : c'est un *Empty*, un objet sans géométrie qui porte une image.
2. Onglet *Object Data* : *Opacity*, *Depth* (*Front*, *Back*), *Show In* (*Perspective*, *Only Axis Aligned*).
3. Comment on en place une : vue de droite (`3`), *Add > Image > Reference*, puis l'image. Elle arrive face à la vue, au curseur 3D, et mesure 5 m de large. *Background* la garde toujours derrière. On peut aussi la faire glisser depuis l'Explorateur Windows.
4. **Ailleurs :** les vues de face et de profil d'un nez de tram, d'un rétroviseur, d'une cabine d'avion d'affaires.

**Ils font, en guidé (3 min),** sur *Croquis_face* : *Opacity* à 0,2 puis 0,5 ; *Depth* sur *Front* puis *Back* ; *Perspective* coché puis décoché dans *Show In*.

**Ils font, en autonomie (5 min) : replacer le croquis de profil.** Ils masquent *Croquis_profil* (œil), puis :
- vue de droite (`3`), *Add > Image > Reference*, `croquis_lampe_profil.png` ;
- *Object Data* : *Size* `560mm`, *Opacity* 0,5, *Depth* *Back* ; *Show In* : *Perspective* décoché, *Only Axis Aligned* coché ;
- `N > Item`, *Location* : X `-300mm`, Z `222mm`.

Ils rouvrent l'œil de *Croquis_profil* pour comparer, puis suppriment le leur (`X`) : le blocage s'appuie sur celui du fichier.

**Point de contrôle :** les deux images se superposent exactement ; ensuite, il ne reste que *Croquis_profil*, visible.

**Pièges fréquents :**
- Une image immense : *Size* vaut encore 5 m.
- Une image couchée : elle a été ajoutée en vue de face ou en perspective. Supprimez-la et recommencez en vue de droite.
- Le croquis introuvable : l'archive n'a pas été décompressée (clic droit > *Extraire tout*). En dernier recours, les réglages seulement, sans replacement.

### 0:57 · À votre main : *Quick Favorites*, navigation, saisie (8 min)

Annoncez-le : « Tout ce qui suit est une option. »

**Vous montrez (4 min),** d'après § 1 « Garder ses outils à portée », « Ajuster la navigation » et « Enregistrer son fichier de démarrage » (figures 1.7 à 1.9) :
1. Menu *View > Area*, clic droit sur *Toggle Quad View*, *Add to Quick Favorites*. La touche `Q` ouvre le menu sous la souris.
2. *Edit > Preferences > Navigation* : *Orbit Around Selection*, *Zoom to Mouse Position* et la case *Depth* de la ligne *Auto*.
3. *Edit > Preferences > Input*, rubrique *Keyboard* : *Default to Advanced Numeric Input*. Cochée, elle rend le `=` inutile : `G Z 25mm` marche directement.
4. *File > Defaults* : *Save Startup File* et *Load Factory Settings*, montrés sans cliquer. « Chez vous, ou pour une équipe, un fichier de démarrage commun garde la même unité pour tous. »

**Ils font :** en guidé (2 min), *Toggle Quad View* dans les *Quick Favorites*, puis `Q` ; en autonomie (2 min), une option de navigation ou de saisie à essayer, à garder ou non.

**Point de contrôle :** `Q` ouvre un menu qui contient au moins une entrée.

**À savoir :** un apprenant qui a cliqué *Save Startup File* n'a rien cassé sur son poste. Prévenez seulement le gestionnaire des postes.

### 1:05 · Pause (10 min)

### 1:15 · La méthode et l'encombrement (12 min)

**Vous montrez (4 min),** d'après § 2 « Une méthode en quatre temps » et « Donner les bonnes dimensions » (figure 1.12) :
1. Au paperboard, la méthode en quatre temps : l'encombrement, les grands volumes, les proportions, la silhouette. « Se tromper vite coûte peu. »
2. `Maj + A > Mesh > Cube` : 2 m de côté. Dans `N > Item`, *Dimensions* : `420mm`, `180mm`, `450mm`. Les champs *Scale* changent en conséquence : cette échelle se remet à 1 avec `Ctrl + A > Scale` avant certaines opérations, comme le biseau de 2:45.
3. *Location* : X `120mm`, Z `225mm`. Renommez le cube *Encombrement*.
4. Vues de face et de droite : le croquis tient dans le cube. `H` le masque, `Alt + H` le réaffiche.
5. **Ailleurs :** l'enveloppe d'un siège d'avion, d'un rétroviseur, d'un pupitre de conduite.

**Ils font, en guidé (8 min) :** les étapes 2 à 4.

**Point de contrôle :** en vues `1` et `3`, le croquis tient dans l'encombrement. *Encombrement* est rangé dans *Scene Collection*, puis masqué avec `H`.

**Pièges fréquents :**
- Un cube qui déborde du croquis : *Location* a été oubliée.
- `Alt + H` ne fait pas réapparaître les variantes : c'est normal, elles sont masquées par l'œil de leur collection.

### 1:27 · Les grands volumes (25 min)

D'après § 2 « Partir des primitives » et « Isoler et masquer » (figures 1.10 et 1.11).

**Le socle et le bras du bas (démo 4 min, guidé 8 min).** Vous montrez :
1. **La collection active.** Dans l'Outliner, clic droit sur *Scene Collection* > *New Collection*, renommez-la *Lampe*, puis cliquez-la : elle est surlignée, et chaque nouvel objet s'y range.
2. *Socle* : `Maj + A > Mesh > Cylinder`, F9 : *Vertices* 32, *Radius* `90mm`, *Depth* `25mm`. Puis `G Z`, `=`, `12.5mm`. « Peu de segments suffisent pour un blocage. »
3. *Bras_bas* : *Cylinder*, F9 : *Vertices* 16, *Radius* `8mm`, *Depth* `260mm`. `R Y 15.6`, puis en vue de face, `G` pour le poser sur le croquis. Repère : *Location* -5, 0, 165 mm.

Ils font, en guidé : *Lampe* active, puis *Socle* et *Bras_bas*, nommés.

**La vue locale (démo 2 min), puis l'autonomie (11 min).** Vous montrez : *Bras_bas* sélectionné, `/` du pavé numérique. Seul le bras reste à l'écran ; `/` ramène la vue complète.

Ils font, seuls, avec l'étape 7 des consignes :
- *Interrupteur* : *Cylinder*, *Vertices* 16, *Radius* `8mm`, *Depth* `6mm`, *Location* `55mm`, `0`, `28mm` ;
- *Bras_haut* : *Cylinder*, *Vertices* 16, *Radius* `7mm`, *Depth* `220mm`, `R Y 50.5`, posé sur le croquis (repère : 115, 0, 360 mm) ;
- chaque pièce vérifiée en vue locale, puis `Ctrl + S`.

**Point de contrôle :** en vue de face, les quatre volumes suivent le croquis. *Socle* mesure 180 × 180 × 25 mm. Les quatre pièces sont rangées dans *Lampe*.

**Corrigé :** dans *Variante A*, *Socle_A*, *Interrupteur_A*, *Bras_bas_A* et *Bras_haut_A*.

**Pièges fréquents :**
- Une pièce rangée dans *Scene Collection* ou dans *Croquis* : la collection active n'était pas *Lampe*. `M > Lampe`.
- Un cylindre de 2 m : F9 a été oublié, ou le panneau s'est refermé après un autre geste.
- Une pièce géante ou minuscule : une valeur tapée sans unité. Lisez l'unité affichée dans le champ.
- Une pièce qui n'apparaît pas à l'origine : le curseur 3D a bougé. `Maj + C`.
- Un bras penché du mauvais côté : `R Y -15.6` au lieu de `R Y 15.6`.
- Un bras juste de face mais décalé en profondeur : la règle de l'initiation, deux vues orthographiques avant de valider.

### 1:52 · Orienter : la tête (15 min)

**Vous montrez (5 min),** d'après § 3 « Choisir l'orientation de transformation » (figures 1.16 et 1.17) :
1. *Tête* : `Maj + A > Mesh > Cone`, F9 : *Vertices* 24, *Radius 1* `60mm`, *Radius 2* `22mm`, *Depth* `110mm`. `R Y -30` : la tête s'incline vers le plan de travail.
2. L'outil *Move* de la barre d'outils : le gizmo suit les axes du monde, *Global*. Menu *Transform Orientation* de l'en-tête, ou `,` : *Local*. Le gizmo s'incline avec la tête.
3. Retour en *Global*, puis `G Z Z` : le second `Z` suit l'axe propre de la tête. Elle avance ou recule sans glisser de côté.
4. **Ailleurs :** un rétroviseur incliné, un volet d'aile, un pare-brise de cabine.

**Ils font, en guidé (8 min) :** la tête, avec les valeurs de la démo ; en vue de face, `G` pour la placer près du haut de *Bras_haut* ; puis `G Z Z` pour l'avancer jusqu'à ce que le petit bout touche le bras. Repère : *Location* 233,5, 0, 372 mm.

**Quiz (2 min),** ensemble à l'écran : le premier quiz de la section 3, `G Z Z`.

**Point de contrôle :** la tête inclinée de 30°, son petit bout contre le haut du bras, son ouverture vers la table. `Ctrl + S`.

**Corrigé :** *Tête_A*, dans *Variante A*.

**Pièges fréquents :**
- `G Z` seul fait monter la tête à la verticale : c'est l'axe du monde. Le second `Z` change d'axe.
- Une tête tournée vers le haut : `R Y 30` au lieu de `R Y -30`.
- Le gizmo reste droit : l'outil actif n'est pas *Move*, ou l'orientation est restée *Global*.

### 2:07 · Aimanter et mesurer : les articulations (28 min)

**L'aimantation (démo 6 min, guidé 8 min, autonomie 5 min, quiz 1 min).** Vous montrez, d'après § 3 « L'aimantation » (figure 1.18) :
1. L'icône d'aimant de l'en-tête et `Maj + Tab`. Au quotidien, `Ctrl` pendant le geste suffit.
2. Le menu à droite de l'aimant : *Snap Base* sur *Center*, *Snap Target* sur *Face Center*. Citez aussi *Face* : l'objet se pose sur une surface. Ils l'essaieront seuls, et le câble du chapitre 2 s'en servira.
3. *Articulation_bas* : `Maj + A > Mesh > UV Sphere`, F9 : *Segments* 16, *Ring Count* 8, *Radius* `15mm`. `G`, puis `Ctrl` en survolant le bout inférieur de *Bras_bas* : la sphère se centre sur la face du bout.
4. Une astuce : `Maj + clic` dans *Snap Target* ajoute une cible ; `B` pendant le geste choisit le point de base.
5. **Ailleurs :** poser une roue sur son moyeu, un siège sur son rail, un feu dans son logement.

Ils font :
- **en guidé :** *Articulation_bas* (*Radius* `15mm`), puis *Articulation_milieu* (*Radius* `14mm`), au bout supérieur de *Bras_bas* ;
- **seuls :** *Articulation_haut* (*Radius* `12mm`), au bout supérieur de *Bras_haut*. La tête doit la toucher, sinon `G Z Z`. Un gros plan sur une articulation rappelle *Clip Start* ;
- **seuls, une pose sur une surface (1 min) :** vue de dessus (`7`), *Snap Target* sur *Face*, *Snap Base* sur *Closest*. *Interrupteur* sélectionné, `G`, puis `Ctrl` au-dessus du socle : l'interrupteur s'y pose.

**Quiz (1 min),** ensemble à l'écran : le second quiz de la section 3, la touche `Ctrl`.

**Mesurer (démo 3 min, guidé 5 min).** Vous montrez, d'après § 3 « Mesurer » (figures 1.22 et 1.23) :
1. En vue de face, l'outil *Measure* de la barre d'outils : cliquez-glissez d'un bord à l'autre du dessus du socle en maintenant `Ctrl`. La règle affiche 180 mm.
2. En Mode Édition, le menu *Mesh Edit Mode*, à droite d'*Overlays* : *Measurement > Edge Length*.

Ils font : le diamètre du socle (180 mm) ; la hauteur totale, du dessous du socle au sommet de l'articulation du haut (environ 442 mm) ; puis *Bras_bas* en Mode Édition, *Edge Length* coché, une arête verticale sélectionnée : 260 mm.

**Point de contrôle :** les trois articulations coiffent les bouts des bras ; l'interrupteur repose sur le socle ; la règle donne 180 mm et environ 440 mm. `Ctrl + S`.

**Corrigé :** dans *Variante A*, les trois articulations, aux bouts exacts des bras : (-40, 0, 40), (30, 0, 290) et (200, 0, 430) mm. *Interrupteur_A* repose sur le socle, son centre à 28 mm de haut.

**Pièges fréquents :**
- La sphère se pose sur un sommet ou sur un bord : *Snap Target* est resté sur *Vertex*, le réglage du fichier livré, ou *Snap Base* sur *Closest*.
- L'interrupteur s'enfonce à moitié dans le socle : *Snap Base* est resté sur *Center*. Passez sur *Closest*.
- Tout s'accroche, même sans `Ctrl` : l'aimant de l'en-tête est allumé. `Maj + Tab`.
- Une règle qui tombe dans le vide : `Ctrl` a été relâché trop tôt.
- Aucune longueur ne s'affiche : *Edge Length* ne montre que les arêtes sélectionnées, en Mode Édition.

### 2:35 · Pause (10 min)

### 2:45 · Éditer avec précision : biseau et extrusions (15 min)

Le travail se fait sur une **pièce d'essai**, pas sur la lampe. L'encart *IMPORTANT* de l'application le dit : un biseau posé trop tôt alourdit chaque correction. « Ces outils serviront dès que les proportions seront arrêtées. »

**Préparation (guidé, 1 min) :** *Socle* sélectionné, `Maj + D`, `X`, `=`, `-400mm`, Entrée. Puis `/` : la copie seule, en vue locale. `Tab`.

**Le biseau mesuré (démo 3 min, guidé 2 min, autonomie 2 min).** Vous montrez, d'après § 3 « Des biseaux mesurés » (figure 1.21) : mode arête (`2`), `Alt + clic` sur l'arête du haut, `Ctrl + B`, un petit mouvement de souris, clic. Puis F9 : *Width* `4mm` ; *Segments* 1, un chanfrein, puis 4, un congé ; *Profile Shape* 0,5, un arc de cercle ; *Clamp Overlap*. Une phrase sur l'encart *WARNING* : sur une échelle non appliquée, le biseau est irrégulier. Citez `Ctrl + Maj + B`, le biseau d'un sommet.

Ils font : en guidé, le même biseau, puis le passage d'un chanfrein à un congé dans F9 ; seuls, un congé de `2mm` sur l'arête du dessous.

**Les extrusions (démo 2 min, guidé 3 min, autonomie 1 min).** Vous montrez, d'après § 3 « Des extrusions adaptées à la forme » (figure 1.20), le menu `Alt + E` :
- *Extrude Faces Along Normals* sur l'anneau de faces du flanc : un bandeau ;
- *Extrude Individual Faces* : citée, ce sont les accoudoirs des sièges de l'initiation ;
- *Extrude Manifold*, vers l'intérieur : une encoche pour la sortie du câble, sans faces parasites.

Ils font :
- **en guidé, l'encoche :** mode face (`3`), quatre faces du flanc arrière, `Alt + E > Extrude Manifold`, `=`, `-5mm`, Entrée ;
- **seuls, le bandeau :** toujours en mode face, `Alt + clic` sur une arête verticale du flanc, `Alt + E > Extrude Faces Along Normals`, `=`, `2mm`, Entrée.

**Survol (1 min, démo seule) :** l'édition proportionnelle (`O`, figure 1.19), `G G` et `Alt + S`. Ils sont dans l'application et dans les défis.

**Pour finir :** `Tab`, `/`, puis `X` : la pièce d'essai est supprimée, pour qu'elle ne parte pas dans les variantes.

**Point de contrôle :** avant la suppression, F9 affiche le dernier réglage ; la pièce montre son congé de 4 mm, son encoche de 5 mm et son bandeau.

**Corrigé :** pas de corrigé dans le fichier. Le résultat se lit dans F9, et la figure 1.21 montre le biseau de 4 mm à 4 segments.

**Pièges fréquents :**
- Un biseau qui part de travers ou s'arrête net : *Clamp Overlap* le limite, ou l'arête choisie n'est pas la boucle entière.
- Une encoche qui ressort au lieu de rentrer : la valeur était positive. `Ctrl + Z`, puis `-5mm`.
- Une extrusion de plusieurs mètres : le `=` a été oublié, dans une scène en mètres. `Ctrl + Z`.
- La copie a été faite en Mode Édition : `Maj + D` a dupliqué la géométrie dans le socle lui-même. `Ctrl + Z`, `Tab`, et recommencez en Mode Objet.

### 3:00 · Variantes et silhouette (15 min)

Retour à la section 2 : « Comparer des variantes » et « Juger la silhouette » (figures 1.13 à 1.15).

***Duplicate Collection* (démo 3 min, guidé 6 min).** Vous montrez :
1. Clic droit sur la collection *Lampe* dans l'Outliner, *Duplicate Collection*. La copie s'appelle *Lampe.001*, ses pièces *Socle.001*, *Bras_bas.001*… Renommez la collection *Lampe_B*.
2. Clic droit sur *Lampe_B* > *Select Objects*, puis `G X`, `=`, `550mm`, Entrée.
3. Une variante : *Bras_haut.001* plus long. *Dimensions* Z `300mm`, puis `G Z Z`, `=`, `40mm`, Entrée : le bas du bras revient sur son articulation. `Ctrl + A > Scale`.
4. *Articulation_haut.001* : `G` avec `Ctrl` sur le nouveau bout du bras (*Face Center*, *Center*). *Tête.001* : `G` pour la rapprocher, puis `G Z Z`.
5. **Ailleurs :** trois pistes de calandre, de nez de train ou de winglet, côte à côte.

Ils font, en guidé : la même variante B.

**La silhouette (démo 2 min, guidé 3 min).** Vous montrez : menu *Viewport Shading*, *Lighting* sur *Flat*, *Color* sur *Custom* avec du noir, *Background* sur *Custom* avec un fond clair. Les deux lampes deviennent des ombres chinoises. Vues `1`, `3` et `7`. Ils font le même réglage, puis les trois vues : « Laquelle se lit le mieux ? »

**Quiz (1 min),** ensemble à l'écran : le quiz de la section 2, la silhouette.

**Point de contrôle :** deux lampes côte à côte, en ombres chinoises ; la variante B a un bras plus long. `Ctrl + S`.

**Corrigé :** *Variante B*, qui allonge elle aussi le bras supérieur, à 300 mm et un peu plus incliné.

**Pièges fréquents :**
- *Duplicate Linked* choisi au lieu de *Duplicate Collection* : changer le bras de B change aussi celui de la lampe. `Ctrl + Z`.
- Le bras de B ne touche plus son articulation du bas : `G Z Z` a été oublié, ou fait dans le mauvais sens.
- Des objets restés à la place de l'original : ils n'étaient pas sélectionnés, par exemple parce qu'ils étaient masqués avec `H`.
- L'articulation se pose sur le bord : *Snap Target* est resté sur *Face* depuis la pose de l'interrupteur. Revenez à *Face Center* et *Center*.

### 3:15 · Atelier · Trois pistes pour une revue de concept (25 min)

La fiche complète est plus bas. Le lancement dure 2 minutes, l'autonomie 20 minutes et la revue 3 minutes.

### 3:40 · Galerie, bilan et passerelle (10 min)

- **Galerie (4 min) :** chaque écran montre ses trois pistes en ombres chinoises, en vue de face. Tout le monde fait le tour des postes.
- **Trois questions (3 min) :**
  - « Pendant un déplacement, comment taper 25 mm, quelle que soit l'unité affichée ? »
  - « Comment avancer la tête dans son propre axe ? »
  - « Quel réglage transforme vos lampes en ombres chinoises ? »
- **Passerelle (2 min) :** « Au chapitre 2, chaque volume devient une pièce propre : un bras à deux tiges, un abat-jour en coque, une grille d'aération, un câble. Votre blocage sert de gabarit. Si votre fichier vous manque, un fichier de départ vous attend. »
- **Dernier contrôle (1 min) :** chacun a enregistré `lampe_blocage_v001.blend`, moteur EEVEE.

<!-- pagebreak -->

## Atelier · Trois pistes pour une revue de concept

**Fichier :** `lampe_blocage_v001.blend` · **Durée :** 25 min · **De 3:15 à 3:40**

**Situation :** « Revue de concept demain matin. Présentez trois pistes de lampe, en silhouette, et défendez celle que vous retenez. »

**Objectif :** décliner une troisième piste, comparer les trois en ombres chinoises, puis retenir la meilleure et la contrôler.

**Pourquoi il fonctionne :**
- Aucune notion nouvelle : l'atelier réinvestit les trois sections, dans l'ordre de la méthode en quatre temps.
- La silhouette rend la comparaison objective : sans couleur ni détail, seules les proportions parlent.
- Le choix argumenté est un vrai geste de designer. Il prépare la revue de design de l'atelier du chapitre 4.

**Le socle, en 5 étapes :**

| Étape | Ce qu'il faut faire | Gestes réinvestis |
|---|---|---|
| 1 | *Duplicate Collection* de *Lampe*, renommée *Lampe_C*, puis `G X = 1100mm` | *Duplicate Collection*, *Select Objects*, saisie avec unité |
| 2 | Une autre piste. Exemple : *Tête.002* supprimée, puis un cylindre de 24 côtés, *Radius* `50mm`, *Depth* `120mm`, `R Y -30`, posé contre l'articulation et avancé avec `G Z Z` | Primitives et F9, orientation *Local*, aimantation |
| 3 | Les trois pistes comparées en ombres chinoises, en vues de face, de droite et de dessus | Réglage silhouette, Quad View |
| 4 | La piste retenue contrôlée : diamètre du socle, hauteur totale | *Measure* |
| 5 | La piste retenue visible, les deux autres masquées (œil) ; l'échelle appliquée sur les pièces redimensionnées ; `Ctrl + S` | Outliner, `Ctrl + A > Scale` |

**Déroulé :**
1. **Lancement (2 min).** Ouvrez l'œil de *Variante C* : une tête cylindrique. « La vôtre peut être différente : socle carré, tête plus large, bras plus court. » Lancez le minuteur.
2. **Autonomie (20 min).** Chacun suit l'étape 12 des consignes. Annoncez les 5 dernières minutes : c'est le moment de choisir et d'enregistrer.
3. **Revue (3 min).** Deux volontaires projettent leurs trois silhouettes. « Laquelle retenez-vous, et pourquoi ? »

**Paliers :**
- **★ :** renommer les pièces des variantes sans `.001`, par exemple *Socle_B* ; une copie de l'encombrement (`Alt + H`, `Maj + D`, `X = 550mm`) pour voir si la variante B le dépasse ; une quatrième piste.
- **★★ :** les défis de la partie « Pour ceux qui avancent vite ».

**Points d'observation :**
- Une troisième piste identique à la deuxième : la copie a été faite à partir de *Lampe_B*. C'est possible, mais le décalage est alors de 550 mm depuis B.
- Une silhouette qui ne dit rien : la vue est restée en perspective. Passez en orthographique.
- Un apprenant qui modifie *Variante C* au lieu de sa propre lampe : `Ctrl + Z`, et refermez l'œil des variantes du corrigé.

**Corrigé :** les collections masquées *Variante A*, *B* et *C*. *Variante C* remplace la tête conique par une tête cylindrique de 100 mm de diamètre et 120 mm de long.

**Ce que le chapitre 2 attend :** `lampe_blocage_v001.blend`, moteur EEVEE, la piste retenue visible. Le chapitre 2 part toutefois de son propre fichier de départ, dont le gabarit est la *Variante A* : un blocage inachevé ne bloque personne.

## Gérer l'hétérogénéité

### Le parcours « première fois »

- Les binômes et les copilotes de l'initiation restent en place.
- Les consignes donnent chaque geste au millimètre, unité comprise. Les valeurs restent indicatives : chacun peut les adapter à son concept.
- Chacun garde l'unité d'affichage qu'il préfère : les consignes marchent avec les deux.
- Le socle de chaque séquence suffit : il couvre tous les points du programme.
- À chaque point de contrôle, passez d'abord par les postes des débutants.
- **Un apprenant très en retard** ouvre l'œil de *Variante A*, fait *Duplicate Collection*, renomme la copie *Lampe*, puis referme l'œil de *Variante A*. Il reprend avec le groupe à la séquence suivante, et le corrigé reste intact.

### Pour ceux qui avancent vite

- Les paliers ★ de l'atelier.
- **Un socle bombé (★★) :** sur une variante, `I` trois fois sur le dessus du socle, puis la face centrale, `O` et `G Z = 8mm` : l'édition proportionnelle galbe le dessus. La molette règle l'influence, `Maj + O` le profil.
- **Une coupe qui glisse (★★) :** `G G` sur un anneau du socle bombé ; `Alt + S` sur les faces de la tête pour la gonfler.
- **Un socle carré aux coins arrondis (★★) :** un cube à 180 × 180 × 25 mm, l'échelle appliquée, puis `Ctrl + Maj + B` sur les sommets du dessus.
- **Caler un croquis à l'œil (★★) :** replacer le croquis de profil sans les valeurs, en ajustant *Size* jusqu'à ce que le socle dessiné mesure 180 mm, contrôlé avec l'outil *Measure*.
- **Plusieurs cibles d'aimantation (★) :** *Vertex* et *Face Center* ensemble (`Maj + clic`), et `B` pendant le geste.
- **Un objet de leur secteur (★★) :** la même méthode en quatre temps sur un rétroviseur, une liseuse de cabine ou une poignée de maintien de tram. Pas de corrigé : vous le validez à l'écran.
- Le rôle de copilote, comme à l'initiation.

## Animer : ce qui change au chapitre 1

Les conseils de l'initiation restent valables : « Regardez, puis à vous », les touches dites à voix haute, les post-it vert et rose, la règle des 3 minutes, la souris qu'on ne prend pas. Ce chapitre en ajoute six :
1. **Dites l'unité à voix haute,** et le `=` avec : « G, Z, égal, vingt-cinq millimètres ». Sur votre poste en configuration d'usine, le `=` est toujours nécessaire.
2. **Présentez les options comme des options.** La première heure montre des réglages ; personne n'est obligé de les garder. Seule la saisie de l'unité est exigée.
3. **Le corrigé se compare, il ne se copie pas.** Rappelez-le à chaque ouverture d'une variante, et faites refermer l'œil ensuite.
4. **Faites tourner la vue avant de valider.** Une pièce juste de face peut être décalée en profondeur : deux vues orthographiques, toujours.
5. **Parlez métier :** encombrement, proportions, silhouette, piste retenue. Le blocage est une décision de designer, pas un exercice de modélisation.
6. **Tenez le rythme de la première heure.** La section 1 compte beaucoup de notions, mais chacune tient en un réglage : une case, un champ ou un menu. La charge réelle vient en section 3 : ne prenez pas de retard avant.

## Si vous prenez du retard

Raccourcissez dans cet ordre :

| Ordre | Ce que l'on coupe | Ce que l'on garde |
|---|---|---|
| D'abord | *À votre main* : démo de 2 minutes, sans essai ; l'option *Length* montrée sans essai | La mention des options |
| Ensuite | Images de référence : réglages sur *Croquis_face* seulement, sans replacer le croquis de profil | L'onglet *Object Data* d'une image, dont le chapitre 2 se sert |
| Ensuite | L'encombrement : vous le montrez, les apprenants ne le font pas | *Dimensions* et `H`, repris à la variante B |
| Ensuite | Les extrusions : démo seule ; le biseau reste en guidé | Le biseau mesuré, point du programme |
| En dernier | L'atelier : deux pistes au lieu de trois (A et B), comparées en silhouette | Le choix de la piste et l'enregistrement |

**Ce qui ne saute jamais,** car les chapitres 2 à 4 s'en servent : la saisie d'une valeur avec son unité ; la vérification du moteur et l'enregistrement sous `lampe_blocage_v001.blend` ; le menu *Viewport Shading* ; *Clip Start* ; la vue locale ; l'orientation *Local* et `G Z Z` ; l'aimantation, avec la pose sur une surface (*Face*) ; la mesure ; *Duplicate Collection*.

## Si vous êtes en avance

- **L'atelier s'enrichit :** les paliers ★, puis les défis ★★ de « Pour ceux qui avancent vite », en commençant par le socle bombé.
- **La revue s'allonge :** chacun présente sa piste retenue en une minute, au lieu de deux volontaires.

<!-- pagebreak -->

## Annexe · Les consignes à projeter ou à imprimer

Le fichier livré n'a pas de texte LISEZ-MOI : ces consignes en tiennent lieu. Chaque valeur porte son unité : elles marchent avec un affichage en mètres comme en millimètres. Les valeurs sont indicatives : chacun peut les adapter à son concept.

> **La règle :** tapez toujours l'unité. Dans un champ : `25mm`. Pendant un geste : `=` d'abord, puis la valeur (`G Z = 25mm`) ; sans `=`, l'unité est ignorée. **Le corrigé :** collections *Variante A*, *B* et *C*, œil fermé. On compare, on ne copie pas.

### 1 · Les cotes (scène d'usine, non enregistrée)

1. `N > Item > Dimensions` : `180mm`, `180mm`, `25mm`.
2. `G Z = 12.5mm`, Entrée.
3. `Ctrl + A > Scale`.
4. Option : *Scene > Units > Length* : *Millimeters*.

Contrôle : 180 × 180 × 25 mm ; *Location* Z 12,5 mm ; *Scale* 1.

### 2 · Le fichier

1. *File > Open* : `PRC02_ch1_blocage_lampe.blend` (*Don't Save*).
2. *File > Save As* : `lampe_blocage_v001.blend`. Puis `Ctrl + S` à chaque contrôle.
3. *Render > Render Engine* : vérifiez EEVEE, choisissez-le si besoin.

### 3 · L'affichage (œil de *Variante A* ouvert, puis refermé)

1. *Viewport Shading* : *Color* *Random*, *Cavity*. Essayez *MatCap*.
2. En perspective (`5`) : `N > View > Clip Start` `10mm`, puis `1mm`.
3. `Ctrl + Alt + Q`, puis de nouveau `Ctrl + Alt + Q`.

### 4 · Le croquis de profil

1. *Croquis_face* : *Object Data* > *Opacity*, *Depth*, *Show In*. Essayez.
2. Masquez *Croquis_profil* (œil). Vue de droite (`3`).
3. *Add > Image > Reference* : `croquis_lampe_profil.png`.
4. *Object Data* : *Size* `560mm` ; *Opacity* 0,5 ; *Depth* *Back* ; *Show In* : *Perspective* décoché, *Only Axis Aligned* coché.
5. `N > Item > Location` : X `-300mm`, Z `222mm`.
6. Rouvrez *Croquis_profil* : les deux coïncident. Supprimez le vôtre (`X`).

### 5 · À votre main (options)

- Clic droit > *Add to Quick Favorites*, puis `Q`.
- *Edit > Preferences > Navigation* ; *Input > Default to Advanced Numeric Input*.

### 6 · L'encombrement

1. `Maj + A > Mesh > Cube`. Renommez-le *Encombrement*.
2. *Dimensions* : `420mm`, `180mm`, `450mm`. *Location* : X `120mm`, Z `225mm`.
3. Vues `1` et `3` : le croquis tient dedans. `H` pour le masquer.

### 7 · Les grands volumes

1. Outliner : clic droit sur *Scene Collection* > *New Collection*. Renommez-la *Lampe*, puis cliquez-la : elle reçoit les nouveaux objets.
2. *Socle* : *Cylinder*, F9 : *Vertices* 32, *Radius* `90mm`, *Depth* `25mm`. `G Z = 12.5mm`.
3. *Bras_bas* : *Cylinder*, F9 : *Vertices* 16, *Radius* `8mm`, *Depth* `260mm`. `R Y 15.6`, puis `G` sur le croquis (repère : -5, 0, 165 mm).
4. À vous : *Interrupteur* : *Cylinder*, *Vertices* 16, *Radius* `8mm`, *Depth* `6mm`, *Location* `55mm`, `0`, `28mm`.
5. À vous : *Bras_haut* : *Cylinder*, *Vertices* 16, *Radius* `7mm`, *Depth* `220mm`, `R Y 50.5` (repère : 115, 0, 360 mm).
6. `/` du pavé numérique : vérifiez une pièce seule, puis `/` pour revenir.

Contrôle : en vue de face (`1`), les volumes suivent le croquis.

### 8 · La tête (orientation *Local*)

1. *Cone*, F9 : *Vertices* 24, *Radius 1* `60mm`, *Radius 2* `22mm`, *Depth* `110mm`. `R Y -30`.
2. Vue de face : `G` près du haut de *Bras_haut*.
3. `G Z Z` : avancez-la dans son axe jusqu'au bras (repère : 233,5, 0, 372 mm).

### 9 · Les articulations (aimantation) et la mesure

1. Menu de l'aimant : *Snap Base* *Center* ; *Snap Target* *Face Center*.
2. *UV Sphere*, F9 : *Segments* 16, *Ring Count* 8, *Radius* `15mm`. `G`, puis `Ctrl` au-dessus du bout bas de *Bras_bas*. Renommez-la *Articulation_bas*.
3. *Articulation_milieu* (*Radius* `14mm`) : bout haut de *Bras_bas*.
4. À vous : *Articulation_haut* (*Radius* `12mm`) : bout haut de *Bras_haut*.
5. À vous : vue de dessus (`7`), *Snap Target* *Face*, *Snap Base* *Closest*. *Interrupteur* : `G`, puis `Ctrl` au-dessus du socle : il se pose dessus.
6. Outil *Measure*, avec `Ctrl` : socle 180 mm ; hauteur totale environ 442 mm.

Contrôle : les articulations coiffent les bouts des bras.

### 10 · Biseau et extrusions (pièce d'essai, supprimée à la fin)

1. *Socle* : `Maj + D`, `X`, `= -400mm`, Entrée. `/`, puis `Tab`.
2. Mode arête (`2`), `Alt + clic` sur l'arête du haut, `Ctrl + B`, clic. F9 : *Width* `4mm` ; *Segments* 1, puis 4 ; *Profile* 0,5.
3. À vous : un congé de `2mm` sur l'arête du bas (*Width* dans F9).
4. Mode face (`3`), 4 faces du flanc arrière : `Alt + E > Extrude Manifold`, `= -5mm`, Entrée.
5. À vous : `Alt + clic` sur une arête verticale du flanc, `Alt + E > Extrude Faces Along Normals`, `= 2mm`, Entrée.
6. `Tab`, `/`, puis `X` : supprimez la pièce d'essai.

### 11 · La variante B et la silhouette

1. Clic droit sur *Lampe* > *Duplicate Collection*. Renommez-la *Lampe_B*.
2. Clic droit sur *Lampe_B* > *Select Objects*. `G X = 550mm`.
3. *Bras_haut.001* : *Dimensions* Z `300mm`, puis `G Z Z = 40mm`. `Ctrl + A > Scale`.
4. *Snap Target* *Face Center*, *Snap Base* *Center*. *Articulation_haut.001* : `G` + `Ctrl` sur le nouveau bout. *Tête.001* : `G`, puis `G Z Z`.
5. *Viewport Shading* : *Lighting* *Flat* ; *Color* *Custom*, noir ; *Background* *Custom*, clair. Vues `1`, `3` et `7`.

### 12 · Atelier

1. *Duplicate Collection* de *Lampe* : *Lampe_C*. *Select Objects*, `G X = 1100mm`.
2. Une autre piste. Exemple : supprimez *Tête.002*, puis *Cylinder*, *Vertices* 24, *Radius* `50mm`, *Depth* `120mm`, `R Y -30`, `G` et `G Z Z`.
3. Comparez les trois silhouettes (vues `1`, `3`, `7` ou Quad View).
4. Mesurez la piste retenue (*Measure*).
5. Laissez-la visible, masquez les deux autres. `Ctrl + S`.

★ Renommez les pièces sans `.001` ; copiez l'*Encombrement* (`Alt + H`, `Maj + D`, `X = 550mm`) pour voir si la variante B le dépasse ; une quatrième piste. ★★ Demandez un défi au formateur : un socle bombé, un socle carré aux coins arrondis, un croquis calé à l'œil…

---

Le fichier `PRC02_ch1_blocage_lampe.blend` est livré tel quel ; son passage sur le moteur EEVEE est prévu avec les corrections de fin de projet. Ce document se convertit en PDF avec `tool/deroule_initiation/export_pdf.ps1 -Source _resources\PRC02-deroule-chap1.md`.
