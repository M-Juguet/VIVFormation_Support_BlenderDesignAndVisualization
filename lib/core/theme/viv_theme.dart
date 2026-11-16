import 'package:flutter/material.dart';
import 'viv_colors.dart';
import 'viv_spacing.dart';
import 'viv_typography.dart';

/// Thème Material aligné sur le design system VIV Formation.
class VivTheme {
  VivTheme._();

  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      colorScheme: const ColorScheme.light(
        primary: VivColors.action,
        onPrimary: VivColors.onAction,
        secondary: VivColors.brandGold,
        onSecondary: VivColors.inkOnPastel,
        surface: VivColors.surface,
        onSurface: VivColors.ink,
        onSurfaceVariant: VivColors.inkMuted,
        outline: VivColors.borderStrong,
        outlineVariant: VivColors.border,
        error: VivColors.danger,
        onError: VivColors.onAction,
      ),
      scaffoldBackgroundColor: VivColors.surfaceSunken,
      fontFamily: VivTypography.sansFont,
      textTheme: const TextTheme(
        displayLarge: VivTypography.displayXl,
        displayMedium: VivTypography.displayLg,
        displaySmall: VivTypography.displayMd,
        headlineMedium: VivTypography.headingLg,
        headlineSmall: VivTypography.headingMd,
        titleMedium: VivTypography.headingSm,
        bodyLarge: VivTypography.bodyLg,
        bodyMedium: VivTypography.body,
        bodySmall: VivTypography.bodySm,
        labelLarge: VivTypography.button,
        labelMedium: VivTypography.label,
        labelSmall: VivTypography.caption,
      ),
      textSelectionTheme: const TextSelectionThemeData(
        cursorColor: VivColors.action,
        selectionColor: VivColors.brandRose,
        selectionHandleColor: VivColors.action,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: VivColors.surface,
        elevation: 0,
        iconTheme: IconThemeData(color: VivColors.ink),
        titleTextStyle: VivTypography.headingMd,
      ),
      iconTheme: const IconThemeData(color: VivColors.ink, size: 20),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: VivColors.action,
          foregroundColor: VivColors.onAction,
          textStyle: VivTypography.button,
          padding: const EdgeInsets.symmetric(
            horizontal: VivSpacing.space5,
            vertical: VivSpacing.space3,
          ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
          ),
          elevation: 0,
        ),
      ),
      checkboxTheme: CheckboxThemeData(
        fillColor: WidgetStateProperty.resolveWith(
          (states) => states.contains(WidgetState.selected) ? VivColors.action : Colors.transparent,
        ),
        checkColor: const WidgetStatePropertyAll(VivColors.onAction),
        side: const BorderSide(color: VivColors.borderStrong, width: 1.5),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(4)),
      ),
      tooltipTheme: TooltipThemeData(
        decoration: BoxDecoration(
          color: VivColors.ink,
          borderRadius: BorderRadius.circular(VivSpacing.radiusSm),
        ),
        textStyle: VivTypography.label.copyWith(color: VivColors.inkInverse),
      ),
      snackBarTheme: SnackBarThemeData(
        backgroundColor: VivColors.ink,
        contentTextStyle: VivTypography.body.copyWith(color: VivColors.inkInverse),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
        ),
      ),
      dividerTheme: const DividerThemeData(
        color: VivColors.border,
        thickness: 1,
        space: VivSpacing.space4,
      ),
      progressIndicatorTheme: const ProgressIndicatorThemeData(
        color: VivColors.action,
      ),
    );
  }
}
