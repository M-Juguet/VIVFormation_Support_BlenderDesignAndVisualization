import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import '../storage/update_provider.dart';
import '../theme/viv_colors.dart';
import '../theme/viv_spacing.dart';
import '../theme/viv_typography.dart';
import 'viv_brand.dart';
import 'viv_markdown.dart';

class UpdateModal extends ConsumerStatefulWidget {
  const UpdateModal({super.key});

  @override
  ConsumerState<UpdateModal> createState() => _UpdateModalState();
}

class _UpdateModalState extends ConsumerState<UpdateModal> {
  bool _ignoreVersion = false;

  @override
  Widget build(BuildContext context) {
    final updateState = ref.watch(updateProvider);
    final release = updateState.release;

    if (release == null) return const SizedBox.shrink();

    final isDownloading = updateState.status == UpdateStatus.downloading;
    final isReady = updateState.status == UpdateStatus.readyToInstall;
    final isError = updateState.status == UpdateStatus.error;

    return Dialog(
      backgroundColor: VivColors.surfaceRaised,
      surfaceTintColor: Colors.transparent,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
        side: const BorderSide(color: VivColors.border, width: 1),
      ),
      elevation: 0,
      clipBehavior: Clip.antiAlias,
      child: Container(
        width: 580,
        decoration: const BoxDecoration(boxShadow: VivColors.shadowLg),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const VivGradientLine(),
            Padding(
              padding: const EdgeInsets.all(VivSpacing.space6),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Container(
                        width: 40,
                        height: 40,
                        decoration: BoxDecoration(
                          gradient: VivColors.gradientBrand,
                          borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
                        ),
                        child: const Icon(LucideIcons.download, color: VivColors.inkOnPastel, size: 22),
                      ),
                      const SizedBox(width: VivSpacing.space4),
                      Expanded(child: Text('Mise à jour disponible', style: VivTypography.headingLg)),
                    ],
                  ),
                  const SizedBox(height: VivSpacing.space5),
                  Text(
                    'La version ${release.tagName} du support est prête. Vous utilisez actuellement la version ${updateState.localVersion ?? "…"}.',
                    style: VivTypography.body,
                  ),
                  const SizedBox(height: VivSpacing.space4),
                  Text('Notes de version', style: VivTypography.headingSm),
                  const SizedBox(height: VivSpacing.space2),
                  Container(
                    height: 220,
                    width: double.infinity,
                    decoration: BoxDecoration(
                      color: VivColors.surfaceSunken,
                      borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
                      border: Border.all(color: VivColors.border),
                    ),
                    clipBehavior: Clip.antiAlias,
                    child: Markdown(
                      data: release.body.isEmpty ? '*Aucune description fournie pour cette version.*' : release.body,
                      styleSheet: VivMarkdown.styleSheet(context, base: VivTypography.bodySm),
                      onTapLink: VivMarkdown.openLink,
                    ),
                  ),
                  const SizedBox(height: VivSpacing.space4),
                  if (isError)
                    Padding(
                      padding: const EdgeInsets.only(bottom: VivSpacing.space3),
                      child: Row(
                        children: [
                          const Icon(LucideIcons.triangleAlert, color: VivColors.danger, size: 16),
                          const SizedBox(width: VivSpacing.space2),
                          Expanded(
                            child: Text(
                              'Erreur : ${updateState.errorMessage ?? 'la mise à jour a échoué.'}',
                              style: VivTypography.bodySm.copyWith(color: VivColors.danger),
                            ),
                          ),
                        ],
                      ),
                    ),
                  if (isDownloading) ...[
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text('Téléchargement en cours…', style: VivTypography.label),
                        Text(
                          '${(updateState.progress * 100).toStringAsFixed(0)} %',
                          style: VivTypography.label.copyWith(color: VivColors.accentDeep),
                        ),
                      ],
                    ),
                    const SizedBox(height: VivSpacing.space2),
                    VivProgressBar(value: updateState.progress),
                  ] else if (isReady) ...[
                    Row(
                      children: [
                        const Icon(LucideIcons.circleCheck, color: VivColors.success, size: 18),
                        const SizedBox(width: VivSpacing.space2),
                        Text(
                          'Téléchargement terminé. Lancement de l\'installeur…',
                          style: VivTypography.label.copyWith(color: VivColors.success),
                        ),
                      ],
                    ),
                  ] else ...[
                    InkWell(
                      onTap: () => setState(() => _ignoreVersion = !_ignoreVersion),
                      borderRadius: BorderRadius.circular(VivSpacing.radiusSm),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          SizedBox(
                            height: 24,
                            width: 24,
                            child: Checkbox(
                              value: _ignoreVersion,
                              onChanged: (val) => setState(() => _ignoreVersion = val ?? false),
                            ),
                          ),
                          const SizedBox(width: VivSpacing.space2),
                          Text('Ignorer cette version', style: VivTypography.label.copyWith(color: VivColors.inkMuted)),
                        ],
                      ),
                    ),
                  ],
                  const SizedBox(height: VivSpacing.space5),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      if (!isDownloading && !isReady) ...[
                        TextButton(
                          onPressed: () {
                            if (_ignoreVersion) {
                              ref.read(updateProvider.notifier).ignoreVersion(release.semanticVersion);
                            }
                            Navigator.of(context).pop();
                          },
                          style: VivButtonStyles.ghost(),
                          child: const Text('Plus tard'),
                        ),
                        const SizedBox(width: VivSpacing.space3),
                        ElevatedButton(
                          style: VivButtonStyles.primary(),
                          onPressed: () => ref.read(updateProvider.notifier).downloadUpdate(),
                          child: const Text('Mettre à jour'),
                        ),
                      ],
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
