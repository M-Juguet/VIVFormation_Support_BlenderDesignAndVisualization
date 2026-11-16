import 'package:flutter/material.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';

import '../../../core/models/content_module.dart';
import '../../../core/theme/viv_colors.dart';
import '../../../core/theme/viv_motion.dart';
import '../../../core/theme/viv_spacing.dart';
import '../../../core/theme/viv_typography.dart';
import '../viv_brand.dart';
import '../viv_markdown.dart';

/// Quiz d'auto-évaluation. La correction apparaît en 200 ms et **reste** écrite ;
/// la bonne réponse est toujours signalée par un mot, pas seulement par une couleur.
class QuizModuleWidget extends StatefulWidget {
  final QuizModule module;

  const QuizModuleWidget({super.key, required this.module});

  @override
  State<QuizModuleWidget> createState() => _QuizModuleWidgetState();
}

class _QuizModuleWidgetState extends State<QuizModuleWidget> {
  final Set<int> _selectedIndices = {};
  bool _isSubmitted = false;

  void _toggleOption(int index) {
    if (_isSubmitted) return;
    setState(() {
      if (_selectedIndices.contains(index)) {
        _selectedIndices.remove(index);
      } else {
        _selectedIndices.add(index);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final isCorrect = _selectedIndices.length == widget.module.correctIndices.length &&
        _selectedIndices.every((i) => widget.module.correctIndices.contains(i));

    return Container(
      width: double.infinity,
      decoration: VivDecorations.card(),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const VivGradientLine(),
          Padding(
            padding: const EdgeInsets.all(VivSpacing.space6),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const VivOverline('Auto-évaluation'),
                const SizedBox(height: VivSpacing.space2),
                Text(widget.module.question, style: VivTypography.headingMd),
                if (widget.module.correctIndices.length > 1) ...[
                  const SizedBox(height: VivSpacing.space1),
                  Text('Plusieurs réponses sont attendues.', style: VivTypography.caption),
                ],
                const SizedBox(height: VivSpacing.space5),
                ...List.generate(widget.module.options.length, _buildOption),
                const SizedBox(height: VivSpacing.space4),
                AnimatedSwitcher(
                  duration: VivMotion.of(context, VivMotion.state),
                  switchInCurve: VivMotion.enter,
                  switchOutCurve: VivMotion.exit,
                  child: _isSubmitted
                      ? _buildExplanationBlock(isCorrect)
                      : SizedBox(
                          key: const ValueKey('submit'),
                          width: double.infinity,
                          child: ElevatedButton(
                            style: VivButtonStyles.primary(),
                            onPressed: _selectedIndices.isEmpty
                                ? null
                                : () => setState(() => _isSubmitted = true),
                            child: const Text('Vérifier mes réponses'),
                          ),
                        ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildOption(int index) {
    final isSelected = _selectedIndices.contains(index);
    final isActuallyCorrect = widget.module.correctIndices.contains(index);

    var borderColor = VivColors.border;
    var background = VivColors.surfaceRaised;
    var markColor = VivColors.borderStrong;
    String? verdict;
    Color verdictColor = VivColors.inkMuted;

    if (_isSubmitted) {
      if (isActuallyCorrect) {
        borderColor = VivColors.success;
        background = VivColors.successSurface;
        markColor = VivColors.success;
        verdict = 'Bonne réponse';
        verdictColor = VivColors.success;
      } else if (isSelected) {
        borderColor = VivColors.danger;
        background = VivColors.dangerSurface;
        markColor = VivColors.danger;
        verdict = 'Réponse incorrecte';
        verdictColor = VivColors.danger;
      }
    } else if (isSelected) {
      borderColor = VivColors.action;
      background = VivColors.surfaceBrand;
      markColor = VivColors.action;
    }

    return Padding(
      padding: const EdgeInsets.only(bottom: VivSpacing.space2),
      child: MouseRegion(
        cursor: _isSubmitted ? MouseCursor.defer : SystemMouseCursors.click,
        child: GestureDetector(
          onTap: () => _toggleOption(index),
          child: AnimatedContainer(
            duration: VivMotion.of(context, VivMotion.micro),
            curve: VivMotion.standard,
            padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space4, vertical: VivSpacing.space3),
            decoration: BoxDecoration(
              color: background,
              borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
              border: Border.all(color: borderColor, width: 1.5),
            ),
            child: Row(
              children: [
                Container(
                  width: 20,
                  height: 20,
                  decoration: BoxDecoration(
                    color: isSelected ? markColor : Colors.transparent,
                    border: Border.all(color: markColor, width: 2),
                    borderRadius: BorderRadius.circular(VivSpacing.radiusSm),
                  ),
                  child: isSelected ? const Icon(LucideIcons.check, size: 12, color: VivColors.onAction) : null,
                ),
                const SizedBox(width: VivSpacing.space3),
                Expanded(child: Text(widget.module.options[index], style: VivTypography.body)),
                if (verdict != null) ...[
                  const SizedBox(width: VivSpacing.space3),
                  Text(verdict, style: VivTypography.label.copyWith(color: verdictColor)),
                ],
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildExplanationBlock(bool isSuccess) {
    final tone = isSuccess ? VivColors.success : VivColors.warning;
    return Column(
      key: const ValueKey('explanation'),
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space5, vertical: VivSpacing.space4),
          decoration: BoxDecoration(
            color: isSuccess ? VivColors.successSurface : VivColors.warningSurface,
            borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
          ),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Padding(
                padding: const EdgeInsets.only(top: 2),
                child: Icon(isSuccess ? LucideIcons.circleCheck : LucideIcons.triangleAlert, color: tone, size: 20),
              ),
              const SizedBox(width: VivSpacing.space3),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      isSuccess ? 'Bonne réponse' : 'À revoir',
                      style: VivTypography.headingSm.copyWith(color: VivColors.ink),
                    ),
                    const SizedBox(height: VivSpacing.space1),
                    VivMarkdown(widget.module.explanation),
                  ],
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: VivSpacing.space4),
        Align(
          alignment: Alignment.centerLeft,
          child: OutlinedButton.icon(
            style: VivButtonStyles.secondary(),
            onPressed: () => setState(() {
              _isSubmitted = false;
              _selectedIndices.clear();
            }),
            icon: const Icon(LucideIcons.rotateCcw, size: 16),
            label: const Text('Recommencer le quiz'),
          ),
        ),
      ],
    );
  }
}
