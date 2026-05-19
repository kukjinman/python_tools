[ Python 3.12 설치 파일 안내 ]

이 폴더에 Python 3.12 설치 파일을 아래 이름으로 넣어주세요:

  python312_installer.exe

다운로드 주소:
  https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe

파일을 이 폴더에 넣은 뒤 setup.bat를 실행하면
인터넷 연결 없이도 Python 3.12 설치가 가능합니다.


[ resource 폴더 안내 ]

이 폴더에 아래 파일 2개를 넣어주세요.
setup.bat 실행 시 자동으로 Python 환경을 구성합니다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[파일 1] Python 3.12 Embeddable 패키지
  파일명 : python-3.12.0-embed-amd64.zip
  다운로드: https://www.python.org/ftp/python/3.12.0/python-3.12.0-embed-amd64.zip
  크기   : 약 11MB
  설명   : 설치 불필요한 경량 Python 실행 환경

[파일 2] pip 설치 스크립트
  파일명 : get-pip.py
  다운로드: https://bootstrap.pypa.io/get-pip.py
  크기   : 약 2MB
  설명   : Python 패키지 관리자 pip 설치용 스크립트

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

준비 완료 후 폴더 구조:
  resource/
  ├── python-3.12.0-embed-amd64.zip
  ├── get-pip.py
  └── README.txt  ← 현재 파일

setup.bat 실행 순서:
  1. zip 압축 해제 → resource/python312/ 생성
  2. pip 설치
  3. virtualenv로 .venv 생성
  4. requirement.txt 패키지 설치

※ Python을 시스템에 설치하지 않아도 동작합니다.
