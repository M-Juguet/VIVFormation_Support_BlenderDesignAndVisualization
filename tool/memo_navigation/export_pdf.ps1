# Exporte memo_navigation_blender.html en PDF A4 paysage avec Microsoft Edge en mode headless.
# Usage : powershell -ExecutionPolicy Bypass -File tool\memo_navigation\export_pdf.ps1
$ErrorActionPreference = 'Stop'

$here   = Split-Path -Parent $MyInvocation.MyCommand.Path
$root   = Resolve-Path (Join-Path $here '..\..')
$source = Join-Path $here 'memo_navigation_blender.html'
$target = Join-Path $root '_resources\exercices\memo_navigation_blender.pdf'

$edge = @(
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { throw 'Microsoft Edge est introuvable.' }

# Profil temporaire : n'utilise ni ne modifie le profil Edge de l'utilisateur.
$edgeProfile = Join-Path $env:TEMP ('edge-pdf-' + [guid]::NewGuid())
$uri = ([System.Uri]$source).AbsoluteUri

& $edge --headless=new --disable-gpu --no-pdf-header-footer `
  --user-data-dir="$edgeProfile" --print-to-pdf="$target" $uri | Out-Null

Start-Sleep -Milliseconds 500
Remove-Item -Recurse -Force $edgeProfile -ErrorAction SilentlyContinue
if (-not (Test-Path $target)) { throw "Le PDF n'a pas été créé." }
Get-Item $target | Select-Object Name, Length
