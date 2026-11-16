import 'package:flutter/material.dart';

import '../../core/widgets/chapter_scaffold.dart';

class Chapter4Screen extends StatelessWidget {
  final String? targetModuleId;

  const Chapter4Screen({
    super.key,
    this.targetModuleId,
  });

  @override
  Widget build(BuildContext context) {
    return ChapterScaffold.forRoute('/chapter-4', targetModuleId: targetModuleId);
  }
}
