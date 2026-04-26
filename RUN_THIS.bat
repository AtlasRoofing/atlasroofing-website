@echo off
REM ============================================================
REM Atlas Roofing — BBB Seal Patch Runner
REM ============================================================
REM Just double-click this file.
REM It must be in the same folder as your repo's index.html.
REM ============================================================

cd /d "%~dp0"
echo.
echo Running BBB seal patch...
echo.
python apply_bbb_seal.py
if errorlevel 1 (
    echo.
    echo Python didn't run. Trying 'py' launcher instead...
    py apply_bbb_seal.py
)
echo.
echo ============================================================
echo Done. Check the message above to see what was changed.
echo Now open GitHub Desktop, commit, and push.
echo ============================================================
echo.
pause
