import 'package:flutter_test/flutter_test.dart';

import 'package:viv_support_blender_design_viz/core/data/course_data.dart';
import 'package:viv_support_blender_design_viz/core/models/content_module.dart';

/// Structure du support : les trois rubriques de la barre latérale, les branches du routeur, les points
/// du Programme et la navigation entre chapitres.
void main() {
  final chapters = CourseData.chapters;

  test('les trois rubriques, dans l\'ordre', () {
    expect(CourseData.basics.map((c) => c.number), [101, 102, 103]);
    expect(CourseData.formation.map((c) => c.number), [1, 2, 3, 4]);
    expect(CourseData.challenges.map((c) => c.route), ['/defi-modelisation', '/defi-procedural']);
    expect(CourseData.core.length, 7);
  });

  test('chaque branche est unique, hors des écrans fixes', () {
    final branches = chapters.map((c) => c.branchIndex).toList();
    expect(branches.toSet().length, branches.length);
    for (final fixed in [
      CourseData.dashboardBranch,
      CourseData.programBranch,
      CourseData.bookmarksBranch,
      CourseData.settingsBranch,
    ]) {
      expect(branches.contains(fixed), isFalse);
    }
    expect(CourseData.challenges.map((c) => c.branchIndex), [11, 12]);
  });

  test('les identifiants de modules sont uniques dans tout le support', () {
    final ids = [for (final c in chapters) for (final m in c.modules) m.id];
    expect(ids.toSet().length, ids.length);
  });

  test('chaque page s\'ouvre sur son titre', () {
    for (final c in chapters.where((c) => c.modules.isNotEmpty)) {
      expect(c.modules.first, isA<TitleModule>(), reason: c.route);
    }
    expect(CourseData.challenges.first.modules.first.id, 'ch2_sec4_title');
    expect(CourseData.challenges.last.modules.first.id, 'ch3_sec4_title');
  });

  test('chaque point du Programme vise un module de son chapitre', () {
    for (final c in chapters) {
      final ids = c.modules.map((m) => m.id).toSet();
      for (final p in c.points) {
        expect(ids.contains(p.targetModuleId), isTrue, reason: '${c.route} : ${p.targetModuleId}');
      }
    }
  });

  test('les défis ne restent plus dans les chapitres 2 et 3', () {
    for (final route in ['/chapter-2', '/chapter-3']) {
      final c = CourseData.byRoute(route)!;
      expect(c.modules.any((m) => m.id.contains('_sec4_')), isFalse, reason: route);
    }
  });

  test('la navigation reste dans son groupe', () {
    final ch4 = CourseData.byRoute('/chapter-4')!;
    final d1 = CourseData.byRoute('/defi-modelisation')!;
    final d2 = CourseData.byRoute('/defi-procedural')!;
    expect(CourseData.nextOf(ch4), isNull);
    expect(CourseData.previousOf(d1), isNull);
    expect(CourseData.nextOf(d1), d2);
    expect(CourseData.nextOf(d2), isNull);
    expect(CourseData.nextOf(CourseData.byRoute('/basics-103')!)?.route, '/chapter-1');
  });

  test('les libellés des défis', () {
    final d2 = CourseData.byRoute('/defi-procedural')!;
    expect(d2.shortLabel, 'Défi 2');
    expect(d2.overline, 'Pour aller plus loin · Défi 2');
    expect(CourseData.screenTitle(d2.branchIndex), 'Matières procédurales');
  });
}
