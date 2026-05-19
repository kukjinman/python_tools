@echo off
chcp 65001 > nul 2>&1
setlocal enabledelayedexpansion
powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '   python_tools 환경 세팅을 시작합니다...' -ForegroundColor Cyan"
powershell -NoProfile -Command "Write-Host '=============================================' -ForegroundColor Cyan"
echo.

:: CPU 아키텍처 감지
set ZIP_FILE=
set ZIP_URL=
if /i "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    set ZIP_FILE=resource\python-3.12.0-embed-amd64.zip
    set ZIP_URL=https://www.python.org/ftp/python/3.12.0/python-3.12.0-embed-amd64.zip
)
if /i "%PROCESSOR_ARCHITECTURE%"=="x86" (
    if /i "%PROCESSOR_ARCHITEW6432%"=="AMD64" (
        set ZIP_FILE=resource\python-3.12.0-embed-amd64.zip
        set ZIP_URL=https://www.python.org/ftp/python/3.12.0/python-3.12.0-embed-amd64.zip
    ) else (
        set ZIP_FILE=resource\python-3.12.0-embed-win32.zip
        set ZIP_URL=https://www.python.org/ftp/python/3.12.0/python-3.12.0-embed-win32.zip
    )
)

if exist "resource\python312\python.exe" (
    powershell -NoProfile -Command "Write-Host '[i] resource\python312 Python 3.12를 사용합니다.' -ForegroundColor Green"
    set PYTHON_CMD=resource\python312\python.exe
    goto CREATE_VENV
)

:: zip 없으면 curl로 자동 다운로드
if not exist "!ZIP_FILE!" (
    powershell -NoProfile -Command "Write-Host '[1/4] Python 3.12 다운로드 중...' -ForegroundColor Yellow"
    if not exist "resource" mkdir resource
    curl -L --progress-bar -o "!ZIP_FILE!" "!ZIP_URL!"
    if errorlevel 1 (
        powershell -NoProfile -Command "Write-Host '[오류] 다운로드에 실패했습니다. 인터넷 연결을 확인하거나' -ForegroundColor Red"
        powershell -NoProfile -Command "Write-Host '       resource\README.txt 를 참고하여 수동으로 파일을 넣어주세요.' -ForegroundColor Red"
        pause
        exit /b
    )
    powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
    echo.
)

:: get-pip.py 없으면 curl로 자동 다운로드
if not exist "resource\get-pip.py" (
    powershell -NoProfile -Command "Write-Host '[1/4] get-pip.py 다운로드 중...' -ForegroundColor Yellow"
    curl -L --progress-bar -o "resource\get-pip.py" "https://bootstrap.pypa.io/get-pip.py"
    if errorlevel 1 (
        powershell -NoProfile -Command "Write-Host '[오류] get-pip.py 다운로드에 실패했습니다.' -ForegroundColor Red"
        pause
        exit /b
    )
    powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
    echo.
)

powershell -NoProfile -Command "Write-Host '[1/4] Python 3.12 압축 해제 중...' -ForegroundColor Yellow"
powershell -NoProfile -Command "Expand-Archive -Path '!ZIP_FILE!' -DestinationPath 'resource\python312' -Force"
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[오류] 압축 해제에 실패했습니다.' -ForegroundColor Red"
    pause
    exit /b
)
powershell -NoProfile -Command "Get-ChildItem 'resource\python312\*._pth' | ForEach-Object { (Get-Content $_.FullName) -replace '#import site','import site' | Set-Content $_.FullName }"
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

powershell -NoProfile -Command "Write-Host '[2/4] pip 설치 중...' -ForegroundColor Yellow"
resource\python312\python.exe resource\get-pip.py --no-warn-script-location -q
if errorlevel 1 (
    powershell -NoProfile -Command "Write-Host '[오류] pip 설치에 실패했습니다.' -ForegroundColor Red"
    pause
    exit /b
)
powershell -NoProfile -Command "Write-Host '완료!' -ForegroundColor Green"
echo.

set PYTHON_CMD=resource\python312\python.exe

:CREATE_VENV
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
