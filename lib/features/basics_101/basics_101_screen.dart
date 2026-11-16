import 'package:flutter/material.dart';

import '../../core/widgets/chapter_scaffold.dart';

class Basics101Screen extends StatelessWidget {
  final String? targetModuleId;

  const Basics101Screen({
    super.key,
    this.targetModuleId,
  });

  @override
  Widget build(BuildContext context) {
    return ChapterScaffold.forRoute('/basics-101', targetModuleId: targetModuleId);
  }
}
