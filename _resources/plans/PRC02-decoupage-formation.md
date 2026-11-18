# PRC02 · Découpage de la formation en 6 demi-journées

Référence validée par le formateur le 18 novembre 2026. Les plans de chapitre de ce dossier doivent la respecter. Les fichiers d'exercice et les ateliers aussi.

## Le calendrier

Chaque demi-journée compte 3 h 30 de contenu, 4 h au maximum, pauses comprises. Elle se déroule en synchrone et en présentiel, pour 5 à 8 apprenants. Les apprenants utilisent Blender 5.2 LTS avec l'interface en anglais.

| Demi-journée | Contenu | Ce que l'apprenant produit |
|---|---|---|
| 1 · Prendre ses repères | Basics 101 en entier ; Basics 102, sections 1, 2 et 4 | Activité A, la maquette en kit |
| 2 · Modéliser | Basics 102, section 3 ; Basics 103 en entier | Activités B et C, puis une passerelle vers la lampe |
| 3 · Chapitre 1 | Environnement de travail, blocage de volumes, transformations précises | Le blocage de la lampe, avec ses variantes |
| 4 · Chapitre 2 | Modificateurs de symétrie, d'épaisseur et de répétition ; courbes de Bézier ; atelier | La lampe remodelée proprement |
| 5 · Chapitre 3 | Principled BSDF, finitions CMF en projection triplanaire, Asset Browser avec Append et Link | La lampe habillée, ses matières rangées en bibliothèque |
| 6 · Chapitre 4 | EEVEE, éclairage de studio et HDRI, caméra et export, atelier final | Les visuels de présentation, puis la galerie et le bilan |

Les demi-journées 1 et 2 forment l'initiation, hors programme officiel. Leur déroulé se trouve dans `_resources/PRC02-deroule-initiation.md`.

Les demi-journées 3 à 6 couvrent les 14 h du programme `_resources/design-visualisation-temps-reel-blender.md` :
- jour 1, « Concept design & modélisation agile » : chapitres 1 et 2 ;
- jour 2, « LookDev & rendu interactif » : chapitres 3 et 4.

## Le fil rouge

Le fil rouge est une lampe de bureau, la même d'un chapitre à l'autre :
1. bloquée au chapitre 1 (`_resources/exercices/PRC02_ch1_blocage_lampe.blend`) ;
2. remodelée au chapitre 2 ;
3. habillée au chapitre 3 ;
4. mise en scène et exportée au chapitre 4.

Le formateur peut retenir une autre piste pour un chapitre. Le changement doit alors être répercuté sur les chapitres suivants.

## Les critères de contrôle d'un plan de chapitre

1. **Durée.** Le minutage tient en 3 h 30 de contenu et 4 h au maximum, pauses comprises.
2. **Périmètre.** Le plan couvre les points du programme et les ancres déclarées dans `lib/core/data/course_data.dart`, sans empiéter sur un autre chapitre :
   - Append et Link appartiennent au chapitre 3 ;
   - EEVEE, l'éclairage et la caméra appartiennent au chapitre 4.
3. **Pas de redite.** Le plan approfondit ce que l'initiation a déjà montré au lieu de le reprendre : Extrude, Bevel, Loop Cut, une première approche des modificateurs, EEVEE, la focale de 50 mm, le format 1920 × 1080.
4. **Continuité.**
   - L'état de la lampe au début du chapitre correspond à celui de la fin du chapitre précédent.
   - Un fichier de départ propre permet de commencer sans le travail de la demi-journée précédente, en cas d'absence, de retard ou de fichier perdu.
5. **Fichiers et ateliers.**
   - Chaque exercice et chaque atelier a un fichier de travail et un corrigé. Le formateur s'appuie sur le corrigé pour savoir où l'on doit aboutir et pour anticiper les questions.
   - **La convention, commune à tous les chapitres.**
     - Le corrigé se trouve dans le fichier de travail, dans une collection masquée (œil fermé) dont le nom commence par « Corrigé ».
     - Le LISEZ-MOI indique en une ligne où le trouver.

     C'est déjà la forme des fichiers livrés pour l'initiation et le chapitre 1, et elle limite le nombre de fichiers à transférer.
   - **Un fichier séparé** n'est prévu que s'il est nécessaire, et il faut le justifier :
     - quand le résultat ne tient pas dans une collection : réglages de rendu, monde, images exportées ;
     - quand le fichier sert aussi de point de départ ou de fichier de secours au chapitre suivant.
   - **Le tableau récapitulatif.** Le plan récapitule ces fichiers dans un tableau : exercice ou atelier, moment du minutage, fichier de travail, emplacement du corrigé.
   - Chaque fichier d'exercice ou d'atelier sert un moment précis du minutage.
   - Chaque fichier s'ouvre seul : ressources empaquetées, chemins relatifs, Blender 5.2 LTS.
   - Les consignes sont graduées par paliers, avec des défis pour ceux qui avancent vite.
6. **Chapitre 4.** Il garde environ 20 à 30 minutes pour la galerie des visuels et le bilan de la formation. Le contenu technique doit donc tenir en 3 h environ.
7. **Progression pédagogique.** Les apprenants ne doivent jamais être perdus. Ils abordent les notions pas à pas, avec une difficulté et une complexité croissantes.
   - **Dans le chapitre :**
     - chaque notion s'appuie sur une notion déjà vue ;
     - une seule notion nouvelle est introduite à la fois ;
     - chaque geste passe de la démonstration à la pratique guidée, puis à la pratique autonome ;
     - l'atelier de fin de chapitre réinvestit les notions du chapitre, sans en introduire de nouvelles.
   - **D'un chapitre à l'autre :**
     - la difficulté monte de la demi-journée 1 à la demi-journée 6 ;
     - les prérequis de chaque chapitre ont tous été vus avant ;
     - aucun chapitre n'exige un geste ou une notion qui n'est expliqué que plus tard.
   - **Charge et repères :**
     - la quantité de notions nouvelles reste raisonnable pour un débutant ;
     - les points de contrôle et les quiz vérifient l'acquis avant de passer à la suite ;
     - chaque chapitre rappelle en ouverture où l'on en est et ce que l'on va construire.

## Les décisions du 18 novembre 2026

Ces décisions ont été prises par le formateur à la relecture des plans des chapitres 2 à 4.

- **Le fil rouge.** La lampe sert de fil rouge jusqu'au bout. La liseuse de cabine, de train ou d'avion, devient un défi ★★ au chapitre 2.
- **Le chapitre 2.**
  - Il garde trois ajouts hors programme : *Screw*, *Shade Auto Smooth* et le parentage.
  - Les bras de la lampe ont deux tiges.
  - Le chapitre compte 5 quiz.
  - Le fichier de démos par secteur est le premier élément coupé en cas de retard.
  - Le *Bevel* se découvre sur le socle, en autonomie. L'ordre de la pile devient une simple remarque.
- **Le chapitre 3.**
  - La case *Raytracing* est cochée dès ce chapitre, pour le verre, avec une phrase d'explication.
  - *Link* est réduit à une phrase, et sa manipulation devient un défi. L'atelier du second coloris est allongé à environ 20 minutes.
  - La bibliothèque déclarée dans les préférences reste une option.
  - Il n'y a pas de mémo des matières imprimé pour l'instant.
- **Le chapitre 4.**
  - Le studio est éclairé par les HDRI livrées avec Blender. Deux HDRI 2K de Poly Haven, sous licence CC0, servent pour l'intérieur et l'extérieur ; leur téléchargement attend l'accord du formateur.
  - Les visuels attendus sont trois vues : héros 16:9, détail 1:1 et situation 16:9.
  - Cycles n'apparaît que dans une image comparative.
- **Les unités.** Afficher les longueurs en millimètres est une recommandation, pas un prérequis : on peut très bien travailler en mètres.
  - L'essentiel est de **saisir chaque valeur avec son unité**, ce qui fonctionne quelle que soit l'unité affichée :
    - dans un champ, on tape `25mm` ;
    - pendant un geste, on tape `G Z = 25mm`. L'unité n'y est lue qu'après `=`, qui ouvre la saisie avancée. Sans `=`, les lettres sont ignorées, et le nombre s'entend dans l'unité affichée.
  - Les plans, les consignes et les LISEZ-MOI donnent donc toujours les valeurs à taper avec leur unité.
  - Les fichiers fournis restent réglés en millimètres : c'est un choix du fichier, pas une exigence envers l'apprenant.
- **Hors périmètre du support : satisfaction et autoévaluation sur les objectifs.** Elles relèvent du questionnaire de satisfaction à chaud de fin de formation, géré en externe par VIV Formation.
  - Le support ne contient donc aucune grille d'autoévaluation (« Je sais… », « Acquis / En cours / À revoir »).
  - Dans le support, la vérification des acquis passe exclusivement par les quiz de l'application, ajoutés avec le module dédié. Ils peuvent se faire ensemble à l'écran en fin de séquence.

## Points de vigilance connus

- **Le chapitre 2 est le plus chargé.** La lampe permet de couvrir tout son programme : symétrie pour le pied, épaisseur pour l'abat-jour, répétition pour une grille d'aération, courbes de Bézier pour le câble et les profils.
- **Le chapitre 1 n'a pas encore de déroulé minuté.** Son contenu est rédigé et validé, mais il n'a pas encore été calé sur 3 h 30.
- **Les fichiers déjà livrés ne sont pas modifiés.** Ils restent tels quels : Basics 101 à 103, activités A, B et C de l'initiation, et `PRC02_ch1_blocage_lampe.blend`. Le formateur les juge bons, et ils portent déjà leur corrigé sous une forme adaptée à des exercices de base. Ce peut être une collection masquée, des formes cibles en orange ou des solutions dans le LISEZ-MOI.
