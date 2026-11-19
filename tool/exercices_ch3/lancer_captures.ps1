# Lance les quatre passes de captures du chapitre 3, une fenêtre Blender séparée par fichier.
# Usage, depuis la racine du dépôt : powershell -NoProfile -ExecutionPolicy Bypass -File tool\exercices_ch3\lancer_captures.ps1 <dossier_sortie> [-Recon] [-Fichiers a,a2,b,c] [-Etapes 302,303]
# Le verrou tool\production\capture.lock doit être posé (par cette session) avant le lancement.
param([Parameter(Mandatory = $true)] [string]$Sortie, [switch]$Recon, [string]$Fichiers = 'a,a2,b,c', [string]$Etapes = '')
$ErrorActionPreference = 'Stop'
$env:BLENDER_USER_CONFIG = Join-Path $env:TEMP 'blender-cfg-captures-ch3'
if ($Recon) { $env:RECON = '1' } else { Remove-Item Env:RECON -ErrorAction SilentlyContinue }
$map = @{
  'a'  = '_resources\exercices\PRC02_ch3_lampe_a_habiller.blend';
  'a2' = 'tool\exercices_ch3\_construction\PRC02_ch3_lampe_habillage\PRC02_ch3_lampe_habillage.blend';
  'b'  = 'tool\exercices_ch3\_construction\PRC02_bibliotheque_CMF\PRC02_ch3_nuancier_cmf.blend';
  'c'  = '_resources\exercices\PRC02_ch3_finitions_triplanaires.blend' }
$exe = "$env:ProgramFiles\Blender Foundation\Blender 5.2\blender.exe"
New-Item -ItemType Directory -Force -Path $Sortie | Out-Null
foreach ($k in $Fichiers.Split(',')) {
  $f = Resolve-Path $map[$k]
  $argsList = @('--factory-startup', '--enable-event-simulate', '-p', '0', '0', '1600', '960', ('"{0}"' -f $f),
                '--python', ('"{0}"' -f (Resolve-Path 'tool\exercices_ch3\captures_brutes.py')), '--', ('"{0}"' -f $Sortie))
  if ($Etapes) { $argsList += $Etapes.Split(',') }
  $log = Join-Path $Sortie ("journal_" + $k + ".log")
  $p = Start-Process -FilePath $exe -ArgumentList $argsList -PassThru -RedirectStandardOutput $log -RedirectStandardError ($log + '.err')
  if (-not $p.WaitForExit(900000)) { Stop-Process -Id $p.Id -Force; Write-Output "DELAI $k" }
  Write-Output ("{0} : code {1}" -f $k, $p.ExitCode)
  Select-String -Path $log -Pattern 'ECHEC|CAPTURES TERMINEES' | ForEach-Object { $_.Line }
}
