@echo off
chcp 65001 > nul 2>&1
setlocal enabledelayedexpansion
powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '   python_tools 환경 세팅을 시작합니다...' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
echo.

:: ─────────────────────────────────────────────
:: [Step 1] resource\python312 준비
:: 이미 압축 해제됨 → 바로 사용
:: tar.gz 있음 → 압축 해제
:: 둘 다 없음 → curl로 자동 다운로드 후 압축 해제
:: ─────────────────────────────────────────────

:: CPU 아키텍처 감지
set TAR_FILE=
set TAR_URL=
if /i "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    set TAR_FILE=resource\cpython-3.12-windows-amd64.tar.gz
    set TAR_URL=https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-x86_64-pc-windows-msvc-shared-install_only.tar.gz
)
if /i "%PROCESSOR_ARCHITECTURE%"=="x86" (
    if /i "%PROCESSOR_ARCHITEW6432%"=="AMD64" (
        set TAR_FILE=resource\cpython-3.12-windows-amd64.tar.gz
        set TAR_URL=https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-x86_64-pc-windows-msvc-shared-install_only.tar.gz
    ) else (
        set TAR_FILE=resource\cpython-3.12-windows-i686.tar.gz
        set TAR_URL=https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-i686-pc-windows-msvc-shared-install_only.tar.gz
    )
)

if exist "resource\python312\python.exe" (
    :: ctypes 정상 동작 여부 확인 (embeddable Python은 ctypes 불완전)
    resource\python312\python.exe -c "import ctypes" > nul 2>&1
    if !errorlevel! equ 0 (
        powershell -NoProfile -Command "Write-Host '[i] resource\python312 Python 3.12를 사용합니다.' -ForegroundColor Green"
        set PYTHON_CMD=resource\python312\python.exe
        goto CREATE_VENV
    ) else (
        powershell -NoProfile -Command "Write-Host '[!] 기존 Python이 불완전합니다. 재설치합니다...' -ForegroundColor Yellow"
        rmdir /s /q resource\python312
        if exist ".venv" rmdir /s /q .venv
        echo.
    )
)

:: tar.gz 없으면 curl로 자동 다운로드
if not exist "!TAR_FILE!" (
    powershell -NoProfile -Command "Write-Host '[1/4] Python 3.12 다운로드 중... (~100MB, 잠시 기다려 주세요)' -ForegroundColor Yellow"
    if not exist "resource" mkdir resource
    curl -L --progress-bar -o "!TAR_FILE!" "!TAR_URL!"
    if errorlevel 1 (
        powershell -NoProfile -Command "Write-Host '[오류] 다운로드에 실패했습니다. 인터넷 연결을 확인하거나' -ForegroundColor Red"
        powershell -NoProfile -Command "Write-Host '       resource\README.txt 를 참고하여 수동으로 파일을 넣어주세요.' -ForegroundColor Red"
        pause
        exit /b
    )
    powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
    echo.
)

powershell -NoProfile -Command "Write-Host '[1/4] Python 3.12 압축 해제 중...' -ForegroundColor Yellow"
if not exist "resource\python312" mkdir resource\python312
tar -xzf "!TAR_FILE!" -C "resource\python312" --strip-components=1
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[오류] 압축 해제에 실패했습니다. (Windows 10 이상 필요)' -ForegroundColor Red"
    pause
    exit /b
)
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

set PYTHON_CMD=resource\python312\python.exe

:CREATE_VENV
:: 기존 .venv가 있으면 삭제 후 재생성 (Python 버전 불일치 방지)
if exist ".venv" (
    powershell -NoProfile -Command "Write-Host '[i] 기존 .venv를 초기화합니다...' -ForegroundColor Yellow"
    rmdir /s /q .venv
)
powershell -NoProfile -Command "Write-Host '[2/4] pip 최신화 중...' -ForegroundColor Yellow"
%PYTHON_CMD% -m pip install --upgrade pip -q
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

powershell -NoProfile -Command "Write-Host '[3/4] 가상환경(.venv) 생성 중...' -ForegroundColor Yellow"
%PYTHON_CMD% -m pip install virtualenv -q
%PYTHON_CMD% -m virtualenv --python="%PYTHON_CMD%" .venv
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[오류] 가상환경 생성에 실패했습니다.' -ForegroundColor Red"
    pause
    exit /b
)
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

call .venv\Scripts\activate

powershell -NoProfile -Command "Write-Host '[4/4] 패키지 설치 중... (시간이 걸릴 수 있습니다)' -ForegroundColor Yellow"
.venv\Scripts\python.exe -m pip install --upgrade pip -q
.venv\Scripts\python.exe -m pip install -r requirement.txt --no-cache-dir
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[경고] 일부 패키지 설치에 실패했습니다.' -ForegroundColor Red"
)
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

powershell -NoProfile -Command "Write-Host '[+] googletrans 동기 호환 패치 적용 중...' -ForegroundColor Yellow"
for /f "delims=" %%i in ('.venv\Scripts\python.exe -c "import site; print(site.getsitepackages()[0])"') do set SITE_PACKAGES=%%i
(
echo try:
echo     import asyncio
echo     import googletrans as _gt
echo     _Orig = _gt.Translator
echo     class _SyncTranslator:
echo         def translate^(self, text, dest='en', src='auto', **kwargs^):
echo             async def _run^(^):
echo                 t = _Orig^(^)
echo                 result = await t.translate^(text, dest=dest, src=src^)
echo                 await t.client.aclose^(^)
echo                 return result
echo             return asyncio.run^(_run^(^)^)
echo         def detect^(self, text, **kwargs^):
echo             async def _run^(^):
echo                 t = _Orig^(^)
echo                 result = await t.detect^(text^)
echo                 await t.client.aclose^(^)
echo                 return result
echo             return asyncio.run^(_run^(^)^)
echo     _gt.Translator = _SyncTranslator
echo except Exception:
echo     pass
) > "%SITE_PACKAGES%\sitecustomize.py"
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '   세팅이 완료되었습니다!' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
echo.
powershell -NoProfile -Command "Write-Host '[PyCharm 인터프리터 설정 방법]' -ForegroundColor Green"
powershell -NoProfile -Command "Write-Host '  1. PyCharm 우측 하단 인터프리터 클릭'"
powershell -NoProfile -Command "Write-Host '  2. Add New Interpreter - Add Local Interpreter'"
powershell -NoProfile -Command "Write-Host '  3. Existing 선택 후 아래 경로 입력:'"
powershell -NoProfile -Command "Write-Host ('     ' + [System.IO.Path]::Combine((Get-Location).Path, '.venv\Scripts\python.exe')) -ForegroundColor Yellow"
echo.
powershell -NoProfile -Command "Write-Host '앞으로 코드 실행 전, 아래 명령어로 가상환경을 활성화하세요:'"
powershell -NoProfile -Command "Write-Host '  .venv\Scripts\activate' -ForegroundColor Yellow"
echo.
pause
