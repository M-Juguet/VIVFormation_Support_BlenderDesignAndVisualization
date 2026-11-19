# Lance la passe de captures du chapitre 4, dans une fenêtre Blender séparée, sur le fichier de secours.
# Usage, depuis la racine du dépôt : powershell -NoProfile -ExecutionPolicy Bypass -File tool\exercices_ch4\lancer_captures.ps1 <dossier_sortie> [-Recon] [-Etapes 403,404]
# Le verrou tool\production\capture.lock est posé pendant la passe, puis retiré ; la passe refuse de
# démarrer si une autre session l'a déjà posé.
param([Parameter(Mandatory = $true)] [string]$Sortie, [switch]$Recon, [string]$Etapes = '')
$ErrorActionPreference = 'Stop'
$lock = 'tool\production\capture.lock'
if (Test-Path $lock) { throw ("verrou présent : " + (Get-Content $lock)) }
'chapitre 4 : captures' | Set-Content -Path $lock -Encoding utf8
try {
  $env:BLENDER_USER_CONFIG = Join-Path $env:TEMP 'blender-cfg-captures-ch4'
  if ($Recon) { $env:RECON = '1' } else { Remove-Item Env:RECON -ErrorAction SilentlyContinue }
  $exe = "$env:ProgramFiles\Blender Foundation\Blender 5.2\blender.exe"
  New-Item -ItemType Directory -Force -Path $Sortie | Out-Null
  $f = Resolve-Path '_resources\exercices\PRC02_ch4_lampe_en_studio.blend'
  $argsList = @('--factory-startup', '--enable-event-simulate', '-p', '0', '0', '1600', '960', ('"{0}"' -f $f),
                '--python', ('"{0}"' -f (Resolve-Path 'tool\exercices_ch4\captures_brutes.py')), '--', ('"{0}"' -f $Sortie))
  if ($Etapes) { $argsList += $Etapes.Split(',') }
  $log = Join-Path $Sortie 'journal.log'
  $p = Start-Process -FilePath $exe -ArgumentList $argsList -PassThru -RedirectStandardOutput $log -RedirectStandardError ($log + '.err')
  if (-not $p.WaitForExit(900000)) { Stop-Process -Id $p.Id -Force; Write-Output 'DELAI' }
  Write-Output ("code {0}" -f $p.ExitCode)
  Select-String -Path $log, ($log + '.err') -Pattern 'ECHEC|CAPTURES TERMINEES|Traceback|Error' | ForEach-Object { $_.Line }
} finally {
  Remove-Item $lock -ErrorAction SilentlyContinue
}
