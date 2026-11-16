import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import '../theme/viv_colors.dart';
import '../theme/viv_motion.dart';
import '../theme/viv_spacing.dart';
import '../theme/viv_typography.dart';

/// Composants de marque VIV Formation transposés en Flutter.
/// Référence : `viv-formation-design-system/` (readme, tokens, components).

// ---------------------------------------------------------------------------
// Filet de dégradé
// ---------------------------------------------------------------------------

/// Filet de 4 px au dégradé de marque : sous un en-tête, en tête d'une carte
/// de module, sous une section. Toujours horizontal.
class VivGradientLine extends StatelessWidget {
  final double height;

  const VivGradientLine({super.key, this.height = VivSpacing.gradientLine});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: height,
      decoration: const BoxDecoration(gradient: VivColors.gradientBrand),
    );
  }
}

// ---------------------------------------------------------------------------
// Logos — jamais de reconstitution typographique, le SVG fait référence.
// ---------------------------------------------------------------------------

enum VivLogoInk { couleur, blanc, noir }

class VivLogo extends StatelessWidget {
  final String _asset;
  final double height;

  const VivLogo._(this._asset, this.height, {super.key});

  /// Logo complet : `couleur` sur fond clair, `blanc` sur fond sombre.
  /// Largeur minimale 120 px.
  factory VivLogo.full({Key? key, VivLogoInk ink = VivLogoInk.couleur, double height = 24}) =>
      VivLogo._('assets/logos/viv-formation-${ink.name}.svg', height, key: key);

  /// Monogramme « Viv » : quand la place manque. Minimum 24 px.
  factory VivLogo.monogramme({Key? key, VivLogoInk ink = VivLogoInk.couleur, double height = 24}) =>
      VivLogo._('assets/logos/viv-monogramme-${ink.name}.svg', height, key: key);

  /// Submark (le V seul), uniquement en noir ou blanc : formats minuscules.
  factory VivLogo.submark({Key? key, bool onDark = true, double height = 24}) =>
      VivLogo._('assets/logos/viv-submark-${onDark ? 'blanc' : 'noir'}.svg', height, key: key);

  @override
  Widget build(BuildContext context) {
    return SvgPicture.asset(
      _asset,
      height: height,
      fit: BoxFit.contain,
      semanticsLabel: 'VIV Formation',
    );
  }
}

// ---------------------------------------------------------------------------
// Typographie de structure
// ---------------------------------------------------------------------------

/// Sur-titre en capitales : numéro de module, catégorie. Regular, ink-muted.
class VivOverline extends StatelessWidget {
  final String text;
  final Color? color;

  const VivOverline(this.text, {super.key, this.color});

  @override
  Widget build(BuildContext context) {
    return Text(
      text.toUpperCase(),
      style: VivTypography.overline.copyWith(color: color ?? VivColors.inkMuted),
    );
  }
}

// ---------------------------------------------------------------------------
// Cartes
// ---------------------------------------------------------------------------

class VivDecorations {
  VivDecorations._();

  /// Carte : surface-raised, filet border, radius-lg, shadow-sm (shadow-md au survol).
  static BoxDecoration card({bool hovered = false}) => BoxDecoration(
        color: VivColors.surfaceRaised,
        borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
        border: Border.all(color: VivColors.border),
        boxShadow: hovered ? VivColors.shadowMd : VivColors.shadowSm,
      );

  /// Carte plate (sans ombre), pour les panneaux de réglages.
  static BoxDecoration flatCard() => BoxDecoration(
        color: VivColors.surfaceRaised,
        borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
        border: Border.all(color: VivColors.border),
      );
}

/// Carte cliquable du système : ombre douce au repos, `shadow-md` au survol,
/// filet de dégradé optionnel en tête (carte de module).
class VivCard extends StatefulWidget {
  final Widget child;
  final VoidCallback? onTap;
  final EdgeInsetsGeometry padding;
  final bool gradientStrip;

  const VivCard({
    super.key,
    required this.child,
    this.onTap,
    this.padding = const EdgeInsets.all(VivSpacing.space5),
    this.gradientStrip = false,
  });

  @override
  State<VivCard> createState() => _VivCardState();
}

class _VivCardState extends State<VivCard> {
  bool _hovered = false;

  @override
  Widget build(BuildContext context) {
    final interactive = widget.onTap != null;
    return MouseRegion(
      cursor: interactive ? SystemMouseCursors.click : MouseCursor.defer,
      onEnter: interactive ? (_) => setState(() => _hovered = true) : null,
      onExit: interactive ? (_) => setState(() => _hovered = false) : null,
      child: AnimatedContainer(
        duration: VivMotion.of(context, VivMotion.state),
        curve: VivMotion.standard,
        decoration: VivDecorations.card(hovered: _hovered),
        clipBehavior: Clip.antiAlias,
        child: Material(
          type: MaterialType.transparency,
          child: InkWell(
            onTap: widget.onTap,
            splashFactory: NoSplash.splashFactory,
            hoverColor: Colors.transparent,
            highlightColor: Colors.transparent,
            focusColor: VivColors.surfaceBrand,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                if (widget.gradientStrip) const VivGradientLine(),
                Padding(padding: widget.padding, child: widget.child),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Badges
// ---------------------------------------------------------------------------

enum VivBadgeTone { neutral, rose, peach, gold, success, warning, danger, info }

/// Étiquette courte en pilule. Regular, jamais de gras.
class VivBadge extends StatelessWidget {
  final String text;
  final VivBadgeTone tone;
  final IconData? icon;

  const VivBadge(this.text, {super.key, this.tone = VivBadgeTone.neutral, this.icon});

  @override
  Widget build(BuildContext context) {
    final (Color bg, Color fg, Color? borderColor) = switch (tone) {
      VivBadgeTone.neutral => (VivColors.surfaceSunken, VivColors.inkMuted, VivColors.border),
      VivBadgeTone.rose => (VivColors.brandRose, VivColors.inkOnPastel, null),
      VivBadgeTone.peach => (VivColors.brandPeach, VivColors.inkOnPastel, null),
      VivBadgeTone.gold => (VivColors.brandGold, VivColors.inkOnPastel, null),
      VivBadgeTone.success => (VivColors.successSurface, VivColors.success, null),
      VivBadgeTone.warning => (VivColors.warningSurface, VivColors.warning, null),
      VivBadgeTone.danger => (VivColors.dangerSurface, VivColors.danger, null),
      VivBadgeTone.info => (VivColors.infoSurface, VivColors.info, null),
    };
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space3, vertical: VivSpacing.space1),
      decoration: BoxDecoration(
        color: bg,
        borderRadius: BorderRadius.circular(VivSpacing.radiusPill),
        border: borderColor != null ? Border.all(color: borderColor) : null,
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (icon != null) ...[
            Icon(icon, size: 14, color: fg),
            const SizedBox(width: VivSpacing.space1),
          ],
          Text(text, style: VivTypography.label.copyWith(color: fg)),
        ],
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Barre de progression — anime sa largeur, jamais sa couleur.
// ---------------------------------------------------------------------------

class VivProgressBar extends StatelessWidget {
  final double value;
  final bool onDark;

  const VivProgressBar({super.key, required this.value, this.onDark = false});

  @override
  Widget build(BuildContext context) {
    final v = value.clamp(0.0, 1.0);
    return Container(
      height: 8,
      decoration: BoxDecoration(
        color: onDark ? VivDarkColors.surfaceSunken : VivColors.surfaceSunken,
        borderRadius: BorderRadius.circular(VivSpacing.radiusPill),
        border: Border.all(color: onDark ? VivDarkColors.border : VivColors.border),
      ),
      clipBehavior: Clip.antiAlias,
      child: LayoutBuilder(
        builder: (context, constraints) => Align(
          alignment: Alignment.centerLeft,
          child: AnimatedContainer(
            duration: VivMotion.of(context, VivMotion.state),
            curve: VivMotion.standard,
            width: constraints.maxWidth * v,
            decoration: BoxDecoration(
              gradient: VivColors.gradientBrand,
              borderRadius: BorderRadius.circular(VivSpacing.radiusPill),
            ),
          ),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Encart d'objectifs pédagogiques
// ---------------------------------------------------------------------------

/// Objectifs sur `surface-accent`, titre en `accent-deep`, puces numérotées dorées.
class VivObjectivesPanel extends StatelessWidget {
  final String title;
  final List<String> items;

  const VivObjectivesPanel({
    super.key,
    this.title = 'Objectifs pédagogiques',
    required this.items,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(VivSpacing.space6),
      decoration: BoxDecoration(
        color: VivColors.surfaceAccent,
        borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: VivTypography.headingSm.copyWith(color: VivColors.accentDeep)),
          const SizedBox(height: VivSpacing.space4),
          for (var i = 0; i < items.length; i++)
            Padding(
              padding: EdgeInsets.only(bottom: i == items.length - 1 ? 0 : VivSpacing.space3),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  if (items.length > 1)
                    Container(
                      width: 22,
                      height: 22,
                      margin: const EdgeInsets.only(top: 1, right: VivSpacing.space3),
                      alignment: Alignment.center,
                      decoration: const BoxDecoration(
                        color: VivColors.brandGold,
                        shape: BoxShape.circle,
                      ),
                      child: Text(
                        '${i + 1}',
                        style: VivTypography.caption.copyWith(
                          color: VivColors.inkOnPastel,
                          fontWeight: FontWeight.w400,
                        ),
                      ),
                    ),
                  Expanded(child: Text(items[i], style: VivTypography.body)),
                ],
              ),
            ),
        ],
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Boutons
// ---------------------------------------------------------------------------

/// Styles de bouton du système : un seul `primary` plein par écran, les autres
/// en `secondary` (contour border-strong) ou `ghost`.
class VivButtonStyles {
  VivButtonStyles._();

  static const EdgeInsets _padding =
      EdgeInsets.symmetric(horizontal: VivSpacing.space5, vertical: VivSpacing.space3);
  static const EdgeInsets _paddingSm =
      EdgeInsets.symmetric(horizontal: VivSpacing.space3, vertical: VivSpacing.space2);

  static ButtonStyle primary({bool onDark = false, bool small = false}) {
    final base = onDark ? VivDarkColors.action : VivColors.action;
    final hover = onDark ? VivDarkColors.actionHover : VivColors.actionHover;
    final fg = onDark ? VivDarkColors.onAction : VivColors.onAction;
    return ButtonStyle(
      backgroundColor: WidgetStateProperty.resolveWith((s) {
        if (s.contains(WidgetState.disabled)) return base.withValues(alpha: 0.45);
        if (s.contains(WidgetState.hovered) || s.contains(WidgetState.pressed)) return hover;
        return base;
      }),
      foregroundColor: WidgetStateProperty.resolveWith(
        (s) => s.contains(WidgetState.disabled) ? fg.withValues(alpha: 0.45) : fg,
      ),
      iconColor: WidgetStateProperty.resolveWith(
        (s) => s.contains(WidgetState.disabled) ? fg.withValues(alpha: 0.45) : fg,
      ),
      overlayColor: const WidgetStatePropertyAll(Colors.transparent),
      elevation: const WidgetStatePropertyAll(0),
      padding: WidgetStatePropertyAll(small ? _paddingSm : _padding),
      textStyle: WidgetStatePropertyAll(small ? VivTypography.buttonSm : VivTypography.button),
      shape: WidgetStatePropertyAll(
        RoundedRectangleBorder(borderRadius: BorderRadius.circular(VivSpacing.radiusMd)),
      ),
      animationDuration: VivMotion.micro,
    );
  }

  static ButtonStyle secondary({bool onDark = false, bool small = false}) {
    final action = onDark ? VivDarkColors.action : VivColors.action;
    final strong = onDark ? VivDarkColors.borderStrong : VivColors.borderStrong;
    final brand = onDark ? VivDarkColors.surfaceBrand : VivColors.surfaceBrand;
    return ButtonStyle(
      backgroundColor: WidgetStateProperty.resolveWith(
        (s) => (s.contains(WidgetState.hovered) || s.contains(WidgetState.pressed)) ? brand : Colors.transparent,
      ),
      foregroundColor: WidgetStateProperty.resolveWith(
        (s) => s.contains(WidgetState.disabled) ? action.withValues(alpha: 0.45) : action,
      ),
      iconColor: WidgetStatePropertyAll(action),
      side: WidgetStateProperty.resolveWith(
        (s) => BorderSide(
          color: (s.contains(WidgetState.hovered) || s.contains(WidgetState.pressed)) ? action : strong,
        ),
      ),
      overlayColor: const WidgetStatePropertyAll(Colors.transparent),
      elevation: const WidgetStatePropertyAll(0),
      padding: WidgetStatePropertyAll(small ? _paddingSm : _padding),
      textStyle: WidgetStatePropertyAll(small ? VivTypography.buttonSm : VivTypography.button),
      shape: WidgetStatePropertyAll(
        RoundedRectangleBorder(borderRadius: BorderRadius.circular(VivSpacing.radiusMd)),
      ),
      animationDuration: VivMotion.micro,
    );
  }

  static ButtonStyle ghost({bool small = false}) {
    return ButtonStyle(
      backgroundColor: WidgetStateProperty.resolveWith(
        (s) => (s.contains(WidgetState.hovered) || s.contains(WidgetState.pressed))
            ? VivColors.surfaceBrand
            : Colors.transparent,
      ),
      foregroundColor: const WidgetStatePropertyAll(VivColors.action),
      iconColor: const WidgetStatePropertyAll(VivColors.action),
      overlayColor: const WidgetStatePropertyAll(Colors.transparent),
      padding: WidgetStatePropertyAll(small ? _paddingSm : _padding),
      textStyle: WidgetStatePropertyAll(small ? VivTypography.buttonSm : VivTypography.button),
      shape: WidgetStatePropertyAll(
        RoundedRectangleBorder(borderRadius: BorderRadius.circular(VivSpacing.radiusMd)),
      ),
      animationDuration: VivMotion.micro,
    );
  }
}

// ---------------------------------------------------------------------------
// Motif de couverture
// ---------------------------------------------------------------------------

/// Motif de couverture de la marque : blocs pastel aux coins radius-xl / radius-lg
/// posés au pas de 32 px, dans lesquels des disques et des pilules sont découpés
/// à la couleur du fond. Repris de la carte « Motif de couverture ».
class VivCoverMotif extends StatelessWidget {
  /// Couleur du fond sur lequel le motif est posé (couleur des découpes).
  final Color background;

  /// Couleur du bloc foncé (action du thème courant).
  final Color deep;

  const VivCoverMotif({
    super.key,
    this.background = VivColors.surface,
    this.deep = VivColors.action,
  });

  /// Proportions du motif (zone droite de la planche de 960 × 288).
  static const double aspectRatio = 496 / 288;

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: aspectRatio,
      child: CustomPaint(painter: _CoverMotifPainter(background, deep)),
    );
  }
}

class _CoverMotifPainter extends CustomPainter {
  final Color background;
  final Color deep;

  _CoverMotifPainter(this.background, this.deep);

  @override
  void paint(Canvas canvas, Size size) {
    final s = size.width / 496;
    canvas.save();
    canvas.clipRect(Offset.zero & size);
    canvas.scale(s);

    void block(double x, double y, double w, double h, double r, Color c) {
      canvas.drawRRect(
        RRect.fromRectAndRadius(Rect.fromLTWH(x, y, w, h), Radius.circular(r)),
        Paint()..color = c,
      );
    }

    final cut = Paint()..color = background;
    void disc(double cx, double cy, double r) => canvas.drawCircle(Offset(cx, cy), r, cut);

    block(0, -24, 152, 336, 28, VivColors.brandRose);
    block(184, 32, 160, 104, 18, VivColors.brandPeach);
    block(376, 32, 120, 104, 18, deep);
    block(184, 168, 312, 104, 18, VivColors.brandGold);

    for (final y in [48.0, 104.0, 160.0, 216.0, 272.0]) {
      disc(76, y, 14);
    }
    for (final x in [216.0, 264.0, 312.0]) {
      disc(x, 84, 14);
    }
    disc(408, 84, 14);
    disc(456, 84, 14);
    canvas.drawRRect(
      RRect.fromRectAndRadius(const Rect.fromLTWH(216, 204, 128, 32), const Radius.circular(16)),
      cut,
    );
    disc(384, 220, 16);
    disc(440, 220, 16);

    canvas.restore();
  }

  @override
  bool shouldRepaint(_CoverMotifPainter old) => old.background != background || old.deep != deep;
}
