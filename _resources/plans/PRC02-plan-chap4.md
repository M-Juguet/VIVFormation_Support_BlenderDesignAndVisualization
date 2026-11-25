# PRC02 · Plan du chapitre 4 · Visualisation temps réel et visuels de présentation avec EEVEE

Plan validé dans l'ensemble par le formateur le 18 novembre 2026. Ses décisions sont reportées dans « Décisions du formateur ». Cette version les intègre et s'aligne sur les plans quasi finaux des chapitres 2 et 3.
Blender 5.2 LTS, interface en anglais : les libellés cités ont été vérifiés dans Blender 5.2.1.
Demi-journée 6, la dernière de la formation. En synchrone et en présentiel, pour 5 à 8 apprenants.
Ce plan suit le découpage validé (`PRC02-decoupage-formation.md`) et ses sept critères de contrôle.

## En bref

**Objectif du chapitre** (déclaré dans `course_data.dart`) : paramétrer EEVEE pour une visualisation photoréaliste instantanée, éclairer en studio ou par HDRI, composer l'image avec la caméra et exporter des visuels de présentation.

**À la fin de la demi-journée, l'apprenant sait :**
- choisir le bon affichage selon le besoin : *Material Preview*, *Rendered* avec EEVEE, ou un rendu Cycles ;
- régler EEVEE pour un rendu fidèle : échantillons, *Raytracing*, transformation de vue ;
- éclairer un produit par une image HDRI, ou en studio avec trois lumières ;
- cadrer avec une focale adaptée, des guides de composition et une profondeur de champ ;
- exporter des visuels au bon format, nommés selon une convention.

**Format :** 3 h 30 de contenu et 2 pauses de 10 minutes, soit 3 h 50. Il reste 10 minutes de marge sur 4 heures. Exemple : de 13 h 30 à 17 h 20.
- Contenu technique : 3 h, accueil compris.
- Galerie des visuels et bilan de la formation : 30 minutes.

**Fil rouge :** la lampe de bureau, habillée au chapitre 3 en deux coloris (`lampe_habillage_v002.blend`). L'apprenant l'amène dans un studio par *File > Append*, la met en scène, puis en exporte trois visuels : une vue héros, un détail et une mise en situation.

**Principe d'animation**, repris de l'initiation : une démo de 10 minutes au plus, puis la pratique guidée, puis un court temps en autonomie. Les apprenants ne passent jamais plus de 15 minutes sans toucher la souris.

### La progression

Le chapitre suit le critère n° 7 du découpage.
- **Une notion à la fois.** Les démos longues sont découpées : une notion montrée, aussitôt pratiquée, puis la suivante.
- **Du connu vers le nouveau :**
  - la section 1 part des modes d'affichage de Basics 101, de *Material Preview*, utilisé pendant tout le chapitre 3, et de la case *Raytracing*, cochée au chapitre 3 pour le verre et expliquée ici ;
  - l'éclairage commence par l'HDRI, qui prolonge les images d'environnement de *Material Preview*. Ses nœuds reprennent *Texture Coordinate* et *Mapping*, vus au chapitre 3. Viennent ensuite les lumières de studio, qui demandent plus de réglages ;
  - la caméra part de la vue caméra (`0`) de Basics 101.
- **Trois temps pour chaque geste :** démonstration, pratique guidée, puis autonomie. L'atelier final sert de pratique autonome pour l'ensemble du chapitre.
- **L'atelier n'apporte aucune notion nouvelle.** Ses paliers ★ et ★★ non plus : la matière émissive de la lampe allumée est fournie toute prête. Les défis qui demandent une notion nouvelle sont à part, dans « Si vous êtes en avance ».
- **Aucun geste avant son explication.** Chaque séquence liste ses prérequis et ce qu'elle apporte.

### Ce que le chapitre ne refait pas

| Déjà vu | Où | Ce que le chapitre 4 en fait |
|---|---|---|
| Les quatre modes d'affichage | Basics 101 § 4 | Basics 101 renvoie au chapitre 4 : on les exploite, sans les présenter de nouveau. |
| EEVEE moteur actif, focale de 50 mm, format 1920 × 1080 | Initiation, chasse aux réglages | On ne les présente plus comme des découvertes. On explique quand et pourquoi les changer. |
| *Material Preview*, ses images d'environnement, le menu *Viewport Shading* | Chapitre 1 (le menu) ; chapitre 3 (tout le chapitre) | On l'oppose au mode *Rendered* et au rendu final. |
| Les cases *Raytracing* (onglet *Render*) et *Raytraced Transmission* (matière), cochées pour le verre ; *Thin Wall* | Chapitre 3, section 1 | *Raytracing* est expliqué ici : ce qu'il apporte au-delà du verre, son coût, sa place dans la scène et non dans la lampe. *Raytraced Transmission* et *Thin Wall* sont seulement rappelés. |
| Le Shader Editor, les nœuds *Texture Coordinate* et *Mapping* | Chapitre 3, section 2 | Les mêmes nœuds font tourner l'HDRI du monde. |
| *File > Append* | Chapitre 3, section 3 (dossier *Material*) | Même geste, dossier *Collection* : la lampe entre dans le studio au lancement, le coloris B au palier ★. |
| La liste des matières d'un objet | Chapitre 3, section 1 | Choisir la matière fournie `Ampoule_allumee`, au palier ★★. |
| L'œil et l'appareil photo de l'Outliner | Basics 101 | Masquer une collection dans la vue, puis au rendu. |
| *Pack Resources* | Basics 102 § 4 ; chapitre 3 | Réinvesti en fin d'atelier, pour livrer un fichier qui s'ouvre seul. |

### Ce que l'on survole

Ces notions restent hors séance. Certaines servent de défi.
- Cycles : une image comparative suffit. Personne ne le manipule en séance (décision du formateur).
- La matière émissive : fournie toute prête pour le palier ★★ ; son réglage reste un défi.
- Les sondes de lumière (*Light Probe Sphere*, *Plane* et *Volume*), les volumes et le flou de mouvement.
- Le compositeur : un défi seulement, avec le nœud *Glare*.
- *Working Space*, *White Balance* et *Curves* dans la gestion des couleurs.
- Les passes de rendu, le *light linking* et les *AOV*.

## Minutage

| Horaire | Durée | Séquence | Ancre | Modalité |
|---|---|---|---|---|
| 0:00 | 10 min | Accueil et lancement de l'atelier | — | Collectif + 1 geste guidé |
| 0:10 | 30 min | Paramétrer EEVEE | `ch4_sec1_title` | 4 cycles courts (démo 10 min + guidé 17 min) + autonomie 3 min |
| 0:40 | 20 min | Éclairer par HDRI | `ch4_sec2_title` | Démo 7 min + guidé 10 min + autonomie 3 min |
| 1:00 | 10 min | Pause | | |
| 1:10 | 35 min | Éclairer en studio | `ch4_sec2_title` | 2 démos de 5 min + guidé 10 et 12 min + autonomie 3 min |
| 1:45 | 40 min | Caméra, composition et export | `ch4_sec3_title` | 2 démos de 6 min + guidé 12 et 13 min + autonomie 3 min |
| 2:25 | 10 min | Pause | | |
| 2:35 | 45 min | Atelier : concept final | `ch4_sec4_title` | Lancement 3 min + autonomie 37 min + dépôt 5 min |
| 3:20 | 15 min | Galerie et restitution | `ch4_sec4_title` | Collectif |
| 3:35 | 15 min | Bilan de la formation | — | Collectif |
| 3:50 | | Fin | | |

Sur 3 h 30 : 39 minutes de démonstration, 74 minutes de pratique guidée, 49 minutes en autonomie et 48 minutes en collectif.

## Avant la séance

### Les postes des apprenants
- [ ] Un rendu F12 du fichier `PRC02_ch4_lampe_en_studio.blend` a été lancé sur chaque poste. Notez le temps : un poste lent se repère avant la séance.
- [ ] Le studio et le fichier de secours du chapitre 4 sont copiés dans le dossier de travail.
- [ ] Le fichier de fin du chapitre 3, `lampe_habillage_v002.blend`, est retrouvé sur chaque poste.
- [ ] Un dossier partagé `Galerie_PRC02` est accessible en écriture depuis tous les postes, ou une clé USB circule.

### Votre poste de démonstration
- Blender en configuration d'usine, *Resolution Scale* agrandi pour le vidéoprojecteur, comme à l'initiation.
- Le fichier de secours est prêt à ouvrir : ses collections « Corrigé » et les notes « Corrigé » du LISEZ-MOI montrent le résultat attendu de chaque étape et aident à répondre aux questions (voir « Fichiers de travail et corrigés »).
- L'image comparative des moteurs et les trois visuels du corrigé sont ouverts dans une visionneuse.
- Le diaporama de la galerie est prêt à lire le dossier `Galerie_PRC02`.
- La planche du récapitulatif, `PRC02_ch4_recapitulatif.png`, est prête pour le bilan.

### Le matériel de la salle
- Les post-it vert et rose pour les points de contrôle.
- Le paperboard, avec une grille « temps de rendu » : poste, temps à 64 échantillons, temps à 128 échantillons.
- Le minuteur visible de tous.

## Séquences et sections

### 0:00 · Accueil et lancement de l'atelier (10 min)

**Prérequis déjà vus :** *File > Append* (chapitre 3, section 3) ; *Save As* et les versions (Basics 102 § 4).
**Nouveau :** rien. Le geste d'Append du chapitre 3 sert ici avec le dossier *Collection* au lieu du dossier *Material*.

- **Rappelez le chemin parcouru.** Le blocage du chapitre 1, la lampe modélisée du chapitre 2, la lampe habillée en deux coloris au chapitre 3. « Maintenant, on la met en scène et on la présente. »
- **Montrez la cible.** Projetez les trois visuels du corrigé. « À 17 heures, vous aurez exporté les vôtres. » Présentez les livrables (voir « L'atelier final ») et le dossier `Galerie_PRC02`.
- **Chacun ouvre son point de départ :**
  - si la lampe du chapitre 3 est exploitable : ouvrir `PRC02_ch4_studio.blend`, puis *File > Append* : `lampe_habillage_v002.blend`, dossier *Collection*, collection *Lampe*. Enregistrer sous `lampe_rendu_v001.blend` ;
  - sinon : ouvrir le fichier de secours `PRC02_ch4_lampe_en_studio.blend` et l'enregistrer sous le même nom.
- **Le coloris B attend.** La collection `Lampe_coloris_B` reste dans le fichier du chapitre 3 : elle n'entre dans le studio qu'au palier ★ de l'atelier. Dans le fichier de secours, elle est déjà là, masquée.
- **Règle de bascule :** au bout de 3 minutes de difficulté (Append qui échoue, matières perdues, échelle non appliquée), on passe au fichier de secours, sans débat. Rassurez : la lampe du chapitre 3 pourra être mise en scène plus tard, dans le même studio.
- **Au paperboard,** les touches du jour, ajoutées au fil de la séance : `Z` (menu des modes d'affichage), `F12` (rendre), `J` (emplacement de rendu suivant), `Ctrl + Alt + 0` du pavé numérique (caméra sur la vue), `Maj + Alt + S` (enregistrer l'image).

**Point de contrôle :** sur chaque écran, la lampe est posée sur le fond du studio, et le titre de la fenêtre affiche `lampe_rendu_v001.blend`.

**Points d'observation**
- L'ampoule ne laisse plus voir le fond de la tête, alors qu'elle le faisait au chapitre 3. C'est normal : la case *Raytracing* appartient à la scène, et l'Append n'apporte que la lampe et ses matières. « On y revient dans un quart d'heure. »
- Dans la fenêtre d'Append, on choisit la collection *Lampe*, pas les objets un par un. Les *Empty* `Grille_pivot` et `Interrupteur_pivot` arrivent avec elle : ne les supprimez pas, la grille et les crans en dépendent.

### Section 1 · Paramétrage d'EEVEE (`ch4_sec1_title`) · 0:10 (30 min)

**Prérequis déjà vus :**
- les quatre modes d'affichage et leurs boutons (Basics 101 § 4) ;
- les onglets de l'éditeur de propriétés (Basics 101) ;
- EEVEE, moteur actif d'un fichier neuf (initiation, chasse aux réglages) ;
- *Material Preview* pour juger les matières, les matières métal, laque et verre (chapitre 3) ;
- les cases *Raytracing* et *Raytraced Transmission*, cochées pour le verre en une phrase (chapitre 3, section 1).

**Nouveau :** le menu circulaire `Z` ; *Scene Lights* et *Scene World* ; le rendu `F12`, sa fenêtre et ses emplacements ; *Samples* ; ce que fait *Raytracing*, cochée au chapitre 3 et expliquée ici ; la transformation de vue.

**Notions**
- **Trois façons de voir la même scène :**
  - *Material Preview* : EEVEE avec une image d'environnement intégrée à Blender. Les lumières et le monde de la scène sont ignorés par défaut (*Scene Lights* et *Scene World* décochés). C'est l'affichage pour juger les matières.
  - *Rendered* : le moteur de rendu actif, avec les lumières et le monde de la scène. Avec EEVEE, c'est déjà presque l'image finale, en temps réel.
  - Le rendu final (`F12`) : le même moteur, avec plus d'échantillons, dans la résolution de sortie.
- **EEVEE et Cycles.** EEVEE calcule l'image comme un moteur de jeu vidéo, avec des approximations : quelques secondes par image. Cycles suit le trajet de la lumière (*path tracing*) : c'est plus juste physiquement, mais une image prend des minutes. Le programme vise le temps réel : la formation n'utilise qu'EEVEE, et Cycles n'est montré qu'en image. Le moteur se choisit dans l'onglet *Render*, champ *Render Engine*.
- **Les réglages qui comptent**, dans l'onglet *Render* :
  - *Sampling* : *Viewport > Samples* (16 par défaut) règle la fluidité de la vue ; *Render > Samples* (64 par défaut) règle la qualité du rendu final. Monter à 128 pour l'image finale, si le poste le permet.
  - *Raytracing* : décoché dans un fichier neuf, comme dans le studio. Au chapitre 3, vous l'avez coché pour que le verre laisse voir ce qui est derrière lui. Il fait davantage : des reflets justes sur le métal poli et la laque, et une meilleure lumière indirecte avec *Fast GI Approximation*, qui en dépend. Il coûte du temps de calcul. *Method* reste sur *Screen-Trace*. La case appartient à la scène : un Append amène la lampe et ses matières, pas les réglages de rendu de son fichier d'origine.
  - *Color Management > View* : *AgX* par défaut, au rendu photographique ; *Standard*, sans compression des hautes lumières ; *Khronos PBR Neutral*, conçu pour restituer fidèlement la couleur de base d'un produit. *Look* et *Exposure* ajustent le contraste et la luminosité.
- **Rappel du chapitre 3 : le verre dans EEVEE.** La matière du verre a la case *Raytraced Transmission* cochée (onglet *Material*, rubrique *Settings*) et *Thin Wall* coché. Cela ne suffit pas : le *Raytracing* de la scène doit être actif. *Render Method* reste sur *Dithered*, sa valeur par défaut.
- **Les emplacements de rendu** (menu *Slot* de la fenêtre de rendu) : comparer deux réglages d'un appui sur `J`.

**Le banc d'essai : quatre cycles courts, puis l'autonomie**, sur la lampe de chacun, avec la caméra `CAM_banc_essai` du studio. Chaque cycle montre une seule notion, puis la fait pratiquer aussitôt.

| Cycle | Vous montrez | Ils font |
|---|---|---|
| 1 · Trois affichages (2 + 3 min) | Le menu circulaire `Z`. *Material Preview*, puis *Rendered*. Dans *Material Preview*, cochez *Scene World* : l'éclairage change. | Passer d'un affichage à l'autre avec `Z`. Cocher puis décocher *Scene World* en *Material Preview*. |
| 2 · EEVEE et Cycles (2 + 0 min) | L'image comparative *Material Preview*, EEVEE et Cycles, avec les temps de rendu. « Cycles est la référence physique ; EEVEE donne une image très proche en quelques secondes. » Le champ *Render Engine*, sans le changer. | Rien : on reste sur EEVEE. |
| 3 · Le *Raytracing* (3 + 7 min) | « Au chapitre 3, vous avez coché cette case pour le verre. Le studio ne l'a pas : voyons tout ce qu'elle change. » `F12`, la fenêtre de rendu et son menu *Slot*. *Raytracing* coché, `F12` dans un autre emplacement, puis `J` pour comparer le chrome des articulations, la laque de la tête et le verre. Le temps de rendu, en haut de la fenêtre. | `F12` dans l'emplacement 1, *Raytracing* décoché. Cocher *Raytracing*, puis `F12` dans l'emplacement 2. Comparer avec `J`. Passer *Render > Samples* de 64 à 128, relancer, puis reporter les deux temps au paperboard. |
| 4 · La transformation de vue (3 + 7 min) | *Color Management* : le nuancier en *AgX*, en *Standard* et en *Khronos PBR Neutral*. | Essayer les trois sur le nuancier du studio. Garder une transformation de vue et savoir dire pourquoi. |

**Seuls (3 min) :** régler son fichier pour la suite de la séance. *Raytracing* coché, un nombre d'échantillons adapté à son poste, la transformation de vue choisie. Enregistrer (`Ctrl + S`).

**Points de contrôle**
- Chaque écran montre deux emplacements de rendu, sans et avec *Raytracing*.
- Les temps de rendu sont au paperboard. Commentez les écarts entre postes : ils guideront le nombre d'échantillons de l'atelier.
- Chacun annonce sa transformation de vue et sa raison.

**Points d'observation**
- Les panneaux de l'onglet *Render* sont repliés : faites-les déplier un par un.
- *Fast GI Approximation* reste grisé tant que *Raytracing* est décoché.
- Un verre qui ne laisse rien voir, *Raytracing* coché : la case *Raytraced Transmission* de sa matière est décochée. Elle se coche dans l'onglet *Material*, rubrique *Settings*, comme au chapitre 3.
- Un poste lent : baisser *Viewport > Samples* à 8, et tester les rendus à 50 % (*Resolution Scale*, onglet *Output*).
- Un apprenant resté dans son fichier du chapitre 3 : il a déjà *Raytracing* coché, mais ni studio ni nuancier. Le ramener dans `lampe_rendu_v001.blend`.

**Quiz prévus (3)**
1. « En *Material Preview*, les lumières de votre scène n'éclairent pas la lampe. Pourquoi ? » Réponse : ce mode utilise une image d'environnement intégrée ; *Scene Lights* et *Scene World* sont décochés par défaut.
2. « Au chapitre 3, votre ampoule laissait voir le fond de la tête. Dans le studio, après l'Append, elle ne le fait plus. Pourquoi ? » Réponse : la case *Raytracing* appartient à la scène ; l'Append amène la lampe et ses matières, pas les réglages de rendu. Leurres : l'Append a abîmé la matière ; *Thin Wall* s'est décoché ; le studio est réglé sur Cycles.
3. « Vous devez vérifier qu'un rouge correspond au nuancier CMF. Quelle transformation de vue choisir ? » Réponse : *Khronos PBR Neutral*. *AgX* désature les couleurs vives et lumineuses.

### Section 2 · Éclairage de studio et HDRI (`ch4_sec2_title`)

La section se joue en deux temps, de part et d'autre de la première pause : l'HDRI d'abord, le studio ensuite.

#### 0:40 · Éclairer par HDRI (20 min)

**Prérequis déjà vus :** les images d'environnement de *Material Preview* (chapitre 3) et la case *Scene World* (section 1) ; `F12` et les emplacements de rendu (section 1) ; l'espace de travail *Shading*, le Shader Editor et les nœuds *Texture Coordinate* et *Mapping* (chapitre 3, section 2).
**Nouveau :** l'onglet *World* ; le sélecteur de monde ; l'HDRI comme source de lumière et de reflets ; *Strength* ; la rotation de l'HDRI.

**Notions**
- **Une HDRI** est une photographie panoramique à 360°, qui enregistre la vraie intensité de la lumière. Placée dans le monde (*World*), elle éclaire la scène et se reflète dans les surfaces brillantes. Le studio s'ouvre sur `Monde_Studio`, une HDRI : c'est elle qui éclairait les rendus de la section 1.
- **Changer de monde** : le sélecteur de monde, en haut de l'onglet *World*, bascule entre les mondes préparés.
- **Mettre en place une HDRI**, onglet *World*, panneau *Surface* : le bouton à gauche du champ *Color* ouvre un menu ; *Environment Texture* ; puis *Open*. *Strength* règle l'intensité.
- **Tourner l'HDRI** : la rotation Z du nœud *Mapping*, le même nœud qui étirait le brossé au chapitre 3, place le reflet principal où on le veut. Dans les mondes du studio, elle se règle directement dans l'onglet *World*.
- **Les licences.** Poly Haven publie ses HDRI sous licence CC0, sans attribution obligatoire. Les trois HDRI du studio en viennent : `studio.exr`, fournie avec Blender, et deux HDRI 2K téléchargées sur Poly Haven, `artist_workshop` et `docklands_01`. Le placage de chêne du plateau de bureau, `oak_veneer_01`, vient aussi de Poly Haven, sous la même licence.
- **Option :** *World > Settings > Sun > Threshold* extrait le soleil d'une HDRI d'extérieur pour obtenir des ombres nettes.

**Vous montrez (7 min)**
1. Le sélecteur de monde : `Monde_Studio`, puis `Monde_Interieur`. Le rendu change de lumière et de reflets.
2. Dans un monde neuf (bouton *New* du sélecteur) : *Color > Environment Texture > Open*, depuis le dossier des HDRI fournies avec Blender (`C:\Program Files\Blender Foundation\Blender 5.2\5.2\datafiles\studiolights\world\`). Puis *Strength*.
3. Les nœuds d'un monde préparé, une fois, dans l'espace *Shading* : le menu *Object* du Shader Editor passé sur *World*. *Texture Coordinate*, *Mapping*, *Environment Texture*, *Background*. Faites reconnaître les deux premiers : ce sont ceux du brossé. « Les mondes du studio sont déjà câblés : vous ne réglerez que la rotation et l'intensité. »
4. La rotation Z du *Mapping* : le reflet glisse sur la tête laquée et sur le chrome des articulations.

**Ils font (10 min)**
1. Passer sur `Monde_Studio`, `Monde_Interieur` et `Monde_Exterieur`, avec un `F12` dans un emplacement différent pour chacun. Comparer avec `J`.
2. Tourner l'HDRI retenue pour placer le reflet principal sur la tête.

**Seuls (3 min) :** choisir l'ambiance de la future vue de situation, son intensité et sa rotation.

**Point de contrôle :** chacun montre sa lampe sous deux mondes, dans deux emplacements de rendu, avec un reflet placé volontairement.

**Points d'observation**
- La lampe disparaît dans une HDRI très claire : baisser *Strength*.
- En fond, une HDRI reste moins nette qu'une photographie : 2K pour l'intérieur et l'extérieur, 1K pour le studio. Pour la vue de situation, cadrer serré ou flouter le fond avec la profondeur de champ.
- Un monde créé par erreur avec *New* : le sélecteur permet de revenir aux mondes du studio, qui ne sont jamais perdus.

**Quiz prévu (1)**
- « Votre HDRI place le reflet principal au mauvais endroit sur la tête laquée. Que faites-vous ? » Réponse : tourner l'HDRI (rotation Z du nœud *Mapping*), plutôt que de déplacer la lampe ou la caméra.

#### 1:00 · Pause (10 min)

#### 1:10 · Éclairer en studio (35 min)

**Prérequis déjà vus :** le sélecteur de monde (séquence précédente) ; le menu *Add* (Basics 102) ; `G`, `R` et le renommage (Basics 102) ; `M > New Collection` (Basics 102 § 4) ; l'œil et l'appareil photo de l'Outliner (Basics 101) ; le mode *Rendered* (section 1).
**Nouveau :** les quatre types de lumière ; *Power*, *Temperature*, *Shape* et *Size* ; l'éclairage en trois points ; la ligne de reflet.

**Notions**
- **Partir du noir.** `Monde_Neutre` est un monde gris très sombre : on éteint la lumière ambiante pour construire la sienne.
- **Les quatre types de lumière** (*Add > Light*) : *Point*, *Sun*, *Spot*, *Area*. En studio, l'*Area* domine : une source étendue, comme une boîte à lumière (*softbox*).
- **Les réglages d'une lumière**, onglet *Light* (*Object Data*) :
  - *Power*, en watts (*Strength* pour *Sun*). Une *Area* neuve fait 10 W pour 1 m de côté ;
  - *Color*, ou *Temperature* en kelvins : cocher la case *Temperature*, décochée par défaut, puis régler la valeur. 2700 K est chaud, 6500 K est froid ;
  - *Shape* et *Size* pour une *Area* : plus la source est grande, plus l'ombre et le reflet sont doux.
- **L'éclairage en trois points :**
  - la principale (*key*), à 45° environ, au-dessus et sur le côté : elle modèle les volumes ;
  - la secondaire (*fill*), du côté opposé, plus faible et plus grande : elle débouche les ombres ;
  - le contre-jour (*rim*), derrière l'objet : il dessine le contour et détache la silhouette du fond.
  Un rapport de 3 à 4 entre principale et secondaire est un bon départ, pas une règle.
- **Les lignes de reflet.** Une *Area* longue et fine (*Rectangle*) trace une ligne de lumière sur une surface brillante : ici, la tête laquée. C'est le geste du studio automobile sur une carrosserie. On le retrouve sur un fuselage ou sur la caisse d'un train.
- **Le fond cyclo** : un fond courbe, sans arête, qui ne montre pas d'horizon. Il est fourni dans le studio.

**Vous montrez · démo A (5 min) : une lumière**
1. Le sélecteur de monde : `Monde_Neutre`. La lampe s'éteint presque.
2. *Add > Light* : une lumière de chaque type devant la lampe, en *Rendered*. Comparez les ombres, puis supprimez-les.
3. Une *Area* : *Power*, *Temperature* (la case, puis la valeur), puis *Size*, petite puis grande. Montrez l'ombre et le reflet sur la tête laquée.

**Ils font · guidé 1 (10 min) : la principale**
1. Passer sur `Monde_Neutre`.
2. Ajouter une *Area*, la nommer `Key`, la placer à 45° au-dessus et sur le côté, l'orienter vers la lampe avec `R`.
3. Essayer deux tailles et deux températures. Garder le réglage qui modèle le mieux la tête.

**Vous montrez · démo B (5 min) : trois lumières**
1. `Fill`, puis `Rim`, ajoutées une à une à côté de `Key`. Fermez leur œil dans l'Outliner à tour de rôle : chacun voit le rôle de chaque lumière.
2. Une *Area* *Rectangle* longue au-dessus de la lampe : la ligne de reflet apparaît sur la tête laquée.

**Ils font · guidé 2 (12 min) : le studio en trois lumières**
1. Ajouter `Fill`, du côté opposé, avec environ un tiers de la puissance de `Key` et une taille plus grande.
2. Ajouter `Rim`, derrière et au-dessus, jusqu'à voir un liseré clair sur le contour de la tête.
3. Ranger les trois lumières dans une collection `Eclairage_studio` (`M > New Collection`).
4. Test : n'en laisser qu'une allumée à la fois avec l'œil, puis les trois.

**Seuls (3 min) :** combiner. Revenir sur `Monde_Studio` avec une *Strength* de 0,3, lumières allumées, puis comparer avec `Monde_Neutre`. Garder la combinaison préférée pour la vue héros. Palier ★ : une *Area* *Rectangle* pour une ligne de reflet sur la tête ; une principale à 4500 K et un contre-jour à 7000 K.

**Points de contrôle**
- En *Rendered*, la silhouette de la lampe se détache du fond.
- L'Outliner montre la collection `Eclairage_studio`, avec `Key`, `Fill` et `Rim`.
- Interrogez deux ou trois apprenants : « Que fait `Rim` ? »

**Points d'observation**
- Une lumière qui n'éclaire rien : elle pointe ailleurs. Regarder la ligne qui indique sa direction.
- La température ne change rien : la case *Temperature* n'est pas cochée.
- L'œil de l'Outliner ne masque une lumière que dans la vue. Pour l'ôter d'un rendu `F12`, il faut aussi l'icône d'appareil photo : c'est la distinction de Basics 101.
- Tout est blanc ou tout est noir : un *Power* dix fois trop fort ou trop faible. Les valeurs dépendent de la distance : la lampe mesure 0,45 m. Les puissances du corrigé donnent un ordre de grandeur.
- Le studio paraît plat : la secondaire est aussi forte que la principale.

**Quiz prévus (2)**
1. « Dans un éclairage en trois points, quel est le rôle du contre-jour (*rim*) ? » Réponse : dessiner le contour et détacher la silhouette du fond.
2. « Pour adoucir l'ombre portée par une *Area*, que modifiez-vous ? » Réponse : sa taille (*Size*), et non sa puissance.

### Section 3 · Caméra, composition et export (`ch4_sec3_title`) · 1:45 (40 min)

**Prérequis déjà vus :**
- la vue à travers la caméra active, `0` du pavé numérique (Basics 101) ;
- le menu *Add* (Basics 102) et les objets *Empty* (chapitre 2 : `Grille_pivot`, `Interrupteur_pivot`) ;
- la barre latérale `N` et le *Clip Start* de la vue (chapitre 1) ;
- `F12` et les emplacements de rendu (section 1) ;
- l'œil et l'appareil photo de l'Outliner (Basics 101) ;
- la notion de focale, au moins la valeur d'usine de 50 mm (initiation).

**Nouveau :** *Align Active Camera to View* ; *Lock Camera to View* ; la caméra active (`Ctrl + 0`) ; le choix de la focale et la caméra *Orthographic* ; les guides de composition ; la profondeur de champ ; le format de sortie ; *Film > Transparent* ; *Image > Save As*.

**Notions**
- **Placer une caméra :**
  - *Add > Camera* ; `0` du pavé numérique pour voir à travers la caméra active ;
  - *View > Align View > Align Active Camera to View* (`Ctrl + Alt + 0` du pavé numérique) ;
  - *Lock Camera to View*, dans la barre latérale (`N`), onglet *View*, rubrique *View Lock* : on cadre en naviguant ;
  - plusieurs caméras : `Ctrl + 0` du pavé numérique fait de la caméra sélectionnée la caméra active. Les nommer : `CAM_heros`, `CAM_detail`, `CAM_situation`.
- **La focale** (*Focal Length*, onglet *Camera*), au-delà de la valeur d'usine :
  - une courte focale (24 mm) exagère la perspective et déforme les proportions ;
  - une longue focale (85 à 100 mm), avec du recul, restitue des proportions fidèles : c'est la focale de la photo de produit ;
  - une caméra de *Type* *Orthographic* donne une vue technique, sans perspective.
- **La composition** : *Viewport Display > Composition Guides* (*Thirds*, *Golden Ratio*, *Center Diagonal*), et le *Passepartout* qui assombrit l'extérieur du cadre.
- **La profondeur de champ** : *Depth of Field*, avec *Focus on Object* (un *Empty* ou une pièce de la lampe) et *F-Stop*. Plus le nombre est petit, plus le fond est flou. En gros plan, la zone nette ne mesure que quelques millimètres : partir de 5,6 à 8. L'effet n'est crédible que si la scène est à l'échelle réelle.
- **Le format de sortie** : onglet *Output*, panneau *Format* : *Resolution X* et *Y*, *Resolution Scale* (%), et le menu des préréglages. Le ratio suit l'usage : 16:9 pour une diapositive, 1:1 ou 4:5 pour un réseau social, A4 pour une impression.
- **Rendre et enregistrer** :
  - `F12` (*Render > Render Image*) ne crée aucun fichier ;
  - *Image > Save As* (`Maj + Alt + S`) : *PNG*, *RGB* ou *RGBA*, *Color Depth* 8, *Color Management* sur *Follow Scene* ;
  - *Film > Transparent* (onglet *Render*) et *RGBA* donnent un PNG sans fond ;
  - option : *View > Viewport Render Image*, une capture rapide de la vue pour une revue ;
  - option : `Ctrl + B` en vue caméra (*Render Region*) limite le rendu à une zone, pour tester vite un détail ; `Ctrl + Alt + B` l'efface.

**Vous montrez · démo A (6 min) : cadrer**
1. *Add > Camera*, `Ctrl + 0` (elle devient la caméra active, sinon l'alignement déplace `CAM_banc_essai`), *Align Active Camera to View*, puis *Lock Camera to View* : cadrage en naviguant. Décochez le verrou une fois le cadrage trouvé.
2. Le même cadrage à 24, 50 et 100 mm, en reculant la caméra à chaque fois. « Laquelle respecte votre dessin ? » Puis *Type* sur *Orthographic*, en une phrase : la vue technique.
3. *Composition Guides > Thirds* et le *Passepartout*.

**Ils font · guidé 1 (12 min) : la vue héros**
1. Créer `CAM_heros`. Trois quarts avant, la caméra légèrement au-dessus du plateau.
2. Focale de 85 mm. Cadrer en naviguant, avec *Lock Camera to View*, puis désactiver le verrou.
3. Guides *Thirds* : la tête de la lampe sur un point fort.

**Vous montrez · démo B (6 min) : détail et export**
1. *Depth of Field* : *Focus on Object* sur un *Empty* `Mise_au_point` posé sur l'interrupteur, *F-Stop* à 1,4 puis à 8.
2. L'onglet *Output* : *Resolution X* et *Y*, *Resolution Scale*, le menu des préréglages.
3. `F12`, puis *Image > Save As* : le dossier `rendus/`, le nom, *PNG* et *Color Management* sur *Follow Scene*. En une phrase : *Film > Transparent* et *RGBA* pour un fond transparent.

**Ils font · guidé 2 (13 min) : le détail et le premier export**
1. Créer `CAM_detail`, à 100 mm, sur un détail : l'interrupteur cranté et la grille d'aération, une articulation, ou l'ampoule dans la tête.
2. Ajouter l'*Empty* `Mise_au_point` sur ce détail. Activer *Depth of Field*, régler *Focus on Object*, puis *F-Stop*, entre 5,6 et 8.
3. Masquer la collection `Nuancier` (œil et appareil photo). Repasser sur `CAM_heros` (`Ctrl + 0`), vérifier le format 1920 × 1080, puis `F12`.
4. Enregistrer `rendus/lampe_heros_<initiales>_v001.png`.
5. Ouvrir le fichier dans l'Explorateur Windows : l'image doit être identique au rendu.

**Seuls (3 min) :** la vue de détail. Activer `CAM_detail`, passer la résolution à 1080 × 1080, rendre, puis enregistrer `rendus/lampe_detail_<initiales>_v001.png`.

**Points de contrôle**
- `CAM_heros` et `CAM_detail` existent, nommées, avec des guides de composition visibles.
- Deux PNG sont dans `rendus/`, avec le bon nom et le bon format, et leurs couleurs sont celles du rendu.

**Points d'observation**
- La résolution appartient à la scène, pas à la caméra. Avant de rendre `CAM_detail` en 1080 × 1080, il faut changer *Resolution X* et *Y*, puis les remettre pour les autres vues.
- Tant que *Lock Camera to View* est actif, chaque geste de navigation déplace la caméra : un coup d'orbite défait le cadrage. Déverrouillez dès que le cadrage est bon.
- Un PNG aux couleurs différentes du rendu : la rubrique *Color Management* de la fenêtre d'enregistrement est passée sur *Override*.
- Une profondeur de champ sans effet : *Focus on Object* est vide, ou la mise au point tombe sur le fond.
- Le détail lui-même est flou : *F-Stop* trop petit pour un gros plan. Le remonter vers 8.
- Un détail coupé net par un plan invisible : la caméra est à moins de 0,1 m de l'objet, sa distance minimale d'affichage par défaut (*Clip Start*, panneau *Lens*). Reculer la caméra et allonger la focale. C'est le même phénomène que le *Clip Start* de la vue, au chapitre 1.

**Quiz prévus (3)**
1. « Pour une vue produit fidèle aux proportions du dessin, quelle focale privilégier ? » Réponse : une longue focale, 85 à 100 mm, avec du recul.
2. « Votre rendu `F12` est terminé. Est-il enregistré sur le disque ? » Réponse : non ; il faut *Image > Save As*.
3. « Vous voulez un PNG sans fond, à poser sur une diapositive. Que réglez-vous ? » Réponse : *Film > Transparent* dans l'onglet *Render*, puis *RGBA* à l'enregistrement.

### Section 4 · Atelier : concept final (`ch4_sec4_title`) · 2:35 (45 min)

**Prérequis déjà vus :** toutes les notions des sections 1 à 3 ; *Pack Resources* (Basics 102 § 4, chapitre 3) ; *File > Append* et la liste des matières (chapitre 3), pour les paliers.
**Nouveau :** rien. L'atelier est la pratique autonome du chapitre ; `CAM_situation` se crée seul, avec les gestes de la section 3. La matière émissive du palier ★★ est fournie toute prête.

Voir « L'atelier final » plus bas pour la situation, les livrables et les paliers.

**Déroulé**
1. **Lancement (3 min).** La situation, les livrables, la grille d'évaluation, le minuteur. Rappelez l'heure de dépôt : 3:15.
2. **Autonomie (37 min).** Régler la lumière définitive, créer `CAM_situation`, exporter les trois vues, empaqueter et enregistrer.
3. **Dépôt (5 min).** Chacun copie ses trois PNG dans `Galerie_PRC02`. Vous vérifiez les noms et lancez le diaporama.

**Points d'observation**
- Le nuancier apparaît dans un visuel : fermer l'œil et l'appareil photo de sa collection avant le rendu.
- La vue de détail sort en 16:9, ou la vue héros en carré : la résolution n'a pas été changée entre deux caméras.
- Un sol qui scintille sous le plateau de bureau : la collection `Studio` est restée visible. La masquer pour la vue de situation.
- Au palier ★, `ABS_Noir.001` ou `PVC_Mat_Noir.001` apparaissent après l'Append du coloris B : ce sont des copies des matières partagées par les deux coloris, sans effet sur le rendu.
- Au palier ★, les deux lampes se touchent : le décalage de 750 mm demandé au chapitre 3 a été oublié ou mal saisi. Aidez l'apprenant à éloigner la copie : clic droit sur `Lampe_coloris_B` dans l'Outliner, *Select Objects*, puis `G X` et une valeur saisie.
- Un apprenant perdu à la fin de la section 3 : il ouvre le fichier de secours, l'enregistre sous `lampe_rendu_v001.blend`, rend visibles les collections « Corrigé éclairage » et « Corrigé caméras » (œil et appareil photo), applique les notes « Corrigé » du LISEZ-MOI, puis commence l'atelier de là.

**Points de contrôle**
- À 2:55, chaque apprenant a exporté au moins la vue héros. Passez d'abord voir ceux qui n'ont pas de post-it vert.
- À 3:15, les trois PNG de chacun sont dans `Galerie_PRC02`, bien nommés.

**Quiz prévu (1, récapitulatif, pour l'application)**
- « Avant d'envoyer vos visuels, que vérifiez-vous ? » Plusieurs bonnes réponses : le nom des fichiers, le format de chaque vue, la gestion des couleurs à l'enregistrement, et un fichier `.blend` empaqueté. Distracteur : « la focale de 50 mm sur toutes les vues ».

### 3:20 · Galerie et restitution (15 min)

**Nouveau :** rien.

- **Diaporama (3 min)** des vues héros, sans commentaire.
- **Restitution (10 min).** Chacun commente sa vue de situation, ou sa vue préférée, en une minute : un choix de lumière, un choix de cadrage. Le groupe pose une question au plus. Appuyez vos retours sur la grille d'évaluation des visuels.
- **Coup de cœur (2 min).** Un post-it vert par personne, sur le visuel d'un autre.

### 3:35 · Bilan de la formation (15 min)

**Nouveau :** rien. C'est un bilan pédagogique : il récapitule, ouvre sur la suite et répond aux questions.

- **Le récapitulatif des six demi-journées (6 min).** Projetez la planche `PRC02_ch4_recapitulatif.png` : une vignette par demi-journée. Pour chacune, le groupe nomme un geste clé.
  1. Prendre ses repères : la maquette en kit.
  2. Modéliser : la rangée de sièges et la clinique du fichier.
  3. Chapitre 1 : le blocage de la lampe.
  4. Chapitre 2 : la lampe remodelée, avec ses modificateurs et ses courbes.
  5. Chapitre 3 : la lampe habillée, ses matières rangées en bibliothèque.
  6. Chapitre 4 : un visuel de la galerie.
  Reliez ce parcours aux cinq objectifs du programme, du blocage aux visuels.
- **Les ressources pour continuer (4 min) :**
  - l'application support : les chapitres, les quiz, les défis et ses mises à jour ;
  - les fichiers de la formation : chaque LISEZ-MOI garde ses consignes par paliers, et les collections « Corrigé » montrent le résultat attendu ;
  - sa bibliothèque CMF du chapitre 3 et le studio du chapitre 4, réutilisables pour ses propres projets ;
  - Poly Haven, pour des HDRI et des textures sous licence CC0 ;
  - le manuel officiel de Blender, en anglais, avec les mêmes libellés que l'interface.
- **Questions et tour de table (5 min) :** les questions du groupe, puis chacun dit en une phrase ce qu'il applique dès la semaine prochaine.

## L'atelier final

### Situation

« Revue de design demain matin. Vous présentez votre concept de lampe au client en trois visuels. Ils doivent faire comprendre la forme, les matières et l'usage. »

Le cadre se transpose à chaque secteur : la revue d'un siège ferroviaire, d'un rétroviseur automobile ou d'une liseuse de cabine d'avion se prépare de la même façon.

### Point de départ

Le point de départ se choisit au lancement de la séance (voir 0:00) :

| Situation de l'apprenant | Fichier | Geste |
|---|---|---|
| Lampe du chapitre 3 exploitable | `PRC02_ch4_studio.blend` | *File > Append* de la collection *Lampe* de `lampe_habillage_v002.blend`, puis *Save As* `lampe_rendu_v001.blend` |
| Lampe absente, incomplète ou abîmée | `PRC02_ch4_lampe_en_studio.blend` | *Save As* `lampe_rendu_v001.blend` |
| Autre objet retenu aux chapitres 2 et 3 | `PRC02_ch4_studio.blend` | Même geste que pour la lampe ; `lampe` devient le nom de l'objet dans les fichiers livrés |

Le fichier de secours reproduit l'état de `lampe_habillage_v002.blend` à la fin du chapitre 3 : la collection *Lampe* en coloris A, la collection `Lampe_coloris_B`, les modificateurs actifs, les échelles à 1 et les matières du corrigé du chapitre 3.

À l'atelier, chacun continue dans son `lampe_rendu_v001.blend`. Celui qui s'est perdu à la section 3 repart du fichier de secours, avec les collections « Corrigé éclairage » et « Corrigé caméras » rendues visibles.

### Livrables

Validés par le formateur le 18 novembre 2026.

| Vue | Caméra | Contenu | Format | Nom du fichier |
|---|---|---|---|---|
| V1 · Héros | `CAM_heros` | La lampe entière en trois quarts avant, câble compris, éclairage de studio, fond cyclo | 1920 × 1080 (16:9), PNG 8 bits *RGB* | `lampe_heros_<initiales>_v001.png` |
| V2 · Détail | `CAM_detail` | Un gros plan, avec profondeur de champ : l'interrupteur cranté et la grille d'aération, une articulation, ou l'ampoule dans la tête | 1080 × 1080 (1:1), PNG 8 bits *RGB* | `lampe_detail_<initiales>_v001.png` |
| V3 · Situation | `CAM_situation` | La lampe dans son usage : sur le plateau de bureau, sous une HDRI d'intérieur ou d'extérieur, ou lampe allumée (palier ★★) | 1920 × 1080 (16:9), PNG 8 bits *RGB* | `lampe_situation_<initiales>_v001.png` |

S'y ajoute le fichier de scène `lampe_rendu_v00x.blend`, ressources empaquetées (*File > External Data > Pack Resources*).

**Convention de nommage :** `<objet>_<vue>_<initiales>_v<version>.png`, en minuscules, sans accent ni espace ; les initiales en majuscules. Exemple : `lampe_heros_MJ_v001.png`. Les images sont enregistrées dans `rendus/`, à côté du fichier `.blend`, puis copiées dans `Galerie_PRC02`.

### Paliers

Les paliers ne réinvestissent que des notions du chapitre ou des chapitres précédents.

- **Socle :** les trois vues, exportées et nommées ; le fichier de scène empaqueté.
- **★ :**
  - une version à fond transparent de la vue héros (*Film > Transparent*, *RGBA*) ;
  - une vue technique de profil, avec une caméra *Orthographic* face à la lampe et `Monde_Neutre` éclairé par le studio ;
  - la gamme : *File > Append* de la collection `Lampe_coloris_B` de `lampe_habillage_v002.blend` (le geste du lancement), puis une caméra `CAM_gamme` qui cadre les deux lampes côte à côte : `lampe_gamme_<initiales>_v001.png`. Dans le fichier de secours, `Lampe_coloris_B` est déjà là : ouvrir son œil et son appareil photo.
- **★★ :**
  - la lampe allumée pour la vue de situation : un *Spot* dans la tête, *Temperature* à 2700 K, la collection `Eclairage_studio` éteinte, et sur l'ampoule la matière fournie `Ampoule_allumee`, choisie dans la liste des matières (chapitre 3). Le réglage de l'émission n'est pas demandé : il n'a été vu qu'en défi au chapitre 3 ;
  - le même studio pour un autre objet : la liseuse de cabine du défi du chapitre 2, la maquette en kit ou la rangée de sièges de l'initiation.

### Grille d'évaluation des visuels (pour le formateur)

Elle guide vos retours pendant le tour des postes et la galerie.

| Critère | Atteint | Partiel | Non atteint |
|---|---|---|---|
| Les livrables sont conformes : trois vues, formats et noms | ☐ | ☐ | ☐ |
| La forme se lit : silhouette détachée du fond, volumes modelés par la lumière | ☐ | ☐ | ☐ |
| Les matières sont crédibles : métal, laque, plastique et verre se reconnaissent | ☐ | ☐ | ☐ |
| Le cadrage est maîtrisé : focale adaptée, composition, aucune coupe gênante | ☐ | ☐ | ☐ |
| Le fichier est propre : caméras et lumières nommées, ressources empaquetées | ☐ | ☐ | ☐ |

## Fichiers d'exercice à construire

Ces fichiers seront construits par la session principale, avec le MCP Blender. Ce plan les décrit sans les créer ni rien télécharger.

### Fichiers de travail et corrigés

Le chapitre suit la convention commune aux chapitres 2 à 4 :
- le corrigé de chaque exercice et de l'atelier se trouve dans le fichier de travail, dans une collection masquée (œil fermé) dont le nom commence par « Corrigé » ;
- le LISEZ-MOI indique en une ligne où le trouver ;
- un fichier séparé n'existe que si le résultat ne tient pas dans une collection (réglages de rendu, monde, images exportées) ou s'il sert de fichier de secours.

Toute la séance se passe dans un seul fichier de travail, `lampe_rendu_v001.blend`. Il naît du studio (`PRC02_ch4_studio.blend` et l'Append de la lampe) ou du fichier de secours (`PRC02_ch4_lampe_en_studio.blend`). Les deux contiennent les mêmes collections « Corrigé ».

| Exercice ou atelier | Moment du minutage | Fichier de travail | Où se trouve le corrigé |
|---|---|---|---|
| Lancement : la lampe dans le studio | 0:00 à 0:10 | `PRC02_ch4_studio.blend`, puis Append de la collection *Lampe* de `lampe_habillage_v002.blend` | Fichier séparé : `PRC02_ch4_lampe_en_studio.blend`. Raison : c'est le fichier de secours, et il montre la lampe en place dans le studio. |
| Section 1 · Le banc d'essai EEVEE | 0:10 à 0:40 | `lampe_rendu_v001.blend` | Note « Corrigé » du LISEZ-MOI : *Raytracing* coché, *Render > Samples* 128, *View* *Khronos PBR Neutral*. Raison : trois réglages de la scène, qui ne tiennent pas dans une collection ; une note suffit, et l'image `PRC02_ch4_comparatif_moteurs.png` en montre l'effet. Un fichier séparé pèserait 13 Mo pour trois cases. |
| Section 2 · Éclairer par HDRI | 0:40 à 1:00 | `lampe_rendu_v001.blend` | Note « Corrigé » du LISEZ-MOI : `Monde_Interieur` et la valeur de sa rotation Z. Raison : un monde n'est pas dans une collection, et le réglage tient en une ligne. |
| Section 2 · Éclairer en studio | 1:10 à 1:45 | `lampe_rendu_v001.blend` | Collection masquée « Corrigé éclairage », avec `Monde_Neutre` rappelé dans le LISEZ-MOI. |
| Section 3 · Caméra, composition et export | 1:45 à 2:25 | `lampe_rendu_v001.blend` | Collection masquée « Corrigé caméras ». Images séparées : `PRC02_ch4_corrige_heros.png` et `PRC02_ch4_corrige_detail.png`. Raison : ce sont des images exportées. |
| Atelier · Le concept final | 2:35 à 3:20 | `lampe_rendu_v001.blend` | Collections masquées « Corrigé caméras » (`CAM_situation_corrige`) et « Corrigé paliers ». Images séparées : les trois PNG du corrigé, plus `PRC02_ch4_corrige_situation_allumee.png` pour le palier ★★. |

Il n'y a donc que deux fichiers `.blend` : le studio et le fichier de secours. Aucun fichier `_fini` n'est prévu. Les images du corrigé accompagnent le fichier de secours et servent de figures dans l'application.

**Point de reprise :** un apprenant perdu en cours de séance ouvre le fichier de secours, l'enregistre sous `lampe_rendu_v001.blend`, ouvre l'œil et l'appareil photo des collections « Corrigé » utiles, puis applique les notes « Corrigé » du LISEZ-MOI.

### Règles communes

- **Version :** Blender 5.2 LTS. Construction en arrière-plan (`blender.exe -b --factory-startup`), puis une courte fenêtre pour la taille des zones, comme pour l'initiation (`finish_ui.py`).
- **Unités :** *Metric*, *Length* en *Millimeters*, *Unit Scale* 1,0, comme aux chapitres 1 à 3. Toutes les cotes ci-dessous sont en mètres, dans le repère du monde.
- **Moteur et sortie :** EEVEE. *Render > Samples* 64, *Viewport > Samples* 16, *View* *AgX*, *Look* *None*, *Exposure* 0. *Output* : 1920 × 1080, 100 %, PNG *RGB* 8 bits, chemin `//rendus/`, *Film > Transparent* décoché.
- **Raytracing, un choix assumé :** le studio et le fichier de secours ont la case *Raytracing* décochée, comme un fichier neuf. `lampe_habillage_v002.blend` l'a cochée, mais la case appartient à la scène et ne suit pas l'Append. Elle est donc décochée pour tous au début de la séance, qu'on arrive par Append ou par le fichier de secours. Le cycle 3 de la section 1 s'appuie sur cet écart pour l'expliquer. La note « Corrigé » de la section 1 la donne cochée.
- **Propreté :** ressources empaquetées, chemins relatifs, aucun chemin absolu caché (`ImagePackedFile.filepath` en relatif ; navigateur de fichiers en `//`), aucun texte d'extension, `save_version = 0` pour éviter le `.blend1`.
- **Noms uniques :**
  - les objets du corrigé portent le suffixe `_corrige`. Les apprenants peuvent ainsi nommer leurs propres lumières et caméras `Key` ou `CAM_heros` sans obtenir `Key.001` ;
  - aucune matière du studio ne reprend un nom de matière du chapitre 3 (`Chrome`, `ABS_Noir`, `Verre_Clair`…) : l'Append de la lampe ne crée pas de doublon `.001`.
- **Lumières :** toutes les lumières du corrigé ont la case *Temperature* cochée.
- **Mondes :** chaque monde reçoit un *Fake User*. Sans lui, un monde inactif disparaît à l'enregistrement. Les quatre mondes sont dans les deux fichiers.
- **Collections « Corrigé » :** trois collections, œil fermé et appareil photo désactivé : « Corrigé éclairage », « Corrigé caméras » et « Corrigé paliers ». Pour en voir une au rendu, on ouvre son œil et son appareil photo.
- **LISEZ-MOI :** un texte `LISEZ-MOI` affiché dans un éditeur de texte en bas de l'écran. Chaque section y a sa ligne « Corrigé ». Son contenu est donné en annexe.

### `PRC02_ch4_studio.blend` · le studio

**Moments :** lancement, point de départ de ceux qui amènent leur lampe ; toute la séance, puisqu'il devient `lampe_rendu_v001.blend` ; base du fichier de secours.

**La lampe de référence,** pour caler le studio : le corrigé du chapitre 2 (`PRC02_ch2_lampe_modele.blend`, cotes de son plan), que le chapitre 3 habille sans le déplacer.
- Socle de Ø 0,180, centré sur l'origine, posé à Z = 0.
- Corps de la lampe : X de −0,09 à 0,313 (bord de la tête), Y de −0,09 à 0,09, Z de 0 à 0,442 (haut de l'articulation du haut), soit environ 0,45 m.
- Câble posé au sol, de la base du socle jusqu'à (−0,333 ; −0,02), entre Y = −0,02 et Y = 0,053.
- Tête inclinée de 30° (rotation Y −30°), ouverture centrée en (0,261 ; 0 ; 0,324), de rayon 0,060.
- Interrupteur en (0,055 ; 0 ; 0,028) ; grille d'aération : 36 lamelles en couronne, de rayon 0,070 à 0,082, sur le dessus du socle.

Point de visée commun : `T` = (0,11 ; 0 ; 0,22), au centre du corps de la lampe.

Les cadrages ci-dessous ont été vérifiés dans Blender 5.2.1, par projection des points extrêmes de la lampe dans chaque caméra :
- toute la lampe, câble compris, entre dans `CAM_banc_essai`, `CAM_heros_corrige`, `CAM_situation_corrige` et `CAM_profil_ortho_corrige` ; les deux lampes entrent dans `CAM_gamme_corrige` ;
- le nuancier entre en partie dans `CAM_heros_corrige` : il est masqué avant chaque export ;
- les coins bas des cadres tombent sur le sol du studio, ou sur le plateau pour `CAM_situation_corrige` ;
- dans `CAM_detail_corrige`, l'interrupteur est au tiers droit du cadre, à 0,39 m de la caméra, et le fond est le sol du studio.

**Collections et objets**

| Collection | Visibilité à l'ouverture | Objet | Description, cotes en mètres |
|---|---|---|---|
| `Studio` | Visible | `Fond_cyclo` | Fond courbe d'une seule pièce. Largeur 4,0 (X de −1,9 à 2,1) : la vue héros, en trois quarts, voit loin sur la gauche du mur. Sol à Z = 0, de Y = −1,4 à Y = 0,5. Raccord en quart de cercle de rayon 0,4 (centre Y = 0,5 ; Z = 0,4), 16 segments. Mur à Y = 0,9, de Z = 0,4 à Z = 1,6. Lissage *Shade Auto Smooth*. Matière `Fond_studio` : *Base Color* #C8C8C8, *Roughness* 0,7. |
| `Studio` | Visible | `CAM_banc_essai` | Caméra active à l'ouverture, pour les sections 1 et 2. Focale 60 mm. Position (0,55 ; −2,30 ; 0,55), visée (0,22 ; −0,03 ; 0,18). Elle cadre toute la lampe, câble compris, et le nuancier. |
| `Nuancier` | Visible | `Nuancier_rouge`, `Nuancier_bleu`, `Nuancier_blanc`, `Ref_chrome`, `Ref_gris` | Cinq sphères UV de 0,06 de diamètre, 32 segments, lissées, posées au sol (Z = 0,03), alignées en X = 0,45 ; 0,53 ; 0,61 ; 0,69 ; 0,77, à Y = −0,15. Matières : `CMF_rouge` #C8102E, `CMF_bleu` #0057B8 et `CMF_blanc` #F2F2F2, *Roughness* 0,35 ; `Ref_chrome` *Metallic* 1, #E0E0E0, *Roughness* 0,03 ; `Ref_gris_18` gris à 18 % (#767676), *Roughness* 0,5. |
| `Mise_en_situation` | Œil fermé, appareil photo désactivé | `Plateau_bureau` | Pavé de 1,4 × 0,8 × 0,03, dessus à Z = 0, centré en (0,10 ; 0 ; −0,015) : X de −0,6 à 0,8, Y de −0,4 à 0,4. Chant arrondi : *Bevel*, *Amount* 3 mm, 3 segments, *Harden Normals*. Matière `Bois_clair` : le placage de chêne `oak_veneer_01` de Poly Haven (CC0) en projection *Box*, la chaîne du chapitre 3 : *Texture Coordinate* (*Object*) > *Mapping* (*Scale* 0,546, l'image couvrant 1,83 m ; *Rotation* Z 90°, le fil dans la longueur) > trois *Image Texture* en *Box*, *Blend* 0,25 : couleur 2K (sRGB) dans *Base Color*, rugosité 1K (*Non-Color*) dans *Roughness*, relief 2K (*Non-Color*) dans un *Bump* (*Strength* 0,15). Couleur en mode *Solid* : #B89268. |
| `Mise_en_situation` | idem | `Carnet` | Pavé de 0,21 × 0,148 × 0,012, en (0,24 ; −0,14 ; 0,006), tourné de −15° en Z. Il donne l'échelle sur le bureau et ne touche ni le socle ni le câble. Matière `Papier` : #E9E4D8, *Roughness* 0,8. |
| « Corrigé éclairage » | Œil fermé, appareil photo désactivé | Lumières du studio | Corrigé de la séquence studio. Voir le tableau suivant. |
| « Corrigé caméras » | idem | Caméras et *Empty* de mise au point | Corrigé de la section 3 et de la vue de situation de l'atelier. |
| « Corrigé paliers » | idem | *Spot* de la lampe allumée, caméras de la gamme et du profil | Corrigé des paliers ★ et ★★. |

**La matière fournie `Ampoule_allumee`** (palier ★★) : *Principled BSDF*, *Base Color* #FFF4E0, *Roughness* 0,4, *Emission Color* #FFA957 (environ 2700 K), *Emission Strength* 10. Aucun objet ne la porte : elle reçoit un *Fake User*, pour rester dans le fichier et apparaître dans la liste des matières de l'ampoule. *Emission Strength* est à caler au premier rendu, `Spot_lampe_corrige` allumé.

**Les collections « Corrigé ».** Les puissances sont des valeurs de départ, à caler au premier rendu (*Khronos PBR Neutral*, *Exposure* 0, `Monde_Neutre`) : ni blanc brûlé ni ombres bouchées. Ces réglages de rendu sont ceux des notes « Corrigé » du LISEZ-MOI.

| Collection | Objet | Type et réglages | Position | Visée |
|---|---|---|---|---|
| « Corrigé éclairage » | `Key_corrige` | *Area* *Square*, *Size* 0,5, 20 W, *Temperature* 5500 K | (−0,60 ; −0,90 ; 0,90) | `T` |
| « Corrigé éclairage » | `Fill_corrige` | *Area* *Square*, *Size* 0,8, 5 W, *Temperature* 6000 K | (1,00 ; −0,60 ; 0,45) | `T` |
| « Corrigé éclairage » | `Rim_corrige` | *Area* *Square*, *Size* 0,3, 15 W, *Temperature* 6500 K | (0,30 ; 0,80 ; 0,90) | La tête, (0,23 ; 0 ; 0,38) |
| « Corrigé éclairage » | `Reflet_bande_corrige` | *Area* *Rectangle*, *Size X* 1,0, *Size Y* 0,06, 10 W | (0,15 ; −0,35 ; 0,95) | Vers le bas, orientée au montage pour que la ligne de reflet passe sur la tête laquée, vue depuis `CAM_heros_corrige` |
| « Corrigé caméras » | `CAM_heros_corrige` | Focale 85 mm, *Composition Guides* *Thirds* | (1,60 ; −2,10 ; 0,65) | `T` |
| « Corrigé caméras » | `CAM_detail_corrige` | Focale 100 mm, *Depth of Field* actif, *Focus on Object* `Mise_au_point_corrige`, *F-Stop* 8 | (0,33 ; −0,22 ; 0,20) | (0,035 ; −0,01 ; 0,03) : l'interrupteur cranté et l'arc de la grille d'aération ; l'articulation et les tiges du bras du bas, floues, à l'arrière-plan |
| « Corrigé caméras » | `Mise_au_point_corrige` | *Empty* *Plain Axes*, taille 0,02 | Sur l'interrupteur, (0,055 ; 0 ; 0,031) | — |
| « Corrigé caméras » | `CAM_situation_corrige` | Focale 35 mm | (−0,30 ; −0,85 ; 0,45) : le regard d'une personne assise au bureau | (0 ; 0 ; 0,21) |
| « Corrigé paliers » | `Spot_lampe_corrige` | *Spot*, *Beam Shape* : *Angle* 70°, *Blend* 0,3, 12 W, *Temperature* 2700 K, *Radius* 0 (valeur d'usine) | (0,254 ; 0 ; 0,338) : dans la tête, juste devant la pointe de l'ampoule | Rotation Y −30°, comme la tête : le faisceau sort par l'ouverture |
| « Corrigé paliers » | `CAM_gamme_corrige` | Focale 70 mm | (0,85 ; −3,00 ; 0,70) | (0,37 ; 0 ; 0,20) : la lampe et `Lampe_coloris_B`, décalée de 0,75 m en X |
| « Corrigé paliers » | `CAM_profil_ortho_corrige` | *Type* *Orthographic*, *Orthographic Scale* 0,95 | (−0,01 ; −2,00 ; 0,40) | Rotation X 85° : vue de face, dans l'axe Y, qui montre le profil des bras ; 5° de plongée font apparaître le sol sous la lampe |

Les caméras et les lumières sont orientées vers leur cible pendant la construction, puis la contrainte est retirée : aucune contrainte ne reste dans le fichier. À vérifier au montage :
- aucun bord du fond n'apparaît dans `CAM_banc_essai`, `CAM_heros_corrige`, `CAM_detail_corrige` ni `CAM_gamme_corrige` ;
- le câble entier est dans `CAM_banc_essai`, `CAM_heros_corrige` et `CAM_situation_corrige` ;
- le bas du cadre de `CAM_situation_corrige` reste sur le plateau de bureau.

**Les mondes**

| Monde | Contenu | À l'ouverture |
|---|---|---|
| `Monde_Studio` | HDRI `studio.exr`, fournie avec Blender, *Strength* 1,0 | Actif : il éclaire les sections 1 et 2 |
| `Monde_Interieur` | HDRI `artist_workshop` 2K, de Poly Haven, *Strength* 1,0 | *Fake User* |
| `Monde_Exterieur` | HDRI `docklands_01` 2K, de Poly Haven, *Strength* 1,0, réglages *Sun* d'usine | *Fake User* |
| `Monde_Neutre` | Couleur unie gris très sombre (valeur linéaire 0,03), *Strength* 1,0 | *Fake User* : il sert à partir de la séquence studio |

Chaque monde à HDRI suit le même câblage : *Texture Coordinate* (*Generated*) → *Mapping* (*Point*, rotation Z à 0°) → *Environment Texture* (image empaquetée) → *Background* → *World Output*. Les HDRI sont décrites plus bas.

**Vue d'ouverture**
- Espace de travail *Layout*. Rien n'est sélectionné.
- Vue 3D en perspective, mode *Material Preview*, depuis un angle proche de `CAM_banc_essai`, la lampe et le nuancier cadrés. On n'est pas en vue caméra.
- Outliner : les collections `Studio`, `Nuancier`, `Mise_en_situation` et les trois collections « Corrigé » repliées.
- Éditeur de propriétés sur l'onglet *Render* : la section 1 commence là.
- En bas, à la place de la *Timeline*, l'éditeur de texte sur `LISEZ-MOI`, à la hauteur des fichiers de l'initiation (151 px).

**Taille estimée :** environ 13 Mo, presque tout dans les deux HDRI 2K.

### `PRC02_ch4_lampe_en_studio.blend` · le fichier de secours

**Moments :** lancement, pour ceux dont la lampe du chapitre 3 n'est pas exploitable ; corrigé du lancement, puisqu'il montre la lampe en place dans le studio ; point de reprise pour un apprenant perdu en cours de séance. Il sert aussi au formateur pour ses démos et pour fabriquer les images du corrigé.

**Pourquoi un fichier séparé :** c'est le fichier de secours que demande le critère 4 du découpage.

**Contenu :** le studio tel quel, collections « Corrigé » comprises, avec en plus les deux collections de `lampe_habillage_v002.blend`, dans leur état de fin du chapitre 3.
- **`Lampe`, visible : le coloris A.**
  - Pièces, avec les noms du chapitre 2 : `Socle`, `Grille_aeration` et son *Empty* `Grille_pivot`, `Interrupteur`, `Interrupteur_crans` et son *Empty* `Interrupteur_pivot`, `Articulation_bas`, `Articulation_milieu`, `Articulation_haut`, `Bras_bas` et `Bras_haut` (deux tiges chacun, par *Mirror*), `Tête`, `Douille`, `Ampoule` (courbe et *Screw*), `Câble` (courbe).
  - Position du chapitre 2 : socle centré sur l'origine, posé à Z = 0.
  - Matières du cahier CMF du chapitre 3 : `Structure_Vert` (socle), `Peinture_Vert` laquée (tête), `ABS_Noir` grainé (grille, interrupteur et ses crans), `Alu_Brosse` (bras), `Chrome` (articulations), `PVC_Mat_Noir` (câble), `Alu_Naturel` (douille), `Verre_Clair` avec *Thin Wall* et *Raytraced Transmission* cochés (ampoule).
- **`Lampe_coloris_B` : le coloris B.**
  - Les mêmes pièces, sous les noms que leur donne *Duplicate Collection* (`Socle.001`…), décalées de + 0,75 m en X, comme le demande l'atelier du chapitre 3. Ce décalage évite que le câble de l'une traverse le socle de l'autre.
  - Œil fermé et appareil photo désactivé à l'ouverture : elle n'entre dans le cadre qu'au palier ★ de la gamme.
  - Matières : `Structure_Blanche`, `Laque_Blanche`, `Alu_Anodise_Noir` brossé, `Laiton` (articulations, douille), `Verre_Depoli` ; `ABS_Noir` et `PVC_Mat_Noir` partagés avec le coloris A.
- Matières marquées comme actifs et rangées en catalogues, comme à la fin du chapitre 3 ; image `grain_structure.png` empaquetée ; aucune matière liée.
- Modificateurs actifs, jamais appliqués ; échelles à 1 ; rotations des bras non appliquées.
- Scène : celle du studio, *Raytracing* décoché (voir « Règles communes »).

**Source :** `PRC02_ch3_lampe_habillage.blend`, la lampe habillée du chapitre 3 (sa fiche A2). C'est l'état attendu de `lampe_habillage_v002.blend`. Ses collections `Lampe` et `Lampe_coloris_B` sont ramenées dans le studio par *File > Append*, le geste même des apprenants, sans renommage ni déplacement.

**Vue d'ouverture :** celle du studio. **LISEZ-MOI :** celui du studio, avec la rubrique « Démarrer (fichier de secours) ».

### Les images du corrigé et du formateur

Ce sont des fichiers séparés, puisque ce sont des images exportées. Elles sont toutes rendues depuis une copie de travail de `PRC02_ch4_lampe_en_studio.blend`, jamais enregistrée par-dessus le fichier de secours, avec les réglages des notes « Corrigé » : *Raytracing* coché, 128 échantillons, *Khronos PBR Neutral*.

| Fichier | Moment | Fabrication |
|---|---|---|
| `PRC02_ch4_corrige_heros.png` | Lancement ; corrigé de la section 3 et de l'atelier ; galerie ; figure | `Monde_Neutre`, « Corrigé éclairage » visible au rendu, `CAM_heros_corrige`, 1920 × 1080, nuancier masqué. |
| `PRC02_ch4_corrige_detail.png` | idem | Même lumière, `CAM_detail_corrige`, 1080 × 1080. |
| `PRC02_ch4_corrige_situation.png` | Lancement ; corrigé de l'atelier ; galerie ; figure | `Monde_Interieur` ; collection `Mise_en_situation` visible ; `Studio`, `Nuancier` et « Corrigé éclairage » masquées (œil et appareil photo) ; `CAM_situation_corrige`, 1920 × 1080. |
| `PRC02_ch4_corrige_situation_allumee.png` | Corrigé du palier ★★ ; figure | Comme la vue de situation, mais `Monde_Neutre`, `Spot_lampe_corrige` allumé et la matière `Ampoule_allumee` sur l'ampoule. |
| `PRC02_ch4_comparatif_moteurs.png` | Section 1, cycle 2 ; figure | `CAM_banc_essai`, `Monde_Studio`, en 1280 × 720 : *Viewport Render Image* en *Material Preview* ; EEVEE à 64 échantillons, *Raytracing* coché ; Cycles à 128 échantillons, débruité. Les trois images côte à côte, chacune légendée avec son moteur et son temps de rendu. Le poste de mesure, carte graphique comprise, est cité dans la légende. |
| `PRC02_ch4_recapitulatif.png` | Bilan | Planche 1920 × 1080 de six vignettes légendées, une par demi-journée : la maquette en kit ; la rangée de sièges et la clinique du fichier ; le blocage de la lampe ; la lampe remodelée ; la lampe habillée en deux coloris ; la vue héros du corrigé. Faite à partir des fichiers d'exercice de chaque demi-journée et de leurs corrigés, sans modifier les fichiers déjà livrés. |

### Les HDRI

**Décision du formateur (18 novembre 2026) : option A + B.** Les HDRI fournies avec Blender pour le studio ; deux HDRI 2K de Poly Haven pour l'intérieur et l'extérieur. Rien n'a été téléchargé. La session principale demandera l'accord du formateur avant de télécharger les deux HDRI 2K, au moment de construire les fichiers. Les informations de Poly Haven ont été lues le 18 novembre 2026 sur le site et dans son API publique.

**La licence.** Poly Haven publie toutes ses HDRI sous licence CC0 : tout usage est permis, y compris commercial, et l'attribution n'est pas obligatoire (<https://polyhaven.com/license>). Les HDRI fournies avec Blender 5.2 sont aussi sous licence CC0, d'après leur fichier `license.txt` : créées par Greg Zaal pour Poly Haven, en définition 1K.

| Monde | HDRI | Source | Auteur | Définition et poids |
|---|---|---|---|---|
| `Monde_Studio` | `studio.exr` | Fournie avec Blender : `C:\Program Files\Blender Foundation\Blender 5.2\5.2\datafiles\studiolights\world\` ; probablement `studio_small_01` de Poly Haven, selon `license.txt` | Greg Zaal | 1K, moins de 1 Mo |
| `Monde_Interieur` | `artist_workshop` : atelier d'artiste, lumière du jour par la fenêtre, faible contraste | [polyhaven.com/a/artist_workshop](https://polyhaven.com/a/artist_workshop), fichier 2K au format `.hdr` | Oliksiy Yakovlyev | 2K, 6,4 Mo |
| `Monde_Exterieur` | `docklands_01` : quai pavé et rivière, ciel partiellement nuageux, faible contraste | [polyhaven.com/a/docklands_01](https://polyhaven.com/a/docklands_01), fichier 2K au format `.hdr` | Savva Zakharov | 2K, 6,1 Mo |

**Pourquoi ce partage :** derrière le fond cyclo, l'HDRI du studio ne se voit que dans les reflets, et la 1K suffit. L'intérieur et l'extérieur apparaissent en fond dans la vue de situation : la 2K y est plus nette.

**Remplaçantes,** mêmes licence et poids, si l'une ne convient pas au montage : [`blender_institute`](https://polyhaven.com/a/blender_institute) pour l'intérieur (Greg Zaal), [`dresden_square`](https://polyhaven.com/a/dresden_square) pour l'extérieur (Greg Zaal).

**Poids :** environ 12,5 Mo d'HDRI par fichier `.blend`, soit environ 13 Mo par fichier et 26 Mo pour les deux fichiers du chapitre, le studio et le fichier de secours.

## Captures à prévoir

Une capture par menu, bouton ou panneau cité, numérotée « Figure 4.N » sur tout le chapitre. Côte à côte : environ 600 × 400 px ; pleine largeur pour les comparatifs et les captures riches en texte. Les panneaux repliés de l'éditeur de propriétés demandent un clic du formateur avant la capture (voir la note de passation du chapitre 1).

### Section 1 · Paramétrage d'EEVEE

| Fichier | Contenu | Mise en page |
|---|---|---|
| `shading_pie_menu_blender.jpg` | Le menu circulaire `Z` des modes d'affichage | Côte à côte |
| `material_preview_popover_blender.jpg` | Le menu *Viewport Shading* en *Material Preview* : images d'environnement, *Scene Lights*, *Scene World*, *World Opacity*. Produite par le chapitre 3 (figure 3.3), réutilisée ici | Côte à côte |
| `rendered_popover_blender.jpg` | Le même menu en *Rendered* : *Scene Lights*, *Scene World*, *Render Pass* | Côte à côte |
| `engines_comparison_blender.jpg` | *Material Preview*, EEVEE et Cycles, avec les temps de rendu | Pleine largeur |
| `render_engine_menu_blender.jpg` | L'onglet *Render*, menu *Render Engine* ouvert | Côte à côte |
| `render_window_slots_blender.jpg` | La fenêtre de rendu : menu *Slot* et temps de rendu | Pleine largeur |
| `eevee_sampling_panel_blender.jpg` | Le panneau *Sampling* : *Viewport*, *Render*, *Shadows* | Côte à côte |
| `eevee_raytracing_panel_blender.jpg` | Le panneau *Raytracing* activé : *Method*, *Resolution*, *Fast GI Approximation* | Côte à côte |
| `raytracing_off_on_blender.jpg` | Les articulations chromées, la tête laquée et l'ampoule, sans puis avec *Raytracing* | Pleine largeur |
| `material_settings_transmission_blender.jpg` | L'onglet *Material*, panneau *Settings* : *Render Method*, *Raytraced Transmission*, *Thickness*. Produite par le chapitre 3 (figure 3.12), réutilisée ici | Côte à côte |
| `color_management_panel_blender.jpg` | Le panneau *Color Management*, menu *View* ouvert | Côte à côte |
| `view_transform_comparison_blender.jpg` | Le nuancier en *AgX*, *Standard* et *Khronos PBR Neutral* | Pleine largeur |

### Section 2 · Éclairage de studio et HDRI

| Fichier | Contenu | Mise en page |
|---|---|---|
| `world_browse_menu_blender.jpg` | Le sélecteur de monde, avec les quatre mondes du studio | Côte à côte |
| `world_surface_panel_blender.jpg` | L'onglet *World*, panneau *Surface* : *Color*, *Strength* | Côte à côte |
| `world_color_link_menu_blender.jpg` | Le menu ouvert depuis le bouton du champ *Color*, avec *Environment Texture* | Côte à côte |
| `world_hdri_rotation_blender.jpg` | L'onglet *World* avec l'HDRI chargée et la rotation Z du *Mapping* | Côte à côte |
| `shader_editor_world_type_blender.jpg` | Le menu du Shader Editor passé de *Object* à *World* | Côte à côte |
| `world_nodes_hdri_blender.jpg` | Les nœuds du monde dans l'espace *Shading* | Pleine largeur |
| `hdri_comparison_blender.jpg` | La lampe sous les trois HDRI | Pleine largeur |
| `world_sun_settings_blender.jpg` | Option : *World > Settings > Sun* (*Threshold*, *Angle*) | Côte à côte |
| `add_light_menu_blender.jpg` | Le sous-menu *Add > Light* | Côte à côte |
| `light_types_comparison_blender.jpg` | La lampe éclairée par *Point*, *Sun*, *Spot* et *Area* | Pleine largeur |
| `light_properties_area_blender.jpg` | L'onglet *Light* d'une *Area* : la case *Temperature* cochée et sa valeur, *Power*, *Shape*, *Size* | Côte à côte |
| `area_size_comparison_blender.jpg` | Une petite et une grande *Area* : ombre et reflet | Pleine largeur |
| `three_point_lighting_top_blender.jpg` | Vue de dessus : `Key`, `Fill` et `Rim` autour de la lampe | Côte à côte |
| `three_point_steps_blender.jpg` | `Key` seule, `Key` et `Fill`, puis les trois | Pleine largeur |
| `outliner_lights_collection_blender.jpg` | La collection `Eclairage_studio` dans l'Outliner, avec ses yeux | Côte à côte |
| `strip_light_reflection_blender.jpg` | Une *Area* *Rectangle* et sa ligne de reflet sur la tête laquée | Côte à côte |

### Section 3 · Caméra, composition et export

| Fichier | Contenu | Mise en page |
|---|---|---|
| `view_cameras_menu_blender.jpg` | Le sous-menu *View > Cameras* : *Set Active Object as Camera*, *Align Active Camera to View* | Côte à côte |
| `sidebar_view_lock_camera_blender.jpg` | La barre latérale, onglet *View*, *View Lock* : *Lock Camera to View* | Côte à côte |
| `camera_view_passepartout_blender.jpg` | La vue caméra, cadre et *Passepartout* | Pleine largeur |
| `camera_lens_panel_blender.jpg` | L'onglet *Camera*, panneau *Lens* : *Type*, *Focal Length*, *Clip Start* | Côte à côte |
| `focal_length_comparison_blender.jpg` | Le même cadrage à 24, 50 et 100 mm | Pleine largeur |
| `composition_guides_menu_blender.jpg` | *Viewport Display > Composition Guides* ouvert | Côte à côte |
| `camera_thirds_overlay_blender.jpg` | La vue caméra avec les tiers, la tête sur un point fort | Côte à côte |
| `camera_dof_panel_blender.jpg` | Le panneau *Depth of Field* : *Focus on Object*, *F-Stop* | Côte à côte |
| `dof_comparison_blender.jpg` | L'interrupteur et la grille à *F-Stop* 1,4 puis 8 | Pleine largeur |
| `output_format_panel_blender.jpg` | L'onglet *Output*, panneau *Format* : résolution, *Resolution Scale*, bouton des préréglages | Côte à côte |
| `format_presets_menu_blender.jpg` | Le menu des préréglages de format | Côte à côte |
| `render_menu_blender.jpg` | Le menu *Render* : *Render Image*, *View Render* | Côte à côte |
| `image_save_as_blender.jpg` | La fenêtre *Save As* : *PNG*, *RGB*/*RGBA*, *Color Depth*, *Color Management* (*Follow Scene*) | Pleine largeur |
| `eevee_film_panel_blender.jpg` | Le panneau *Film* : *Filter Size*, *Transparent* | Côte à côte |
| `viewport_render_menu_blender.jpg` | Option : *View > Viewport Render Image* | Côte à côte |
| `render_region_blender.jpg` | Option : une *Render Region* tracée en vue caméra | Côte à côte |

### Section 4 · Atelier et défis

| Fichier | Contenu | Mise en page |
|---|---|---|
| `append_collection_browser_blender.jpg` | *File > Append*, dossier *Collection* de `lampe_habillage_v002.blend` : *Lampe* et `Lampe_coloris_B` | Pleine largeur |
| `atelier_heros_blender.jpg`, `atelier_detail_blender.jpg`, `atelier_situation_blender.jpg` | Les trois visuels du corrigé | Pleine largeur |
| `ortho_camera_profile_blender.jpg` | Palier ★ : la vue technique orthographique | Côte à côte |
| `lamp_gamme_two_colorways_blender.jpg` | Palier ★ : les coloris A et B côte à côte, dans le studio | Pleine largeur |
| `lamp_on_situation_blender.jpg` | Palier ★★ : la lampe allumée, le *Spot* dans la tête, `Ampoule_allumee` sur l'ampoule | Pleine largeur |
| `spot_light_beam_angle_blender.jpg` | Défi : l'onglet *Light* d'un *Spot*, rubrique *Beam Shape* : *Angle* et *Blend* | Côte à côte |
| `principled_emission_panel_blender.jpg` | Défi : la rubrique *Emission* de la matière. Produite par le chapitre 3 (figure 3.14), réutilisée ici | Côte à côte |
| `compositor_glare_bloom_blender.jpg` | Défi : le nœud *Glare* en *Bloom* | Pleine largeur |
| `timeline_bind_camera_blender.jpg` | Défi : les marqueurs liés aux caméras dans la *Timeline* | Pleine largeur |
| `output_path_panel_blender.jpg` | Défi : le panneau *Output*, chemin `//rendus/` et format | Côte à côte |
| `damped_track_constraint_blender.jpg` | Défi : la contrainte *Damped Track* d'une lumière vers un *Empty* | Côte à côte |

Réutilisées sans nouvelle capture : la liste des matières, `material_browse_list_blender.jpg` (chapitre 3, figure 3.6), pour le palier ★★ ; *Pack Resources*, `external_data_pack_blender.jpg` (Basics 102). Les captures des défis ne sont utiles que si leurs fiches entrent dans l'application. Sinon, le LISEZ-MOI suffit.

## Si vous prenez du retard

Raccourcissez dans cet ordre. On ne sacrifie jamais l'export des trois vues ni le bilan.

| Ordre | Ce que l'on coupe | Temps gagné |
|---|---|---|
| 1 | HDRI : pas de mise en place dans un monde neuf ; on bascule seulement entre les mondes préparés | 3 min |
| 2 | Section 1 : la transformation de vue reste une démo, sans essai | 5 min |
| 3 | Section 3 : la vue de détail sans profondeur de champ | 5 min |
| 4 | Studio : on règle seulement `Key`. `Fill` et `Rim` viennent de la collection « Corrigé éclairage » : déplacer `Fill_corrige` et `Rim_corrige` dans `Eclairage_studio` avec `M`, puis vérifier leur œil et leur appareil photo | 10 min |
| 5 | Galerie : diaporama seul, sans restitution | 10 min |

## Si vous êtes en avance

D'abord les paliers ★ et ★★ de l'atelier. Ensuite, des défis qui ajoutent une notion nouvelle, chacun avec sa fiche dans le LISEZ-MOI :
- **Le spot réglé finement :** *Angle* et *Blend*, rubrique *Beam Shape*, pour un cône de lumière net ou doux sur le plateau.
- **Sa propre ampoule allumée :** la rubrique *Emission* de la matière (*Color*, *Strength*), vue en défi au chapitre 3, au lieu de la matière fournie.
- **L'éclat de l'ampoule :** un nœud *Glare* de type *Bloom* dans le compositeur.
- **Toutes les vues en un seul lancement :** un marqueur par caméra dans la *Timeline*, *Marker > Bind Camera to Markers* (`Ctrl + B`), le chemin de sortie de l'onglet *Output*, puis *Render > Render Animation*.
- **Une présentation tournante (*turntable*)** de 72 images, exportée en vidéo.
- **Des lumières qui suivent la lampe :** une contrainte *Damped Track* vers un *Empty*.
- **Le studio en bibliothèque :** ranger le studio et ses lumières en *asset* dans la bibliothèque du chapitre 3, pour les réutiliser d'un projet à l'autre.

## Coordination avec les chapitres 2 et 3

Les plans `PRC02-plan-chap2.md` et `PRC02-plan-chap3.md`, quasi finaux, ont été relus le 18 novembre 2026, avec leurs notes de passation. Leurs retouches en cours ne changent ni les noms d'objets ni les noms de fichiers. Ce plan ne modifie aucun de leurs fichiers.

### Ce que le chapitre 4 reçoit

| Point | Chapitres 2 et 3 | Dans ce plan |
|---|---|---|
| Fichier d'entrée | `lampe_habillage_v002.blend`, la fin du chapitre 3 | Append de la collection *Lampe* au lancement |
| Collections | *Lampe* en coloris A ; `Lampe_coloris_B`, créée à l'atelier du chapitre 3 | *Lampe* au lancement ; `Lampe_coloris_B` par Append au palier ★ de la gamme, jamais recréée |
| Fichier de secours | — | `PRC02_ch4_lampe_en_studio.blend` reproduit l'état de `lampe_habillage_v002.blend`, coloris B compris |
| Pièces | `Socle`, `Grille_aeration` et `Grille_pivot`, `Interrupteur`, `Interrupteur_crans` et `Interrupteur_pivot`, trois articulations, `Bras_bas` et `Bras_haut` en tiges doubles, `Tête`, `Douille`, `Ampoule`, `Câble` | La vue de détail du corrigé porte sur l'interrupteur cranté et la grille d'aération |
| Dimensions | Hauteur d'environ 0,45 m ; câble au sol jusqu'à X = −0,333 | La lampe de référence du studio et les cadrages sont recalculés sur le corrigé du chapitre 2, câble compris |
| Modificateurs | Actifs, jamais appliqués ; rotations des bras non appliquées | EEVEE les rend tels quels |
| Matières | Cahier CMF du chapitre 3 : chrome sur les articulations, aluminium brossé sur les bras, laque sur la tête, verre *Thin Wall* sur l'ampoule | Le reflet en bande vise la tête laquée ; le *Raytracing* se juge sur le chrome, la laque et le verre |
| *Raytracing* | Coché au chapitre 3 pour le verre, avec une phrase d'explication | Expliqué au cycle 3 de la section 1 ; décoché dans le studio, puisque la case ne suit pas l'Append |
| *Raytraced Transmission*, *Thin Wall* | Vus au chapitre 3 | Rappelés seulement |
| Émission | Encart NOTE et défi ★ au chapitre 3 | Non supposée acquise : la matière `Ampoule_allumee` est fournie pour le palier ★★ |
| Nœuds | Shader Editor, *Texture Coordinate*, *Mapping* (chapitre 3) | Lecture des nœuds du monde, rotation de l'HDRI |
| Append et Link | Chapitre 3, section 3, qui annonce la réutilisation au chapitre 4 | Append réinvesti sans nouvelle explication |
| Monde, HDRI, lumières, caméra | Absents des chapitres 2 et 3 | Tous au chapitre 4 |
| Captures partagées | `material_preview_popover_blender.jpg` (3.3), `material_settings_transmission_blender.jpg` (3.12), `principled_emission_panel_blender.jpg` (3.14) et `material_browse_list_blender.jpg` (3.6), produites par le chapitre 3 | Réutilisées ici |
| *Clip Start* de la caméra | Signalé par le chapitre 2 | Point d'observation de la section 3 |
| Fil rouge alternatif | Projecteur multisecteur, non recommandé ; liseuse de cabine en défi | Palier ★★ « un autre objet » |

### Incohérences relevées

Les trois points relevés ont été traités à la relecture, le 18 novembre 2026.

1. **Le décalage des lampes au chapitre 3 : harmonisé à 0,75 m en X.**
   - Le chapitre 3 fait saisir `G X = 750mm` à l'atelier.
   - Sa fiche A décale ses corrigés de 0,75 m et de 1,50 m.
   - Avec l'ancien écart de 0,40 m, le câble d'une copie traversait le socle voisin : le câble s'étend jusqu'à X = −0,333, et le socle a un rayon de 0,090.
2. **Le palier de la lampe allumée : un palier ★★.** La section « Coordination » du plan du chapitre 2 a été corrigée.
3. **Le moteur du fichier du chapitre 1**, pour mémoire. Ce fichier est réglé sur Cycles, et sa correction est prévue en fin de projet. Cela n'a pas d'effet au chapitre 4 : le check-up du chapitre 3 traite ce point.

La grille d'aération, signalée comme absente dans la version précédente de ce plan, existe bien depuis le chapitre 2 : ce point est clos.

### Contrôle face aux critères du découpage

| Critère | Comment le plan y répond |
|---|---|
| 1 · Durée | 210 minutes de contenu et 20 minutes de pauses : 3 h 50, sous les 4 heures. |
| 2 · Périmètre | Les quatre ancres `ch4_sec1_title` à `ch4_sec4_title` ; EEVEE, l'éclairage et la caméra. Append est réinvesti, pas réexpliqué. |
| 3 · Pas de redite | Tableau « Ce que le chapitre ne refait pas ». |
| 4 · Continuité | Entrée : `lampe_habillage_v002.blend`. Fichier de départ propre : `PRC02_ch4_lampe_en_studio.blend`, au même état, qui sert aussi de point de reprise en cours de séance. |
| 5 · Fichiers et ateliers | Tableau « Fichiers de travail et corrigés », selon la convention commune aux chapitres 2 à 4 : corrigés dans des collections masquées « Corrigé », notes « Corrigé » du LISEZ-MOI pour les réglages de rendu et le monde, fichiers séparés pour les images et le fichier de secours seulement. Ressources empaquetées ; LISEZ-MOI par paliers ; défis à part. |
| 6 · Chapitre 4 | Contenu technique de 3 h, accueil compris ; galerie et bilan de 30 minutes. |
| 7 · Progression | Prérequis et nouveautés en tête de chaque séquence ; une notion par cycle ; démo, guidé, puis autonome ; un atelier sans notion nouvelle, la matière émissive étant fournie. |

## Décisions du formateur (18 novembre 2026)

1. **Les HDRI : option A + B.** `studio.exr`, fournie avec Blender, pour le studio ; `artist_workshop` et `docklands_01`, en 2K, de Poly Haven, pour l'intérieur et l'extérieur. Le téléchargement se fera avec l'accord du formateur, à la construction des fichiers.
2. **Les livrables :** les trois vues, héros en 16:9, détail en 1:1 et situation en 16:9, nommées `<objet>_<vue>_<initiales>_v001.png`.
3. **Cycles :** une image comparative seulement, `PRC02_ch4_comparatif_moteurs.png`. Aucune manipulation de Cycles en séance : le défi de comparaison avec Cycles est retiré.
4. **Le questionnaire de satisfaction :** hors du support, géré par VIV Formation. Il est retiré du plan, avec la grille d'autoévaluation qui relevait de la même procédure. Ses minutes vont au bilan pédagogique : le récapitulatif des six demi-journées, les ressources pour continuer et les questions.

**Ajouts du 18 novembre, confirmés à la relecture :**
- les corrigés selon la convention commune aux chapitres 2 à 4 : trois collections masquées « Corrigé » dans le fichier de travail, une note « Corrigé » du LISEZ-MOI pour les réglages de rendu et le monde, aucun fichier `_fini` ;
- le palier ★ des coloris devient une vue de gamme, `lampe_gamme_<initiales>_v001.png`, avec le coloris B amené par Append ;
- le décalage de `Lampe_coloris_B` : 0,75 m en X, harmonisé avec le chapitre 3 (point 1 ci-dessus) ;
- le fichier de secours est renommé `PRC02_ch4_lampe_en_studio.blend`, pour ne pas le confondre avec `PRC02_ch3_lampe_habillage.blend`. Il est tiré de ce dernier par Append.

## Décisions de production, 19 novembre 2026

Prises par délégation pendant la production des fichiers, du texte et des captures, à confirmer par le formateur.

1. **Les objets du coloris B** gardent dans le fichier de secours les noms que donne *Duplicate Collection* (`Socle.001`…), comme dans la lampe habillée du chapitre 3 (fiche A2), et non un suffixe `_B` : le fichier de secours reflète exactement `lampe_habillage_v002.blend`. Les matières de la lampe restent des actifs, comme après un Append ; le fichier de catalogues n'est pas livré, le chapitre 4 n'utilise pas l'Asset Browser.
2. **Les puissances du corrigé, calées au premier rendu** (*Khronos PBR Neutral*, `Monde_Neutre`) : `Key` 20 W à 5500 K, `Fill` 5 W à 6000 K, `Rim` 15 W à 6500 K, la bande 10 W, le *Spot* 12 W. Les valeurs de départ du plan (40, 10, 25, 15 et 8 W) brûlaient le fond. Les températures sont un peu plus neutres, pour un fond moins rosé.
3. **La bande de reflet** est placée par le calcul : la face de la tête qui renvoie le regard de `CAM_heros_corrige` vers le haut, à 45° environ. Elle se trouve en (0,36 ; 0,42 ; 0,805), hors du cadre de la vue héros, sa longueur dans l'axe de la tête.
4. **La rotation de `Monde_Interieur`** vaut 135° : choisie parmi huit rendus, de 0 à 315°, pour le reflet de la fenêtre sur la tête et le fond de la vue de situation.
5. **La vue « lampe allumée »** du corrigé se rend sous `Monde_Interieur` baissé à 0,12, réglage fait en mémoire seulement, et non sous `Monde_Neutre` : la pièce reste lisible autour du cône de lumière.
6. **L'enregistrement de l'image.** Dans Blender 5.2, la fenêtre *Save As* d'un rendu n'a plus de case *Save as Render* : la rubrique *Color Management* y vaut *Follow Scene*, et l'image garde la transformation de vue de la scène (vérifié). Le texte, le quiz et le LISEZ-MOI suivent.
7. **Les libellés de Blender 5.2.1 :** *Align Active Camera to View* est sous *View > Align View*, et non *View > Cameras* ; le cône du *Spot* se règle dans la rubrique *Beam Shape*, champs *Angle* et *Blend* ; l'onglet *Light* affiche aussi *Tint*, *Exposure* et *Normalize*. Une lumière neuve fait 10 W, une *Area* neuve mesure 1 m, et la case *Temperature* est décochée.
8. **Les images du corrigé** sont livrées dans un zip, `PRC02_ch4_images_corrige.zip` (8,8 Mo) : héros, détail, situation, situation allumée et comparatif des moteurs. Le comparatif n'a pas de légende incrustée : la légende de la figure 4.6 donne les moteurs et les temps.
9. **Les temps du comparatif,** mesurés en 1280 × 720 : EEVEE 1,0 s ; Cycles, 128 échantillons débruités, 2,8 s sur la carte graphique (RTX 5070 Ti) et 10,9 s sur le processeur (Core Ultra 7 265KF). Le texte dit que l'écart grandit sur une scène lourde ou un poste moins puissant, sans promettre de minutes.
10. **Les figures :** 41, dont 26 captures d'interface ; l'échelle minimale est 0,54 (le graphe du monde). Trois captures trop larges pour le côte à côte passent en pleine largeur : la fenêtre *Append*, la fenêtre de rendu et la vue de dessus des trois lumières. Les captures d'interface gardent leur résolution d'origine.
11. **Les défis sans figure :** le nœud *Glare*, les marqueurs liés aux caméras et la contrainte *Damped Track* sont cités en défi, avec leur chemin dans le LISEZ-MOI, sans capture. Le *Spot* a la sienne (figure 4.41).
12. **La planche du bilan,** `PRC02_ch4_recapitulatif.png`, n'est pas produite : elle dépend des visuels des six demi-journées. Le texte demande au formateur de projeter une vignette par demi-journée ; la planche reste à faire.
13. **Le *Fond_cyclo*** est lissé par le lissage des faces (*Shade Smooth*), avec deux arêtes de raccord serrées, et non par *Shade Auto Smooth* : aucun groupe de nœuds lié n'entre dans le studio.
14. **Le plateau de bureau en chêne,** demandé par le formateur à la relecture du 19 novembre : la vue de situation qui clôt la formation montrait un plateau d'une seule couleur. Le placage `oak_veneer_01` de Poly Haven (CC0, téléchargement accordé par le formateur) est posé en projection *Box*, la chaîne du parcours principal du chapitre 3, pour que chaque apprenant puisse la lire dans le *Shader Editor*. Trois cartes seulement, 3,8 Mo en tout : la couleur en 2K, la rugosité en 1K et le relief en 2K. Le relief passe par la carte de hauteur dans un *Bump*, comme le grain du socle au chapitre 3. La carte de normales en projection *Box* fonctionne aussi sans UV, avec un *Normal Map* (vérifié le 25 novembre 2026 ; recette du socle en lot PBR, chapitre 3). Pas de vernis (*Coat*) : l'essai ne changeait presque rien à cet angle. Le plateau reçoit aussi un chant arrondi (*Bevel*). Le studio et le fichier de secours pèsent 3,7 Mo de plus (15,2 et 15,5 Mo). L'atelier ne s'allonge pas : la consigne « Situation » invite seulement à ouvrir la matière. Figures refaites : 4.1, 4.39 et 4.40.
15. **La figure 4.6, refaite le 19 novembre :** le premier montage était noir (un agrandissement mal géré dans le script) et le panneau *Material Preview* gardait la barre d'outils. Les trois images ont désormais le même cadrage, sans barre d'outils, et la figure fait 1920 px de large pour la visionneuse. Les PNG du zip du corrigé ne gardent plus de métadonnées : Blender y écrivait le chemin local du fichier.

## Annexe · Les textes LISEZ-MOI

### Le studio et le fichier de secours

Le même texte dans les deux fichiers ; seule la rubrique « Démarrer » change. Les heures ne sont pas écrites : le formateur les annonce.

```text
LISEZ-MOI · PRC02 · Chapitre 4 · Mettre en scène et exporter
Blender 5.2 LTS. Ctrl + Espace agrandit ce texte.

DÉMARRER (fichier studio)
- Votre lampe du chapitre 3 est prête : File > Append,
  lampe_habillage_v002.blend, dossier Collection, collection Lampe.
- Sinon : ouvrez plutôt PRC02_ch4_lampe_en_studio.blend.
- Puis File > Save As : lampe_rendu_v001.blend.
- L'ampoule ne laisse plus voir le fond de la tête : c'est normal,
  la section 1 explique pourquoi.

DÉMARRER (fichier de secours)
- La lampe habillée est déjà là. Son coloris B attend, masqué, dans
  la collection Lampe_coloris_B. File > Save As : lampe_rendu_v001.blend.

1 · PARAMÉTRER EEVEE : le banc d'essai
1. Z : passez de Material Preview à Rendered. En Material Preview,
   cochez puis décochez Scene World (menu Viewport Shading).
2. F12 : un rendu dans l'emplacement 1 (menu Slot), Raytracing décoché.
3. Onglet Render : cochez Raytracing, la case du chapitre 3 que le
   studio n'a pas. Emplacement 2, puis F12. Comparez avec J :
   le chrome, la laque et le verre.
4. Render > Samples : 128. F12. Notez les deux temps de rendu.
5. Color Management > View : AgX, Standard, Khronos PBR Neutral.
   Regardez le nuancier.
Seul : gardez Raytracing, un nombre d'échantillons adapté à votre poste
et une transformation de vue. Ctrl + S.

2 · ÉCLAIRER PAR HDRI
1. Onglet World : choisissez Monde_Studio, Monde_Interieur, puis
   Monde_Exterieur. Un F12 dans un emplacement différent pour chacun.
2. Rotation Z du Mapping : placez le reflet principal sur la tête.
Seul : choisissez l'ambiance de votre vue de situation.

3 · ÉCLAIRER EN STUDIO
1. Onglet World : Monde_Neutre.
2. Add > Light > Area. Nommez-la Key. À 45°, au-dessus et sur le côté,
   tournée vers la lampe. Cochez Temperature pour régler les kelvins.
3. Fill : du côté opposé, un tiers de la puissance de Key, plus grande.
4. Rim : derrière et au-dessus, jusqu'au liseré clair sur la tête.
5. M > New Collection : Eclairage_studio.
6. Allumez-les une à une avec l'œil, puis les trois.
Seul : Monde_Studio à Strength 0,3, lumières allumées. Gardez la
combinaison que vous préférez.
★ Une Area Rectangle longue : une ligne de reflet sur la tête.
  Key à 4500 K, Rim à 7000 K.

4 · CAMÉRA ET EXPORT
1. Add > Camera, nommée CAM_heros, puis Ctrl + 0 du pavé : elle devient
   la caméra active. View > Align View > Align Active Camera to View
   (Ctrl + Alt + 0 du pavé).
2. Focal Length : 85 mm. N > View > Lock Camera to View : cadrez en
   naviguant, puis décochez.
3. Viewport Display > Composition Guides > Thirds.
4. CAM_detail : Add > Camera, Ctrl + 0, 100 mm, alignée sur un détail
   (interrupteur et grille, articulation ou ampoule). Un Empty Mise_au_point sur ce détail.
   Depth of Field : Focus on Object, F-Stop entre 5,6 et 8.
5. Masquez la collection Nuancier (œil et appareil photo).
   CAM_heros active (Ctrl + 0 du pavé). Format 1920 × 1080. F12.
   Image > Save As : rendus/lampe_heros_<initiales>_v001.png,
   PNG, Color Management sur Follow Scene.
Seul : CAM_detail active, résolution 1080 × 1080, F12,
rendus/lampe_detail_<initiales>_v001.png.

ATELIER · LE CONCEPT FINAL
Revue de design demain matin : présentez votre lampe en trois visuels.
- V1 Héros, CAM_heros, 1920 × 1080 : lampe_heros_<initiales>_v001.png
- V2 Détail, CAM_detail, 1080 × 1080 : lampe_detail_<initiales>_v001.png
- V3 Situation, CAM_situation, 1920 × 1080 :
  lampe_situation_<initiales>_v001.png
  (Mise_en_situation visible, Studio masqué, une HDRI)
- File > External Data > Pack Resources, puis Ctrl + S.
- Copiez les trois PNG dans Galerie_PRC02.
Socle : les trois vues et le fichier empaqueté.
★  Une vue héros à fond transparent (Film > Transparent, RGBA).
★  Une vue technique de profil : caméra Orthographic, Monde_Neutre.
★  La gamme : File > Append, collection Lampe_coloris_B de
   lampe_habillage_v002.blend (fichier de secours : ouvrez son œil et
   son appareil photo). CAM_gamme cadre les deux lampes :
   lampe_gamme_<initiales>_v001.png
★★ La lampe allumée : un Spot dans la tête, Temperature 2700 K,
   Eclairage_studio éteint. Sur l'ampoule, la matière Ampoule_allumee
   (liste des matières).
★★ Le même studio pour un autre objet.
Avant d'envoyer : nuancier masqué (œil et appareil photo), bonne
résolution pour chaque vue, noms vérifiés.

POUR ALLER PLUS LOIN (notions nouvelles)
- Spot : rubrique Beam Shape, Angle et Blend.
- Votre propre ampoule allumée : rubrique Emission de la matière.
- L'éclat de l'ampoule : nœud Glare, type Bloom, dans le compositeur.
- Toutes les vues d'un coup : marqueurs, Marker > Bind Camera to Markers,
  chemin de sortie, Render > Render Animation.
- Une présentation tournante de 72 images.
- Des lumières qui suivent la lampe : contrainte Damped Track.

CORRIGÉ
Trois collections masquées (œil fermé) : Corrigé éclairage, Corrigé
caméras, Corrigé paliers. Pour en voir une au rendu, ouvrez son œil et
son appareil photo. Réglages de rendu et monde : la ligne « Corrigé »
de chaque section. Images : PRC02_ch4_corrige_*.png.
Perdu en cours de route ? Ouvrez PRC02_ch4_lampe_en_studio.blend,
enregistrez-le sous lampe_rendu_v001.blend, puis suivez les corrigés.
```

Les lignes « Corrigé » de chaque section, une par section :

| Rubrique | Ligne à placer en fin de rubrique |
|---|---|
| Démarrer (fichier studio) | `Corrigé : PRC02_ch4_lampe_en_studio.blend montre la lampe en place.` |
| 1 · Paramétrer EEVEE | `Corrigé : Raytracing coché, Render > Samples 128, View Khronos PBR Neutral.` |
| 2 · Éclairer par HDRI | `Corrigé : Monde_Interieur, rotation Z du Mapping <valeur notée au montage> °.` |
| 3 · Éclairer en studio | `Corrigé : collection « Corrigé éclairage », avec Monde_Neutre.` |
| 4 · Caméra et export | `Corrigé : collection « Corrigé caméras » ; images PRC02_ch4_corrige_heros.png et _detail.png.` |
| Atelier | `Corrigé : CAM_situation_corrige (« Corrigé caméras ») et « Corrigé paliers » ; images PRC02_ch4_corrige_*.png.` |
