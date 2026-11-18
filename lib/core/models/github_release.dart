class GithubRelease {
  final String tagName;
  final String body;
  final String downloadUrl;

  /// Taille de l'installeur en octets, telle que l'annonce GitHub (0 si inconnue).
  final int downloadSize;

  GithubRelease({
    required this.tagName,
    required this.body,
    required this.downloadUrl,
    this.downloadSize = 0,
  });

  factory GithubRelease.fromJson(Map<String, dynamic> json) {
    String url = '';
    int size = 0;

    // On cherche l'asset qui se termine par .exe
    if (json['assets'] != null) {
      final assets = json['assets'] as List;
      for (var asset in assets) {
        final downloadUrl = asset['browser_download_url'] as String?;
        if (downloadUrl != null && downloadUrl.endsWith('.exe')) {
          url = downloadUrl;
          size = (asset['size'] as num?)?.toInt() ?? 0;
          break; // Prend le premier .exe trouvé
        }
      }
    }

    return GithubRelease(
      tagName: json['tag_name'] ?? '',
      body: json['body'] ?? '',
      downloadUrl: url,
      downloadSize: size,
    );
  }

  // Retourne la version sémantique pure sans le "v" (ex: "v1.0.0" -> "1.0.0")
  String get semanticVersion {
    if (tagName.toLowerCase().startsWith('v')) {
      return tagName.substring(1);
    }
    return tagName;
  }
}
