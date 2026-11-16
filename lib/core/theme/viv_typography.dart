import 'package:flutter/material.dart';
import 'viv_colors.dart';

/// Typographie du design system VIV Formation (`tokens/typography.css`).
///
/// Deux familles : Playfair Display Bold Italic pour les titres et les noms,
/// Noto Sans pour tout le reste. **Il n'existe pas de gras droit** : les
/// sous-titres sont en italique gras, les libellés et boutons en Regular, et la
/// hiérarchie vient de la taille, de la couleur et de l'espacement.
/// N'écrivez jamais `FontWeight.w500/w600/bold` sur une face droite.
class VivTypography {
  VivTypography._();

  static const String displayFont = 'Playfair Display';
  static const String sansFont = 'Noto Sans';
  static const String monoFont = 'Noto Sans Mono';

  // Titres Playfair — jamais sous 20 px, jamais en texte courant.
  static const TextStyle displayXl = TextStyle(
    fontFamily: displayFont,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
    fontSize: 56,
    height: 58 / 56,
    letterSpacing: -0.56,
    color: VivColors.ink,
  );

  static const TextStyle displayLg = TextStyle(
    fontFamily: displayFont,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
    fontSize: 40,
    height: 46 / 40,
    color: VivColors.ink,
  );

  /// Ouverture de chapitre, titre de section longue.
  static const TextStyle displayMd = TextStyle(
    fontFamily: displayFont,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
    fontSize: 32,
    height: 38 / 32,
    color: VivColors.ink,
  );

  static const TextStyle identity = TextStyle(
    fontFamily: displayFont,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
    fontSize: 20,
    height: 28 / 20,
    color: VivColors.ink,
  );

  // Sous-titres Noto Sans en italique gras (règle de charte, cartes comprises).
  static const TextStyle headingLg = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
    fontSize: 24,
    height: 32 / 24,
    color: VivColors.ink,
  );

  static const TextStyle headingMd = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
    fontSize: 20,
    height: 28 / 20,
    color: VivColors.ink,
  );

  static const TextStyle headingSm = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w700,
    fontStyle: FontStyle.italic,
    fontSize: 17,
    height: 24 / 17,
    color: VivColors.ink,
  );

  /// Sur-titre : à composer en capitales (`toUpperCase()`), Regular, ink-muted.
  static const TextStyle overline = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 12,
    height: 16 / 12,
    letterSpacing: 0.96,
    color: VivColors.inkMuted,
  );

  // Corps
  static const TextStyle bodyLg = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 17,
    height: 28 / 17,
    color: VivColors.ink,
  );

  static const TextStyle body = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 15,
    height: 24 / 15,
    color: VivColors.ink,
  );

  static const TextStyle bodySm = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 13,
    height: 20 / 13,
    color: VivColors.ink,
  );

  static const TextStyle quote = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontStyle: FontStyle.italic,
    fontSize: 20,
    height: 32 / 20,
    color: VivColors.ink,
  );

  /// Légende, mention, numéro de version — jamais sous 12 px.
  static const TextStyle caption = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w300,
    fontSize: 12,
    height: 18 / 12,
    color: VivColors.inkMuted,
  );

  static const TextStyle label = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 13,
    height: 18 / 13,
    color: VivColors.ink,
  );

  static const TextStyle button = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 15,
    height: 20 / 15,
  );

  static const TextStyle buttonSm = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 13,
    height: 18 / 13,
  );

  /// Valeur chiffrée, mise en avant par accent-deep, pas par le gras.
  static const TextStyle data = TextStyle(
    fontFamily: sansFont,
    fontWeight: FontWeight.w400,
    fontSize: 15,
    height: 22 / 15,
    letterSpacing: 0.15,
    color: VivColors.ink,
  );

  static const TextStyle code = TextStyle(
    fontFamily: monoFont,
    fontWeight: FontWeight.w400,
    fontSize: 14,
    height: 22 / 14,
    color: VivColors.ink,
  );

  static const TextStyle kbd = TextStyle(
    fontFamily: monoFont,
    fontWeight: FontWeight.w400,
    fontSize: 13,
    height: 18 / 13,
    color: VivColors.ink,
  );

  /// Mise en relief dans un texte courant (`**gras**` du Markdown) : la seule
  /// face grasse disponible est l'italique gras.
  static TextStyle strongOf(TextStyle base) =>
      base.copyWith(fontWeight: FontWeight.w700, fontStyle: FontStyle.italic);
}
