<#
.SYNOPSIS
  Compile l'application en mode Release puis produit l'installeur Windows (Inno Setup).

.DESCRIPTION
  1. Lit la version dans pubspec.yaml (ex. 0.1.0+1 -> 0.1.0).
  2. Lance `flutter build windows --release`.
  3. Compile setup.iss avec ISCC en lui transmettant cette version.
  L'installeur est écrit dans Output\blender_design_visualisation_setup_v<version>.exe,
  prêt à être joint à une release GitHub (tag v<version>).

.PARAMETER Flutter
  Chemin de flutter.bat si Flutter n'est pas dans le PATH.

.PARAMETER Iscc
  Chemin de ISCC.exe si Inno Setup n'est pas dans un emplacement standard.

.PARAMETER SkipBuild
  Ne recompile pas l'application, ne refait que l'installeur.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File tool\build_release.ps1
#>
param(
  [string]$Flutter = "",
  [string]$Iscc = "",
  [switch]$SkipBuild
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

# --- Version -----------------------------------------------------------------
$versionLine = Select-String -Path (Join-Path $root 'pubspec.yaml') -Pattern '^version:\s*([0-9]+\.[0-9]+\.[0-9]+)' | Select-Object -First 1
if (-not $versionLine) { throw "Version introuvable dans pubspec.yaml." }
$version = $versionLine.Matches[0].Groups[1].Value
Write-Host "Version : $version"

# --- Outils --------------------------------------------------------------------
if (-not $Flutter) {
  $cmd = Get-Command flutter -ErrorAction SilentlyContinue
  if ($cmd) { $Flutter = $cmd.Source }
  elseif (Test-Path "$env:USERPROFILE\develop\flutter\bin\flutter.bat") { $Flutter = "$env:USERPROFILE\develop\flutter\bin\flutter.bat" }
  else { throw "Flutter introuvable : ajoutez-le au PATH ou passez -Flutter <chemin de flutter.bat>." }
}
if (-not $Iscc) {
  $candidates = @(
    "$env:LOCALAPPDATA\Programs\Inno Setup 6\ISCC.exe",
    "${env:ProgramFiles(x86)}\Inno Setup 6\ISCC.exe",
    "$env:ProgramFiles\Inno Setup 6\ISCC.exe"
  )
  $Iscc = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
  if (-not $Iscc) { throw "ISCC.exe introuvable : installez Inno Setup 6 ou passez -Iscc <chemin>." }
}

# --- Compilation de l'application ----------------------------------------------
if (-not $SkipBuild) {
  & $Flutter build windows --release
  if ($LASTEXITCODE -ne 0) { throw "La compilation Flutter a échoué." }
}

# --- Installeur ----------------------------------------------------------------
& $Iscc "/DAppVersion=$version" (Join-Path $root 'setup.iss')
if ($LASTEXITCODE -ne 0) { throw "La compilation de l'installeur a échoué." }

$setup = Join-Path $root "Output\blender_design_visualisation_setup_v$version.exe"
Write-Host ""
Write-Host "Installeur prêt : $setup"
Write-Host "Publication : créez une release GitHub avec le tag v$version et joignez ce fichier."
