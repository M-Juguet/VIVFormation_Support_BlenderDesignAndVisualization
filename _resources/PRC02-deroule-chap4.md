# Chapitre 4 · Rendu temps réel et visuels de présentation : déroulé formateur

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 6 sur 6, en présentiel, de 5 à 8 apprenants · Version du 19 novembre 2026, application support 1.0.0

## En bref

- **Objectif :** à la fin de la demi-journée, chaque apprenant choisit l'affichage adapté à son besoin et règle EEVEE pour un rendu fidèle : échantillons, *Raytracing*, transformation de vue. Il éclaire sa lampe par une HDRI, puis en studio avec trois lumières. Il la cadre avec une focale adaptée, des guides de composition et une profondeur de champ. Il exporte enfin trois visuels, nommés selon une convention.
- **Format :** 3 h 50, dont 3 h 30 de contenu et 2 pauses de 10 minutes. Il reste 10 minutes de marge sur 4 heures. Exemple : de 13 h 30 à 17 h 20. Les 30 dernières minutes vont à la galerie des visuels et au bilan de la formation.
- **Principe :** le même qu'aux demi-journées précédentes. Une notion à la fois : vous la montrez en quelques minutes, ils la pratiquent en guidé, puis seuls. Ce qui est déjà vu sert sans être redit : les modes d'affichage, *Material Preview*, la case *Raytracing* du chapitre 3, *File > Append*, l'œil et l'appareil photo de l'Outliner.
- **L'idée du jour : comparer deux images avant de choisir.** `F12` dans un emplacement de rendu, un réglage, `F12` dans un autre emplacement, puis `J` pour passer de l'un à l'autre. Le geste sert au *Raytracing*, aux échantillons, aux mondes et aux lumières. Et `F12` n'enregistre rien : seul *Image > Save As* crée un fichier.
- **Fil rouge :** la lampe habillée au chapitre 3, en deux coloris (`lampe_habillage_v002.blend`). Elle entre dans le studio par *File > Append*, et toute la séance se passe dans un seul fichier, `lampe_rendu_v001.blend`. Chacun en exporte trois visuels : une vue héros, un détail et une mise en situation. Leur galerie clôt la formation.

### Ce que l'on survole

Ces notions sont dans l'application. Elles ne sont pas exigées en séance, et certaines servent de défi.
- Cycles : une image comparative (figure 4.6) et le menu *Render Engine*, ouvert sans être changé. Personne ne manipule Cycles en séance.
- *Look*, *Exposure* et *Render Pass* : une phrase chacun.
- *Film > Transparent* et la caméra *Orthographic* : une phrase en démo, puis un palier ★ de l'atelier.
- La matière émissive : fournie toute prête, `Ampoule_allumee`, pour le palier ★★. Son réglage reste un défi.
- Le nœud *Glare*, les marqueurs liés aux caméras, *Render Animation* et la contrainte *Damped Track* : des défis, dont le LISEZ-MOI donne le chemin.
- Hors formation, et absents de l'application : les sondes de lumière, les volumes, le flou de mouvement, les passes de rendu et le *light linking*. Une phrase suffit si on vous les demande.

### Les fichiers

| Fichier | Moment | Contenu |
|---|---|---|
| `PRC02_ch4_studio.blend` | 0:00, puis toute la séance | Le studio : fond courbe, nuancier, plateau de bureau en chêne et carnet (collection *Mise_en_situation*, masquée), quatre mondes, la caméra `CAM_banc_essai` et la matière fournie `Ampoule_allumee`. Les corrigés sont dans trois collections masquées : « Corrigé éclairage », « Corrigé caméras » et « Corrigé paliers » |
| `PRC02_ch4_lampe_en_studio.blend` | 0:00 ; point de reprise ; vos démos | Le fichier de secours : le même studio, avec la lampe habillée du chapitre 3 en place. Le coloris A est visible, dans *Lampe* ; le coloris B est masqué, dans `Lampe_coloris_B` |
| `lampe_habillage_v002.blend` | 0:00, puis palier ★ | Le fichier de fin du chapitre 3, sur chaque poste : sa collection *Lampe* entre dans le studio au lancement, `Lampe_coloris_B` au palier ★ de la gamme |
| `PRC02_ch3_lampe_habillage.zip` | 0:00, au besoin | La lampe habillée du chapitre 3, pour qui a fait le défi procédural à la place de l'atelier : même Append, depuis le `.blend` décompressé |
| `PRC02_ch4_images_corrige.zip` | 0:00, 0:10, corrigés, galerie | Cinq PNG : la vue héros, le détail, la situation, la situation allumée du palier ★★ et le comparatif des moteurs |

L'application propose le studio et le fichier de secours en section 1, juste après la figure 4.1, et les images du corrigé en section 4, sous les consignes de l'atelier. L'archive de la lampe habillée est au chapitre 3, avec les consignes du coloris B.

> **À savoir :** les deux fichiers s'ouvrent sur un texte LISEZ-MOI, en bas de l'écran : les consignes de chaque partie, les paliers de l'atelier, une ligne « Corrigé » par partie et le chemin des défis. Il tient lieu d'annexe : ce document n'en a pas. `Ctrl + Espace` agrandit la zone.

## Avant la demi-journée

### Les postes des apprenants

- [ ] L'application support 1.0.0 est installée. Une version plus ancienne propose la mise à jour à son démarrage.
- [ ] Blender 5.2 LTS s'ouvre, avec une souris à trois boutons. *Emulate Numpad* reste activé sur les portables sans pavé numérique : `Ctrl + 0` et `Ctrl + Alt + 0` passent alors par la rangée des chiffres.
- [ ] Le dossier de travail contient `PRC02_ch4_studio.blend`, `PRC02_ch4_lampe_en_studio.blend` et un sous-dossier `rendus`, vide. À défaut, chacun télécharge les fichiers depuis l'application à 0:00 : comptez environ 15 Mo par fichier.
- [ ] Le fichier de fin du chapitre 3, `lampe_habillage_v002.blend`, est retrouvé sur chaque poste. Sinon, l'apprenant partira du fichier de secours.
- [ ] **Les temps de rendu EEVEE sont mesurés.** Sur chaque poste, ouvrez le fichier de secours, cochez *Raytracing*, puis lancez un `F12` à 64, puis à 128 échantillons. Notez les temps, puis refermez sans enregistrer : un poste lent se repère avant la séance. Les temps de la figure 4.6 viennent d'un poste récent, avec une carte graphique puissante ; ceux de la salle n'ont pas encore été mesurés. Cycles n'est pas à tester : en séance, il n'existe qu'en image.

### Votre poste de démonstration

- **Lancez Blender en configuration d'usine** (`blender.exe --factory-startup`), comme aux demi-journées précédentes, et agrandissez l'interface pour le vidéoprojecteur : *Resolution Scale* à 1,3.
- **Préparez une copie de travail du fichier de secours,** enregistrée sous un autre nom, pour vos démos : le fichier livré reste intact. Ses collections « Corrigé » et les lignes « Corrigé » du LISEZ-MOI montrent le résultat de chaque étape.
- **Pour montrer l'Append à 0:00,** gardez le studio et une lampe du chapitre 3 : la vôtre, ou celle de `PRC02_ch3_lampe_habillage.zip`, décompressée.
- **Ouvrez les images du corrigé dans une visionneuse,** décompressées de `PRC02_ch4_images_corrige.zip` : les trois visuels pour 0:00, le comparatif des moteurs pour 0:10.
- **Préparez six vignettes pour le bilan, une par demi-journée.** La planche récapitulative `PRC02_ch4_recapitulatif.png` n'est pas produite. Une capture par fichier suffit : `PRC02_init_maquette_en_kit.blend`, la cabine de `PRC02_init_rangee_sieges.blend` (collection *Corrigé*), les trois variantes de `PRC02_ch1_blocage_lampe.blend`, `PRC02_ch2_lampe_modele.blend` et la lampe habillée en deux coloris. La sixième est un visuel de la galerie, choisi en direct. Les productions du groupe, si vous les avez gardées, valent mieux encore.
- **Gardez l'application ouverte** sur le chapitre 4, pour projeter les quiz.

### Le matériel de la salle

- Les post-it vert et rose des points de contrôle, et le minuteur.
- **Le dossier de la galerie, à préparer par vous :** un dossier partagé, par exemple `Galerie_PRC02`, accessible en écriture depuis chaque poste, ou une clé USB qui circule. Ni l'application ni le LISEZ-MOI n'en donnent le nom. Le diaporama est prêt à lire ce dossier.
- Le paperboard, préparé avant l'arrivée des apprenants :
  - l'idée du jour : « Comparez deux images : `F12` dans un emplacement, un réglage, `F12` dans un autre, puis `J`. » ;
  - la grille des temps de rendu, une ligne par poste : temps à 64 échantillons, temps à 128 ;
  - le corrigé : « Trois collections Corrigé, œil fermé, et une ligne Corrigé par partie du LISEZ-MOI. On compare, on ne copie pas. » ;
  - les livrables : `lampe_heros_<initiales>_v001.png`, de même `detail` et `situation`, dans `rendus`, puis dans le dossier de la galerie, dont vous écrivez le nom ;
  - les touches du jour, complétées au fil de la séance : `Z`, `F12`, `J`, `F11`, `Ctrl + 0` et `Ctrl + Alt + 0` du pavé numérique, `Maj + Alt + S`.

## La demi-journée · Du studio aux visuels

Les quatre sections du chapitre 4, dans l'ordre de l'application. La section 2 se joue en deux temps, de part et d'autre de la première pause : l'HDRI d'abord, le studio ensuite. Les apprenants repartent avec trois visuels exportés et leur fichier `lampe_rendu_v001.blend`, empaqueté. Dans la colonne « Modalité », les durées sont en minutes.

| Horaire | Durée | Séquence | Section | Modalité |
|---|---|---|---|---|
| 0:00 | 10 min | Accueil : la lampe entre dans le studio | 1 | Collectif 5 + guidé 5 |
| 0:10 | 30 min | Paramétrer EEVEE : le banc d'essai | 1 | Démo 10 + guidé 14 + quiz 3 + autonomie 3 |
| 0:40 | 20 min | Éclairer par HDRI | 2 | Démo 7 + guidé 9 + autonomie 3 + quiz 1 |
| 1:00 | 10 min | Pause | | |
| 1:10 | 35 min | Éclairer en studio | 2 | Démo 10 + guidé 20 + autonomie 3 + quiz 2 |
| 1:45 | 40 min | Caméra, composition et export | 3 | Démo 12 + guidé 23 + autonomie 3 + quiz 2 |
| 2:25 | 10 min | Pause | | |
| 2:35 | 45 min | Atelier · Le concept final | 4 | Lancement 3 + autonomie 36 + quiz 1 + dépôt 5 |
| 3:20 | 15 min | Galerie et restitution | 4 | Collectif |
| 3:35 | 15 min | Bilan de la formation | 4 | Collectif |

### 0:00 · Accueil : la lampe entre dans le studio (10 min)

- **Le chemin parcouru (collectif, 5 min) :** le blocage du chapitre 1, la lampe modélisée au chapitre 2, habillée en deux coloris au chapitre 3. « C'est la dernière demi-journée : on met la lampe en scène, et on la présente. »
- **Montrez la cible :** les trois visuels du corrigé (figure 4.1). « Dans trois heures, vous aurez exporté les vôtres. » Annoncez les livrables et le dossier de la galerie.
- **La règle de bascule :** au bout de 3 minutes de difficulté (un Append qui échoue, des matières perdues, une échelle non appliquée), on passe au fichier de secours, sans débat. « Votre lampe pourra être mise en scène plus tard, dans le même studio. »

**Ils font, pas à pas (5 min),** d'après § 1 « Recette · Amener la lampe dans le studio » et « Le dossier Collection » (figure 4.2) :
1. *File > Open* : `PRC02_ch4_studio.blend`.
2. *File > Append* : double-clic sur `lampe_habillage_v002.blend`, puis sur le dossier *Collection*. La collection *Lampe*, puis *Append* : la lampe arrive à sa place, posée sur le fond, avec ses matières.
3. *File > Save As* : `lampe_rendu_v001.blend`, dans le dossier de travail. Le studio livré reste intact.
4. Le tour du fichier : les collections *Studio*, *Nuancier*, *Mise_en_situation* (œil fermé) et les trois « Corrigé » ; le LISEZ-MOI en bas. « Le coloris B attend dans votre fichier du chapitre 3 : il servira au palier ★. »

Sans lampe exploitable, chacun ouvre le fichier de secours et l'enregistre sous le même nom ; le coloris B y est déjà, masqué. Qui a fait le défi procédural au chapitre 3 amène sa propre lampe, gardée dans la collection *Lampe*, ou celle de `PRC02_ch3_lampe_habillage.zip`, par le même geste.

**Point de contrôle :** la lampe est posée sur le fond du studio ; la barre de titre affiche `lampe_rendu_v001.blend`.

**Corrigé :** le fichier de secours montre la lampe en place.

**Pièges fréquents :**
- Des objets choisis un par un au lieu de la collection : les *Empty* `Grille_pivot` et `Interrupteur_pivot` manquent, et la grille et les crans en dépendent. `Ctrl + Z`, puis la collection.
- Rien d'utile dans la fenêtre d'Append : le dossier ouvert est *Material* ou *Object*. Remontez d'un niveau, puis *Collection*.
- Un apprenant qui travaille dans `PRC02_ch4_studio.blend` : le *Save As* a été oublié. Faites-le tout de suite.

**À savoir :** l'ampoule ne laisse plus voir le fond de la tête. C'est normal : « On y revient dans un quart d'heure. »

### 0:10 · Paramétrer EEVEE : le banc d'essai (30 min)

Quatre cycles courts, sur la lampe de chacun. `F12` rend toujours par la caméra active du studio, `CAM_banc_essai`, qui cadre la lampe et le nuancier ; `0` du pavé numérique montre son cadre. Chaque cycle montre une notion, puis la fait pratiquer aussitôt.

**Cycle 1 · Trois affichages (démo 2 min, guidé 2 min, quiz 1 min).** Vous montrez, d'après § 1 « Trois façons de voir la même scène » (figures 4.3 à 4.5) : `Z`, le pointeur dans la vue 3D, ouvre le menu circulaire des modes. *Material Preview*, puis *Rendered* : la lampe prend la lumière du studio. De retour en *Material Preview*, menu *Viewport Shading* : *Scene World* cochée, l'éclairage change. Ils font la « Recette · Trois affichages ». **Quiz,** ensemble à l'écran : le premier quiz de la section 1, *Material Preview* et les lumières de la scène. Chacun répond pour soi, puis on commente les erreurs.

**Cycle 2 · EEVEE et Cycles (démo 2 min).** D'après § 1 « EEVEE et Cycles » (figures 4.6 et 4.7), projetez le comparatif des moteurs : EEVEE à 64 échantillons en 1 s ; Cycles, 128 échantillons débruités, en 3 s avec la carte graphique et 11 s sans elle. « Cycles suit le trajet de la lumière : c'est la référence physique. EEVEE donne une image très proche, et il la donne aussi en temps réel, dans la vue. Sur une scène lourde, l'écart grandit. » Ouvrez le menu *Render Engine* de l'onglet *Render*, sans le changer. Ils ne font rien : on reste sur EEVEE.

**Cycle 3 · Le *Raytracing* (démo 3 min, guidé 6 min, quiz 1 min).** Vous montrez, d'après § 1 « Rendre une image : F12 et les emplacements », « Le Raytracing, expliqué » et « Les échantillons : Samples » (figures 4.8 à 4.11) :
1. « Au chapitre 3, vous avez coché cette case pour le verre. Le studio ne l'a pas : voyons tout ce qu'elle change. »
2. `F12` : la fenêtre de rendu, son champ *Slot* et le temps de calcul, en haut à gauche de l'image.
3. Onglet *Render*, *Raytracing* coché ; emplacement 2, puis `F12`. `J` : le chrome des articulations, la laque de la tête, le verre de l'ampoule. *Fast GI Approximation*, qui en dépend, n'est plus grisée.
4. La rubrique *Sampling* : *Viewport > Samples* pour la vue, *Render > Samples* pour `F12`.

Ils font la « Recette · Le banc d'essai » : l'emplacement 1 sans *Raytracing*, l'emplacement 2 avec, `J` ; puis *Render > Samples* à 128 dans l'emplacement 3. Chacun reporte ses deux temps sur la grille du paperboard. **Quiz :** le deuxième quiz de la section 1, l'ampoule qui ne laisse plus voir le fond de la tête.

**Cycle 4 · La transformation de vue (démo 3 min, guidé 6 min, quiz 1 min).** Vous montrez, d'après § 1 « La transformation de vue » (figures 4.12 et 4.13), en *Rendered* : la rubrique *Color Management*, en bas de l'onglet *Render*, menu *View*. Le nuancier en *AgX*, qui pâlit le rouge CMF ; en *Standard*, qui brûle les reflets ; en *Khronos PBR Neutral*, qui garde la couleur de base. *Look* et *Exposure* : une phrase. **Ailleurs :** la teinte d'une sellerie de train, d'une planche de bord ou d'un panneau de cabine se vérifie face au nuancier du client, en *Khronos PBR Neutral*. Ils font : les trois transformations sur le nuancier ; chacun en garde une et sait dire pourquoi. **Quiz :** le troisième quiz de la section 1, le rouge du nuancier CMF.

**En autonomie (3 min) :** la consigne « Régler son fichier » : *Raytracing* coché, un nombre d'échantillons adapté au poste, une transformation de vue, `Ctrl + S`.

**Point de contrôle :** deux emplacements montrent la lampe sans et avec *Raytracing* ; les temps sont au paperboard. Commentez les écarts entre postes : ils guident le nombre d'échantillons de l'atelier. Chacun annonce sa transformation de vue et sa raison.

**Corrigé :** la ligne « Corrigé » de la partie 1 du LISEZ-MOI : *Raytracing* coché, *Render > Samples* 128, *View* sur *Khronos PBR Neutral*. La figure 4.10 en montre l'effet.

**Pièges fréquents :**
- Un réglage introuvable : les rubriques de l'onglet *Render* sont repliées. Dépliez-les une par une.
- Un verre qui ne laisse rien voir, *Raytracing* coché : sa matière n'a pas *Raytraced Transmission* (onglet *Material*, rubrique *Settings*, figure 3.13).
- Un poste lent : *Viewport > Samples* à 8, et des rendus d'essai à 50 % (champ *%*, onglet *Output*, rubrique *Format*).
- La fenêtre de rendu cache Blender : fermez-la. Elle revient au prochain `F12`, ou avec `F11`.
- Un apprenant resté dans son fichier du chapitre 3 : *Raytracing* y est coché, mais il n'a ni studio ni nuancier. Ramenez-le dans `lampe_rendu_v001.blend`.

### 0:40 · Éclairer par HDRI (20 min)

**Vous montrez (7 min),** d'après § 2 « Une HDRI : la lumière d'un lieu », « Le sélecteur de monde », « Mettre en place une HDRI » et « Tourner l'HDRI : Mapping » (figures 4.14 à 4.17), en *Rendered* :
1. Une HDRI est une photo panoramique à 360°, qui garde la vraie intensité de la lumière. Placée dans le monde, elle éclaire la lampe et se reflète dans ses surfaces brillantes. `Monde_Studio` éclairait déjà la section 1.
2. Onglet *World*, sélecteur de monde : `Monde_Studio`, puis `Monde_Interieur`. La lumière et les reflets changent.
3. Comment on en met une en place : *New* dans le sélecteur ; rubrique *Surface*, le bouton à gauche de *Color*, *Environment Texture*, puis *Open*. Les HDRI de Blender sont dans son dossier d'installation, sous `datafiles\studiolights\world`. *Strength* règle l'intensité. Revenez ensuite à `Monde_Interieur` : rien n'est perdu.
4. Les nœuds du monde, une fois : espace *Shading*, menu *Object* du Shader Editor passé sur *World*. *Texture Coordinate*, *Mapping*, *Environment Texture*, *Background*. Faites reconnaître les deux premiers : ceux du brossé du chapitre 3. « Les mondes du studio sont câblés : vous ne réglez que la rotation et l'intensité. » Retour à l'espace *Layout*.
5. Onglet *World*, rubrique *Surface*, entrée *Vector* dépliée : la rotation Z du *Mapping*. Le reflet glisse sur la tête laquée et sur le chrome.
6. **Ailleurs :** un rétroviseur sous un ciel d'extérieur, un siège de train sous la lumière d'un quai, une liseuse dans une cabine. L'HDRI apporte le lieu sans modéliser le décor.

**Ils font, en guidé (9 min) :** la « Recette · Trois mondes, un reflet ». `Monde_Studio`, `Monde_Interieur` et `Monde_Exterieur`, chacun rendu avec `F12` dans un emplacement différent, puis comparés avec `J`. Ils gardent l'HDRI qu'ils préfèrent et tournent sa rotation Z jusqu'à placer le reflet principal sur la tête.

**En autonomie (3 min) :** choisir l'ambiance de la future vue de situation : le monde, son intensité, sa rotation.

**Quiz (1 min),** ensemble à l'écran : le quiz de l'HDRI, le reflet mal placé.

**Point de contrôle :** chacun montre sa lampe sous deux mondes, dans deux emplacements, avec un reflet placé volontairement.

**Corrigé :** la ligne « Corrigé » de la partie 2 du LISEZ-MOI : `Monde_Interieur`, rotation Z à 135°. Les figures 4.14, 4.16 et 4.17 montrent ce réglage.

**Pièges fréquents :**
- Le monde change, la vue non : elle est restée en *Material Preview*, qui ignore le monde. Passez en *Rendered*, ou rendez avec `F12`.
- La lampe disparaît dans une HDRI très claire : baissez *Strength*.
- Les reflets basculent, l'horizon penche : c'est la rotation X ou Y qui a bougé. Remettez-la à 0 ; seule la rotation Z fait tourner le lieu.
- Un monde créé par erreur avec *New* : le sélecteur ramène les mondes du studio, jamais perdus.
- Un fond flou derrière la lampe : une HDRI reste moins nette qu'une photo. Pour la vue de situation, cadrez serré, ou floutez le fond avec la profondeur de champ.

### 1:00 · Pause (10 min)

### 1:10 · Éclairer en studio (35 min)

**Une lumière (démo 5 min, guidé 10 min).** Vous montrez, d'après § 2 « Partir du noir », « Les quatre types de lumière » et « Les réglages d'une lumière » (figures 4.18 à 4.21), en *Rendered* :
1. Sélecteur de monde : `Monde_Neutre`. La lampe s'éteint presque. « On part du noir : chaque lumière ajoutée se voit seule. »
2. `Maj + A > Light`, une à la fois devant la lampe : *Point*, *Sun*, *Spot*, *Area*. Comparez les ombres, puis supprimez-les.
3. Une *Area*, onglet *Light* : *Power* ; la case *Temperature*, puis sa valeur ; *Size*, petite puis grande. L'ombre et le reflet sur la tête s'adoucissent avec la taille.

Ils font la « Recette · La principale » :
1. `Monde_Neutre`, la vue en *Rendered*.
2. *Add > Light > Area*, renommée `Key` (`F2`).
3. À 45° environ, au-dessus de la lampe et sur le côté, tournée vers elle avec `R`. Repère : `Key_corrige` est à X `-600mm`, Y `-900mm`, Z `900mm`.
4. *Temperature* cochée. Deux tailles et deux températures : *Size* `300mm` puis `800mm`, 5500 K puis 4500 K. *Power* vers 20 W.

**Trois lumières (démo 5 min, guidé 10 min).** Vous montrez, d'après § 2 « L'éclairage en trois points », « Trois lumières, vues de dessus » et « Les lignes de reflet » (figures 4.22, 4.23 et 4.25) :
1. Au paperboard, les trois rôles : la principale modèle les volumes ; la secondaire, plus faible et plus grande, débouche les ombres ; le contre-jour dessine le contour. Un rapport de 3 à 4 entre principale et secondaire : un départ, pas une règle.
2. `Fill`, puis `Rim`, ajoutées à côté de `Key`. En vue de dessus (`7`), les trois entourent la lampe. Fermez leur œil dans l'Outliner à tour de rôle : le rôle de chaque lumière se voit.
3. Une *Area* *Rectangle*, longue et fine, au-dessus de la lampe : une ligne de lumière suit la tête laquée.
4. **Ailleurs :** le studio automobile aligne de longues *Area* au-dessus de la voiture pour dessiner ses lignes ; une caisse de train ou un fuselage en maquette se lit mieux avec un contre-jour franc.

Ils font la « Recette · Le studio en trois lumières » (figure 4.24) :
1. `Fill` : une *Area* du côté opposé à `Key`, avec environ un tiers de sa puissance et une taille plus grande.
2. `Rim` : une *Area* derrière et au-dessus, jusqu'au liseré clair sur le contour de la tête.
3. Les trois sélectionnées, `M > New Collection` : `Eclairage_studio`.
4. Dans l'Outliner, l'œil de deux lumières fermé : le rôle de la troisième. Puis les trois rallumées.

**En autonomie (3 min) :** la consigne « Combiner ». `Monde_Studio` à *Strength* 0,3, lumières allumées, comparé à `Monde_Neutre` ; chacun garde sa combinaison pour la vue héros. Palier ★ : une *Area* *Rectangle* pour une ligne de reflet ; `Key` à 4500 K et `Rim` à 7000 K.

**Quiz (2 min),** ensemble à l'écran : les deux derniers quiz de la section 2, le rôle du contre-jour et l'ombre d'une *Area*.

**Point de contrôle :** en *Rendered*, la silhouette de la lampe se détache du fond ; l'Outliner montre `Eclairage_studio`, avec `Key`, `Fill` et `Rim`. Demandez à deux ou trois apprenants : « Que fait `Rim` ? » `Ctrl + S`.

**Corrigé :** la collection « Corrigé éclairage », sous `Monde_Neutre` : `Key_corrige` (*Area* de 500 mm, 20 W, 5500 K), `Fill_corrige` (800 mm, 5 W, 6000 K), `Rim_corrige` (300 mm, 15 W, 6500 K) et `Reflet_bande_corrige` (*Rectangle* de 1000 × 60 mm, 10 W). Pour la voir au rendu, ouvrez son œil et son appareil photo.

**Pièges fréquents :**
- Une lumière qui n'éclaire rien : elle pointe ailleurs, ou elle est née au curseur 3D, dans le socle. La ligne qui part de la lumière montre sa direction.
- La température ne change rien : la case *Temperature* n'est pas cochée.
- Tout est blanc ou tout est noir : un *Power* dix fois trop fort ou trop faible. La lampe mesure 450 mm : les puissances du corrigé donnent l'ordre de grandeur.
- Le studio paraît plat : `Fill` est aussi forte que `Key`.
- Une lumière masquée par l'œil éclaire encore au rendu `F12` : fermez aussi son appareil photo. C'est la distinction de Basics 101.

### 1:45 · Caméra, composition et export (40 min)

**Cadrer (démo 6 min, guidé 11 min).** Vous montrez, d'après § 3 « Placer une caméra », « La focale » et « La composition » (figures 4.26 à 4.31) :
1. *Add > Camera*, renommée, puis `Ctrl + 0` du pavé numérique : elle devient la caméra active. « Sans ce geste, la commande suivante déplacerait `CAM_banc_essai`. »
2. Naviguez jusqu'au point de vue voulu, puis *View > Align View > Align Active Camera to View* (`Ctrl + Alt + 0`). *Lock Camera to View* (`N`, onglet *View*, rubrique *View Lock*) : on affine en naviguant, puis on décoche.
3. Le même cadrage à `24mm`, `50mm` et `100mm` (*Focal Length*, onglet *Camera*, rubrique *Lens*), en reculant la caméra à chaque fois. « Laquelle respecte votre dessin ? » Puis *Type* sur *Orthographic*, en une phrase : la vue technique.
4. Rubrique *Viewport Display* : *Composition Guides > Thirds* et le *Passepartout*. La tête sur un point fort.
5. **Ailleurs :** une longue focale pour la photo d'un rétroviseur ou d'une calandre ; une caméra *Orthographic* pour le profil technique d'un siège ou d'une rame.

Ils font la « Recette · La vue héros » :
1. *Add > Camera*, renommée `CAM_heros`, puis `Ctrl + 0`.
2. *Focal Length* : `85mm`.
3. Une vue de trois quarts avant, un peu au-dessus de la lampe, puis *Align Active Camera to View*.
4. *Lock Camera to View* : le cadrage affiné en naviguant, puis la case décochée.
5. *Composition Guides > Thirds* : la tête sur un point fort. Repère : `CAM_heros_corrige` est à X `1600mm`, Y `-2100mm`, Z `650mm`.

**Le détail et l'export (démo 6 min, guidé 12 min).** Vous montrez, d'après § 3 « La profondeur de champ », « Le format de sortie » et « Rendre et enregistrer » (figures 4.32 à 4.38) :
1. Rubrique *Depth of Field* cochée, *Focus on Object* sur un *Empty* posé sur l'interrupteur ; *F-Stop* à 1,4, puis à 8. « En gros plan, la zone nette ne fait que quelques millimètres : partez de 5,6 à 8. »
2. Onglet *Output*, rubrique *Format* : *Resolution X* et *Y*, le pourcentage, le bouton des préréglages. « La résolution appartient à la scène, pas à la caméra. »
3. `F12`, puis dans la fenêtre de rendu *Image > Save As* (`Maj + Alt + S`) : le dossier `rendus`, le nom, *PNG*, *RGB*, *Color Depth* 8, *Color Management* sur *Follow Scene*. « `F12` n'enregistre rien. »
4. En une phrase : *Film > Transparent*, dans l'onglet *Render*, et *RGBA* donnent un PNG sans fond.

Ils font la « Recette · Le détail et le premier export » :
1. `CAM_detail` : *Add > Camera*, `Ctrl + 0`, *Focal Length* `100mm`, cadrée comme `CAM_heros` sur un détail : l'interrupteur cranté et la grille, une articulation, ou l'ampoule dans la tête.
2. `Mise_au_point` : la pièce du détail sélectionnée, `Maj + S > Cursor to Selected`, puis *Add > Empty > Plain Axes*. Rubrique *Depth of Field* de `CAM_detail` : cochée, *Focus on Object* `Mise_au_point`, *F-Stop* entre 5,6 et 8.
3. La collection *Nuancier* masquée, œil et appareil photo : elle entre dans le cadre de la vue héros.
4. `CAM_heros` active (`Ctrl + 0`), le format vérifié à 1920 × 1080, puis `F12`.
5. *Image > Save As* : `rendus/lampe_heros_<initiales>_v001.png`, *PNG*, *Follow Scene*.
6. L'image ouverte dans l'Explorateur Windows : elle est identique au rendu.

**En autonomie (3 min) :** la consigne « La vue de détail » : `CAM_detail` active, résolution 1080 × 1080, `F12`, puis `rendus/lampe_detail_<initiales>_v001.png`.

**Quiz (2 min),** ensemble à l'écran : les trois quiz de la section 3, la focale, le rendu non enregistré et le PNG sans fond.

**Point de contrôle :** `CAM_heros` et `CAM_detail` existent, nommées, avec leurs guides ; deux PNG sont dans `rendus`, au bon nom, au bon format et aux couleurs du rendu. `Ctrl + S`.

**Corrigé :** la collection « Corrigé caméras » : `CAM_heros_corrige` (85 mm, *Thirds*) et `CAM_detail_corrige` (100 mm, *F-Stop* 8, mise au point sur `Mise_au_point_corrige`, posé sur l'interrupteur). Les images `PRC02_ch4_corrige_heros.png` et `PRC02_ch4_corrige_detail.png`.

**Pièges fréquents :**
- `CAM_banc_essai` a bougé, pas la nouvelle caméra : *Align Active Camera to View* déplace la caméra active. `Ctrl + Z`, puis `Ctrl + 0` sur la bonne caméra.
- Le cadrage se défait au moindre coup d'orbite : *Lock Camera to View* est resté coché.
- La vue de détail sort en 16:9 : la résolution n'a pas été changée. Elle se remet à 1920 × 1080 avant la vue suivante.
- Un PNG aux couleurs différentes du rendu : la rubrique *Color Management* de la fenêtre d'enregistrement est passée sur *Override*. Remettez *Follow Scene*.
- Une profondeur de champ sans effet : *Focus on Object* est vide. Un détail flou : *F-Stop* trop petit. Un détail coupé net : la caméra est à moins de 100 mm de l'objet (*Clip Start*, figure 4.28) ; reculez-la et allongez la focale.

### 2:25 · Pause (10 min)

### 2:35 · Atelier · Le concept final (45 min)

La fiche complète est plus bas. Le lancement dure 3 minutes, l'autonomie 36 minutes, le quiz récapitulatif 1 minute et le dépôt 5 minutes.

### 3:20 · Galerie et restitution (15 min)

D'après § 4 « Galerie et restitution ».
- **Diaporama (3 min) :** les vues héros du dossier de la galerie, sans commentaire.
- **Restitution (10 min) :** chacun commente sa vue de situation, ou sa vue préférée, en une minute : un choix de lumière, un choix de cadrage. Le groupe pose une question au plus. Appuyez vos retours sur les critères de la fiche de l'atelier, en commençant par ce qui fonctionne.
- **Coup de cœur (2 min) :** un post-it vert par personne, sur le visuel d'un autre.

### 3:35 · Bilan de la formation (15 min)

Le déroulé est plus bas, après la fiche de l'atelier : le récapitulatif des six demi-journées, les ressources pour continuer, puis les questions et le tour de table.

<!-- pagebreak -->

## Atelier · Le concept final

**Fichier :** `lampe_rendu_v001.blend` · **Durée :** 45 min · **De 2:35 à 3:20**

**Situation :** « Revue de design demain matin. Vous présentez votre concept de lampe au client en trois visuels. Ils doivent faire comprendre la forme, les matières et l'usage. » Le cadre se transpose : la revue d'un siège ferroviaire, d'un rétroviseur automobile ou d'une liseuse de cabine d'avion se prépare de la même façon.

**Objectif :** régler la lumière définitive, créer la caméra de situation, exporter les trois visuels au bon format et au bon nom, puis livrer un fichier empaqueté.

**Pourquoi il fonctionne :**
- Aucune notion nouvelle : l'atelier réinvestit les sections 1 à 3, *Pack Resources* (Basics 102) et, pour les paliers, *File > Append* et la liste des matières (chapitre 3). La matière émissive du palier ★★ est fournie.
- Trois vues, trois décisions : une lumière de studio, un gros plan, la lumière d'un lieu.
- Un vrai livrable : des images nommées selon une convention, comme pour un client. La galerie leur donne un public.

**Les livrables :**

| Vue | Caméra | Contenu | Format | Nom du fichier |
|---|---|---|---|---|
| V1 · Héros | `CAM_heros` | La lampe entière en trois quarts avant, câble compris, en studio | 1920 × 1080, PNG *RGB* 8 bits | `lampe_heros_<initiales>_v001.png` |
| V2 · Détail | `CAM_detail` | Un gros plan, avec profondeur de champ | 1080 × 1080, PNG *RGB* 8 bits | `lampe_detail_<initiales>_v001.png` |
| V3 · Situation | `CAM_situation` | La lampe sur le plateau de bureau, sous une HDRI | 1920 × 1080, PNG *RGB* 8 bits | `lampe_situation_<initiales>_v001.png` |

S'y ajoute `lampe_rendu_v001.blend`, ressources empaquetées. Les noms suivent la convention `<objet>_<vue>_<initiales>_v<version>.png` : en minuscules, sans accent ni espace, les initiales en majuscules (`lampe_heros_AB_v001.png`). Les images vont dans `rendus`, puis dans le dossier de la galerie.

**Le socle, en 5 étapes :**

| Étape | Ce qu'il faut faire | Gestes réinvestis |
|---|---|---|
| 1 | La lumière définitive de la vue héros et du détail : `Eclairage_studio`, sur `Monde_Neutre` ou sur `Monde_Studio` baissé | Les trois points, *Power*, *Size*, sélecteur de monde |
| 2 | V1 et V2 rendues avec cette lumière, chacune à sa résolution, puis enregistrées | `Ctrl + 0`, rubrique *Format*, `F12`, *Image > Save As* sur *Follow Scene* |
| 3 | La situation : *Mise_en_situation* visible (œil et appareil photo), *Studio* et *Nuancier* masqués, une HDRI d'intérieur ou d'extérieur, `Eclairage_studio` éteint si besoin. La matière du plateau, ouverte dans le *Shader Editor* | Outliner, onglet *World*, rotation Z du *Mapping*, nœuds du chapitre 3 |
| 4 | `CAM_situation`, vers `35mm`, à hauteur d'yeux d'une personne assise ; 1920 × 1080, `F12`, puis `lampe_situation_<initiales>_v001.png` | Caméra active, focale, cadrage en naviguant, export |
| 5 | *File > External Data > Pack Resources*, `Ctrl + S` ; les trois PNG copiés dans le dossier de la galerie | Basics 102, Explorateur Windows |

**Déroulé :**
1. **Lancement (3 min).** La situation, les livrables et le nom du dossier de la galerie, au paperboard. Projetez la vue de situation et les paliers du corrigé, d'après § 4 « Consignes · Le concept final, par paliers » (figures 4.39 à 4.41). « Le plateau est en chêne plaqué, posé en projection *Box* comme vos finitions du chapitre 3 : sélectionnez-le, et lisez sa matière dans le *Shader Editor*. » Lancez le minuteur et annoncez l'heure du dépôt : 3:15.
2. **Autonomie (36 min).** Chacun suit la partie « Atelier » du LISEZ-MOI. À 2:55, chacun a exporté au moins la vue héros : passez d'abord voir ceux qui n'ont pas de post-it vert. Annoncez les 5 dernières minutes : on empaquette et on enregistre.
3. **Quiz (1 min),** ensemble à l'écran : le quiz récapitulatif de la section 4, à plusieurs bonnes réponses. C'est la liste des vérifications avant l'envoi.
4. **Dépôt (5 min).** Chacun copie ses trois PNG dans le dossier de la galerie. Vous vérifiez les noms, puis lancez le diaporama.

**Paliers :**
- **★ :** une version de la vue héros à fond transparent (*Film > Transparent*, *RGBA*) ; une vue technique de profil, avec une caméra *Orthographic* face à la lampe et `Monde_Neutre` ; la gamme : *File > Append* de `Lampe_coloris_B` depuis `lampe_habillage_v002.blend` (dans le fichier de secours, on ouvre son œil et son appareil photo), puis une caméra `CAM_gamme` qui cadre les deux lampes : `lampe_gamme_<initiales>_v001.png`.
- **★★ :** la lampe allumée pour la vue de situation. Un *Spot* dans la tête, devant l'ampoule et tourné comme la tête, *Temperature* à 2700 K, *Power* vers 12 W, `Eclairage_studio` éteint ; sur l'ampoule, la matière fournie `Ampoule_allumee`, choisie dans la liste des matières (figure 3.6). Ou le même studio pour un autre objet : la liseuse de cabine du chapitre 2, la maquette en kit ou la rangée de sièges de l'initiation.

**Ce que vous regardez dans les visuels,** pour vos retours pendant le tour des postes et la galerie :
- les livrables sont conformes : trois vues, leurs formats, leurs noms ;
- la forme se lit : la silhouette se détache du fond, la lumière modèle les volumes ;
- les matières sont crédibles : le métal, la laque, le plastique et le verre se reconnaissent ;
- le cadrage est maîtrisé : focale adaptée, composition, aucune coupe gênante ;
- le fichier est propre : caméras et lumières nommées, ressources empaquetées.

**Points d'observation :**
- Le nuancier apparaît dans un visuel : fermez l'œil et l'appareil photo de sa collection.
- Un sol qui scintille sous le plateau de bureau : la collection *Studio* est restée visible. Masquez-la pour la vue de situation.
- Le plateau paraît uni : la vue est en mode *Solid*, qui ne montre que sa couleur d'affichage. Le chêne se voit en *Material Preview*, en *Rendered* et au rendu.
- Au palier ★, `ABS_Noir.001` ou `PVC_Mat_Noir.001` apparaissent après l'Append du coloris B : des copies des matières partagées par les deux coloris, sans effet sur le rendu.
- Au palier ★, les deux lampes se touchent : le décalage de 750 mm du chapitre 3 a été oublié. Clic droit sur `Lampe_coloris_B` > *Select Objects*, puis `G X = 750mm`.
- Au palier ★★, la pièce est noire autour du cône : le corrigé garde `Monde_Interieur`, baissé vers 0,12, plutôt que `Monde_Neutre`.
- Un apprenant perdu à la fin de la section 3 ouvre le fichier de secours et l'enregistre sous `lampe_rendu_v001.blend`. Il rend visibles « Corrigé éclairage » et « Corrigé caméras » (œil et appareil photo), applique les lignes « Corrigé » du LISEZ-MOI, puis commence l'atelier de là.

**Corrigé :** `CAM_situation_corrige`, dans « Corrigé caméras » : 35 mm, à X `-300mm`, Y `-850mm`, Z `450mm`, le regard d'une personne assise au bureau. La collection « Corrigé paliers » : `Spot_lampe_corrige` (*Spot*, 12 W, 2700 K, *Angle* 70°, *Blend* 0,3), `CAM_gamme_corrige` (70 mm) et `CAM_profil_ortho_corrige` (*Orthographic*). Les images du corrigé, dont `PRC02_ch4_corrige_situation_allumee.png` pour le palier ★★.

## Le bilan de la formation

**De 3:35 à 3:50 · 15 min · collectif.** D'après § 4 « Bilan de la formation ». C'est un bilan pédagogique : il récapitule, ouvre sur la suite et répond aux questions. Il n'apporte rien de nouveau.

**Les six demi-journées (6 min).** Projetez les six vignettes préparées avant la séance, une à une. Pour chacune, le groupe nomme un geste clé. Exemples de réponses :
- prendre ses repères, la maquette en kit : deux vues orthographiques avant de valider ;
- modéliser, la rangée de sièges et la clinique du fichier : *Array* et *Mirror*, l'échelle appliquée ;
- chapitre 1, le blocage de la lampe : taper l'unité, `G Z Z`, comparer des silhouettes ;
- chapitre 2, la lampe modélisée : des modificateurs jamais appliqués, les courbes ;
- chapitre 3, la lampe habillée : le *Principled BSDF*, la projection *Box*, la bibliothèque de matières ;
- chapitre 4, un visuel de la galerie : trois lumières, une longue focale, *Image > Save As*.

Reliez ce parcours aux cinq objectifs du programme : optimiser son environnement de travail, explorer un concept par le blocage, modéliser de façon non destructive, créer des matières sans dépliage complexe, produire des visuels en temps réel avec EEVEE.

**Les ressources pour continuer (4 min) :**
- l'application support : les chapitres, les quiz et les défis, avec ses mises à jour ;
- les fichiers de la formation, avec leurs consignes par paliers et leurs corrigés ;
- leur bibliothèque CMF du chapitre 3 et le studio de ce chapitre, à réutiliser pour leurs projets ;
- Poly Haven (polyhaven.com), pour des HDRI et des textures sous licence CC0 ;
- le manuel officiel de Blender, en anglais, avec les mêmes libellés que l'interface.

**Questions et tour de table (5 min).** Le temps qui reste sert aux questions du groupe. Pour finir, chacun dit en une phrase ce qu'il appliquera dès la semaine prochaine.

Avant le départ du groupe, faites remplir le questionnaire de satisfaction et l'évaluation des objectifs, selon la procédure de VIV Formation.

## Gérer l'hétérogénéité

### Le parcours « première fois »

- Les binômes et les copilotes des demi-journées précédentes restent en place.
- Le fichier de secours est le filet de sécurité : la règle des 3 minutes au lancement, puis le point de reprise à tout moment. Personne ne manque l'atelier faute de lampe.
- Les recettes de l'application et le LISEZ-MOI donnent chaque geste. Les valeurs restent indicatives : chacun peut les adapter à son concept.
- Orienter une lumière est le geste le plus délicat du jour : placez-la en vue de dessus (`7`), puis de face (`1`), et suivez la ligne qui part d'elle.
- Le socle de chaque séquence suffit : il couvre tous les points du programme.
- À chaque point de contrôle, passez d'abord par les postes des débutants.
- **Un apprenant très en retard** garde sa `Key` et passe `Fill_corrige` et `Rim_corrige` dans `Eclairage_studio` avec `M`, puis vérifie leur œil et leur appareil photo. Pour les caméras, il ouvre l'œil et l'appareil photo de « Corrigé caméras », puis fait de `CAM_heros_corrige` la caméra active (`Ctrl + 0`). Ses visuels comptent comme ceux des autres.

### Pour ceux qui avancent vite

- Les paliers ★ de l'atelier, puis les ★★.
- **Le *Spot* réglé finement (★★) :** *Angle* et *Blend*, rubrique *Beam Shape* (figure 4.41), pour un cône net ou doux sur le plateau.
- **Leur propre ampoule allumée (★★) :** la rubrique *Emission* de la matière (figure 3.15), au lieu de la matière fournie.
- **L'éclat de l'ampoule (★★) :** un nœud *Glare*, de type *Bloom*, dans le compositeur.
- **Toutes les vues d'un coup (★★) :** un marqueur par caméra dans la *Timeline*, *Marker > Bind Camera to Markers*, le chemin de sortie de l'onglet *Output*, puis *Render > Render Animation*.
- **Des lumières qui suivent la lampe (★★) :** une contrainte *Damped Track* vers un *Empty*.
- **Le studio en bibliothèque (★★) :** le studio et ses lumières rangés en actifs, comme les matières du chapitre 3.
- Ces défis apportent une notion nouvelle. Ils n'ont pas de corrigé, sauf le *Spot* (`Spot_lampe_corrige`) : vous les validez à l'écran.
- Le rôle de copilote, comme aux demi-journées précédentes.

## Animer : ce qui change au chapitre 4

Les conseils de l'initiation restent valables : « Regardez, puis à vous », les touches dites à voix haute, les post-it vert et rose, la règle des 3 minutes, la souris qu'on ne prend pas. Ce chapitre en ajoute six :
1. **Faites juger sur une image rendue.** La vue *Rendered* sert à régler, `F12` à décider. Deux emplacements et `J` valent mieux qu'un souvenir.
2. **Une lumière à la fois.** Partez du noir, ajoutez une lumière, regardez ce qu'elle apporte, puis passez à la suivante. Faites fermer les yeux de l'Outliner à tour de rôle : le rôle de chacune se voit.
3. **Occupez les temps de rendu.** Pendant un `F12`, posez la question du cycle ou faites deviner ce qui va changer. La grille du paperboard aide chacun à choisir ses échantillons sans attendre les autres.
4. **Parlez photo et revue de design :** principale, secondaire, contre-jour, focale, point fort, livrable. Ce sont les mots du studio et du client.
5. **Protégez l'heure du dépôt.** La vue héros est exportée à 2:55, les trois PNG sont déposés à 3:20. Un apprenant en retard prend le point de reprise plutôt que de manquer la galerie.
6. **Terminez sur les réussites.** La galerie et le bilan clôturent six demi-journées : commencez chaque retour par ce qui fonctionne, et rappelez le chemin parcouru depuis la maquette en kit.

## Si vous prenez du retard

Raccourcissez dans cet ordre. Entre parenthèses, le temps gagné :

| Ordre | Ce que l'on coupe | Ce que l'on garde |
|---|---|---|
| D'abord | HDRI : pas de mise en place dans un monde neuf ; on bascule seulement entre les mondes préparés (3 min) | Le sélecteur de monde et la rotation Z du *Mapping* |
| Ensuite | Section 1 : la transformation de vue reste une démo, sans essai (5 min) | Le choix de *Khronos PBR Neutral*, dit et donné par la ligne « Corrigé » |
| Ensuite | Section 3 : la vue de détail sans profondeur de champ (5 min) | Le format 1080 × 1080 et l'export nommé |
| Ensuite | Studio : chacun règle seulement `Key`. `Fill_corrige` et `Rim_corrige` passent dans `Eclairage_studio` avec `M` ; vérifiez leur œil et leur appareil photo (10 min) | Le rôle des trois lumières, montré en démo |
| En dernier | Galerie : le diaporama seul, sans restitution (10 min) | Le dépôt dans la galerie et le bilan |

**Ce qui ne saute jamais,** car l'atelier et la galerie en dépendent : l'export des trois vues et le bilan ; la case *Raytracing* et sa raison ; `F12`, les emplacements et `J` ; le sélecteur de monde ; une lumière principale réglée par chacun, dans `Eclairage_studio` ; la caméra active (`Ctrl + 0`) et *Align Active Camera to View* ; la focale ; la résolution, réglée vue par vue ; *Image > Save As* sur *Follow Scene* ; *Pack Resources*.

## Si vous êtes en avance

- **L'atelier s'enrichit :** les paliers ★, puis ★★, puis les défis de « Pour ceux qui avancent vite », en commençant par le *Spot* réglé finement.
- **La restitution s'allonge :** chacun présente ses trois visuels, au lieu d'un seul.
- **Le bilan s'ouvre :** montrez à l'écran un défi réussi, par exemple toutes les vues rendues d'un coup.

---

Les fichiers `PRC02_ch4_…` se reconstruisent avec les scripts de `tool/exercices_ch4/` : `construire.ps1` lance `build_studio.py` (Blender 5.2 en arrière-plan), puis `finish_ui.py` pour la zone LISEZ-MOI, et contrôle chaque fichier avec `verifier_blend.py`. Les HDRI et le placage de chêne de Poly Haven restent hors du dépôt, dans `tool/exercices_ch4/hdri/` et `tool/exercices_ch4/textures/`. Ce document se convertit en PDF avec `tool/deroule_initiation/export_pdf.ps1 -Source _resources\PRC02-deroule-chap4.md`.
