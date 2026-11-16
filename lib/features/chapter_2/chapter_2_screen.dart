import 'package:flutter/material.dart';

import '../../core/widgets/chapter_scaffold.dart';

class Chapter2Screen extends StatelessWidget {
  final String? targetModuleId;

  const Chapter2Screen({
    super.key,
    this.targetModuleId,
  });

  @override
  Widget build(BuildContext context) {
    return ChapterScaffold.forRoute('/chapter-2', targetModuleId: targetModuleId);
  }
}
