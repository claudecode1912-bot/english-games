@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================
echo   Озвучка учебника «Читаю по-английски»
echo ============================================
echo.
set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY (
  python -c "import sys" >nul 2>nul && set "PY=python"
)
if not defined PY (
  echo Python не найден. Сейчас установлю его через winget...
  winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
  echo.
  echo Если установка прошла успешно, закройте это окно и снова дважды щёлкните make_audio.bat.
  echo Если winget не сработал, установите Python с сайта python.org ^(галочка "Add python.exe to PATH"^).
  pause
  exit /b
)
echo Устанавливаю edge-tts...
%PY% -m pip install --quiet --upgrade edge-tts
echo.
%PY% make_audio.py %*
echo.
pause
