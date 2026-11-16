import 'package:flutter/material.dart';

import '../../../core/models/content_module.dart';
import '../../../core/models/content_module_labels.dart';
import '../../../core/theme/viv_colors.dart';
import '../../../core/theme/viv_spacing.dart';
import '../../../core/theme/viv_typography.dart';
import '../viv_brand.dart';
import '../viv_markdown.dart';

/// Encart (`Callout` du design system) : sort une information de son flux.
/// Chaque type garde son mot-titre : une icône seule ne signale jamais un statut.
class InfoModuleWidget extends StatelessWidget {
  final InfoModule module;

  const InfoModuleWidget({super.key, required this.module});

  @override
  Widget build(BuildContext context) {
    final (Color surface, Color mark, Color titleColor) = switch (module.type) {
      InfoType.idea => (VivColors.surfaceBrand, VivColors.action, VivColors.ink),
      InfoType.tip => (VivColors.successSurface, VivColors.success, VivColors.ink),
      InfoType.warning => (VivColors.warningSurface, VivColors.warning, VivColors.ink),
      InfoType.info => (VivColors.infoSurface, VivColors.info, VivColors.ink),
      InfoType.objective => (VivColors.surfaceAccent, VivColors.accentDeep, VivColors.accentDeep),
      InfoType.challenge => (VivColors.surfaceRaised, VivColors.action, VivColors.ink),
    };

    final body = Padding(
      padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space5, vertical: VivSpacing.space4),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.only(top: 2),
            child: Icon(module.type.icon, color: mark, size: 20),
          ),
          const SizedBox(width: VivSpacing.space3),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(module.type.label, style: VivTypography.headingSm.copyWith(color: titleColor)),
                const SizedBox(height: VivSpacing.space1),
                VivMarkdown(module.text),
              ],
            ),
          ),
        ],
      ),
    );

    // Le défi fil rouge est une carte de module : filet de dégradé en tête.
    if (module.type == InfoType.challenge) {
      return Container(
        width: double.infinity,
        decoration: VivDecorations.card(),
        clipBehavior: Clip.antiAlias,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [const VivGradientLine(), body],
        ),
      );
    }

    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: surface,
        borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
      ),
      child: body,
    );
  }
}
