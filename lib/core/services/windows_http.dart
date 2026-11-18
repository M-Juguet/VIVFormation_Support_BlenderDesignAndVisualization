import 'dart:ffi';
import 'dart:io';
import 'dart:isolate';
import 'dart:typed_data';

import 'package:ffi/ffi.dart';

/// Requêtes HTTP par WinINet, la pile réseau de Windows.
///
/// Contrairement au client HTTP de Dart, WinINet utilise le proxy configuré
/// dans Windows (y compris un script PAC ou la détection automatique) et le
/// magasin de certificats de Windows. C'est la pile du navigateur : si GitHub
/// s'ouvre dans Edge, il répond aussi par ce canal, même derrière un pare-feu
/// qui inspecte les connexions chiffrées.
///
/// Les appels sont bloquants : ils s'exécutent dans un isolate séparé, sans
/// processus externe ni fenêtre de console.
class WindowsHttpResult {
  final int statusCode;
  final Uint8List? body;
  final String? error;

  const WindowsHttpResult({this.statusCode = 0, this.body, this.error});
}

/// Lit une URL en mémoire.
Future<WindowsHttpResult> windowsHttpGet(String url, {Map<String, String> headers = const {}}) {
  final headerText = _formatHeaders(headers);
  return Isolate.run(() => _request(url, headerText, null));
}

/// Télécharge une URL dans un fichier, écrit au fil de la réception.
Future<WindowsHttpResult> windowsHttpDownload(String url, String savePath,
    {Map<String, String> headers = const {}}) {
  final headerText = _formatHeaders(headers);
  return Isolate.run(() => _request(url, headerText, savePath));
}

String _formatHeaders(Map<String, String> headers) =>
    headers.entries.map((e) => '${e.key}: ${e.value}\r\n').join();

// --- Liaisons WinINet ---------------------------------------------------------

const int _internetOpenTypePreconfig = 0;
const int _internetOptionConnectTimeout = 2;
const int _internetOptionReceiveTimeout = 6;
const int _httpQueryStatusCode = 19;
const int _httpQueryFlagNumber = 0x20000000;
// INTERNET_FLAG_RELOAD | NO_CACHE_WRITE | NO_COOKIES | NO_UI
const int _openUrlFlags = 0x80000000 | 0x04000000 | 0x00080000 | 0x00000200;
const String _userAgent = 'VIV-Support-PRC02';

typedef _InternetOpenC = Pointer<Void> Function(Pointer<Utf16>, Uint32, Pointer<Utf16>, Pointer<Utf16>, Uint32);
typedef _InternetOpenDart = Pointer<Void> Function(Pointer<Utf16>, int, Pointer<Utf16>, Pointer<Utf16>, int);
typedef _InternetOpenUrlC = Pointer<Void> Function(Pointer<Void>, Pointer<Utf16>, Pointer<Utf16>, Uint32, Uint32, IntPtr);
typedef _InternetOpenUrlDart = Pointer<Void> Function(Pointer<Void>, Pointer<Utf16>, Pointer<Utf16>, int, int, int);
typedef _HttpQueryInfoC = Int32 Function(Pointer<Void>, Uint32, Pointer<Void>, Pointer<Uint32>, Pointer<Uint32>);
typedef _HttpQueryInfoDart = int Function(Pointer<Void>, int, Pointer<Void>, Pointer<Uint32>, Pointer<Uint32>);
typedef _InternetReadFileC = Int32 Function(Pointer<Void>, Pointer<Uint8>, Uint32, Pointer<Uint32>);
typedef _InternetReadFileDart = int Function(Pointer<Void>, Pointer<Uint8>, int, Pointer<Uint32>);
typedef _InternetSetOptionC = Int32 Function(Pointer<Void>, Uint32, Pointer<Void>, Uint32);
typedef _InternetSetOptionDart = int Function(Pointer<Void>, int, Pointer<Void>, int);
typedef _InternetCloseHandleC = Int32 Function(Pointer<Void>);
typedef _InternetCloseHandleDart = int Function(Pointer<Void>);
typedef _GetLastErrorC = Uint32 Function();
typedef _GetLastErrorDart = int Function();

class _WinInet {
  _WinInet._(DynamicLibrary wininet, DynamicLibrary kernel32)
      : open = wininet.lookupFunction<_InternetOpenC, _InternetOpenDart>('InternetOpenW'),
        openUrl = wininet.lookupFunction<_InternetOpenUrlC, _InternetOpenUrlDart>('InternetOpenUrlW'),
        queryInfo = wininet.lookupFunction<_HttpQueryInfoC, _HttpQueryInfoDart>('HttpQueryInfoW'),
        readFile = wininet.lookupFunction<_InternetReadFileC, _InternetReadFileDart>('InternetReadFile'),
        setOption = wininet.lookupFunction<_InternetSetOptionC, _InternetSetOptionDart>('InternetSetOptionW'),
        closeHandle = wininet.lookupFunction<_InternetCloseHandleC, _InternetCloseHandleDart>('InternetCloseHandle'),
        lastError = kernel32.lookupFunction<_GetLastErrorC, _GetLastErrorDart>('GetLastError');

  factory _WinInet.load() =>
      _WinInet._(DynamicLibrary.open('wininet.dll'), DynamicLibrary.open('kernel32.dll'));

  final _InternetOpenDart open;
  final _InternetOpenUrlDart openUrl;
  final _HttpQueryInfoDart queryInfo;
  final _InternetReadFileDart readFile;
  final _InternetSetOptionDart setOption;
  final _InternetCloseHandleDart closeHandle;
  final _GetLastErrorDart lastError;
}

/// Libellés des erreurs WinINet les plus fréquentes.
String _describeError(String step, int code) {
  const labels = {
    12002: 'délai dépassé',
    12007: 'nom de serveur introuvable',
    12029: 'connexion impossible',
    12030: 'connexion interrompue',
    12031: 'connexion réinitialisée',
    12037: 'certificat expiré ou pas encore valide',
    12038: 'nom du certificat incorrect',
    12044: 'certificat client demandé',
    12045: 'autorité de certification non reconnue',
    12057: 'révocation du certificat impossible à vérifier',
    12175: 'erreur du canal sécurisé (TLS)',
  };
  final label = labels[code];
  return 'WinINet, $step : erreur $code${label != null ? ' ($label)' : ''}';
}

/// Requête synchrone, exécutée dans un isolate.
WindowsHttpResult _request(String url, String headers, String? savePath) {
  if (!Platform.isWindows) {
    return const WindowsHttpResult(error: 'Canal réservé à Windows.');
  }

  final api = _WinInet.load();
  final agent = _userAgent.toNativeUtf16(allocator: calloc);
  final urlPtr = url.toNativeUtf16(allocator: calloc);
  final headersPtr = headers.isEmpty ? nullptr : headers.toNativeUtf16(allocator: calloc);
  final buffer = calloc<Uint8>(65536);
  final bytesRead = calloc<Uint32>();
  final status = calloc<Uint32>();
  final statusLength = calloc<Uint32>()..value = 4;
  final option = calloc<Uint32>();
  var session = nullptr.cast<Void>();
  var request = nullptr.cast<Void>();
  RandomAccessFile? file;

  try {
    session = api.open(agent, _internetOpenTypePreconfig, nullptr, nullptr, 0);
    if (session == nullptr) {
      return WindowsHttpResult(error: _describeError('ouverture de session', api.lastError()));
    }
    option.value = 30000;
    api.setOption(session, _internetOptionConnectTimeout, option.cast(), 4);
    option.value = 60000;
    api.setOption(session, _internetOptionReceiveTimeout, option.cast(), 4);

    request = api.openUrl(
      session,
      urlPtr,
      headersPtr,
      headers.isEmpty ? 0 : 0xFFFFFFFF, // -1 : en-têtes terminés par un zéro
      _openUrlFlags,
      0,
    );
    if (request == nullptr) {
      return WindowsHttpResult(error: _describeError('connexion', api.lastError()));
    }

    if (api.queryInfo(request, _httpQueryStatusCode | _httpQueryFlagNumber, status.cast(), statusLength, nullptr) == 0) {
      return WindowsHttpResult(error: _describeError('lecture du statut', api.lastError()));
    }
    final code = status.value;
    if (code != 200) {
      return WindowsHttpResult(statusCode: code, error: 'Réponse HTTP $code');
    }

    final builder = BytesBuilder(copy: false);
    if (savePath != null) file = File(savePath).openSync(mode: FileMode.write);
    while (true) {
      if (api.readFile(request, buffer, 65536, bytesRead) == 0) {
        return WindowsHttpResult(statusCode: code, error: _describeError('réception', api.lastError()));
      }
      final count = bytesRead.value;
      if (count == 0) break;
      final chunk = Uint8List.fromList(buffer.asTypedList(count));
      if (file != null) {
        file.writeFromSync(chunk);
      } else {
        builder.add(chunk);
      }
    }
    return WindowsHttpResult(statusCode: code, body: file == null ? builder.takeBytes() : null);
  } catch (e) {
    return WindowsHttpResult(error: '${e.runtimeType} : $e');
  } finally {
    try {
      file?.closeSync();
    } catch (_) {}
    if (request != nullptr) api.closeHandle(request);
    if (session != nullptr) api.closeHandle(session);
    calloc.free(agent);
    calloc.free(urlPtr);
    if (headersPtr != nullptr) calloc.free(headersPtr);
    calloc.free(buffer);
    calloc.free(bytesRead);
    calloc.free(status);
    calloc.free(statusLength);
    calloc.free(option);
  }
}
