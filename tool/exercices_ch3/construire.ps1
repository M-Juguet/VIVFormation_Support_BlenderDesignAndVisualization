# Construit tous les fichiers d'exercice du chapitre 3, dans l'ordre, puis les contrôle.
#   1. textures_cmf.py (option -Textures) : les cinq images et PRC02_ch3_textures_cmf.zip
#   2. build_bibliotheque.py : le nuancier (fiche B)
#   3. build_lampe.py : la lampe à habiller (fiche A) et la lampe habillée (fiche A2)
#   4. build_finitions.py : les finitions triplanaires (fiche C)
#   5. finish_ui.py, dans une fenêtre séparée : LISEZ-MOI, vignettes des actifs, espace Shading
#   6. livrer.py : PRC02_bibliotheque_CMF.zip et PRC02_ch3_lampe_habillage.zip
#   7. verifier_blend.py sur chaque fichier
# Usage, depuis la racine du dépôt :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\exercices_ch3\construire.ps1 [-Textures]
param([switch]$Textures)
$ErrorActionPreference = 'Stop'
$cli = 'tool\blender\blender_cli.ps1'
$exe = "$env:ProgramFiles\Blender Foundation\Blender 5.2\blender.exe"
$py = "$env:ProgramFiles\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe"
function Build($script, [string[]]$rest) {
  $out = & powershell -NoProfile -ExecutionPolicy Bypass -File $cli -Script $script -TimeoutSec 600 -Retries 1 @rest
  $log = ($out | Select-String 'Journal : (.*)$').Matches | Select-Object -Last 1
  $path = $log.Groups[1].Value.Trim()
  if (Test-Path "$path.err") {
    $tb = Select-String -Path "$path.err" -Pattern 'Traceback' -Quiet
    if ($tb) { Get-Content "$path.err" -Tail 20; throw "échec : $script" }
  }
  Select-String -Path $path -Pattern 'ENREGISTRE|ZIP|ACTIFS' | ForEach-Object { $_.Line }
}
if ($Textures) { Build 'tool\exercices_ch3\textures_cmf.py' @() }
Build 'tool\exercices_ch3\build_bibliotheque.py' @()
Build 'tool\exercices_ch3\build_lampe.py' @()
Build 'tool\exercices_ch3\build_finitions.py' @()

$lock = 'tool\production\capture.lock'
$own = -not (Test-Path $lock)
if ($own) { 'chapitre 3 : construction' | Set-Content -Path $lock -Encoding utf8 }
try {
  $env:BLENDER_USER_CONFIG = Join-Path $env:TEMP 'blender-cfg-exercices-ch3'
  $env:UI_LOG = Join-Path $env:TEMP 'ui_ch3.log'
  Remove-Item $env:UI_LOG -ErrorAction SilentlyContinue
  Remove-Item Env:UI_SHOT -ErrorAction SilentlyContinue
  $files = @('_resources\exercices\PRC02_ch3_lampe_a_habiller.blend',
             'tool\exercices_ch3\_construction\PRC02_ch3_lampe_habillage\PRC02_ch3_lampe_habillage.blend',
             'tool\exercices_ch3\_construction\PRC02_bibliotheque_CMF\PRC02_ch3_nuancier_cmf.blend',
             '_resources\exercices\PRC02_ch3_finitions_triplanaires.blend')
  foreach ($f in $files) {
    $p = Start-Process -FilePath $exe -PassThru -ArgumentList @('--factory-startup', '--enable-event-simulate', '-p', '0', '0', '1600', '960',
      ('"{0}"' -f (Resolve-Path $f)), '--python', ('"{0}"' -f (Resolve-Path 'tool\exercices_ch3\finish_ui.py')))
    if (-not $p.WaitForExit(180000)) { Stop-Process -Id $p.Id -Force; throw "délai : finish_ui $f" }
  }
  Get-Content $env:UI_LOG
} finally {
  if ($own) { Remove-Item $lock -ErrorAction SilentlyContinue }
}
& $py -I 'tool\exercices_ch3\livrer.py'
foreach ($f in $files) {
  & $exe -b --factory-startup $f --python 'tool\exercices_ch3\verifier_blend.py' 2>&1 |
    Select-String '^(FICHIER|TROUVE|MOTIFS|BIBLIOTHEQUES|REFERENCES|CHEMINS)' | ForEach-Object { $_.Line }
}
