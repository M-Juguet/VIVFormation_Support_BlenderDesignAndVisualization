import 'package:flutter/widgets.dart';

import '../../core/widgets/chapter_scaffold.dart';

/// Écran d'un défi de la rubrique « Pour aller plus loin » : la même mise en page qu'un chapitre,
/// pour la route donnée (voir `CourseData.chapters`).
class ChallengeScreen extends StatelessWidget {
  final String route;
  final String? targetModuleId;

  const ChallengeScreen({
    super.key,
    required this.route,
    this.targetModuleId,
  });

  @override
  Widget build(BuildContext context) {
    return ChapterScaffold.forRoute(route, targetModuleId: targetModuleId);
  }
}
