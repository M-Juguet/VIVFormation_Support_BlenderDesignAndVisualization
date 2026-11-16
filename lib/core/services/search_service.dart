import '../models/content_module.dart';
import '../models/content_module_labels.dart';
import '../data/course_data.dart';

class SearchResult {
  final String chapterTitle;
  final String routePath;
  final int chapterIndex;
  final String moduleId;
  final String moduleType;
  final String moduleTitle;
  final String snippet;

  SearchResult({
    required this.chapterTitle,
    required this.routePath,
    required this.chapterIndex,
    required this.moduleId,
    required this.moduleType,
    required this.moduleTitle,
    required this.snippet,
  });
}

class SearchService {
  static List<SearchResult> search(String query) {
    if (query.trim().isEmpty) return [];

    final cleanQuery = query.trim().toLowerCase();
    final List<SearchResult> results = [];

    // Tous les chapitres du registre, dans l'ordre du parcours.
    for (final chapter in CourseData.chapters) {
      for (final module in chapter.modules) {
        final matches = _matchModule(module, cleanQuery);
        if (matches.isMatch) {
          results.add(SearchResult(
            chapterTitle: chapter.title,
            routePath: chapter.route,
            chapterIndex: chapter.branchIndex,
            moduleId: module.id,
            moduleType: module.typeKey,
            moduleTitle: _getModuleTitle(module),
            snippet: matches.snippet,
          ));
        }
      }
    }

    return results;
  }

  static _SearchMatch _matchModule(ContentModule module, String query) {
    if (module is TitleModule) {
      if (module.title.toLowerCase().contains(query)) {
        return _SearchMatch(true, module.title);
      }
    } else if (module is TextModule) {
      if (module.title != null && module.title!.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.title!, query));
      }
      if (module.content.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.content, query));
      }
    } else if (module is SideBySideModule) {
      if (module.title != null && module.title!.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.title!, query));
      }
      if (module.content.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.content, query));
      }
      if (module.caption != null && module.caption!.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.caption!, query));
      }
    } else if (module is FullMediaModule) {
      if (module.caption != null && module.caption!.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.caption!, query));
      }
    } else if (module is InfoModule) {
      if (module.text.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.text, query));
      }
    } else if (module is ResourceModule) {
      if (module.title.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.title, query));
      }
      if (module.description.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.description, query));
      }
      if (module.fileName.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.fileName, query));
      }
    } else if (module is ListModule) {
      if (module.title.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.title, query));
      }
      if (module.intro != null && module.intro!.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.intro!, query));
      }
      for (var item in module.items) {
        if (item.toLowerCase().contains(query)) {
          return _SearchMatch(true, _generateSnippet(item, query));
        }
      }
      if (module.outro != null && module.outro!.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.outro!, query));
      }
    } else if (module is QuizModule) {
      if (module.question.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.question, query));
      }
      for (var opt in module.options) {
        if (opt.toLowerCase().contains(query)) {
          return _SearchMatch(true, _generateSnippet(opt, query));
        }
      }
      if (module.explanation.toLowerCase().contains(query)) {
        return _SearchMatch(true, _generateSnippet(module.explanation, query));
      }
    }

    return const _SearchMatch(false, '');
  }

  static String _generateSnippet(String text, String query) {
    final index = text.toLowerCase().indexOf(query);
    if (index == -1) {
      return text.length > 80 ? '${text.substring(0, 80)}...' : text;
    }
    final start = (index - 40).clamp(0, text.length);
    final end = (index + query.length + 40).clamp(0, text.length);
    var snippet = text.substring(start, end);
    if (start > 0) snippet = '...$snippet';
    if (end < text.length) snippet = '$snippet...';
    return snippet.replaceAll('\n', ' ');
  }

  static String _getModuleTitle(ContentModule module) {
    if (module is TitleModule) return module.title;
    if (module is TextModule) return module.title ?? 'Texte explicatif';
    if (module is SideBySideModule) return module.title ?? 'Module scindé';
    if (module is FullMediaModule) return module.caption ?? 'Image pleine largeur';
    if (module is InfoModule) return module.type.label;
    if (module is ResourceModule) return module.title;
    if (module is ListModule) return module.title;
    if (module is QuizModule) return 'Quiz';
    return 'Module de contenu';
  }
}

class _SearchMatch {
  final bool isMatch;
  final String snippet;

  const _SearchMatch(this.isMatch, this.snippet);
}
