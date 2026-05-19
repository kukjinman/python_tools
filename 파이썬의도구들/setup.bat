@echo off
chcp 65001 > nul 2>&1
setlocal enabledelayedexpansion
powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '   python_tools 환경 세팅을 시작합니다...' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
echo.

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

:: [Step 1] resource\python312 준비
if exist "resource\python312\python.exe" (
    resource\python312\python.exe -c "import ctypes; ctypes.windll.kernel32.GetCurrentProcessId()" > nul 2>&1
    if !errorlevel! equ 0 (
        powershell -NoProfile -Command "Write-Host '[OK] resource\python312 Python 3.12를 사용합니다.' -ForegroundColor Green"
        set PYTHON_CMD=resource\python312\python.exe
        goto CREATE_VENV
    ) else (
        powershell -NoProfile -Command "Write-Host '[!] 기존 Python이 불완전합니다. 재설치합니다...' -ForegroundColor Yellow"
        rmdir /s /q resource\python312
        if exist ".venv" rmdir /s /q .venv
        echo.
    )
)

:: tar.gz 없으면 curl 자동 다운로드
if not exist "!TAR_FILE!" (
    powershell -NoProfile -Command "Write-Host '[1/3] Python 3.12 다운로드 중... (~100MB)' -ForegroundColor Yellow"
    if not exist "resource" mkdir resource
    curl -L --progress-bar -o "!TAR_FILE!" "!TAR_URL!"
    if errorlevel 1 (
        powershell -NoProfile -Command "Write-Host '[오류] 다운로드 실패. 인터넷 연결 확인 또는 resource\README.txt 참고.' -ForegroundColor Red"
        pause
        exit /b
    )
    powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
    echo.
)

powershell -NoProfile -Command "Write-Host '[1/3] Python 3.12 압축 해제 중...' -ForegroundColor Yellow"
if not exist "resource\python312" mkdir resource\python312
tar -xzf "!TAR_FILE!" -C "resource\python312" --strip-components=1
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[오류] 압축 해제 실패. (Windows 10 이상 필요)' -ForegroundColor Red"
    pause
    exit /b
)
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

set PYTHON_CMD=resource\python312\python.exe

:CREATE_VENV
:: 기존 .venv 초기화
if exist ".venv" (
    powershell -NoProfile -Command "Write-Host '[i] 기존 .venv를 초기화합니다...' -ForegroundColor Yellow"
    rmdir /s /q .venv
)

:: [Step 2] virtualenv로 .venv 생성
powershell -NoProfile -Command "Write-Host '[2/3] 가상환경(.venv) 생성 중...' -ForegroundColor Yellow"
%PYTHON_CMD% -m pip install virtualenv -q
%PYTHON_CMD% -m virtualenv --python="%PYTHON_CMD%" .venv
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[오류] 가상환경 생성에 실패했습니다.' -ForegroundColor Red"
    pause
    exit /b
)
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

:: [Step 3] 패키지 설치
powershell -NoProfile -Command "Write-Host '[3/3] 패키지 설치 중... (시간이 걸릴 수 있습니다)' -ForegroundColor Yellow"
.venv\Scripts\python.exe -m pip install --upgrade pip -q
.venv\Scripts\python.exe -m pip install -r requirement.txt --no-cache-dir
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[경고] 일부 패키지 설치에 실패했습니다.' -ForegroundColor Red"
)
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

:: googletrans 동기 호환 패치
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
