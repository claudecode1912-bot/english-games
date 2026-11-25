@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================
echo   Озвучка игр тем же голосом, что и учебник
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
  echo Если установка прошла успешно, закройте это окно и снова дважды щёлкните make_games_audio.bat.
  echo Если winget не сработал, установите Python с сайта python.org ^(галочка "Add python.exe to PATH"^).
  pause
  exit /b
)
echo Устанавливаю edge-tts...
%PY% -m pip install --quiet --upgrade edge-tts
echo.
%PY% make_games_audio.py %*
echo.
echo Упаковываю файлы для GitHub...
powershell -NoProfile -Command "Compress-Archive -Force -Path 'games-audio\*' -DestinationPath 'games-audio.zip'; Compress-Archive -Force -Path '..\chitayu-site\audio\*' -DestinationPath 'chitayu-audio.zip'"
echo Архивы games-audio.zip и chitayu-audio.zip готовы.
echo.
pause
