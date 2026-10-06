@echo off
cd /d "%~dp0"
if not exist "index.html" (
  echo No se encontro index.html. Extraiga primero el ZIP completo.
  pause
  exit /b 1
)
start "" "%~dp0index.html"
