# [SU] Design & visualisation temps réel avec Blender

Support de formation interactif de la formation **PRC02 — Design & visualisation temps réel avec Blender** de VIV Formation : une application de bureau Windows (Flutter) qui accompagne les participants pendant et après la session.

Le projet reprend le format validé des supports précédents (dépôt modèle : `M-Juguet/VIV_TrainingResource_BlenderImagery`). Il en garde la structure, l'arborescence et le fonctionnement, et passe de la charte VIVProd au design system **VIV Formation**.

## Ce que contient l'application

- **Tableau de bord** : progression, accès direct au prochain chapitre, dernier signet, liens utiles.
- **Programme** : chapitres de la formation et points clés, avec un lien direct vers chaque section.
- **Les bases** (Basics 101 à 103) : initiation au logiciel, pour un public qui découvre Blender.
- **Formation** (chapitres 1 à 4), alignés sur les quatre compétences visées :
  1. Environnement de travail et blocage de volumes
  2. Modélisation non destructive : modificateurs et courbes
  3. Matières et finitions réalistes sans dépliage UV
  4. Visualisation temps réel et visuels de présentation avec EEVEE
- **Signets**, **recherche plein texte**, **quiz d'auto-évaluation**, **mises à jour automatiques** depuis les releases GitHub.

Un chapitre sans contenu s'affiche « en préparation » avec ses points clés.

## Arborescence

```text
lib/
  core/
    data/
      course_data.dart          # Registre des chapitres : titres, objectifs, icônes, routes (source unique)
      mock_chapters_data.dart   # Contenu des chapitres (listes de modules)
    models/                     # Modules de contenu (texte, image, encart, quiz, ressource…)
    router/                     # GoRouter : une branche par écran
    services/                   # Recherche, mises à jour GitHub
    storage/                    # Préférences locales : progression, signets, réglages
    theme/                      # Jetons du design system VIV Formation (couleurs, typo, espacements, mouvement)
    widgets/                    # Page de chapitre, rendu des modules, composants de marque (viv_brand.dart)
  features/                     # Écrans : tableau de bord, programme, signets, chapitres, paramètres, coque
_resources/                     # Sources Markdown : programme PRC02 et textes des chapitres
viv-formation-design-system/    # Référence du design system (tokens, composants, logos, polices)
writer_guide.md                 # Format Markdown des sources de chapitre
setup.iss                       # Installeur Inno Setup
tool/build_release.ps1          # Compilation Release + installeur
```

## Prérequis

- **Flutter** (canal stable, testé avec 3.50.0) avec le support Windows ;
- **Visual Studio** avec la charge de travail « Développement Desktop en C++ » ;
- **Mode développeur Windows** activé (liens symboliques des plugins) ;
- **Inno Setup 6** pour produire l'installeur.

## Développer

```bash
flutter pub get
flutter run -d windows
flutter analyze
```

## Ajouter ou modifier du contenu

1. Rédiger le chapitre en Markdown dans `_resources/` en suivant `writer_guide.md` (fichiers `PRC02-SU-26v01_<chapitre>.md`).
2. Le transcrire en modules dans `lib/core/data/mock_chapters_data.dart` (`chapter1Modules`…). Les identifiants de section (`ch1_sec1_title`…) doivent correspondre aux `targetModuleId` des points clés déclarés dans `course_data.dart`.
3. Déposer les captures dans `assets/images/` (`<sujet>_blender.jpg`, captures prises dans le thème sombre de Blender, à partir des fichiers d'exercice).
4. Titres, objectifs, libellés et icônes des chapitres : `lib/core/data/course_data.dart` uniquement.

## Publier une version

1. Incrémenter `version:` dans `pubspec.yaml` (ex. `0.2.0+2`).
2. Lancer :

   ```bash
   powershell -ExecutionPolicy Bypass -File tool/build_release.ps1
   ```

   Le script compile l'application et produit `Output/blender_design_visualisation_setup_v<version>.exe`.
3. Créer une release GitHub sur ce dépôt avec le tag `v<version>` et y joindre l'installeur. Les postes équipés sont prévenus au lancement suivant et se mettent à jour en silence.

> L'`AppId` de `setup.iss` est propre à ce support : ne jamais le modifier ni le réutiliser pour un autre support, sinon les mises à jour ne remplaceraient plus l'installation existante.

## Design system

Le dossier `viv-formation-design-system/` est la référence. Les points qui s'appliquent ici :

- deux familles, Playfair Display Bold Italic (titres) et Noto Sans, **sans gras droit** ;
- le texte et les actions sont en `action` (#9c3f68), l'accent en `accent-deep` ;
- les pastels de marque et le dégradé (`brand-rose` → `brand-gold`, toujours horizontal) servent à habiller, jamais à écrire ;
- un seul bouton plein par bloc, les autres en contour ;
- une barre de navigation sombre, un contenu clair, un filet de dégradé sous l'en-tête ;
- pas d'emoji ;
- mouvement limité à 120, 200 ou 320 ms, coupé si le système demande de réduire les animations.
