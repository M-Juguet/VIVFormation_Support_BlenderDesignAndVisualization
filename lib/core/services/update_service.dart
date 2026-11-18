import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:dio/dio.dart';
import '../models/github_release.dart';
import 'windows_http.dart';

/// Canal par lequel l'API GitHub a répondu.
enum UpdateChannel {
  /// Connexion directe de l'application (Dio).
  direct,

  /// Pile réseau de Windows (WinINet) : proxy et certificats du système.
  windows,
}

/// Résultat d'une interrogation de l'API GitHub.
class _FetchResult {
  final Map<String, dynamic>? json;
  final int? statusCode;
  final UpdateChannel? channel;
  final String? directError;
  final String? windowsError;
  final String? hint;

  const _FetchResult({
    this.json,
    this.statusCode,
    this.channel,
    this.directError,
    this.windowsError,
    this.hint,
  });
}

class UpdateService {
  final Dio _dio = Dio(BaseOptions(
    connectTimeout: const Duration(seconds: 15),
    receiveTimeout: const Duration(seconds: 30),
  ));
  final String owner;
  final String repo;

  // Récupération optionnelle d'un token d'accès via les variables d'environnement (--dart-define=GITHUB_TOKEN=...)
  static const String _githubToken = String.fromEnvironment('GITHUB_TOKEN');

  UpdateService({required this.owner, required this.repo}) {
    if (_githubToken.isNotEmpty) {
      _dio.options.headers['Authorization'] = 'Bearer $_githubToken';
    }
    _dio.options.headers['Accept'] = 'application/vnd.github.v3+json';
  }

  String get _latestReleaseUrl => 'https://api.github.com/repos/$owner/$repo/releases/latest';

  /// Vérifie la dernière version disponible sur GitHub
  Future<GithubRelease?> getLatestRelease() async {
    final result = await _fetchLatestRelease();
    if (result.directError != null) {
      debugPrint('Connexion directe à GitHub impossible : ${result.directError}');
    }
    if (result.windowsError != null) {
      debugPrint('Connexion par le réseau Windows impossible : ${result.windowsError}');
    }
    final json = result.json;
    return json == null ? null : GithubRelease.fromJson(json);
  }

  /// Interroge l'API GitHub, d'abord en direct, puis par le réseau Windows.
  ///
  /// La connexion directe de l'application ignore le proxy du système et peut
  /// refuser le certificat d'un pare-feu qui inspecte les connexions chiffrées,
  /// ce qui est fréquent sur les réseaux d'entreprise et de centres de
  /// formation. Dans ce cas, la requête repasse par WinINet, qui utilise la
  /// même pile réseau que le navigateur.
  Future<_FetchResult> _fetchLatestRelease() async {
    int? statusCode;
    String? directError;
    String? hint;

    try {
      final response = await _dio.get(_latestReleaseUrl);
      statusCode = response.statusCode;
      if (statusCode == 200 && response.data is Map<String, dynamic>) {
        return _FetchResult(
          json: response.data as Map<String, dynamic>,
          statusCode: statusCode,
          channel: UpdateChannel.direct,
        );
      }
      directError = 'Réponse inattendue (HTTP $statusCode).';
    } on DioException catch (e) {
      statusCode = e.response?.statusCode;
      directError = _describeDioError(e);
      hint = _hintFor(e);
      // GitHub a répondu (404, limite de requêtes…) : le réseau n'est pas en
      // cause, un autre canal n'y changerait rien.
      if (e.response != null) {
        return _FetchResult(statusCode: statusCode, directError: directError, hint: hint);
      }
    } catch (e) {
      directError = '${e.runtimeType} : $e';
    }

    final windows = await _fetchTextViaWindows(_latestReleaseUrl);
    if (windows.data != null) {
      try {
        final json = jsonDecode(windows.data!) as Map<String, dynamic>;
        return _FetchResult(
          json: json,
          statusCode: 200,
          channel: UpdateChannel.windows,
          directError: directError,
          hint: hint,
        );
      } catch (e) {
        return _FetchResult(
          statusCode: statusCode,
          directError: directError,
          windowsError: 'Réponse illisible : $e',
          hint: hint,
        );
      }
    }
    return _FetchResult(
      statusCode: statusCode,
      directError: directError,
      windowsError: windows.error,
      hint: hint,
    );
  }

  static String _describeDioError(DioException e) {
    final parts = <String>['Type : ${e.type.name}'];
    if (e.message != null) parts.add('Message : ${e.message}');
    if (e.error != null) parts.add('Cause : ${e.error.runtimeType} : ${e.error}');
    if (e.response != null) parts.add('Réponse : HTTP ${e.response?.statusCode}');
    return parts.join('\n');
  }

  static String? _hintFor(DioException e) {
    final cause = e.error;
    if (cause is TlsException) {
      return 'Le certificat présenté pour api.github.com n\'est pas reconnu par l\'application. '
          'Le réseau inspecte probablement les connexions chiffrées (pare-feu, proxy ou antivirus).';
    }
    if (cause is SocketException ||
        e.type == DioExceptionType.connectionError ||
        e.type == DioExceptionType.connectionTimeout) {
      return 'La connexion directe à api.github.com est bloquée ou doit passer par un proxy.';
    }
    final status = e.response?.statusCode;
    if (status == 403 || status == 429) {
      return 'GitHub limite le nombre de requêtes depuis ce réseau. Réessayez dans une heure.';
    }
    if (status == 404) {
      return 'Aucune version publiée n\'a été trouvée sur le dépôt.';
    }
    return null;
  }

  /// Dossier temporaire réservé aux installeurs de cette application.
  ///
  /// Les mises à jour y sont téléchargées et seul ce dossier est nettoyé :
  /// les autres fichiers du répertoire temporaire de Windows (installeurs
  /// d'autres logiciels, autres supports VIV) ne sont jamais touchés.
  Directory get _updatesDir =>
      Directory('${Directory.systemTemp.path}${Platform.pathSeparator}$repo-updates');

  /// Supprime les installeurs téléchargés lors des mises à jour précédentes.
  Future<void> cleanOldInstallers() async {
    try {
      final dir = _updatesDir;
      if (!await dir.exists()) return;
      await for (final entity in dir.list()) {
        if (entity is File && entity.path.toLowerCase().endsWith('.exe')) {
          try {
            await entity.delete();
          } catch (_) {
            // Fichier potentiellement en cours d'utilisation
          }
        }
      }
    } catch (e) {
      debugPrint('Erreur lors du nettoyage des installeurs : $e');
    }
  }

  /// Télécharge la mise à jour et renvoie le chemin du fichier local
  Future<String?> downloadUpdate(
    String url,
    void Function(int count, int total) onReceiveProgress, {
    int expectedSize = 0,
  }) async {
    final String savePath;
    try {
      // Nettoyage préalable des installeurs de cette application uniquement
      await cleanOldInstallers();

      final dir = _updatesDir;
      await dir.create(recursive: true);
      final fileName = url.split('/').last.split('?').first;
      // On s'assure d'avoir un nom valide
      final safeFileName = fileName.toLowerCase().endsWith('.exe') ? fileName : 'update.exe';
      savePath = '${dir.path}${Platform.pathSeparator}$safeFileName';
    } catch (e) {
      debugPrint('Erreur lors de la préparation du téléchargement : $e');
      return null;
    }

    try {
      await _dio.download(
        url,
        savePath,
        onReceiveProgress: onReceiveProgress,
        options: Options(
          receiveTimeout: const Duration(seconds: 60),
          headers: {
            'Accept': 'application/octet-stream',
            if (_githubToken.isNotEmpty) 'Authorization': 'Bearer $_githubToken',
          },
        ),
      );
      return savePath;
    } catch (e) {
      debugPrint('Téléchargement direct impossible, essai par le réseau Windows : $e');
    }

    // Repli : téléchargement par la pile réseau de Windows.
    final file = File(savePath);
    try {
      if (await file.exists()) await file.delete();
    } catch (_) {}

    final total = expectedSize > 0 ? expectedSize : -1;
    final timer = Timer.periodic(const Duration(milliseconds: 500), (_) {
      try {
        if (file.existsSync()) onReceiveProgress(file.lengthSync(), total);
      } catch (_) {}
    });
    final result = await _downloadViaWindows(url, savePath);
    timer.cancel();

    try {
      if (result.error == null && await file.exists()) {
        final length = await file.length();
        if (expectedSize == 0 || length == expectedSize) {
          onReceiveProgress(length, length);
          return savePath;
        }
        debugPrint('Installeur incomplet : $length octets sur $expectedSize.');
      } else {
        debugPrint('Erreur lors du téléchargement par le réseau Windows : ${result.error}');
      }
    } catch (e) {
      debugPrint('Erreur lors de la vérification de l\'installeur : $e');
    }
    return null;
  }

  /// Lance l'installeur en mode détaché et ferme l'application courante
  Future<void> runInstaller(String filePath) async {
    try {
      await Process.start(
        filePath,
        ['/SILENT'], // Optionnel : /SILENT ou /VERYSILENT selon la configuration InnoSetup
        mode: ProcessStartMode.detached,
      );
      // On ferme l'application Flutter pour libérer les fichiers afin qu'InnoSetup puisse les écraser
      exit(0);
    } catch (e) {
      debugPrint('Erreur lors du lancement de l\'installeur : $e');
      rethrow;
    }
  }

  /// Diagnostique la connexion à l'API GitHub et renvoie un rapport détaillé
  Future<Map<String, dynamic>> diagnoseConnection() async {
    final Map<String, dynamic> report = {
      'targetUrl': _latestReleaseUrl,
      'hasToken': _githubToken.isNotEmpty,
      'channel': null,
      'statusCode': null,
      'directError': null,
      'windowsError': null,
      'hint': null,
      'releaseFound': false,
      'tagName': null,
      'hasExeAsset': false,
      'downloadUrl': null,
    };

    try {
      final result = await _fetchLatestRelease();
      report['channel'] = result.channel?.name;
      report['statusCode'] = result.statusCode;
      report['directError'] = result.directError;
      report['windowsError'] = result.windowsError;
      report['hint'] = result.hint;

      final json = result.json;
      if (json != null) {
        final release = GithubRelease.fromJson(json);
        report['releaseFound'] = true;
        report['tagName'] = release.tagName;
        if (release.downloadUrl.isNotEmpty) {
          report['hasExeAsset'] = true;
          report['downloadUrl'] = release.downloadUrl;
        }
      }
    } catch (e) {
      report['directError'] = '${e.runtimeType} : $e';
    }
    return report;
  }

  // --- Pile réseau de Windows (WinINet) --------------------------------------

  Map<String, String> _windowsHeaders(String accept) => {
        'Accept': accept,
        if (_githubToken.isNotEmpty) 'Authorization': 'Bearer $_githubToken',
      };

  Future<({String? data, String? error})> _fetchTextViaWindows(String url) async {
    try {
      final result = await windowsHttpGet(url, headers: _windowsHeaders('application/vnd.github.v3+json'))
          .timeout(const Duration(seconds: 120));
      if (result.body != null) return (data: utf8.decode(result.body!), error: null);
      return (data: null, error: result.error ?? 'Réponse vide.');
    } on TimeoutException {
      return (data: null, error: 'Délai dépassé (120 s).');
    } catch (e) {
      return (data: null, error: '${e.runtimeType} : $e');
    }
  }

  Future<({String? data, String? error})> _downloadViaWindows(String url, String savePath) async {
    try {
      final result = await windowsHttpDownload(url, savePath, headers: _windowsHeaders('application/octet-stream'))
          .timeout(const Duration(minutes: 20));
      return (data: result.error == null ? savePath : null, error: result.error);
    } on TimeoutException {
      return (data: null, error: 'Délai dépassé (20 min).');
    } catch (e) {
      return (data: null, error: '${e.runtimeType} : $e');
    }
  }
}
