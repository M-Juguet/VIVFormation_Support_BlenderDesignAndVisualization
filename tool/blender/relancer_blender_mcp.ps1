# Vérifie que le serveur MCP de Blender répond et le relance au besoin, sans intervention.
#
# Le module MCP de Blender (extension « MCP » de Blender Lab) écoute sur localhost:9876.
# Son option « Auto Start » est active par défaut : un Blender relancé normalement
# (profil utilisateur, extensions chargées) redémarre le serveur tout seul.
#
# Usage :
#   powershell -NoProfile -ExecutionPolicy Bypass -File tool\blender\relancer_blender_mcp.ps1
#   ... -Mode Background     serveur MCP sans fenêtre (blender --background --command blender_mcp)
#   ... -ForceRestart        ferme un Blender figé (ne répond plus) avant de relancer
#
# Le script ne ferme jamais un Blender qui répond : une session de travail ouverte
# n'est jamais interrompue. Il écrit un journal dans tool\blender\relance.log.
param(
  [ValidateSet('Gui', 'Background')] [string]$Mode = 'Gui',
  [int]$Port = 9876,
  [int]$WaitSeconds = 90,
  [switch]$ForceRestart,
  [string]$BlenderExe = "$env:ProgramFiles\Blender Foundation\Blender 5.2\blender.exe"
)
$ErrorActionPreference = 'Stop'
$log = Join-Path $PSScriptRoot 'relance.log'
function Log([string]$msg) {
  $line = '{0:yyyy-MM-dd HH:mm:ss}  {1}' -f (Get-Date), $msg
  Add-Content -Path $log -Value $line -Encoding utf8
  Write-Output $line
}
function PortOpen {
  try {
    $c = New-Object System.Net.Sockets.TcpClient
    $iar = $c.BeginConnect('127.0.0.1', $Port, $null, $null)
    $ok = $iar.AsyncWaitHandle.WaitOne(1500) -and $c.Connected
    $c.Close()
    return $ok
  } catch { return $false }
}

if (-not (Test-Path $BlenderExe)) { Log "ERREUR : Blender introuvable ($BlenderExe)."; exit 2 }

if (PortOpen) { Log "OK : le serveur MCP répond sur le port $Port. Rien à faire."; exit 0 }
Log "Le serveur MCP ne répond pas sur le port $Port."

$procs = @(Get-Process blender -ErrorAction SilentlyContinue)
if ($procs.Count -gt 0) {
  $hung = @($procs | Where-Object { -not $_.Responding })
  if ($hung.Count -gt 0) {
    # Deuxième lecture après 20 s : un Blender occupé par un long calcul répond de nouveau.
    Start-Sleep -Seconds 20
    $hung = @($hung | Where-Object { $p = Get-Process -Id $_.Id -ErrorAction SilentlyContinue; $p -and -not $p.Responding })
  }
  if ($hung.Count -gt 0) {
    if ($ForceRestart) {
      foreach ($p in $hung) { Log "Blender figé (PID $($p.Id), « $($p.MainWindowTitle) ») : fermeture forcée."; Stop-Process -Id $p.Id -Force }
      Start-Sleep -Seconds 3
    } else {
      Log "Blender figé (PID $(($hung | ForEach-Object Id) -join ', ')). Relancez avec -ForceRestart pour le fermer."
      exit 3
    }
  } elseif ($Mode -eq 'Gui') {
    Log "Un Blender répond déjà (PID $(($procs | ForEach-Object Id) -join ', ')) sans serveur MCP : lancement d'une nouvelle instance."
  }
}

if ($Mode -eq 'Background') {
  $bgArgs = @('--background', '--command', 'blender_mcp', '--port', "$Port")
  $p = Start-Process -FilePath $BlenderExe -ArgumentList $bgArgs -WindowStyle Hidden -PassThru
  Log "Serveur MCP lancé sans fenêtre (PID $($p.Id))."
} else {
  $p = Start-Process -FilePath $BlenderExe -PassThru
  Log "Blender lancé avec le profil utilisateur (PID $($p.Id)) ; le serveur MCP démarre seul (Auto Start)."
}

$deadline = (Get-Date).AddSeconds($WaitSeconds)
while ((Get-Date) -lt $deadline) {
  Start-Sleep -Seconds 3
  if (PortOpen) { Log "OK : le serveur MCP répond de nouveau sur le port $Port."; exit 0 }
}
Log "ERREUR : le serveur MCP ne répond toujours pas après $WaitSeconds s."
exit 1
