import 'package:flutter/material.dart';
import 'dart:ui';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import 'package:window_manager/window_manager.dart';

import '../../core/data/course_data.dart';
import '../../core/theme/viv_colors.dart';
import '../../core/theme/viv_motion.dart';
import '../../core/theme/viv_spacing.dart';
import '../../core/theme/viv_typography.dart';
import '../../core/router/app_router.dart';
import '../../core/services/search_service.dart';
import '../../core/widgets/viv_brand.dart';

/// Coque de l'application : barre latérale sombre (bande de navigation),
/// en-tête clair souligné du filet de dégradé, zone de contenu et recherche.
class MainShell extends ConsumerStatefulWidget {
  final StatefulNavigationShell navigationShell;

  const MainShell({super.key, required this.navigationShell});

  @override
  ConsumerState<MainShell> createState() => _MainShellState();
}

class _MainShellState extends ConsumerState<MainShell> {
  bool _isSidebarCollapsed = false;
  bool _isBasicsExpanded = true;
  bool _isFormationExpanded = true;
  bool _isChallengesExpanded = true;

  bool _isSearchActive = false;
  final TextEditingController _searchController = TextEditingController();
  final FocusNode _searchFocusNode = FocusNode();
  List<SearchResult> _searchResults = [];

  @override
  void dispose() {
    _searchController.dispose();
    _searchFocusNode.dispose();
    super.dispose();
  }

  void _goBranch(int index) {
    widget.navigationShell.goBranch(
      index,
      initialLocation: index == widget.navigationShell.currentIndex,
    );
  }

  void _closeSearch() {
    setState(() {
      _isSearchActive = false;
      _searchController.clear();
      _searchResults.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    final selectedIndex = widget.navigationShell.currentIndex;

    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (ref.read(activeBranchIndexProvider) != selectedIndex) {
        ref.read(activeBranchIndexProvider.notifier).changeIndex(selectedIndex);
      }
    });

    return Stack(
      children: [
        Scaffold(
          backgroundColor: VivColors.surface,
          body: Row(
            children: [
              _buildSidebar(selectedIndex),
              Expanded(
                child: Column(
                  children: [
                    _buildHeader(selectedIndex),
                    Expanded(child: widget.navigationShell),
                  ],
                ),
              ),
            ],
          ),
        ),
        if (_isSearchActive) _buildSearchOverlay(context),
      ],
    );
  }

  // -------------------------------------------------------------------------
  // Barre latérale (thème sombre)
  // -------------------------------------------------------------------------

  Widget _buildSidebar(int selectedIndex) {
    return AnimatedContainer(
      duration: VivMotion.of(context, VivMotion.panel),
      curve: VivMotion.standard,
      width: _isSidebarCollapsed ? 64 : 260,
      decoration: const BoxDecoration(
        color: VivDarkColors.surface,
        borderRadius: BorderRadius.only(
          topRight: Radius.circular(VivSpacing.radiusMd),
          bottomRight: Radius.circular(VivSpacing.radiusMd),
        ),
      ),
      child: LayoutBuilder(
        builder: (context, constraints) {
          final isCompact = constraints.maxWidth < 160;

          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Signature de marque : logo blanc sur fond sombre, submark en compact.
              DragToMoveArea(
                child: Container(
                  height: 70,
                  padding: EdgeInsets.symmetric(horizontal: isCompact ? 0 : VivSpacing.space5),
                  alignment: isCompact ? Alignment.center : Alignment.centerLeft,
                  child: AnimatedSwitcher(
                    duration: VivMotion.of(context, VivMotion.state),
                    child: isCompact
                        ? VivLogo.submark(key: const ValueKey('mark'), onDark: true, height: 24)
                        : VivLogo.full(key: const ValueKey('full'), ink: VivLogoInk.blanc, height: 24),
                  ),
                ),
              ),
              const SizedBox(height: VivSpacing.space2),
              Expanded(
                child: ListView(
                  padding: EdgeInsets.symmetric(horizontal: isCompact ? VivSpacing.space2 : VivSpacing.space3),
                  children: [
                    if (!isCompact) _sidebarLabel('Menu'),
                    _buildNavItem(
                      icon: LucideIcons.layoutDashboard,
                      title: CourseData.screenTitle(CourseData.dashboardBranch),
                      index: CourseData.dashboardBranch,
                      selectedIndex: selectedIndex,
                      isCompact: isCompact,
                    ),
                    _buildNavItem(
                      icon: LucideIcons.bookOpen,
                      title: CourseData.screenTitle(CourseData.programBranch),
                      index: CourseData.programBranch,
                      selectedIndex: selectedIndex,
                      isCompact: isCompact,
                    ),
                    _buildNavItem(
                      icon: LucideIcons.bookmark,
                      title: CourseData.screenTitle(CourseData.bookmarksBranch),
                      index: CourseData.bookmarksBranch,
                      selectedIndex: selectedIndex,
                      isCompact: isCompact,
                    ),
                    const SizedBox(height: VivSpacing.space4),
                    ..._buildSection(
                      title: 'Les bases',
                      chapters: CourseData.basics,
                      isExpanded: _isBasicsExpanded,
                      onToggle: () => setState(() => _isBasicsExpanded = !_isBasicsExpanded),
                      selectedIndex: selectedIndex,
                      isCompact: isCompact,
                    ),
                    const SizedBox(height: VivSpacing.space4),
                    ..._buildSection(
                      title: 'Formation',
                      chapters: CourseData.formation,
                      isExpanded: _isFormationExpanded,
                      onToggle: () => setState(() => _isFormationExpanded = !_isFormationExpanded),
                      selectedIndex: selectedIndex,
                      isCompact: isCompact,
                    ),
                    const SizedBox(height: VivSpacing.space4),
                    ..._buildSection(
                      title: 'Pour aller plus loin',
                      chapters: CourseData.challenges,
                      isExpanded: _isChallengesExpanded,
                      onToggle: () => setState(() => _isChallengesExpanded = !_isChallengesExpanded),
                      selectedIndex: selectedIndex,
                      isCompact: isCompact,
                    ),
                  ],
                ),
              ),
              Padding(
                padding: EdgeInsets.symmetric(
                  horizontal: isCompact ? VivSpacing.space2 : VivSpacing.space4,
                  vertical: VivSpacing.space2,
                ),
                child: const Divider(color: VivDarkColors.border, height: 1, thickness: 1),
              ),
              Padding(
                padding: EdgeInsets.only(
                  left: isCompact ? VivSpacing.space2 : VivSpacing.space3,
                  right: isCompact ? VivSpacing.space2 : VivSpacing.space3,
                  bottom: VivSpacing.space4,
                ),
                child: _buildNavItem(
                  icon: LucideIcons.settings,
                  title: CourseData.screenTitle(CourseData.settingsBranch),
                  index: CourseData.settingsBranch,
                  selectedIndex: selectedIndex,
                  isCompact: isCompact,
                ),
              ),
            ],
          );
        },
      ),
    );
  }

  Widget _sidebarLabel(String text) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space3, vertical: VivSpacing.space2),
      child: VivOverline(text, color: VivDarkColors.inkSubtle),
    );
  }

  List<Widget> _buildSection({
    required String title,
    required Iterable<CourseChapter> chapters,
    required bool isExpanded,
    required VoidCallback onToggle,
    required int selectedIndex,
    required bool isCompact,
  }) {
    return [
      if (!isCompact) _buildSectionHeader(title: title, isExpanded: isExpanded, onTap: onToggle),
      AnimatedSize(
        duration: VivMotion.of(context, VivMotion.state),
        curve: VivMotion.standard,
        alignment: Alignment.topCenter,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (isExpanded || isCompact)
              for (final chapter in chapters)
                _buildNavItem(
                  icon: chapter.icon,
                  title: chapter.navLabel,
                  index: chapter.branchIndex,
                  selectedIndex: selectedIndex,
                  isCompact: isCompact,
                ),
          ],
        ),
      ),
    ];
  }

  Widget _buildNavItem({
    required IconData icon,
    required String title,
    required int index,
    required int selectedIndex,
    required bool isCompact,
  }) {
    return _SidebarItem(
      icon: icon,
      title: title,
      isSelected: selectedIndex == index,
      isCompact: isCompact,
      onTap: () => _goBranch(index),
    );
  }

  Widget _buildSectionHeader({
    required String title,
    required bool isExpanded,
    required VoidCallback onTap,
  }) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(VivSpacing.radiusSm),
        hoverColor: VivDarkColors.surfaceRaised,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space3, vertical: 6.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              VivOverline(title, color: VivDarkColors.inkSubtle),
              Icon(
                isExpanded ? LucideIcons.chevronDown : LucideIcons.chevronRight,
                color: VivDarkColors.inkSubtle,
                size: 14,
              ),
            ],
          ),
        ),
      ),
    );
  }

  // -------------------------------------------------------------------------
  // En-tête collant : surface, shadow-md, filet de dégradé
  // -------------------------------------------------------------------------

  Widget _buildHeader(int selectedIndex) {
    return Container(
      decoration: const BoxDecoration(
        color: VivColors.surface,
        boxShadow: VivColors.shadowMd,
      ),
      child: Column(
        children: [
          SizedBox(
            height: 66,
            child: Row(
              children: [
                const SizedBox(width: VivSpacing.space2),
                IconButton(
                  tooltip: _isSidebarCollapsed ? 'Déplier le menu' : 'Replier le menu',
                  onPressed: () => setState(() => _isSidebarCollapsed = !_isSidebarCollapsed),
                  icon: Icon(
                    _isSidebarCollapsed ? LucideIcons.menu : LucideIcons.panelLeft,
                    size: 20,
                    color: VivColors.ink,
                  ),
                ),
                Expanded(
                  child: DragToMoveArea(
                    child: Container(
                      height: double.infinity,
                      padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space2),
                      alignment: Alignment.centerLeft,
                      child: Text(CourseData.screenTitle(selectedIndex), style: VivTypography.headingMd),
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(right: VivSpacing.space2),
                  child: IconButton(
                    tooltip: 'Rechercher',
                    onPressed: () => setState(() => _isSearchActive = true),
                    icon: const Icon(LucideIcons.search, size: 20, color: VivColors.ink),
                    hoverColor: VivColors.surfaceBrand,
                  ),
                ),
                _buildWindowControls(),
              ],
            ),
          ),
          const VivGradientLine(),
        ],
      ),
    );
  }

  // -------------------------------------------------------------------------
  // Recherche
  // -------------------------------------------------------------------------

  Widget _buildSearchOverlay(BuildContext context) {
    final groupedResults = <String, List<SearchResult>>{};
    for (var res in _searchResults) {
      groupedResults.putIfAbsent(res.chapterTitle, () => []).add(res);
    }

    return Positioned.fill(
      child: Stack(
        children: [
          Positioned.fill(
            child: GestureDetector(
              onTap: _closeSearch,
              child: BackdropFilter(
                filter: ImageFilter.blur(sigmaX: 7.0, sigmaY: 7.0),
                child: Container(color: VivColors.ink.withValues(alpha: 0.4)),
              ),
            ),
          ),
          Center(
            child: Material(
              color: Colors.transparent,
              child: Container(
                width: 650,
                constraints: const BoxConstraints(maxHeight: 480),
                decoration: BoxDecoration(
                  color: VivColors.surfaceRaised,
                  borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
                  border: Border.all(color: VivColors.border),
                  boxShadow: VivColors.shadowLg,
                ),
                clipBehavior: Clip.antiAlias,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(VivSpacing.space4),
                      child: Row(
                        children: [
                          const Icon(LucideIcons.search, color: VivColors.action, size: 20),
                          const SizedBox(width: VivSpacing.space3),
                          Expanded(
                            child: TextField(
                              controller: _searchController,
                              focusNode: _searchFocusNode,
                              autofocus: true,
                              onChanged: (val) => setState(() => _searchResults = SearchService.search(val)),
                              style: VivTypography.body,
                              cursorColor: VivColors.action,
                              decoration: InputDecoration(
                                hintText: 'Rechercher un mot-clé, un chapitre…',
                                hintStyle: VivTypography.body.copyWith(color: VivColors.inkSubtle),
                                border: InputBorder.none,
                                isDense: true,
                                contentPadding: EdgeInsets.zero,
                              ),
                            ),
                          ),
                          IconButton(
                            tooltip: 'Fermer la recherche',
                            padding: EdgeInsets.zero,
                            constraints: const BoxConstraints(),
                            icon: const Icon(LucideIcons.x, color: VivColors.inkMuted, size: 20),
                            onPressed: _closeSearch,
                          ),
                        ],
                      ),
                    ),
                    const Divider(color: VivColors.border, height: 1),
                    Flexible(
                      child: SingleChildScrollView(
                        child: _searchController.text.trim().isEmpty
                            ? _buildSearchGuide(context)
                            : _searchResults.isEmpty
                                ? _buildEmptyState(context)
                                : _buildResultsList(context, groupedResults),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSearchGuide(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(VivSpacing.space5),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          const VivOverline('Accès rapide'),
          const SizedBox(height: VivSpacing.space3),
          GridView.count(
            crossAxisCount: 2,
            shrinkWrap: true,
            mainAxisSpacing: VivSpacing.space3,
            crossAxisSpacing: VivSpacing.space3,
            childAspectRatio: 3.6,
            physics: const NeverScrollableScrollPhysics(),
            children: [
              for (final ch in CourseData.chapters)
                Material(
                  color: Colors.transparent,
                  child: InkWell(
                    onTap: () {
                      _closeSearch();
                      context.go(ch.route);
                    },
                    borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
                    hoverColor: VivColors.surfaceBrand,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: VivSpacing.space3),
                      decoration: BoxDecoration(
                        border: Border.all(color: VivColors.border),
                        borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
                      ),
                      child: Row(
                        children: [
                          Icon(ch.icon, color: VivColors.action, size: 20),
                          const SizedBox(width: VivSpacing.space3),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Text(ch.shortLabel, style: VivTypography.label),
                                Text(
                                  ch.title,
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: VivTypography.caption,
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
            ],
          ),
          const SizedBox(height: VivSpacing.space5),
          Text('Astuce : cliquez en dehors de la boîte de recherche pour la fermer.', style: VivTypography.caption),
        ],
      ),
    );
  }

  Widget _buildEmptyState(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: VivSpacing.space8, horizontal: VivSpacing.space6),
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(LucideIcons.searchX, color: VivColors.borderStrong, size: 48),
            const SizedBox(height: VivSpacing.space4),
            Text(
              'Aucun résultat pour « ${_searchController.text} »',
              textAlign: TextAlign.center,
              style: VivTypography.headingSm,
            ),
            const SizedBox(height: VivSpacing.space2),
            Text(
              'Vérifiez l\'orthographe ou essayez d\'autres mots-clés.',
              textAlign: TextAlign.center,
              style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildResultsList(BuildContext context, Map<String, List<SearchResult>> groupedResults) {
    return Padding(
      padding: const EdgeInsets.all(VivSpacing.space4),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: groupedResults.entries.map((entry) {
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Padding(
                padding: const EdgeInsets.symmetric(vertical: VivSpacing.space2, horizontal: VivSpacing.space2),
                child: VivOverline(entry.key),
              ),
              ...entry.value.map((item) => _buildResultItemCard(context, item)),
              const SizedBox(height: VivSpacing.space3),
            ],
          );
        }).toList(),
      ),
    );
  }

  Widget _buildResultItemCard(BuildContext context, SearchResult item) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 4),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: () {
            _closeSearch();
            context.go('${item.routePath}?target=${item.moduleId}');
          },
          borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
          hoverColor: VivColors.surfaceBrand,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
            decoration: BoxDecoration(
              border: Border.all(color: VivColors.border),
              borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
            ),
            child: Row(
              children: [
                Icon(_getIconForModuleType(item.moduleType), color: VivColors.inkMuted, size: 18),
                const SizedBox(width: VivSpacing.space3),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(item.moduleTitle, style: VivTypography.label),
                      const SizedBox(height: 4),
                      _buildHighlightText(item.snippet, _searchController.text),
                    ],
                  ),
                ),
                const SizedBox(width: VivSpacing.space2),
                const Icon(LucideIcons.chevronRight, color: VivColors.borderStrong, size: 14),
              ],
            ),
          ),
        ),
      ),
    );
  }

  /// Surligne l'occurrence trouvée sur un aplat brand-gold (surlignage de marque).
  Widget _buildHighlightText(String text, String query) {
    final muted = VivTypography.bodySm.copyWith(color: VivColors.inkMuted);
    if (query.isEmpty) return Text(text, style: muted);

    final lowerText = text.toLowerCase();
    final lowerQuery = query.toLowerCase();
    final List<TextSpan> spans = [];

    int start = 0;
    int index = lowerText.indexOf(lowerQuery, start);

    while (index != -1) {
      if (index > start) {
        spans.add(TextSpan(text: text.substring(start, index)));
      }
      spans.add(TextSpan(
        text: text.substring(index, index + query.length),
        style: const TextStyle(color: VivColors.inkOnPastel, backgroundColor: VivColors.brandGold),
      ));
      start = index + query.length;
      index = lowerText.indexOf(lowerQuery, start);
    }

    if (start < text.length) {
      spans.add(TextSpan(text: text.substring(start)));
    }

    return RichText(
      text: TextSpan(children: spans, style: muted),
      maxLines: 2,
      overflow: TextOverflow.ellipsis,
    );
  }

  IconData _getIconForModuleType(String type) {
    switch (type) {
      case 'title':
        return LucideIcons.heading;
      case 'text':
      case 'sideBySide':
        return LucideIcons.fileText;
      case 'media':
        return LucideIcons.image;
      case 'info':
        return LucideIcons.info;
      case 'resource':
        return LucideIcons.download;
      case 'list':
        return LucideIcons.list;
      case 'quiz':
        return LucideIcons.circleQuestionMark;
      default:
        return LucideIcons.file;
    }
  }

  // -------------------------------------------------------------------------
  // Contrôles de fenêtre (barre de titre masquée)
  // -------------------------------------------------------------------------

  Widget _buildWindowControls() {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        _WindowButton(icon: LucideIcons.minus, tooltip: 'Réduire', onTap: () => windowManager.minimize()),
        _WindowButton(
          icon: LucideIcons.square,
          tooltip: 'Agrandir',
          onTap: () async {
            if (await windowManager.isMaximized()) {
              windowManager.unmaximize();
            } else {
              windowManager.maximize();
            }
          },
        ),
        _WindowButton(icon: LucideIcons.x, tooltip: 'Fermer', onTap: () => windowManager.close(), isClose: true),
      ],
    );
  }
}

/// Entrée de la barre latérale, sur fond sombre.
class _SidebarItem extends StatefulWidget {
  final IconData icon;
  final String title;
  final bool isSelected;
  final bool isCompact;
  final VoidCallback onTap;

  const _SidebarItem({
    required this.icon,
    required this.title,
    required this.isSelected,
    required this.isCompact,
    required this.onTap,
  });

  @override
  State<_SidebarItem> createState() => _SidebarItemState();
}

class _SidebarItemState extends State<_SidebarItem> {
  bool _hovered = false;

  @override
  Widget build(BuildContext context) {
    final selected = widget.isSelected;
    final background = selected
        ? VivDarkColors.surfaceBrand
        : (_hovered ? VivDarkColors.surfaceRaised : Colors.transparent);
    final iconColor = selected ? VivDarkColors.action : VivDarkColors.inkMuted;
    final textColor = selected ? VivDarkColors.ink : VivDarkColors.inkMuted;

    final item = Padding(
      padding: const EdgeInsets.symmetric(vertical: 1),
      child: MouseRegion(
        cursor: SystemMouseCursors.click,
        onEnter: (_) => setState(() => _hovered = true),
        onExit: (_) => setState(() => _hovered = false),
        child: GestureDetector(
          onTap: widget.onTap,
          child: AnimatedContainer(
            duration: VivMotion.of(context, VivMotion.micro),
            curve: VivMotion.standard,
            padding: EdgeInsets.symmetric(
              horizontal: widget.isCompact ? VivSpacing.space2 : VivSpacing.space3,
              vertical: widget.isCompact ? VivSpacing.space2 : 7.0,
            ),
            decoration: BoxDecoration(
              color: background,
              borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
            ),
            child: Row(
              mainAxisAlignment: widget.isCompact ? MainAxisAlignment.center : MainAxisAlignment.start,
              children: [
                Icon(widget.icon, color: iconColor, size: 20),
                if (!widget.isCompact) ...[
                  const SizedBox(width: VivSpacing.space3),
                  Expanded(
                    child: Text(
                      widget.title,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      softWrap: false,
                      style: VivTypography.label.copyWith(color: textColor),
                    ),
                  ),
                  if (selected)
                    Container(
                      width: 6,
                      height: 6,
                      decoration: const BoxDecoration(color: VivDarkColors.action, shape: BoxShape.circle),
                    ),
                ],
              ],
            ),
          ),
        ),
      ),
    );

    return widget.isCompact ? Tooltip(message: widget.title, child: item) : item;
  }
}

class _WindowButton extends StatefulWidget {
  final IconData icon;
  final String tooltip;
  final VoidCallback onTap;
  final bool isClose;

  const _WindowButton({
    required this.icon,
    required this.tooltip,
    required this.onTap,
    this.isClose = false,
  });

  @override
  State<_WindowButton> createState() => _WindowButtonState();
}

class _WindowButtonState extends State<_WindowButton> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    final hoverBgColor = widget.isClose ? VivColors.danger : VivColors.surfaceBrand;
    final iconColor = (_isHovered && widget.isClose) ? VivColors.onAction : VivColors.ink;

    return Tooltip(
      message: widget.tooltip,
      waitDuration: const Duration(milliseconds: 600),
      child: MouseRegion(
        onEnter: (_) => setState(() => _isHovered = true),
        onExit: (_) => setState(() => _isHovered = false),
        child: GestureDetector(
          onTap: widget.onTap,
          child: AnimatedContainer(
            duration: VivMotion.of(context, VivMotion.micro),
            width: 48,
            height: double.infinity,
            color: _isHovered ? hoverBgColor : Colors.transparent,
            child: Icon(widget.icon, size: 14, color: iconColor),
          ),
        ),
      ),
    );
  }
}
