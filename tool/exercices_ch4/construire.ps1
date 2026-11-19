# Construit les deux fichiers d'exercice du chapitre 4, puis les contrôle.
#   1. build_studio.py : le fichier de secours PRC02_ch4_lampe_en_studio.blend, puis le studio PRC02_ch4_studio.blend
#   2. finish_ui.py, dans une fenêtre séparée : zone LISEZ-MOI, Outliner replié, vignettes des actifs
#   3. verifier_blend.py sur chaque fichier
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\exercices_ch4\construire.ps1
$ErrorActionPreference = 'Stop'
$cli = 'tool\blender\blender_cli.ps1'
$exe = "$env:ProgramFiles\Blender Foundation\Blender 5.2\blender.exe"
$out = & powershell -NoProfile -ExecutionPolicy Bypass -File $cli -Script 'tool\exercices_ch4\build_studio.py' -TimeoutSec 600 -Retries 1
$log = (($out | Select-String 'Journal : (.*)$').Matches | Select-Object -Last 1).Groups[1].Value.Trim()
if ((Test-Path "$log.err") -and (Select-String -Path "$log.err" -Pattern 'Traceback' -Quiet)) {
  Get-Content "$log.err" -Tail 20; throw 'échec : build_studio.py'
}
Select-String -Path $log -Pattern 'ENREGISTRE|BANDE' | ForEach-Object { $_.Line }

$files = @('_resources\exercices\PRC02_ch4_lampe_en_studio.blend', '_resources\exercices\PRC02_ch4_studio.blend')
$lock = 'tool\production\capture.lock'
$own = -not (Test-Path $lock)
if ($own) { 'chapitre 4 : construction' | Set-Content -Path $lock -Encoding utf8 }
try {
  $env:BLENDER_USER_CONFIG = Join-Path $env:TEMP 'blender-cfg-exercices-ch4'
  $env:UI_LOG = Join-Path $env:TEMP 'ui_ch4.log'
  Remove-Item $env:UI_LOG -ErrorAction SilentlyContinue
  foreach ($f in $files) {
    $p = Start-Process -FilePath $exe -PassThru -ArgumentList @('--factory-startup', '--enable-event-simulate', '-p', '0', '0', '1600', '960',
      ('"{0}"' -f (Resolve-Path $f)), '--python', ('"{0}"' -f (Resolve-Path 'tool\exercices_ch4\finish_ui.py')))
    if (-not $p.WaitForExit(180000)) { Stop-Process -Id $p.Id -Force; throw "délai : finish_ui $f" }
  }
  Get-Content $env:UI_LOG
} finally {
  if ($own) { Remove-Item $lock -ErrorAction SilentlyContinue }
}
foreach ($f in $files) {
  & $exe -b --factory-startup $f --python 'tool\exercices_ch4\verifier_blend.py' 2>&1 |
    Select-String '^(FICHIER|TROUVE|MOTIFS|BIBLIOTHEQUES|REFERENCES|CHEMINS|MONDES|IMAGES|RENDU|MASQUEES|RAYTRACING|COLLECTION|MOTEUR)' | ForEach-Object { $_.Line }
}
