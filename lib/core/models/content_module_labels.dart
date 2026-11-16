import 'package:flutter/widgets.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';

import 'content_module.dart';

/// Libellés et icônes communs à la recherche, aux signets et au tableau de bord.
extension ContentModuleLabels on ContentModule {
  /// Clé de type stable (utilisée par la recherche).
  String get typeKey => switch (this) {
        TitleModule() => 'title',
        TextModule() => 'text',
        SideBySideModule() => 'sideBySide',
        FullMediaModule() => 'media',
        InfoModule() => 'info',
        ResourceModule() => 'resource',
        ListModule() => 'list',
        QuizModule() => 'quiz',
        _ => 'unknown',
      };

  IconData get typeIcon {
    final m = this;
    return switch (m) {
      TitleModule() => LucideIcons.heading,
      TextModule() => LucideIcons.textAlignStart,
      SideBySideModule() => LucideIcons.columns2,
      FullMediaModule() => LucideIcons.image,
      InfoModule() => m.type.icon,
      ResourceModule() => LucideIcons.download,
      ListModule() => LucideIcons.list,
      QuizModule() => LucideIcons.circleQuestionMark,
      _ => LucideIcons.fileText,
    };
  }

  /// Titre lisible d'un module, tronqué si le module n'a pas de titre propre.
  String get displayTitle {
    final m = this;
    String cut(String s, int max) {
      final t = s.trim();
      return t.length > max ? '${t.substring(0, max - 3)}...' : t;
    }

    return switch (m) {
      TitleModule() => m.title,
      TextModule() => (m.title?.trim().isNotEmpty ?? false) ? m.title! : cut(m.content, 60),
      SideBySideModule() => (m.title?.trim().isNotEmpty ?? false) ? m.title! : cut(m.content, 60),
      FullMediaModule() => (m.caption?.trim().isNotEmpty ?? false) ? m.caption! : 'Illustration pleine largeur',
      InfoModule() => '${m.type.label} : ${cut(m.text, 50)}',
      ResourceModule() => 'Ressource : ${m.title.trim().isNotEmpty ? m.title : m.fileName}',
      ListModule() => m.title.trim().isNotEmpty ? m.title : 'Liste de points',
      QuizModule() => 'Quiz : ${cut(m.question, 50)}',
      _ => 'Point technique',
    };
  }
}

/// Libellé et icône de chaque type d'encart.
extension InfoTypeLabels on InfoType {
  String get label => switch (this) {
        InfoType.idea => 'Idée',
        InfoType.tip => 'Conseil d\'expert',
        InfoType.warning => 'Attention',
        InfoType.info => 'Information',
        InfoType.objective => 'Objectif',
        InfoType.challenge => 'Défi fil rouge',
      };

  IconData get icon => switch (this) {
        InfoType.idea => LucideIcons.lightbulb,
        InfoType.tip => LucideIcons.sparkles,
        InfoType.warning => LucideIcons.triangleAlert,
        InfoType.info => LucideIcons.info,
        InfoType.objective => LucideIcons.target,
        InfoType.challenge => LucideIcons.flag,
      };
}
