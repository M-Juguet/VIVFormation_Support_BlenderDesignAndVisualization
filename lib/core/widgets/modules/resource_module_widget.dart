import 'package:flutter/material.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../../core/models/content_module.dart';
import '../../../core/theme/viv_colors.dart';
import '../../../core/theme/viv_spacing.dart';
import '../../../core/theme/viv_typography.dart';
import '../viv_brand.dart';

/// Fichier ressource à récupérer (fichier d'exercice, kit de démarrage…).
class ResourceModuleWidget extends StatelessWidget {
  final ResourceModule module;

  const ResourceModuleWidget({super.key, required this.module});

  Future<void> _open() async {
    final uri = Uri.tryParse(module.downloadUrl);
    if (uri == null) return;
    try {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    } catch (_) {
      // Lien non ouvrable : on ignore silencieusement.
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(VivSpacing.space5),
      decoration: BoxDecoration(
        color: VivColors.surfaceBrand,
        borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
      ),
      child: Row(
        children: [
          // Pastille pleine au dégradé de marque : action à forte visibilité.
          Container(
            width: 48,
            height: 48,
            decoration: BoxDecoration(
              gradient: VivColors.gradientBrand,
              borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
            ),
            child: const Icon(LucideIcons.download, color: VivColors.inkOnPastel, size: 24),
          ),
          const SizedBox(width: VivSpacing.space4),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                VivOverline(module.title),
                const SizedBox(height: VivSpacing.space1),
                Text(module.fileName, style: VivTypography.headingSm),
                const SizedBox(height: VivSpacing.space1),
                Text(module.description, style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted)),
              ],
            ),
          ),
          const SizedBox(width: VivSpacing.space4),
          ElevatedButton.icon(
            style: VivButtonStyles.primary(),
            onPressed: _open,
            icon: const Icon(LucideIcons.externalLink, size: 16),
            label: const Text('Récupérer'),
          ),
        ],
      ),
    );
  }
}
