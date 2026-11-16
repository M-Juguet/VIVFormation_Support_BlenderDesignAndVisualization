import '../models/content_module.dart';

const List<ContentModule> basics101Modules = [
  TitleModule(
    id: 'basics101_title',
    title: 'Découverte et prise en main',
  ),
  TitleModule(
    id: 'basics101_sec1_title',
    title: '1. Installation et configuration',
  ),
  TextModule(
    id: 'basics101_sec1_txt1',
    title: 'Télécharger la bonne version',
    content: 'Blender se télécharge gratuitement depuis le site officiel, blender.org. Vous y trouverez deux pistes de téléchargement. La version **LTS** (*Long Term Support*) est une version stabilisée, maintenue sur le long terme : c\'est le choix de la sérénité, idéal en production. La version **récente** apporte les dernières fonctionnalités, au prix d\'une stabilité parfois un peu moindre. Pour suivre cette formation, le plus simple est d\'installer la version utilisée tout au long du parcours afin que votre interface corresponde exactement aux captures et aux libellés présentés.',
  ),
  TextModule(
    id: 'basics101_sec1_txt2',
    title: 'Installer sous Windows',
    content: 'Deux formats d\'installation existent. L\'**installeur** classique (`.msi`) intègre Blender au système comme n\'importe quel logiciel, avec un raccourci dans le menu Démarrer. La version **portable** (`.zip`) ne s\'installe pas : on la décompresse dans un dossier et on lance l\'exécutable directement. Cette seconde option est précieuse lorsqu\'on ne dispose pas des droits administrateur, ou pour transporter Blender sur une clé USB.',
  ),
  TextModule(
    id: 'basics101_sec1_txt3',
    title: 'Premier lancement et fichier de démarrage',
    content: 'Au premier démarrage, un écran d\'accueil (*splash screen*) propose quelques réglages rapides. Une fois passé, vous arrivez sur le **fichier de démarrage** par défaut, qui contient systématiquement trois éléments : un cube, une caméra et une lampe. Ce fichier sert de point de départ neuf à chaque nouveau projet ; vous pourrez plus tard le personnaliser pour qu\'il corresponde à vos habitudes.',
  ),
  TextModule(
    id: 'basics101_sec1_txt4',
    title: 'Configurer les préférences essentielles',
    content: 'Les préférences s\'ouvrent via le menu *Edit > Preferences*. Trois réglages méritent votre attention dès le départ. Dans l\'onglet **Interface**, vous pouvez choisir la **langue** de l\'affichage. Dans l\'onglet **System**, à la rubrique *Cycles Render Devices*, vous sélectionnez le **backend GPU** correspondant à votre carte graphique — CUDA ou OptiX pour une carte NVIDIA, HIP pour une carte AMD, oneAPI pour une puce Intel — puis vous cochez votre carte. Enfin, l\'onglet **Add-ons** permet d\'activer des extensions fournies avec Blender. Les préférences sont enregistrées automatiquement.',
  ),
  SideBySideModule(
    id: 'basics101_sec1_side1',
    title: 'Activer le GPU pour le rendu',
    content: 'La capture montre la rubrique Cycles Render Devices dans l\'onglet System. On y choisit d\'abord le backend adapté à sa carte graphique, puis on coche la carte dans la liste. Sans cette étape, Cycles calcule sur le processeur, bien plus lentement : c\'est l\'un des tout premiers réglages à effectuer.',
    imagePath: 'assets/images/preferences_system_gpu_blender.jpg',
    caption: 'Figure 1.1 : L\'onglet System des préférences, avec la sélection du backend GPU pour Cycles.',
    layout: ContentLayout.textLeft,
  ),
  InfoModule(
    id: 'basics101_sec1_info1',
    type: InfoType.warning,
    text: 'Pensez à activer votre carte graphique dans les préférences avant tout travail de rendu avec Cycles. Si ce réglage est oublié, Cycles utilisera par défaut le processeur (CPU), avec des temps de calcul souvent plusieurs fois plus longs. EEVEE, le moteur temps réel utilisé tout au long de cette formation, s\'appuie quant à lui toujours sur la carte graphique.',
  ),
  InfoModule(
    id: 'basics101_sec1_info2',
    type: InfoType.tip,
    text: 'En contexte professionnel ou pédagogique, privilégiez une version **LTS**. Sa stabilité garantie sur la durée évite les mauvaises surprises liées à un changement de comportement entre deux mises à jour, ce qui est précieux quand plusieurs personnes doivent travailler sur les mêmes fichiers.',
  ),
  QuizModule(
    id: 'basics101_sec1_quiz1',
    question: 'Pourquoi est-il important d\'activer sa carte graphique dans les préférences de Blender ?',
    options: [
      'Pour changer la langue de l\'interface',
      'Pour accélérer fortement les calculs de rendu avec Cycles',
      'Pour pouvoir sauvegarder ses fichiers',
      'Pour afficher le cube de départ',
    ],
    correctIndices: [1],
    explanation: 'Activer le **backend GPU** dans *System > Cycles Render Devices* permet à Cycles de calculer sur la carte graphique plutôt que sur le processeur, ce qui réduit considérablement les temps de rendu.',
  ),
  TitleModule(
    id: 'basics101_sec2_title',
    title: '2. L\'interface : éditeurs, zones et workspaces',
  ),
  TextModule(
    id: 'basics101_sec2_txt1',
    title: 'Tout est éditeur',
    content: 'L\'interface de Blender repose sur un principe simple : l\'écran est divisé en **zones**, et chaque zone contient un **éditeur**. La grande fenêtre centrale est la vue 3D, mais l\'Outliner, l\'éditeur de propriétés ou la *Timeline* sont eux aussi des éditeurs occupant leur propre zone. Comprendre cette logique modulaire est la clé pour ne jamais se sentir perdu : il n\'y a pas de fenêtres flottantes éparpillées, seulement un écran que l\'on découpe à sa guise.',
  ),
  TextModule(
    id: 'basics101_sec2_txt2',
    title: 'L\'en-tête et le sélecteur de type d\'éditeur',
    content: 'Chaque éditeur possède un **en-tête** (*header*), une barre regroupant ses menus et options. Tout à gauche de cet en-tête se trouve une petite icône : c\'est le **sélecteur de type d\'éditeur**. En cliquant dessus, vous transformez la zone courante en n\'importe quel autre éditeur. Une zone affichant la vue 3D peut ainsi devenir un éditeur d\'image, un Outliner ou un Shader Editor en un clic.',
  ),
  SideBySideModule(
    id: 'basics101_sec2_side1',
    title: 'Changer le type d\'un éditeur',
    content: 'La capture met en évidence l\'icône du sélecteur, à l\'extrémité gauche de l\'en-tête. Le menu déroulé révèle la liste des éditeurs disponibles. C\'est ce mécanisme qui rend l\'interface entièrement reconfigurable : chaque zone peut accueillir l\'outil dont vous avez besoin à l\'instant T.',
    imagePath: 'assets/images/editor_type_selector_blender.jpg',
    caption: 'Figure 2.1 : Le sélecteur de type d\'éditeur, en haut à gauche de l\'en-tête d\'une zone.',
    layout: ContentLayout.textRight,
  ),
  TextModule(
    id: 'basics101_sec2_txt3',
    title: 'Diviser, fusionner et redimensionner les zones',
    content: 'Les zones se réorganisent à la souris. Pour **redimensionner**, glissez la bordure entre deux zones. Pour **diviser** une zone en deux, saisissez l\'un de ses coins et tirez vers l\'intérieur. Pour **fusionner**, faites glisser une bordure par-dessus la zone voisine jusqu\'à ce qu\'elle disparaisse. Avec un peu de pratique, on façonne en quelques secondes la disposition idéale pour une tâche donnée.',
  ),
  TextModule(
    id: 'basics101_sec2_txt4',
    title: 'Les workspaces',
    content: 'Plutôt que de tout reconfigurer manuellement, Blender propose des **workspaces** : des dispositions d\'éditeurs préréglées pour chaque grande tâche. Ce sont les onglets alignés tout en haut de la fenêtre — Layout, Modeling, Sculpting, Shading, et ainsi de suite. Passer de l\'un à l\'autre est instantané et ne change rien à la scène : seul l\'agencement de l\'écran évolue. Vous en avez déjà utilisé plusieurs dans cette formation, comme Shading et UV Editing.',
  ),
  InfoModule(
    id: 'basics101_sec2_info1',
    type: InfoType.info,
    text: 'Un workspace n\'est qu\'un **agencement d\'éditeurs**, pas un fichier ni une scène séparée. Quand vous passez de Layout à Shading, vous travaillez toujours sur les mêmes objets : vous changez simplement la disposition des outils affichés à l\'écran. Rien n\'est perdu en basculant d\'un workspace à l\'autre.',
  ),
  QuizModule(
    id: 'basics101_sec2_quiz1',
    question: 'Que se passe-t-il lorsque vous cliquez sur un autre onglet de workspace (par exemple de Layout à Shading) ?',
    options: [
      'Vous ouvrez un nouveau fichier vide',
      'Vous changez l\'agencement des éditeurs à l\'écran, sans modifier la scène',
      'Vous supprimez les objets non sélectionnés',
      'Vous lancez un rendu',
    ],
    correctIndices: [1],
    explanation: 'Un **workspace** est une simple disposition d\'éditeurs préréglée. En changer modifie l\'agencement de l\'écran pour l\'adapter à une tâche, mais la scène et ses objets restent rigoureusement identiques.',
  ),
  TitleModule(
    id: 'basics101_sec3_title',
    title: '3. L\'éditeur de propriétés et l\'Outliner',
  ),
  TextModule(
    id: 'basics101_sec3_txt1',
    title: 'L\'éditeur de propriétés',
    content: 'À droite de l\'écran, l\'**éditeur de propriétés** rassemble la grande majorité des réglages d\'une scène. Une colonne d\'icônes verticale, sur son bord gauche, donne accès à ses différents onglets : *Render* (moteur et qualité), *Output* (sortie), *Scene*, *World* (environnement), *Object* (l\'objet sélectionné), *Modifiers*, *Material*, et d\'autres encore. Cet éditeur est **contextuel** : les onglets proposés dépendent de l\'élément actif. Sélectionner une lampe ou une caméra n\'affiche pas exactement les mêmes onglets qu\'un maillage.',
  ),
  SideBySideModule(
    id: 'basics101_sec3_side1',
    title: 'Les onglets des propriétés',
    content: 'La capture détaille la colonne d\'icônes qui structure l\'éditeur de propriétés. Chaque icône ouvre une catégorie de réglages. Repérer rapidement le bon onglet — la clé à molette pour les modificateurs, la sphère à damier pour les matériaux — fait gagner un temps précieux au quotidien.',
    imagePath: 'assets/images/properties_editor_tabs_blender.jpg',
    caption: 'Figure 3.1 : La colonne d\'onglets de l\'éditeur de propriétés (Render, Output, Object, Material…).',
    layout: ContentLayout.textLeft,
  ),
  TextModule(
    id: 'basics101_sec3_txt2',
    title: 'Lire et modifier une valeur',
    content: 'Les champs numériques de Blender se manipulent de plusieurs façons. Un **clic** simple permet de saisir une valeur précise au clavier. Un **glissé** horizontal sur le champ fait varier la valeur de façon continue, ce qui est pratique pour ajuster à l\'œil. On peut même cliquer-glisser verticalement sur une colonne de plusieurs champs pour les régler d\'un coup. Ces gestes deviennent vite des automatismes.',
  ),
  TextModule(
    id: 'basics101_sec3_txt3',
    title: 'L\'Outliner',
    content: 'En haut à droite, l\'**Outliner** affiche l\'arborescence complète de la scène : les collections, les objets qu\'elles contiennent, et les données rattachées à chaque objet. On y **sélectionne** un élément d\'un clic, on le **renomme** par un double-clic, et on contrôle sa visibilité à l\'aide des icônes en bout de ligne — l\'**œil** pour l\'affichage dans la vue, l\'icône d\'**appareil photo** pour sa présence dans le rendu final.',
  ),
  SideBySideModule(
    id: 'basics101_sec3_side2',
    title: 'L\'Outliner, plan de la scène',
    content: 'La capture présente l\'arborescence de l\'Outliner : les collections regroupent les objets, et chaque objet peut être déplié pour révéler ses données (maillage, matériau…). Les icônes de visibilité à droite de chaque ligne permettent de masquer un élément dans la vue ou de l\'exclure du rendu.',
    imagePath: 'assets/images/outliner_hierarchy_blender.jpg',
    caption: 'Figure 3.2 : L\'Outliner et son arborescence de collections, objets et données.',
    layout: ContentLayout.textRight,
  ),
  TextModule(
    id: 'basics101_sec3_txt4',
    title: 'Le lien contexte, Outliner et propriétés',
    content: 'Ces deux éditeurs ne fonctionnent pas isolément : ils sont reliés par la notion d\'**objet actif**. L\'objet que vous sélectionnez devient l\'objet actif ; l\'Outliner le met en surbrillance, et l\'éditeur de propriétés affiche aussitôt ses réglages. Saisir ce trio — sélection, Outliner, propriétés — est ce qui permet de toujours savoir « sur quoi » l\'on agit, et constitue l\'un des réflexes les plus structurants pour travailler sereinement.',
  ),
  InfoModule(
    id: 'basics101_sec3_info1',
    type: InfoType.tip,
    text: 'Ne confondez pas les deux principales icônes de visibilité de l\'Outliner. L\'**œil** masque ou affiche l\'objet dans la vue 3D, sans rien changer au rendu. L\'icône d\'**appareil photo** contrôle au contraire sa présence dans l\'image finale rendue. Un objet peut donc être visible à l\'écran mais absent du rendu, et inversement.',
  ),
  QuizModule(
    id: 'basics101_sec3_quiz1',
    question: 'Dans l\'Outliner, à quoi sert l\'icône en forme d\'appareil photo placée à côté d\'un objet ?',
    options: [
      'À déplacer l\'objet vers la caméra',
      'À contrôler la présence de l\'objet dans le rendu final',
      'À masquer l\'objet uniquement dans la vue 3D',
      'À renommer l\'objet',
    ],
    correctIndices: [1],
    explanation: 'L\'icône d\'**appareil photo** détermine si l\'objet apparaît dans le **rendu final**. Elle se distingue de l\'**œil**, qui ne gère que la visibilité dans la vue 3D, sans incidence sur l\'image rendue.',
  ),
  TitleModule(
    id: 'basics101_sec4_title',
    title: '4. Naviguer dans la vue 3D',
  ),
  TextModule(
    id: 'basics101_sec4_txt1',
    title: 'Orbiter, faire un panoramique et zoomer',
    content: 'Trois gestes suffisent à se déplacer autour d\'une scène. Le **bouton du milieu de la souris** (la molette pressée) maintenu fait **orbiter** la vue autour du point central. Combiné à la touche `Maj`, il réalise un **panoramique** (déplacement latéral). La rotation de la molette, enfin, **zoome** en avant ou en arrière. Ces trois mouvements forment le socle absolu de toute manipulation : tant qu\'ils ne sont pas devenus naturels, le reste paraît laborieux.',
  ),
  TextModule(
    id: 'basics101_sec4_txt2',
    title: 'Le gizmo de navigation',
    content: 'Pour celles et ceux qui ne disposent pas d\'une souris à trois boutons, un **gizmo de navigation** est affiché en haut à droite de la vue 3D. Il regroupe plusieurs aides : le petit repère d\'axes coloré (cliquer sur un axe aligne instantanément la vue sur lui), une main pour le panoramique, une loupe pour le zoom, et une icône d\'appareil photo pour basculer dans la vue de la caméra. C\'est un filet de sécurité commode quand les raccourcis de souris ne sont pas disponibles.',
  ),
  SideBySideModule(
    id: 'basics101_sec4_side1',
    title: 'Le gizmo de navigation',
    content: 'La capture isole le gizmo et ses commandes : le repère d\'axes pour s\'aligner sur une vue, la main pour le panoramique, la loupe pour le zoom et l\'icône de caméra. Cliquer directement sur les lettres X, Y ou Z du repère est un moyen rapide et sans raccourci d\'obtenir une vue de face, de côté ou de dessus.',
    imagePath: 'assets/images/navigation_gizmo_blender.jpg',
    caption: 'Figure 4.1 : Le gizmo de navigation en haut à droite de la vue 3D.',
    layout: ContentLayout.textLeft,
  ),
  TextModule(
    id: 'basics101_sec4_txt3',
    title: 'Les vues prédéfinies du pavé numérique',
    content: 'Le pavé numérique offre des raccourcis de vue extrêmement efficaces, à mémoriser en priorité :\n- `1` : vue de face ; `Ctrl + 1` : vue de derrière.\n- `3` : vue de droite ; `Ctrl + 3` : vue de gauche.\n- `7` : vue de dessus ; `Ctrl + 7` : vue de dessous.\n- `0` : vue à travers la caméra active.\n- `5` : bascule entre projection perspective et orthographique.\n- `.` (point) : recadre la vue sur l\'objet sélectionné.\nCes raccourcis font gagner un temps considérable dès qu\'on cherche à se positionner précisément.',
  ),
  TextModule(
    id: 'basics101_sec4_txt4',
    title: 'Perspective, orthographique et modes d\'affichage',
    content: 'La touche `5` du pavé numérique bascule entre deux projections. La vue **perspective** imite l\'œil humain : les lignes parallèles convergent au loin, ce qui donne une impression de profondeur. La vue **orthographique** conserve les lignes parallèles, sans déformation de distance, ce qui est idéal pour aligner des objets avec précision. Enfin, le coin supérieur droit de la vue propose quatre **modes d\'affichage** — *Wireframe* (fil de fer), *Solid* (volumes mats), *Material Preview* (aperçu des matériaux) et *Rendered* (rendu réel du moteur) — que vous retrouverez et exploiterez pleinement au chapitre 4, consacré au rendu avec EEVEE.',
  ),
  ResourceModule(
    id: 'basics101_sec4_res1',
    title: 'Mémo de navigation et raccourcis',
    description: 'Fiche de référence récapitulant les gestes de navigation et les raccourcis du pavé numérique, à garder sous la main pendant vos premières heures de pratique.',
    fileName: 'memo_navigation_blender.pdf (0.4 Mo)',
    downloadUrl: 'https://example.com/files/memo-navigation-blender',
  ),
  InfoModule(
    id: 'basics101_sec4_info1',
    type: InfoType.tip,
    text: 'Sur un ordinateur portable dépourvu de pavé numérique ou de souris à trois boutons, activez les options *Emulate Numpad* et *Emulate 3 Button Mouse* dans les préférences (onglet *Input*). La première redirige les chiffres de la rangée principale vers les vues prédéfinies, la seconde remplace le bouton du milieu par une combinaison de touches. Indispensable pour travailler confortablement sur portable.',
  ),
  QuizModule(
    id: 'basics101_sec4_quiz1',
    question: 'Quelle touche du pavé numérique permet de basculer entre vue perspective et vue orthographique ?',
    options: [
      'La touche 0',
      'La touche 1',
      'La touche 5',
      'La touche 7',
    ],
    correctIndices: [2],
    explanation: 'La touche `5` du pavé numérique bascule entre la projection **perspective** (lignes convergentes, impression de profondeur) et la projection **orthographique** (lignes parallèles, idéale pour l\'alignement précis).',
  ),
];

const List<ContentModule> basics102Modules = [
  TitleModule(
    id: 'basics102_title',
    title: 'Manipuler et organiser son travail',
  ),
  TitleModule(
    id: 'basics102_sec1_title',
    title: '1. Sélectionner et transformer les objets',
  ),
  TextModule(
    id: 'basics102_sec1_txt1',
    title: 'Sélectionner dans la vue 3D',
    content: 'Avant d\'agir sur un objet, il faut le sélectionner. Un **clic gauche** sélectionne l\'objet sous le curseur, qui devient alors l\'**objet actif**, signalé par un contour clair. Maintenir `Maj` en cliquant **ajoute ou retire** des objets de la sélection. Pour des sélections multiples rapides, la sélection rectangulaire (touche `B` ou simple glissé) et la sélection circulaire (`C`) sont précieuses. Enfin, `A` sélectionne tout, et `Alt + A` désélectionne tout.\n\nLa distinction entre **sélection** et **objet actif** est importante : on peut avoir plusieurs objets sélectionnés, mais un seul est actif (le dernier cliqué). Certaines opérations s\'appliquent à toute la sélection, d\'autres uniquement à l\'objet actif.',
  ),
  TextModule(
    id: 'basics102_sec1_txt2',
    title: 'Les trois transformations : déplacer, tourner, redimensionner',
    content: 'Toute la manipulation d\'objets repose sur trois actions, associées à trois touches faciles à mémoriser : `G` pour déplacer (*Grab*), `R` pour tourner (*Rotate*) et `S` pour redimensionner (*Scale*). Le principe est toujours le même : on appuie sur la touche, on bouge la souris pour ajuster, puis on **clique gauche pour valider** ou l\'on appuie sur `Échap` (ou clic droit) pour annuler. Ces trois raccourcis sont le geste fondateur de la pratique Blender, à acquérir en tout premier.',
  ),
  SideBySideModule(
    id: 'basics102_sec1_side1',
    title: 'Déplacer, tourner, redimensionner',
    content: 'La capture illustre les trois transformations fondamentales. Une fois la touche pressée, l\'objet suit la souris, et un retour visuel indique la transformation en cours. Ce trio G/R/S, combiné aux contraintes d\'axe vues juste après, couvre l\'immense majorité des manipulations du quotidien.',
    imagePath: 'assets/images/placeholder_grab_rotate_scale_blender.jpg',
    caption: 'Figure 1.1 : Les trois transformations de base appliquées à un objet : déplacer (G), tourner (R), redimensionner (S).',
    layout: ContentLayout.textLeft,
  ),
  TextModule(
    id: 'basics102_sec1_txt3',
    title: 'Contrainte d\'axe et saisie numérique',
    content: 'La vraie puissance de ces transformations vient de deux compléments. Après avoir appuyé sur `G`, `R` ou `S`, presser `X`, `Y` ou `Z` **contraint** le mouvement à l\'axe choisi. Et plutôt que d\'ajuster à la souris, on peut **taper une valeur précise** au clavier. Cette combinaison rend chaque geste exact et reproductible :\n- `G` puis `X` puis `2` puis `Entrée` : déplace l\'objet de 2 mètres le long de l\'axe X.\n- `R` puis `Z` puis `90` puis `Entrée` : effectue une rotation de 90° autour de l\'axe Z.\n- `S` puis `2` puis `Entrée` : double la taille de l\'objet sur tous les axes.\n- `Maj + Z` après `G` : déplace dans le plan XY en **excluant** l\'axe Z.',
  ),
  TextModule(
    id: 'basics102_sec1_txt4',
    title: 'Annuler et refaire',
    content: 'Toute erreur se corrige sans crainte : `Ctrl + Z` annule la dernière action, et `Ctrl + Maj + Z` la rétablit. Ce filet de sécurité permet d\'expérimenter librement. À côté des raccourcis, des **gizmos** interactifs (les poignées colorées des outils Déplacer, Tourner et Redimensionner, dans la barre d\'outils de gauche) offrent une alternative visuelle pour qui préfère la souris au clavier.',
  ),
  InfoModule(
    id: 'basics102_sec1_info1',
    type: InfoType.tip,
    text: 'Prenez tôt l\'habitude de la **saisie numérique** pendant une transformation. Taper `G X 1` est plus rapide et infiniment plus précis que d\'essayer de glisser l\'objet pile au bon endroit. C\'est ce réflexe qui sépare une manipulation approximative d\'un travail rigoureux et propre.',
  ),
  QuizModule(
    id: 'basics102_sec1_quiz1',
    question: 'Comment déplacer un objet d\'exactement 3 mètres le long de l\'axe Y ?',
    options: [
      'G puis 3 puis Entrée',
      'G puis Y puis 3 puis Entrée',
      'S puis Y puis 3 puis Entrée',
      'R puis Y puis 3 puis Entrée',
    ],
    correctIndices: [1],
    explanation: 'On presse `G` (déplacer), puis `Y` pour **contraindre** le mouvement à l\'axe Y, puis on tape `3` et `Entrée` pour la **valeur exacte**. C\'est la combinaison transformation + axe + saisie numérique.',
  ),
  TitleModule(
    id: 'basics102_sec2_title',
    title: '2. Curseur 3D, pivots et opérations courantes',
  ),
  TextModule(
    id: 'basics102_sec2_txt1',
    title: 'Le curseur 3D',
    content: 'Ce petit repère en forme de cible, visible au centre de la scène par défaut, est le **curseur 3D**. Il joue deux rôles. D\'abord, c\'est le **point d\'apparition** des nouveaux objets : tout ce que vous ajoutez se crée là où il se trouve. Ensuite, il peut servir de **point de pivot** pour les transformations. On le déplace avec `Maj + clic droit`, et `Maj + C` le réinitialise au centre du monde (origine).',
  ),
  TextModule(
    id: 'basics102_sec2_txt2',
    title: 'Le point de pivot',
    content: 'Lorsqu\'on tourne ou redimensionne, encore faut-il savoir **autour de quoi**. C\'est le rôle du point de pivot, sélectionnable dans l\'en-tête de la vue 3D. Plusieurs options existent : *Median Point* (le centre de la sélection, par défaut), *Bounding Box Center* (le centre de la boîte englobante), *3D Cursor* (le curseur 3D), *Individual Origins* (chaque objet pivote sur lui-même) et *Active Element* (autour de l\'objet actif). Le même geste de rotation produit des résultats radicalement différents selon ce choix.',
  ),
  SideBySideModule(
    id: 'basics102_sec2_side1',
    title: 'Choisir le point de pivot',
    content: 'La capture montre le menu déroulant des points de pivot. Comprendre cette option évite bien des surprises : une rotation autour du curseur 3D fait tourner les objets « en orbite », tandis qu\'avec Individual Origins chacun pivote sur place. C\'est un réglage à vérifier dès qu\'une rotation ne donne pas l\'effet attendu.',
    imagePath: 'assets/images/pivot_points_blender.jpg',
    caption: 'Figure 2.1 : Le menu de sélection du point de pivot dans l\'en-tête de la vue 3D.',
    layout: ContentLayout.textRight,
  ),
  TextModule(
    id: 'basics102_sec2_txt3',
    title: 'Ajouter, dupliquer et supprimer',
    content: 'On ajoute un élément via le menu **Add** (`Maj + A`) : maillages, lampes, caméras, etc. apparaissent à l\'emplacement du curseur 3D. Pour copier un objet, deux commandes coexistent et ne font pas la même chose. `Maj + D` crée une **copie indépendante** (duplication réelle). `Alt + D` crée une **copie liée**, qui partage les mêmes données que l\'original. Enfin, `X` ou `Suppr` supprime la sélection.',
  ),
  TextModule(
    id: 'basics102_sec2_txt4',
    title: 'Le panneau « Ajuster la dernière opération »',
    content: 'Après la plupart des opérations, un petit panneau apparaît en bas à gauche de la vue (on le rouvre avec `F9`). Il permet de **modifier après coup** les paramètres de l\'action que vous venez d\'effectuer. Vous venez d\'ajouter une sphère ? Ce panneau vous laisse changer son rayon ou son nombre de segments sans la recréer. C\'est un outil de confort majeur, à connaître dès le départ.',
  ),
  SideBySideModule(
    id: 'basics102_sec2_side2',
    title: 'Le panneau F9',
    content: 'La capture montre le panneau ouvert après l\'ajout d\'une primitive, exposant ses paramètres modifiables (rayon, segments, emplacement). Tant qu\'aucune autre action n\'est effectuée, ces réglages restent ajustables : un excellent moyen d\'affiner sans refaire.',
    imagePath: 'assets/images/adjust_last_operation_f9_blender.jpg',
    caption: 'Figure 2.2 : Le panneau Ajuster la dernière opération (F9) après l\'ajout d\'un objet.',
    layout: ContentLayout.textLeft,
  ),
  InfoModule(
    id: 'basics102_sec2_info1',
    type: InfoType.info,
    text: 'Retenez bien la différence entre `Maj + D` et `Alt + D`. La première produit une copie **totalement indépendante** : modifier l\'une n\'affecte pas l\'autre. La seconde crée une copie **liée**, qui partage ses données avec l\'original : modifier la géométrie de l\'une transforme aussi toutes les autres. Ce comportement est au cœur de la notion de données partagées, abordée à la section suivante.',
  ),
  QuizModule(
    id: 'basics102_sec2_quiz1',
    question: 'Quelle commande crée une copie qui partage ses données avec l\'objet d\'origine ?',
    options: [
      'Maj + D (duplication)',
      'Alt + D (duplication liée)',
      'Maj + A (ajouter)',
      'Maj + C (réinitialiser le curseur)',
    ],
    correctIndices: [1],
    explanation: '`Alt + D` crée une **copie liée** qui partage les mêmes données que l\'original : modifier la géométrie de l\'une affecte toutes les copies liées. `Maj + D`, au contraire, produit une copie totalement indépendante.',
  ),
  TitleModule(
    id: 'basics102_sec3_title',
    title: '3. Mode Objet, Mode Édition et données partagées',
  ),
  TextModule(
    id: 'basics102_sec3_txt1',
    title: 'Deux modes pour deux niveaux d\'action',
    content: 'Blender distingue deux modes de travail principaux, que l\'on bascule avec la touche `Tab`. Le **Mode Objet** manipule les objets dans leur ensemble : on les déplace, on les tourne, on les organise les uns par rapport aux autres. Le **Mode Édition** ouvre l\'objet pour en modifier la **géométrie interne** : ses sommets, ses arêtes et ses faces. Le sélecteur de mode, dans l\'en-tête de la vue, indique en permanence où vous vous trouvez.',
  ),
  TextModule(
    id: 'basics102_sec3_txt2',
    title: 'Un aperçu du Mode Édition',
    content: 'En Mode Édition, on choisit ce que l\'on manipule grâce aux touches `1`, `2` et `3` (sommets, arêtes, faces), puis on déplace ces éléments avec les mêmes `G`, `R`, `S` que les objets. Nous n\'entrons pas ici dans la modélisation proprement dite : l\'objectif est seulement de comprendre que c\'est dans ce mode que se sculpte la forme, par opposition au Mode Objet où l\'on agit sur l\'objet entier.',
  ),
  SideBySideModule(
    id: 'basics102_sec3_side1',
    title: 'Mode Objet et Mode Édition',
    content: 'À gauche, en Mode Objet, le cube se manipule comme un bloc unique. À droite, en Mode Édition, sa géométrie est exposée : sommets, arêtes et faces deviennent sélectionnables et modifiables. La touche Tab fait passer de l\'un à l\'autre instantanément.',
    imagePath: 'assets/images/object_vs_edit_mode_blender.jpg',
    caption: 'Figure 3.1 : Un même cube en Mode Objet (à gauche) et en Mode Édition (à droite), sommets visibles.',
    layout: ContentLayout.textRight,
  ),
  TextModule(
    id: 'basics102_sec3_txt3',
    title: 'Objet et données : le concept à ne pas manquer',
    content: 'Voici l\'idée la plus structurante de tout ce chapitre. Un **objet** n\'est qu\'un conteneur qui porte une position, une rotation et une échelle ; il **pointe vers des données** (un *data-block*) qui décrivent réellement son contenu — pour un maillage, ce sont ses sommets et faces. L\'objet et son maillage sont donc deux choses distinctes. C\'est exactement ce que reflète l\'Outliner, où chaque objet peut être déplié pour révéler les données qu\'il contient.',
  ),
  TextModule(
    id: 'basics102_sec3_txt4',
    title: 'Les données partagées',
    content: 'Conséquence directe : **plusieurs objets peuvent pointer vers les mêmes données**. C\'est précisément ce que produit la duplication liée (`Alt + D`). Modifier la géométrie partagée se répercute alors sur tous les objets concernés. Un compteur, affiché à côté du nom des données, indique combien d\'objets les utilisent ; cliquer dessus crée une copie indépendante (*single-user*) pour rompre le partage. Maîtriser cette mécanique évite l\'une des plus grandes confusions du débutant.',
  ),
  InfoModule(
    id: 'basics102_sec3_info1',
    type: InfoType.warning,
    text: 'Ne confondez jamais un **objet** et ses **données**. Renommer un objet ne renomme pas son maillage, et supprimer un objet ne supprime pas forcément ses données si un autre objet les utilise encore. Garder à l\'esprit cette séparation — l\'objet est le contenant, les données sont le contenu — clarifie une grande partie du fonctionnement de Blender.',
  ),
  QuizModule(
    id: 'basics102_sec3_quiz1',
    question: 'Que se passe-t-il si vous modifiez la géométrie d\'un maillage partagé par plusieurs objets (créés via Alt + D) ?',
    options: [
      'Seul l\'objet actif est modifié',
      'Tous les objets partageant ces données sont modifiés',
      'Rien, les données partagées sont verrouillées',
      'Un nouveau fichier est créé',
    ],
    correctIndices: [1],
    explanation: 'Des objets qui **partagent les mêmes données** sont tous affectés par une modification de la géométrie. Pour n\'en modifier qu\'un seul, il faut d\'abord en faire une copie indépendante (single-user) via le compteur d\'utilisateurs.',
  ),
  TitleModule(
    id: 'basics102_sec4_title',
    title: '4. Organiser et sauvegarder son travail',
  ),
  TextModule(
    id: 'basics102_sec4_txt1',
    title: 'Les collections',
    content: 'À mesure qu\'une scène grossit, les **collections** permettent de la ranger, à la manière de dossiers ou de calques. On crée une collection, on y déplace des objets (touche `M`, ou par glissé dans l\'Outliner), et l\'on contrôle sa visibilité dans la vue comme dans le rendu. Une scène bien organisée en collections — par exemple « Décor », « Éclairage », « Sujet » — reste lisible et agréable à manipuler, même avec des dizaines d\'objets.',
  ),
  TextModule(
    id: 'basics102_sec4_txt2',
    title: 'L\'hygiène de nommage',
    content: 'Le réflexe le plus simple et le plus rentable est de **nommer clairement** ses objets dans l\'Outliner (double-clic pour renommer). Une scène où tout s\'appelle « Cube.001 », « Cube.002 » devient vite illisible. Des noms parlants font gagner un temps précieux, à soi-même comme à toute personne qui reprendra le fichier.',
  ),
  TextModule(
    id: 'basics102_sec4_txt3',
    title: 'Sauvegarder un fichier .blend',
    content: 'Le travail se sauvegarde dans un fichier `.blend`, qui contient toute la scène. Quelques pratiques essentielles :\n- `Ctrl + S` enregistre le fichier courant ; `Maj + Ctrl + S` ouvre *Save As* pour enregistrer sous un nouveau nom.\n- Dans la fenêtre *Save As*, un bouton `+` **incrémente** automatiquement le numéro du fichier (projet_001, projet_002…), pour garder un historique de versions.\n- En cas de plantage, Blender conserve des sauvegardes temporaires : on récupère son travail via *File > Recover > Auto Save*.\nPrendre l\'habitude de sauvegarder souvent et par versions met votre travail définitivement à l\'abri.',
  ),
  TextModule(
    id: 'basics102_sec4_txt4',
    title: 'Chemins de fichiers et packing des textures',
    content: 'Point capital, en lien direct avec le travail des matériaux : par défaut, les textures **ne sont pas stockées dans le `.blend`**. Le fichier ne conserve que le **chemin** vers chaque image sur le disque. Déplacer le `.blend` ou l\'envoyer sans les textures rompt ces liens, et les images apparaissent en rose (« texture manquante »). Deux outils du menu *File > External Data* résolvent ce problème : **Make Paths Relative** transforme les chemins en chemins relatifs (les liens survivent tant que tout reste dans le même dossier), et **Pack Resources** **embarque les textures à l\'intérieur du `.blend`** lui-même — l\'étape indispensable avant de partager ou d\'archiver un projet.',
  ),
  SideBySideModule(
    id: 'basics102_sec4_side1',
    title: 'Sécuriser ses textures',
    content: 'La capture montre le menu External Data déroulé. L\'option Pack Resources intègre toutes les textures dans le fichier .blend, garantissant qu\'aucune image ne sera perdue lors d\'un transfert. C\'est le réflexe à adopter systématiquement avant d\'envoyer un projet contenant des matériaux texturés.',
    imagePath: 'assets/images/external_data_pack_blender.jpg',
    caption: 'Figure 4.1 : Le menu File > External Data avec les options Pack Resources et Make Paths Relative.',
    layout: ContentLayout.textLeft,
  ),
  ResourceModule(
    id: 'basics102_sec4_res1',
    title: 'Modèle de projet organisé',
    description: 'Fichier .blend structuré en collections nommées, avec ses textures déjà empaquetées, à utiliser comme point de départ propre pour vos propres projets.',
    fileName: 'modele_projet_organise.blend (5.1 Mo)',
    downloadUrl: 'https://example.com/files/modele-projet-organise',
  ),
  TextModule(
    id: 'basics102_sec4_txt5',
    title: 'Append, Link et fichier de démarrage',
    content: 'Pour réutiliser des éléments d\'un autre fichier, deux commandes existent. **Append** (*File > Append*) importe une **copie** d\'une donnée — un objet, un matériau — dans votre fichier ; elle devient indépendante. **Link** crée au contraire un **lien** vers la donnée d\'origine, qui se met à jour si le fichier source change. Enfin, vous pouvez figer votre propre scène de départ idéale via *File > Defaults > Save Startup File*, pour que chaque nouveau projet démarre selon vos habitudes.',
  ),
  InfoModule(
    id: 'basics102_sec4_info1',
    type: InfoType.challenge,
    text: '**Défi d\'application :** préparez un projet propre de bout en bout. Rangez vos objets dans des collections nommées, donnez des noms clairs à chaque élément, sauvegardez votre travail en plusieurs versions incrémentales, puis empaquetez les textures via *Pack Resources* comme si vous deviez l\'envoyer à un collègue. Vérifiez enfin qu\'aucune texture n\'apparaît en rose : c\'est la garantie d\'un projet réellement transférable.',
  ),
  QuizModule(
    id: 'basics102_sec4_quiz1',
    question: 'Quelle opération garantit qu\'aucune texture ne sera perdue en envoyant votre fichier .blend à quelqu\'un d\'autre ?',
    options: [
      'Renommer les objets dans l\'Outliner',
      'Empaqueter les textures via File > External Data > Pack Resources',
      'Sauvegarder avec Ctrl + S',
      'Passer en Mode Édition',
    ],
    correctIndices: [1],
    explanation: 'Par défaut, le `.blend` ne stocke que les chemins vers les textures. **Pack Resources** intègre les images directement dans le fichier, ce qui garantit qu\'elles voyageront avec lui et n\'apparaîtront pas en rose chez le destinataire.',
  ),
];

const List<ContentModule> basics103Modules = [
  TitleModule(
    id: 'basics103_title',
    title: 'Bases de la modélisation',
  ),
  TitleModule(
    id: 'basics103_sec1_title',
    title: '1. Le maillage et le Mode Édition',
  ),
  TextModule(
    id: 'basics103_sec1_txt1',
    title: 'L\'anatomie d\'un maillage',
    content: 'Tout objet modélisé dans Blender est un **maillage** (*mesh*), constitué de trois éléments fondamentaux. Les **sommets** (*vertices*) sont des points dans l\'espace. Les **arêtes** (*edges*) sont les segments qui relient deux sommets. Les **faces** sont les surfaces délimitées par des arêtes, le plus souvent par trois ou quatre d\'entre elles. Modéliser, ce n\'est rien d\'autre que manipuler ces trois éléments — les déplacer, en ajouter, en supprimer — pour façonnage d\'une forme.',
  ),
  TextModule(
    id: 'basics103_sec1_txt2',
    title: 'Entrer et sortir du Mode Édition',
    content: 'La sculpture de la géométrie se fait dans le **Mode Édition**. On y bascule depuis le Mode Objet avec la touche `Tab`, et l\'on en ressort de la même façon. Le rappel est utile : le Mode Objet manipule l\'objet dans son ensemble, tandis que le Mode Édition ouvre son maillage pour en modifier l\'intérieur. Le sélecteur de mode, dans l\'en-tête de la vue, indique toujours où vous vous trouvez.',
  ),
  TextModule(
    id: 'basics103_sec1_txt3',
    title: 'Les trois modes de sélection',
    content: 'Une fois en Mode Édition, un choix s\'impose : sur quel type d\'élément voulez-vous agir ? Trois boutons dans l\'en-tête, accessibles par les touches `1`, `2` et `3`, basculent entre les modes de sélection.',
  ),
  SideBySideModule(
    id: 'basics103_sec1_side1',
    title: 'Sommets, arêtes, faces',
    content: 'La capture montre les trois boutons de l\'en-tête. La touche `1` active la sélection par **sommets**, la `2` par **arêtes** et la `3` par **faces**. On passe de l\'un à l\'autre en permanence selon l\'opération : sélectionner une boucle d\'arêtes pour la biseauter, une face pour l\'extruder, un sommet pour l\'ajuster finement.',
    imagePath: 'assets/images/placeholder_select_modes_blender.jpg',
    caption: 'Figure 1.1 : Les trois modes de sélection en Mode Édition — Sommets, Arêtes, Faces.',
    layout: ContentLayout.textRight,
  ),
  TextModule(
    id: 'basics103_sec1_txt4',
    title: 'Sélectionner efficacement en édition',
    content: 'Le Mode Édition offre des méthodes de sélection bien plus riches que le simple clic. Les maîtriser fait gagner un temps considérable :\n- **Clic** pour sélectionner, `Maj + clic` pour ajouter ou retirer, boîte (`B`) et cercle (`C`) pour des sélections multiples.\n- `Alt + clic` sur une arête sélectionne toute la **boucle d\'arêtes** (*edge loop*) qui en fait le tour — l\'outil le plus rentable de l\'édition.\n- `Ctrl + Alt + clic` sélectionne l\'**anneau** (*edge ring*) perpendiculaire.\n- `L` sélectionne tout l\'**îlot** connecté sous le curseur.\n- `Ctrl + Pavé +` et `Ctrl + Pavé -` **agrandissent** ou **réduisent** la sélection de proche en proche.',
  ),
  InfoModule(
    id: 'basics103_sec1_info1',
    type: InfoType.tip,
    text: 'Le raccourci `Alt + clic` pour sélectionner une boucle d\'arêtes complète est sans doute le geste le plus rentable du Mode Édition. Plutôt que de cliquer une à une les dizaines d\'arêtes qui font le tour d\'un cylindre, un seul `Alt + clic` les sélectionne toutes d\'un coup. À intégrer dès vos premières manipulations.',
  ),
  QuizModule(
    id: 'basics103_sec1_quiz1',
    question: 'En Mode Édition, quel raccourci permet de sélectionner d\'un coup toute une boucle d\'arêtes qui fait le tour d\'une forme ?',
    options: [
      'Un clic simple',
      'Alt + clic sur une arête',
      'La touche B',
      'La touche 3',
    ],
    correctIndices: [1],
    explanation: '`Alt + clic` sur une arête sélectionne l\'ensemble de la **boucle d\'arêtes** (*edge loop*). C\'est l\'un des gestes les plus efficaces de la modélisation, qui évite de sélectionner les arêtes une par une.',
  ),
  TitleModule(
    id: 'basics103_sec2_title',
    title: '2. Les outils de modélisation essentiels',
  ),
  TextModule(
    id: 'basics103_sec2_txt1',
    title: 'Partir d\'une primitive',
    content: 'On ne modélise presque jamais à partir de rien : on part d\'une **primitive** — un cube, un cylindre, un plan — que l\'on ajoute via le menu *Add* (`Maj + A`), puis que l\'on façonne progressivement. Cette approche, dite « modélisation par boîte » (*box modeling*), consiste à partir d\'une forme simple et à la sculpter avec les outils d\'édition jusqu\'à obtenir l\'objet voulu.',
  ),
  ResourceModule(
    id: 'basics103_sec2_res1',
    title: 'Scène d\'exercices - Primitives',
    description: 'Fichier contenant plusieurs primitives de départ et quelques formes cibles à reproduire, pour vous entraîner aux outils d\'édition de cette section.',
    fileName: 'exercices_modelisation_primitives.blend (3.6 Mo)',
    downloadUrl: 'https://example.com/files/exercices-modelisation-primitives',
  ),
  TextModule(
    id: 'basics103_sec2_txt2',
    title: 'Extrude : l\'outil fondamental',
    content: 'L\'**extrusion** (`E`) est l\'outil de modélisation par excellence. Il tire de la nouvelle géométrie à partir d\'une sélection : une face extrudée engendre un volume, une arête extrudée prolonge une surface. On appuie sur `E`, on déplace la souris, puis on clique pour valider. C\'est ainsi que l\'on fait pousser un objet, face après face.',
  ),
  SideBySideModule(
    id: 'basics103_sec2_side1',
    title: 'L\'extrusion',
    content: 'Sur la capture, une face sélectionnée est extrudée vers le haut : Blender crée de nouvelles arêtes reliant la face d\'origine à sa copie déplacée, formant un volume. Répéter cette opération dans différentes directions est la base de la construction d\'un objet complexe à partir d\'une simple primitive.',
    imagePath: 'assets/images/placeholder_extrude_tool_blender.jpg',
    caption: 'Figure 2.1 : Extrusion d\'une face pour créer un nouveau volume.',
    layout: ContentLayout.textLeft,
  ),
  TextModule(
    id: 'basics103_sec2_txt3',
    title: 'Inset et Bevel',
    content: 'Deux outils affinent les faces et les arêtes. L\'**Inset** (`I`) crée une face plus petite à l\'intérieur d\'une face existante, idéale pour préparer un renfoncement ou un bouton. Le **Bevel** (`Ctrl + B`) chanfreine ou arrondit une arête vive ; en faisant tourner la molette pendant l\'opération, on ajoute des segments pour passer d\'un simple chanfrein à un arrondi lisse.',
  ),
  TextModule(
    id: 'basics103_sec2_txt4',
    title: 'Loop Cut et Subdivide',
    content: 'Pour ajouter de la résolution là où on en a besoin, deux outils s\'imposent. Le **Loop Cut** (`Ctrl + R`) insère une boucle d\'arêtes continue tout autour du maillage, ce qui permet de le plier ou de le détailler à cet endroit précis. La **Subdivision** (*Subdivide*) découpe les faces sélectionnées en plusieurs, augmentant la densité localement.',
  ),
  TextModule(
    id: 'basics103_sec2_txt5',
    title: 'Fusionner et couper',
    content: 'Enfin, deux outils complètent la panoplie de base. Le **Merge** (`M`) fusionne plusieurs sommets en un seul, utile pour refermer une forme ou nettoyer une géométrie. Le **couteau** (*Knife*, `K`) permet de tracer des découpes personnalisées directement sur la surface.',
  ),
  InfoModule(
    id: 'basics103_sec2_info1',
    type: InfoType.warning,
    text: 'Piège classique de l\'extrusion : après avoir appuyé sur `E`, si vous annulez le déplacement avec `Échap` ou un clic droit, l\'extrusion **n\'est pas annulée** — seul le déplacement l\'est. La nouvelle géométrie reste alors superposée exactement sur l\'ancienne, créant des faces en double invisibles. Pour tout annuler, utilisez plutôt `Ctrl + Z`.',
  ),
  InfoModule(
    id: 'basics103_sec2_info2',
    type: InfoType.tip,
    text: 'Après un Bevel ou une Subdivision, pensez au panneau **« Ajuster la dernière opération » (`F9`)** vu dans Basics 102 : il vous laisse régler après coup le nombre de segments ou de coupes, sans refaire l\'opération.',
  ),
  QuizModule(
    id: 'basics103_sec2_quiz1',
    question: 'Quel outil permet de faire pousser un nouveau volume à partir d\'une face sélectionnée ?',
    options: [
      'L\'Inset (I)',
      'L\'Extrude (E)',
      'Le Loop Cut (Ctrl + R)',
      'Le Merge (M)',
    ],
    correctIndices: [1],
    explanation: 'L\'**Extrude** (`E`) tire de la nouvelle géométrie à partir de la sélection : une face extrudée engendre un volume. C\'est l\'outil fondamental de la modélisation.',
  ),
  TitleModule(
    id: 'basics103_sec3_title',
    title: '3. La modélisation non destructive : les modificateurs',
  ),
  TextModule(
    id: 'basics103_sec3_txt1',
    title: 'Le principe de la pile',
    content: 'Un **modificateur** applique un effet sur le maillage **sans en altérer la géométrie de base**. On les gère dans l\'onglet *Modifiers* de l\'éditeur de propriétés (icône de clé à molette), où ils s\'empilent en une **pile** (*stack*) évaluée de haut en bas. L\'atout est double : le maillage d\'origine reste modifiable à tout moment sous le modificateur, et l\'on peut régler ou retirer l\'effet quand on veut. C\'est le pendant, en modélisation, de la retouche non destructive vue au compositing.',
  ),
  SideBySideModule(
    id: 'basics103_sec3_side1',
    title: 'Le modificateur Subdivision Surface',
    content: 'À gauche de l\'illustration, le maillage de base (une simple cage cubique) reste modifiable ; à droite, le modificateur Subdivision Surface l\'affiche lissé et arrondi. On sculpte la cage grossière, et le modificateur se charge du lissage en temps réel — l\'essence même de la modélisation non destructive.',
    imagePath: 'assets/images/placeholder_subdivision_surface_blender.jpg',
    caption: 'Figure 3.1 : Un cube avec un modificateur Subdivision Surface, lissé en forme arrondie.',
    layout: ContentLayout.textRight,
  ),
  TextModule(
    id: 'basics103_sec3_txt2',
    title: 'Les modificateurs clés de la modélisation',
    content: 'Quelques modificateurs reviennent en permanence et méritent d\'être connus dès le départ :\n- **Subdivision Surface** : lisse et arrondit le maillage en ajoutant de la résolution (raccourci `Ctrl + 1`, `Ctrl + 2`…). C\'est le modificateur roi pour les formes douces.\n- **Mirror** : modélise une moitié et reflète automatiquement l\'autre selon un axe. On divise le travail par deux et l\'on garantit une symétrie parfaite.\n- **Array** : répète l\'objet en copies régulières, parfait pour une clôture, un escalier ou une rangée.\n- **Solidify** : donne une épaisseur à une surface plane, transformant un plan en volume.\n- **Bevel** (modificateur) : arrondit globalement toutes les arêtes vives, sans avoir à les biseauter une à une.\n- **Boolean** : combine, soustrait ou intersecte deux objets, pour percer un trou ou fusionner des formes.',
  ),
  TextModule(
    id: 'basics103_sec3_txt3',
    title: 'L\'ordre compte, et l\'application',
    content: 'Dans la pile, **l\'ordre des modificateurs change le résultat**. Un Mirror placé avant une Subdivision Surface ne produit pas le même effet que l\'inverse : chaque modificateur agit sur le résultat du précédent. On peut, à tout moment, activer ou désactiver leur affichage dans la vue. Et lorsqu\'on a besoin de figer l\'effet en véritable géométrie — pour l\'exporter ou continuer à l\'éditer manuellement — on **applique** le modificateur.',
  ),
  InfoModule(
    id: 'basics103_sec3_info1',
    type: InfoType.info,
    text: 'Tant qu\'un modificateur n\'est pas appliqué, tous ses réglages restent modifiables : niveau de subdivision, axe de miroir, nombre de copies d\'un Array… C\'est cette souplesse qui fait tout l\'intérêt de l\'approche non destructive. N\'appliquez un modificateur que lorsque vous êtes certain de ne plus vouloir revenir sur ses paramètres.',
  ),
  QuizModule(
    id: 'basics103_sec3_quiz1',
    question: 'Quel est le principal avantage de la modélisation par modificateurs ?',
    options: [
      'Elle rend le maillage impossible à modifier',
      'Elle applique des effets sans altérer le maillage de base, réglables à tout moment',
      'Elle supprime automatiquement les sommets en double',
      'Elle ne fonctionne qu\'en Mode Objet',
    ],
    correctIndices: [1],
    explanation: 'Les modificateurs sont **non destructifs** : ils appliquent leurs effets par-dessus le maillage de base, qui reste intact et modifiable. Leurs réglages restent ajustables tant qu\'on ne les a pas appliqués.',
  ),
  TitleModule(
    id: 'basics103_sec4_title',
    title: '4. Topologie, normales et bonnes pratiques',
  ),
  TextModule(
    id: 'basics103_sec4_txt1',
    title: 'Quads, triangles et n-gons',
    content: 'Une face peut avoir un nombre variable de côtés. Une face à quatre côtés est un **quad**, à trois un **triangle** (*tri*), à pics ou plus un **n-gon**. La règle d\'or de la modélisation propre est de **privilégier les quads** : ils se subdivisent proprement, se déforment bien et se déplient plus facilement en UV. Les triangles et n-gons sont tolérables sur des surfaces planes, mais à éviter sur les zones courbes ou destinées à être lissées, où ils provoquent des artefacts.',
  ),
  TextModule(
    id: 'basics103_sec4_txt2',
    title: 'Une topologie propre',
    content: 'La **topologie** désigne la manière dont les faces s\'organisent sur la surface. Une bonne topologie présente un flux de quads régulier, dont les boucles d\'arêtes suivent naturellement les formes de l\'objet. Ce n\'est pas qu\'une question d\'esthétique : une topologie propre conditionne la qualité du lissage, la facilité du dépliage UV et le bon comportement lors des déformations.',
  ),
  TextModule(
    id: 'basics103_sec4_txt3',
    title: 'Les normales',
    content: 'Chaque face possède une **normale** : un vecteur qui indique le côté vers lequel elle est orientée, son « extérieur ». Quand une normale est inversée (elle pointe vers l\'intérieur), la face réagit mal à la lumière et produit des erreurs de rendu — zones sombres, reflets incohérents. On corrige cela avec **Recalculate Outside** (`Maj + N`), qui réoriente toutes les normales vers l\'extérieur. L\'overlay *Face Orientation* aide à repérer le problème : les faces correctes apparaissent en bleu, les inversées en rouge.',
  ),
  SideBySideModule(
    id: 'basics103_sec4_side1',
    title: 'Vérifier les normales',
    content: 'La capture montre un objet sous l\'overlay Face Orientation : les faces bleues sont correctement orientées vers l\'extérieur, les rouges ont leur normale inversée. Un simple `Maj + N` recalcule l\'ensemble vers l\'extérieur. Des normales saines sont indispensables à un shading correct, comme vous le verrez au chapitre 3 consacré aux matières.',
    imagePath: 'assets/images/placeholder_face_orientation_blender.jpg',
    caption: 'Figure 4.1 : L\'overlay Face Orientation — faces correctes en bleu, normales inversées en rouge.',
    layout: ContentLayout.textLeft,
  ),
  TextModule(
    id: 'basics103_sec4_txt4',
    title: 'Le point d\'origine et l\'application des transformations',
    content: 'Deux notions d\'hygiène ferment ce chapitre. Le **point d\'origine** (le petit point orange de l\'objet) sert de référence à sa position, sa rotation et son échelle ; on peut le repositionner via *Object > Set Origin*. Surtout, il faut **appliquer les transformations** avec `Ctrl + A` — l\'échelle en particulier. Un objet dont l\'échelle n\'a pas été appliquée conserve une déformation cachée qui perturbe de nombreux outils en aval.',
  ),
  TextModule(
    id: 'basics103_sec4_txt5',
    title: 'La checklist des bonnes pratiques',
    content: 'Avant de considérer un objet comme « terminé », prenez le réflexe de vérifier ces points :\n- La géométrie privilégie les **quads**, surtout sur les zones courbes.\n- Les **normales** sont recalculées vers l\'extérieur (`Maj + N`).\n- L\'**échelle est appliquée** (`Ctrl + A > Scale`), affichant des valeurs de 1,000.\n- Le **point d\'origine** est placé de façon cohérente (souvent au centre ou à la base de l\'objet).\n- Les éventuels **sommets en double** ont été fusionnés (*Merge by Distance*).\nCette hygiène évite l\'écrasante majorité des problèmes rencontrés plus tard.',
  ),
  InfoModule(
    id: 'basics103_sec4_info1',
    type: InfoType.info,
    text: '**Appliquez toujours l\'échelle** (`Ctrl + A > Scale`) avant de déplier les UV ou d\'ajouter un Bevel. Une échelle non appliquée fausse la taille des textures, produit des biseaux d\'épaisseur irrégulière et perturbe les simulations physiques. C\'est l\'erreur numéro un du débutant, et elle a des répercussions directes sur la modélisation non destructive du chapitre 2 (biseaux, épaisseur) et sur les projections de matières du chapitre 3.',
  ),
  InfoModule(
    id: 'basics103_sec4_info2',
    type: InfoType.challenge,
    text: '**Défi d\'application :** modélisez un objet simple à partir d\'une primitive — un mug, une table basse ou une clé USB. Imposez-vous d\'y appliquer toutes les bonnes pratiques : rester en quads autant que possible, recalculer les normales, appliquer l\'échelle et placer un point d\'origine cohérent. Vous obtiendrez un objet réellement prêt à être texturé et rendu dans la suite de la formation.',
  ),
  QuizModule(
    id: 'basics103_sec4_quiz1',
    question: 'Pourquoi faut-il appliquer l\'échelle (Ctrl + A) avant de déplier les UV ou d\'ajouter un Bevel ?',
    options: [
      'Pour supprimer l\'objet de la scène',
      'Parce qu\'une échelle non appliquée fausse les textures et les biseaux',
      'Pour changer la couleur de l\'objet',
      'Cela n\'a aucune importance',
    ],
    correctIndices: [1],
    explanation: 'Une échelle non appliquée conserve une déformation cachée qui **fausse la taille des textures et l\'épaisseur des biseaux**. Appliquer l\'échelle (`Ctrl + A > Scale`) remet ces valeurs à 1,000 et garantit un comportement correct en aval.',
  ),
];

// ---------------------------------------------------------------------------
// Chapitres de la formation PRC02 — contenus à rédiger.
// Sources Markdown attendues dans `_resources/` (voir writer_guide.md).
// Tant qu'une liste est vide, le chapitre s'affiche « en préparation ».
// ---------------------------------------------------------------------------

const List<ContentModule> chapter1Modules = [];

const List<ContentModule> chapter2Modules = [];

const List<ContentModule> chapter3Modules = [];

const List<ContentModule> chapter4Modules = [];
