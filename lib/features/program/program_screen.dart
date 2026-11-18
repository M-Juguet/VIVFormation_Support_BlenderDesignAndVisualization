import 'package:flutter/material.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import 'package:go_router/go_router.dart';

import '../../core/data/course_data.dart';
import '../../core/theme/viv_colors.dart';
import '../../core/theme/viv_motion.dart';
import '../../core/theme/viv_spacing.dart';
import '../../core/theme/viv_typography.dart';
import '../../core/widgets/viv_brand.dart';

class ProgramScreen extends StatelessWidget {
  const ProgramScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(VivSpacing.space6),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const VivOverline('Programme de formation · ${CourseData.reference}'),
          const SizedBox(height: VivSpacing.space3),
          Text(CourseData.trainingTitle, style: VivTypography.displayLg),
          const SizedBox(height: VivSpacing.space4),
          ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 800),
            child: Text(
              '${CourseData.trainingSummary} Chaque chapitre ci-dessous correspond à une compétence visée ; '
              'cliquez sur un point clé pour ouvrir directement la section correspondante.',
              style: VivTypography.bodyLg.copyWith(color: VivColors.inkMuted),
            ),
          ),
          const SizedBox(height: VivSpacing.space10),
          Column(
            children: CourseData.formation.map((chapter) => _buildChapterCard(context, chapter)).toList(),
          ),
        ],
      ),
    );
  }

  Widget _buildChapterCard(BuildContext context, CourseChapter chapter) {
    return Padding(
      padding: const EdgeInsets.only(bottom: VivSpacing.space6),
      child: VivCard(
        gradientStrip: true,
        padding: const EdgeInsets.all(VivSpacing.space6),
        onTap: () => context.go(chapter.route),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                VivBadge('Chapitre ${chapter.number.toString().padLeft(2, '0')}', tone: VivBadgeTone.gold),
                if (chapter.showsPreparationBadge) ...[
                  const SizedBox(width: VivSpacing.space2),
                  const VivBadge('En préparation'),
                ],
                const Spacer(),
                Icon(chapter.icon, color: VivColors.action, size: 24),
              ],
            ),
            const SizedBox(height: VivSpacing.space4),
            Text(chapter.title, style: VivTypography.headingLg),
            const SizedBox(height: VivSpacing.space2),
            Text(chapter.objective, style: VivTypography.body.copyWith(color: VivColors.inkMuted)),
            const SizedBox(height: VivSpacing.space5),
            const Divider(color: VivColors.border, height: 1),
            const SizedBox(height: VivSpacing.space4),
            Text('Points clés au programme', style: VivTypography.headingSm),
            const SizedBox(height: VivSpacing.space3),
            Wrap(
              spacing: VivSpacing.space3,
              runSpacing: VivSpacing.space2,
              children: chapter.points.map((point) => _KeyPointChip(chapter: chapter, point: point)).toList(),
            ),
          ],
        ),
      ),
    );
  }
}

class _KeyPointChip extends StatefulWidget {
  final CourseChapter chapter;
  final ChapterPoint point;

  const _KeyPointChip({required this.chapter, required this.point});

  @override
  State<_KeyPointChip> createState() => _KeyPointChipState();
}

class _KeyPointChipState extends State<_KeyPointChip> {
  bool _hovered = false;

  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      cursor: SystemMouseCursors.click,
      onEnter: (_) => setState(() => _hovered = true),
      onExit: (_) => setState(() => _hovered = false),
      child: GestureDetector(
        onTap: () => context.go('${widget.chapter.route}?target=${widget.point.targetModuleId}'),
        child: AnimatedContainer(
          duration: VivMotion.of(context, VivMotion.micro),
          padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space3, vertical: VivSpacing.space2),
          decoration: BoxDecoration(
            color: _hovered ? VivColors.surfaceBrand : VivColors.surfaceRaised,
            borderRadius: BorderRadius.circular(VivSpacing.radiusPill),
            border: Border.all(color: _hovered ? VivColors.action : VivColors.border),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Icon(LucideIcons.check, color: VivColors.success, size: 14),
              const SizedBox(width: VivSpacing.space2),
              Text(widget.point.label, style: VivTypography.label),
            ],
          ),
        ),
      ),
    );
  }
}
