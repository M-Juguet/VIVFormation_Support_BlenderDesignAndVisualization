# Chapitre 3 · Matières et finitions sans dépliage UV : déroulé formateur

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 5 sur 6, en présentiel, de 5 à 8 apprenants · Version du 25 novembre 2026 : le lot de textures PBR du socle entre dans le fil rouge. Il paraît dans l'application à la version qui suit la 1.1.0.

## En bref

- **Objectif :** à la fin de la demi-journée, chaque apprenant règle une matière de métal, de plastique ou de verre avec le Principled BSDF. Il ajoute une finition brossée, grainée ou structurée, puis pose un lot de textures PBR sur le socle, sans dépliage UV. Il range ses matières en actifs dans l'Asset Browser et récupère une matière d'un autre fichier avec *File > Append*. Enfin, il décline sa lampe en un second coloris.
- **Format :** 3 h 50, dont 3 h 30 de contenu et 2 pauses de 10 minutes. Il reste 10 minutes de marge sur 4 heures. Exemple : de 9 h 00 à 12 h 50. La première pause tombe à la même heure qu'à la première demi-journée de l'initiation ; la seconde, quatre minutes plus tard, à 2:44, après le lot PBR.
- **Principe :** le même qu'à l'initiation. Une notion à la fois : vous la montrez en quelques minutes, ils la pratiquent en guidé, puis seuls. Personne ne passe plus de 15 minutes sans toucher la souris. C'est le chapitre le plus abstrait : la section 1 se fait entièrement dans l'onglet *Material*, sans aucun nœud ; le Shader Editor n'arrive qu'en section 2, un nœud à la fois. Tout le chapitre se fait en vue *Material Preview*.
- **L'idée du jour : une matière se partage.** Plusieurs pièces peuvent porter la même matière, comme les roues de la maquette partageaient leur maillage à l'initiation. Avant de changer une matière pour une seule pièce, un clic sur son compteur la rend indépendante. Ce geste revient au socle structuré (2:11) et au coloris B (atelier). Au lot PBR (2:32), le bouclier garde la peinture structurée dans le fichier.
- **Fil rouge :** la lampe modélisée au chapitre 2, `lampe_modele_v001.blend`, enregistrée sous `lampe_habillage_v001.blend`. Elle repart habillée, en deux coloris, ses matières rangées en actifs, dans `lampe_habillage_v002.blend`. Le socle du coloris A y porte un lot de textures PBR, au choix de l'apprenant : noyer, béton ou palissandre. Le chapitre 4 en importe la collection *Lampe* par *File > Append*.

### Ce que l'on survole

Ces notions sont dans l'application. Elles ne sont pas exigées en séance, et certaines servent de défi.
- Le choix de l'image d'environnement et sa rotation (figure 3.3) : une option, dans votre démo de 0:35.
- `Ctrl + L > Link Materials` (figure 3.7) : une astuce pour les plus rapides.
- L'IOR : cité avec le verre ; on n'y touche pas.
- Le verre dépoli ou fumé : un défi ★, l'essai en autonomie de 1:15 n'est plus minuté.
- *Emission* (figure 3.15) et les deux matières d'une pièce (figures 3.16 et 3.17) : des défis ★.
- Ce qu'EEVEE simplifie (*Anisotropic*, le nœud *Bevel*, *Thin Film*) : une phrase, au moment du brossé.
- *Node Wrangler* (figure 3.36), son `Ctrl + Maj + T` pour charger un lot d'un coup (figure 3.37), et *Automatically Pack Resources* : cités.
- La carte de hauteur `disp` d'un lot, par un *Bump* chaîné au *Normal Map* : pour ceux qui ont fini.
- La description d'un actif, dans la barre latérale de l'Asset Browser : un défi ★, montrée dans votre démo de 2:54.
- *Link* : une phrase ; sa manipulation devient un défi ★ (figure 3.53).
- La bibliothèque déclarée dans les préférences et le menu *Import Method* (figures 3.48 à 3.50) : une minute de démonstration sur votre poste. Les préférences des postes ne sont pas touchées.
- Le défi facultatif « Matières procédurales », dans la rubrique « Pour aller plus loin » de la barre latérale : hors minutage, voir sa partie plus bas.

### Les fichiers

| Fichier | Moment | Contenu |
|---|---|---|
| `lampe_modele_v001.blend` | 0:00 | Le fichier de fin du chapitre 2, propre à chaque apprenant ; enregistré sous `lampe_habillage_v001.blend` |
| `PRC02_ch3_lampe_a_habiller.blend` | 0:00 (secours), puis vos démos jusqu'à 3:12 | La lampe du chapitre 2, sans matière ; les collections masquées *Corrigé coloris A* (sections 1 à 3, socle en peinture structurée), *Corrigé socle PBR* (le socle en noyer, fin de la section 2) et *Corrigé coloris B* (atelier), dont les matières portent le suffixe `_corrige`. Les images du corrigé sont empaquetées : 1,9 Mo |
| `PRC02_bibliotheque_CMF.zip` | 0:35 (votre démo), 3:12, atelier | Le dossier `PRC02_bibliotheque_CMF` : le nuancier `PRC02_ch3_nuancier_cmf.blend` (vingt-cinq matières en cinq catalogues, et la grille *Metallic* / *Roughness*) et son `blender_assets.cats.txt`. C'est aussi le corrigé du rangement en actifs |
| `PRC02_ch3_textures_cmf.zip` | 2:11 | Le dossier `textures_cmf` : cinq images raccordables, dont `grain_structure.png`, et un `LISEZ-MOI.txt` |
| `PRC02_ch3_finitions_triplanaires.blend` | 2:11 (votre démo), défis ★★ | Cinq pièces sans dépliage UV, des trois secteurs ; la collection masquée *Corrigé* |
| `PRC02_ch3_textures_pbr.zip` | 2:32 | Le dossier `textures_pbr` : trois lots CC0 de Poly Haven en 1K, un sous-dossier par lot : `walnut_veneer_02` (noyer, celui de la recette), `granular_concrete` (béton lisse) et `rosewood_veneer1` (palissandre verni). Quatre cartes JPG par lot (`diff`, `rough`, `nor_gl`, `disp`) et un `LISEZ-MOI.txt` : source, licence, *Color Space* de chaque carte. 6,7 Mo |
| `PRC02_ch3_lampe_habillage.zip` | 0:00 (le but du jour), fin | Un exemple de `lampe_habillage_v002.blend`, avec son fichier de catalogues ; un point de départ possible du chapitre 4. Son socle garde la peinture structurée : ceux des apprenants portent leur lot PBR |
| `PRC02_ch3_defi_procedural.blend` | Hors minutage | Le défi facultatif ; la collection masquée « Corrigé défi procédural » |
| `PRC02_CMF_planche.zip` | Après la séance, ou pour une présentation CMF | La ressource complémentaire qui ferme le chapitre : une planche de présentation sous éclairage fixe et neutre, vierge et habillée, avec les matières du chapitre en actifs, des gabarits réglables et un mémo d'une page |

L'application propose la lampe à habiller en section 1, sous « Où l'on en est ». Les images et les finitions triplanaires sont en section 2, sous « Une image projetée sur trois axes : Box » ; les lots PBR, plus loin dans la même section, sous « Où trouver des lots : Poly Haven ». La bibliothèque est en section 3, sous « Récupérer une matière : File > Append ». La lampe habillée suit l'atelier, et la planche CMF ferme le chapitre. Le défi est dans la rubrique « Pour aller plus loin » de la barre latérale (Défi 2).

> **À savoir :** chaque fichier `.blend` du chapitre contient un texte LISEZ-MOI, affiché à l'ouverture : en bas de l'écran dans l'espace *Layout*, en haut à gauche dans les deux fichiers qui s'ouvrent sur l'espace *Shading*. Il donne les consignes par paliers (socle, ★, ★★) et dit où se trouve le corrigé. Ce document n'a donc pas d'annexe de consignes : projetez le LISEZ-MOI ou renvoyez-y. Celui de la lampe marque *Coat* et le grain de l'ABS d'une étoile : en séance, tout le monde les fait. Les matières des corrigés ne sont pas des actifs : la bibliothèque *Current File* est vide au début de la section 3. Un apprenant qui garde sa propre lampe n'a pas le corrigé dans son fichier : il le voit sur votre écran, ou ouvre `PRC02_ch3_lampe_a_habiller.blend` dans une seconde fenêtre de Blender.

## Avant la demi-journée

### Les postes des apprenants

- [ ] L'application support 1.0.0 est installée. Une version plus ancienne propose la mise à jour à son démarrage.
- [ ] Le dossier de travail contient le fichier de fin du chapitre 2, `lampe_modele_v001.blend`.
- [ ] Il contient aussi les fichiers du chapitre 3, décompressés : `PRC02_ch3_lampe_a_habiller.blend`, les dossiers `textures_cmf` et `textures_pbr`, et le dossier `PRC02_bibliotheque_CMF`, où le nuancier reste à côté de son `blender_assets.cats.txt`. À défaut, chacun les télécharge depuis l'application au moment voulu.
- [ ] Blender 5.2 LTS s'ouvre, avec une souris à trois boutons : la molette cliquée déplace la vue du Shader Editor.
- [ ] Les préférences des postes ne sont pas modifiées : le parcours principal n'en a pas besoin.
- [ ] **Le temps de compilation des matières, à tester sur le poste le plus modeste de la salle.** Mesurez la première bascule en *Material Preview* sur la lampe à habiller, puis le même affichage avec la case *Raytracing* cochée, puis le fichier du défi avec toutes ses collections visibles. Ce temps n'a pas encore été mesuré sur un poste de la salle. Si un poste peine, la parade est prévue à 1:15.

### Votre poste de démonstration

- **Lancez Blender en configuration d'usine** (`blender.exe --factory-startup`), comme à l'initiation : votre écran correspond à celui des apprenants, et vos préférences ne sont pas touchées. En contrepartie, une bibliothèque déclarée dans les préférences ne survit pas à un redémarrage : pour l'option de 3:12, déclarez-la pendant la pause de 2:44.
- **Agrandissez l'interface** pour le vidéoprojecteur : *Resolution Scale* à 1,3.
- **Préparez une copie de travail de `PRC02_ch3_lampe_a_habiller.blend`,** enregistrée sous un autre nom, avec les dossiers `textures_cmf` et `textures_pbr` à côté. Toutes vos démos sur la lampe s'y font, et ses corrigés se projettent aux points de contrôle. Sa case *Raytracing* est décochée, comme chez les apprenants : vous la cochez à 1:15.
- **Gardez à portée** le dossier `PRC02_bibliotheque_CMF` (démos de 0:35 et 3:12), une copie de `PRC02_ch3_finitions_triplanaires.blend` (démo de 2:11) et la lampe habillée, décompressée de `PRC02_ch3_lampe_habillage.zip` (ouverture). Enregistrez votre copie avant chaque changement de fichier ; *File > Open Recent* vous ramène à la lampe.
- **Gardez l'application ouverte** sur le chapitre 3, pour projeter les figures et les quiz.
- **Pour la démo de Poly Haven (2:32),** vérifiez l'accès à Internet de votre poste et ouvrez à l'avance la page du noyer, `https://polyhaven.com/a/walnut_veneer_02`. Sans Internet, décrivez le téléchargement d'après le § 2 « Où trouver des lots : Poly Haven » : le dossier `textures_pbr` contient déjà les trois lots.

### Le matériel de la salle

- Les post-it vert et rose des points de contrôle, et le minuteur.
- Le paperboard, préparé avant l'arrivée des apprenants :
  - l'idée du jour : « Une matière se partage. Avant de la changer pour une seule pièce : un clic sur son compteur. » ;
  - le cahier CMF du coloris A : *Socle* et *Tête* `Peinture_Vert`, puis `Structure_Vert` sur le socle, puis le lot PBR `Bois_Noyer` (ou `Beton_Lisse`, `Palissandre_Verni`) ; *Interrupteur*, ses crans et *Grille_aeration* `ABS_Noir` ; bras `Alu_Naturel`, qui devient `Alu_Brosse` ; articulations `Chrome` ; *Câble* `PVC_Mat_Noir` ; *Ampoule* `Verre_Clair` ; *Douille* `Alu_Naturel`, pris dans le nuancier ;
  - le corrigé : « collections *Corrigé coloris A* et *B*, œil fermé, dans `PRC02_ch3_lampe_a_habiller.blend` : on compare, on ne copie pas » ;
  - les fichiers : `lampe_habillage_v001.blend`, puis `lampe_habillage_v002.blend`, toujours avec `blender_assets.cats.txt` à côté ;
  - la chaîne des finitions, complétée au fil de la section 2 : *Texture Coordinate* (*Object*) → *Mapping* → texture → *Bump* → entrée *Normal* du Principled ; puis celle du lot PBR : un seul *Mapping* → trois *Image Texture* en *Box* → `diff` (*sRGB*) dans *Base Color*, `rough` (*Non-Color*) dans *Roughness*, `nor_gl` (*Non-Color*) → *Normal Map* → *Normal* ;
  - les raccourcis du jour, complétés au fil de la séance : `/` ; dans le Shader Editor, `Maj + A`, `G`, `X`, `Maj + D` et `Origine` ; `Ctrl + A > Scale` ; `N` dans l'Asset Browser.

## La demi-journée · Habiller la lampe

Les trois sections du chapitre 3, puis l'atelier. Les apprenants repartent avec leur lampe habillée, en deux coloris, ses matières rangées en actifs, dans `lampe_habillage_v002.blend`. Les neuf quiz des sections 1 à 3 se font ensemble à l'écran, une minute chacun, à la fin de la séquence qui les prépare. Dans la colonne « Modalité », les durées sont en minutes.

| Horaire | Durée | Séquence | Section | Modalité |
|---|---|---|---|---|
| 0:00 | 15 min | Ouverture et check-up du modèle | | Collectif 5 + poste 10 |
| 0:15 | 20 min | Une matière dans Blender | 1 | Démo 7 + guidé 13 |
| 0:35 | 30 min | Métal et plastique, puis *Coat* | 1 | Démo 7 + guidé 7 + autonomie 9 + quiz 1 ; *Coat* : démo 2 + guidé 3 + quiz 1 |
| 1:05 | 10 min | Pause | | |
| 1:15 | 16 min | Le verre | 1 | Démo 6 + guidé 9 + quiz 1 |
| 1:31 | 15 min | Le Shader Editor : la matière en nœuds | 2 | Démo 6 + guidé 9 |
| 1:46 | 25 min | Finitions procédurales sans UV | 2 | Démo 8 + guidé 11 + autonomie 5 + quiz 1 |
| 2:11 | 21 min | Projection triplanaire d'images | 2 | Démo 8 + guidé 9 + autonomie 3 + quiz 1 |
| 2:32 | 12 min | Un lot de textures PBR sur le socle | 2 | Démo Poly Haven 2 + démo 3 + guidé 5 + *Pack Resources* 1 + quiz 1 |
| 2:44 | 10 min | Pause | | |
| 2:54 | 18 min | Ranger ses matières en actifs | 3 | Démo 6 + guidé 7 + autonomie 4 + quiz 1 |
| 3:12 | 12 min | Réutiliser : récupérer une matière par Append | 3 | Démo 5 + guidé 6 + quiz 1 |
| 3:24 | 20 min | Atelier · Le second coloris | | Lancement 2 + autonomie 16 + revue 2 |
| 3:44 | 6 min | Tour des postes, bilan et passerelle vers le chapitre 4 | | Collectif, dont 1 quiz |

Le lot PBR du socle a pris 12 minutes, reprises ailleurs avec l'accord du formateur (25 novembre 2026) : l'essai du verre dépoli ou fumé devient un défi ★ (−4) ; *Pack Resources* passe après le lot, un seul geste pour toutes les images (−3) ; le quiz du *Bump* devient celui du lot (−1) ; la description d'un actif devient un défi ★ (−2) ; le bilan garde une question orale sur deux (−2).

### 0:00 · Ouverture et check-up du modèle (15 min)

- **Le parcours de la lampe (collectif, 5 min) :** bloquée au chapitre 1, modélisée au chapitre 2, habillée aujourd'hui, mise en scène au chapitre 4.
- **Montrez le but :** ouvrez la lampe habillée, `PRC02_ch3_lampe_habillage.blend`, en *Material Preview* : les deux coloris côte à côte (figure 3.1). « À la fin de la demi-journée, votre lampe ressemble à celle-ci, et ses matières sont rangées pour vos prochains projets. »
- **Le mot du jour :** CMF, pour *Color, Material, Finish*. C'est le métier qui choisit les teintes, les matières et les finitions d'un produit : la sellerie d'un train, la planche de bord d'une voiture, l'habillage d'une cabine d'avion.
- **Une phrase sur les Basics,** qui l'annonçaient : « *Material Preview* sert aujourd'hui à juger les matières ; *Rendered* viendra au chapitre 4, consacré au rendu. »
- **Une phrase sur le défi :** « Pour ceux qui sont à l'aise, ou qui connaissent déjà ces sujets : un défi facultatif, hors programme, dans la rubrique « Pour aller plus loin » de l'application. » Pas de démonstration.

**Le check-up (sur poste, 10 min),** d'après § 1 « Recette · Prendre le fichier en main » : chacun ouvre `lampe_modele_v001.blend` et l'enregistre aussitôt sous `lampe_habillage_v001.blend` (*File > Save As*). Puis il vérifie cinq points déjà vus, numérotés de 2 à 6 dans l'application :
- chaque pièce porte un nom clair dans la collection *Lampe* ;
- l'échelle est appliquée : *Scale* à 1 dans `N > Item`, sinon `Ctrl + A > Scale` ;
- aucune face rouge en *Face Orientation* ;
- aucune facette sur les pièces courbes, surtout les tiges des bras et les articulations, qui seront en métal : sinon *Object > Shade Auto Smooth* ;
- le moteur de rendu est EEVEE, dans l'onglet *Render* : le fichier du chapitre 1 était réglé sur Cycles.

Un modèle incomplet ou abîmé ? L'apprenant ouvre `PRC02_ch3_lampe_a_habiller.blend` et l'enregistre sous `lampe_habillage_v001.blend`.

**Point de contrôle :** un post-it vert sur chaque écran. Les cinq points sont bons, ou le fichier de secours est ouvert ; la barre de titre affiche `lampe_habillage_v001.blend`.

**Corrigé :** pas de corrigé pour le check-up : la collection *Lampe* du fichier de secours est le modèle vérifié.

**Pièges fréquents :**
- Un apprenant répare son modèle depuis plus de 5 minutes : arrêtez-le, le fichier de secours est fait pour cela.
- Des faces rouges, une échelle différente de 1 : ce sont les patients 1 et 2 de la clinique du fichier. Renvoyez-y : `Tab`, `A`, `Maj + N` ; puis `Ctrl + A > Scale` en Mode Objet.
- Un fichier resté sur Cycles : la case *Raytracing* de 1:15 n'apparaîtra pas. Corrigez-le maintenant.

### 0:15 · Une matière dans Blender (20 min)

**Vous montrez (7 min),** d'après § 1 « Voir les matières : Material Preview » (figure 3.2), « Créer et nommer une matière » (figures 3.4 et 3.5) et « Une matière pour plusieurs pièces » (figure 3.6), sur votre copie de la lampe à habiller :
1. En *Solid*, aucune matière ne s'affiche. Le bouton *Material Preview*, en haut à droite de la vue 3D : Blender calcule les matières avec EEVEE. Prévenez : « La première bascule fige l'écran quelques secondes. C'est normal. »
2. Le socle sélectionné : onglet *Material*, la sphère rouge, bouton *New*. Double-clic sur le nom : `Peinture_Vert`. La rubrique *Surface* indique *Principled BSDF*. « Aujourd'hui, un seul réglage : *Base Color*. » Changez la teinte.
3. La tête sélectionnée : l'icône à gauche du nom ouvre la liste des matières ; choisissez `Peinture_Vert`. Le chiffre 2 apparaît à droite du nom. Changez la teinte : les deux pièces changent. « Vous avez déjà vu ça : les roues de la maquette. »
4. **Ailleurs :** une même teinte sur toutes les pièces d'une livrée de train, d'une gamme de carrosserie ou d'un habillage de cabine.

**Ils font, en guidé (13 min),** d'après § 1 « Recette · Une peinture et un plastique partagés », étapes 1 à 5 : *Material Preview* ; `Peinture_Vert` sur le socle, puis sur la tête par la liste ; `ABS_Noir`, un gris très sombre, sur l'*Interrupteur*, puis sur *Interrupteur_crans* et *Grille_aeration* par la liste.

**Point de contrôle :** socle et tête de la même teinte ; interrupteur, crans et grille en gris très sombre. Le compteur affiche 2 pour `Peinture_Vert` et 3 pour `ABS_Noir`.

**Corrigé :** la collection *Corrigé coloris A*, objets suffixés `_A`. Elle montre l'état de fin de section 3 : le socle y porte déjà sa peinture structurée.

**Pièges fréquents :**
- Pas d'onglet *Material* : un *Empty* est sélectionné, *Grille_pivot* ou *Interrupteur_pivot*. Sélectionnez la pièce elle-même.
- *New* sur une pièce qui a déjà une matière en crée une nouvelle, `Material.001` : renommez-la aussitôt.
- La matière choisie dans la liste arrive sur la mauvaise pièce : l'objet actif n'était pas celui que l'on croyait. `Ctrl + Z`.
- Pour les plus rapides : `Ctrl + L > Link Materials` donne la matière de l'objet actif à toute la sélection (figure 3.7).

### 0:35 · Métal et plastique, puis *Coat* (30 min)

**Vous montrez (7 min),** d'après § 1 « Métal ou non : Metallic » et « Du poli au mat : Roughness » (figure 3.8), sur le nuancier `PRC02_ch3_nuancier_cmf.blend` :
1. La grille du fond : rangée arrière *Metallic* 1, rangée avant *Metallic* 0 ; de gauche à droite, *Roughness* de 0 à 1.
2. *Metallic* vaut 0 pour un plastique, une peinture ou un verre, 1 pour un métal. « Une valeur entre les deux ne correspond à aucune matière réelle : la pièce paraît sale. »
3. La couleur d'un métal se règle dans *Base Color* : gris clair pour l'aluminium, jaune doré pour le laiton. Montrez la pastille `Laiton`.
4. En option, d'après § 1 « Voir les matières : Material Preview » (figure 3.3) : le menu *Viewport Shading*, l'image *studio*, puis *Rotation*. Les reflets glissent : « C'est ainsi qu'on juge une finition. » *Scene Lights* et *Scene World* restent décochées, pour le chapitre 4.
5. **Ailleurs :** une jante en aluminium ou une planche de bord en plastique (automobile), une main courante en inox (ferroviaire), un carénage en aluminium (aéronautique). Le § « Des valeurs de départ » donne les réglages de chaque famille : projetez-le.

Revenez à la lampe par *File > Open Recent*.

**Ils font, en guidé (7 min),** d'après § 1 « Recette · L'aluminium des bras » : `Alu_Naturel` sur *Bras_bas*, *Metallic* `1`, *Roughness* `0.3`, *Base Color* gris très clair ; puis la même matière sur *Bras_haut*, par la liste.

**Ils font, seuls (9 min),** d'après § 1 « Consignes · Le chrome, le câble et le plastique » :
- `Chrome` sur les trois articulations : *Metallic* `1`, *Roughness* `0.03` ;
- `PVC_Mat_Noir` sur le câble : *Roughness* `0.7`, *Base Color* presque noire ;
- la *Roughness* de `ABS_Noir` à `0.15`.

**Quiz (1 min),** ensemble à l'écran : le premier quiz de la section 1, l'aluminium qui ressemble à du plastique.

***Coat* (démo 2 min, guidé 3 min).** Vous montrez, d'après § 1 « Laque et vernis : Coat » et « La rubrique Coat » (figure 3.9) : sur `Peinture_Vert`, dépliez la rubrique *Coat*, *Weight* `1`, *Roughness* `0.03`. La peinture devient une laque, au reflet net. **Ailleurs :** une carrosserie, une livrée de train, un carénage peint. Ils font la même chose sur leur peinture.

**Quiz (1 min),** ensemble à l'écran : le troisième quiz de la section 1, le vernis.

**Point de contrôle :** vue de face, en *Material Preview*. On distingue au premier regard le métal, aux reflets nets et colorés par l'environnement, la laque, au reflet net sur la teinte, et le plastique.

**Corrigé :** dans *Corrigé coloris A*, `Chrome_corrige`, `PVC_Mat_Noir_corrige`, `ABS_Noir_corrige` et `Peinture_Vert_corrige`. Les bras y sont déjà brossés (`Alu_Brosse_corrige`) : c'est l'état de la section 2.

**Pièges fréquents :**
- *Metallic* à 0,5 : la pièce paraît sale. Revenez à 0 ou à 1.
- Une pièce qui perd tout modelé : sa *Base Color* est noire pure. Gardez un gris très sombre.
- Des reflets en escalier sur une tige : *Shade Auto Smooth* manque (point 5 du check-up).
- Le câble est une courbe : son onglet *Material* fonctionne comme celui d'un maillage.
- Gardez le nom `Alu_Naturel` jusqu'à 1:46 : il devient alors `Alu_Brosse`, ce qui évite un conflit avec l'`Alu_Naturel` du nuancier à 3:12.

### 1:05 · Pause (10 min)

### 1:15 · Le verre (16 min)

**Vous montrez (6 min),** d'après § 1 « Le verre : Transmission » (figure 3.10), « Voir à travers le verre : deux interrupteurs » (figures 3.11 à 3.13) et « Un verre fin : Thin Wall » (figure 3.14) :
1. L'ampoule et la tête sélectionnées, `/` : la vue locale. `Verre_Clair` sur l'ampoule ; dépliez *Transmission*, *Weight* `1` ; *Roughness* `0`. L'ampoule ne montre que le paysage de l'image d'environnement. Faites deviner pourquoi.
2. Les deux interrupteurs : onglet *Render*, case *Raytracing* (figure 3.12) ; onglet *Material*, rubrique *Settings*, case *Raytraced Transmission* (figure 3.13). Pour *Raytracing*, une seule phrase : « Sans elle, le verre ne réfracte pas ; le chapitre 4 explique ce réglage. » Une seule case cochée ne change rien.
3. L'ampoule du chapitre 2 est un volume plein : elle déforme comme une boule de cristal. La case *Thin Wall*, sous *Alpha*, en fait une paroi fine (figure 3.11, à droite).
4. *Roughness* `0.4` : un verre dépoli. Une *Base Color* teintée : un verre fumé, un feu arrière. L'IOR se cite seulement : 1,5 pour le verre, 1,58 pour le polycarbonate.
5. **Ailleurs :** un pare-brise ou une vitre de cabine, en paroi fine ; un feu arrière en polycarbonate, en volume plein, garde *Thin Wall* décochée.

**Ils font, en guidé (9 min),** d'après § 1 « Recette · Le verre de l'ampoule », étapes 1 à 5, jusqu'au retour par `/`.

**Pour ceux qui ont fini (défi ★, hors minutage) :** un verre dépoli (*Roughness* `0.4`) ou fumé (*Base Color* grise). Chacun garde celui qui convient à sa lampe.

**Quiz (1 min),** ensemble à l'écran : le deuxième quiz de la section 1, les deux interrupteurs.

**Point de contrôle :** en vue de dessous, la douille se voit à travers l'ampoule, sans déformation.

**Corrigé :** `Verre_Clair_corrige`, sur *Ampoule_A*. Le fichier de secours a sa case *Raytracing* décochée : cochez-la pour voir le corrigé à travers le verre.

**Pièges fréquents :**
- Une seule des deux cases cochée : rien ne change. Il faut les deux.
- La case *Raytracing* n'apparaît pas : le moteur est resté sur Cycles (point 6 du check-up).
- Un poste devient lent : décochez *Raytracing* le temps des autres séquences, puis recochez-la avant d'enregistrer en fin de séance.
- L'ampoule est une courbe avec un modificateur *Screw* : son onglet *Material* fonctionne comme celui d'un maillage.
- La douille introuvable au contrôle : la vue locale est restée active. `/`.

### 1:31 · Le Shader Editor : la matière en nœuds (15 min)

**Vous montrez (6 min),** d'après § 2 « Pourquoi pas de dépliage UV », « Le Shader Editor : la même matière, vue en nœuds » (figure 3.18), « Un nœud, des entrées, des sorties » (figure 3.19), « Se déplacer et agir dans le Shader Editor » et « Ajouter un nœud et le relier » (figures 3.20 et 3.21) :
1. Une phrase sur l'UV : « Un dépliage sert à poser une image à un endroit précis, comme un logo. Un grain, un brossé ou un lot de textures de bois s'appliquent en 3D, sans dépliage. »
2. L'onglet *Shading* : la vue 3D en *Material Preview* en haut, le Shader Editor en bas, l'éditeur de propriétés à droite.
3. *Bras_bas* sélectionné : deux nœuds, *Principled BSDF* relié à *Material Output*. « C'est `Alu_Naturel`, vue autrement. » Changez *Roughness* dans le nœud : l'onglet *Material* suit.
4. Les entrées à gauche, les sorties à droite ; le lien va de *BSDF* à *Surface*. La molette zoome, le clic molette déplace la vue, `Origine` cadre tout ; `G` déplace un nœud, `X` le supprime.
5. `Maj + A > Texture > Noise Texture`. Glissez sa sortie *Color* vers *Base Color* : le bras se couvre de nuages gris. Glissez le lien hors de *Base Color* : le bras redevient uni.

**Ils font, en guidé (9 min),** d'après § 2 « Recette · La matière en nœuds », étapes 1 à 5. Le nœud *Noise Texture* reste dans l'éditeur : il resservira.

**Point de contrôle :** chaque bras a montré des nuages gris, puis il est redevenu uni. Le nœud *Noise Texture* est toujours là.

**Corrigé :** pas de corrigé : le geste se vérifie à l'écran, et la figure 3.21 montre les nuages.

**Pièges fréquents :**
- Le Shader Editor est vide : l'objet actif n'a pas de matière, ou ce n'est pas le bon objet.
- Un raccourci sans effet : le pointeur n'était pas au-dessus du Shader Editor.
- Le lien est tombé sur une autre entrée : glissez-le hors de cette entrée et recommencez.
- Les reflets changent en passant dans l'espace *Shading* : sa vue 3D a ses propres réglages, dont l'image d'environnement.

### 1:46 · Finitions procédurales sans UV (25 min)

Trois nœuds, l'un après l'autre. Chaque étape suit le même rythme : vous montrez, puis ils font l'étape de la recette, avant la suivante. Ils suivent § 2 « Recette · L'aluminium brossé ». Ajoutez chaque nœud à la chaîne du paperboard.

**Étape 1 · Les coordonnées (démo 3 min, guidé 3 min),** d'après § 2 « Étape 1 · Les coordonnées : Texture Coordinate » (figure 3.22). Reliez de nouveau *Color* du *Noise* à *Base Color* : le motif est étiré sur la longueur du bras. `Maj + A > Input > Texture Coordinate` ; sa sortie *Object* vers l'entrée *Vector* du *Noise* : le motif garde la même taille partout. La lampe est petite : *Scale* du *Noise* passe de 5 à `1000`, environ un motif par millimètre. Ils font les étapes 1 et 2 de la recette.

**Étape 2 · Le relief (démo 3 min, guidé 4 min),** d'après § 2 « Étape 2 · Du motif au relief : Bump » (figure 3.23). Défaites le lien vers *Base Color*. `Maj + A > Displacement > Bump` : *Factor* du *Noise* vers *Height*, *Normal* du *Bump* vers *Normal* du Principled. Le motif devient un relief. *Strength* passe de 1 à `0.2` ; *Distance* garde sa valeur. « La force par défaut est trop forte pour un si petit objet : le relief scintille. » Ils font l'étape 3.

**Étape 3 · Le brossé (démo 2 min, guidé 4 min),** d'après § 2 « Étape 3 · Étirer pour brosser : Mapping » (figure 3.24). `Maj + A > Utilities > Vector > Mapping`, entre *Texture Coordinate* et *Noise*. *Scale* Z à `0.02` : le grain s'étire en fines rayures dans l'axe du bras. L'axe Z de chaque tige suit sa longueur, car leur rotation n'a pas été appliquée au chapitre 2 : c'est voulu. *Strength* du *Bump* à `0.15`. Renommez la matière `Alu_Brosse`. Une phrase, d'après l'encart « Ce qu'EEVEE simplifie » de la section 1 : *Anisotropic* ne marche que sous Cycles ; le brossé se simule ainsi. Ils font les étapes 4 et 5.

**Ailleurs :** une main courante en inox brossé (ferroviaire), une jante brossée (automobile), une garniture de cabine en aluminium brossé (aéronautique).

**Ils font, seuls (5 min),** d'après § 2 « Consignes · Le grain de l'ABS » : la même chaîne, sans *Mapping*, sur `ABS_Noir`. *Noise* *Scale* `1500`, *Bump* *Strength* `0.05`. Pour ceux qui ont fini : les articulations microbillées, *Noise* *Scale* `2000`, *Strength* `0.03`, *Roughness* `0.5`.

**Quiz (1 min),** ensemble à l'écran : le premier quiz de la section 2, la sortie *Object*.

**Point de contrôle :** sur chaque tige, les rayures suivent la longueur du bras. Le grain de l'interrupteur, de ses crans et de la grille est régulier.

**Corrigé :** dans *Corrigé coloris A*, `Alu_Brosse_corrige` et `ABS_Noir_corrige`, avec leurs chaînes de nœuds.

**Pièges fréquents :**
- Rien ne se voit : *Scale* du *Noise* est resté trop faible, un seul motif couvre la pièce.
- Un relief qui scintille : *Strength* est trop forte. Divisez-la par deux.
- Des rayures en travers : l'axe étiré dans *Mapping* n'est pas le bon. Essayez X ou Y.
- Le *Mapping* est posé, mais rien ne s'étire : la sortie *Object* va encore directement au *Noise*.
- La matière n'a pas été renommée `Alu_Brosse` : faites-le maintenant, sinon l'Append de 3:12 donnera `Alu_Naturel.001`.

### 2:11 · Projection triplanaire d'images (21 min)

**Vous montrez (8 min),** d'après § 2 « Une image projetée sur trois axes : Box » (figures 3.25 à 3.28), « Les images de données : Non-Color » (figure 3.29) et « L'échelle appliquée, condition de la projection » (figure 3.30), sur `PRC02_ch3_finitions_triplanaires.blend`, qui s'ouvre sur l'espace *Shading*, l'accoudoir sélectionné :
1. L'accoudoir n'a pas de dépliage UV. Sa matière a son Principled réglé et un nœud *Image Texture* déjà chargé, `grain_cuir`, non relié. Reliez l'image à *Base Color*, sans coordonnées : rien de lisible. Avec *Texture Coordinate* (*Object*) et la projection *Flat* : l'image coule sur les flancs.
2. Le menu de projection, *Box* : l'image est projetée sur trois axes, d'où le nom de projection triplanaire. Les raccords se voient à 45° ; *Blend* `0.3` les fond (figure 3.28).
3. *Color Space* sur *Non-Color* : une image de relief est une donnée, pas une couleur. Une image de couleur, comme celle du carbone, reste en *sRGB*.
4. La chaîne complète (figure 3.27) : *Mapping* *Scale* `25`, l'image vers *Height* d'un *Bump* (*Strength* `0.3`), puis *Normal*. Retirez le lien vers *Base Color*.
5. Le piège : l'accoudoir jumeau, dont l'échelle X de 2 n'est pas appliquée. Son grain s'étire. `Ctrl + A > Scale` le remet d'aplomb : « C'est le patient 2 de la clinique. »
6. **Ailleurs :** un accoudoir en cuir grainé (aéronautique), une coque de rétroviseur grainée (automobile), un marchepied en tôle larmée (ferroviaire). Le fichier propose ces pièces.

**Ils font, en guidé (9 min),** d'après § 2 « Recette · La peinture structurée du socle », sur leur lampe :
1. Un clic sur le compteur de `Peinture_Vert`, sur le socle ; la copie est renommée `Structure_Vert`. « Même teinte, autre finition : c'est une décision CMF. »
2. *Coat Weight* `0`, *Roughness* `0.6`.
3. `Maj + A > Texture > Image Texture`, *Open*, `textures_cmf/grain_structure.png` ; *Non-Color* ; *Box*, *Blend* `0.25`.
4. *Texture Coordinate* (*Object*), *Mapping* (*Scale* `50` sur les trois axes), l'image, *Bump* (*Strength* `0.2`), puis *Normal*.

**Ils font, seuls (3 min),** d'après § 2 « Consignes · Sans raccord » : le tour du socle, *Blend* et *Scale* réglés jusqu'à ne plus voir de raccord ; `Ctrl + S`. *Pack Resources* attend la fin du lot PBR : un seul geste pour toutes les images.

**Quiz (1 min),** ensemble à l'écran : le deuxième quiz de la section 2, le grain étiré.

**Point de contrôle :** le socle est grainé, la tête reste laquée et lisse ; aucun raccord au tour du socle.

**Corrigé :** `Structure_Vert_corrige`, sur *Socle_A*. Pour la démo : la collection masquée *Corrigé* du fichier des finitions.

**Pièges fréquents :**
- Le grain apparaît aussi sur la tête : la laque n'a pas été rendue indépendante avant la modification. `Ctrl + Z`, puis un clic sur le compteur.
- Un grain trop contrasté, ou un peu coloré : *Color Space* est resté en *sRGB*.
- Le grain du socle est une image de hauteur, en niveaux de gris : elle passe par un *Bump*. Une carte de normales passe par un *Normal Map* : c'est la séquence suivante, sans dépliage UV elle aussi.
- L'image introuvable : l'archive n'a pas été décompressée (clic droit > *Extraire tout*), ou le dossier `textures_cmf` n'est pas à côté du fichier de travail.

### 2:32 · Un lot de textures PBR sur le socle (12 min)

**Vous montrez le téléchargement (2 min),** d'après § 2 « Un lot de textures PBR » et « Où trouver des lots : Poly Haven », dans votre navigateur :
1. « Un designer CMF part le plus souvent d'un échantillon numérisé : un lot de textures PBR. Une image par réglage du Principled : la couleur, la rugosité, les normales, la hauteur. »
2. La page `https://polyhaven.com/a/walnut_veneer_02` : la licence CC0 et la taille réelle de l'échantillon, « 1m wide ». « CC0 : tout usage est permis, y compris commercial, sans attribution obligatoire. »
3. La définition, en haut à droite : passez de 4K à 1K, « assez pour un objet de 18 cm ». La flèche à droite de *Download* liste les cartes : *Diffuse*, *Rough*, *Normal (GL)*, *Displacement*, chacune en EXR, JPG ou PNG. Téléchargez une carte en JPG.
4. « Le dossier `textures_pbr` de l'application contient déjà trois lots : le noyer, un béton lisse et un palissandre verni. »

**Vous montrez la chaîne (3 min),** d'après § 2 « Toutes les cartes en projection Box », « La carte de normales : Normal Map » (figure 3.31), « Garder une matière : le bouclier » (figure 3.32) et la recette (figures 3.33 à 3.35), sur votre copie de la lampe, dans l'espace *Shading*, le socle sélectionné :
1. Le bouclier de `Structure_Vert` : « Une matière qu'aucune pièce ne porte disparaît à l'enregistrement. Le bouclier la garde, pour le coloris B. » Puis le bouton de copie, juste à droite : `Bois_Noyer`.
2. Dans le nœud *Image Texture*, le bouton de dossier : la carte `diff`, en *sRGB*, vers *Base Color* ; le *Bump* supprimé ; *Scale* du *Mapping* à `2`.
3. `Maj + D` sur l'image : une copie, déjà en *Box*. Le lien du *Mapping*, la carte `rough` en *Non-Color*, vers *Roughness*.
4. Encore `Maj + D` : la carte `nor_gl`, en *Non-Color*. `Maj + A > Displacement > Normal Map`, à côté de *Bump* : « Une carte de normales n'est pas une hauteur. Elle passe par *Normal Map*, en projection *Box*, sans dépliage UV. » Faites tourner l'image d'environnement : les reflets suivent le fil du bois.
5. **Ailleurs :** une tablette en placage de bois (ferroviaire, aviation d'affaires), un dessus de console (automobile).

**Ils font, en guidé (5 min),** d'après § 2 « Recette · Un lot PBR sur le socle », étapes 1 à 4 : le bouclier et la copie `Bois_Noyer` ; la couleur ; la rugosité ; les normales et le *Normal Map*.

**Ils font, seuls (1 min),** d'après § 2 « Consignes · Votre lot, puis empaqueter » : *File > External Data > Pack Resources* (figure 3.38), puis `Ctrl + S`. Le choix d'un autre lot, béton ou palissandre, se fait pendant l'atelier ou après la séance.

**Quiz (1 min),** ensemble à l'écran : le troisième quiz de la section 2, le nœud *Normal Map*.

**Point de contrôle :** le socle porte le veinage du noyer, net et sans raccord ; `Structure_Vert` reste dans la liste des matières, son bouclier activé. Après *Pack Resources*, le fichier ne dépend plus des dossiers `textures_cmf` et `textures_pbr`.

**Corrigé :** `Bois_Noyer_corrige`, sur *Socle_PBR*, dans la collection masquée *Corrigé socle PBR*, devant la lampe du coloris A. La collection *Corrigé coloris A* garde le socle en peinture structurée : c'est l'état de 2:11.

**Pièges fréquents :**
- Le socle devient bleu violet : la carte `nor_gl` est reliée à *Base Color*. Elle va dans le *Normal Map*.
- Des creux en bosse : la carte `nor_dx` a été téléchargée au lieu de `nor_gl`.
- Un bois délavé : la carte `diff` est en *Non-Color*. Un socle trop brillant ou trop mat : la carte `rough` est restée en *sRGB*.
- Une carte décalée des autres : son entrée *Vector* n'est pas reliée au *Mapping*. `Maj + D` ne copie pas ce lien.
- Le bouclier oublié : `Structure_Vert` disparaîtra à la prochaine ouverture. Activez-le maintenant ; sinon, le coloris B reprendra `Structure_Vert_corrige`.
- Un apprenant qui a activé *Node Wrangler* et charge le lot par `Ctrl + Maj + T` (figure 3.37) : sortie *Object* au lieu de *UV*, chaque image en *Box*, et pas de carte `disp`.

### 2:44 · Pause (10 min)

### 2:54 · Ranger ses matières en actifs (18 min)

**Vous montrez (6 min),** d'après § 3 « Pourquoi une bibliothèque » (figure 3.39), « Faire d'une matière un actif » (figure 3.40), « Le sélecteur de type d'éditeur » (figures 3.41 et 3.42), « Ranger en catalogues » (figure 3.43), « Décrire un actif » (figure 3.44) et « Appliquer un actif par glisser-déposer » (figure 3.45) :
1. Une phrase : « Une équipe CMF réutilise ses matières d'un projet à l'autre, au lieu de les recréer. » La figure 3.39 montre le nuancier de la classe.
2. Clic droit sur le nom de `Alu_Brosse`, dans l'onglet *Material* : *Mark as Asset*. Une vignette se calcule.
3. La zone du bas, celle du LISEZ-MOI ou de la Timeline : le sélecteur de type d'éditeur, colonne *Data*, *Asset Browser*. Agrandissez la zone. Bibliothèque : *Current File*.
4. Le bouton `+` de la liste des catalogues : *Métaux*, renommé d'un double-clic. Glissez la vignette dessus.
5. La barre latérale (`N`) : une description, par exemple « Aluminium brossé. Bras de lampe ; convient aussi à une main courante ou à une jante. » Les apprenants le feront en défi ★.
6. La douille est encore nue : glissez sur elle la vignette de `Chrome`. Blender affiche « Drop Chrome on Douille ». « Un essai : la douille recevra mieux tout à l'heure. »
7. `Ctrl + S`. L'encart *IMPORTANT* : les catalogues partent dans un fichier `blender_assets.cats.txt`, à côté du `.blend`. « Copiez toujours les deux ensemble. »

**Ils font, en guidé (7 min),** d'après § 3 « Recette · Ranger les matières de la lampe », étapes 1 à 5 : `Alu_Brosse`, `Chrome` et `Peinture_Vert` en actifs ; trois catalogues, *Métaux*, *Plastiques et peintures* et *Verres* ; le rangement ; `Chrome` glissé sur la douille.

**Ils font, seuls (4 min),** d'après § 3 « Consignes · Jusqu'à la dernière matière » : `ABS_Noir`, `PVC_Mat_Noir`, `Verre_Clair` et la matière du socle (`Bois_Noyer`…) marqués et rangés, le socle dans un quatrième catalogue, *Bois et minéraux* ; `Ctrl + S`, puis un coup d'œil dans l'Explorateur Windows : `blender_assets.cats.txt` est apparu. Décrire un actif devient un défi ★.

**Quiz (1 min),** ensemble à l'écran : le troisième quiz de la section 3, *Current File*.

**Point de contrôle :** dans *Current File*, chaque matière de la lampe est rangée dans un catalogue ; *Métaux* montre l'aluminium brossé et le chrome. La douille est chromée.

**Corrigé :** la bibliothèque CMF elle-même, avec ses actifs, ses catalogues, ses descriptions et ses étiquettes. Les matières `_corrige` du fichier de secours ne sont pas des actifs.

**Pièges fréquents :**
- *Mark as Asset* lancé depuis le menu *Object* marque la pièce, pas sa matière. `Ctrl + Z`.
- Une vignette noire : relancez son calcul avec *Generate Preview*, dans la barre latérale.
- La vignette lâchée à côté de la pièce ne fait rien : relâchez le bouton avec le pointeur sur la pièce.
- Une matière introuvable dans les catalogues : elle est dans *Unassigned*, qui regroupe les actifs non rangés.
- Les catalogues ont disparu après une copie du fichier : `blender_assets.cats.txt` est resté dans l'ancien dossier. Les actifs, eux, sont toujours là. Gardez aussi la lampe hors du dossier `PRC02_bibliotheque_CMF`, qui a son propre fichier de catalogues.

### 3:12 · Réutiliser : récupérer une matière par Append (12 min)

**Vous montrez (5 min),** d'après § 3 « Récupérer une matière : File > Append » (figure 3.46) et « Un fichier .blend s'ouvre comme un dossier » (figure 3.47) :
1. Le nuancier de 0:35 : « La gamme CMF de la classe. » Revenez à la lampe par *File > Open Recent*.
2. Le menu *File* : *Link…* et *Append…*. *File > Append*, le dossier `PRC02_bibliotheque_CMF`, puis double-clic sur `PRC02_ch3_nuancier_cmf.blend` : il s'ouvre comme un dossier, avec *Collection*, *Material*, *Object*… Dossier *Material*, `Alu_Naturel`, bouton *Append*.
3. La matière est dans la liste des matières, modifiable, avec ses images. Elle garde son statut d'actif : sa vignette apparaît dans *Current File*. Glissez-la sur la douille : elle remplace l'essai en chrome.
4. *Link*, en une phrase : « Link lie la matière en lecture seule ; on l'utilise pour partager une bibliothèque d'équipe. » Le fichier qui part au chapitre 4 n'en contient aucune.
5. « Le chapitre 4 reprendra ce geste, dans le dossier *Collection*, pour amener la lampe dans son studio. »
6. En option (1 min), d'après § 3 « Option : déclarer une bibliothèque » et « Option : la section Asset Libraries » (figures 3.48 à 3.50) : sur votre poste, la bibliothèque déclarée dans *Edit > Preferences > Asset Libraries* apparaît dans le menu des bibliothèques de l'Asset Browser. Le menu *Import Settings* propose *Follow Asset or Preferences*, *Link*, *Append* et *Pack*. Une bibliothèque déclarée importe en *Pack* par défaut : pour une matière à modifier, on préfère *Append*. « C'est l'usage d'une équipe. Aujourd'hui, nous ne touchons pas aux préférences des postes. »
7. **Ailleurs :** la gamme de teintes d'un constructeur automobile, la charte des intérieurs d'une compagnie aérienne, les matières homologuées feu et fumée d'un aménagement ferroviaire.

**Ils font, en guidé (6 min),** d'après § 3 « Recette · L'aluminium de la douille », étapes 1 à 4 : *File > Append* ; `Alu_Naturel` sur la douille, par sa vignette ou par la liste ; l'actif rangé dans *Métaux* ; `Ctrl + S`.

**Quiz (1 min),** ensemble à l'écran : le premier quiz de la section 3, le chemin de *File > Append*.

**Point de contrôle :** la douille porte `Alu_Naturel`, et ses réglages ne sont pas grisés. Aucune matière liée ne reste dans le fichier.

**Corrigé :** `Alu_Naturel_corrige`, sur *Douille_A*.

**Pièges fréquents :**
- Pas de dossier *Material* : l'apprenant est resté dans le dossier `PRC02_bibliotheque_CMF`. Double-clic sur le fichier `.blend`.
- La matière s'appelle `Alu_Naturel.001` : l'aluminium des bras n'a pas été renommé `Alu_Brosse` à 1:46. Renommez les deux.
- Des réglages grisés : la matière a été liée par *File > Link*. `Ctrl + Z`, puis *File > Append*.
- Le dossier introuvable : l'archive n'a pas été décompressée (clic droit > *Extraire tout*).

### 3:24 · Atelier · Le second coloris (20 min)

La fiche complète est plus bas. Le lancement dure 2 minutes, l'autonomie 16 minutes et la revue 2 minutes.

### 3:44 · Tour des postes, bilan et passerelle (6 min)

- **Tour des postes (2 min) :** les écrans en *Material Preview*, les deux coloris côte à côte, chaque socle avec son lot. Tout le monde fait le tour.
- **Une question (1 min) :** « Pourquoi l'ampoule ne montrait-elle que l'image d'environnement ? »
- **Quiz (1 min),** ensemble à l'écran : le deuxième quiz de la section 3, *Link* face à *Append*. Puis : « Append ou Link, pour envoyer votre fichier à un client ? »
- **Passerelle (2 min) :** « Au chapitre 4, la lampe sort de la vue de travail. Vous l'amènerez dans un studio par Append, vous l'éclairerez, vous la cadrerez et vous en tirerez des visuels. » Vérifiez que chacun a enregistré `lampe_habillage_v002.blend`, images empaquetées, avec `blender_assets.cats.txt` à côté.
- **Pour aller plus loin :** les défis de « Pour ceux qui avancent vite », et le défi facultatif « Matières procédurales ».

<!-- pagebreak -->

## Atelier · Le second coloris

**Fichier :** `lampe_habillage_v001.blend`, enregistré sous `lampe_habillage_v002.blend` · **Durée :** 20 min · **De 3:24 à 3:44**

**Situation :** « La revue de design demande une seconde proposition de couleurs : le coloris B. »

**Objectif :** décliner la lampe dans un second coloris, sans toucher au premier.

**Pourquoi il fonctionne :**
- Aucune notion nouvelle : l'atelier réinvestit *Duplicate Collection* (chapitre 1), le compteur d'utilisateurs, les réglages du Principled, les nœuds et la bibliothèque.
- Le piège est le vrai sujet : la copie partage les matières de l'original. Rendre une matière indépendante avant de la changer, c'est l'idée du jour, en situation.
- Le coloris est un vrai livrable CMF. Le chapitre 4 peut reprendre `Lampe_coloris_B` pour décliner ses visuels.

**Le socle, en 5 étapes :**

| Étape | Ce qu'il faut faire | Gestes réinvestis |
|---|---|---|
| 1 | Clic droit sur *Lampe* > *Duplicate Collection* (figure 3.51) ; la copie renommée `Lampe_coloris_B` | *Duplicate Collection* (chapitre 1) |
| 2 | Clic droit sur `Lampe_coloris_B` > *Select Objects*, puis `G X = 750mm` | Saisie avec unité (chapitre 1) |
| 3 | Sur chaque pièce à changer : un clic sur le compteur de sa matière, puis un nouveau nom (`Laque_Blanche`…) | Le compteur d'utilisateurs (section 1, initiation) |
| 4 | Au moins quatre matières changées, dont une peinture et un métal. Pour le socle : `Structure_Vert`, gardée par son bouclier, copiée en `Structure_Blanche`, ou un autre lot PBR | *Base Color*, *Metallic*, *Roughness*, *Coat*, le verre ; les nœuds suivent la copie ; le bouton de copie et les cartes d'un lot (section 2) |
| 5 | Une teinte du coloris B changée : le coloris A ne bouge pas. *File > Save As*, bouton `+` : `lampe_habillage_v002.blend` | L'enregistrement incrémental (initiation) |

**Déroulé :**
1. **Lancement (2 min).** Faites les étapes 1 et 2 à l'écran. « Avec moins de 750 mm, le câble de la copie traverserait le socle de l'original. Attention : la copie partage les matières de l'original. » À qui manque d'idée, proposez le coloris B du corrigé : une version claire pour un bureau d'études, avec structure et laque blanches, bras anodisés noirs, articulations et douille en laiton, verre dépoli. Lancez le minuteur.
2. **Autonomie (16 min).** Chacun compose son coloris B, pièce par pièce, d'après § 3 « Consignes · Le coloris B, par paliers ». La collection *Lampe* garde le coloris A et son nom : le chapitre 4 l'importe sous ce nom. Passez voir chaque poste au moins une fois. Annoncez les 5 dernières minutes.
3. **Revue (2 min).** Chacun change une teinte du coloris B, vérifie que le coloris A ne bouge pas, puis enregistre sous `lampe_habillage_v002.blend` avec le bouton `+`.

**Paliers :**
- **★ :** toutes les pièces du coloris B suivent une gamme cohérente. Ses nouvelles matières sont des actifs, rangés dans les catalogues. Une matière au moins vient du nuancier par *File > Append*, par exemple `Laiton`.
- **★★ :** un coloris C « premium » : laiton, carbone en projection triplanaire, verre fumé. Le nuancier propose `Carbone_Serge` et `Verre_Fume`.

**Points d'observation :**
- Les deux lampes changent ensemble : la matière est encore partagée. Un clic sur son compteur la rend indépendante. *Duplicate Collection* copie les objets et les maillages, mais pas les matières.
- Une copie de matière garde ses nœuds : l'aluminium brossé, rendu indépendant puis teinté en noir, reste brossé. Faites-le remarquer : c'est la section 2 réinvestie.
- Un verre créé avec *New*, au lieu d'une copie de `Verre_Clair`, ne montre que l'image d'environnement : il faut recocher *Raytraced Transmission* et *Thin Wall*.
- `ABS_Noir` et `PVC_Mat_Noir` peuvent rester partagées : seule une matière que l'on change doit être rendue indépendante.
- Le socle du coloris B porte d'abord le lot PBR du coloris A : la peinture structurée revient par la liste des matières, grâce à son bouclier. Sans bouclier, elle a disparu à la réouverture : reprenez `Structure_Vert_corrige` du fichier de secours, ou un autre lot.
- La collection *Lampe* renommée par erreur : redonnez-lui son nom, le chapitre 4 la cherche.

**Corrigé :** la collection masquée *Corrigé coloris B* de `PRC02_ch3_lampe_a_habiller.blend`, objets suffixés `_B` : `Structure_Blanche_corrige`, `Laque_Blanche_corrige`, `Alu_Anodise_Noir_corrige` (brossé), `Laiton_corrige` sur les articulations et la douille, `Verre_Depoli_corrige`. `ABS_Noir_corrige` et `PVC_Mat_Noir_corrige` y restent partagées avec le coloris A. La lampe habillée, `PRC02_ch3_lampe_habillage.zip`, montre le même résultat sous les vrais noms (figure 3.52) ; son coloris A garde le socle en peinture structurée.

**Ce que le chapitre 4 attend :** `lampe_habillage_v002.blend`, avec la collection *Lampe* en coloris A, son socle en lot PBR, et `Lampe_coloris_B` ; des images empaquetées, cartes du lot comprises, et aucune matière liée ; le verre avec *Raytraced Transmission* et *Thin Wall* ; EEVEE, case *Raytracing* cochée. Un atelier inachevé ne bloque personne : le chapitre 4 a son propre fichier de secours, `PRC02_ch4_lampe_en_studio.blend`, tiré de la lampe habillée.

## Le défi facultatif · Matières procédurales

Le Défi 2 de la rubrique « Pour aller plus loin » de la barre latérale, qui prolonge ce chapitre, hors programme de base et hors minutage : environ 3 heures, en deux paliers et sept étapes. Vous n'en faites aucune démonstration.

**À qui :** aux apprenants qui parcourent vite le contenu principal, et à ceux qui maîtrisent déjà ces sujets. En cas de doute, les trois quiz de la section 2 servent de test d'entrée.

**Quand le proposer :**
- annoncez-le en une phrase à l'ouverture, sans plus ;
- pendant l'atelier, une fois le socle du coloris B fait et `lampe_habillage_v002.blend` enregistré, à la place des paliers ★ et ★★ ;
- après la séance : chacun reprend à l'étape où il s'est arrêté.

Son introduction permet aussi de le faire à la place de parties de base. L'apprenant reprend alors le chapitre 4 avec son fichier de secours, avec la lampe habillée ou avec sa propre lampe, gardée dans la collection *Lampe* de `lampe_habillage_v002.blend`.

**Le fichier :** `PRC02_ch3_defi_procedural.blend`, proposé en tête du défi et enregistré sous `defi_procedural_v001.blend`. Il s'ouvre dans l'espace *Shading*, sur les rangées des étapes 1 et 2 ; les autres rangées et la copie de la lampe, `Lampe_defi`, sont masquées. Sa case *Raytracing* est décochée : l'ampoule de `Lampe_defi` ne montre que l'environnement, c'est voulu.

| Palier | Étape | Durée | Ce que l'on apprend |
|---|---|---|---|
| | Avant de commencer | 5 min | L'aperçu d'un nœud, `Ctrl + Maj + clic` (figure D2.3) |
| 1 | 1 · Lire les textures de bruit | 20 min | *Noise*, *Voronoi*, *Wave*, *Gabor* |
| 1 | 2 · Remapper les valeurs | 20 min | *Color Ramp*, *Map Range*, *Math* |
| 1 | 3 · Masques et couches | 20 min | *Mix Color*, *Mix*, *Separate XYZ* |
| 1 | 4 · Le relief procédural | 15 min | Deux *Bump* chaînés, *Coat Normal* |
| 2 | 5 · L'usure | 30 min | Les arêtes par la normale, les creux par *Ambient Occlusion*, les rayures, les traces de doigts |
| 2 | 6 · Les motifs | 40 min | Tôle perforée (*Alpha*), cuir, tissu ; en ★, moletage et carbone |
| 2 | 7 · Les groupes de nœuds | 25 min | `Ctrl + G` et les paramètres exposés ; le défi final sur `Lampe_defi` |

Chaque étape suit le même ordre : un exemple terminé, une recette guidée, un petit défi. Neuf quiz vérifient les acquis : les quiz 1 à 5 closent le palier 1, les quiz 6 à 9 le palier 2.

**Corrigé :** la collection masquée « Corrigé défi procédural », avec une sous-collection par étape, de « Corrigé étape 1 » à « Corrigé étape 7 » ; objets et matières suffixés `_corrige`. « Corrigé étape 7 » contient aussi `Lampe_defi_corrige` et les groupes `PRC_Usure_Bords_corrige` et `PRC_Tole_Perforee_corrige`, visibles dans `Maj + A > Group`. Les pièces `…_Exemple_…` restent visibles : ce sont des exemples à observer, pas des corrigés.

**L'accompagner sans y passer la séance :**
- le groupe passe d'abord : une visite courte, au même rythme que les autres postes ;
- demandez l'aperçu (`Ctrl + Maj + clic`) du nœud qui pose problème : il montre où la chaîne casse ;
- renvoyez au corrigé de l'étape et au quiz qui la clôt, plutôt que de dépanner nœud par nœud ;
- vérifiez que la lampe du chapitre 4 est enregistrée à part : le défi a son propre fichier.

**Pièges principaux :**
- **Les temps de compilation.** *Material Preview* calcule chaque matière visible : plus il y en a, plus l'affichage ralentit, et chaque collection rouverte demande un temps de calcul. Une seule collection visible à la fois, celle de l'étape en cours, comme le dit le LISEZ-MOI. Ce temps est à mesurer avant la séance sur le poste le plus modeste.
- Une pièce grise et sans reflet : l'aperçu n'a pas été annulé. `Ctrl + Maj + clic` sur le *Principled BSDF*.
- Une plaquette presque uniforme : *Scale* est resté à 5. Avec les coordonnées *Object*, `100` donne un motif tous les 10 mm environ.
- Le blanc de l'aperçu paraît gris clair : c'est la transformation de vue *AgX*. On lit les contrastes, pas les valeurs.
- Un nœud sans effet : *Pointiness*, le nœud *Bevel*, *Random Per Island* et *Anisotropic* ne marchent que sous Cycles. Les recettes les remplacent.

## Gérer l'hétérogénéité

### Le parcours « première fois »

- Les binômes et les copilotes de l'initiation restent en place.
- La section 1 ne montre aucun nœud : rassurez ceux qu'inquiète le Shader Editor, il n'arrive qu'à 1:31, à partir d'une matière déjà connue.
- Le LISEZ-MOI de la lampe reprend chaque partie par paliers. Les valeurs restent indicatives : chacun compose sa gamme, seuls les noms comptent pour la suite.
- Le socle de chaque séquence suffit : il couvre tous les points du programme.
- À chaque point de contrôle, passez d'abord par les postes des débutants.
- **Un modèle du chapitre 2 abîmé ou absent :** le fichier de secours dès 0:00, enregistré sous `lampe_habillage_v001.blend`.
- **Un apprenant très en retard** reprend avec le groupe sur la pièce de l'exercice en cours : chaque exercice porte sur ses propres pièces, les bras, le socle, la douille. Il finit les pièces sautées après la séance, avec la collection *Corrigé coloris A*.

### Pour ceux qui avancent vite

- Les paliers ★ et ★★ de l'atelier.
- **Le lot PBR :** un autre lot sur le socle, béton ou palissandre ; la carte de hauteur `disp` dans un *Bump* chaîné au *Normal Map* (★) ; un lot chargé d'un coup par `Ctrl + Maj + T` de *Node Wrangler*, puis repassé en *Box* (figure 3.37).
- **Les défis ★ de l'application :** le verre dépoli et le verre fumé ; la description d'un actif ; l'intérieur blanc de la tête, par un second emplacement et le *Material Offset* du *Solidify* (figures 3.16 et 3.17) ; un voyant lumineux par *Emission* (figure 3.15) ; *File > Link* d'une matière du nuancier, qui arrive grisée (figure 3.53), puis `Ctrl + Z` ; `Ctrl + L > Link Materials`.
- **La bibliothèque déclarée (★) :** dans *Edit > Preferences > Asset Libraries*, puis une vignette glissée et le menu *Import Method*. Elle s'enregistre dans les préférences du poste : prévenez le gestionnaire si la salle est partagée.
- **Les articulations microbillées (★★ dans le LISEZ-MOI) :** la consigne de 1:46.
- **Automobile (★★) :** la peinture métallisée du nuancier, `Peinture_Metallisee_Bleu`, décortiquée dans le Shader Editor, puis reproduite.
- **Aéronautique (★★) :** l'accoudoir en cuir grainé et le panneau carbone, sur le fichier des finitions triplanaires, d'après son LISEZ-MOI.
- **Ferroviaire (★★) :** le marchepied en tôle larmée, puis la rangée de sièges de l'initiation, `PRC02_init_rangee_sieges.blend`, habillée avec la bibliothèque.
- **Sa propre bibliothèque (★★) :** son dossier de travail déclaré comme bibliothèque, puis un objet habillé dans un nouveau fichier.
- Le défi facultatif « Matières procédurales », et le rôle de copilote, comme à l'initiation.

## Animer : ce qui change au chapitre 3

Les conseils de l'initiation restent valables : « Regardez, puis à vous », les touches dites à voix haute, les post-it vert et rose, la règle des 3 minutes, la souris qu'on ne prend pas. Ce chapitre en ajoute six :
1. **Annoncez les attentes.** La première bascule en *Material Preview* fige l'écran quelques secondes, le temps que Blender prépare ses calculs de matières. Dites-le avant : sinon, les apprenants cliquent partout.
2. **Un nœud à la fois, dit à voix haute.** « La sortie *Factor* du *Noise* va dans *Height* du *Bump*. » Partez toujours de la matière connue, et complétez la chaîne du paperboard à chaque nœud ajouté.
3. **Jugez aux reflets.** Un métal, une laque ou un brossé se jugent aux reflets, pas à la teinte. Faites tourner l'image d'environnement, ou la vue, avant de valider.
4. **Le compteur avant la modification.** Posez la question à chaque changement de finition ou de coloris : « Cette matière est-elle partagée ? » Elle revient au socle structuré et dans tout l'atelier. Au lot PBR, une seconde question : « Cette matière doit-elle rester dans le fichier ? » Le bouclier la garde.
5. **Les valeurs sont des points de départ.** Teintes, *Roughness*, *Scale* et *Strength* se règlent à l'œil. Seuls les noms des matières et de la collection *Lampe* comptent pour le chapitre 4.
6. **Parlez métier CMF :** teinte, matière, finition, gamme, coloris. « Même teinte, autre finition » est une décision de designer, pas un réglage technique.

## Si vous prenez du retard

Raccourcissez dans cet ordre :

| Ordre | Ce que l'on coupe | Ce que l'on garde |
|---|---|---|
| D'abord | *Coat* : démo seule, sans essai | Le réglage montré, que l'atelier peut réinvestir |
| D'abord | L'option de la bibliothèque déclarée | *Mark as Asset* et les catalogues |
| D'abord | La démo du téléchargement sur Poly Haven : projetez le § 2 « Où trouver des lots : Poly Haven » | Le lot du dossier `textures_pbr`, posé sur le socle |
| Ensuite | L'autonomie du procédural, le grain de l'ABS | La chaîne du brossé, en trois étapes |
| Ensuite | L'autonomie de la projection, réduite à l'enregistrement | La projection *Box* sur le socle |
| Ensuite | Le lot PBR réduit à deux cartes, la couleur et les normales ; la rugosité après la séance | Le *Normal Map* en projection *Box*, puis *Pack Resources* |
| En dernier | L'atelier réduit à son socle, en 10 minutes ; la suite après la séance, avec le LISEZ-MOI et *Corrigé coloris B* | `Lampe_coloris_B` et l'enregistrement sous `lampe_habillage_v002.blend` |

**Ce qui ne saute jamais,** car le chapitre 4 s'en sert : *Material Preview* et le Principled (*Metallic*, *Roughness*) ; le verre et ses deux interrupteurs ; le Shader Editor et la chaîne du brossé ; la projection *Box* sur le socle ; le lot PBR et son *Normal Map* ; *Mark as Asset* et *File > Append* ; l'enregistrement final, images empaquetées.

## Si vous êtes en avance

- **L'atelier s'enrichit :** les paliers ★, puis le coloris C du palier ★★.
- **La revue s'allonge :** chacun présente son coloris B en une minute, avec sa gamme et une décision CMF.
- **Les finitions triplanaires :** l'accoudoir, puis la coque (★), puis le marchepied et le carbone (★★), d'après le LISEZ-MOI du fichier.
- **Le socle, trois lots :** chacun essaie le béton et le palissandre, puis garde le lot de son coloris A ; montrez la figure 3.35.
- **Le défi facultatif,** pour ceux qui le veulent, à partir de l'étape 1.

---

Les fichiers du chapitre se reconstruisent avec les scripts de `tool/exercices_ch3/` : `construire.ps1` pour la lampe, la bibliothèque et les finitions (option `-Textures` pour les images), `textures_pbr.py` pour le zip des lots de Poly Haven (cartes rangées hors du dépôt, dans `tool/exercices_ch3/textures_pbr/`), `build_defi.py` pour le défi facultatif. Les textes LISEZ-MOI se lisent dans les scripts `build_*.py`. Ce document se convertit en PDF avec `tool/deroule_initiation/export_pdf.ps1 -Source _resources\PRC02-deroule-chap3.md`.
