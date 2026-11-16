import 'package:flutter/material.dart';

import '../../core/widgets/chapter_scaffold.dart';

class Chapter3Screen extends StatelessWidget {
  final String? targetModuleId;

  const Chapter3Screen({
    super.key,
    this.targetModuleId,
  });

  @override
  Widget build(BuildContext context) {
    return ChapterScaffold.forRoute('/chapter-3', targetModuleId: targetModuleId);
  }
}
