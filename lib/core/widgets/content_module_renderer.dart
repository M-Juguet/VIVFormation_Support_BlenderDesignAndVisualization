import 'package:flutter/material.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import 'package:cached_network_image/cached_network_image.dart';

import '../models/content_module.dart';
import '../theme/viv_colors.dart';
import '../theme/viv_spacing.dart';
import '../theme/viv_typography.dart';
import 'modules/info_module_widget.dart';
import 'modules/resource_module_widget.dart';
import 'modules/quiz_module_widget.dart';
import 'viv_markdown.dart';

class ContentModuleRenderer extends StatelessWidget {
  final ContentModule module;
  final bool isBookmarked;
  final VoidCallback? onBookmarkToggle;
  final Function(String path, String? caption)? onImageTap;

  const ContentModuleRenderer({
    super.key,
    required this.module,
    this.isBookmarked = false,
    this.onBookmarkToggle,
    this.onImageTap,
  });

  @override
  Widget build(BuildContext context) {
    final hasBookmark = onBookmarkToggle != null && module is! TitleModule;

    return Padding(
      padding: const EdgeInsets.only(bottom: VivSpacing.space8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Signet discret à gauche du module
          if (hasBookmark) ...[
            SizedBox(
              width: 28,
              height: 28,
              child: IconButton(
                padding: EdgeInsets.zero,
                constraints: const BoxConstraints(),
                icon: Icon(
                  LucideIcons.bookmark,
                  color: isBookmarked ? VivColors.action : VivColors.borderStrong,
                  size: 16,
                ),
                onPressed: onBookmarkToggle,
                tooltip: isBookmarked ? 'Retirer des signets' : 'Ajouter aux signets',
              ),
            ),
            const SizedBox(width: VivSpacing.space2),
          ],
          Expanded(child: _buildModuleContent(context)),
        ],
      ),
    );
  }

  Widget _buildModuleContent(BuildContext context) {
    final mod = module;
    if (mod is TitleModule) {
      return Padding(
        padding: const EdgeInsets.only(top: VivSpacing.space4),
        child: Text(mod.title, style: VivTypography.headingLg),
      );
    } else if (mod is TextModule) {
      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (mod.title != null) ...[
            Text(mod.title!, style: VivTypography.headingMd),
            const SizedBox(height: VivSpacing.space3),
          ],
          VivMarkdown(mod.content),
        ],
      );
    } else if (mod is SideBySideModule) {
      final isTextLeft = mod.layout == ContentLayout.textLeft;
      final text = VivMarkdown(mod.content);
      final image = _buildClickableImage(context, mod.imagePath, mod.caption);
      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (mod.title != null) ...[
            Text(mod.title!, style: VivTypography.headingMd),
            const SizedBox(height: VivSpacing.space4),
          ],
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Expanded(child: isTextLeft ? text : image),
              const SizedBox(width: VivSpacing.space6),
              Expanded(child: isTextLeft ? image : text),
            ],
          ),
        ],
      );
    } else if (mod is FullMediaModule) {
      return _buildClickableImage(context, mod.imagePath, mod.caption, isFullWidth: true);
    } else if (mod is InfoModule) {
      return InfoModuleWidget(module: mod);
    } else if (mod is ResourceModule) {
      return ResourceModuleWidget(module: mod);
    } else if (mod is ListModule) {
      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(mod.title, style: VivTypography.headingMd),
          const SizedBox(height: VivSpacing.space3),
          if (mod.intro != null) ...[
            VivMarkdown(mod.intro!),
            const SizedBox(height: VivSpacing.space1),
          ],
          ...mod.items.map(
            (item) => Padding(
              padding: const EdgeInsets.only(bottom: VivSpacing.space2, left: VivSpacing.space1),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Puce de liste : pastille dorée, l'écho du point sur le i.
                  Container(
                    width: 8,
                    height: 8,
                    margin: const EdgeInsets.only(top: 8),
                    decoration: const BoxDecoration(color: VivColors.brandGold, shape: BoxShape.circle),
                  ),
                  const SizedBox(width: VivSpacing.space3),
                  Expanded(child: VivMarkdown(item)),
                ],
              ),
            ),
          ),
          if (mod.outro != null) ...[
            const SizedBox(height: VivSpacing.space2),
            VivMarkdown(mod.outro!),
          ],
        ],
      );
    } else if (mod is QuizModule) {
      return QuizModuleWidget(module: mod);
    }
    return const SizedBox.shrink();
  }

  /// Image au format `Figure` : contour border, radius-lg, légende en caption.
  /// Ni ombre portée, ni perspective.
  Widget _buildClickableImage(BuildContext context, String imagePath, String? caption, {bool isFullWidth = false}) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        MouseRegion(
          cursor: SystemMouseCursors.click,
          child: GestureDetector(
            onTap: onImageTap != null ? () => onImageTap!(imagePath, caption) : null,
            child: Container(
              width: double.infinity,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
                border: Border.all(color: VivColors.border),
                color: VivColors.surfaceSunken,
              ),
              clipBehavior: Clip.antiAlias,
              constraints: BoxConstraints(maxHeight: isFullWidth ? 450.0 : 300.0),
              child: imagePath.startsWith('http')
                  ? CachedNetworkImage(
                      imageUrl: imagePath,
                      fit: BoxFit.contain,
                      placeholder: (context, url) => _ImagePlaceholder(isFullWidth: isFullWidth),
                      errorWidget: (context, url, error) => _ImageError(
                        isFullWidth: isFullWidth,
                        title: 'Image indisponible hors ligne',
                        message:
                            'Cette image sera mise en cache lors de sa première consultation en ligne afin d\'être visible hors ligne.',
                      ),
                    )
                  : Image.asset(
                      imagePath,
                      fit: BoxFit.contain,
                      errorBuilder: (context, error, stackTrace) => _ImageError(
                        isFullWidth: isFullWidth,
                        title: 'Capture à venir',
                        message: 'Cette illustration sera ajoutée dans une prochaine mise à jour du support.',
                      ),
                    ),
            ),
          ),
        ),
        if (caption != null) ...[
          const SizedBox(height: VivSpacing.space2),
          Text(caption, style: VivTypography.caption),
        ],
      ],
    );
  }
}

class _ImageError extends StatelessWidget {
  final bool isFullWidth;
  final String title;
  final String message;

  const _ImageError({required this.isFullWidth, required this.title, required this.message});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: isFullWidth ? 300 : 200,
      width: double.infinity,
      color: VivColors.surfaceSunken,
      padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space6, vertical: VivSpacing.space4),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Icon(LucideIcons.image, color: VivColors.inkSubtle, size: 32),
          const SizedBox(height: VivSpacing.space3),
          Text(title, style: VivTypography.headingSm, textAlign: TextAlign.center),
          const SizedBox(height: VivSpacing.space1),
          Text(
            message,
            style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
}

/// Emplacement d'image pendant le chargement : statique, les images ne bougent pas.
class _ImagePlaceholder extends StatelessWidget {
  final bool isFullWidth;
  const _ImagePlaceholder({required this.isFullWidth});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: isFullWidth ? 300 : 200,
      width: double.infinity,
      color: VivColors.surfaceSunken,
      child: const Center(child: Icon(LucideIcons.image, color: VivColors.borderStrong, size: 40)),
    );
  }
}
