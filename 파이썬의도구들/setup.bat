@echo off
chcp 65001 > nul 2>&1
setlocal enabledelayedexpansion
echo =============================================
echo    python_tools 환경 세팅을 시작합니다...
echo =============================================
echo.

:: ─────────────────────────────────────────────
:: [Step 1] resource\python312 준비
:: 이미 압축 해제됨 → 바로 사용
:: zip 있음 → 압축 해제
:: 둘 다 없음 → curl로 자동 다운로드 후 압축 해제
:: ─────────────────────────────────────────────

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
    echo [i] resource\python312 Python 3.12를 사용합니다.
    set PYTHON_CMD=resource\python312\python.exe
    goto CREATE_VENV
)

:: zip 없으면 curl로 자동 다운로드
if not exist "!ZIP_FILE!" (
    echo [1/4] Python 3.12 다운로드 중...
    if not exist "resource" mkdir resource
    curl -L --progress-bar -o "!ZIP_FILE!" "!ZIP_URL!"
    if errorlevel 1 (
        echo [오류] 다운로드에 실패했습니다. 인터넷 연결을 확인하거나
        echo        resource\README.txt 를 참고하여 수동으로 파일을 넣어주세요.
        pause
        exit /b
    )
    echo 완료!
    echo.
)

:: get-pip.py 없으면 curl로 자동 다운로드
if not exist "resource\get-pip.py" (
    echo [1/4] get-pip.py 다운로드 중...
    curl -L --progress-bar -o "resource\get-pip.py" "https://bootstrap.pypa.io/get-pip.py"
    if errorlevel 1 (
        echo [오류] get-pip.py 다운로드에 실패했습니다.
        pause
        exit /b
    )
    echo 완료!
    echo.
)

echo [1/4] Python 3.12 압축 해제 중...
powershell -NoProfile -Command "Expand-Archive -Path '!ZIP_FILE!' -DestinationPath 'resource\python312' -Force"
if errorlevel 1 (
    echo [오류] 압축 해제에 실패했습니다.
    pause
    exit /b
)
powershell -NoProfile -Command "Get-ChildItem 'resource\python312\*._pth' | ForEach-Object { (Get-Content $_.FullName) -replace '#import site','import site' | Set-Content $_.FullName }"
echo 완료!
echo.

echo [2/4] pip 설치 중...
resource\python312\python.exe resource\get-pip.py --no-warn-script-location -q
if errorlevel 1 (
    echo [오류] pip 설치에 실패했습니다.
    pause
    exit /b
)
echo 완료!
echo.

set PYTHON_CMD=resource\python312\python.exe

:CREATE_VENV
:: ─────────────────────────────────────────────
:: [Step 3] virtualenv로 .venv 생성
:: ─────────────────────────────────────────────
echo [3/4] 가상환경(.venv) 생성 중...
%PYTHON_CMD% -m pip install virtualenv -q
%PYTHON_CMD% -m virtualenv .venv
if errorlevel 1 (
    echo [오류] 가상환경 생성에 실패했습니다.
    pause
    exit /b
)
echo 완료!
echo.

:: 가상환경 활성화
call .venv\Scripts\activate

:: ─────────────────────────────────────────────
:: [Step 4] 패키지 설치
:: ─────────────────────────────────────────────
echo [4/4] 패키지 설치 중... (시간이 걸릴 수 있습니다)
python -m pip install --upgrade pip -q
python -m pip install -r requirement.txt --no-cache-dir
if errorlevel 1 (
    echo [경고] 일부 패키지 설치에 실패했습니다.
)
echo 완료!
echo.

:: ─────────────────────────────────────────────
:: googletrans 4.x async → sync 호환 패치
:: ─────────────────────────────────────────────
echo [+] googletrans 동기 호환 패치 적용 중...
for /f "delims=" %%i in ('python -c "import site; print(site.getsitepackages()[0])"') do set SITE_PACKAGES=%%i
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
echo 완료!
echo.

echo =============================================
echo    세팅이 완료되었습니다!
echo =============================================
echo.
echo [PyCharm 인터프리터 설정 방법]
echo   1. PyCharm 우측 하단 인터프리터 클릭
echo   2. Add New Interpreter - Add Local Interpreter
echo   3. Existing 선택 후 아래 경로 입력:
echo      %CD%\.venv\Scripts\python.exe
echo.
echo 앞으로 코드 실행 전, 아래 명령어로 가상환경을 활성화하세요:
echo   .venv\Scripts\activate
echo.
pause
