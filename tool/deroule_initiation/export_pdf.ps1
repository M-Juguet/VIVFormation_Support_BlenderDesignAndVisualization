# Exporte _resources\PRC02-deroule-initiation.md en PDF A4 portrait, à la charte VIV Formation.
# 1. md_to_html.py (Python fourni avec Blender 5.2) produit deroule_initiation.html à côté de ce script ;
# 2. Microsoft Edge en mode headless l'imprime en PDF, à côté du Markdown.
# Usage : powershell -ExecutionPolicy Bypass -File tool\deroule_initiation\export_pdf.ps1
$ErrorActionPreference = 'Stop'

$here   = Split-Path -Parent $MyInvocation.MyCommand.Path
$root   = Resolve-Path (Join-Path $here '..\..')
$source = Join-Path $root '_resources\PRC02-deroule-initiation.md'
$html   = Join-Path $here 'deroule_initiation.html'
$target = Join-Path $root '_resources\PRC02-deroule-initiation.pdf'

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

Start-Sleep -Milliseconds 800
Remove-Item -Recurse -Force $edgeProfile -ErrorAction SilentlyContinue
if (-not (Test-Path $target)) { throw "Le PDF n'a pas été créé." }
Get-Item $target | Select-Object Name, Length
