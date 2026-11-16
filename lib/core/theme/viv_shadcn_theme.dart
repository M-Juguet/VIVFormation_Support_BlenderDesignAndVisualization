import 'package:flutter/material.dart';
import 'package:shadcn_ui/shadcn_ui.dart';
import 'viv_colors.dart';
import 'viv_spacing.dart';
import 'viv_typography.dart';

/// Thème shadcn_ui aligné sur le design system VIV Formation.
class VivShadcnTheme {
  VivShadcnTheme._();

  static ShadThemeData get lightTheme {
    const defaultColorScheme = ShadZincColorScheme.light();

    return ShadThemeData(
      colorScheme: defaultColorScheme.copyWith(
        background: VivColors.surface,
        foreground: VivColors.ink,
        card: VivColors.surfaceRaised,
        cardForeground: VivColors.ink,
        popover: VivColors.surfaceRaised,
        popoverForeground: VivColors.ink,
        primary: VivColors.action,
        primaryForeground: VivColors.onAction,
        secondary: VivColors.surfaceBrand,
        secondaryForeground: VivColors.action,
        muted: VivColors.surfaceSunken,
        mutedForeground: VivColors.inkMuted,
        accent: VivColors.surfaceBrand,
        accentForeground: VivColors.ink,
        destructive: VivColors.danger,
        destructiveForeground: VivColors.onAction,
        border: VivColors.border,
        input: VivColors.borderStrong,
        ring: VivColors.focus,
        selection: VivColors.brandRose,
      ),
      radius: BorderRadius.circular(VivSpacing.radiusMd),
      textTheme: ShadTextTheme(family: VivTypography.sansFont),
    );
  }
}
