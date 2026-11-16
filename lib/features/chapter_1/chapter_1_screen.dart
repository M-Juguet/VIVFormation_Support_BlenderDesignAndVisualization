import 'package:flutter/material.dart';

import '../../core/widgets/chapter_scaffold.dart';

class Chapter1Screen extends StatelessWidget {
  final String? targetModuleId;

  const Chapter1Screen({
    super.key,
    this.targetModuleId,
  });

  @override
  Widget build(BuildContext context) {
    return ChapterScaffold.forRoute('/chapter-1', targetModuleId: targetModuleId);
  }
}
