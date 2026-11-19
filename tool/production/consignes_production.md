# PRC02 · Consignes de production des chapitres 2 à 4

Ces consignes valent pour toutes les sessions qui produisent les contenus des chapitres 2 à 4 : fichiers d'exercice, texte, captures et intégration dans l'application. Elles complètent la référence `_resources/plans/PRC02-decoupage-formation.md` et le plan de votre chapitre.

## L'organisation

- **Une session à la fois.** Les chapitres se produisent l'un après l'autre, dans cet ordre :
  1. le chapitre 2 ;
  2. le chapitre 3 ;
  3. le défi procédural du chapitre 3 ;
  4. le chapitre 4.

  La session principale relit chaque chapitre et le commite avant de lancer le suivant.
- **Les questions vont à la session principale,** par `SendMessage` vers `local_42f4e6d7-b44f-4625-9aae-2f68b20090a5`. N'utilisez jamais `AskUserQuestion` : le formateur dort et a délégué ses décisions à la session principale. Pour un point mineur, appliquez votre recommandation et notez-la dans le plan, avec la mention « par délégation, à confirmer par le formateur ».
- **Ni commit, ni push, ni publication.** La session principale commite après sa relecture. Le push et la publication attendent la relecture du formateur.
- **Les limites du travail :**
  - ne modifiez que les fichiers de votre chapitre, et ne touchez pas aux fichiers d'exercice déjà livrés ;
  - n'écrivez rien en dehors du dépôt et du dossier temporaire de votre session ;
  - ne fermez jamais le Blender ouvert sur le poste, qui porte le serveur MCP, et n'enregistrez rien par-dessus.

## Les règles de contenu

Ce sont celles du formateur, à appliquer sans exception :
- vouvoiement, phrases simples, pas d'emoji ;
- les réglages présentés comme des options, jamais comme des prérequis ;
- des exemples dans les trois secteurs : ferroviaire, automobile et aéronautique ;
- une progression crescendo, une notion nouvelle à la fois : démonstration, puis pratique guidée, puis autonomie ;
- **les unités.** L'affichage en millimètres est recommandé, pas exigé. Toute valeur à taper porte son unité : `25mm` dans un champ, `G Z = 25mm` pendant un geste. Pendant un geste, Blender ne lit l'unité qu'après `=` ;
- **aucune grille d'autoévaluation.** La vérification des acquis passe uniquement par les quiz de l'application ;
- **les corrigés** sont dans le fichier de travail, dans une collection masquée dont le nom commence par « Corrigé ». Un fichier séparé n'existe que s'il est justifié, et le plan donne sa raison ;
- **les captures avant tout.** C'est une formation à un logiciel : chaque menu, bouton ou panneau cité a sa capture, lisible dans l'application. Pour les captures côte à côte, comptez environ 600 × 400 px ; les captures riches en texte passent en pleine largeur. Ne sacrifiez pas les captures pour gagner du temps.
- **l'échelle d'affichage.** La colonne de l'application fait 715 px de large :
  - une figure pleine largeur s'affiche dans 715 × 450 px au plus, à l'échelle min(715/L, 450/H) ;
  - une figure côte à côte s'affiche dans 345 × 300 px au plus, à l'échelle min(345/L, 300/H).

  Toute figure qui montre l'interface doit s'afficher à 0,5 au moins : les libellés des nœuds et les valeurs des champs se lisent sans cliquer. Une image large ne va jamais en côte à côte. Pour un graphe de nœuds, capturez une bande large, nœuds zoomés, et montrez la vue 3D à côté ou dans une autre figure, pas en dessous. Calculez l'échelle de chaque figure avant de rendre la main.
- **les libellés de Blender 5.2.1**, interface en anglais :
  - *Array (Legacy)* pour le modificateur classique ;
  - *Amount* dans le panneau du modificateur *Bevel* ;
  - *Face Cull* ;
  - dans le Shader Editor, *Bump* est sous `Maj + A > Displacement`, *Mapping* sous *Utilities > Vector*, et la sortie du *Noise* s'appelle *Factor*.

## Les fichiers d'exercice

- Construisez-les par scripts rejouables, dans `tool/exercices_chN/`. Lancez Blender en arrière-plan avec `tool/blender/blender_cli.ps1`, qui impose un délai maximal et relance Blender s'il plante :

  ```
  powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 -Script <script.py> [-Blend <fichier.blend>] [-TimeoutSec 900] [-Retries 2] [arguments du script]
  ```
- Si vous utilisez le MCP de Blender et qu'il ne répond plus, lancez `tool/blender/relancer_blender_mcp.ps1`. Il relance Blender sans rien fermer. Ajoutez `-ForceRestart` seulement si le Blender est figé.
- **Les réglages de chaque fichier :**
  - Blender 5.2 LTS, moteur EEVEE ;
  - *Length* en *Millimeters*, *Unit Scale* 1 ;
  - un texte LISEZ-MOI en bas de l'écran ;
  - ressources empaquetées, chemins relatifs, `save_version = 0` ;
  - aucun texte d'extension tierce.
- **Shade Auto Smooth** lie le groupe « Smooth by Angle » depuis l'installation de Blender. Rendez-le local, puis retirez la bibliothèque : `bpy.data.libraries` doit être vide.
- **Contrôle obligatoire après décompression.** Le fichier est compressé en zstd sur plusieurs trames ; lisez-le avec `ZstdDecompressor().stream_reader(..., read_across_frames=True)`, fourni par le Python livré avec Blender. Il ne doit contenir aucun chemin absolu, aucun nom d'utilisateur, aucun `AppData` ni `Program Files`, même dans un tampon de l'explorateur de fichiers. Vous pouvez réutiliser `tool/exercices_ch2_defi/verifier_blend.py`.
- Faites une image de rendu EEVEE de chaque fichier et de chaque corrigé, et regardez-la.
- **Les HDRI du chapitre 4** sont déjà téléchargées depuis Poly Haven, sous licence CC0, dans `tool/exercices_ch4/hdri/` : `artist_workshop_2k.hdr` (Oliksiy Yakovlyev) et `docklands_01_2k.hdr` (Savva Zakharov). Elles ne sont pas suivies par git : empaquetez-les dans les fichiers.
- Les liens de téléchargement suivent ce modèle : `https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/<fichier>`. Pour plusieurs fichiers ou des images, livrez un zip.

## Le texte et l'application

- La source Markdown est `_resources/PRC02-SU-26v01_chapN_<titre>.md`, au format de `writer_guide.md`.
- **Les données de l'application :**
  - les modules vont uniquement dans `lib/core/data/chapterN_data.dart` ;
  - le script `tool/exercices_ch2_defi/md_vers_dart.py` convertit le Markdown en Dart. Adaptez-le ou copiez-le pour votre chapitre ;
  - les identifiants suivent le plan : `chN_secX_title`, et ainsi de suite. Les ancres du programme, dans `course_data.dart`, doivent exister.
- **Avant de rendre la main, vérifiez :**
  - `flutter analyze` : 27 avertissements au plus, tous dus à `material.dart`, déprécié ;
  - `flutter build windows --release` doit réussir ;
  - Flutter se trouve dans `%USERPROFILE%\develop\flutter`.
- **Pour les captures,** utilisez une fenêtre Blender courte, lancée à part, comme pour les fichiers de l'initiation et du défi de modélisation. Si vous simulez des clics, vérifiez qu'aucune autre session n'est en train de capturer : le fichier `tool/production/capture.lock` sert de verrou. Créez-le avant de capturer et supprimez-le après.

## Le compte rendu de fin

Quand vous avez terminé, envoyez à la session principale un message court qui donne :
- ce qui est fait et vérifié : les fichiers et leur contrôle, les captures, `flutter analyze` et la compilation ;
- ce qui reste, s'il reste quelque chose ;
- la liste des fichiers modifiés et créés ;
- les décisions prises par délégation.
