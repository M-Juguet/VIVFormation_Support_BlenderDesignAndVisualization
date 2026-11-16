import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../core/data/course_data.dart';
import '../../core/models/content_module.dart';
import '../../core/models/content_module_labels.dart';
import '../../core/theme/viv_colors.dart';
import '../../core/theme/viv_spacing.dart';
import '../../core/theme/viv_typography.dart';
import '../../core/storage/bookmarks_provider.dart';
import '../../core/storage/chapter_progress_provider.dart';
import '../../core/widgets/viv_brand.dart';

class DashboardScreen extends ConsumerWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final bookmarkedIds = ref.watch(bookmarksProvider);
    final completedChapters = ref.watch(chapterProgressProvider);

    final allChapters = CourseData.chapters;
    final completedCount = allChapters.where((c) => completedChapters.contains(c.route)).length;
    final progress = completedCount / allChapters.length;
    final formation = CourseData.formation.toList();

    return Scaffold(
      backgroundColor: Colors.transparent, // Affiché dans la zone de contenu de MainShell
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(VivSpacing.space6),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // 1. Bandeau d'accueil : accès direct au prochain chapitre
            _buildHeroSection(context, completedCount, allChapters.length, progress, completedChapters),
            const SizedBox(height: VivSpacing.space8),

            // 2. Chapitres, signet récent et liens utiles
            LayoutBuilder(
              builder: (context, constraints) {
                final isLargeScreen = constraints.maxWidth > 960;
                final chaptersBlock = Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const VivOverline('Chapitres de formation'),
                    const SizedBox(height: VivSpacing.space3),
                    if (isLargeScreen)
                      GridView.builder(
                        shrinkWrap: true,
                        physics: const NeverScrollableScrollPhysics(),
                        itemCount: formation.length,
                        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                          crossAxisCount: 2,
                          crossAxisSpacing: VivSpacing.space6,
                          mainAxisSpacing: VivSpacing.space6,
                          mainAxisExtent: 236,
                        ),
                        itemBuilder: (context, index) => _buildChapterCard(
                          context,
                          formation[index],
                          completedChapters.contains(formation[index].route),
                        ),
                      )
                    else
                      ...formation.map((chapter) => Padding(
                            padding: const EdgeInsets.only(bottom: VivSpacing.space4),
                            child: _buildChapterCard(context, chapter, completedChapters.contains(chapter.route)),
                          )),
                  ],
                );
                final sideBlock = Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    _buildRecentBookmarksWidget(context, bookmarkedIds),
                    const SizedBox(height: VivSpacing.space6),
                    _buildUsefulLinksWidget(context),
                  ],
                );

                if (isLargeScreen) {
                  return Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Expanded(flex: 2, child: chaptersBlock),
                      const SizedBox(width: VivSpacing.space6),
                      Expanded(
                        flex: 1,
                        child: Padding(
                          padding: const EdgeInsets.only(top: VivSpacing.space6 + 4),
                          child: sideBlock,
                        ),
                      ),
                    ],
                  );
                }
                return Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [chaptersBlock, const SizedBox(height: VivSpacing.space4), sideBlock],
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  /// Bande sombre en haut de page, avec le motif de couverture de la marque.
  Widget _buildHeroSection(
    BuildContext context,
    int completedCount,
    int totalCount,
    double progress,
    Set<String> completedChapters,
  ) {
    CourseChapter? nextChapter;
    for (final c in CourseData.chapters) {
      if (!completedChapters.contains(c.route)) {
        nextChapter = c;
        break;
      }
    }

    final String nextTargetPath;
    final String buttonText;
    final IconData buttonIcon;
    if (nextChapter == null) {
      nextTargetPath = '/program';
      buttonText = 'Voir le programme complet';
      buttonIcon = LucideIcons.bookOpen;
    } else if (completedCount == 0) {
      nextTargetPath = nextChapter.route;
      buttonText = 'Commencer : ${nextChapter.title}';
      buttonIcon = LucideIcons.play;
    } else {
      nextTargetPath = nextChapter.route;
      buttonText = 'Continuer : ${nextChapter.shortLabel}';
      buttonIcon = LucideIcons.arrowRight;
    }

    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: VivDarkColors.surface,
        borderRadius: BorderRadius.circular(VivSpacing.radiusXl),
      ),
      clipBehavior: Clip.antiAlias,
      child: LayoutBuilder(
        builder: (context, constraints) {
          final showMotif = constraints.maxWidth > 860;
          return Stack(
            children: [
              // Motif de couverture confiné au tiers droit du bandeau : il remplit
              // la hauteur et déborde à gauche plutôt que de passer sous le texte.
              if (showMotif)
                Positioned(
                  right: 0,
                  top: 0,
                  bottom: 0,
                  width: constraints.maxWidth * 0.38,
                  child: const ClipRect(
                    child: FittedBox(
                      fit: BoxFit.cover,
                      alignment: Alignment.centerRight,
                      child: SizedBox(
                        width: 496,
                        height: 288,
                        child: VivCoverMotif(
                          background: VivDarkColors.surface,
                          deep: VivDarkColors.action,
                        ),
                      ),
                    ),
                  ),
                ),
              Padding(
                padding: const EdgeInsets.all(VivSpacing.space10),
                child: ConstrainedBox(
                  constraints: BoxConstraints(maxWidth: showMotif ? constraints.maxWidth * 0.62 - VivSpacing.space10 * 2 : 640),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const VivOverline('Formation en cours · ${CourseData.reference}', color: VivDarkColors.inkMuted),
                      const SizedBox(height: VivSpacing.space3),
                      Text(
                        CourseData.trainingTitle,
                        style: VivTypography.displayLg.copyWith(color: VivDarkColors.ink),
                      ),
                      const SizedBox(height: VivSpacing.space4),
                      Text(
                        'Parcourez les chapitres interactifs, testez vos acquis avec les quiz et retrouvez vos points clés grâce aux signets.',
                        style: VivTypography.bodyLg.copyWith(color: VivDarkColors.inkMuted),
                      ),
                      const SizedBox(height: VivSpacing.space6),
                      ConstrainedBox(
                        constraints: const BoxConstraints(maxWidth: 400),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Text(
                                  'Progression : $completedCount sur $totalCount chapitres',
                                  style: VivTypography.label.copyWith(color: VivDarkColors.ink),
                                ),
                                Text(
                                  '${(progress * 100).round()} %',
                                  style: VivTypography.label.copyWith(color: VivDarkColors.accentDeep),
                                ),
                              ],
                            ),
                            const SizedBox(height: VivSpacing.space2),
                            VivProgressBar(value: progress, onDark: true),
                          ],
                        ),
                      ),
                      const SizedBox(height: VivSpacing.space8),
                      ElevatedButton.icon(
                        onPressed: () => context.go(nextTargetPath),
                        style: VivButtonStyles.primary(onDark: true),
                        icon: Icon(buttonIcon, size: 16),
                        label: Text(buttonText, overflow: TextOverflow.ellipsis),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          );
        },
      ),
    );
  }

  /// Carte de module : filet de dégradé en tête, sur-titre, titre, résumé, pied.
  Widget _buildChapterCard(BuildContext context, CourseChapter chapter, bool isCompleted) {
    return VivCard(
      gradientStrip: true,
      onTap: () => context.go(chapter.route),
      child: SizedBox(
        height: 236 - VivSpacing.gradientLine - VivSpacing.space5 * 2 - 2,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(chapter.icon, color: VivColors.action, size: 20),
                const SizedBox(width: VivSpacing.space2),
                Expanded(child: VivOverline('Chapitre ${chapter.number.toString().padLeft(2, '0')}')),
                if (isCompleted)
                  const VivBadge('Terminé', tone: VivBadgeTone.success, icon: LucideIcons.check)
                else if (chapter.isInPreparation)
                  const VivBadge('En préparation'),
              ],
            ),
            const SizedBox(height: VivSpacing.space3),
            Text(chapter.title, style: VivTypography.headingMd, maxLines: 2, overflow: TextOverflow.ellipsis),
            const SizedBox(height: VivSpacing.space2),
            Expanded(
              child: Text(
                chapter.objective,
                style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted),
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
              ),
            ),
            const Divider(color: VivColors.border, height: VivSpacing.space4),
            Row(
              children: [
                Text('Y accéder', style: VivTypography.label.copyWith(color: VivColors.action)),
                const Spacer(),
                const Icon(LucideIcons.arrowRight, color: VivColors.action, size: 16),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildRecentBookmarksWidget(BuildContext context, Set<String> bookmarkedIds) {
    CourseChapter? recentChapter;
    ContentModule? recentModule;
    if (bookmarkedIds.isNotEmpty) {
      final targetId = bookmarkedIds.last;
      for (final chapter in CourseData.chapters) {
        for (final module in chapter.modules) {
          if (module.id == targetId) {
            recentChapter = chapter;
            recentModule = module;
          }
        }
      }
    }

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(VivSpacing.space5),
      decoration: VivDecorations.card(),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Row(
            children: [
              Icon(LucideIcons.bookmark, size: 18, color: VivColors.action),
              SizedBox(width: VivSpacing.space2),
              VivOverline('Signet récent'),
            ],
          ),
          const SizedBox(height: VivSpacing.space4),
          if (recentModule == null || recentChapter == null) ...[
            Text('Aucun signet enregistré', style: VivTypography.headingSm),
            const SizedBox(height: VivSpacing.space1),
            Text(
              'Marquez des paragraphes ou des quiz pendant votre lecture pour y revenir directement.',
              style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted),
            ),
          ] else ...[
            Text(recentModule.displayTitle, style: VivTypography.headingSm, maxLines: 2, overflow: TextOverflow.ellipsis),
            const SizedBox(height: VivSpacing.space1),
            Text(recentChapter.title, style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted)),
            const SizedBox(height: VivSpacing.space4),
            SizedBox(
              width: double.infinity,
              child: OutlinedButton(
                onPressed: () => context.go('${recentChapter!.route}?target=${recentModule!.id}'),
                style: VivButtonStyles.secondary(small: true),
                child: const Text('Y retourner'),
              ),
            ),
          ],
        ],
      ),
    );
  }

  Widget _buildUsefulLinksWidget(BuildContext context) {
    Future<void> launchUrlHelper(String urlString) async {
      try {
        await launchUrl(Uri.parse(urlString), mode: LaunchMode.externalApplication);
      } catch (e) {
        debugPrint('Erreur lors du lancement de l\'URL : $e');
      }
    }

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(VivSpacing.space5),
      decoration: VivDecorations.card(),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Row(
            children: [
              Icon(LucideIcons.link, size: 18, color: VivColors.action),
              SizedBox(width: VivSpacing.space2),
              VivOverline('Ressources utiles'),
            ],
          ),
          const SizedBox(height: VivSpacing.space3),
          _buildLinkItem(
            icon: LucideIcons.fileText,
            label: 'Documentation officielle de Blender',
            onTap: () => launchUrlHelper('https://docs.blender.org/manual/fr/latest/'),
          ),
          const Divider(height: VivSpacing.space4, color: VivColors.border),
          _buildLinkItem(
            icon: LucideIcons.download,
            label: 'Télécharger Blender',
            onTap: () => launchUrlHelper('https://www.blender.org/download/'),
          ),
        ],
      ),
    );
  }

  Widget _buildLinkItem({
    required IconData icon,
    required String label,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(VivSpacing.radiusSm),
      hoverColor: VivColors.surfaceBrand,
      child: Padding(
        padding: const EdgeInsets.symmetric(vertical: VivSpacing.space2, horizontal: VivSpacing.space1),
        child: Row(
          children: [
            Icon(icon, size: 16, color: VivColors.inkMuted),
            const SizedBox(width: VivSpacing.space3),
            Expanded(child: Text(label, style: VivTypography.body)),
            const Icon(LucideIcons.externalLink, size: 14, color: VivColors.inkSubtle),
          ],
        ),
      ),
    );
  }
}
