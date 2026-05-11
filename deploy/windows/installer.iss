; Data-Continuum Installer Script for Inno Setup
#define MyAppName "Data-Continuum"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "Data-Continuum Team"
#define MyAppURL "https://github.com/rakrsh/data-continuum"
#define MyAppExeName "data-continuum-api.exe"

[Setup]
AppId={{D1A2B3C4-E5F6-4A5B-8C9D-0E1F2A3B4C5D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppProvider={#MyAppPublisher}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=dist
OutputBaseFilename=DataContinuumInstaller
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Compiled executables from Nuitka
Source: "build\data-continuum-api.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\data-continuum-ml.exe"; DestDir: "{app}"; Flags: ignoreversion
; UI static files
Source: "ui\dist\*"; DestDir: "{app}\ui"; Flags: ignoreversion recursesubdirs createallsubdirs
; NSSM for service management
Source: "deploy\windows\nssm.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Install services using NSSM
Filename: "{app}\nssm.exe"; Parameters: "install DC_API ""{app}\data-continuum-api.exe"""; Flags: runhidden
Filename: "{app}\nssm.exe"; Parameters: "set DC_API AppDirectory ""{app}"""; Flags: runhidden
Filename: "{app}\nssm.exe"; Parameters: "install DC_ML ""{app}\data-continuum-ml.exe"""; Flags: runhidden
Filename: "{app}\nssm.exe"; Parameters: "set DC_ML AppDirectory ""{app}"""; Flags: runhidden
; Start services
Filename: "{app}\nssm.exe"; Parameters: "start DC_API"; Flags: runhidden
Filename: "{app}\nssm.exe"; Parameters: "start DC_ML"; Flags: runhidden

[UninstallRun]
; Stop and remove services
Filename: "{app}\nssm.exe"; Parameters: "stop DC_API"; Flags: runhidden
Filename: "{app}\nssm.exe"; Parameters: "remove DC_API confirm"; Flags: runhidden
Filename: "{app}\nssm.exe"; Parameters: "stop DC_ML"; Flags: runhidden
Filename: "{app}\nssm.exe"; Parameters: "remove DC_ML confirm"; Flags: runhidden
