/// Échelle d'espacement de 4 px et rayons du design system VIV Formation
/// (`tokens/space.css`). Padding de carte space5, écart entre cartes space6,
/// entre sections space12.
class VivSpacing {
  VivSpacing._();

  static const double space1 = 4.0;
  static const double space2 = 8.0;
  static const double space3 = 12.0;
  static const double space4 = 16.0;
  static const double space5 = 20.0;
  static const double space6 = 24.0;
  static const double space8 = 32.0;
  static const double space10 = 40.0;
  static const double space12 = 48.0;
  static const double space16 = 64.0;

  // Rayons — ligne douce et amicale, à grands rayons.
  static const double radiusSm = 6.0; // champs, cases, petites vignettes
  static const double radiusMd = 10.0; // boutons, badges rectangulaires, encarts
  static const double radiusLg = 18.0; // cartes, panneaux, images
  static const double radiusXl = 28.0; // grands blocs de couverture
  static const double radiusPill = 999.0; // badges de statut, pastilles

  /// Hauteur du filet de dégradé de marque.
  static const double gradientLine = 4.0;
}
