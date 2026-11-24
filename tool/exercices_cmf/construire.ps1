# Construit la planche CMF (deux fichiers), puis la contrôle et la livre en zip.
#   1. build_planche.py : PRC02_CMF_planche_vierge.blend, PRC02_CMF_planche_exemple.blend, blender_assets.cats.txt
#   2. finish_ui.py, dans une fenêtre séparée : espace CMF (Asset Browser, LISEZ-MOI, Outliner réduit), vignettes
#   3. verifier_blend.py sur chaque fichier
#   4. livrer.py : _resources\exercices\PRC02_CMF_planche.zip, relu fichier par fichier
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\exercices_cmf\construire.ps1
$ErrorActionPreference = 'Stop'
$cli = 'tool\blender\blender_cli.ps1'
$exe = "$env:ProgramFiles\Blender Foundation\Blender 5.2\blender.exe"
$py = "$env:ProgramFiles\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe"
$out = & powershell -NoProfile -ExecutionPolicy Bypass -File $cli -Script 'tool\exercices_cmf\build_planche.py' -TimeoutSec 600 -Retries 1
$log = (($out | Select-String 'Journal : (.*)$').Matches | Select-Object -Last 1).Groups[1].Value.Trim()
if ((Test-Path "$log.err") -and (Select-String -Path "$log.err" -Pattern 'Traceback' -Quiet)) {
  Get-Content "$log.err" -Tail 20; throw 'échec : build_planche.py'
}
Select-String -Path $log -Pattern 'ENREGISTRE|ACTIFS' | ForEach-Object { $_.Line }

$dir = 'tool\exercices_cmf\_construction\PRC02_CMF_planche'
$files = @("$dir\PRC02_CMF_planche_vierge.blend", "$dir\PRC02_CMF_planche_exemple.blend")
$lock = 'tool\production\capture.lock'
$own = -not (Test-Path $lock)
if ($own) { 'planche CMF : construction' | Set-Content -Path $lock -Encoding utf8 }
try {
  $env:BLENDER_USER_CONFIG = Join-Path $env:TEMP 'blender-cfg-exercices-cmf'
  $env:UI_LOG = Join-Path $env:TEMP 'ui_cmf.log'
  Remove-Item $env:UI_LOG -ErrorAction SilentlyContinue
  foreach ($f in $files) {
    $p = Start-Process -FilePath $exe -PassThru -ArgumentList @('--factory-startup', '--enable-event-simulate', '-p', '0', '0', '1600', '960',
      ('"{0}"' -f (Resolve-Path $f)), '--python', ('"{0}"' -f (Resolve-Path 'tool\exercices_cmf\finish_ui.py')))
    if (-not $p.WaitForExit(200000)) { Stop-Process -Id $p.Id -Force; throw "délai : finish_ui $f" }
  }
  Get-Content $env:UI_LOG
} finally {
  if ($own) { Remove-Item $lock -ErrorAction SilentlyContinue }
}
foreach ($f in $files) {
  & $exe -b --factory-startup $f --python 'tool\exercices_cmf\verifier_blend.py' 2>&1 |
    Select-String '^(FICHIER|TROUVE|MOTIFS|BIBLIOTHEQUES|REFERENCES|CHEMINS|MONDES|IMAGES EMP|RENDU|VUE|CYCLES|SORTIE|CAMERAS|LUMIERES|EXCLUES|ESPACES|EMPLACEMENTS|SCRIPTS|COLLECTION)' | ForEach-Object { $_.Line }
}
& $py -I 'tool\exercices_cmf\livrer.py'
