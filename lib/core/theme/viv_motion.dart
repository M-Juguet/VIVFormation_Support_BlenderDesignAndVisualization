import 'package:flutter/widgets.dart';

/// Mouvement du design system VIV Formation (`tokens/motion.css`) : trois durées,
/// trois courbes, huit pixels d'amplitude. Pas de rebond, pas d'élastique.
/// Le mouvement est une aide, jamais une condition.
class VivMotion {
  VivMotion._();

  /// Survol, focus, pression.
  static const Duration micro = Duration(milliseconds: 120);

  /// Encart, onglet, correction de quiz.
  static const Duration state = Duration(milliseconds: 200);

  /// Panneau latéral, modale, menu. Rien au-delà.
  static const Duration panel = Duration(milliseconds: 320);

  /// Ce qui arrive décélère.
  static const Curve enter = Cubic(0, 0, 0.2, 1);

  /// Ce qui part accélère.
  static const Curve exit = Cubic(0.4, 0, 1, 1);

  /// Ce qui se transforme sur place.
  static const Curve standard = Cubic(0.2, 0, 0, 1);

  /// Déplacement maximal d'une apparition.
  static const double shift = 8.0;

  /// Applique la règle « mouvement réduit » : si le système demande de couper
  /// les animations, toute transition tombe à 1 ms.
  static Duration of(BuildContext context, Duration duration) {
    final reduce = MediaQuery.maybeDisableAnimationsOf(context) ?? false;
    return reduce ? const Duration(milliseconds: 1) : duration;
  }
}
