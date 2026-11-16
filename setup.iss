; Installeur Windows du support PRC02 - Design & visualisation temps reel avec Blender.
; Compilation conseillee : tool\build_release.ps1, qui lit la version dans pubspec.yaml
; et la transmet ici (/DAppVersion=x.y.z). Sans ce parametre, la valeur ci-dessous sert.

#ifndef AppVersion
  #define AppVersion "0.1.0"
#endif
#define AppName "Blender Design & Visualisation"
#define AppExeName "viv_support_blender_design_viz.exe"

[Setup]
; REMARQUE : AppId identifie l'application. Ne le modifiez jamais d'une version a l'autre,
; sinon les mises a jour s'installeraient a cote de l'ancienne version au lieu de la remplacer.
; Il est propre a ce support : ne le reprenez pas pour un autre support.
AppId={{7FB09CDA-5A09-4AE2-B8D8-CEFB74839E80}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher=VIV Formation
; Installation au niveau utilisateur pour eviter l'UAC (necessaire pour les mises a jour automatiques silencieuses)
DefaultDirName={userpf}\BlenderDesignVisualisation
DefaultGroupName=VIV Formation
DisableProgramGroupPage=yes
SetupIconFile=windows\runner\resources\app_icon.ico
UninstallDisplayIcon={app}\{#AppExeName}
PrivilegesRequired=lowest
OutputDir=Output
OutputBaseFilename=blender_design_visualisation_setup_v{#AppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
; Force la fermeture de l'application Flutter en cours d'execution
CloseApplications=force

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "build\windows\x64\runner\Release\{#AppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\windows\x64\runner\Release\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#AppName}"; Filename: "{app}\{#AppExeName}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExeName}"; Description: "{cm:LaunchProgram,{#AppName}}"; Flags: nowait postinstall skipifsilent
