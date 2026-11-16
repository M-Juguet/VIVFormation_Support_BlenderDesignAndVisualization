## 1. Un environnement adapté au design produit

> [!NOTE]
> Ce chapitre part du principe que vous savez naviguer dans la vue 3D, sélectionner un objet et le transformer avec `G`, `R` et `S`. Si ces gestes ne vous sont pas encore familiers, les chapitres Basics 101 à 103 les reprennent pas à pas. Les captures et les libellés correspondent à Blender 5.2 LTS, avec l'interface en anglais.

### Adapter Blender à votre façon de travailler
Blender fonctionne très bien avec ses réglages d'origine. Les options présentées dans cette section ne sont donc pas des passages obligés : elles rapprochent le logiciel de vos habitudes et de celles de votre équipe.

Gardez celles qui vous font gagner du temps et laissez les autres de côté. Vous pourrez y revenir le jour où un projet le demande.

### Choisir l'unité d'affichage
Par défaut, Blender mesure tout en mètres, ce qui convient très bien à un véhicule entier ou à un aménagement intérieur. Si vos plans et vos cotes sont exprimés dans une autre unité, vous pouvez changer l'unité d'affichage dans l'éditeur de propriétés, onglet *Scene*, rubrique *Units* : le champ *Length* propose notamment *Centimeters* et *Millimeters*.

Quelle que soit l'unité affichée, vous pouvez aussi la préciser en tapant une valeur dans un champ : `35mm`, `3.5cm` ou `1m 20mm` sont compris tels quels.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/scene_units_blender.jpg"
caption: "Figure 1.1 : La rubrique Units de l'onglet Scene, avec la longueur affichée en millimètres."
title: "Afficher les cotes dans votre unité"
---
La capture montre la rubrique Units de l'onglet Scene. Seul le champ Length a changé : il passe de Meters à Millimeters. Unit Scale reste à 1,000, ce qui conserve l'échelle réelle de la scène : un objet de 120 mm mesure toujours 0,12 m pour Blender.
```

> [!WARNING]
> Le champ *Unit Scale* change lui aussi les valeurs affichées, mais pas le comportement interne de la scène : les simulations physiques, par exemple, continuent de calculer en unités internes. Pour simplement afficher une autre unité, le champ *Length* suffit et *Unit Scale* peut rester à 1,000.

### Voir de près les petits objets
Quand vous zoomez très près d'un petit objet, une partie peut disparaître, comme coupée par un plan invisible. C'est la distance minimale d'affichage de la vue, *Clip Start*, réglée par défaut à 10 mm.

Si cela vous gêne, vous pouvez la réduire dans la barre latérale (`N`), onglet *View*, par exemple à 1 mm. Mieux vaut ne pas descendre beaucoup plus bas : plus l'écart avec *Clip End* est grand, moins l'affichage de la profondeur est précis, et des surfaces proches peuvent se mettre à scintiller.

![Figure 1.2 : L'interrupteur de la lampe, 16 mm de diamètre, vu de très près : avec Clip Start réglé à 1 mm dans l'onglet View de la barre latérale, il reste entièrement visible.](assets/images/clip_start_sidebar_blender.jpg)

### Lire la forme dans la vue 3D
Le mode d'affichage *Solid*, celui par défaut, propose plusieurs options pour mieux lire les volumes. Elles se trouvent dans le menu *Viewport Shading*, ouvert par la petite flèche à droite des quatre boutons de mode d'affichage, en haut à droite de la vue 3D :
- *Lighting* : *Studio* éclaire les volumes comme en studio photo, *MatCap* (*material capture*, une image de matière qui simule éclairage et reflets) révèle les courbures, *Flat* supprime tout éclairage.
- *Color* : *Random* donne une couleur différente à chaque objet, pratique pour distinguer des volumes qui se touchent.
- *Cavity* : souligne les arêtes saillantes et les creux.
- *Outline* : trace le contour de chaque objet.
Ces réglages ne changent que l'affichage dans la vue : ils n'ont aucun effet sur le rendu final.

```side-by-side
layout: "textRight"
imagePath: "assets/images/solid_shading_options_blender.jpg"
caption: "Figure 1.3 : Le menu Viewport Shading du mode Solid, avec la couleur Random et l'option Cavity activées."
title: "Des volumes faciles à distinguer"
---
La capture montre le menu ouvert à côté du blocage d'une lampe. Avec la couleur Random, chaque volume se détache de ses voisins ; avec Cavity, les arêtes vives ressortent en clair. Regardez la jonction entre le socle et le bras : elle se lit d'un coup d'œil.
```

### Travailler avec des images de référence
Un croquis, une vue de face ou de profil, la photo d'une maquette : une image de référence aide à respecter les proportions d'un concept. Pour en placer une, passez dans une vue orthographique, par exemple la vue de face (`1` du pavé numérique), puis utilisez *Add > Image > Reference*, ou *Background* pour qu'elle reste toujours derrière les objets. Vous pouvez aussi faire glisser l'image depuis l'Explorateur Windows dans la vue 3D.

L'image est portée par un objet *Empty*, un objet sans géométrie que vous déplacez et redimensionnez comme les autres. Dans son onglet *Object Data*, quelques réglages la rendent plus confortable : *Opacity* pour la rendre transparente, *Depth* pour l'afficher devant ou derrière les objets, et *Show In* pour ne la montrer que dans les vues orthographiques.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/reference_image_blender.jpg"
caption: "Figure 1.4 : Un croquis de face placé en image de référence derrière le blocage de la lampe, en vue orthographique."
title: "Caler le volume sur un croquis"
---
Le croquis est affiché en transparence derrière les volumes. Vous vérifiez d'un coup d'œil que la hauteur du bras et le diamètre du socle suivent le dessin. Une seconde image, placée dans la vue de côté, permet de caler le volume sur un deuxième axe.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/reference_image_settings_blender.jpg"
caption: "Figure 1.5 : Les réglages de l'image de référence dans l'onglet Object Data : opacité, profondeur et vues où elle s'affiche."
title: "Régler l'affichage de l'image"
---
La capture montre l'onglet Object Data du croquis de face. Opacity, à 0,5, rend l'image transparente ; Depth sur Back la garde derrière les volumes. Avec Show In réglé sur Orthographic et Only Axis Aligned, le croquis ne s'affiche qu'en vue orthographique de face : il disparaît dès que vous tournez autour de l'objet.
```

### Voir sous tous les angles avec la Quad View
`Ctrl + Alt + Q` divise la vue 3D en quatre : trois vues orthographiques (dessus, face et droite) et une vue en perspective. C'est une mise en plan qui se met à jour en direct : chaque modification se lit simultanément sous tous les angles. Le même raccourci revient à une seule vue.

![Figure 1.6 : La Quad View : vues de dessus, de face et de droite en orthographique, et vue en perspective en haut à droite.](assets/images/quad_view_blender.jpg)

### Garder ses outils à portée : les Quick Favorites
Certains outils et réglages reviennent sans cesse. Pour les garder sous la main, faites un clic droit sur un outil ou une entrée de menu, puis choisissez *Add to Quick Favorites*. La touche `Q` ouvre ensuite ce menu personnel à l'endroit du curseur.

Vous pouvez y ranger, par exemple, la Quad View, l'aimantation ou un mode d'affichage que vous utilisez souvent.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/quick_favorites_menu_blender.jpg"
caption: "Figure 1.7 : Le menu Quick Favorites, ouvert avec la touche Q, avec trois commandes ajoutées par clic droit : Toggle Quad View, Snap et Toggle X-Ray."
title: "Un menu à votre main"
---
La touche Q ouvre le menu Quick Favorites à l'endroit du curseur. Les trois entrées de la capture y ont été ajoutées par un clic droit, puis Add to Quick Favorites : Toggle Quad View depuis le menu View > Area, Snap depuis le bouton en forme d'aimant de l'en-tête, et Toggle X-Ray depuis le bouton placé à gauche des modes d'affichage. Le menu rappelle à droite le raccourci de chaque entrée. Pour en retirer une, faites un clic droit dessus dans ce menu, puis Remove from Quick Favorites.
```

### Ajuster la navigation
L'onglet *Navigation* des préférences (*Edit > Preferences*) contient trois options désactivées par défaut, qui changent nettement le confort de travail autour d'un objet :
- *Orbit Around Selection* : la vue tourne autour de la sélection plutôt qu'autour du centre de l'écran.
- *Zoom to Mouse Position* : le zoom se dirige vers le curseur de la souris.
- *Auto Depth*, la case *Depth* de la ligne *Auto* : la navigation s'adapte à la profondeur de la surface pointée, utile pour tourner autour d'un détail.
Testez-les et gardez celles qui vous conviennent.

![Figure 1.8 : L'onglet Navigation des préférences : Orbit Around Selection, la case Depth de la ligne Auto et Zoom to Mouse Position sont désactivées par défaut.](assets/images/preferences_navigation_blender.jpg)

### Enregistrer son fichier de démarrage
Les préférences s'enregistrent automatiquement, mais l'unité, les options d'affichage et la disposition des vues appartiennent au fichier ouvert. Pour retrouver votre environnement à chaque nouveau projet, réglez un fichier à votre goût, puis choisissez *File > Defaults > Save Startup File*.

En cas de besoin, *File > Defaults > Load Factory Settings* rétablit le fichier de démarrage et les préférences d'origine.

```side-by-side
layout: "textRight"
imagePath: "assets/images/file_defaults_menu_blender.jpg"
caption: "Figure 1.9 : Le sous-menu File > Defaults, avec Save Startup File et Load Factory Settings."
title: "Le sous-menu Defaults"
---
Le sous-menu Defaults du menu File réunit les deux commandes. Save Startup File enregistre le fichier courant comme point de départ de chaque nouveau projet ; Load Factory Settings revient aux réglages d'origine de Blender.
```

> [!TIP]
> Dans une équipe, un fichier de démarrage commun garantit que tout le monde travaille avec la même unité et les mêmes repères. Les fichiers échangés s'ouvrent alors avec les mêmes réglages chez chacun.

```quiz
question: "Vos cotes sont en millimètres. Quel réglage permet de les afficher dans cette unité, sans rien changer au comportement interne de la scène ?"
options:
  - "Passer Unit Scale à 0,001"
  - "Régler Length sur Millimeters dans la rubrique Units de l'onglet Scene"
  - "Diviser toutes les dimensions des objets par 1000"
  - "Réduire Clip Start à 1 mm"
correctIndices:
  - 1
explanation: "Le champ **Length** de la rubrique *Units* change l'unité d'affichage et de saisie. *Unit Scale* agit aussi sur l'affichage, mais introduit un écart avec les unités internes, que la physique, par exemple, ne prend pas en compte. *Clip Start* ne règle que la distance minimale d'affichage de la vue."
```

## 2. Explorer un concept par blocage de volumes

### Le blocage, une maquette numérique rapide
Le blocage de volumes, souvent appelé *greyboxing* (« boîte grise »), consiste à assembler des formes simples pour représenter un objet dans ses grandes masses. C'est l'équivalent numérique d'une maquette en mousse : on y juge les proportions, la silhouette et l'encombrement, sans s'occuper des détails.

Son intérêt est de pouvoir se tromper vite. Un volume mal proportionné se corrige en quelques secondes, une forme détaillée en plusieurs heures. Le blocage permet ainsi de comparer plusieurs pistes avant d'investir du temps dans l'une d'elles.

### Une méthode en quatre temps
Il n'existe pas une seule bonne façon de bloquer un concept. Ces quatre étapes offrent un point de départ fiable, à adapter à votre objet :
1. **Poser l'encombrement** : un simple cube, aux cotes maximales de l'objet, sert de gabarit.
2. **Placer les grands volumes** : une primitive par masse principale (socle, bras, tête…), avec peu de segments.
3. **Ajuster les proportions** : à la souris, ou en saisissant les cotes au chiffre près.
4. **Lire la silhouette et itérer** : comparer, corriger, essayer une variante.
Le blocage s'arrête quand les proportions vous conviennent : le détail viendra au chapitre 2.

```resource
title: "Fichier d'exercice : blocage de la lampe de bureau"
description: "Scène de départ du fil rouge, avec les croquis de face et de profil de la lampe et un exemple de blocage terminé, masqué, pour comparer votre travail."
fileName: "PRC02_ch1_blocage_lampe.blend (0.2 Mo)"
downloadUrl: "https://example.com/files/prc02-ch1-blocage-lampe"
```

### Partir des primitives
Les primitives s'ajoutent avec *Add > Mesh* (`Maj + A`) : cube, cylindre, sphère, cône… Juste après l'ajout, le panneau *Ajuster la dernière opération*, en bas à gauche de la vue (rouvert avec `F9`), règle leurs paramètres : nombre de sommets (*Vertices*), rayon, profondeur.

Pour un blocage, peu de segments suffisent : un cylindre à 16 ou 24 sommets reste léger et se lit aussi bien qu'un cylindre à 64. Nommer chaque volume dès sa création (double-clic dans l'Outliner) vous fera gagner du temps au moment de comparer et de modifier.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/add_mesh_menu_blender.jpg"
caption: "Figure 1.10 : Le sous-menu Mesh du menu Add, ouvert à côté du blocage de la lampe."
title: "Le menu des primitives"
---
La capture montre le sous-menu Mesh du menu Add (Maj + A dans la vue 3D). Cube, Cylinder, UV Sphere et Cone suffisent à la plupart des blocages ; Plane et Circle servent de base aux formes plates.
```

![Figure 1.11 : Le blocage d'une lampe de bureau : une primitive par volume, nommée dans l'Outliner et affichée en couleur aléatoire.](assets/images/greybox_lamp_blender.jpg)

### Donner les bonnes dimensions
Pour obtenir une taille précise, la barre latérale (`N`), onglet *Item*, affiche le champ *Dimensions* : la taille réelle de l'objet sur X, Y et Z. Vous pouvez y taper directement une cote, par exemple `180mm` pour le diamètre du socle. Blender ajuste alors l'échelle (*Scale*) de l'objet en conséquence.

Cette échelle gagne à être appliquée avant certaines opérations, comme le biseau : `Ctrl + A > Scale` la ramène à 1,000 sans changer la forme. Basics 103 explique pourquoi.

```side-by-side
layout: "textRight"
imagePath: "assets/images/dimensions_sidebar_blender.jpg"
caption: "Figure 1.12 : Le panneau Transform de la barre latérale : les champs Dimensions donnent la taille réelle de l'objet sélectionné."
title: "Saisir une cote"
---
La capture montre le socle de la lampe sélectionné. Les champs Dimensions indiquent son diamètre et sa hauteur, tandis que les champs Scale montrent le facteur d'échelle qui en découle. Taper une cote dans Dimensions est souvent plus parlant que de chercher le bon facteur d'échelle.
```

### Isoler et masquer
Quand les volumes se multiplient, quelques raccourcis aident à se concentrer :
- `/` du pavé numérique bascule en **vue locale** : seuls les objets sélectionnés restent affichés ; le même raccourci ramène la vue complète.
- `H` masque la sélection, `Maj + H` masque tout le reste, `Alt + H` réaffiche tout.
Ces commandes ne changent que l'affichage dans la vue 3D : rien n'est supprimé.

### Comparer des variantes
Le blocage prend tout son sens quand on compare plusieurs pistes côte à côte. Rangez chaque proposition dans sa propre collection (les collections sont présentées dans Basics 102), par exemple « Variante A ».

Un clic droit sur la collection dans l'Outliner, puis *Duplicate Collection*, en crée une copie complète. Décalez-la sur le côté et modifiez-la librement : bras plus long, tête plus large, socle carré…

```side-by-side
layout: "textRight"
imagePath: "assets/images/duplicate_collection_menu_blender.jpg"
caption: "Figure 1.13 : Le menu contextuel d'une collection dans l'Outliner, avec Duplicate Collection."
title: "Dupliquer une variante"
---
La capture montre le menu ouvert par un clic droit sur la collection Variante A dans l'Outliner. Duplicate Collection copie la collection avec tous ses objets ; Duplicate Linked crée des copies liées, qui partagent leur géométrie avec l'original.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/variants_collections_blender.jpg"
caption: "Figure 1.14 : Trois variantes du concept, chacune dans sa collection, alignées pour être comparées."
title: "Une collection par variante"
---
Chaque variante occupe sa propre collection dans l'Outliner. L'icône en forme d'œil permet d'afficher une seule variante ou de les comparer toutes. Ici, la variante B allonge le bras supérieur et la variante C remplace la tête conique par une tête cylindrique.
```

### Juger la silhouette
Une forme se reconnaît d'abord à sa silhouette. Pour l'évaluer sans être distrait par le modelé des volumes, vous pouvez régler temporairement le mode *Solid* ainsi : *Lighting* sur *Flat*, *Color* sur *Custom* avec une couleur noire, et *Background* sur *Custom* avec un fond clair.

Les objets deviennent des ombres chinoises, à observer dans les vues de face, de côté et de dessus. Une silhouette lisible et équilibrée sous ces trois angles est un bon signe pour la suite.

![Figure 1.15 : Le test de silhouette sur les trois variantes : en aplat noir, les différences de proportions sautent aux yeux.](assets/images/silhouette_check_blender.jpg)

> [!IMPORTANT]
> Tant que les proportions ne sont pas arrêtées, des volumes simples suffisent. Un biseau ou un perçage ajouté trop tôt alourdit chaque correction suivante, et une finition soignée masque souvent un problème de proportions.

> [!NOTE]
> Le blocage ne disparaît pas une fois validé. Il sert de gabarit au chapitre 2 : la modélisation propre s'appuie sur ses volumes et ses cotes.

```quiz
question: "Pour juger la silhouette d'un concept, quel réglage du mode Solid est le plus parlant ?"
options:
  - "Lighting sur Flat, avec une couleur unie sombre sur un fond clair"
  - "Color sur Random"
  - "Lighting sur MatCap"
  - "L'option Cavity"
correctIndices:
  - 0
explanation: "Sans éclairage (**Flat**) et avec une couleur unie sombre sur fond clair, les objets deviennent des **ombres chinoises** : seul le contour compte. Random, MatCap et Cavity, au contraire, aident à lire les volumes et le modelé."
```

## 3. Transformer et éditer avec précision

### Aller plus loin que les gestes de base
Les transformations (`G`, `R`, `S`) et les outils d'édition (*Extrude*, *Inset*, *Bevel*, *Loop Cut*) sont présentés dans Basics 102 et 103. Cette section les complète par ce qui fait la différence sur un concept produit : contrôler la direction d'un geste, s'accrocher à la géométrie existante et ajuster une forme sans la reconstruire.

### Choisir l'orientation de transformation
Une transformation contrainte à un axe, `G` puis `Z` par exemple, suit par défaut les axes du monde : c'est l'orientation *Global*. Dès qu'un élément est incliné, comme la tête d'une lampe tournée vers le plan de travail, ces axes ne correspondent plus à sa forme. Le menu *Transform Orientation* de l'en-tête, ou le menu circulaire `,` (virgule), propose notamment ces repères :
- *Global* : les axes du monde.
- *Local* : les axes propres de l'objet, qui tournent avec lui.
- *Normal* : en Mode Édition, l'axe perpendiculaire à la face ou à l'arête sélectionnée.
- *View* : les axes de l'écran.
- *Cursor* : les axes du curseur 3D.
Un raccourci évite de passer par le menu : appuyer deux fois sur la touche d'axe. Avec l'orientation *Global*, `G Z Z` déplace l'objet le long de son propre axe Z.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/transform_orientation_menu_blender.jpg"
caption: "Figure 1.16 : Le menu Transform Orientation de l'en-tête, avec l'orientation Global active."
title: "Le menu des orientations"
---
La capture montre le menu ouvert depuis le bouton Global de l'en-tête de la vue 3D. Il propose aussi Gimbal et Parent, plus rarement utiles pour un blocage. Le bouton + crée une orientation personnalisée à partir de la sélection.
```

```side-by-side
layout: "textRight"
imagePath: "assets/images/local_orientation_blender.jpg"
caption: "Figure 1.17 : La tête de lampe inclinée, avec le gizmo de déplacement en orientation Local : ses axes suivent l'inclinaison."
title: "Des axes qui suivent l'objet"
---
Sur la capture, la tête de la lampe est inclinée. En orientation Local, la flèche bleue du gizmo pointe dans l'axe de la tête : un déplacement le long de cette flèche l'avance ou la recule sans la décaler de côté.
```

### L'aimantation
L'aimantation (*snapping*) accroche l'élément déplacé à une cible : la grille, un sommet, une arête, une face. Elle s'active avec l'icône d'aimant de l'en-tête ou `Maj + Tab`. Au quotidien, maintenir `Ctrl` pendant un déplacement l'active seulement le temps du geste.

Le menu déroulant à côté de l'aimant règle deux choses. *Snap Target* désigne la cible : *Increment* (le pas de la grille, par défaut), *Vertex*, *Edge*, *Face*, ou encore *Edge Center* et *Face Center* pour viser un milieu. *Snap Base* désigne le point de l'objet déplacé qui vient se poser sur la cible : le plus proche (*Closest*), le centre (*Center*), la moyenne (*Median*) ou l'élément actif (*Active*).

Par exemple, pour centrer une articulation sur l'extrémité d'un bras, choisissez la cible *Face Center* et le point de base *Center*, puis déplacez l'articulation en maintenant `Ctrl` au-dessus de la face du bout du bras.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/snapping_menu_blender.jpg"
caption: "Figure 1.18 : Le menu d'aimantation de l'en-tête, avec la cible Face Center et le point de base Center."
title: "Régler la cible et le point de base"
---
La capture montre le menu déroulé à droite de l'icône d'aimant. La partie haute choisit le point de base, la liste Snap Target choisit la cible. Ce réglage reste actif jusqu'à ce que vous le changiez : pensez à le vérifier quand une aimantation ne tombe pas où vous l'attendiez.
```

> [!TIP]
> Plusieurs cibles peuvent être actives en même temps : `Maj + clic` dans la liste *Snap Target* en ajoute une. Pendant un déplacement, la touche `B` permet aussi de choisir à la volée le point de base de l'aimantation.

### L'édition proportionnelle
L'édition proportionnelle (`O`, ou son bouton dans l'en-tête de la vue 3D) entraîne les éléments voisins de la sélection, avec une influence qui diminue avec la distance. Vous déplacez un sommet, et la surface alentour suit en douceur : de quoi bomber le dessus d'un socle ou galber un capot.

Pendant le geste, la molette agrandit ou réduit le cercle d'influence ; `Maj + O`, ou le menu à droite du bouton, change le profil d'atténuation (doux, linéaire, pointu…). L'outil a besoin de géométrie pour agir : sur un cube à six faces, il n'y a rien à entraîner. Quelques boucles ajoutées avec *Loop Cut* (`Ctrl + R`) lui donnent de la matière.

![Figure 1.19 : Un sommet soulevé avec l'édition proportionnelle : la surface voisine suit en douceur. En haut, le bouton de l'édition proportionnelle, actif, et son menu de profils d'atténuation, ici Smooth.](assets/images/proportional_editing_blender.jpg)

### Des extrusions adaptées à la forme
Au-delà de l'extrusion simple (`E`), le menu `Alt + E` propose des variantes utiles en Mode Édition :
- *Extrude Faces Along Normals* : chaque face avance perpendiculairement à elle-même, pour épaissir une surface courbe.
- *Extrude Individual Faces* : chaque face s'extrude séparément, par exemple pour une série de plots.
- *Extrude Manifold* : en extrudant vers l'intérieur, l'outil découpe et supprime automatiquement les faces voisines, pour creuser proprement un logement ou une rainure.
Une *normale* est la direction perpendiculaire à une face, qui indique son côté extérieur.

```side-by-side
layout: "textLeft"
imagePath: "assets/images/extrude_menu_alt_e_blender.jpg"
caption: "Figure 1.20 : Le menu Extrude, ouvert avec Alt + E en Mode Édition."
title: "Le menu Extrude"
---
La capture montre le menu ouvert avec Alt + E, la grande face de la tête de lampe sélectionnée. Extrude Faces correspond à l'extrusion simple (E) ; les trois entrées suivantes sont les variantes décrites ci-dessus.
```

### Des biseaux mesurés
Le biseau (`Ctrl + B`) se règle avec précision juste après l'opération, dans le panneau *Ajuster la dernière opération* :
- *Width* : la largeur, que vous pouvez saisir avec son unité (`2mm`).
- *Segments* : un segment donne un chanfrein (coupe plate), plusieurs segments un congé arrondi.
- *Profile Shape* : le profil de l'arrondi ; la valeur 0,5 donne un arc de cercle.
- *Clamp Overlap* : empêche des biseaux voisins de se chevaucher.
`Ctrl + Maj + B` biseaute un sommet seul, pour arrondir un coin sans toucher aux arêtes.

```side-by-side
layout: "textRight"
imagePath: "assets/images/bevel_adjust_panel_blender.jpg"
caption: "Figure 1.21 : Le panneau du biseau, rouvert avec F9 : largeur, nombre de segments et profil se règlent au chiffre près."
title: "Régler un biseau après coup"
---
La capture montre le bord du socle biseauté avec une largeur de 4 mm et 4 segments. Le panneau replié en bas à gauche de la vue, ou la touche F9, donne accès aux réglages. Tant qu'aucune autre opération n'a été lancée, chaque valeur reste modifiable : vous passez d'un chanfrein à un congé sans refaire le biseau.
```

> [!WARNING]
> Sur un objet dont l'échelle n'est pas appliquée, un biseau donne des largeurs irrégulières : 2 mm d'un côté, davantage de l'autre. En cas de doute, `Ctrl + A > Scale` avant de biseauter remet les choses d'aplomb.

### Ajuster sans reconstruire
Deux gestes corrigent une forme sans refaire l'opération qui l'a créée :
- `G G` (deux fois `G`) fait **glisser** une arête ou un sommet le long des arêtes voisines : la forme ne se déforme pas, seule la position de la coupe change.
- `Alt + S` (*Shrink/Fatten*) **gonfle ou rétrécit** la sélection le long des normales, pour épaissir ou affiner une zone courbe.

### Mesurer
Pour contrôler une cote, l'outil *Measure* de la barre d'outils, à gauche de la vue, trace une règle : cliquez-glissez d'un point à un autre, en maintenant `Ctrl` pour vous accrocher aux sommets et aux arêtes. Cliquer au milieu de la règle la transforme en rapporteur d'angle.

En Mode Édition, un second menu de superpositions apparaît à droite du menu *Overlays* : *Mesh Edit Mode*. Dans sa rubrique *Measurement*, l'option *Edge Length* affiche en permanence la longueur des arêtes sélectionnées.

```side-by-side
layout: "textRight"
imagePath: "assets/images/measure_tool_ruler_blender.jpg"
caption: "Figure 1.22 : Une règle tracée avec l'outil Measure d'un bord à l'autre du socle : 180 mm, son diamètre."
title: "Tracer une règle"
---
La capture montre une règle tracée avec l'outil Measure, actif dans la barre d'outils, d'un bord à l'autre du dessus du socle, en maintenant Ctrl. Ses extrémités se sont accrochées à deux sommets opposés : la cote, 180 mm, est le diamètre du socle. Elle s'affiche au milieu de la règle, dans l'unité de la scène. La règle reste affichée tant que l'outil est actif : vous pouvez en déplacer les extrémités pour reprendre la mesure.
```

```side-by-side
layout: "textLeft"
imagePath: "assets/images/edge_length_overlay_blender.jpg"
caption: "Figure 1.23 : L'option Edge Length en Mode Édition : la longueur des arêtes sélectionnées s'affiche directement dans la vue."
title: "Lire les cotes dans la vue"
---
La capture montre la tête de la lampe en Mode Édition, avec les quatre arêtes d'une face sélectionnées. Leur longueur s'affiche au milieu de chacune, dans l'unité choisie pour la scène. En haut à droite, la rubrique Measurement du menu Mesh Edit Mode, avec Edge Length cochée. Pendant un déplacement, les valeurs se mettent à jour en direct.
```

> [!CAUTION]
> Bloquez le concept d'une lampe de bureau articulée, qui vous accompagnera jusqu'au chapitre 4. Placez les croquis du fichier d'exercice en images de référence, puis assemblez socle, bras et tête avec des primitives. Cotes indicatives : socle de 180 mm de diamètre, hauteur totale d'environ 450 mm, tête de 120 mm de diamètre. Utilisez l'aimantation pour poser les articulations et l'orientation *Local* pour incliner et avancer la tête. Déclinez ensuite deux variantes, comparez leurs silhouettes, puis enregistrez celle que vous retenez sous `lampe_blocage_v001.blend`. Ces cotes sont un point de départ : libre à vous de les adapter à votre propre concept.

```quiz
question: "La tête de la lampe est inclinée. L'orientation Global est active : comment la déplacer le long de son propre axe Z ?"
options:
  - "G puis Z"
  - "G puis Z puis Z"
  - "G puis Maj + Z"
  - "R puis Z"
correctIndices:
  - 1
explanation: "Un premier appui sur `Z` contraint le déplacement à l'axe Z de l'orientation active, ici **Global**. Un second appui bascule sur l'axe Z **Local**, celui de l'objet incliné. `Maj + Z` exclurait au contraire l'axe Z."
```

```quiz
question: "Pendant un déplacement, quelle touche maintenir pour activer l'aimantation le temps du geste, sans l'allumer dans l'en-tête ?"
options:
  - "Maj"
  - "Ctrl"
  - "Alt"
  - "B"
correctIndices:
  - 1
explanation: "Maintenir **Ctrl** active l'aimantation le temps du geste, avec la cible réglée dans le menu de l'en-tête. La touche `B`, elle, sert à choisir le point de base de l'aimantation pendant le déplacement."
```
