import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:lucide_icons_flutter/lucide_icons.dart';
import 'package:shadcn_ui/shadcn_ui.dart' hide LucideIcons;

import '../../core/data/course_data.dart';
import '../../core/theme/viv_colors.dart';
import '../../core/theme/viv_spacing.dart';
import '../../core/theme/viv_typography.dart';
import '../../core/storage/settings_provider.dart';
import '../../core/storage/update_provider.dart';
import '../../core/widgets/viv_brand.dart';

class SettingsScreen extends ConsumerWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final settings = ref.watch(settingsProvider);
    final updateState = ref.watch(updateProvider);
    final localVersion = updateState.localVersion ?? '…';
    final diagnosticState = ref.watch(updateDiagnosticProvider);

    ref.listen<UpdateState>(updateProvider, (previous, next) {
      if (previous?.status == UpdateStatus.checking) {
        if (next.status == UpdateStatus.upToDate) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Vous disposez déjà de la dernière version.')),
          );
        } else if (next.status == UpdateStatus.error) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text('Erreur : ${next.errorMessage ?? 'vérification impossible.'}'),
              backgroundColor: VivColors.danger,
            ),
          );
        }
      }
    });

    return SingleChildScrollView(
      padding: const EdgeInsets.all(VivSpacing.space6),
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 960),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildSectionHeader('Application', LucideIcons.monitor),
            const SizedBox(height: VivSpacing.space4),
            _buildCard([
              _buildSettingRow(
                title: 'Afficher en plein écran',
                description: 'Bascule l\'application en mode plein écran immersif.',
                trailing: ShadSwitch(
                  value: settings.isFullScreen,
                  onChanged: (val) => ref.read(settingsProvider.notifier).setFullScreen(val),
                ),
              ),
            ]),
            const SizedBox(height: VivSpacing.space8),
            _buildSectionHeader('Mise à jour', LucideIcons.refreshCw),
            const SizedBox(height: VivSpacing.space4),
            _buildCard([
              _buildSettingRow(
                title: 'Rechercher une mise à jour',
                description: updateState.status == UpdateStatus.checking
                    ? 'Vérification en cours sur GitHub…'
                    : 'Vérifier manuellement si une nouvelle version est disponible.',
                trailing: ElevatedButton(
                  style: VivButtonStyles.primary(small: true),
                  onPressed: updateState.status == UpdateStatus.checking
                      ? null
                      : () => ref.read(updateProvider.notifier).checkForUpdates(silent: false),
                  child: Text(updateState.status == UpdateStatus.checking ? 'Recherche…' : 'Vérifier'),
                ),
              ),
            ]),
            const SizedBox(height: VivSpacing.space8),
            _buildSectionHeader('Diagnostic de connexion', LucideIcons.activity),
            const SizedBox(height: VivSpacing.space4),
            _buildCard([
              _buildSettingRow(
                title: 'Tester la communication avec GitHub',
                description: 'Vérifier la connexion à l\'API des versions pour diagnostiquer les mises à jour.',
                trailing: OutlinedButton(
                  style: VivButtonStyles.secondary(small: true),
                  onPressed: diagnosticState.isLoading
                      ? null
                      : () => ref.read(updateDiagnosticProvider.notifier).runDiagnostic(),
                  child: Text(diagnosticState.isLoading ? 'Diagnostic…' : 'Lancer le test'),
                ),
              ),
              if (diagnosticState.hasValue && diagnosticState.value != null) ...[
                const Divider(height: VivSpacing.space8, color: VivColors.border),
                _buildDiagnosticResult(diagnosticState.value!),
              ] else if (diagnosticState.hasError) ...[
                const Divider(height: VivSpacing.space8, color: VivColors.border),
                Text(
                  'Erreur lors du test : ${diagnosticState.error}',
                  style: VivTypography.bodySm.copyWith(color: VivColors.danger),
                ),
              ],
            ]),
            const SizedBox(height: VivSpacing.space8),
            _buildSectionHeader('À propos', LucideIcons.info),
            const SizedBox(height: VivSpacing.space4),
            _buildCard([
              _buildInfoRow('Support', CourseData.supportName),
              const Divider(height: VivSpacing.space6, color: VivColors.border),
              _buildInfoRow('Référence', '${CourseData.reference}-SU'),
              const Divider(height: VivSpacing.space6, color: VivColors.border),
              _buildInfoRow('Version de l\'application', localVersion),
              const Divider(height: VivSpacing.space6, color: VivColors.border),
              _buildInfoRow('Éditeur', '© 2026 VIV Formation. Tous droits réservés.'),
            ]),
          ],
        ),
      ),
    );
  }

  Widget _buildSettingRow({required String title, required String description, required Widget trailing}) {
    return Row(
      children: [
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title, style: VivTypography.headingSm),
              const SizedBox(height: VivSpacing.space1),
              Text(description, style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted)),
            ],
          ),
        ),
        const SizedBox(width: VivSpacing.space4),
        trailing,
      ],
    );
  }

  Widget _buildInfoRow(String label, String value) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(width: 220, child: Text(label, style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted))),
        Expanded(child: Text(value, style: VivTypography.data, textAlign: TextAlign.right)),
      ],
    );
  }

  Widget _buildSectionHeader(String title, IconData icon) {
    return Row(
      children: [
        Icon(icon, size: 20, color: VivColors.action),
        const SizedBox(width: VivSpacing.space3),
        Text(title, style: VivTypography.headingLg),
      ],
    );
  }

  Widget _buildDiagnosticResult(Map<String, dynamic> report) {
    final hasError = report['error'] != null ||
        report['statusCode'] != 200 ||
        !report['releaseFound'] ||
        !report['hasExeAsset'];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        VivBadge(
          hasError ? 'Problème détecté' : 'Connexion établie',
          tone: hasError ? VivBadgeTone.danger : VivBadgeTone.success,
          icon: hasError ? LucideIcons.triangleAlert : LucideIcons.circleCheck,
        ),
        const SizedBox(height: VivSpacing.space4),
        _buildDiagnosticRow('URL ciblée', report['targetUrl'] ?? ''),
        const SizedBox(height: VivSpacing.space2),
        _buildDiagnosticRow('Jeton d\'accès configuré', report['hasToken'] == true ? 'Oui' : 'Non'),
        const SizedBox(height: VivSpacing.space2),
        _buildDiagnosticRow(
          'Code HTTP retourné',
          report['statusCode'] != null ? '${report['statusCode']}' : 'Aucun (échec réseau)',
          color: report['statusCode'] == 200 ? VivColors.success : VivColors.danger,
        ),
        const SizedBox(height: VivSpacing.space2),
        _buildDiagnosticRow(
          'Version publiée trouvée',
          report['releaseFound'] == true ? 'Oui (tag : ${report['tagName']})' : 'Non',
        ),
        const SizedBox(height: VivSpacing.space2),
        _buildDiagnosticRow('Installeur (.exe) détecté', report['hasExeAsset'] == true ? 'Oui' : 'Non'),
        if (report['error'] != null) ...[
          const SizedBox(height: VivSpacing.space4),
          Text('Message d\'erreur technique', style: VivTypography.headingSm),
          const SizedBox(height: VivSpacing.space2),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(VivSpacing.space3),
            decoration: BoxDecoration(
              color: VivColors.surfaceCode,
              borderRadius: BorderRadius.circular(VivSpacing.radiusSm),
            ),
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: SelectableText(
                '${report['error']}',
                style: VivTypography.code.copyWith(fontSize: 12, color: VivColors.danger),
              ),
            ),
          ),
        ],
      ],
    );
  }

  Widget _buildDiagnosticRow(String label, String value, {Color? color}) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(width: 220, child: Text(label, style: VivTypography.bodySm.copyWith(color: VivColors.inkMuted))),
        Expanded(
          child: Text(
            value,
            style: VivTypography.bodySm.copyWith(color: color ?? VivColors.ink),
            textAlign: TextAlign.right,
          ),
        ),
      ],
    );
  }

  Widget _buildCard(List<Widget> children) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(VivSpacing.space6),
      decoration: VivDecorations.flatCard(),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: children),
    );
  }
}
