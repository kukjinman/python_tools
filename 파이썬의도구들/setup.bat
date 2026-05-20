@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo =============================================
echo    python_tools 환경 세팅을 시작합니다...
echo =============================================
echo.

REM -----------------------------------------------
REM STEP 1. Python 3.12 설치 확인
REM -----------------------------------------------
py -3.12 --version > nul 2>&1
if errorlevel 1 (
    echo [오류] Python 3.12가 설치되어 있지 않습니다.
    echo        https://www.python.org 에서 Python 3.12 설치 후 다시 실행해 주세요.
    pause
    exit /b 1
)
echo [OK] Python 3.12 확인 완료
echo.

REM -----------------------------------------------
REM STEP 2. 가상환경 생성
REM -----------------------------------------------
if exist .venv (
    echo [i] 기존 .venv 삭제 중...
    rmdir /s /q .venv
)

echo [1/3] 가상환경(.venv) 생성 중...
py -3.12 -m venv .venv
if errorlevel 1 (
    echo [오류] 가상환경 생성 실패.
    pause
    exit /b 1
)
echo [OK] 가상환경 생성 완료
echo.

REM -----------------------------------------------
REM STEP 3. 패키지 설치
REM -----------------------------------------------
echo [2/3] pip 업그레이드 중...
.venv\Scripts\python.exe -m pip install --upgrade pip --quiet
echo.

echo [3/3] 패키지 설치 중... (시간이 걸릴 수 있습니다)
.venv\Scripts\python.exe -m pip install -r requirement.txt
if errorlevel 1 (
    echo [경고] 일부 패키지 설치 실패. 위 오류 메시지를 확인하세요.
) else (
    echo [OK] 패키지 설치 완료
)
echo.

REM -----------------------------------------------
REM STEP 4. googletrans 동기 호환 패치
REM   .venv\Lib\site-packages\sitecustomize.py 생성
REM -----------------------------------------------
echo [+] googletrans 동기 호환 패치 적용 중...

.venv\Scripts\python.exe -c ^
"import site; path = site.getsitepackages()[1] + '\\sitecustomize.py'; open(path,'w',encoding='utf-8').write('try:\n    import asyncio\n    import googletrans as _gt\n    _Orig = _gt.Translator\n    class _Sync:\n        def translate(self, text, dest=\"en\", src=\"auto\", **kw):\n            async def _r():\n                t = _Orig()\n                r = await t.translate(text, dest=dest, src=src)\n                await t.client.aclose()\n                return r\n            return asyncio.run(_r())\n        def detect(self, text, **kw):\n            async def _r():\n                t = _Orig()\n                r = await t.detect(text)\n                await t.client.aclose()\n                return r\n            return asyncio.run(_r())\n    _gt.Translator = _Sync\nexcept Exception:\n    pass\n'); print('[OK] 패치 적용 위치:', path)"

if errorlevel 1 (
    echo [경고] googletrans 패치 적용 실패.
)
echo.

REM -----------------------------------------------
REM 완료
REM -----------------------------------------------
echo =============================================
echo    세팅 완료!
echo =============================================
echo.
echo  [PyCharm 인터프리터 경로]
echo  %CD%\.venv\Scripts\python.exe
echo.
echo  [가상환경 활성화]
echo  .venv\Scripts\activate
echo.
pause

