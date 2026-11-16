import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';

import '../../core/data/course_data.dart';
import '../../core/models/content_module.dart';
import '../../core/models/content_module_labels.dart';
import '../../core/theme/viv_colors.dart';
import '../../core/theme/viv_spacing.dart';
import '../../core/theme/viv_typography.dart';
import '../../core/storage/bookmarks_provider.dart';
import '../../core/widgets/viv_brand.dart';

class BookmarkItemData {
  final CourseChapter chapter;
  final ContentModule module;

  const BookmarkItemData({required this.chapter, required this.module});
}

class BookmarksScreen extends ConsumerWidget {
  const BookmarksScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final bookmarkedIds = ref.watch(bookmarksProvider);

    // Tous les chapitres du registre, dans l'ordre du parcours.
    final bookmarkedItems = <BookmarkItemData>[
      for (final chapter in CourseData.chapters)
        for (final module in chapter.modules)
          if (bookmarkedIds.contains(module.id)) BookmarkItemData(chapter: chapter, module: module),
    ];

    return Scaffold(
      backgroundColor: Colors.transparent, // Affiché dans la zone de contenu de MainShell
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(VivSpacing.space6),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const VivOverline('Mes signets'),
            const SizedBox(height: VivSpacing.space3),
            Text('Points techniques favoris', style: VivTypography.displayLg),
            const SizedBox(height: VivSpacing.space4),
            ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 800),
              child: Text(
                'Retrouvez ici les modules et points précis que vous avez marqués d\'un signet au fil de la formation. Cliquez sur un élément pour l\'ouvrir directement.',
                style: VivTypography.bodyLg.copyWith(color: VivColors.inkMuted),
              ),
            ),
            const SizedBox(height: VivSpacing.space10),
            if (bookmarkedItems.isEmpty)
              _buildEmptyState()
            else
              Column(children: bookmarkedItems.map((item) => _buildBookmarkCard(context, ref, item)).toList()),
          ],
        ),
      ),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Padding(
        padding: const EdgeInsets.symmetric(vertical: VivSpacing.space12),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: const EdgeInsets.all(VivSpacing.space5),
              decoration: const BoxDecoration(color: VivColors.surfaceBrand, shape: BoxShape.circle),
              child: const Icon(LucideIcons.bookmark, size: 40, color: VivColors.action),
            ),
            const SizedBox(height: VivSpacing.space5),
            Text('Aucun signet pour le moment', style: VivTypography.headingMd),
            const SizedBox(height: VivSpacing.space2),
            ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 420),
              child: Text(
                'Dans un chapitre, cliquez sur l\'icône de signet à gauche d\'un paragraphe ou d\'un quiz pour le retrouver ici.',
                textAlign: TextAlign.center,
                style: VivTypography.body.copyWith(color: VivColors.inkMuted),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildBookmarkCard(BuildContext context, WidgetRef ref, BookmarkItemData item) {
    return Padding(
      padding: const EdgeInsets.only(bottom: VivSpacing.space4),
      child: VivCard(
        onTap: () => context.go('${item.chapter.route}?target=${item.module.id}'),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(VivSpacing.space3),
              decoration: BoxDecoration(
                color: VivColors.surfaceBrand,
                borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
              ),
              child: Icon(item.module.typeIcon, color: VivColors.action, size: 20),
            ),
            const SizedBox(width: VivSpacing.space4),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(item.module.displayTitle, style: VivTypography.headingSm, maxLines: 1, overflow: TextOverflow.ellipsis),
                  const SizedBox(height: VivSpacing.space1),
                  Text(
                    '${item.chapter.shortLabel} · ${item.chapter.title}',
                    style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted),
                  ),
                ],
              ),
            ),
            const SizedBox(width: VivSpacing.space3),
            IconButton(
              icon: const Icon(LucideIcons.bookmarkMinus, color: VivColors.action, size: 20),
              onPressed: () => ref.read(bookmarksProvider.notifier).toggleBookmark(item.module.id),
              tooltip: 'Retirer des signets',
            ),
            const Icon(LucideIcons.chevronRight, color: VivColors.inkSubtle, size: 16),
          ],
        ),
      ),
    );
  }
}
