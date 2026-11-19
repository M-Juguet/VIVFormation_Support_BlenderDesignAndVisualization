import 'package:flutter/widgets.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';

import '../models/content_module.dart';
import 'mock_chapters_data.dart';

/// Section de la barre latérale à laquelle appartient un chapitre.
enum CourseSection { bases, formation }

/// Point clé du programme, lien direct vers une section d'un chapitre.
class ChapterPoint {
  final String label;
  final String targetModuleId;

  const ChapterPoint({
    required this.label,
    required this.targetModuleId,
  });
}

/// Description complète d'un chapitre du support.
///
/// C'est la **seule source** des titres, objectifs, icônes, routes et contenus :
/// la navigation, le tableau de bord, le programme, la recherche et les signets
/// la lisent toutes. Ajouter ou renommer un chapitre se fait ici.
class CourseChapter {
  /// Route GoRouter du chapitre (ex. `/chapter-1`).
  final String route;

  /// Index de la branche dans le `StatefulShellRoute` (voir `app_router.dart`).
  final int branchIndex;

  final CourseSection section;

  /// Numéro affiché : 101, 102, 103 pour les bases, 1 à 4 pour la formation.
  final int number;

  /// Libellé court de la barre latérale et de l'en-tête.
  final String navLabel;

  /// Titre complet du chapitre.
  final String title;

  /// Objectif du chapitre, à l'infinitif.
  final String objective;

  final IconData icon;

  /// Contenu du chapitre. Vide : le chapitre s'affiche « en préparation ».
  final List<ContentModule> modules;

  /// Points clés présentés sur l'écran Programme.
  final List<ChapterPoint> points;

  /// Le contenu de base manque encore, mais le chapitre a déjà des modules (un défi
  /// facultatif, par exemple) : il s'ouvre, et garde son badge « En préparation ».
  final bool baseContentPending;

  const CourseChapter({
    required this.route,
    required this.branchIndex,
    required this.section,
    required this.number,
    required this.navLabel,
    required this.title,
    required this.objective,
    required this.icon,
    required this.modules,
    this.points = const [],
    this.baseContentPending = false,
  });

  bool get isBasics => section == CourseSection.bases;

  bool get isInPreparation => modules.isEmpty;

  /// Badge « En préparation » du tableau de bord et du Programme.
  bool get showsPreparationBadge => isInPreparation || baseContentPending;

  /// « Basics 101 » ou « Chapitre 1 ».
  String get shortLabel => isBasics ? 'Basics $number' : 'Chapitre $number';

  /// Sur-titre du chapitre (à composer en capitales).
  String get overline => isBasics ? 'Les bases · Basics $number' : 'Formation · Chapitre $number';
}

/// Identité de la formation et registre ordonné de ses chapitres.
class CourseData {
  CourseData._();

  static const String reference = 'PRC02';
  static const String trainingTitle = 'Design & visualisation temps réel avec Blender';
  static const String supportName = '[SU] $trainingTitle';
  static const String trainingSummary =
      'Concevez et visualisez vos concepts produit dans Blender : blocage de volumes, '
      'modélisation non destructive, matières réalistes et visuels en temps réel avec EEVEE.';

  static const int dashboardBranch = 0;
  static const int programBranch = 1;
  static const int bookmarksBranch = 2;
  static const int settingsBranch = 10;

  static const List<CourseChapter> chapters = [
    // --- Les bases : deux demi-journées d'initiation au logiciel ------------
    CourseChapter(
      route: '/basics-101',
      branchIndex: 3,
      section: CourseSection.bases,
      number: 101,
      navLabel: 'Basics 101',
      title: 'Découverte et prise en main',
      objective:
          'Installer et configurer Blender, comprendre l\'organisation de son interface et naviguer avec aisance dans la vue 3D.',
      icon: LucideIcons.mousePointer,
      modules: basics101Modules,
    ),
    CourseChapter(
      route: '/basics-102',
      branchIndex: 4,
      section: CourseSection.bases,
      number: 102,
      navLabel: 'Basics 102',
      title: 'Manipuler et organiser son travail',
      objective:
          'Sélectionner et transformer les objets, utiliser le curseur 3D et les points de pivot, puis organiser et sauvegarder proprement ses projets avec les collections et l\'empaquetage des textures.',
      icon: LucideIcons.move,
      modules: basics102Modules,
    ),
    CourseChapter(
      route: '/basics-103',
      branchIndex: 5,
      section: CourseSection.bases,
      number: 103,
      navLabel: 'Basics 103',
      title: 'Bases de la modélisation',
      objective:
          'Modifier un maillage en Mode Édition avec les outils essentiels (Extrude, Inset, Bevel, Loop Cut), découvrir les modificateurs et adopter les bonnes pratiques de topologie.',
      icon: LucideIcons.box,
      modules: basics103Modules,
    ),

    // --- Formation : bloc 1, concept design et modélisation agile ----------
    CourseChapter(
      route: '/chapter-1',
      branchIndex: 6,
      section: CourseSection.formation,
      number: 1,
      navLabel: 'Blocage & environnement',
      title: 'Environnement de travail et blocage de volumes',
      objective:
          'Configurer un environnement de travail adapté au design produit, puis explorer rapidement volumes et silhouettes par blocage de formes avec les outils de transformation et d\'édition interactive.',
      icon: LucideIcons.shapes,
      modules: chapter1Modules,
      points: [
        ChapterPoint(label: 'Interface et outils pour le design', targetModuleId: 'ch1_sec1_title'),
        ChapterPoint(label: 'Blocage de volumes (greyboxing)', targetModuleId: 'ch1_sec2_title'),
        ChapterPoint(label: 'Transformation et édition interactive', targetModuleId: 'ch1_sec3_title'),
      ],
    ),
    CourseChapter(
      route: '/chapter-2',
      branchIndex: 7,
      section: CourseSection.formation,
      number: 2,
      navLabel: 'Modélisation non destructive',
      title: 'Modélisation non destructive : modificateurs et courbes',
      objective:
          'Modéliser un objet industriel de façon non destructive avec les modificateurs de symétrie, d\'épaisseur et de répétition, et dessiner profils et détails organiques avec les courbes de Bézier.',
      icon: LucideIcons.spline,
      modules: chapter2Modules,
      points: [
        ChapterPoint(label: 'Modificateurs : symétrie, épaisseur, répétition', targetModuleId: 'ch2_sec1_title'),
        ChapterPoint(label: 'Courbes de Bézier : profils et détails', targetModuleId: 'ch2_sec2_title'),
        ChapterPoint(label: 'Atelier : concept d\'objet industriel', targetModuleId: 'ch2_sec3_title'),
        ChapterPoint(label: 'Défi facultatif : modélisation avancée', targetModuleId: 'ch2_sec4_title'),
      ],
    ),

    // --- Formation : bloc 2, LookDev et rendu interactif (EEVEE) -----------
    CourseChapter(
      route: '/chapter-3',
      branchIndex: 8,
      section: CourseSection.formation,
      number: 3,
      navLabel: 'Matières & finitions',
      title: 'Matières et finitions réalistes sans dépliage UV',
      objective:
          'Créer des matières réalistes avec le Principled BSDF (métal, plastique, verre), appliquer des finitions CMF par projection triplanaire et organiser ses matières dans la bibliothèque d\'actifs.',
      icon: LucideIcons.palette,
      modules: chapter3Modules,
      points: [
        ChapterPoint(label: 'Principled BSDF : métal, plastique, verre', targetModuleId: 'ch3_sec1_title'),
        ChapterPoint(label: 'Finitions CMF en projection triplanaire', targetModuleId: 'ch3_sec2_title'),
        ChapterPoint(label: 'Bibliothèque d\'actifs (Asset Browser)', targetModuleId: 'ch3_sec3_title'),
        ChapterPoint(label: 'Atelier : le second coloris', targetModuleId: 'ch3_atelier'),
      ],
    ),
    CourseChapter(
      route: '/chapter-4',
      branchIndex: 9,
      section: CourseSection.formation,
      number: 4,
      navLabel: 'Rendu temps réel EEVEE',
      title: 'Visualisation temps réel et visuels de présentation avec EEVEE',
      objective:
          'Paramétrer EEVEE pour une visualisation photoréaliste instantanée, éclairer en studio ou par HDRI, composer l\'image avec la caméra et exporter des visuels de présentation.',
      icon: LucideIcons.camera,
      modules: chapter4Modules,
      points: [
        ChapterPoint(label: 'Paramétrage d\'EEVEE', targetModuleId: 'ch4_sec1_title'),
        ChapterPoint(label: 'Éclairage de studio et HDRI', targetModuleId: 'ch4_sec2_title'),
        ChapterPoint(label: 'Caméra, composition et export', targetModuleId: 'ch4_sec3_title'),
        ChapterPoint(label: 'Atelier : concept final', targetModuleId: 'ch4_sec4_title'),
      ],
    ),
  ];

  static Iterable<CourseChapter> get basics => chapters.where((c) => c.isBasics);

  static Iterable<CourseChapter> get formation => chapters.where((c) => !c.isBasics);

  static CourseChapter? byRoute(String route) {
    for (final c in chapters) {
      if (c.route == route) return c;
    }
    return null;
  }

  static CourseChapter byBranch(int branchIndex) =>
      chapters.firstWhere((c) => c.branchIndex == branchIndex);

  static CourseChapter? previousOf(CourseChapter chapter) {
    final i = chapters.indexOf(chapter);
    return i > 0 ? chapters[i - 1] : null;
  }

  static CourseChapter? nextOf(CourseChapter chapter) {
    final i = chapters.indexOf(chapter);
    return (i >= 0 && i < chapters.length - 1) ? chapters[i + 1] : null;
  }

  /// Titres des écrans hors chapitres, par index de branche.
  static String screenTitle(int branchIndex) {
    switch (branchIndex) {
      case dashboardBranch:
        return 'Tableau de bord';
      case programBranch:
        return 'Programme';
      case bookmarksBranch:
        return 'Mes signets';
      case settingsBranch:
        return 'Paramètres';
      default:
        for (final c in chapters) {
          if (c.branchIndex == branchIndex) return c.navLabel;
        }
        return '';
    }
  }
}
