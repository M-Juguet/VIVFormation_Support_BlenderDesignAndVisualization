# Initiation à Blender : déroulé formateur

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Deux demi-journées en présentiel, de 5 à 8 apprenants · Version du 17 novembre 2026

## En bref

- **Objectif :** à la fin de l'initiation, chaque apprenant navigue sans se perdre et place un objet au chiffre près. Il range et enregistre son fichier, puis modélise un objet simple par extrusion et modificateurs. Il aborde ainsi le chapitre 1 sans buter sur les gestes de base.
- **Format :** 2 demi-journées de 3 h 40, pauses comprises. Chacune compte 3 h 20 de contenu et 2 pauses de 10 minutes, ce qui laisse environ 20 minutes de marge sur 4 heures. Exemple : de 9 h 00 à 12 h 40.
- **Principe :** une démo de 10 minutes au plus, un geste guidé, puis un réinvestissement. Les apprenants ne passent jamais plus de 15 minutes sans toucher la souris.
- **Fil conducteur :** trois activités dans le logiciel, liées au design de transport. En demi-journée 1, la maquette en kit ; en demi-journée 2, la rangée de sièges et la clinique du fichier.

### Répartition des Basics

| | Demi-journée 1 · Prendre ses repères | Demi-journée 2 · Modéliser |
|---|---|---|
| Basics | 101 en entier ; 102 § 1, 2 et 4 | 102 § 3 ; 103 en entier |
| Notions | Interface, Outliner et propriétés, navigation, sélection, transformations, curseur 3D, copies, collections, sauvegarde | Mode Édition, objet et données, Extrude, Inset, Bevel, Loop Cut, modificateurs, normales, échelle, origine |
| Activités | A · La maquette en kit (45 min) | B · La rangée de sièges (50 min) ; C · La clinique du fichier (25 min) |

Le § 3 de Basics 102 (objet et données, Mode Édition) passe en demi-journée 2. C'est la porte d'entrée de la modélisation, et l'activité A le prépare : ses roues sont des copies liées.

### Ce que l'on survole

Ces contenus restent dans l'application : les apprenants les retrouvent au besoin.
- L'installation et les préférences GPU : Blender est déjà installé, et Cycles ne sert pas dans cette formation.
- La visite de l'interface menu par menu : une chasse aux réglages la remplace.
- Append et Link : ils reviennent avec l'Asset Browser au chapitre 3.
- Knife, Merge, quads et n-gons : une phrase chacun, au moment où ils servent.

### Les fichiers

| Fichier | Moment | Contenu |
|---|---|---|
| `memo_navigation_blender.pdf` | DJ1, navigation | Mémo A4 paysage, à imprimer pour chaque apprenant |
| `PRC02_ch1_blocage_lampe.blend` | DJ1, navigation ; DJ2, passerelle | Le blocage de la lampe du chapitre 1 |
| `PRC02_init_maquette_en_kit.blend` | DJ1, activité A | Trois véhicules en vrac et leurs gabarits |
| `modele_projet_organise.blend` | DJ1, organiser | Démo de Pack Resources (textures empaquetées) |
| `exercices_modelisation_primitives.blend` | DJ2, outils d'édition | Exercices 1 à 4 et défi Boîtier |
| `PRC02_init_rangee_sieges.blend` | DJ2, activité B | Le siège de départ, la cabine et le corrigé masqué |
| `PRC02_init_clinique_fichier.blend` | DJ2, activité C | Cinq pièces à soigner, chacune avec sa jumelle saine |

Tous ces fichiers se trouvent dans `_resources/exercices/`. Chaque fichier d'activité s'ouvre sur un texte LISEZ-MOI en bas de l'écran, avec les consignes par paliers ; `Ctrl + Espace` l'agrandit.

> **À savoir :** les trois fichiers `PRC02_init_…` ne sont pas reliés à l'application. Distribuez-les par clé USB ou dossier partagé. Une fois poussés sur la branche `main` du dépôt, ils sont aussi téléchargeables à l'adresse `https://raw.githubusercontent.com/M-Juguet/VIVFormation_Support_BlenderDesignAndVisualization/main/_resources/exercices/` suivie du nom du fichier.

## Avant la première demi-journée

### Les postes des apprenants

- [ ] Blender 5.2 LTS est installé et a été ouvert une fois.
- [ ] Une souris à trois boutons (molette cliquable) est branchée. Avec un pavé tactile, Blender devient vite pénible.
- [ ] Sur un portable sans pavé numérique, *Emulate Numpad* est à activer à l'accueil (*Edit > Preferences > Input*).
- [ ] L'application support v0.1.0 est installée.
- [ ] Les fichiers d'exercice sont copiés dans un dossier de travail.

### Votre poste de démonstration

- **Lancez Blender en configuration d'usine pour vos démos**, avec un raccourci Windows vers `blender.exe --factory-startup`. Votre Blender habituel a le bouton du milieu réglé sur *Pan* et des onglets d'extensions (BlenderKit, Geo-Scatter…). En configuration d'usine, ce que vous montrez correspond exactement à l'écran des apprenants. Vos préférences ne sont pas touchées : dans ce mode, Blender n'enregistre rien en quittant. Évitez seulement le bouton *Save Preferences*.
- **Agrandissez l'interface pour le vidéoprojecteur** : *Edit > Preferences > Interface > Resolution Scale*, par exemple à 1,3. En configuration d'usine, ce réglage est à refaire à chaque lancement.
- **Testez le vidéoprojecteur** avec le fichier de la maquette en kit : le fil de fer du gabarit doit rester lisible.

### Le matériel de la salle

- Le mémo de navigation imprimé, un par apprenant.
- Des post-it de deux couleurs, vert et rose, pour les points de contrôle (voir « Animer »).
- Un paperboard pour les raccourcis du jour.
- Un minuteur visible de tous pour les phases en autonomie.

## Demi-journée 1 · Prendre ses repères

Basics 101 et 102 (§ 1, 2 et 4). Les apprenants repartent avec une maquette remontée, rangée et enregistrée.

| Horaire | Durée | Séquence | Modalité |
|---|---|---|---|
| 0:00 | 15 min | Accueil et lancement | Collectif |
| 0:15 | 25 min | L'interface en trois idées | Démo 10 min + chasse aux réglages 15 min |
| 0:40 | 25 min | Naviguer | Démo 10 min + défi des vues 15 min |
| 1:05 | 10 min | Pause | |
| 1:15 | 40 min | Sélectionner et transformer | Démo 15 min + pratique guidée 25 min |
| 1:55 | 45 min | Activité A · La maquette en kit | Autonomie |
| 2:40 | 10 min | Pause | |
| 2:50 | 30 min | Organiser et sauvegarder | Démo 10 min + pratique guidée 20 min |
| 3:20 | 20 min | Galerie et bilan | Collectif |

### 0:00 · Accueil et lancement (15 min)

- **Tour de table en trois questions :**
  - votre secteur ;
  - les outils 3D ou de CAO que vous pratiquez (Alias, CATIA, Rhino, KeyShot, Gravity Sketch…) ;
  - Blender : jamais ouvert, un peu, ou régulièrement.
- **Formez les binômes** d'après les réponses. Chaque débutant complet s'assoit à côté d'une personne plus à l'aise : son copilote.
- **Annoncez le résultat attendu :** « Dans deux demi-journées, vous saurez remonter, ranger et modéliser un objet simple. »
- **Faites le contrôle technique.** Sur chaque poste, Blender 5.2 est ouvert et la souris est branchée. Sur les portables sans pavé numérique, *Emulate Numpad* est activé.
- **Montrez l'application support :** les Basics y sont rédigés, avec des quiz. « Pendant la séance, gardez les yeux sur Blender. L'application sert après. »

### 0:15 · L'interface en trois idées (25 min)

**Vous montrez (10 min),** d'après Basics 101 § 2 et 3 :
1. Tout est éditeur : avec le sélecteur de type d'éditeur, changez la Timeline en Outliner, puis remettez-la. Divisez une zone, puis refusionnez-la.
2. Les workspaces : passez de *Layout* à *Shading*, puis revenez. La scène ne change pas.
3. Le trio sélection, Outliner et propriétés : cliquez la lampe dans la vue, puis la caméra dans l'Outliner. L'éditeur de propriétés suit.

**Ils font (15 min) : la chasse aux réglages.** Sur la scène de démarrage (*File > New > General*), ils cherchent :
1. la puissance de la lampe ;
2. la focale de la caméra ;
3. le moteur de rendu actif ;
4. la résolution de l'image de sortie.

Ensuite, ils renomment le cube « Gabarit » dans l'Outliner. Ils masquent la lampe avec l'œil et excluent la caméra du rendu avec l'icône d'appareil photo.

**Point de contrôle :** les réponses à voix haute : 1000 W, 50 mm, EEVEE, 1920 × 1080. Faites remarquer que le maillage du cube s'appelle toujours « Cube ». Vous y reviendrez en demi-journée 2.

### 0:40 · Naviguer (25 min)

**Vous montrez (10 min),** d'après Basics 101 § 4, le mémo en main :
- orbite, panoramique et zoom ;
- le gizmo de navigation ;
- les vues 1, 3 et 7 (avec `Ctrl` pour la vue opposée) ;
- la touche 5 pour l'orthographique ;
- `.` pour cadrer la sélection, `Origine` pour toute la scène.

**Ils font (15 min) : le défi des vues.** Ils ouvrent `PRC02_ch1_blocage_lampe.blend` et affichent la collection *Variante A* (œil dans l'Outliner). Vous annoncez une vue, et ils la prennent au plus vite :
- « De face, en orthographique » : le croquis apparaît derrière la lampe ;
- « Dessus » ;
- « Profil gauche » ;
- « Cadrez la tête de la lampe » ;
- « Vue d'ensemble » ;
- « Tournez autour du socle, puis revenez de face ».

Accélérez au fil des annonces. Terminez par deux minutes libres pour tourner autour de la lampe.

**Point de contrôle :** au signal, tous les écrans montrent la même vue. Vous voyez d'un coup d'œil qui est perdu.

**Le petit plus :** cette lampe est l'objet du chapitre 1. Les apprenants la retrouveront.

### 1:05 · Pause (10 min)

### 1:15 · Sélectionner et transformer (40 min)

**Vous montrez (15 min),** d'après Basics 102 § 1 et 2 :
- La sélection et l'objet actif : `Maj + clic`, `A`, `Alt + A`.
- Les transformations : `G`, `R` ou `S`, puis l'axe, puis la valeur (`G X 2`, `R Z 90`, `S 0.5`). `Échap` ou un clic droit annule le geste en cours, `Ctrl + Z` la dernière action.
- `Maj + A` et le panneau F9.
- Le curseur 3D : `Maj + clic droit` pour le placer, `Maj + C` pour le ramener au centre.
- `Maj + D` et `Alt + D` : montrez seulement que les deux copient. Leur différence viendra en demi-journée 2.
- Le point de pivot : une rotation de trois objets en *Median Point*, puis en *Individual Origins*.

**Ils font (25 min) : la balise, au chiffre près.** Dans un fichier neuf (*File > New > General*), après avoir supprimé le cube avec `X` :
1. `Maj + A > Mesh > Cylinder`, puis F9 : *Vertices* 16, *Radius* 0.1, *Depth* 2.
2. `G Z 1` : le mât repose sur le sol.
3. `Maj + A > Mesh > Cube`, `S 0.3`, puis `G Z 2.2` : la tête.
4. `Maj + A > Mesh > UV Sphere`, F9 : *Radius* 0.12. Puis `G Z 2.3` et `G Y -0.3` : un feu, sur la face avant.
5. `Maj + D`, `Z`, `-0.3`, Entrée : un second feu, sous le premier.
6. `A`, puis `R Z 45` : tout tourne autour du mât. `Ctrl + Z`, passez le pivot en *Individual Origins* et recommencez : les feux se détachent de la tête.

**Point de contrôle :** dans la barre latérale (`N`), onglet *Item*, le mât affiche *Location Z* 1 m et la tête 2,2 m. Passez voir les débutants en premier. Un écart de position vient presque toujours d'un `G` sans axe.

### 1:55 · Activité A · La maquette en kit (45 min)

La fiche complète est plus bas. Le lancement dure 5 minutes : la situation, le choix du kit, le gabarit fil de fer et la règle « deux vues orthographiques avant de valider ». Viennent ensuite 35 minutes en autonomie et 5 minutes de retour.

### 2:40 · Pause (10 min)

### 2:50 · Organiser et sauvegarder (30 min)

**Vous montrez (10 min),** d'après Basics 102 § 4 :
- `M > New Collection`, et renommer par double-clic dans l'Outliner ou avec `F2`.
- *Save As* (`Maj + Ctrl + S`) et le bouton `+`, qui incrémente le numéro. *File > Recover > Auto Save* après un plantage.
- **Pack Resources**, avec `modele_projet_organise.blend` : passez en *Material Preview* pour montrer les textures, puis ouvrez *File > External Data*. Expliquez la texture rose sans la provoquer.
- Append et Link : une phrase, « vous les verrez au chapitre 3 ».

**Ils font (20 min) sur leur kit :**
- des collections *Carrosserie*, *Vitrage* et *Roues* ;
- des noms clairs pour les copies, par exemple `Roue_arrière_gauche_voiture` à la place de `Roue_avant_gauche_voiture.002` ;
- un enregistrement sous `kit_<secteur>_001.blend`, une modification, puis la version `_002` avec le bouton `+`.

**Point de contrôle :** chaque Outliner montre au moins trois collections nommées et plus aucun nom en `.001`. Le dossier contient deux versions du fichier.

### 3:20 · Galerie et bilan (20 min)

- **Galerie (8 min) :** chacun laisse sa maquette à l'écran, sous son meilleur angle. Tout le monde se lève et fait le tour des postes.
- **Trois questions (5 min) :**
  - « Pourquoi fallait-il des vues orthographiques pour aligner ? »
  - « Quelle différence entre l'œil et l'appareil photo, dans l'Outliner ? »
  - « Comment poser une pièce à 2,6 m exactement ? »
- **Un post-it par personne (5 min) :** « ce qui me bloque encore ». Lisez-les avant la demi-journée 2.
- **Annonce (2 min) :** la prochaine fois, on modélise. Ceux qui le souhaitent peuvent faire les quiz de Basics 101 et 102 dans l'application.

## Demi-journée 2 · Modéliser

Basics 102 (§ 3) et Basics 103. Les apprenants repartent avec une cabine modélisée et les réflexes d'un fichier sain.

| Horaire | Durée | Séquence | Modalité |
|---|---|---|---|
| 0:00 | 15 min | Réactivation | Collectif |
| 0:15 | 25 min | Objet, données et Mode Édition | Démo 10 min + pratique guidée 15 min |
| 0:40 | 45 min | Les outils d'édition | Démo 15 min + exercices 30 min |
| 1:25 | 10 min | Pause | |
| 1:35 | 20 min | Les modificateurs | Démo 15 min + essai 5 min |
| 1:55 | 50 min | Activité B · La rangée de sièges | Autonomie |
| 2:45 | 10 min | Pause | |
| 2:55 | 25 min | Activité C · La clinique du fichier | Autonomie + retour collectif |
| 3:20 | 20 min | Passerelle vers le chapitre 1 et bilan | Collectif |

### 0:00 · Réactivation (15 min)

- **Les post-it de la dernière fois :** répondez en 3 minutes aux blocages les plus cités.
- **Trois gestes en trois minutes :** chacun rouvre son kit, cadre une roue (`.`), passe en vue de dessus (7), puis revient à la vue d'ensemble (`Origine`).
- **La question qui lance la séance.** Sur votre écran, sélectionnez une roue, puis `Tab`, `A`, `S X 1.4` et `Tab` : toutes les roues s'élargissent. « Pourquoi ? » Laissez chercher une minute avant de répondre.

### 0:15 · Objet, données et Mode Édition (25 min)

**Vous montrez (10 min),** d'après Basics 102 § 3 et Basics 103 § 1 :
- `Tab`, puis 1, 2 et 3 : sommets, arêtes, faces.
- `Alt + clic` sur une arête pour sélectionner la boucle, `L` pour un îlot, `Ctrl + Pavé +` pour agrandir la sélection.
- Dans l'Outliner, dépliez une roue : on voit l'objet et son maillage. Dans l'onglet *Object Data*, le compteur indique combien d'objets partagent ce maillage.
- Un clic sur ce compteur crée une copie indépendante (*single user*).

**Ils font (15 min) sur leur kit :**
1. lire le compteur de leurs roues : 4 pour la voiture, 8 pour le tram, 3 pour les roues de l'avion ;
2. rendre une roue indépendante, puis l'élargir seule en Mode Édition ;
3. sélectionner une boucle d'arêtes autour d'une roue avec `Alt + clic`.

**Point de contrôle :** « Combien affiche votre compteur ? » Sur chaque écran, une seule roue est plus large que les autres.

### 0:40 · Les outils d'édition (45 min)

**Vous montrez (15 min),** d'après Basics 103 § 2, sur `exercices_modelisation_primitives.blend` :
- Extrude (`E`), et le piège de `Échap` juste après ;
- Inset (`I`) ;
- Bevel (`Ctrl + B`), avec la molette pour les segments et F9 pour corriger ;
- Loop Cut (`Ctrl + R`) ;
- Merge (`M`) et Knife (`K`) : citez-les simplement.

**Ils font (30 min) :** les exercices 1 à 4 du fichier, environ 6 minutes chacun. Chaque forme cible, en orange, sert de corrigé. Les plus rapides passent au défi Boîtier.

**Point de contrôle :** après chaque exercice, la forme grise ressemble à la cible orange. Allez voir d'abord l'exercice 1 des débutants : c'est là que le piège de `Échap` frappe.

### 1:25 · Pause (10 min)

### 1:35 · Les modificateurs (20 min)

**Vous montrez (15 min),** d'après Basics 103 § 3, sur le défi Boîtier ou un simple cube :
- l'onglet *Modifiers*, reconnaissable à sa clé à molette ;
- *Subdivision Surface* (`Ctrl + 2`) et sa cage ;
- *Mirror* et *Array* ;
- *Solidify*, sur un plan ;
- *Bevel* ; *Boolean*, en une phrase ;
- l'ordre de la pile, l'affichage dans la vue et *Apply*.

**Ils font (5 min) :** `Ctrl + 2` sur leur boîtier, puis `Tab` et le déplacement d'un sommet de la cage.

**Point de contrôle :** chacun voit la cage noire et la forme lissée qui la suit.

### 1:55 · Activité B · La rangée de sièges (50 min)

La fiche complète est plus bas. Le lancement dure 5 minutes, le socle 35 minutes en autonomie. Les 10 dernières minutes servent aux paliers ★ et à un retour collectif sur le pas entre les rangs.

### 2:45 · Pause (10 min)

### 2:55 · Activité C · La clinique du fichier (25 min)

La fiche complète est plus bas. Tout le monde traite les patients 1 à 3 (15 minutes) ; les patients 4 et 5 sont pour les plus rapides. Le retour collectif dure 10 minutes : pour chaque défaut, sa cause et son soin. Terminez par la checklist de Basics 103 § 4, à l'écran.

### 3:20 · Passerelle vers le chapitre 1 et bilan (20 min)

- **Ouvrez `PRC02_ch1_blocage_lampe.blend`** et affichez les trois variantes. « Des primitives, des cotes, des collections : vous savez déjà tout faire. Le chapitre 1 ajoute les unités, l'aimantation et les images de référence. »
- **Autoévaluation (5 min) :** chacun se situe sur la grille ci-dessous.
- **Tour de table express :** un mot pour finir.
- **Pour aller plus loin :** les quiz de Basics 103, les défis des Basics et les patients restants de la clinique.

| Je sais… | Acquis | En cours | À revoir |
|---|---|---|---|
| naviguer et prendre une vue précise sans me perdre | ☐ | ☐ | ☐ |
| déplacer, tourner et redimensionner au chiffre près | ☐ | ☐ | ☐ |
| retrouver, masquer et renommer un objet dans l'Outliner | ☐ | ☐ | ☐ |
| ranger mon fichier en collections et l'enregistrer par versions | ☐ | ☐ | ☐ |
| modéliser une forme simple avec Extrude, Inset, Bevel et Loop Cut | ☐ | ☐ | ☐ |
| construire avec des modificateurs, et corriger normales et échelle | ☐ | ☐ | ☐ |

<!-- pagebreak -->

## Activité A · La maquette en kit

**Fichier :** `PRC02_init_maquette_en_kit.blend` · **Durée :** 45 min · **Demi-journée 1**

**Situation :** « Un collègue vous envoie la maquette d'un concept pour la revue de design de demain. Le fichier est arrivé en vrac. Remontez-la. »

**Objectif :** remettre chaque pièce dans un gabarit fil de fer, puis poser les roues avec des copies liées.

**Pourquoi elle fonctionne :**
- Aligner une pièce en perspective est impossible. Les apprenants découvrent seuls l'utilité des vues orthographiques.
- Le gabarit leur montre eux-mêmes si c'est juste. Vous restez disponible pour ceux qui bloquent.
- Chaque geste prend un sens métier : la voie, l'empattement, l'entraxe des bogies.
- Le choix du secteur motive. Les copies liées préparent la notion de données partagées.

| Kit | Pièces à remettre en place | Copies liées (`Alt + D`) |
|---|---|---|
| Aéronautique · avion d'affaires | Fuselage, Aile (tournés), Cône de queue (retourné), Nez (trop petit), Empennage horizontal (masqué), `Cube.013` (la dérive, couchée) | Réacteur : `X -2.6` ; roue principale : `X -2.4` ; roue avant : `X -1.2`, puis `G Y -4.4` |
| Automobile · voiture compacte | Feux arrière et rétroviseur droit (déplacés), Caisse (tournée), Habitacle (retourné), Phare gauche, Phare droit (masqué, trop grand), `Cube.004` (le rétroviseur gauche, tourné de 45°) | La voie : `X -1.6` ; puis les deux roues avant : `Y 2.6`, l'empattement |
| Ferroviaire · avant de tram | Bogie (déplacé) ; Caisse, Nez, Pare-brise, Attelage (tournés) ; Phare gauche ; Phare droit (masqué, trop petit) ; `Cube.009` (le pantographe, couché) | `X -1.5` (même essieu) ; `Y 1.8` (second essieu) ; puis les 4 roues et le bogie : `Y 5.2` (bogie arrière) |

Les noms se terminent par le véhicule (`Caisse_voiture`, `Nez_tram`…), car deux objets d'un même fichier ne peuvent pas porter le même nom. Gauche et droite s'entendent depuis le poste de conduite ; l'avant regarde la vue de face. Le LISEZ-MOI donne aussi la position exacte de chaque pièce, pour le palier ★.

**Déroulé :**
1. **Lancement (5 min).** Projetez le fichier et montrez le gabarit. Remettez une pièce en place devant les apprenants : vue de face et `G Z`, puis vue de dessus et `G X`. Montrez ensuite le contrôle dans `N` : *Rotation* 0 et *Scale* 1. Donnez la règle d'or : « Avant de valider, vérifiez sous deux vues orthographiques. »
2. **Autonomie (35 min).** Chacun ferme l'œil des deux autres kits dans l'Outliner, puis suit le LISEZ-MOI. Astuce : `Ctrl + clic` sur un œil isole une collection.
3. **Retour (5 min).** Projetez une maquette remontée et demandez : « Qu'est-ce qui était difficile ? » Gardez la question des roues pour la demi-journée 2.

**Paliers :**
- **Socle :** toutes les pièces en place, les roues posées.
- **★ :** les positions exactes saisies dans `N > Item` ; `Alt + R` et `Alt + S` pour nettoyer rotation et échelle.
- **★★ :** élargir toutes les roues d'un coup ; une variante par *Duplicate Collection* ; une caméra de revue avec `Ctrl + Alt + 0`.

**Points d'observation :**
- Une pièce juste de face mais décalée en profondeur : faites tourner la vue.
- `Alt + D`, puis un clic avant de taper l'axe : la copie se pose sous la souris. `Ctrl + Z`, et on recommence.
- `R Z 90` dans le mauvais sens : `Ctrl + Z`, puis `-90`. Une rotation qui affiche 360° est juste aussi.
- Un clic sur le gabarit ne sélectionne rien : c'est voulu, il est verrouillé.
- Faites chercher la pièce masquée dans l'Outliner, à son œil fermé, plutôt qu'avec `Alt + H` : c'est l'occasion de pratiquer l'Outliner.

**Corrigé :** chaque pièce en place affiche *Rotation* 0, 0, 0 (ou 360°) et *Scale* 1, 1, 1, et ses arêtes se confondent avec celles du gabarit. Les positions exactes sont dans la partie ★ du LISEZ-MOI.

## Activité B · La rangée de sièges

**Fichier :** `PRC02_init_rangee_sieges.blend` · **Durée :** 50 min · **Demi-journée 2**

**Situation :** « Aménagement de cabine. Vous proposez un siège passager et la configuration d'une rangée. Le même siège se retrouve dans un train, un avion ou un car. »

**Objectif :** façonner un siège à partir d'un pavé, puis construire une cabine de 24 sièges avec deux Array et un Mirror.

**Pourquoi elle fonctionne :**
- Les quatre outils de Basics 103 servent tout de suite, dans un ordre qui a du sens : Loop Cut, Extrude, Inset, Bevel.
- Les modificateurs produisent un effet marquant : un siège devient une cabine.
- Le pas entre les rangs se règle dans un seul champ. C'est un vrai raisonnement de designer (confort, nombre de places), avec une silhouette de 1,75 m pour l'échelle.

**Le socle, en 9 étapes** (valeurs indicatives, en mètres) :

| Étape | Geste | Résultat |
|---|---|---|
| 1 | Clic sur *Siège*, `.`, puis `Tab` | Le Mode Édition |
| 2 | `Ctrl + R` sur une arête qui va de l'avant vers l'arrière, clic, clic droit, puis `G Y 0.15` | Une bande de 10 cm à l'arrière |
| 3 | `3`, la face du dessus de la bande, puis `E 0.65` | Le dossier |
| 4 | `G Y 0.12` | Le dossier s'incline |
| 5 | `Ctrl + B`, la molette jusqu'à 3 segments, puis `0.04` | Le haut du dossier s'arrondit |
| 6 | La face du dessus de l'assise, `I 0.025`, puis `E 0.03` | Un coussin |
| 7 | `Ctrl + 7`, la grande face avant du dessous, `I 0.12`, puis `E 0.33` | Le pied, jusqu'au sol |
| 8 | `Tab`, onglet *Modifiers* : Array (Count 2, Relative Offset X 1.05) ; Array (Constant Offset : Distance X 0, Y 0.8 ; Count 6) ; Mirror (X) | Une cabine 2+2 de 24 sièges |
| 9 | `Tab`, `A`, puis `S X 0.9` | Les 24 sièges s'affinent ensemble |

**Déroulé :**
1. **Lancement (5 min).** Montrez le siège cible. Montrez aussi l'origine de l'objet *Siège*, placée exprès sur l'axe du couloir : le Mirror s'en sert.
2. **Socle (35 min).** Trois points de contrôle : le dossier (étape 3), le pied (étape 7) et la cabine (étape 8).
3. **★ et retour (10 min).** Chacun essaie deux pas, par exemple 0.78 puis 0.95. Retour collectif : « Quel pas choisiriez-vous pour un trajet de 20 minutes ? Et pour un trajet de 3 heures ? »

**Paliers :**
- **★ :** essayer d'autres pas ; passer en 3+3 ; élargir le couloir ; ajouter un Bevel en haut de la pile ; mettre le Mirror en premier pour voir que l'ordre compte.
- **★★ :** des accoudoirs, avec `Alt + E > Extrude Individual Faces` ; une première classe 2+1, avec une copie liée.

**Points d'observation :**
- Dans le second Array, *Constant Offset* vaut 1 en X par défaut. Il faut le remettre à 0, sinon les rangs partent en biais.
- Étape 7 : l'Inset ne se fait que sur la grande face avant du dessous. Sur les deux faces, une face se retourne.
- Étape 9 faite en Mode Objet : `S X 0.9` rétrécit toute la cabine, couloir compris, et laisse une échelle non appliquée. C'est le patient 2 de la clinique.

**Corrigé :** la collection *Corrigé*, masquée, contient la cabine terminée. Ouvrez son œil dans l'Outliner.

## Activité C · La clinique du fichier

**Fichier :** `PRC02_init_clinique_fichier.blend` · **Durée :** 25 min · **Demi-journée 2**

**Situation :** « Un collègue vous confie cinq pièces d'une maquette. Chacune présente un défaut. Diagnostiquez, puis soignez. »

**Objectif :** reconnaître, à leur symptôme, les cinq pièges les plus courants du débutant, puis les corriger.

**Pourquoi elle fonctionne :** l'apprenant part de ce qu'il voit, comme il le fera seul sur ses propres fichiers. Chaque pièce a une jumelle saine, en orange, pour comparer. Les indices évitent les blocages, et les solutions sont à la fin du LISEZ-MOI.

| Patient | Symptôme | Cause | Soin |
|---|---|---|---|
| 1 · Le carénage cabossé | Le flanc paraît enfoncé, en escalier | Des normales inversées | *Overlays > Face Orientation* pour les voir ; `Tab`, `A`, `Maj + N` |
| 2 · L'accoudoir déformé | Des arrondis étirés aux bouts, presque vifs sur les côtés | Une échelle non appliquée (2,4 × 0,5 × 0,4) sous un Bevel | `Ctrl + A > Scale` |
| 3 · Le bouton qui ne s'arrondit pas | Un dessus plat bordé d'une arête vive | Une extrusion annulée avec `Échap` : 12 sommets au lieu de 8 | `Tab`, `A`, `M > By Distance` |
| 4 · Les hublots jumeaux | Modifier l'un modifie l'autre | Des copies liées : le maillage est partagé (compteur 2) | Clic sur le compteur, puis `Tab`, `A`, `S Z 1.5` |
| 5 · La porte qui tourne mal | `R Z 90` la fait tourner sur elle-même | Une origine au centre de la porte | Arête des charnières, `Maj + S > Cursor to Selected`, puis *Object > Set Origin > Origin to 3D Cursor* |

**Déroulé :**
1. **Lancement (2 min).** « Lisez le symptôme, cherchez la cause, puis soignez. Les solutions sont à la fin du texte : cherchez d'abord. »
2. **Autonomie (15 min).** Les patients 1 à 3 pour tous ; les patients 4 et 5 pour les plus rapides.
3. **Retour (8 min).** Un apprenant volontaire par patient montre le symptôme, puis le soin. Terminez par la checklist de Basics 103 § 4, à l'écran, et une phrase sur les quads et les n-gons.

**Points d'observation :**
- Patient 1 : en mode *Solid*, le défaut ressemble à un vrai creux. Faites tourner la vue autour de la pièce avant d'activer *Face Orientation*.
- Patient 2 : la différence se voit de près. Cadrez avec `.`.
- Patient 4 : ceux qui ont déjà étiré les deux hublots font `Ctrl + Z` avant de soigner.
- Faites le lien avec ce qu'ils ont déjà vécu. Le patient 4, ce sont les roues de la maquette ; le patient 2, c'est le `S X` des sièges fait en Mode Objet.

## Gérer l'hétérogénéité

### Le parcours « première fois »

Pour ceux qui n'ont jamais ouvert Blender :
- **Un copilote** est assis à côté, plus à l'aise. Règle : le copilote explique, mais ne prend jamais la souris.
- **Le mémo imprimé** est posé à côté du clavier.
- **Trois touches de survie** sont écrites au paperboard dès l'accueil : `Ctrl + Z` pour annuler, `Échap` pour abandonner un geste, `Origine` pour retrouver la scène.
- **Le socle de chaque activité suffit** : il couvre tous les gestes de la demi-journée.
- **Dans la maquette en kit**, si la personne hésite, proposez le kit automobile : ses gestes de roues sont les plus simples.
- **À chaque point de contrôle**, passez d'abord par ces postes.

### Les défis pour ceux qui avancent vite

- Les paliers ★ et ★★ de chaque activité, écrits dans le LISEZ-MOI.
- Les patients 4 et 5 de la clinique.
- Un avant-goût du chapitre 1 :
  - la Quad View (`Ctrl + Alt + Q`) ;
  - l'aimantation pendant un déplacement (`Ctrl` maintenu) ;
  - l'affichage des unités en millimètres.
- Le rôle de copilote : expliquer un geste à un voisin ancre ses propres acquis.

## Animer : conseils pratiques

1. **« Regardez, puis à vous. »** Pendant une démo, les mains restent loin du clavier ; les apprenants refont ensuite le geste seuls. Ceux qui suivent en direct décrochent au premier écart.
2. **Dites chaque touche à voix haute** (« Tab… 3… E, zéro virgule six cinq, Entrée »), puis notez-la au paperboard. La liste reste visible toute la demi-journée.
3. **Faites deviner avant d'expliquer.** « Pourquoi n'arrivez-vous pas à aligner cette pièce ? » « Pourquoi les quatre roues ont-elles changé ? » Une minute de recherche marque plus qu'une réponse immédiate.
4. **Rendez les points de contrôle visibles.** Un post-it vert sur l'écran veut dire « c'est fait », un rose « je bloque ». Depuis l'avant de la salle, vous voyez d'un coup d'œil où aller.
5. **Appliquez la règle des 3 minutes.** Un apprenant bloqué depuis plus de 3 minutes colle son post-it rose : personne ne reste perdu en silence.
6. **Ne prenez pas la souris.** Guidez à l'oral. Si vous devez montrer, faites `Ctrl + Z` ensuite et laissez l'apprenant refaire.
7. **Faites le tour des postes toujours dans le même ordre**, en commençant par les débutants.
8. **Affichez un minuteur** pour chaque phase en autonomie, et annoncez les 5 dernières minutes.
9. **Tenez un tableau des pièges.** Notez au paperboard chaque erreur qui revient : `Échap` après `E`, Mode Édition oublié, mauvais objet sélectionné. Relisez-le au bilan.
10. **Parlez métier.** Voie, empattement, entraxe, pas entre les rangs : les gestes deviennent des décisions de designer.
11. **Gardez l'interface en anglais.** Traduisez un libellé à l'oral la première fois, puis employez le terme anglais : c'est celui du support et des tutoriels.
12. **Montrez les productions.** La galerie de la demi-journée 1 et les cabines de la demi-journée 2 montrent à chacun ce qu'il sait déjà faire.

## Si vous prenez du retard

Raccourcissez dans cet ordre :

| Ordre | Demi-journée 1 | Demi-journée 2 |
|---|---|---|
| D'abord | Chasse aux réglages limitée à 4 questions ; défi des vues en 8 min | Exercices d'édition 1 et 3 seulement : Inset et Loop Cut reviennent dans les sièges |
| Ensuite | Organiser : démo de Pack Resources seule, enregistrement sans incrément | Modificateurs : démo de 10 min, sans essai |
| En dernier | Maquette en kit : le socle seulement, sans ★ ni ★★ | Clinique : patients 1 et 2 en séance, la suite après |

## Si vous êtes en avance

- **Demi-journée 1 :** le palier ★★ de la maquette (variante, caméra de revue), puis le défi de Basics 102 : un projet propre de bout en bout.
- **Demi-journée 2 :** les ★★ des sièges ; la Quad View et l'aimantation du chapitre 1 ; le défi de Basics 103 : un mug, une table basse ou une clé USB.

---

Les fichiers `PRC02_init_…` se reconstruisent avec les scripts de `tool/exercices_initiation/` (Blender 5.2 en arrière-plan, puis `finish_ui.py` pour la taille des zones). Ce document se convertit en PDF avec `tool/deroule_initiation/export_pdf.ps1`.
