import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import 'package:go_router/go_router.dart';
import 'package:cached_network_image/cached_network_image.dart';

import '../data/course_data.dart';
import '../models/content_module.dart';
import 'content_module_renderer.dart';
import 'chapter_outline_widget.dart';
import 'viv_brand.dart';
import '../theme/viv_colors.dart';
import '../theme/viv_motion.dart';
import '../theme/viv_spacing.dart';
import '../theme/viv_typography.dart';
import '../router/app_router.dart';
import '../storage/bookmarks_provider.dart';
import '../storage/chapter_progress_provider.dart';

/// Page de lecture d'un chapitre : en-tête, modules de contenu, sommaire
/// flottant et navigation vers les chapitres voisins.
///
/// Un chapitre sans contenu s'affiche « en préparation » avec ses points clés.
class ChapterScaffold extends ConsumerStatefulWidget {
  final CourseChapter chapter;
  final String? targetModuleId;

  const ChapterScaffold({
    super.key,
    required this.chapter,
    this.targetModuleId,
  });

  /// Raccourci pour les écrans de chapitre : retrouve le chapitre par sa route.
  factory ChapterScaffold.forRoute(String route, {Key? key, String? targetModuleId}) {
    return ChapterScaffold(
      key: key,
      chapter: CourseData.byRoute(route)!,
      targetModuleId: targetModuleId,
    );
  }

  @override
  ConsumerState<ChapterScaffold> createState() => _ChapterScaffoldState();
}

class _ChapterScaffoldState extends ConsumerState<ChapterScaffold> {
  final ScrollController _scrollController = ScrollController();
  final Map<String, GlobalKey> _moduleKeys = {};
  String? _activeModuleId;

  CourseChapter get _chapter => widget.chapter;

  @override
  void initState() {
    super.initState();
    _scrollToTarget();
    _scrollController.addListener(_onScroll);
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _onScroll();
    });
  }

  @override
  void didUpdateWidget(ChapterScaffold oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.targetModuleId != oldWidget.targetModuleId) {
      _scrollToTarget();
    }
  }

  @override
  void dispose() {
    _scrollController.removeListener(_onScroll);
    _scrollController.dispose();
    super.dispose();
  }

  void _onScroll() {
    if (!mounted) return;

    String? newActiveId;
    double bestDy = -double.infinity;
    const double threshold = 200.0; // Seuil sous la barre d'en-tête pour considérer un module actif

    for (var entry in _moduleKeys.entries) {
      final context = entry.value.currentContext;
      if (context != null) {
        final box = context.findRenderObject() as RenderBox?;
        if (box != null && box.hasSize) {
          final dy = box.localToGlobal(Offset.zero).dy;
          if (dy <= threshold && dy > bestDy) {
            bestDy = dy;
            newActiveId = entry.key;
          }
        }
      }
    }

    if (newActiveId == null && _moduleKeys.isNotEmpty) {
      newActiveId = _moduleKeys.keys.first;
    }

    if (newActiveId != _activeModuleId) {
      setState(() {
        _activeModuleId = newActiveId;
      });
    }
  }

  void _ensureVisible(String moduleId) {
    final key = _moduleKeys[moduleId];
    if (key != null && key.currentContext != null) {
      Scrollable.ensureVisible(
        key.currentContext!,
        duration: VivMotion.of(context, VivMotion.panel),
        curve: VivMotion.standard,
        alignment: 0.15, // Espace par rapport au haut de l'écran
      );
    }
  }

  void _scrollToTarget() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      Future.delayed(const Duration(milliseconds: 100), () {
        if (!mounted) return;
        if (widget.targetModuleId != null) {
          _ensureVisible(widget.targetModuleId!);
        } else if (_scrollController.hasClients) {
          // Remonter en haut de la page si aucun module cible n'est spécifié
          _scrollController.animateTo(
            0.0,
            duration: VivMotion.of(context, VivMotion.panel),
            curve: VivMotion.standard,
          );
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    ref.listen<int>(activeBranchIndexProvider, (previous, current) {
      if (current == _chapter.branchIndex) {
        _scrollToTarget();
      }
    });

    final bookmarks = ref.watch(bookmarksProvider);
    final modules = _chapter.modules;
    final hasHeader = modules.isNotEmpty && modules.first is TitleModule;
    final mainTitleModule = hasHeader ? modules.first as TitleModule : null;
    final otherModules = hasHeader ? modules.skip(1) : modules;

    if (mainTitleModule != null) {
      _moduleKeys.putIfAbsent(mainTitleModule.id, () => GlobalKey());
    }

    return Stack(
      children: [
        Positioned.fill(
          child: SingleChildScrollView(
            controller: _scrollController,
            padding: const EdgeInsets.only(
              top: VivSpacing.space6,
              bottom: VivSpacing.space12,
              right: 80, // Marge de respiration pour le sommaire
            ),
            child: Center(
              child: Container(
                constraints: const BoxConstraints(maxWidth: 800),
                padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space6),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    _buildPreviousButton(context),
                    Container(
                      key: mainTitleModule != null ? _moduleKeys[mainTitleModule.id] : null,
                      child: _buildChapterHeader(mainTitleModule?.title ?? _chapter.title),
                    ),
                    if (_chapter.isInPreparation)
                      _buildInPreparation()
                    else
                      ...otherModules.map((module) {
                        _moduleKeys.putIfAbsent(module.id, () => GlobalKey());
                        return Container(
                          key: _moduleKeys[module.id],
                          child: ContentModuleRenderer(
                            module: module,
                            isBookmarked: bookmarks.contains(module.id),
                            onBookmarkToggle: () {
                              ref.read(bookmarksProvider.notifier).toggleBookmark(module.id);
                            },
                            onImageTap: (path, caption) => _showFullscreenImage(context, path, caption),
                          ),
                        );
                      }),
                    _buildBottomActions(context, ref),
                  ],
                ),
              ),
            ),
          ),
        ),

        // Sommaire flottant à droite
        if (!_chapter.isInPreparation)
          Positioned(
            top: VivSpacing.space6,
            right: VivSpacing.space4,
            child: ChapterOutlineWidget(
              modules: modules,
              activeModuleId: _activeModuleId,
              onNavigate: _ensureVisible,
            ),
          ),
      ],
    );
  }

  // -------------------------------------------------------------------------
  // En-tête : sur-titre, titre display-md, objectif sur surface-accent.
  // -------------------------------------------------------------------------

  Widget _buildChapterHeader(String title) {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(bottom: VivSpacing.space8),
      decoration: VivDecorations.card(),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const VivGradientLine(),
          Padding(
            padding: const EdgeInsets.all(VivSpacing.space8),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(_chapter.icon, size: 20, color: VivColors.action),
                    const SizedBox(width: VivSpacing.space2),
                    VivOverline(_chapter.overline),
                  ],
                ),
                const SizedBox(height: VivSpacing.space3),
                Text(title, style: VivTypography.displayMd),
                const SizedBox(height: VivSpacing.space6),
                VivObjectivesPanel(
                  title: 'Objectif du chapitre',
                  items: [_chapter.objective],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildInPreparation() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space5, vertical: VivSpacing.space4),
          decoration: BoxDecoration(
            color: VivColors.infoSurface,
            borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
          ),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Padding(
                padding: EdgeInsets.only(top: 2),
                child: Icon(LucideIcons.info, size: 20, color: VivColors.info),
              ),
              const SizedBox(width: VivSpacing.space3),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('Contenu en préparation', style: VivTypography.headingSm),
                    const SizedBox(height: VivSpacing.space1),
                    Text(
                      'Ce chapitre est en cours de rédaction. Il sera disponible dans une prochaine mise à jour du support, installée automatiquement au lancement de l\'application.',
                      style: VivTypography.body,
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
        if (_chapter.points.isNotEmpty) ...[
          const SizedBox(height: VivSpacing.space8),
          Text('Au programme de ce chapitre', style: VivTypography.headingLg),
          const SizedBox(height: VivSpacing.space4),
          for (var i = 0; i < _chapter.points.length; i++)
            Padding(
              padding: const EdgeInsets.only(bottom: VivSpacing.space3),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    width: 28,
                    height: 28,
                    alignment: Alignment.center,
                    decoration: const BoxDecoration(color: VivColors.brandGold, shape: BoxShape.circle),
                    child: Text('${i + 1}', style: VivTypography.label.copyWith(color: VivColors.inkOnPastel)),
                  ),
                  const SizedBox(width: VivSpacing.space3),
                  Expanded(
                    child: Padding(
                      padding: const EdgeInsets.only(top: 3),
                      child: Text(_chapter.points[i].label, style: VivTypography.body),
                    ),
                  ),
                ],
              ),
            ),
        ],
      ],
    );
  }

  // -------------------------------------------------------------------------
  // Navigation entre chapitres
  // -------------------------------------------------------------------------

  Widget _buildPreviousButton(BuildContext context) {
    final previous = CourseData.previousOf(_chapter);
    if (previous == null) return const SizedBox.shrink();

    return Padding(
      padding: const EdgeInsets.only(bottom: VivSpacing.space4),
      child: TextButton.icon(
        onPressed: () => context.go(previous.route),
        style: VivButtonStyles.ghost(small: true),
        icon: const Icon(LucideIcons.chevronLeft, size: 16),
        label: Text('${previous.shortLabel} : ${previous.title}'),
      ),
    );
  }

  Widget _buildBottomActions(BuildContext context, WidgetRef ref) {
    final completedChapters = ref.watch(chapterProgressProvider);
    final isCompleted = completedChapters.contains(_chapter.route);
    final next = CourseData.nextOf(_chapter);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const SizedBox(height: VivSpacing.space8),
        const Divider(color: VivColors.border, height: 1),
        const SizedBox(height: VivSpacing.space6),
        Wrap(
          alignment: WrapAlignment.spaceBetween,
          crossAxisAlignment: WrapCrossAlignment.center,
          spacing: VivSpacing.space4,
          runSpacing: VivSpacing.space3,
          children: [
            if (!_chapter.isInPreparation)
              OutlinedButton.icon(
                onPressed: () {
                  ref.read(chapterProgressProvider.notifier).toggleCompletion(_chapter.route);
                },
                style: isCompleted
                    ? VivButtonStyles.secondary().copyWith(
                        backgroundColor: const WidgetStatePropertyAll(VivColors.successSurface),
                        foregroundColor: const WidgetStatePropertyAll(VivColors.success),
                        iconColor: const WidgetStatePropertyAll(VivColors.success),
                        side: const WidgetStatePropertyAll(BorderSide(color: VivColors.success)),
                      )
                    : VivButtonStyles.secondary(),
                icon: Icon(isCompleted ? LucideIcons.circleCheck : LucideIcons.circle, size: 16),
                label: Text(isCompleted ? 'Chapitre terminé' : 'Marquer comme terminé'),
              )
            else
              const SizedBox.shrink(),
            if (next != null)
              ElevatedButton.icon(
                onPressed: () => context.go(next.route),
                style: VivButtonStyles.primary(),
                iconAlignment: IconAlignment.end,
                icon: const Icon(LucideIcons.arrowRight, size: 16),
                label: Text('${next.shortLabel} : ${next.title}'),
              ),
          ],
        ),
      ],
    );
  }

  // -------------------------------------------------------------------------
  // Visionneuse plein écran (thème sombre, verre dépoli)
  // -------------------------------------------------------------------------

  void _showFullscreenImage(BuildContext context, String imagePath, String? caption) {
    final isNetwork = imagePath.startsWith('http');
    showGeneralDialog(
      context: context,
      barrierDismissible: true,
      barrierLabel: 'Fermer la visionneuse',
      barrierColor: Colors.transparent,
      transitionDuration: VivMotion.of(context, VivMotion.panel),
      pageBuilder: (context, animation, secondaryAnimation) {
        return Scaffold(
          backgroundColor: Colors.transparent,
          body: Stack(
            children: [
              Positioned.fill(
                child: GestureDetector(
                  onTap: () => Navigator.of(context).pop(),
                  child: BackdropFilter(
                    filter: ImageFilter.blur(sigmaX: 7.0, sigmaY: 7.0),
                    child: Container(color: VivDarkColors.surfaceSunken.withValues(alpha: 0.82)),
                  ),
                ),
              ),
              Positioned.fill(
                child: Center(
                  child: Padding(
                    padding: const EdgeInsets.all(VivSpacing.space12),
                    child: InteractiveViewer(
                      minScale: 0.8,
                      maxScale: 5.0,
                      clipBehavior: Clip.none,
                      child: isNetwork
                          ? CachedNetworkImage(
                              imageUrl: imagePath,
                              fit: BoxFit.contain,
                              placeholder: (context, url) => const Center(
                                child: CircularProgressIndicator(color: VivDarkColors.action),
                              ),
                              errorWidget: (context, url, error) => _darkMessage(
                                'Image indisponible hors ligne',
                                'Cette image sera mise en cache lors de sa première consultation en ligne afin d\'être visible hors ligne.',
                              ),
                            )
                          : Image.asset(
                              imagePath,
                              fit: BoxFit.contain,
                              errorBuilder: (context, error, stackTrace) => _darkMessage(
                                'Capture à venir',
                                'Cette illustration sera ajoutée dans une prochaine mise à jour du support.',
                              ),
                            ),
                    ),
                  ),
                ),
              ),
              Positioned(
                top: VivSpacing.space6,
                right: VivSpacing.space6,
                child: Tooltip(
                  message: 'Fermer',
                  child: Material(
                    color: VivDarkColors.glassSurface,
                    shape: const CircleBorder(side: BorderSide(color: VivDarkColors.glassBorder)),
                    clipBehavior: Clip.antiAlias,
                    child: InkWell(
                      onTap: () => Navigator.of(context).pop(),
                      child: const Padding(
                        padding: EdgeInsets.all(12.0),
                        child: Icon(LucideIcons.x, color: VivDarkColors.ink, size: 20),
                      ),
                    ),
                  ),
                ),
              ),
              if (caption != null && caption.isNotEmpty)
                Positioned(
                  left: VivSpacing.space6,
                  right: VivSpacing.space6,
                  bottom: VivSpacing.space8,
                  child: Center(
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
                      child: BackdropFilter(
                        filter: ImageFilter.blur(sigmaX: 7.0, sigmaY: 7.0),
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space5, vertical: VivSpacing.space3),
                          decoration: BoxDecoration(
                            color: VivDarkColors.glassSurface,
                            borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
                            border: Border.all(color: VivDarkColors.glassBorder),
                          ),
                          child: Text(
                            caption,
                            textAlign: TextAlign.center,
                            style: VivTypography.bodySm.copyWith(color: VivDarkColors.ink),
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
            ],
          ),
        );
      },
      transitionBuilder: (context, animation, secondaryAnimation, child) {
        final curved = CurvedAnimation(parent: animation, curve: VivMotion.enter, reverseCurve: VivMotion.exit);
        return FadeTransition(
          opacity: curved,
          child: ScaleTransition(
            scale: Tween<double>(begin: 0.98, end: 1.0).animate(curved),
            child: child,
          ),
        );
      },
    );
  }

  Widget _darkMessage(String title, String message) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        const Icon(LucideIcons.image, color: VivDarkColors.inkSubtle, size: 64),
        const SizedBox(height: VivSpacing.space3),
        Text(title, style: VivTypography.headingSm.copyWith(color: VivDarkColors.ink), textAlign: TextAlign.center),
        const SizedBox(height: VivSpacing.space2),
        Text(message, style: VivTypography.bodySm.copyWith(color: VivDarkColors.inkMuted), textAlign: TextAlign.center),
      ],
    );
  }
}
