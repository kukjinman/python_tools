@echo off
chcp 65001 > nul
echo =============================================
echo    python_tools 환경 세팅을 시작합니다...
echo =============================================
echo.

:: Python 3.12 설치 여부 확인
py -3.12 --version > nul 2>&1
if errorlevel 1 (
    echo [!] Python 3.12가 설치되어 있지 않습니다.
    echo     Python 3.12를 자동으로 다운로드 및 설치합니다...
    echo.
    :: Python 3.12 설치 파일 다운로드
    curl -o python312_installer.exe https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
    if errorlevel 1 (
        echo [오류] 다운로드에 실패했습니다. 인터넷 연결을 확인해 주세요.
        pause
        exit /b
    )
    echo     설치 중... (잠시 기다려 주세요)
    python312_installer.exe /quiet InstallAllUsers=0 PrependPath=1 Include_launcher=1
    del python312_installer.exe
    echo     Python 3.12 설치 완료!
    echo.
    :: PATH 갱신을 위해 새 환경변수 로드
    call refreshenv > nul 2>&1
)

:: 가상환경 생성
echo [1/3] 가상환경(.venv) 생성 중...
py -3.12 -m venv .venv
echo 완료!
echo.

:: 가상환경 활성화
echo [2/3] 가상환경 활성화 중...
call .venv\Scripts\activate
echo 완료!
echo.

:: 패키지 설치
echo [3/3] 패키지 설치 중... (시간이 걸릴 수 있습니다)
py -m pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir --force-reinstall --no-deps
echo 완료!
echo.

echo =============================================
echo    세팅이 완료되었습니다!
echo =============================================
echo.
echo 앞으로 코드 실행 전, 아래 명령어로 가상환경을 활성화하세요:
echo   .venv\Scripts\activate
echo.
pause
