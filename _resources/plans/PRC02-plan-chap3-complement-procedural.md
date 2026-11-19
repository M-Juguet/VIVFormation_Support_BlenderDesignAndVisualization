# Chapitre 3 · Complément · Défi facultatif : matières procédurales : plan

PRC02 · Design & visualisation temps réel avec Blender · Blender 5.2 LTS, interface en anglais
Demi-journée 5 et travail personnel · Complément facultatif, hors programme de base · Plan rédigé et validé le 18 novembre 2026, précisions du formateur intégrées ; produit le 19 novembre 2026 (voir « Décisions de production »)

## En bref

- **Un complément facultatif, hors programme de base :** le défi n'est pas prévu dans la formation initiale. Il ajoute des connaissances utiles qu'elle ne couvre pas. L'écran Programme, le titre de la section et son introduction le signalent comme facultatif.
- **Pour qui :** deux profils d'apprenants (précision du formateur) :
  - ceux qui parcourent vite les contenus de base, parce qu'ils sont à l'aise ;
  - ceux qui maîtrisent déjà ces sujets en début de formation.

  Le chapitre 3 couvre les cas courants : des matières simples, une finition procédurale (grain, brossé) et des images projetées sans dépliage UV. Ce complément apprend à **construire soi-même** des matières procédurales plus riches.
- **Forme (décision du 18 novembre 2026) :** une section 4 du chapitre 3 dans l'application, « Défi facultatif · Matières procédurales ». Elle a sa propre ancre, `ch3_sec4_title`, et un quatrième point au programme, marqué facultatif. Elle se lit en autonomie : recettes, captures et quiz, avec les modules existants.
- **Moment (précision du formateur) :** au choix de l'apprenant.
  - **À la suite des parties de base,** s'il lui reste du temps : en séance, puis après la séance si besoin.
  - **À la place des parties de base,** pour l'apprenant qui veut un complément et des défis plus poussés. Il reprend alors le chapitre 4 par l'une des trois voies décrites dans « Quand et comment ».
- **Périmètre (décision du 18 novembre 2026) :** 7 étapes en 2 paliers, pour environ 3 heures de travail.
  - Palier 1 : lire les bruits, remapper, masquer, mettre en relief.
  - Palier 2 : l'usure, les motifs, les groupes de nœuds.
- **Supports (décision du 18 novembre 2026) :** un fichier dédié, avec des pièces des trois secteurs. Le défi final applique les techniques à une copie de la lampe du fil rouge.
- **Le rôle du formateur :** il ne fait aucune démonstration. Il annonce la section en une phrase, passe voir les apprenants concernés et les renvoie aux corrigés. Le minutage du chapitre 3 ne change pas.
- **Affichage :** tout se fait en *Material Preview*, avec l'image *studio*, comme le chapitre 3. Chaque recette a été rendue sous EEVEE dans Blender 5.2.1 LTS : aucune ne dépend de Cycles.
- **Corrigés :** dans le fichier de travail, dans la collection masquée « Corrigé défi procédural », avec une sous-collection par étape. Il n'y a aucun fichier séparé.
- **Vérification des acquis :** 9 quiz dans l'application. Il n'y a pas de grille d'autoévaluation.

## Objectifs

À la fin du complément, l'apprenant sait :
- lire et régler les quatre textures de bruit de Blender : *Noise*, *Voronoi*, *Wave* et *Gabor* ;
- transformer une valeur avec *Color Ramp*, *Map Range* et *Math* ;
- construire un masque et s'en servir pour superposer deux matières avec *Mix* ;
- empiler des reliefs, y compris sur le vernis (*Coat Normal*) ;
- user une pièce sous EEVEE : bords, creux, rayures, traces de doigts ;
- construire un motif régulier : tôle perforée, cuir, tissu, et en option moletage et carbone ;
- regrouper une chaîne de nœuds dans un groupe réutilisable, avec des paramètres exposés.

## Prérequis : ce que le chapitre 3 a déjà montré

Le complément part de ces acquis, sans les reprendre.

| Déjà vu | Où, dans le chapitre 3 | Ce que le complément en fait |
|---|---|---|
| Le Principled BSDF : *Base Color*, *Metallic*, *Roughness*, *Coat*, *Alpha*, la transmission | Section 1 | Les entrées que pilotent les masques |
| Le Shader Editor, le nœud et le lien, `Maj + A`, `G`, `X` | Section 2, 1:35 | L'outil de tout le complément |
| *Noise Texture* et son réglage *Scale* | Section 2, 1:35 et 1:50 | Le point de départ de l'étape 1 |
| *Texture Coordinate*, sortie *Object* | Section 2, 1:50, étape 1 | Les coordonnées de toutes les recettes ; la sortie *Normal* arrive à l'étape 5 |
| *Bump* : *Height*, *Strength*, entrée *Normal* | Section 2, 1:50, étape 2 | Les reliefs chaînés de l'étape 4 |
| *Mapping*, l'étirement du brossé | Section 2, 1:50, étape 3 | Les rayures de l'étape 5 |
| L'onglet *Material*, rubrique *Settings* (*Render Method*) | Section 1, figure 3.13 | La tôle perforée (étape 6) |
| *Mark as Asset*, l'Outliner, *File > Append* | Section 3 | Le groupe de nœuds rangé en actif (étape 7) |
| Le compteur d'utilisateurs | Section 1 ; initiation | Un groupe partagé par plusieurs matières (étape 7) |
| La lampe en coloris A | Atelier ; fiche A2 | Le défi final, sur une copie |
| *Shade Auto Smooth*, le modificateur Bevel | Chapitre 2 | La condition de l'usure des bords (étape 5) |

Pour commencer, l'apprenant doit avoir ces acquis :
- soit il a suivi la séquence « Finitions procédurales » (1:50) ;
- soit il les avait déjà en début de formation.

En cas de doute, les trois quiz de la section 2 du chapitre 3 servent de test d'entrée : s'il les réussit, il peut commencer. La projection triplanaire et la bibliothèque ne sont pas nécessaires avant l'étape 7.

## Ce que le complément n'aborde pas

- **Le dépliage UV et les images peintes :** le principe du chapitre reste le même, pas de dépliage UV.
- **Normal Map :** ce nœud lit des images de normales en espace tangent, qui demandent un dépliage UV. Avec des textures procédurales, *Bump* suffit. Un encart NOTE le dit en une phrase (étape 4).
- **Le déplacement réel (Displacement) :** il demande une géométrie très dense et touche aux réglages de la matière. Le relief reste un *Bump*.
- **Le baking,** les Geometry Nodes, le nœud *Script* (OSL), les zones *Repeat* et *Closure* de Blender 5.
- **Les nœuds réservés à Cycles,** avec leur alternative EEVEE (tableau suivant).
- **L'éclairage et le rendu :** ils restent au chapitre 4. Le complément ne touche ni aux lumières, ni au monde, ni aux réglages de rendu.

### Ce qu'EEVEE ne fait pas, et ce que l'on fait à la place

Les informations viennent du manuel de Blender 5.2, page *EEVEE > Limitations > Nodes Support*. Les alternatives ont été rendues sous EEVEE.

| Besoin | Ce qui ne marche pas sous EEVEE | Alternative compatible EEVEE | Étape |
|---|---|---|---|
| Repérer les arêtes pour les user | *Geometry > Pointiness* ; nœud *Bevel* | La normale de la pièce (*Texture Coordinate > Normal*), sur une pièce biseautée (modificateur Bevel) et lissée | 5.1 |
| Repérer les arêtes par l'occlusion | *Ambient Occlusion* avec *Inside* : sous EEVEE, presque aucun signal à l'échelle de la lampe (testé) | La normale, ci-dessus | 5.1 |
| Repérer les creux | *Ambient Occlusion > Only Local* | *Ambient Occlusion* sans *Only Local*, avec une rampe très serrée près de 1 | 5.2 |
| Un brossé à reflets étirés | *Anisotropic* du Principled | Un relief étiré : *Gabor*, ou *Noise* et *Mapping* comme au chapitre 3 | 1, 5.3 |
| Une valeur au hasard par îlot | *Geometry > Random Per Island* | *Voronoi*, sortie *Color*, une valeur par cellule ; *Object Info > Random*, une par objet | 1 |
| Un velours, un tissu | *Sheen* : seulement approché sous EEVEE | *Sheen* garde un effet léger ; le relief du tissage fait l'essentiel | 6.3 |

## Quand et comment

**L'annonce.** À l'ouverture du chapitre 3, le formateur signale le défi en une phrase : « Pour ceux qui sont à l'aise, ou qui connaissent déjà ces sujets : un défi facultatif, hors programme, en section 4 du chapitre 3 dans l'application, avec le fichier `PRC02_ch3_defi_procedural.blend`. » Il ne fait aucune démonstration, et le minutage du chapitre 3 ne change pas.

**À la suite des parties de base.** L'apprenant suit le chapitre 3, puis ouvre le défi quand il lui reste du temps, en séance ou après. Il enregistre d'abord son fichier de travail : le défi se fait dans un autre fichier, et la lampe qui part au chapitre 4 n'est pas touchée.

**À la place des parties de base.** L'apprenant qui maîtrise déjà une partie du chapitre 3 peut faire le défi à sa place, pour un complément et des défis plus poussés. Il n'a alors pas forcément `lampe_habillage_v002.blend`, le point de départ du chapitre 4. Au choix, il reprend le chapitre 4 :
- avec le fichier de secours `PRC02_ch4_lampe_en_studio.blend`, enregistré sous `lampe_rendu_v001.blend`, comme le prévoit le chapitre 4 ;
- ou avec la lampe habillée du chapitre 3, `PRC02_ch3_lampe_habillage.blend` : dans le studio, il fait *File > Append* de sa collection *Lampe*, au lieu de celle de `lampe_habillage_v002.blend` ;
- ou avec sa propre lampe, habillée de ses matières procédurales. Elles fonctionnent sous EEVEE. Il garde le nom de collection *Lampe* et enregistre sous `lampe_habillage_v002.blend` : l'Append du chapitre 4 fonctionne alors sans changement.

C'est une option, pas une obligation. L'encart d'introduction de la section 4 le dit en deux phrases.

**Après la séance.** L'apprenant reprend à l'étape où il s'est arrêté. Chaque étape se termine par un point d'arrêt : un quiz de l'application et la comparaison avec le corrigé.

**Le même ordre à chaque étape :**
1. **Exemple :** une pièce terminée dans le fichier. L'apprenant l'observe, puis entre dans ses nœuds.
2. **Pratique guidée :** une recette numérotée, refaite sur une pièce à compléter.
3. **Petit défi :** une variante sans recette complète, avec son corrigé.

## La progression

### Une notion nouvelle à la fois

Chaque étape introduit une seule notion. Ses nœuds arrivent un par un, dans des sous-étapes. Les sous-étapes marquées ★ sont facultatives.

| Étape | Durée | La notion nouvelle | Les nœuds, dans l'ordre | Elle s'appuie sur |
|---|---|---|---|---|
| Avant de commencer | 5 min | L'aperçu d'un nœud | `Ctrl + Maj + clic` | Le nœud et le lien |
| **Palier 1** | | | | |
| 1 · Lire les textures de bruit | 20 min | Les réglages d'une texture procédurale | *Noise* (réglages), *Voronoi*, *Wave*, *Gabor* | *Noise*, *Scale*, *Object* |
| 2 · Remapper les valeurs | 20 min | Transformer une valeur en une autre | *Color Ramp*, *Map Range*, *Math* | Étape 1 |
| 3 · Masques et couches | 20 min | Un masque qui choisit entre deux couches | *Mix Color*, *Mix* (Float), puis *Separate XYZ* et *Math > Multiply* pour superposer | Étape 2 |
| 4 · Le relief procédural | 15 min | Enchaîner des reliefs | *Bump* chaîné ; *Coat Normal* ; un masque en relief | *Bump* (chapitre 3), étape 3 |
| **Palier 2** | | | | |
| 5 · L'usure | 30 min | Des masques tirés de la forme | *Texture Coordinate > Normal*, puis *Ambient Occlusion* ; rayures et traces en réemploi | Étapes 2 à 4 |
| 6 · Les motifs | 40 min | Un motif régulier construit à partir des coordonnées | *Voronoi* 2D en grille, puis *Alpha*, puis *Checker* ; ★ *Gradient* radial, ★ *Floor* | Étapes 1 à 4 |
| 7 · Les groupes de nœuds | 25 min | Le groupe et ses paramètres exposés | `Ctrl + G`, *Group Input*, *Group Output*, onglet *Group* ; option *Frame* | Étapes 2 et 5 ; *Mark as Asset* |

Durée totale : 175 minutes, soit environ 3 heures. Palier 1 : 80 minutes ; palier 2 : 95 minutes. Les durées sont indicatives : un apprenant à l'aise va plus vite.

### Les repères d'échelle

Toutes les recettes partent de *Texture Coordinate*, sortie *Object* : la texture se mesure en mètres. Ces repères servent à toutes les étapes :
- *Noise* et *Voronoi* : *Scale* donne à peu près le nombre de motifs par mètre. Avec *Scale* 100, il y a un motif tous les 10 mm environ ;
- *Wave* : une bande tous les 0,314 / *Scale* mètre. Avec *Scale* 40, il y a une bande tous les 7,9 mm ;
- *Bump* : comme au chapitre 3, le relief se règle avec *Strength*, de 0 à 1, et *Distance* garde sa valeur par défaut (0,001). Sur des pièces de la taille de la lampe, *Strength* va de 0,05 à 0,5.

## Les recettes, étape par étape

Conventions :
- les menus sont ceux de Blender 5.2, vérifiés dans le code de l'interface ;
- les couleurs sont en hexadécimal sRGB, comme dans le sélecteur de couleur de Blender ;
- toutes les valeurs ont été rendues sous EEVEE, sous l'image *studio*. Elles sont des points de départ et se retouchent à l'œil ;
- « TC » désigne le nœud *Texture Coordinate* ;
- « aperçu » désigne le geste `Ctrl + Maj + clic` (voir « Avant de commencer »).

### Les menus du Shader Editor dans Blender 5.2

Le menu `Maj + A` a été réorganisé depuis les versions 4 de Blender : il n'y a plus de catégorie *Vector* ni *Converter* au premier niveau.

| Nœud | Chemin dans `Maj + A` |
|---|---|
| *Texture Coordinate*, *Ambient Occlusion* | *Input* |
| *Noise*, *Voronoi*, *Wave*, *Gabor*, *Gradient*, *Checker* Texture | *Texture* |
| *Color Ramp*, *Mix Color* | *Color* |
| *Map Range*, *Math*, *Mix* (Float), *Clamp* | *Utilities > Math* |
| *Mapping*, *Separate XYZ*, *Vector Math* | *Utilities > Vector* |
| *Bump* | *Displacement* |
| Les groupes du fichier, *New Group* | *Group* |
| *Frame*, *Reroute* | *Layout* |

La recherche (`Maj + A`, puis taper le nom du nœud) trouve tout, y compris une opération de *Math* (« Ping-Pong », « Greater Than »…). Elle est conseillée aux apprenants.

### Avant de commencer (5 min)

**Nouveau :** l'aperçu d'un nœud. **Déjà vu :** le nœud et le lien, l'espace *Shading*.

1. Ouvrir `PRC02_ch3_defi_procedural.blend`, puis l'enregistrer sous `defi_procedural_v001.blend`.
2. Masquer (œil fermé) les collections des étapes suivantes. *Material Preview* calcule chaque matière visible : moins il y en a, plus l'affichage reste fluide.
3. **L'aperçu.** `Ctrl + Maj + clic` sur un nœud relie sa sortie directement à l'entrée *Surface* du *Material Output*. La pièce affiche alors la valeur brute du nœud :
   - en niveaux de gris : noir pour 0, blanc pour 1 ;
   - ou en couleurs, pour une sortie *Color*.

   Un nouveau `Ctrl + Maj + clic` sur le même nœud passe à sa sortie suivante. `Ctrl + Maj + clic` sur le *Principled BSDF* rétablit la matière. Ce geste est natif dans Blender 5.2 : Node Wrangler n'est pas nécessaire.

**Rendu attendu :** la pièce en niveaux de gris, sans reflet.

**Erreurs fréquentes :**
- Le blanc paraît gris clair : c'est la transformation de vue *AgX*, réglée par défaut. Lisez les contrastes, pas les valeurs absolues.
- La pièce reste grise et plate : l'aperçu n'a pas été annulé. `Ctrl + Maj + clic` sur le *Principled BSDF*.
- Rien ne se passe : le clic est tombé à côté du nœud.

### Palier 1

### Étape 1 · Lire les textures de bruit (20 min)

**Nouveau :** les réglages d'une texture procédurale, puis trois textures de plus. **Déjà vu :** *Noise Texture*, *Scale*, TC (*Object*), l'aperçu.

**Exemple :** quatre plaquettes de 80 × 80 mm, `E1_Exemple_Noise`, `_Voronoi`, `_Wave` et `_Gabor`, chacune en aperçu de sa texture. Observez, puis entrez dans les nœuds.

**Pratique guidée,** sur la plaquette `E1_Pratique` (80 × 80 × 4 mm). Chaque sous-étape change un seul nœud.

**1.1 · Noise Texture**

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | *Input > Texture Coordinate* | | *Object* → *Vector* du *Noise* |
| 2 | *Texture > Noise Texture* | *Scale* 100 | Aperçu sur *Factor* |
| 3 | Le même | *Detail* 8, *Roughness* 0,7 | |
| 4 | Le même | *Detail* 2, *Distortion* 2 | |
| 5 | Le même | Menu du type : *Ridged Multifractal* ; *Scale* 60, *Detail* 4, *Distortion* 0 | |

**Rendu attendu,** dans l'ordre :
- des nuages doux, environ huit sur la largeur ;
- un grain plus fin, plus riche ;
- des tourbillons ;
- des veines nettes et contrastées, pour un plastique marbré ou une pierre.

La sortie *Color* donne des nuages de couleurs pastel : elle sert rarement.

**1.2 · Voronoi Texture.** Remplacez *Noise* par *Texture > Voronoi Texture*, relié de la même façon, *Scale* 100.
- Sortie *Distance*, réglage *F1* (par défaut) : une tache sombre au centre de chaque cellule.
- Menu des réglages, *Distance to Edge* : de fins sillons sombres entre les cellules. C'est la base du cuir et des craquelures.
- Sortie *Color* : une couleur au hasard par cellule. Elle sert à faire varier légèrement chaque cellule.

**1.3 · Wave Texture.** *Texture > Wave Texture*, *Scale* 40.
- *Bands*, direction *X*, profil *Sine* : des bandes droites, une tous les 7,9 mm.
- *Distortion* 4, *Detail* 4 : des bandes ondulées.
- *Rings*, direction *Z* : des cercles concentriques, comme l'usinage d'un bouton ou d'un enjoliveur.

**1.4 · Gabor Texture.** *Texture > Gabor Texture*, *Scale* 100, type *2D*.
- Réglages par défaut : des stries fines, orientées à 45° (*Orientation* 0,785 rad).
- *Frequency* 6 : des stries plus serrées.
- *Anisotropy* 0 : plus d'orientation, le motif devient vermiculé.
- *Frequency* 6, *Anisotropy* 1, *Orientation* 1,571 (90°) : des stries serrées dans l'axe X ; avec *Orientation* 0, elles suivent l'axe Y.

**Rendu attendu :** les planches des figures 3.52, 3.54, 3.56 et 3.58.

**Erreurs fréquentes :**
- Une plaquette presque uniforme : *Scale* est resté à 5, sa valeur par défaut. Il n'y a qu'un motif pour 20 cm.
- Un motif étiré ou qui glisse avec la pièce : TC n'est pas relié. Le nœud utilise alors les coordonnées *Generated*, comme au chapitre 3.
- *Gabor* 2D sur une face verticale : il ne lit que X et Y, et les stries s'étirent sur les flancs. Gardez-le pour les faces planes et horizontales. Le type *3D* existe, avec une orientation en vecteur : c'est une piste à explorer.
- L'aperçu montre un dégradé de couleurs : c'est la sortie *Color*, pas *Factor* ou *Distance*.

**Petit défi (encart CAUTION) :** reproduisez trois plaquettes cibles, montrées sans leur recette (figure 3.59). Elles se font sur `E1_Defi_A`, `_B` et `_C`. Les solutions ci-dessous restent dans le plan et dans le corrigé : l'application ne montre que les cibles.
- **A, accoudoir d'avion :** des cellules séparées par des sillons. Solution : *Voronoi*, *Distance to Edge*, *Scale* 100.
- **B, bouton de commande automobile :** des cercles d'usinage. Solution : *Wave*, *Rings*, *Z*, *Scale* 40.
- **C, main courante de train :** un brossé fin dans l'axe X. Solution : *Gabor*, *Scale* 100, *Frequency* 6, *Orientation* 1,571 (90°).

Corrigé : sous-collection « Corrigé étape 1 ».

### Étape 2 · Remapper les valeurs (20 min)

**Nouveau :** transformer une valeur en une autre, avec trois nœuds, l'un après l'autre. **Déjà vu :** *Noise*, l'aperçu.

**Exemple :** `E2_Exemple_Coque`, une coque de siège ferroviaire en plastique recyclé moucheté.

**2.1 · Color Ramp,** sur `E2_Pratique_Mouchete` (plaquette 80 × 80 × 4 mm).

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC | | *Object* → *Vector* |
| 2 | *Noise Texture* | *Scale* 100 | *Factor* → *Factor* du *Color Ramp* |
| 3 | *Color > Color Ramp* | Curseur noir à 0,45, curseur blanc à 0,55 | Aperçu sur *Color* |
| 4 | Le même | Menu d'interpolation : *Constant* ; noir à 0, blanc à 0,5 | |
| 5 | *Noise* et *Color Ramp* | *Noise* : *Scale* 1500, *Detail* 0. *Color Ramp*, toujours en *Constant* : curseur 0 en #2B2D2F (anthracite), curseur 0,74 en #D8D6D0 (blanc cassé) | *Color* → *Base Color* ; *Roughness* 0,5 ; rétablir le Principled |

**Rendu attendu :**
- étape 3 : des taches nettes ;
- étape 4 : deux tons francs ;
- étape 5 : de fines mouchetures claires, environ une pour vingt, sur un fond anthracite.

**Repères :**
- avec le curseur clair à 0,70, les mouchetures deviennent trop denses ;
- à 0,62, la pièce paraît granitée.

**2.2 · Map Range,** sur `E2_Pratique_Planche` (plaquette noire, planche de bord automobile, *Base Color* #151515).

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Noise Texture* | *Scale* 40, *Detail* 3 | *Factor* → *Value* du *Map Range* |
| 2 | *Utilities > Math > Map Range* | *From Min* 0,35, *From Max* 0,65, *To Min* 0,08, *To Max* 0,35 ; *Clamp* coché | *Result* → *Roughness* |

**Rendu attendu :** des reflets nets par endroits et voilés ailleurs. C'est la brillance irrégulière d'un plastique injecté. Faites tourner l'image d'environnement pour la voir (menu *Viewport Shading*, chapitre 3).

**À retenir :** *From* décrit les valeurs qui entrent, *To* celles qui sortent. *To Min* et *To Max* sont de vraies valeurs de *Roughness*. *Clamp* empêche d'en sortir.

**2.3 · Math,** sur `E2_Pratique_Mouchete`, à côté du *Color Ramp*, sans toucher au Principled.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | *Utilities > Math > Math* | Opération *Greater Than*, *Threshold* 0,74 | Sortie du *Noise* (*Factor*) → première entrée ; aperçu sur *Value* |

**Rendu attendu :** les mêmes mouchetures, en blanc sur noir. *Greater Than* rend 1 au-dessus du seuil et 0 en dessous.

**À retenir :**
- le *Color Ramp* se règle à l'œil ;
- *Map Range* et *Math* se règlent en chiffres. Leurs chiffres pourront devenir les paramètres d'un groupe (étape 7).

**Erreurs fréquentes :**
- Le masque est inversé : les curseurs sont dans le mauvais ordre. Inversez-les, ou utilisez *Flip Color Ramp* dans le menu de la flèche du *Color Ramp*.
- *Map Range* ne change rien : les valeurs *From* et *To* ont été confondues.
- *Math* rend une pièce blanche : l'opération est restée sur *Add*, sa valeur par défaut.

**Petit défi (encart CAUTION) :** des mouchetures en deux couleurs, pour une coque de siège ferroviaire. Ajoutez un troisième curseur avec le bouton `+` : à 0,82, en #9B6B43 (terre cuite). Entre 0,74 et 0,82, les mouchetures restent claires ; au-dessus de 0,82, elles sont terre cuite, et plus rares.

Corrigé : sous-collection « Corrigé étape 2 ».

### Étape 3 · Masques et couches (20 min)

**Nouveau :** un masque qui choisit entre deux couches, puis la superposition de deux masques. **Déjà vu :** *Color Ramp*, *Map Range*, *Math*.

**Exemple :** `E3_Exemple_Main_courante`, une main courante en laiton patiné, celle d'une voiture-bar ou d'un train historique. Le même masque pilote trois entrées du Principled.

**Pratique guidée,** sur `E3_Pratique_Main_courante`. C'est un tube Ø 32 × 300 mm, en laiton neuf, couché sur X ; la rotation n'est pas appliquée, son axe local Z suit donc le tube.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Noise Texture* | *Scale* 40, *Detail* 6, *Roughness* 0,6 | *Factor* → *Color Ramp* |
| 2 | *Color Ramp* | Noir à 0,50, blanc à 0,60 | Aperçu : les taches blanches sont la patine. C'est le masque |
| 3 | *Color > Mix Color* | *A* #E0C27A (laiton), *B* #3A3B2C (patine) | Masque → *Factor* ; *Result* → *Base Color* |
| 4 | *Utilities > Math > Mix* (Float) | *A* 1, *B* 0 | Masque → *Factor* ; *Result* → *Metallic* |
| 5 | Un second *Mix* (Float) | *A* 0,25, *B* 0,7 | Masque → *Factor* ; *Result* → *Roughness* |

**Rendu attendu :** un laiton poli et brillant, avec des taches sombres, mates et non métalliques.

**3.4 · Superposer deux masques :** la patine ne reste qu'aux extrémités, là où les mains ne passent pas.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 6 | TC, puis *Utilities > Vector > Separate XYZ* | | *Object* → *Vector* ; sortie *Z* |
| 7 | *Math* | *Absolute* | *Z* → entrée |
| 8 | *Map Range* | *From Min* 0,08, *From Max* 0,14 | Aperçu : noir au centre, blanc aux deux bouts |
| 9 | *Math* | *Multiply* | Masque de patine (étape 2) × masque des extrémités (étape 8) → les trois *Factor* des Mix |

**Rendu attendu :** de la patine aux deux extrémités seulement. Au centre, le laiton reste poli.

**À retenir :**
- multiplier deux masques garde ce qu'ils ont en commun ;
- *Maximum* les additionne ;
- *Subtract* retire l'un de l'autre.

**Encart NOTE :** on peut aussi mélanger deux Principled avec *Mix Shader*. Un seul Principled, dont on mélange les entrées, est plus léger et plus simple à régler.

**Erreurs fréquentes :**
- La patine ne se voit pas : le masque n'est relié qu'à *Base Color*. Le laiton garde alors ses reflets métalliques. Reliez aussi *Metallic* et *Roughness*.
- La patine est partout et le laiton nulle part : *A* et *B* sont inversés.
- *Mix Color* a été pris pour *Mix* (Float) : le nœud n'a pas d'entrée chiffrée. Vérifiez le menu du type de données en haut du nœud.
- La patine se trouve au centre : le masque des extrémités est inversé. Échangez *From Min* et *From Max*.

**Petit défi (encart CAUTION) :** une main courante de quai en inox (#C8C8C6, *Metallic* 1, *Roughness* 0,15), entartrée de calcaire blanc (#D9D4C7, *Metallic* 0, *Roughness* 0,8). Les nœuds sont les mêmes, seules les valeurs changent. Pièce : `E3_Defi_Main_courante`.

Corrigé : sous-collection « Corrigé étape 3 ».

### Étape 4 · Le relief procédural (15 min)

**Nouveau :** enchaîner des reliefs, et donner son propre relief au vernis. **Déjà vu :** *Bump* (chapitre 3), le masque de l'étape 3, *Coat* (chapitre 3, section 1).

**Exemple :** `E4_Exemple_Coque`, une coque de rétroviseur en laque rouge à peau d'orange.

**4.1 · Deux reliefs chaînés,** sur `E4_Pratique_Boitier`. C'est un boîtier d'avionique en aluminium de 120 × 80 × 30 mm, avec un Bevel de 3 mm, en #D9DADB, *Metallic* 1 et *Roughness* 0,45.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Noise* A | *Scale* 2000, *Detail* 0 | *Factor* → *Height* du *Bump* A |
| 2 | *Displacement > Bump* (A) | *Strength* 0,1 | *Normal* → entrée *Normal* du *Bump* B |
| 3 | TC, puis *Noise* B | *Scale* 150, *Detail* 4 | *Factor* → *Height* du *Bump* B |
| 4 | *Bump* (B) | *Strength* 0,2 | *Normal* → *Normal* du Principled |

**Rendu attendu :** un grain microbillé et des ondulations douces, un aspect martelé.

**À retenir :** le dernier *Bump* de la chaîne va au Principled ; chaque *Bump* reçoit le précédent par son entrée *Normal*.

**4.2 · La peau d'orange,** sur `E4_Pratique_Coque`. C'est une coque de rétroviseur, un demi-ellipsoïde de 220 × 140 × 120 mm, en laque rouge #A3161A : *Roughness* 0,4, *Coat Weight* 1, *Coat Roughness* 0,03.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Noise* | *Scale* 600, *Detail* 1 | *Factor* → *Height* |
| 2 | *Bump* | *Strength* 0,15 | *Normal* → **Coat Normal** (rubrique *Coat* du Principled) |

**Rendu attendu :** les reflets du vernis ondulent légèrement, comme sur une carrosserie réelle. Avec *Strength* 0,3, le défaut devient visible, comme une retouche. À 0,05, il disparaît presque.

**4.3 · Un masque en relief,** sur la main courante de l'étape 3. Le masque de patine → *Height* d'un nouveau *Bump*, *Strength* 0,1 → *Normal* du Principled. La patine forme une couche en léger relief. La case *Invert* du *Bump* la met en creux.

**Encart NOTE :** le nœud *Normal Map* lit des images de normales, qui demandent un dépliage UV. Avec des textures procédurales, *Bump* suffit.

**Erreurs fréquentes :**
- Seul le grain fin se voit : la sortie *Normal* du *Bump* A n'entre pas dans le *Bump* B.
- Un relief qui scintille : *Strength* est trop forte. Divisez-la par deux, comme au chapitre 3.
- La peau d'orange trouble la teinte, mais le vernis reste lisse : elle est branchée sur *Normal* et non sur *Coat Normal*.
- *Filter Width*, nouveau dans Blender 5, reste à sa valeur par défaut, 0,1.

**Petit défi (encart CAUTION) :** une peinture métallisée automobile. Gardez la peau d'orange sur *Coat Normal*. Ajoutez des paillettes sous le vernis : *Voronoi* (*Scale* 3000) → *Bump* (*Strength* 0,1) → *Normal*. Réglez la base en #1C3F7A, *Metallic* 1. Comparez avec `Peinture_Metallisee_Bleu` du nuancier, récupérée par *File > Append* (chapitre 3, section 3). Pièce : `E4_Defi_Coque`.

Corrigé : sous-collection « Corrigé étape 4 ».

**Point d'arrêt du palier 1 :** les quiz 1 à 5.

### Palier 2

### Étape 5 · L'usure (30 min)

**Nouveau :** des masques tirés de la forme de la pièce : la normale (5.1), puis l'occlusion (5.2). Les rayures et les traces réemploient des nœuds connus. **Déjà vu :** *Separate XYZ*, *Math*, *Color Ramp*, *Mix*, *Mapping*, *Coat*.

**Encart IMPORTANT :** sous Cycles, on repère les arêtes avec *Pointiness* ou le nœud *Bevel*. Ni l'un ni l'autre ne fonctionne sous EEVEE. Les recettes de cette étape ont toutes été rendues sous EEVEE.

**Exemple :** `E5_Exemple_Coffret`, un coffret électrique de quai, peint en vert, aux arêtes usées et sali au pied.

**5.1 · Les bords usés,** sur `E5_Pratique_Socle`. C'est un cylindre de Ø 180 × 25 mm, avec un modificateur Bevel de 3 mm à 4 segments et *Shade Auto Smooth*, peint en #2F5D3A.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC | | Sortie **Normal** → *Separate XYZ* |
| 2 | *Separate XYZ* | | *Z* → *Math* |
| 3 | *Math* | *Absolute* | → *Color Ramp* |
| 4 | *Color Ramp* | Trois curseurs : noir à 0,10 ; blanc à 0,50 (bouton `+`) ; noir à 0,90 | Aperçu : un liseré blanc sur les arêtes du dessus et du dessous |
| 5 | TC (*Object*), puis *Noise* | *Scale* 400, *Detail* 8, *Roughness* 0,7 | *Factor* → *Math* |
| 6 | *Math* | *Multiply* | *Color Ramp* × *Noise* |
| 7 | *Map Range* | *From Min* 0,30, *From Max* 0,40 | *Result* : le masque d'usure |
| 8 | *Mix Color* | *A* #2F5D3A (peinture), *B* #B8B9BA (métal) | Masque → *Factor* ; *Result* → *Base Color* |
| 9 | — | | Masque → *Metallic* |
| 10 | *Map Range* | *To Min* 0,45, *To Max* 0,30 | Masque → *Value* ; *Result* → *Roughness* |

**Pourquoi ça marche :** la normale pointe vers le haut sur le dessus, vers le côté sur le flanc, et entre les deux dans le biseau. Le *Color Ramp* ne garde que l'entre-deux.

**Rendu attendu :** un liseré métallique irrégulier sur les arêtes. Il n'est jamais plus large que le biseau.

**★ Variante pour une pièce prismatique (boîtier, coffret) :** *Vector Math* (*Absolute*) sur la normale → *Separate XYZ* → *Math Maximum* (X, Y) → *Math Maximum* (résultat, Z) → *Color Ramp* (blanc à 0,80, noir à 0,97). Toutes les arêtes s'usent, y compris les verticales. Ne l'utilisez pas sur un cylindre : son flanc s'userait par bandes (figure 3.73).

**Erreurs fréquentes :**
- Rien ne s'use : la pièce n'a pas de biseau, ou elle n'est pas lissée. Ajoutez un modificateur Bevel d'au moins 3 segments, puis *Shade Auto Smooth* (chapitre 2).
- L'usure est trop fine : sa largeur dépend du biseau. Élargissez le Bevel du modificateur ; le shader ne peut pas aller au-delà.
- Toute une surface s'use : la pièce est bombée, comme la tête de la lampe ou une coque. La normale y prend toutes les directions, et la méthode ne convient qu'aux pièces à faces planes ou cylindriques.
- L'usure est sur le flanc et pas sur le dessus : la rotation de la pièce a été appliquée, et son axe n'est plus Z. Prenez la sortie X ou Y de *Separate XYZ*.
- Il y a trop d'usure : montez *From Min* et *From Max* du *Map Range* de la ligne 7.

**5.2 · La saleté dans les creux,** sur `E5_Pratique_Marchepied`. C'est une plaque de 200 × 200 × 10 mm à trois nervures de 12 × 180 × 12 mm, en aluminium #9A9C9E, *Metallic* 1, *Roughness* 0,35.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | *Input > Ambient Occlusion* | *Distance* `20mm` ; *Inside* et *Only Local* décochés | Sortie **AO** → *Color Ramp* |
| 2 | *Color Ramp* | Blanc à 0,85, noir à 0,99 | Aperçu : un trait sombre au pied des nervures |
| 3 | TC, puis *Noise* | *Scale* 200, *Detail* 6 | → *Color Ramp* (noir à 0,35, blanc à 0,65) |
| 4 | *Math* | *Multiply* | Les deux rampes : le masque de saleté |
| 5 | *Mix Color* | *A* #9A9C9E, *B* #3B342C | → *Base Color* |
| 6 | *Mix* (Float) | *A* 1, *B* 0 | → *Metallic* |
| 7 | *Map Range* | *To Min* 0,35, *To Max* 0,9 | → *Roughness* |

**Rendu attendu :** une crasse mate et irrégulière au pied des nervures.

**Encart NOTE, l'occlusion sous EEVEE :**
- elle se calcule à partir de l'image affichée. Elle change un peu quand on tourne autour de la pièce, et ne tient compte que de ce qui est à l'écran ;
- ses valeurs restent très proches de 1, d'où la rampe très serrée ;
- *Only Local* n'est pas pris en charge.

**Erreurs fréquentes :**
- Rien ne se voit : la rampe est restée entre 0 et 1. Resserrez-la près de 1.
- Toute la pièce s'assombrit, avec des halos : *Distance* est trop grande. Gardez l'ordre de grandeur du creux.
- La saleté se met sur les arêtes : *Inside* est coché.

**5.3 · Les rayures,** sur `E5_Pratique_Main_courante`. C'est un tube inox de Ø 32 × 300 mm, d'axe local Z, en #C8C8C6, *Metallic* 1.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Mapping* | *Scale* : X 1, Y 1, Z 0,02 | *Vector* → *Noise* |
| 2 | *Noise* | *Scale* 2000, *Detail* 2 | → *Color Ramp* |
| 3 | *Color Ramp* | Noir à 0,68, blanc à 0,70 | Aperçu : de rares traits blancs dans la longueur |
| 4 | *Map Range* | *To Min* 0,05, *To Max* 0,5 | → *Roughness* |

**Rendu attendu :** de fines rayures mates dans la longueur, visibles dans les reflets. C'est le brossé du chapitre 3, avec un seuil.

**Erreurs fréquentes :**
- Les rayures sont en travers : l'axe étiré dans *Mapping* n'est pas le bon.
- Il y en a trop : montez les deux curseurs, par exemple à 0,72 et 0,74.
- Elles ne se voient pas : la pièce est déjà trop mate. Gardez un *To Min* bas.

**5.4 · Les traces de doigts,** sur `E5_Pratique_Console`. C'est une console noir piano de 200 × 120 × 10 mm, comme sur une planche de bord automobile : #0A0A0A, *Roughness* 0,3, *Coat Weight* 1, *Coat Roughness* 0,02.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Noise* | *Scale* 25, *Detail* 6, *Roughness* 0,7, *Distortion* 0,3 | → *Map Range* |
| 2 | *Map Range* | *From Min* 0,55, *From Max* 0,75, *To Min* 0,02, *To Max* 0,4 | → **Coat Roughness** |

**Rendu attendu :** des halos voilés dans le reflet du vernis. Une trace de doigt ne change pas la couleur : seulement la brillance du vernis.

**Erreurs fréquentes :**
- Les traces sont branchées sur *Base Color* : la pièce devient grise par plaques.
- Elles sont branchées sur *Roughness* : sous un vernis brillant, elles ne se voient presque pas.
- Elles ne se voient qu'à un endroit : c'est normal, il faut un reflet. Faites tourner l'image d'environnement.

**Petit défi (encart CAUTION) :** `E5_Defi_Coffret`, un coffret de quai de 200 × 120 × 80 mm, avec un Bevel de 4 mm, posé sur une plinthe. Usez ses arêtes (variante prismatique), puis salissez son pied. Deux couches successives : un premier *Mix* passe de la peinture au métal, un second passe de ce résultat à la saleté.

Corrigé : sous-collection « Corrigé étape 5 ».

### Étape 6 · Les motifs (40 min)

**Nouveau :** un motif régulier, construit à partir des coordonnées. Les sous-notions arrivent une par une : la grille, puis le perçage, puis le croisement de deux motifs. **Déjà vu :** *Voronoi*, *Wave*, *Math*, *Mix*, *Bump*, *Alpha* (chapitre 3).

**Exemple :** `E6_Exemple_Dalle`, une dalle à pastilles en relief, comme un plancher antidérapant ou une dalle podotactile de quai.
- *Voronoi Texture*, type **2D**, *Scale* 125, *Randomness* **0** → *Distance* → *Color Ramp* (blanc à 0,28, noir à 0,32) → *Bump* (*Strength* 0,5) → *Normal*.
- Avec *Randomness* 0, les cellules forment une grille parfaite.
- Rendu : des pastilles de Ø 4,8 mm au pas de 8 mm.

**6.1 · La tôle perforée,** sur `E6_Pratique_Grille`. C'est une plaque de 120 × 80 × 1,5 mm, posée à plat : une grille de haut-parleur automobile ou un plafond perforé de voiture ferroviaire. Elle est en #B8B9BA, *Metallic* 1, *Roughness* 0,35.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Voronoi* | Type 2D, *Scale* 250, *Randomness* 0 | *Distance* → *Math* |
| 2 | *Math* | *Greater Than*, *Threshold* 0,3 | *Value* → **Alpha** du Principled |

**Rendu attendu :** des trous ronds de Ø 2,4 mm au pas de 4 mm. On voit à travers, et l'ombre de la plaque est percée.

**Formules utiles :**
- *Scale* = 1000 / pas en mm ;
- seuil = diamètre / (2 × pas).

*Render Method* reste sur *Dithered*, sa valeur par défaut (onglet *Material*, rubrique *Settings*, figure 3.13).

**Erreurs fréquentes :**
- Les trous manquent ou n'ont pas tous la même taille : le *Voronoi* est en 3D. Le plan coupe alors la grille entre deux rangées de points. Passez-le en 2D.
- Les trous sont en désordre : *Randomness* est resté à 1.
- Il ne reste que des pastilles qui flottent : l'opération est *Less Than* au lieu de *Greater Than*.
- Les trous sont étirés sur une plaque dressée : le type 2D ne lit que X et Y. Ajoutez un *Mapping*, *Rotation* X 90°.

**6.2 · Le cuir grainé,** sur `E6_Pratique_Accoudoir`. C'est un accoudoir d'avion de 300 × 60 × 50 mm, avec un Bevel de 8 mm, en #1E1B19, *Roughness* 0,55.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Voronoi* | Type 3D, *Scale* 500, *Distance to Edge* | *Distance* → *Color Ramp* |
| 2 | *Color Ramp* | Noir à 0, blanc à 0,08 | → *Height* |
| 3 | *Bump* | *Strength* 0,2 | → *Normal* |

**Rendu attendu :** un grain fin et régulier, des cellules de 2 mm aux sillons creusés. Le chapitre 3 utilisait une image (`grain_cuir.png`). Ici, tout est calculé et il n'y a aucun raccord. Option : *Detail* 2 rend le grain irrégulier.

**6.3 · Le tissu de siège,** sur `E6_Pratique_Assise`. C'est un échantillon d'assise ferroviaire, un coussin de 120 × 120 × 40 mm avec un Bevel de 10 mm à 6 segments.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Texture > Checker Texture* | *Scale* 500 | *Factor* → *Factor* d'un *Mix* (Float) |
| 2 | *Wave* A | *Bands*, direction X, *Scale* 157 | *Factor* → *A* du *Mix* |
| 3 | *Wave* B | *Bands*, direction Y, *Scale* 157 | *Factor* → *B* du *Mix* |
| 4 | *Mix* (Float) | | *Result* → *Height* d'un *Bump* (*Strength* 0,4) → *Normal* |
| 5 | *Mix Color* | *A* #141C30, *B* #2E3D63 | Le même *Result* → *Factor* ; → *Base Color* |
| 6 | Principled | *Roughness* 0,8, *Sheen Weight* 0,5 | |

**La règle :** le *Scale* des *Wave* vaut 0,314 × le *Scale* du *Checker*. On obtient alors une bosse de fil par case.

**Rendu attendu :** une armure toile bleu marine, avec des fils de 2 mm. Le *Checker* alterne les fils dans un sens et dans l'autre.

**Erreurs fréquentes :**
- Les fils sont décalés ou moirés : la règle des 0,314 n'est pas respectée.
- Un moiré à distance : les fils sont trop fins pour l'écran. C'est un effet d'affichage, il disparaît de près.
- Un tissu trop brillant : *Roughness* est trop basse ; un tissu reste mat.

**Petit défi (encart CAUTION), deux motifs ★ avec leur recette complète.** Essayez d'abord avec l'indice.

**6.4 · ★ Le moletage,** sur `E6_Defi_Molette`. C'est un bouton de commande de Ø 30 × 40 mm, d'axe local Z, pour l'automobile ou un cockpit d'avion : #C8C8C6, *Metallic* 1, *Roughness* 0,35. Indice : on « déroule » le cylindre.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, puis *Texture > Gradient Texture* | Type **Radial** | *Factor* : l'angle autour de Z, de 0 à 1 |
| 2 | *Math* | *Multiply* × 60 (le nombre de dents) | = u |
| 3 | TC, *Separate XYZ*, *Math* | *Multiply* × 636,6, soit 60 / (2π × 0,015) | Z → v |
| 4 | *Math* *Add* et *Math* *Subtract* | u + v ; u − v | |
| 5 | Deux *Math* *Ping-Pong* | *Scale* 0,5 | Un par résultat |
| 6 | *Math* | *Minimum* | Les deux *Ping-Pong* → *Height* d'un *Bump* (*Strength* 0,3) → *Normal* |

**Rendu attendu :** des pointes de diamant de 1,6 mm, sans couture.
- Le nombre de dents doit être entier, sinon une couture apparaît.
- Sur les faces du dessus et du dessous, le motif forme des rayons : donnez-leur une autre matière, ou acceptez-les.

**6.5 · ★ Le carbone sergé 2/2,** sur `E6_Defi_Panneau`. C'est un panneau de 300 × 200 × 2 mm, légèrement cintré. Indice : on numérote les cases.

| Ordre | Nœud | Réglages | Lien |
|---|---|---|---|
| 1 | TC, *Separate XYZ* | | X et Y |
| 2 | Deux *Math* *Multiply* × 250, puis deux *Math* *Floor* | | Le numéro de colonne et de rangée |
| 3 | *Math* *Add*, puis *Floored Modulo* 4, puis *Less Than* 2 | | Le masque du sergé |
| 4 | *Wave* X et *Wave* Y | *Bands*, *Scale* 78,5 (0,314 × 250) | → *A* et *B* d'un *Mix* (Float), *Factor* = masque |
| 5 | *Bump* | *Strength* 0,1 | *Result* → *Height* ; → *Normal* |
| 6 | *Mix Color* | *A* #0B0B0C, *B* #26262A | Masque → *Factor* ; → *Base Color* |
| 7 | Principled | *Roughness* 0,3, *Coat Weight* 1, *Coat Roughness* 0,02 | |

**Rendu attendu :** un sergé 2/2 en diagonale, avec des mèches de 4 mm, comme un carbone 12K. Avec 500 au lieu de 250, on obtient un 3K plus fin.

**La limite :** sur une pièce très galbée, le motif s'étire, car il n'y a pas de coordonnées UV. Dans ce cas, préférez le carbone en projection triplanaire du chapitre 3 (`Carbone_Serge`).

Corrigé : sous-collection « Corrigé étape 6 ».

### Étape 7 · Les groupes de nœuds (25 min)

**Nouveau :** le groupe de nœuds et ses paramètres exposés. **Déjà vu :** la chaîne des bords usés (5.1), *Map Range* et *Math* (étape 2), le compteur d'utilisateurs, *Mark as Asset* (chapitre 3, section 3).

**Exemple :** `E7_Exemple_Grain`. Sa matière contient un seul nœud de groupe, `PRC_Grain_Fin`, qui regroupe *Noise* et *Bump*. Il a deux entrées, *Échelle* (1500) et *Relief* (0,00005), et une sortie *Normal*. `Tab` pour entrer dans le groupe, `Tab` pour en sortir.

**Pratique guidée,** sur `E7_Pratique_Socle` : le même socle qu'en 5.1, avec la chaîne des bords usés déjà construite.

**7.1 · Préparer : des chiffres à la place des curseurs.** Les curseurs d'un *Color Ramp* ne peuvent pas devenir des paramètres d'un groupe. On remplace donc le *Color Ramp* à trois curseurs par trois nœuds :
- *Math* *Ping-Pong* (*Scale* 0,5) ;
- *Math* *Multiply* × 2 ;
- *Map Range*, *From Min* 0,2, *From Max* 1.

L'aperçu montre le même liseré : c'est le même calcul, écrit en chiffres.

**7.2 · Créer le groupe.**
1. Sélectionnez les nœuds du masque, de TC au dernier *Map Range*, sans le Principled ni les *Mix*.
2. `Ctrl + G` (menu *Node > Make Group*). Les nœuds deviennent un seul nœud de groupe.
3. `Tab` : l'intérieur du groupe, avec *Group Input* à gauche et *Group Output* à droite. Chaque lien qui sortait de la sélection est devenu une sortie du groupe.

**7.3 · Exposer les paramètres.**
1. Glissez la prise vide de *Group Input* vers une entrée d'un nœud. Elle devient un paramètre du groupe.
2. Exposez trois paramètres :
   - *Largeur* : *From Min* = 1 − *Largeur*, par un *Math* *Subtract* dont la première valeur vaut 1 ;
   - *Quantité* : le seuil du dernier *Map Range*. *From Min* = 0,7 − *Quantité* et *From Max* = *From Min* + 0,1, avec deux *Math* ;
   - *Échelle du bruit* : *Scale* du *Noise*.
3. Barre latérale (`N`), onglet *Group* :
   - nommez le groupe `PRC_Usure_Bords`, puis ajoutez une description ;
   - dans la rubrique *Group Sockets*, la liste des entrées et des sorties, renommez chaque prise. Réglez *Largeur* (défaut 0,8) et *Quantité* (défaut 0,4) entre 0 et 1, avec le sous-type *Factor*, qui affiche un curseur. Avec ces valeurs, le groupe refait exactement la chaîne de 5.1. Réglez *Échelle du bruit* à 400 par défaut ;
   - nommez la sortie *Masque*.

   Le bouton `+`, menu *New Item*, ajoute une entrée, une sortie ou un panneau.
4. `Tab` pour sortir. Sur le nœud de groupe, *Largeur* et *Quantité* se règlent comme des réglages de Blender.

**7.4 · Réutiliser.** Sur une autre pièce, `Maj + A > Group > PRC_Usure_Bords`. Reliez *Masque* à un *Mix Color* et à *Metallic*, comme en 5.1.

**7.5 · Option : ranger et partager.**
- `Ctrl + J` encadre les nœuds sélectionnés dans un *Frame*. Son nom se règle dans la barre latérale, onglet *Node*, champ *Label*.
- `Maj + clic droit` glissé sur un lien ajoute un *Reroute*, pour plier les liens. `Ctrl + clic droit` glissé coupe des liens.
- Dans l'Outliner, en mode *Blender File*, rubrique *Node Groups* : clic droit sur le groupe, *Mark as Asset*. Le groupe rejoint la bibliothèque, comme les matières du chapitre 3.

**Rendu attendu :** le socle s'use comme en 5.1, et *Largeur* et *Quantité* se règlent sans entrer dans le groupe. Rendu sous EEVEE avec les valeurs par défaut, *Largeur* 0,8 et *Quantité* 0,4.

**Erreurs fréquentes :**
- Le groupe sort un shader : le Principled était dans la sélection. `Ctrl + Z`, puis resélectionnez sans lui.
- Le groupe ne rend rien : rien n'est relié au *Group Output*.
- Un paramètre accepte des valeurs absurdes : son *Min* et son *Max* n'ont pas été réglés.
- Le nom a changé sur le nœud seulement : c'est son *Label*, pas le nom du groupe. Le nom se règle dans l'onglet *Group*.
- Modifier le groupe change toutes les pièces qui l'utilisent : c'est voulu, comme une matière partagée (compteur d'utilisateurs). Pour une variante, rendez le groupe indépendant par son compteur.

**Petit défi (encart CAUTION)**
- **★ Un axe au choix :** ajoutez une entrée *Axe* (*Vector*, défaut 0, 0, 1). Remplacez *Separate XYZ* (Z) par *Vector Math* *Dot Product* (normale · *Axe*). Le même groupe use alors une articulation couchée sur Y, même si sa rotation a été appliquée.
- **★★ La tôle perforée en millimètres :** un groupe `PRC_Tole_Perforee`, avec deux entrées, *Pas (mm)* (4) et *Diamètre (mm)* (2,4), et une sortie *Alpha*. À l'intérieur :
  - *Math* *Divide* (1000 / *Pas*) → *Scale* du *Voronoi* 2D ;
  - *Math* *Divide* (*Diamètre* / *Pas*) → *Math* *Multiply* 0,5 → *Threshold* du *Greater Than*.

  Le designer règle des millimètres, pas des échelles. Rendu vérifié avec 4 mm et 2,4 mm, puis 8 mm et 6 mm.

**Défi final · La lampe d'atelier (encart CAUTION) :** sur la copie `Lampe_defi`, en coloris A, donnez à la lampe dix ans de service :
- `PRC_Usure_Bords` sur le socle, qui laisse voir l'aluminium, et sur les articulations, dont le chrome s'use jusqu'au laiton. Pas sur la tête : elle est bombée, voir 5.1 ;
- la saleté de 5.2 au pied des lamelles de la grille d'aération, avec *Distance* `5mm` ;
- les rayures de 5.3 sur les bras ;
- les traces de 5.4 sur la laque de la tête, par son *Coat Roughness*.

Corrigé : sous-collection « Corrigé étape 7 ».

**Point d'arrêt du palier 2 :** les quiz 6 à 9.

## Les quiz de vérification des acquis

Neuf quiz, au format du module de quiz de l'application (`question`, `options`, `correctIndices` à partir de 0, `explanation`). Chacun se place à la fin de l'étape indiquée. Ils peuvent aussi se faire ensemble à l'écran.

| N° | Placé après | Question | Options (la bonne en gras) | Explication |
|---|---|---|---|---|
| 1 | Étape 1 | « Une Noise Texture, reliée en coordonnées Object, couvre une plaquette de 80 mm d'une teinte presque uniforme. Que faites-vous ? » | **Augmenter Scale, vers 100** ; augmenter Detail ; augmenter Distortion ; passer en Ridged Multifractal | « Avec les coordonnées Object, *Scale* compte à peu près les motifs par mètre. À 5, sa valeur par défaut, un seul motif couvre 20 cm. » |
| 2 | Étape 1 | « Quelle texture et quel réglage donnent des cellules séparées par de fins sillons, comme un grain de cuir ? » | Voronoi en F1 ; **Voronoi en Distance to Edge** ; Wave en Rings ; Noise en Ridged Multifractal | « *Distance to Edge* mesure la distance au bord de chaque cellule : les bords deviennent des sillons sombres. *F1* marque au contraire le centre des cellules. » |
| 3 | Étape 2 | « Vous voulez que la Roughness varie entre 0,08 et 0,35 selon un bruit. Quel nœud règle ces deux valeurs en chiffres ? » | Color Ramp ; **Map Range** ; Mix Color ; Bump | « *Map Range* fait passer les valeurs de *From Min*–*From Max* à *To Min*–*To Max*. Ici, *To Min* 0,08 et *To Max* 0,35 sont de vraies valeurs de *Roughness*. » |
| 4 | Étape 3 | « Sur la main courante patinée, un même masque pilote les entrées du Principled. Lesquelles faut-il relier pour passer du laiton à la patine ? » (plusieurs réponses) | **Base Color** ; **Metallic** ; **Roughness** ; IOR | « La patine change la teinte, n'est plus métallique et devient mate. Les trois entrées suivent le même masque, par trois *Mix*. » |
| 5 | Étape 4 | « La peau d'orange d'une laque se voit dans le reflet du vernis. Où brancher son Bump ? » | Normal ; **Coat Normal** ; Base Color ; Displacement du Material Output | « Le vernis a son propre relief, *Coat Normal*. Branché sur *Normal*, le relief trouble la teinte, mais le vernis reste lisse. » |
| 6 | Étape 5 | « Sous EEVEE, comment repérer les arêtes d'une pièce biseautée pour les user ? » | Geometry > Pointiness ; le nœud Bevel ; **La normale (Texture Coordinate > Normal), triée par un Color Ramp** ; Ambient Occlusion avec Inside | « *Pointiness* et le nœud *Bevel* ne fonctionnent que sous Cycles. Sous EEVEE, *Inside* ne donne presque rien à cette échelle. Dans un biseau lissé, la normale passe d'une direction à l'autre : c'est elle que l'on trie. » |
| 7 | Étape 5 | « Votre masque de saleté, tiré du nœud Ambient Occlusion, ne montre presque rien. Que faites-vous ? » | Cocher Only Local ; **Resserrer le Color Ramp près de 1, par exemple de 0,85 à 0,99** ; passer Distance à 1 m ; augmenter Detail du bruit | « Sous EEVEE, les valeurs de l'occlusion restent très proches de 1 : il faut une rampe très serrée. *Only Local* n'est pas pris en charge, et une grande *Distance* assombrit toute la pièce. » |
| 8 | Étape 6 | « Pour percer une tôle sans modéliser les trous, sur quelle entrée du Principled branchez-vous le masque ? » | Transmission Weight ; Normal ; **Alpha** ; Coat Weight | « *Alpha* à 0 rend la surface invisible : on voit au travers, et l'ombre est percée. *Transmission* ferait un verre, pas un trou. » |
| 9 | Étape 7 | « Pourquoi remplacer le Color Ramp par Map Range et Math avant de créer le groupe ? » | Un Color Ramp ne fonctionne pas dans un groupe ; **Les curseurs d'un Color Ramp ne peuvent pas devenir des paramètres du groupe** ; Map Range est plus rapide sous EEVEE ; Ctrl + G supprime les Color Ramp | « Un groupe expose des entrées de nœuds. Les curseurs d'un *Color Ramp* n'en sont pas, alors que *From Min* ou *Threshold* en sont. » |

Les quiz 1 à 5 forment le point d'arrêt du palier 1, les quiz 6 à 9 celui du palier 2.

## Fichiers d'exercice

La session principale construit ce fichier avec le MCP Blender, d'après la fiche ci-dessous. Ce plan n'en crée aucun.

### Où trouver le corrigé, exercice par exercice

La convention est commune aux chapitres 2 à 4 :
- le corrigé est dans le fichier de travail, dans une collection masquée (œil fermé) dont le nom commence par « Corrigé » ;
- le LISEZ-MOI indique en une ligne où le trouver.

Le complément a un seul fichier de travail. **Aucun fichier séparé n'est justifié :**
- tout le résultat tient dans des collections ;
- le complément ne règle ni le rendu ni le monde ;
- sa seule image, celle de la peinture structurée de la lampe, est empaquetée ;
- il ne sert de point de départ à aucun chapitre.

| Exercice | Moment | Fichier de travail | Où se trouve le corrigé |
|---|---|---|---|
| Avant de commencer | À la suite des parties de base, ou à leur place | `PRC02_ch3_defi_procedural.blend`, enregistré sous `defi_procedural_v001.blend` | Sans objet : un geste |
| Étape 1 · Bruits | En séance ou après | Le même | Sous-collection « Corrigé étape 1 » de la collection masquée « Corrigé défi procédural » |
| Étape 2 · Remapper | En séance ou après | Le même | « Corrigé étape 2 » |
| Étape 3 · Masques | En séance ou après | Le même | « Corrigé étape 3 » |
| Étape 4 · Relief | En séance ou après | Le même | « Corrigé étape 4 » |
| Étape 5 · Usure | En séance ou après | Le même | « Corrigé étape 5 » |
| Étape 6 · Motifs | En séance ou après | Le même | « Corrigé étape 6 » |
| Étape 7 · Groupes et défi final | En séance ou après | Le même | « Corrigé étape 7 », avec `Lampe_defi_corrige` |

### Fiche F · `PRC02_ch3_defi_procedural.blend`

La lettre E n'est pas reprise : au chapitre 3, elle désignait le mémo imprimé, reporté.

**Rôle :** le banc d'échantillons du défi. Pour chaque étape, il contient une pièce d'exemple terminée, les pièces à compléter et leur corrigé masqué. Il contient aussi une copie de la lampe pour le défi final.

**Règles communes,** celles du chapitre 3 :
- Blender 5.2 LTS ; construction par script en arrière-plan, scripts rejouables dans `tool/exercices_ch3/` ;
- unités *Metric*, *Length* en *Millimeters*, *Unit Scale* 1,0 ;
- aucun chemin absolu, aucun texte d'extension tierce, `save_version` à 0 ;
- une seule image, empaquetée : `grain_structure.png`, celle de la peinture structurée du socle de `Lampe_defi` ; toutes les recettes du défi sont procédurales ;
- pièces sans dépliage UV : supprimer les couches UV des primitives ;
- *Shade Auto Smooth* sur toutes les pièces biseautées ;
- rotations non appliquées sur les tubes et les molettes, pour que leur axe local Z suive la pièce.

**Scène :**
- EEVEE, *Raytracing* décoché, pour garder le fichier fluide. L'ampoule de `Lampe_defi` ne montre que l'environnement : le LISEZ-MOI le signale.
- Aucune lumière : *Material Preview* avec l'image *studio*, comme au chapitre 3.

**Collections visibles,** une par étape, une rangée par étape. Dispositions indicatives : rangées espacées de 0,32 m en Y, pièces espacées de 0,12 à 0,40 m en X selon leur taille. Le titre de chaque rangée est un objet texte de 0,010 m de haut, avec la matière `Etiquette` (gris très sombre, mate).

| Collection | Objet | Forme et dimensions | Matière de départ |
|---|---|---|---|
| `Etape_1_Bruits` | `E1_Exemple_Noise`, `_Voronoi`, `_Wave`, `_Gabor` | Plaquettes de 0,080 × 0,080 × 0,004 m, Bevel 0,0015 m à 3 segments | Terminées : chaque texture en aperçu, relié à *Surface* (réglages de 1.1 à 1.4) |
| | `E1_Pratique` | Même plaquette | `E1_Pratique` : Principled gris par défaut |
| | `E1_Defi_A`, `_B`, `_C` | Même plaquette | Principled par défaut |
| `Etape_2_Remapper` | `E2_Exemple_Coque` | Échantillon de coque de siège : une plaque de 0,200 × 0,240 m cintrée (Simple Deform, *Bend* 30°), Solidify 0,004 m | Terminée : moucheté de 2.1 |
| | `E2_Pratique_Mouchete` | Plaquette | Principled, *Roughness* 0,5 |
| | `E2_Pratique_Planche` | Plaquette | #151515 |
| | `E2_Defi` | Plaquette | Principled, *Roughness* 0,5 |
| `Etape_3_Masques` | `E3_Exemple_Main_courante` | Tube Ø 0,032 × 0,300 m, couché sur X (rotation Y 90°, non appliquée), Bevel 0,002 m | Terminée : patine avec extrémités (3.4) |
| | `E3_Pratique_Main_courante` | Même tube | Laiton #E0C27A, *Metallic* 1, *Roughness* 0,25 |
| | `E3_Defi_Main_courante` | Même tube | Inox #C8C8C6, *Metallic* 1, *Roughness* 0,15 |
| `Etape_4_Relief` | `E4_Exemple_Coque` | Demi-ellipsoïde de 0,220 × 0,140 × 0,120 m (UV Sphere 96 × 48 aplatie, échelle appliquée) | Terminée : laque à peau d'orange (4.2) |
| | `E4_Pratique_Boitier` | Pavé de 0,120 × 0,080 × 0,030 m, Bevel 0,003 m à 4 segments | #D9DADB, *Metallic* 1, *Roughness* 0,45 |
| | `E4_Pratique_Coque` | Comme l'exemple | Laque #A3161A, *Roughness* 0,4, *Coat* 1 / 0,03 |
| | `E4_Defi_Coque` | Comme l'exemple | #1C3F7A, *Metallic* 1, *Roughness* 0,35, *Coat* 1 / 0,02 |
| `Etape_5_Usure` | `E5_Exemple_Coffret` et `E5_Exemple_Plinthe` | Pavé de 0,200 × 0,120 × 0,080 m, Bevel 0,004 m à 4 segments, sur une plinthe de 0,240 × 0,160 × 0,020 m | Terminés : usure prismatique et saleté |
| | `E5_Pratique_Socle` | Cylindre Ø 0,180 × 0,025 m, 64 côtés, Bevel 0,003 m à 4 segments | #2F5D3A, *Roughness* 0,45 |
| | `E5_Pratique_Marchepied` | Plaque de 0,200 × 0,200 × 0,010 m et trois nervures de 0,012 × 0,180 × 0,012 m (objets séparés, même matière), Bevel 0,002 m | #9A9C9E, *Metallic* 1, *Roughness* 0,35 |
| | `E5_Pratique_Main_courante` | Tube de l'étape 3 | #C8C8C6, *Metallic* 1, *Roughness* 0,08 |
| | `E5_Pratique_Console` | Pavé de 0,200 × 0,120 × 0,010 m, Bevel 0,002 m | #0A0A0A, *Roughness* 0,3, *Coat* 1 / 0,02 |
| | `E5_Defi_Coffret` et `E5_Defi_Plinthe` | Comme l'exemple | #2F5D3A ; plinthe #4A4D50 |
| `Etape_6_Motifs` | `E6_Exemple_Dalle` | Pavé de 0,120 × 0,080 × 0,006 m | Terminée : pastilles |
| | `E6_Pratique_Grille` et `E6_Fond` | Plaque de 0,120 × 0,080 × 0,0015 m ; un fond coloré 0,030 m dessous, pour voir à travers | #B8B9BA, *Metallic* 1, *Roughness* 0,35 ; fond #D04010 |
| | `E6_Pratique_Accoudoir` | Pavé de 0,300 × 0,060 × 0,050 m, Bevel 0,008 m à 4 segments | #1E1B19, *Roughness* 0,55 |
| | `E6_Pratique_Assise` | Pavé de 0,120 × 0,120 × 0,040 m, Bevel 0,010 m à 6 segments | Principled, *Roughness* 0,8 |
| | `E6_Defi_Molette` | Cylindre Ø 0,030 × 0,040 m, 128 côtés, Bevel 0,001 m | #C8C8C6, *Metallic* 1, *Roughness* 0,35 |
| | `E6_Defi_Panneau` | Panneau de 0,300 × 0,200 m, galbé dans le maillage lui-même (rayon 0,6 m), à plat dans son plan XY local, Solidify 0,002 m | Principled, *Roughness* 0,3, *Coat* 1 / 0,02 |
| `Etape_7_Groupes` | `E7_Exemple_Grain` | Plaquette | Terminée : groupe `PRC_Grain_Fin` (entrées *Échelle* 1500 et *Relief* 0,05, sortie *Normal*) vers le Principled |
| | `E7_Pratique_Socle` | Cylindre de 5.1 | Terminée jusqu'au masque de 5.1 : la chaîne des bords usés, avec son *Color Ramp* à trois curseurs |
| `Lampe_defi` | La lampe | Copie de la collection *Lampe* de la fiche A2, décalée en Y | Les matières du coloris A, suffixées `_defi` (`Structure_Vert_defi`…), pour ne pas entrer en conflit avec une lampe que l'apprenant ajouterait par Append |

**Collection masquée « Corrigé défi procédural »,** décalée de X + 2,4 m. Elle contient une sous-collection par étape, de « Corrigé étape 1 » à « Corrigé étape 7 ».
- Chaque sous-collection contient la copie terminée de chaque pièce *Pratique* et *Defi* de son étape. Les objets et les matières portent le suffixe `_corrige`, comme au chapitre 3.
- Les valeurs sont celles des recettes de ce plan, rendues sous EEVEE.
- « Corrigé étape 7 » contient aussi :
  - les groupes `PRC_Usure_Bords_corrige`, avec son entrée *Axe*, et `PRC_Tole_Perforee_corrige` ;
  - `Lampe_defi_corrige`, la lampe d'atelier.

  Ces groupes ne sont pas marqués comme actifs. Ils apparaissent toutefois dans `Maj + A > Group`, qui liste tous les groupes du fichier : le LISEZ-MOI le signale.
- Les objets d'exemple ne sont pas des corrigés : ils restent visibles et s'observent librement.

**Vue d'ouverture :**
- espace *Shading* ;
- vue 3D en *Material Preview*, image *studio*, de trois quarts plongeante sur les rangées 1 et 2. Les collections des étapes 3 à 7 et `Lampe_defi` sont masquées, pour un premier affichage rapide ;
- `E1_Pratique` est sélectionné, et sa matière est visible dans le Shader Editor ;
- le LISEZ-MOI est en bas.

**Texte du LISEZ-MOI :**

```
PRC02 · Chapitre 3 · Défi facultatif, hors programme : matières procédurales
Enregistrez ce fichier sous defi_procedural_v001.blend. Suivez la section 4 du chapitre 3 dans l'application.
Corrigés : collection « Corrigé défi procédural » (œil fermé), une sous-collection par étape, suffixe _corrige.
Affichez seulement la collection de l'étape en cours : l'affichage reste fluide.
Aperçu d'un nœud : Ctrl + Maj + clic sur le nœud. Retour : Ctrl + Maj + clic sur le Principled BSDF.
Valeurs indicatives, vérifiées sous EEVEE : retouchez-les à l'œil. Le relief se règle avec Strength du Bump.

PALIER 1
1 · Bruits : Noise (Scale 100), Voronoi (Distance to Edge), Wave (Rings, Z), Gabor (Frequency 6).
2 · Remapper : Color Ramp (Constant, curseur à 0,74), Map Range (To 0,08 à 0,35 vers Roughness),
    Math (Greater Than 0,74).
3 · Masques : un masque, trois Mix (Base Color, Metallic, Roughness).
    Patine aux extrémités : Separate XYZ (Z) > Absolute > Map Range > Multiply.
4 · Relief : Bump A > Normal du Bump B > Principled. Peau d'orange : Bump (Strength 0,15) > Coat Normal.

PALIER 2
5 · Usure : Texture Coordinate > Normal > Separate XYZ (Z) > Absolute > Color Ramp (0,10 / 0,50 / 0,90).
    Saleté : Ambient Occlusion (Distance 20mm) > Color Ramp (0,85 / 0,99).
    Rayures : Mapping (Z 0,02) > Noise (2000) > Color Ramp (0,68 / 0,70) > Roughness.
    Traces : Noise (25) > Map Range > Coat Roughness.
6 · Motifs : tôle perforée = Voronoi 2D (Scale 250, Randomness 0) > Greater Than 0,3 > Alpha.
    Cuir, tissu, et en défi moletage et carbone : recettes dans l'application.
7 · Groupes : remplacez le Color Ramp par Math et Map Range, puis Ctrl + G, Tab, barre latérale N > Group.
    Défi final : la collection Lampe_defi (rendez-la visible).
Les groupes « _corrige » de Maj + A > Group sont ceux du corrigé.
La case Raytracing est décochée : l'ampoule ne montre que l'environnement, c'est normal.
```

**Corrigé attendu, contrôles :**
- chaque pièce *Pratique* et *Defi* a son double terminé, suffixé `_corrige` ;
- le rendu de chaque corrigé correspond au « Rendu attendu » de sa recette ;
- `PRC_Usure_Bords_corrige` expose *Axe*, *Largeur*, *Quantité* et *Échelle du bruit* ;
- `PRC_Tole_Perforee_corrige` perce des trous de 2,4 mm au pas de 4 mm avec ses valeurs par défaut.

**Dans l'application :** un module ressource en tête de la section 4. Le fichier `.blend` se distribue seul : sa seule image est empaquetée, et il n'a pas de catalogue d'actifs à accompagner.

## Captures Blender à prévoir

Une capture pour chaque nœud, menu ou panneau cité : 49 figures, de 3.48 à 3.96, numérotées dans l'ordre du texte (le chapitre 3 s'arrête à 3.47). Trois figures du chapitre 3 sont réutilisées : 3.13 (*Render Method*, rubrique *Settings* de l'onglet *Material*), 3.20 (le menu *Add*) et 3.24 (*Mapping* et le brossé). L'échelle est celle de l'affichage dans l'application, calculée par `tool/exercices_ch3/echelles.py` : la plus basse vaut 0,51.

| Figure | Fichier | Ce qu'elle montre | Format | Échelle |
|---|---|---|---|---|
| 3.48 | `procedural_challenge_overview_blender.jpg` | Le banc d'échantillons du défi, terminé : une rangée par étape, des bruits aux groupes de nœuds, et la lampe usée du défi final. | Pleine largeur | 0,66 |
| 3.49 | `shader_add_submenus_blender.jpg` | Quatre sous-menus de Maj + A dans Blender 5.2 : Color, Utilities > Math, Utilities > Vector et Displacement. | Pleine largeur | 0,75 |
| 3.50 | `node_preview_ctrl_shift_click_blender.jpg` | L'aperçu par Ctrl + Maj + clic : la sortie Factor du Noise reliée directement à Surface. Le Principled BSDF reste en place, sans lien. À droite, la plaquette en niveaux de gris. | Pleine largeur | 0,51 |
| 3.51 | `noise_texture_node_blender.jpg` | Le nœud Noise Texture et le menu de son type : fBM par défaut, Multifractal, Ridged Multifractal, Hybrid Multifractal, Hetero Terrain. | Côte à côte | 0,64 |
| 3.52 | `noise_settings_comparison_blender.jpg` | Le Noise sur une plaquette de 80 mm : Scale 5 par défaut, Scale 100, Detail 8, Distortion 2, puis Ridged Multifractal. | Pleine largeur | 0,51 |
| 3.53 | `voronoi_texture_node_blender.jpg` | Le nœud Voronoi Texture et le menu de ses réglages : F1, F2, Smooth F1, Distance to Edge, N-Sphere Radius. | Côte à côte | 0,55 |
| 3.54 | `voronoi_comparison_blender.jpg` | Le Voronoi à Scale 100 : F1, Distance to Edge, puis la sortie Color. | Pleine largeur | 0,66 |
| 3.55 | `wave_texture_node_blender.jpg` | Le nœud Wave Texture : Bands ou Rings, la direction, le profil Sine, puis Scale, Distortion et Detail. | Côte à côte | 0,59 |
| 3.56 | `wave_comparison_blender.jpg` | Le Wave à Scale 40 : des bandes, des bandes ondulées, puis des anneaux. | Pleine largeur | 0,66 |
| 3.57 | `gabor_texture_node_blender.jpg` | Le nœud Gabor Texture : le type 2D ou 3D, Scale, Frequency, Anisotropy et Orientation. | Côte à côte | 0,65 |
| 3.58 | `gabor_comparison_blender.jpg` | Le Gabor à Scale 100 : par défaut, Frequency 6, puis Anisotropy 0. | Pleine largeur | 0,66 |
| 3.59 | `step1_target_tiles_blender.jpg` | Le petit défi de l'étape 1 : les plaquettes cibles A, B et C, de gauche à droite. | Pleine largeur | 0,66 |
| 3.60 | `color_ramp_node_blender.jpg` | Le nœud Color Ramp et le menu de son interpolation : Ease, Cardinal, Linear, B-Spline, Constant. | Côte à côte | 0,57 |
| 3.61 | `color_ramp_comparison_blender.jpg` | Le bruit brut, puis contrasté par deux curseurs rapprochés, puis en interpolation Constant. | Pleine largeur | 0,66 |
| 3.62 | `speckled_plastic_blender.jpg` | La chaîne du moucheté : Texture Coordinate, Noise (Scale 1500, Detail 0), Color Ramp en Constant, Base Color. À droite, la coque de siège. | Pleine largeur | 0,51 |
| 3.63 | `map_range_node_blender.jpg` | Le nœud Map Range : From Min et From Max, To Min et To Max, la case Clamp et le menu d'interpolation. | Côte à côte | 0,64 |
| 3.64 | `uneven_gloss_dashboard_blender.jpg` | La chaîne de la brillance irrégulière : Noise, Map Range (0,35 à 0,65 vers 0,08 à 0,35), Roughness. À droite, la planche de bord. | Pleine largeur | 0,51 |
| 3.65 | `math_node_operations_blender.jpg` | Le nœud Math et le menu de ses opérations : Add, Multiply, Power, Absolute, Minimum, Maximum, Less Than, Greater Than, Floor… La liste continue plus bas, avec Floored Modulo et Ping-Pong. | Pleine largeur | 0,64 |
| 3.66 | `mix_color_and_float_nodes_blender.jpg` | Le nœud Mix Color (Factor, A, B et le menu de mélange), puis le nœud Mix en Float. | Côte à côte | 0,51 |
| 3.67 | `separate_xyz_node_blender.jpg` | Le nœud Separate XYZ : une entrée Vector, trois sorties X, Y et Z. | Côte à côte | 1,22 |
| 3.68 | `one_mask_three_mixes_blender.jpg` | La chaîne du laiton patiné : le masque de patine (Noise, Color Ramp) multiplié par le masque des extrémités (Separate XYZ, Absolute, Map Range), puis trois Mix vers Base Color, Metallic et Roughness. | Pleine largeur | 0,62 |
| 3.69 | `patina_handrail_comparison_blender.jpg` | La main courante patinée partout, puis seulement aux extrémités. | Pleine largeur | 0,71 |
| 3.70 | `bump_node_settings_blender.jpg` | Le nœud Bump : la case Invert, Strength, Distance, Filter Width, puis les entrées Height et Normal. | Côte à côte | 0,82 |
| 3.71 | `chained_bump_nodes_blender.jpg` | Deux Bump chaînés : le Bump A (grain fin) entre dans l'entrée Normal du Bump B (ondulations), qui va au Principled. À droite, le boîtier martelé. | Pleine largeur | 0,51 |
| 3.72 | `principled_coat_normal_blender.jpg` | La peau d'orange : Noise (Scale 600, Detail 1), Bump (Strength 0,15), puis l'entrée Normal de la rubrique Coat, dépliée, du Principled BSDF. | Pleine largeur | 0,69 |
| 3.73 | `orange_peel_comparison_blender.jpg` | Le reflet sur la coque laquée : lisse, puis avec la peau d'orange à Strength 0,15, puis à 0,3. | Pleine largeur | 0,51 |
| 3.74 | `edge_wear_normal_chain_blender.jpg` | La chaîne des bords usés : Texture Coordinate (Normal), Separate XYZ, Absolute, Color Ramp à trois curseurs, multiplié par un Noise, puis Map Range, vers Mix Color, Metallic et Roughness. | Pleine largeur | 0,63 |
| 3.75 | `vector_math_node_blender.jpg` | Le nœud Vector Math, ici en Absolute ; son menu propose aussi Dot Product. | Côte à côte | 1,24 |
| 3.76 | `edge_wear_mask_comparison_blender.jpg` | Le masque des arêtes en aperçu sur le socle, le socle usé, puis le boîtier usé par la variante prismatique, et le faux positif de cette variante sur un cylindre. | Pleine largeur | 0,51 |
| 3.77 | `ambient_occlusion_node_blender.jpg` | Le nœud Ambient Occlusion : les sorties Color et AO, les entrées Distance et Normal, les réglages Samples, Inside et Only Local. | Côte à côte | 0,72 |
| 3.78 | `dirt_crevices_comparison_blender.jpg` | Le marchepied : l'occlusion brute, presque blanche ; la même, resserrée par le Color Ramp ; puis la saleté. | Pleine largeur | 0,54 |
| 3.79 | `scratches_handrail_blender.jpg` | Le masque des rayures en aperçu, puis la main courante en inox rayé. | Pleine largeur | 0,71 |
| 3.80 | `fingerprints_piano_black_blender.jpg` | La console noir piano, neuve, puis avec des traces de doigts dans le reflet du vernis. | Pleine largeur | 0,64 |
| 3.81 | `procedural_patterns_overview_blender.jpg` | Les motifs de l'étape 6 : la dalle à pastilles, la tôle perforée, le cuir grainé, le tissu de siège, puis, en défi, le moletage et le carbone sergé. | Pleine largeur | 0,53 |
| 3.82 | `perforated_sheet_alpha_blender.jpg` | La chaîne de la tôle perforée : Voronoi 2D (Scale 250, Randomness 0), Greater Than 0,3, Alpha. À droite, la grille au-dessus de son fond orange. | Pleine largeur | 0,51 |
| 3.83 | `leather_grain_procedural_blender.jpg` | La chaîne du cuir : Voronoi (Distance to Edge, Scale 500), Color Ramp, Bump. À droite, l'accoudoir grainé. | Pleine largeur | 0,51 |
| 3.84 | `checker_texture_node_blender.jpg` | Le nœud Checker Texture : Color1, Color2, Scale, et les sorties Color et Factor. | Côte à côte | 0,88 |
| 3.85 | `seat_fabric_weave_blender.jpg` | La chaîne du tissu : un Checker (Scale 500) choisit, case par case, entre deux Wave (Scale 157) en X et en Y ; le résultat va au Bump et à Mix Color. | Pleine largeur | 0,63 |
| 3.86 | `gradient_texture_radial_blender.jpg` | Le nœud Gradient Texture et le menu de son type, avec Radial. | Côte à côte | 0,65 |
| 3.87 | `knurling_procedural_blender.jpg` | La chaîne du moletage : Gradient Radial et Separate XYZ donnent u et v ; Add, Subtract, deux Ping-Pong et Minimum dessinent les pointes ; puis Bump. | Pleine largeur | 0,51 |
| 3.88 | `carbon_twill_procedural_blender.jpg` | La chaîne du carbone sergé : les numéros de case (Multiply, Floor, Add, Floored Modulo, Less Than) choisissent entre deux Wave, vers Bump et Mix Color. | Pleine largeur | 0,54 |
| 3.89 | `node_make_group_menu_blender.jpg` | Le menu Node du Shader Editor : Make Group (Ctrl + G) et Ungroup. | Côte à côte | 1,08 |
| 3.90 | `node_group_inside_blender.jpg` | L'intérieur du groupe PRC_Usure_Bords : Group Input à gauche, avec Axe, Largeur, Quantité et Échelle du bruit ; le masque calculé en chiffres ; Group Output à droite. | Pleine largeur | 0,52 |
| 3.91 | `node_group_sidebar_interface_blender.jpg` | La barre latérale du Shader Editor, onglet Group : le nom du groupe, sa description, la liste des entrées et des sorties, et les réglages de la prise Largeur. | Côte à côte | 0,56 |
| 3.92 | `add_menu_group_list_blender.jpg` | Maj + A > Group : New Group, puis les groupes du fichier. | Côte à côte | 1,49 |
| 3.93 | `node_group_in_use_blender.jpg` | Le groupe en service sur le socle : un seul nœud, avec ses paramètres Largeur, Quantité et Échelle du bruit, relié à Mix Color et Metallic. | Pleine largeur | 0,67 |
| 3.94 | `node_frame_label_blender.jpg` | Option : les nœuds du masque d'usure encadrés dans un Frame intitulé « Masque d'usure » ; à droite, son Label dans l'onglet Node de la barre latérale. | Pleine largeur | 0,58 |
| 3.95 | `node_group_mark_as_asset_blender.jpg` | Option : l'Outliner en mode Blender File, rubrique Node Groups, et le clic droit sur le groupe, avec Mark as Asset. | Côte à côte | 0,56 |
| 3.96 | `workshop_lamp_wear_blender.jpg` | Le défi final : la lampe neuve, la lampe d'atelier, puis son socle vu de près, à l'arête usée jusqu'à l'aluminium. | Pleine largeur | 0,59 |

**Méthode :** celle du chapitre 3, dans une fenêtre Blender séparée (1600 × 960, *Resolution Scale* 1,25), avec une configuration temporaire et le verrou `tool/production/capture.lock`.
- **Les captures d'interface** : `tool/exercices_ch3/captures_defi.py`. Les bandes de nœuds sont prises dans le Shader Editor agrandi, sur une copie de la matière réduite aux nœuds montrés ; les menus d'un nœud s'ouvrent avec `wm.context_menu_enum` et s'isolent par différence.
- **Les rendus des planches** : `tool/exercices_ch3/rendus_figures_defi.py`, sous EEVEE, avec l'image *studio* de *Material Preview* et un fond uni.
- **Le recadrage** : `tool/exercices_ch3/recadrer_defi.py`, qui reprend les outils de `recadrer.py`. Les figures pleine largeur font au plus 1400 px de large.

## Comment le complément s'insère dans l'application

Rien n'est codé à ce stade. Voici ce que la session principale aura à faire.

- **Le texte source :** la section `## 4. Défi facultatif · Matières procédurales`, à la fin du fichier Markdown du chapitre 3, au format de `writer_guide.md`. Elle vient après la section 3 et avant le module de fin du chapitre, s'il y en a un.
- **Le registre :** dans `lib/core/data/course_data.dart`, chapitre 3, un quatrième point : `ChapterPoint(label: 'Défi facultatif : matières procédurales', targetModuleId: 'ch3_sec4_title')`. Il apparaît sur l'écran Programme, et son libellé dit qu'il est facultatif.
- **L'encart d'introduction** (`ch3_sec4_info_intro`) dit, en phrases courtes :
  - ce complément est facultatif et n'est pas prévu au programme de base. Il ajoute des connaissances utiles, hors de la formation initiale ;
  - il s'adresse à ceux qui sont à l'aise avec les contenus de base, ou qui maîtrisent déjà ces sujets ;
  - il se fait à la suite des parties de base, s'il reste du temps, ou à leur place ;
  - pour les prérequis, les trois quiz de la section 2 servent de test d'entrée ;
  - celui qui remplace des parties de base reprend le chapitre 4 par l'une des trois voies de « Quand et comment ». C'est une option, pas une obligation.
- **Les modules,** dans `chapter3Modules` de `lib/core/data/mock_chapters_data.dart`. Aucun nouveau type de module n'est nécessaire.

| Contenu | Module | Identifiants |
|---|---|---|
| Titre de la section | `TitleModule` | `ch3_sec4_title`, « 4. Défi facultatif · Matières procédurales » |
| Les deux paliers | `TextModule` | `ch3_sec4_palier1`, `ch3_sec4_palier2` |
| Statut facultatif, pour qui, quand, prérequis, reprise au chapitre 4 | `InfoModule` de type `info` (NOTE) | `ch3_sec4_info_intro` |
| Le fichier | `ResourceModule` | `ch3_sec4_res1`, `PRC02_ch3_defi_procedural.blend` |
| Ce qu'EEVEE ne fait pas | `InfoModule` de type `info` (encart IMPORTANT, converti comme une note par `md_vers_dart.py`, comme au chapitre 3) | `ch3_sec4_info_eevee` |
| Chaque étape : notion, exemple | `TextModule` avec sous-titre (« Étape 1 · Lire les textures de bruit ») | `ch3_sec4_e1_txt1`… |
| Chaque nœud ou menu | `SideBySideModule` | `ch3_sec4_e1_side1`… |
| Chaque recette | `ListModule` numéroté (« Recette · … ») : un élément par ligne du tableau, avec le menu, les réglages et le lien | `ch3_sec4_e1_list1`… |
| Planches, chaînes, comparaisons | `FullMediaModule` | `ch3_sec4_e1_media1`… |
| Rendu attendu, à retenir | `TextModule` | |
| Erreurs fréquentes | `InfoModule` de type `warning` | `ch3_sec4_e1_warn1`… |
| Notes (*Normal Map*, occlusion, *Mix Shader*) | `InfoModule` de type `info` | |
| Petit défi, défi final | `InfoModule` de type `challenge` (CAUTION) | `ch3_sec4_e1_chal1`… |
| Quiz | `QuizModule` | `ch3_sec4_quiz1` à `quiz9` |

- **Les paliers :** un `TextModule` court ouvre chaque palier : « Palier 1 · Lire et combiner », « Palier 2 · Usure, motifs, groupes ». Il rappelle la durée et le point d'arrêt.
- **Les signets et la recherche** reprennent les modules automatiquement, comme pour les autres sections.
- **Le style :** vouvoiement, phrases courtes, réglages présentés comme des options et des valeurs de départ, aucun emoji, aucune grille d'autoévaluation.

## Coordination avec le chapitre 3 et les autres plans

Ce plan ne modifie aucun plan existant. Les points ci-dessous sont à reporter par la session principale, sauf ceux marqués « corrigé ».

1. **Les menus de Blender 5.2 dans le plan du chapitre 3 (corrigé le 18 novembre 2026 par la session principale).** Dans Blender 5.2, il n'y a plus de catégorie *Vector* au premier niveau : *Bump* est sous `Maj + A > Displacement`, et *Mapping* sous `Maj + A > Utilities > Vector`. Vérifié dans `node_add_menu_shader.py` de Blender 5.2.1. Reste à appliquer au contenu du chapitre 3, quand il sera rédigé.
2. **« Fac » devient « Factor » (corrigé le 18 novembre 2026 par la session principale).** Dans Blender 5.2, la sortie de *Noise Texture* et l'entrée du *Color Ramp* s'appellent *Factor*.
3. **L'aperçu natif.** `Ctrl + Maj + clic` sur un nœud est natif dans Blender 5.2, sans Node Wrangler. Le chapitre 3 peut le citer en astuce à 1:35.
4. **Les renvois vers le complément.** L'ouverture du chapitre 3 peut signaler le défi facultatif en une phrase (voir « Quand et comment »). La rubrique « Pour ceux qui avancent vite » et la ligne « Pour aller plus loin » du bilan peuvent renvoyer à la section 4. Le défi ★★ « peinture métallisée décortiquée » rejoint le petit défi de l'étape 4.
5. **La dépendance de construction.** `Lampe_defi` vient de la fiche A2 (`PRC02_ch3_lampe_habillage.blend`) : le fichier du complément se construit après elle.
6. **Le chapitre 4.** Le complément ne touche ni à la lampe qui part au chapitre 4, ni à l'éclairage, ni au rendu. Ses matières fonctionnent sous EEVEE ; un apprenant qui en garde une sur sa lampe la retrouve au chapitre 4. L'apprenant qui a fait le défi à la place des parties de base reprend le chapitre 4 par l'une des trois voies de « Quand et comment ». Elles sont toutes compatibles avec le plan du chapitre 4 : son fichier de secours, l'Append de la collection *Lampe* (depuis la fiche A2 ou depuis sa propre lampe). Le chapitre 4 n'a rien à changer. Seul le palier « gamme » de son atelier suppose `Lampe_coloris_B`, présente dans le fichier de secours et dans la fiche A2.

## Contrôle face aux critères du découpage

| Critère | Comment le plan y répond |
|---|---|
| 1 · Durée | Hors minutage : le complément ne prend aucune minute au chapitre 3, et le formateur ne fait aucune démonstration. L'apprenant le fait à la suite des parties de base, s'il lui reste du temps, ou à leur place ; le reste se fait après la séance. |
| 2 · Périmètre | Complément facultatif, hors programme de base : il ajoute des connaissances utiles, non prévues dans la formation initiale. Il est signalé comme tel sur l'écran Programme (« Défi facultatif : matières procédurales »), dans le titre de la section et dans son introduction. Il prolonge le point 2 du programme (finitions CMF), dans l'ancre `ch3_sec4_title`, sans rien exiger des chapitres suivants. Il ne touche ni à l'éclairage, ni à la caméra, ni au rendu, qui appartiennent au chapitre 4. |
| 3 · Pas de redite | *Noise*, *Object*, *Bump*, *Mapping*, *Coat*, *Alpha*, *Mark as Asset* sont réemployés, pas réexpliqués (tableau des prérequis). |
| 4 · Continuité | Point de départ : les acquis de la séquence 1:50 du chapitre 3, suivie ou déjà maîtrisés. La lampe du défi final est une copie : `lampe_habillage_v002.blend` et le fichier du chapitre 4 ne changent pas. L'apprenant qui remplace des parties de base reprend le chapitre 4 par l'une des trois voies de « Quand et comment » : fichier de secours, fiche A2, ou sa propre lampe sous la collection *Lampe*. |
| 5 · Fichiers | Un seul fichier de travail. Les corrigés sont dans la collection masquée « Corrigé défi procédural », signalée en une ligne dans le LISEZ-MOI. Aucun fichier séparé. Le fichier s'ouvre seul : image empaquetée, aucun chemin. |
| 7 · Progression | Les prérequis sont vérifiés à l'entrée par les trois quiz de la section 2 du chapitre 3. Une notion par étape, des nœuds introduits un par un. Chaque étape suit le même ordre : exemple, pratique guidée, petit défi. Un point d'arrêt et des quiz à la fin de chaque palier. Les sous-étapes difficiles (moletage, carbone, axe au choix, tôle en millimètres) sont marquées ★ et restent facultatives. |

## Points techniques vérifiés dans Blender 5.2.1 LTS

Vérifiés le 18 novembre 2026, dans un Blender lancé en arrière-plan (`-b --factory-startup`), sans toucher à la session du formateur. Chaque recette a été rendue sous EEVEE, sous l'image *studio*, à l'échelle réelle.

- **Libellés et réglages par défaut :**
  - *Noise* : *Scale* 5, *Detail* 2, *Roughness* 0,5, *Lacunarity* 2, *Distortion* 0, *Normalize* coché. Types *fBM* (défaut), *Multifractal*, *Ridged Multifractal*, *Hybrid Multifractal*, *Hetero Terrain*. Sorties *Factor* et *Color*.
  - *Voronoi* : *Scale* 5, *Detail* 0, *Randomness* 1. Réglages *F1*, *F2*, *Smooth F1*, *Distance to Edge*, *N-Sphere Radius*. Sorties *Distance*, *Color*, *Position*.
  - *Wave* : *Bands*/*Rings* ; directions *X*, *Y*, *Z*, *Diagonal* ou *Spherical* ; profils *Sine*, *Saw*, *Triangle*.
  - *Gabor* : *Scale* 5, *Frequency* 2, *Anisotropy* 1, *Orientation* 0,785 ; types *2D* et *3D* ; sorties *Value*, *Phase*, *Intensity*.
  - *Map Range* : *Clamp* coché ; interpolations *Linear*, *Stepped Linear*, *Smooth Step*, *Smoother Step*.
  - *Mix* : types *Float*, *Vector*, *Color*, *Rotation*.
  - *Bump* : *Strength* 1, *Distance* 0,001, *Filter Width* 0,1, case *Invert*.
  - *Ambient Occlusion* : *Distance* 1, *Samples* 16, *Inside*, *Only Local*.
- **Le menu `Maj + A` :** tableau « Les menus du Shader Editor dans Blender 5.2 », relevé dans `scripts/startup/bl_ui/node_add_menu_shader.py`. `Maj + A > Group` liste *New Group* et tous les groupes du fichier.
- **Les raccourcis** (fichier `blender_default.py`) :
  - `Ctrl + Maj + clic` : *Connect to Output*, l'aperçu natif ;
  - `Ctrl + G` : *Make Group* ; `Ctrl + Alt + G` : *Ungroup* ; `Tab` : entrer dans un groupe ou en sortir ;
  - `Ctrl + J` : *Join Nodes* dans un *Frame* ;
  - `Maj + clic droit` glissé : *Reroute* ; `Ctrl + clic droit` glissé : couper des liens.
- **L'aperçu :** une sortie de couleur ou de valeur reliée à *Surface* s'affiche sous EEVEE, sans réglage.
- **Les limites d'EEVEE** (manuel, *Nodes Support*) :
  - *Pointiness* et *Random Per Island* ne sont pas pris en charge ;
  - le nœud *Bevel* n'est pas pris en charge ;
  - *Only Local* de l'*Ambient Occlusion* n'est pas pris en charge ;
  - *Anisotropic* n'est pas pris en charge ;
  - *Sheen* n'est qu'approché ;
  - *Gabor* fonctionne.
- **L'occlusion sous EEVEE :**
  - *Inside* ne donne presque aucun signal sur les arêtes à l'échelle de la lampe ;
  - sans *Inside*, les creux se lisent, mais les valeurs restent proches de 1. Une rampe de 0,85 à 0,99 les rend nettes ;
  - le résultat est le même avec ou sans *Raytracing*, et avec une précision de *Fast GI* augmentée.
- **La normale :** les bords usés par la normale fonctionnent sur un cylindre (variante Z) et sur un boîtier (variante prismatique), avec un Bevel de 3 à 4 mm à 4 segments. La variante prismatique use à tort le flanc d'un cylindre.
- **Alpha :** *Render Method* vaut *Dithered* par défaut, et la tôle perforée par *Alpha* s'affiche sans autre réglage, ombre percée comprise.
- **Les groupes :** l'interface d'un groupe accepte des entrées *Vector* et *Float* au sous-type *Factor*, avec *Min* et *Max*. `PRC_Usure_Bords` (avec *Axe*) et `PRC_Tole_Perforee` (en millimètres) ont été construits et rendus.

À vérifier pendant la construction du fichier :
- l'occlusion en *Material Preview*, et pas seulement en rendu, ainsi que la distance de `5mm` pour les lamelles de la grille de la lampe ;
- un groupe marqué comme actif dans *Current File* apparaît-il dans `Maj + A`, rangé par catalogue ?
- *Gabor* en type *3D* sur une pièce en volume ;
- le temps de compilation de *Material Preview* avec toutes les collections affichées, sur le poste le plus modeste de la salle ;

## Décisions du formateur, 18 novembre 2026

1. **Forme :** une section 4 du chapitre 3 dans l'application, « Défi facultatif · Matières procédurales », avec son ancre et un quatrième point au programme, « Défi facultatif : matières procédurales ».
2. **Statut :** un complément facultatif, hors programme de base. Il ajoute des connaissances utiles, non prévues dans la formation initiale.
3. **Public et moment :** ceux qui parcourent vite les contenus de base parce qu'ils sont à l'aise, et ceux qui maîtrisent déjà ces sujets en début de formation. Ils font le défi à la suite des parties de base, s'il leur reste du temps, ou à leur place, pour un complément et des défis plus poussés. Celui qui remplace des parties de base reprend le chapitre 4 par l'une des trois voies prévues ; c'est une option, pas une obligation. Il n'y a aucune démonstration du formateur, et le minutage du chapitre 3 ne change pas.
4. **Périmètre :** 7 étapes en 2 paliers, de la lecture des bruits aux groupes de nœuds. *Normal Map* n'est cité qu'en note.
5. **Supports :** un fichier d'échantillons multisectoriels, et un défi final sur une copie de la lampe.

## Décisions de production, 19 novembre 2026

Prises par délégation pendant la production du fichier, du texte et des captures, à confirmer par le formateur.

1. **Le relief se règle avec *Strength*,** comme au chapitre 3 : *Distance* garde sa valeur par défaut (0,001). La correspondance *Strength* = *Distance* du plan × 1000 a été vérifiée en rendu EEVEE. Quatre reliefs fins disparaissaient avec elle, et sont renforcés :
   - la peau d'orange passe à 0,15 au lieu de 0,05 (0,3 pour le défaut visible) ;
   - le grain microbillé du boîtier passe à 0,1 au lieu de 0,03 ;
   - les paillettes de la peinture métallisée passent à 0,1 au lieu de 0,02 ;
   - la patine en relief passe à 0,1 au lieu de 0,05.

   Les autres valeurs suivent la correspondance : dalle 0,5, tissu 0,4, moletage 0,3, cuir 0,2, ondulations du boîtier 0,2, carbone 0,1, grain du groupe `PRC_Grain_Fin` 0,05. La *Distance* de l'*Ambient Occlusion* est une longueur : `20mm`, et `5mm` pour la grille de la lampe.
2. **L'orientation du Gabor.** Avec *Orientation* 0, les stries suivent l'axe Y (vérifié en rendu). Le brossé dans l'axe X demande 1,571 rad, soit 90° : la recette 1.4, le petit défi C et leurs corrigés suivent.
3. **L'option *Previews* est retirée.** Le menu *Overlays* du Shader Editor de Blender 5.2 ne la propose pas (vérifié par capture). La figure prévue est supprimée : le défi compte 49 figures, de 3.48 à 3.96.
4. **Deux figures passent en pleine largeur :** le relief du vernis (*Coat Normal*, 3.72) et le *Frame* (3.94). Leurs bandes de nœuds ne tiennent pas à l'échelle 0,5 dans 345 × 300 px.
5. **Les bandes de nœuds** sont capturées sur une copie de la matière, réduite aux nœuds montrés, et à un zoom proche de 1. Pour une chaîne longue, la figure montre la partie nouvelle : le masque des bords usés (3.74), le masque du sergé (3.88). Le texte décrit la suite, déjà vue. L'intérieur du groupe (3.90) montre ses nœuds de calcul repliés (`Ctrl + H`) et resserrés, avec *Group Input* et *Group Output* dépliés.
6. **Les figures pleine largeur font au plus 1400 px de large** (échelle 0,51), pour garder les nœuds lisibles à côté du rendu de la pièce.
7. **Le panneau carbone** est galbé dans le maillage lui-même, à plat dans son plan XY local. Construit debout puis couché, comme au chapitre 3, il aurait son axe X le long de sa normale, et la recette du sergé, qui lit X et Y, y dessinait des bandes.
8. **L'échantillon de coque de siège** mesure 200 × 240 mm, au lieu de 400 × 450 mm, à l'échelle des autres échantillons.
9. **Le tissu :** le *Checker* est rangé à part des deux *Wave*, pour une bande de nœuds moins haute. La recette ne change pas.
10. **Le défi final :** l'interrupteur, en ABS, n'est plus usé (son usure ne découvrirait aucun métal). Les articulations chromées s'usent jusqu'au laiton.
11. **Une image dans le fichier :** `grain_structure.png`, empaquetée, celle de la peinture structurée du socle de `Lampe_defi`. La lampe est construite par les scripts de la fiche A2 (`build_lampe.py`), avec ses matières du coloris A suffixées `_defi`.
12. **Le corrigé** est décalé de X + 2,4 m, les rangées étant plus longues que prévu. Il contient aussi `E4_Relief_Main_courante_corrige` (le masque en relief de 4.3), et `E7_Grille_mm_corrige` avec son fond (la tôle en millimètres du défi ★★).
13. **Les nœuds du fichier** sont rangés en colonnes serrées, sans chevauchement, pour que les exemples et les corrigés se lisent dès leur ouverture. La rubrique *Coat* est dépliée sur les matières dont le vernis porte la recette.
14. **Les captures du groupe** montrent les noms que l'apprenant donne, `PRC_Usure_Bords` et `PRC_Tole_Perforee` : les groupes du corrigé sont renommés en mémoire pendant la capture, le fichier n'est pas modifié.
15. **La barre latérale, onglet *Group* :** la liste des entrées et des sorties s'appelle *Group Sockets* dans Blender 5.2 (vérifié par capture). Le texte le dit.
16. **Les scripts du chapitre 3 touchés :**
    - `finish_ui.py` traite aussi ce fichier dans l'espace *Shading* ;
    - `rendus_controle.py` a ses cadrages ;
    - `recadrer.py` peut être importé sans rien recadrer ;
    - `md_vers_dart.py` donne les identifiants de ce plan à la section 4.

    Les identifiants des sections 1 à 3 et `ch3_atelier` ne changent pas (vérifié).
