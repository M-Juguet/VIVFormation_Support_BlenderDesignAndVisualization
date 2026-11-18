# Lance Blender en arrière-plan sur un script Python, avec un délai maximal et des reprises.
#
# Un Blender qui plante ou se fige n'arrête pas le travail : le processus lancé par ce
# script est fermé au bout du délai, puis relancé. Seul ce processus est touché ;
# aucun autre Blender ouvert n'est fermé.
#
# Usage :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\blender_cli.ps1 `
#     -Script tool\exercices_ch2\build_lampe.py [-Blend fichier.blend] [-TimeoutSec 900] [-Retries 2] [arguments du script, à la suite]
#
# Code de sortie : celui de Blender au dernier essai, ou 124 si le délai est dépassé.
[CmdletBinding(PositionalBinding = $false)]
param(
  [Parameter(Mandatory = $true)] [string]$Script,
  [string]$Blend = '',
  [int]$TimeoutSec = 900,
  [int]$Retries = 2,
  [switch]$NoFactoryStartup,
  [string]$BlenderExe = "$env:ProgramFiles\Blender Foundation\Blender 5.2\blender.exe",
  [Parameter(ValueFromRemainingArguments = $true)] [string[]]$ScriptArgs
)
$ErrorActionPreference = 'Stop'
$logDir = Join-Path $PSScriptRoot 'journaux'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp = '{0:yyyyMMdd-HHmmss}' -f (Get-Date)
$name = [IO.Path]::GetFileNameWithoutExtension($Script)

$argList = @('-b')
if (-not $NoFactoryStartup) { $argList += '--factory-startup' }
if ($Blend) { $argList += ('"{0}"' -f (Resolve-Path $Blend)) }
$argList += @('--python', ('"{0}"' -f (Resolve-Path $Script)))
if ($ScriptArgs -and $ScriptArgs.Count -gt 0) {
  $rest = @($ScriptArgs)
  if ($rest.Count -gt 0) { $argList += '--'; $argList += ($rest | ForEach-Object { '"{0}"' -f $_ }) }
}

for ($try = 1; $try -le ($Retries + 1); $try++) {
  $out = Join-Path $logDir "$stamp-$name-essai$try.log"
  $err = "$out.err"
  $p = Start-Process -FilePath $BlenderExe -ArgumentList $argList -NoNewWindow -PassThru `
    -RedirectStandardOutput $out -RedirectStandardError $err
  $null = $p.Handle  # garde le handle : sans lui, ExitCode reste vide après WaitForExit
  if ($p.WaitForExit($TimeoutSec * 1000)) {
    $code = $p.ExitCode
    Write-Output "Essai $try : Blender terminé, code $code. Journal : $out"
    if ($code -eq 0) { Get-Content $out -Tail 15; exit 0 }
  } else {
    Write-Output "Essai $try : délai de $TimeoutSec s dépassé, fermeture du processus $($p.Id)."
    Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
    $code = 124
  }
  if ($try -le $Retries) { Start-Sleep -Seconds 5 }
}
Get-Content $out -Tail 30
exit $code
