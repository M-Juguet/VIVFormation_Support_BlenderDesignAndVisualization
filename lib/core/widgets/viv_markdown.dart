import 'package:flutter/material.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'package:url_launcher/url_launcher.dart';

import '../theme/viv_colors.dart';
import '../theme/viv_spacing.dart';
import '../theme/viv_typography.dart';

/// Rendu Markdown commun aux modules de contenu, aux encarts, aux quiz et aux
/// notes de version.
///
/// - `**gras**` passe en italique gras (seule face grasse de la charte) ;
/// - `` `code` `` passe en Noto Sans Mono sur `surface-code` ;
/// - les liens sont en `action` et s'ouvrent dans le navigateur.
class VivMarkdown extends StatelessWidget {
  final String data;
  final TextStyle? baseStyle;

  const VivMarkdown(this.data, {super.key, this.baseStyle});

  static MarkdownStyleSheet styleSheet(BuildContext context, {TextStyle? base}) {
    final p = base ?? VivTypography.body;
    return MarkdownStyleSheet.fromTheme(Theme.of(context)).copyWith(
      p: p,
      pPadding: const EdgeInsets.only(bottom: VivSpacing.space3),
      strong: VivTypography.strongOf(p),
      em: p.copyWith(fontStyle: FontStyle.italic),
      a: p.copyWith(color: VivColors.action, decoration: TextDecoration.underline),
      code: VivTypography.code.copyWith(
        fontSize: (p.fontSize ?? 15) - 1,
        color: VivColors.ink,
        backgroundColor: VivColors.surfaceCode,
      ),
      codeblockPadding: const EdgeInsets.all(VivSpacing.space3),
      codeblockDecoration: BoxDecoration(
        color: VivColors.surfaceCode,
        borderRadius: BorderRadius.circular(VivSpacing.radiusSm),
      ),
      listBullet: p,
      h1: VivTypography.headingMd,
      h2: VivTypography.headingSm,
      h3: VivTypography.headingSm,
      blockquoteDecoration: BoxDecoration(
        color: VivColors.surfaceSunken,
        borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
      ),
    );
  }

  static Future<void> openLink(String text, String? href, String title) async {
    if (href == null) return;
    final uri = Uri.tryParse(href);
    if (uri == null) return;
    try {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    } catch (_) {
      // Lien non ouvrable : on ignore silencieusement.
    }
  }

  @override
  Widget build(BuildContext context) {
    return MarkdownBody(
      data: data,
      styleSheet: styleSheet(context, base: baseStyle),
      onTapLink: openLink,
    );
  }
}
