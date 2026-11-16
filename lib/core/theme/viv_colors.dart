import 'package:flutter/material.dart';

/// Couleurs du design system VIV Formation (`viv-formation-design-system/tokens/colors.css`).
///
/// Les pastels de marque habillent, ils n'écrivent pas : le texte et les éléments
/// interactifs passent par [action], l'accent doré par [accentDeep].
/// Trois niveaux de texte : [ink], [inkMuted], [inkSubtle].
class VivColors {
  VivColors._();

  // Marque — les deux arrêts du dégradé du logo et leur milieu dérivé.
  static const Color brandRose = Color(0xFFDAA5BC);
  static const Color brandPeach = Color(0xFFEDC6A6);
  static const Color brandGold = Color(0xFFFBDE96);

  // Surfaces
  static const Color surface = Color(0xFFFFFFFF);
  static const Color surfaceSunken = Color(0xFFFAF6F7);
  static const Color surfaceRaised = Color(0xFFFFFFFF);
  static const Color surfaceBrand = Color(0xFFFBF1F5);
  static const Color surfaceAccent = Color(0xFFFDF6E8);
  static const Color surfaceCode = Color(0xFFF4F0F2);

  // Encres
  static const Color ink = Color(0xFF1C161B);
  static const Color inkMuted = Color(0xFF5A4E56);
  static const Color inkSubtle = Color(0xFF736570);
  static const Color inkOnPastel = Color(0xFF1C161B);
  static const Color inkInverse = Color(0xFFFFFFFF);

  // Action et accent
  static const Color action = Color(0xFF9C3F68);
  static const Color actionHover = Color(0xFF7F3253);
  static const Color onAction = Color(0xFFFFFFFF);
  static const Color accentDeep = Color(0xFF8F5C0E);

  // Filets et focus
  static const Color border = Color(0xFFECE3E6);
  static const Color borderStrong = Color(0xFF9A8490);
  static const Color focus = Color(0xFF9C3F68);

  // Statuts — toujours accompagnés d'un mot.
  static const Color success = Color(0xFF1F7A5C);
  static const Color successSurface = Color(0xFFEEF7F3);
  static const Color warning = Color(0xFF8F5C0E);
  static const Color warningSurface = Color(0xFFFDF6E8);
  static const Color danger = Color(0xFFB3261E);
  static const Color dangerSurface = Color(0xFFFDF0EF);
  static const Color info = Color(0xFF2F5F8F);
  static const Color infoSurface = Color(0xFFEEF3F9);

  /// Le dégradé du logo : deux arrêts, horizontal, plateaux aux extrémités.
  /// Jamais en vertical ni en diagonale.
  static const LinearGradient gradientBrand = LinearGradient(
    begin: Alignment.centerLeft,
    end: Alignment.centerRight,
    colors: [brandRose, brandRose, brandGold, brandGold],
    stops: [0.0, 0.15, 0.76, 1.0],
  );

  // Ombres
  static const List<BoxShadow> shadowSm = [
    BoxShadow(color: Color(0x141C161B), blurRadius: 2, offset: Offset(0, 1)),
  ];
  static const List<BoxShadow> shadowMd = [
    BoxShadow(color: Color(0x1A1C161B), blurRadius: 16, offset: Offset(0, 4)),
  ];
  static const List<BoxShadow> shadowLg = [
    BoxShadow(color: Color(0x241C161B), blurRadius: 40, offset: Offset(0, 16)),
  ];
}

/// Thème « sombre » du design system : bandes sombres (navigation, bandeau d'accueil)
/// et visionneuse d'images. Les pastels de marque y restent inchangés.
class VivDarkColors {
  VivDarkColors._();

  static const Color surface = Color(0xFF171216);
  static const Color surfaceSunken = Color(0xFF110D10);
  static const Color surfaceRaised = Color(0xFF221B21);
  static const Color surfaceBrand = Color(0xFF2B1F28);
  static const Color surfaceAccent = Color(0xFF2A2418);

  static const Color ink = Color(0xFFF7F2F4);
  static const Color inkMuted = Color(0xFFC6B8C0);
  static const Color inkSubtle = Color(0xFFA2939C);

  static const Color action = Color(0xFFF0B8CE);
  static const Color actionHover = Color(0xFFF8CFDF);
  static const Color onAction = Color(0xFF2B1119);
  static const Color accentDeep = Color(0xFFF3C86A);

  static const Color border = Color(0xFF332A31);
  static const Color borderStrong = Color(0xFF75636D);
  static const Color focus = Color(0xFFF0B8CE);

  /// Fond du verre dépoli posé sur un aplat sombre ou une image.
  static const Color glassSurface = Color(0x94221B21);
  static const Color glassBorder = Color(0x2EF7F2F4);
}
