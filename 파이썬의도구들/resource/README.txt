[ resource 폴더 안내 ]
setup.bat / setup.sh 실행 시 이 폴더의 파일을 자동으로 사용합니다.
파일이 없으면 인터넷에서 자동 다운로드합니다.
오프라인 환경이라면 아래 파일을 미리 넣어주세요.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
★ Windows 사용자 (setup.bat)   ※ Windows 10 이상 필요
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
※ 내 PC가 몇 비트인지 모른다면?
   윈도우 키 → "시스템 정보" 검색 → [시스템 종류] 항목 확인
[64비트 Windows] ← 대부분의 최신 PC
  파일명 : cpython-3.12-windows-amd64.tar.gz
  다운로드: https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-x86_64-pc-windows-msvc-shared-install_only.tar.gz
  크기   : 약 100MB
[32비트 Windows] ← 오래된 PC
  파일명 : cpython-3.12-windows-i686.tar.gz
  다운로드: https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-i686-pc-windows-msvc-shared-install_only.tar.gz
  크기   : 약 90MB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
★ Mac 사용자 (setup.sh)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
※ Mac은 Homebrew가 있으면 파일 없이도 자동 설치됩니다.
[Apple Silicon (M1/M2/M3)]
  파일명 : cpython-3.12-aarch64-apple-darwin.tar.gz
  다운로드: https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-aarch64-apple-darwin-install_only.tar.gz
  크기   : 약 60MB
[Intel Mac]
  파일명 : cpython-3.12-x86_64-apple-darwin.tar.gz
  다운로드: https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-x86_64-apple-darwin-install_only.tar.gz
  크기   : 약 60MB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
준비 완료 후 폴더 구조 예시 (Windows 64비트):
  resource/
  ├── cpython-3.12-windows-amd64.tar.gz
  └── README.txt
