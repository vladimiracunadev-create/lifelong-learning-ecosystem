@echo off
cd /d "%~dp0"
where uv >nul 2>nul
if not errorlevel 1 (
  uv run --offline python scripts/validate.py
  goto finish
)
where py >nul 2>nul
if not errorlevel 1 (
  py -3 scripts/validate.py
  goto finish
)
python scripts/validate.py
:finish
set "LLE_RESULT=%errorlevel%"
echo.
if "%LLE_RESULT%"=="0" (echo Comprobacion finalizada.) else (echo Revise los mensajes anteriores.)
pause
exit /b %LLE_RESULT%
