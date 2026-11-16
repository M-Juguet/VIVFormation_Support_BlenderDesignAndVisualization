import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shadcn_ui/shadcn_ui.dart';
import 'package:window_manager/window_manager.dart';
import 'package:intl/date_symbol_data_local.dart';

import 'core/data/course_data.dart';
import 'core/theme/viv_theme.dart';
import 'core/theme/viv_shadcn_theme.dart';
import 'core/router/app_router.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await initializeDateFormatting('fr_FR', null);

  await windowManager.ensureInitialized();

  const windowOptions = WindowOptions(
    size: Size(1280, 800),
    minimumSize: Size(1280, 800),
    center: true,
    backgroundColor: Colors.transparent,
    skipTaskbar: false,
    title: CourseData.trainingTitle,
    titleBarStyle: TitleBarStyle.hidden,
  );

  windowManager.waitUntilReadyToShow(windowOptions, () async {
    await windowManager.show();
    await windowManager.focus();
  });

  runApp(
    const ProviderScope(
      child: VivSupportApp(),
    ),
  );
}

class VivSupportApp extends ConsumerWidget {
  const VivSupportApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final goRouter = ref.watch(routerProvider);

    return ShadApp.router(
      title: CourseData.trainingTitle,
      debugShowCheckedModeBanner: false,
      theme: VivShadcnTheme.lightTheme,
      materialThemeBuilder: (context, shadTheme) {
        return VivTheme.lightTheme;
      },
      routerConfig: goRouter,
    );
  }
}
