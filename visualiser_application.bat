@echo off
rem ---------------------------------------------------------------------------
rem  Visualiser le support PRC02 en mode developpement.
rem
rem  Double-cliquez sur ce fichier depuis l'Explorateur Windows : il met a jour
rem  les paquets Dart (flutter pub get) puis lance l'application
rem  (flutter run -d windows). Rien n'est modifie en dehors de ce projet.
rem
rem  Pourquoi le "pub get" a chaque lancement : les paquets telecharges depuis
rem  les outils de Claude restent dans le stockage prive de l'application
rem  Claude et sont invisibles ici. Ce "pub get" les recupere dans le cache
rem  normal de Windows ; il est quasi instantane quand rien ne manque.
rem ---------------------------------------------------------------------------
setlocal
chcp 65001 >nul
title Support PRC02 - Design ^& visualisation temps réel avec Blender
cd /d "%~dp0"

rem Flutter : chemin complet de flutter.bat (celui du PATH, sinon l'installation
rem de ce poste). Le chemin complet est indispensable : appele par son seul nom
rem depuis un .bat, flutter.bat se trompe sur son propre dossier.
set "FLUTTER="
for /f "delims=" %%F in ('where flutter.bat 2^>nul') do if not defined FLUTTER set "FLUTTER=%%F"
if not defined FLUTTER if exist "%USERPROFILE%\develop\flutter\bin\flutter.bat" set "FLUTTER=%USERPROFILE%\develop\flutter\bin\flutter.bat"
if not defined FLUTTER (
  echo Flutter est introuvable : installez-le ou ajoutez son dossier bin au PATH.
  pause
  exit /b 1
)

rem Chaque commande Flutter tourne dans un cmd enfant : si flutter.bat s'arrete
rem sur une erreur, cette fenetre reste ouverte et affiche le message.
echo.
echo [1/2] Mise à jour des paquets : flutter pub get
echo.
cmd /c ""%FLUTTER%" pub get"
if errorlevel 1 (
  echo.
  echo La mise à jour des paquets a échoué. Vérifiez la connexion Internet puis relancez ce fichier.
  pause
  exit /b 1
)

echo.
echo [2/2] Lancement de l'application : flutter run -d windows
echo       Dans cette fenêtre : r = recharger le code, R = redémarrer, q = quitter.
echo.
cmd /c ""%FLUTTER%" run -d windows"

echo.
echo Application fermée.
pause
endlocal
