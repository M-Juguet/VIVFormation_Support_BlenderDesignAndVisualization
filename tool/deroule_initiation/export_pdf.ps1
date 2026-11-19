# Exporte un déroulé formateur en PDF A4 portrait, à la charte VIV Formation.
# 1. md_to_html.py (Python fourni avec Blender 5.2) produit le HTML à côté de ce script
#    (PRC02-deroule-chap1.md -> deroule_chap1.html) ;
# 2. Microsoft Edge en mode headless l'imprime en PDF, à côté du Markdown, sous le même nom.
# Usage, depuis la racine du dépôt :
#   powershell -ExecutionPolicy Bypass -File tool\deroule_initiation\export_pdf.ps1
#   powershell -ExecutionPolicy Bypass -File tool\deroule_initiation\export_pdf.ps1 -Source _resources\PRC02-deroule-chap1.md
param(
  [string]$Source = '_resources\PRC02-deroule-initiation.md'
)
$ErrorActionPreference = 'Stop'

$here   = Split-Path -Parent $MyInvocation.MyCommand.Path
$root   = Resolve-Path (Join-Path $here '..\..')
if (-not [System.IO.Path]::IsPathRooted($Source)) { $Source = Join-Path $root $Source }
$source = (Resolve-Path $Source).Path
$name   = [System.IO.Path]::GetFileNameWithoutExtension($source)          # PRC02-deroule-chap1
$html   = Join-Path $here (($name -replace '^PRC02-', '' -replace '-', '_') + '.html')
$target = [System.IO.Path]::ChangeExtension($source, '.pdf')

$python = 'C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe'
if (-not (Test-Path $python)) { throw "Python de Blender 5.2 introuvable : $python" }
& $python -I (Join-Path $here 'md_to_html.py') $source $html
if ($LASTEXITCODE -ne 0) { throw 'La conversion en HTML a échoué.' }

$edge = @(
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { throw 'Microsoft Edge est introuvable.' }

# Profil temporaire : n'utilise ni ne modifie le profil Edge de l'utilisateur.
$edgeProfile = Join-Path $env:TEMP ('edge-pdf-' + [guid]::NewGuid())
$uri = ([System.Uri]$html).AbsoluteUri
if (Test-Path $target) { Remove-Item $target }

& $edge --headless=new --disable-gpu --no-pdf-header-footer `
  --user-data-dir="$edgeProfile" --print-to-pdf="$target" $uri | Out-Null

# Edge rend la main avant d'avoir fini d'écrire : on attend un fichier de taille stable.
$last = -1
for ($i = 0; $i -lt 60; $i++) {
  Start-Sleep -Milliseconds 500
  if (Test-Path $target) {
    $size = (Get-Item $target).Length
    if ($size -gt 0 -and $size -eq $last) { break }
    $last = $size
  }
}
Remove-Item -Recurse -Force $edgeProfile -ErrorAction SilentlyContinue
if (-not (Test-Path $target)) { throw "Le PDF n'a pas été créé." }
Get-Item $target | Select-Object Name, Length
