import 'dart:ui';
import 'package:flutter/material.dart';

import '../models/content_module.dart';
import '../theme/viv_colors.dart';
import '../theme/viv_motion.dart';
import '../theme/viv_spacing.dart';
import '../theme/viv_typography.dart';
import 'viv_brand.dart';

class OutlineItem {
  final String id;
  final String title;
  final bool isMain;

  OutlineItem({
    required this.id,
    required this.title,
    required this.isMain,
  });
}

/// Sommaire flottant du chapitre : des repères discrets au repos, un panneau en
/// verre dépoli au survol (le texte du chapitre passe dessous).
class ChapterOutlineWidget extends StatefulWidget {
  final List<ContentModule> modules;
  final String? activeModuleId;
  final ValueChanged<String> onNavigate;

  const ChapterOutlineWidget({
    super.key,
    required this.modules,
    required this.activeModuleId,
    required this.onNavigate,
  });

  @override
  State<ChapterOutlineWidget> createState() => _ChapterOutlineWidgetState();
}

class _ChapterOutlineWidgetState extends State<ChapterOutlineWidget> {
  bool _isExpanded = false;
  final ScrollController _outlineScrollController = ScrollController();

  @override
  void dispose() {
    _outlineScrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final outlineItems = <OutlineItem>[];
    for (var module in widget.modules) {
      if (module is TitleModule) {
        outlineItems.add(OutlineItem(id: module.id, title: module.title, isMain: true));
      } else if (module is TextModule && module.title != null) {
        outlineItems.add(OutlineItem(id: module.id, title: module.title!, isMain: false));
      } else if (module is SideBySideModule && module.title != null) {
        outlineItems.add(OutlineItem(id: module.id, title: module.title!, isMain: false));
      } else if (module is ResourceModule) {
        outlineItems.add(OutlineItem(id: module.id, title: module.title, isMain: false));
      } else if (module is ListModule) {
        outlineItems.add(OutlineItem(id: module.id, title: module.title, isMain: false));
      } else if (module is QuizModule) {
        outlineItems.add(OutlineItem(id: module.id, title: module.question, isMain: false));
      }
    }

    if (outlineItems.isEmpty) return const SizedBox.shrink();

    final duration = VivMotion.of(context, VivMotion.state);

    return ExcludeSemantics(
      child: MouseRegion(
        onEnter: (_) => setState(() => _isExpanded = true),
        onExit: (_) => setState(() => _isExpanded = false),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
          child: BackdropFilter(
            filter: ImageFilter.blur(
              sigmaX: _isExpanded ? 7.0 : 0.0, // flou unique du système : 14 px
              sigmaY: _isExpanded ? 7.0 : 0.0,
            ),
            child: AnimatedContainer(
              duration: duration,
              curve: VivMotion.standard,
              width: _isExpanded ? 260.0 : 40.0,
              constraints: BoxConstraints(
                maxHeight: _isExpanded
                    ? MediaQuery.of(context).size.height - 180
                    : MediaQuery.of(context).size.height - 220,
              ),
              decoration: BoxDecoration(
                color: _isExpanded ? const Color(0xB8FFFFFF) : Colors.transparent,
                borderRadius: BorderRadius.circular(VivSpacing.radiusLg),
                border: Border.all(
                  color: _isExpanded ? const Color(0x1F1C161B) : Colors.transparent,
                  width: 1,
                ),
                boxShadow: _isExpanded ? VivColors.shadowMd : const [],
              ),
              padding: EdgeInsets.symmetric(
                vertical: VivSpacing.space4,
                horizontal: _isExpanded ? VivSpacing.space4 : 12,
              ),
              child: ClipRect(
                child: Scrollbar(
                  controller: _outlineScrollController,
                  thumbVisibility: false,
                  child: SingleChildScrollView(
                    controller: _outlineScrollController,
                    physics: _isExpanded
                        ? const ClampingScrollPhysics()
                        : const NeverScrollableScrollPhysics(),
                    child: _isExpanded
                        ? SingleChildScrollView(
                            scrollDirection: Axis.horizontal,
                            physics: const NeverScrollableScrollPhysics(),
                            child: SizedBox(
                              width: 226.0,
                              child: _buildExpandedContent(outlineItems),
                            ),
                          )
                        : _buildCollapsedContent(outlineItems),
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildCollapsedContent(List<OutlineItem> items) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.end,
      children: items.map((item) {
        final isActive = item.id == widget.activeModuleId;
        return Padding(
          padding: const EdgeInsets.symmetric(vertical: 3.0),
          child: AnimatedContainer(
            duration: VivMotion.of(context, VivMotion.micro),
            height: 2,
            width: isActive ? 20.0 : (item.isMain ? 12.0 : 6.0),
            decoration: BoxDecoration(
              color: isActive ? VivColors.action : VivColors.borderStrong.withValues(alpha: 0.6),
              borderRadius: BorderRadius.circular(1),
            ),
          ),
        );
      }).toList(),
    );
  }

  Widget _buildExpandedContent(List<OutlineItem> items) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const VivOverline('Sommaire'),
        const SizedBox(height: VivSpacing.space3),
        const Divider(color: VivColors.border, height: 1),
        const SizedBox(height: VivSpacing.space2),
        ...items.map((item) {
          final isActive = item.id == widget.activeModuleId;
          return _OutlineItemRow(
            item: item,
            isActive: isActive,
            onTap: () => widget.onNavigate(item.id),
          );
        }),
      ],
    );
  }
}

class _OutlineItemRow extends StatefulWidget {
  final OutlineItem item;
  final bool isActive;
  final VoidCallback onTap;

  const _OutlineItemRow({
    required this.item,
    required this.isActive,
    required this.onTap,
  });

  @override
  State<_OutlineItemRow> createState() => _OutlineItemRowState();
}

class _OutlineItemRowState extends State<_OutlineItemRow> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    final base = widget.item.isMain
        ? VivTypography.bodySm.copyWith(color: VivColors.ink)
        : VivTypography.bodySm.copyWith(color: VivColors.inkMuted);
    final color = widget.isActive ? VivColors.action : (_isHovered ? VivColors.ink : base.color);

    return MouseRegion(
      cursor: SystemMouseCursors.click,
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      child: GestureDetector(
        onTap: widget.onTap,
        child: AnimatedContainer(
          duration: VivMotion.of(context, VivMotion.micro),
          width: double.infinity,
          padding: const EdgeInsets.symmetric(vertical: 6.0, horizontal: 8.0),
          margin: const EdgeInsets.only(bottom: 2.0),
          decoration: BoxDecoration(
            color: _isHovered ? VivColors.surfaceBrand : Colors.transparent,
            borderRadius: BorderRadius.circular(VivSpacing.radiusMd),
          ),
          child: Padding(
            padding: EdgeInsets.only(left: widget.item.isMain ? 0.0 : 12.0),
            child: Row(
              children: [
                if (widget.isActive) ...[
                  Container(
                    width: 6,
                    height: 6,
                    decoration: const BoxDecoration(color: VivColors.action, shape: BoxShape.circle),
                  ),
                  const SizedBox(width: 6),
                ],
                Expanded(
                  child: Text(
                    widget.item.title,
                    style: base.copyWith(color: color),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
