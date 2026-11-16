import 'package:flutter/material.dart';

import '../../core/widgets/chapter_scaffold.dart';

class Basics103Screen extends StatelessWidget {
  final String? targetModuleId;

  const Basics103Screen({
    super.key,
    this.targetModuleId,
  });

  @override
  Widget build(BuildContext context) {
    return ChapterScaffold.forRoute('/basics-103', targetModuleId: targetModuleId);
  }
}
