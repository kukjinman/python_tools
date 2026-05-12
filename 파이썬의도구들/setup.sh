#!/bin/bash

# ANSI 색상 코드
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=============================================="
echo "    python_tools 환경 세팅을 시작합니다...    "
echo "=============================================="
echo ""

# Python 3.12 설치 여부 확인
if ! command -v python3.12 &> /dev/null; then
    echo -e "${YELLOW}[!] Python 3.12가 설치되어 있지 않습니다.${NC}"
    echo ""

    # Homebrew 설치 여부 확인
    if ! command -v brew &> /dev/null; then
        echo -e "${RED}[오류] Homebrew가 설치되어 있지 않습니다.${NC}"
        echo "아래 명령어로 Homebrew를 먼저 설치해 주세요:"
        echo "/bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        echo ""
        read -p "Homebrew 설치 후 이 스크립트를 다시 실행해 주세요. (Enter 키를 눌러주세요)"
        exit 1
    fi

    echo "    Homebrew로 Python 3.12를 설치합니다..."
    brew install python@3.12

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}    Python 3.12 설치 완료!${NC}"
    else
        echo -e "${RED}    [오류] Python 3.12 설치에 실패했습니다.${NC}"
        exit 1
    fi
    echo ""
else
    PYTHON_VERSION=$(python3.12 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}[✓] Python ${PYTHON_VERSION}이(가) 설치되어 있습니다.${NC}"
    echo ""
fi

# 가상환경 생성
echo -e "${GREEN}[1/3] 가상환경(.venv) 생성 중...${NC}"
python3.12 -m venv .venv
if [ $? -eq 0 ]; then
    echo -e "${GREEN}완료!${NC}"
else
    echo -e "${RED}[오류] 가상환경 생성에 실패했습니다.${NC}"
    exit 1
fi
echo ""

# 가상환경 활성화
echo -e "${GREEN}[2/3] 가상환경 활성화 중...${NC}"
source .venv/bin/activate
if [ $? -eq 0 ]; then
    echo -e "${GREEN}완료!${NC}"
else
    echo -e "${RED}[오류] 가상환경 활성화에 실패했습니다.${NC}"
    exit 1
fi
echo ""

# 패키지 설치
echo -e "${GREEN}[3/3] 패키지 설치 중... (시간이 걸릴 수 있습니다)${NC}"
python -m pip install --upgrade pip
pip install -r requirement.txt --no-cache-dir
if [ $? -eq 0 ]; then
    echo -e "${GREEN}완료!${NC}"
else
    echo -e "${RED}[경고] 일부 패키지 설치에 실패했습니다.${NC}"
fi
echo ""

echo "=============================================="
echo "    세팅이 완료되었습니다!                   "
echo "=============================================="
echo ""
echo "앞으로 코드 실행 전, 아래 명령어로 가상환경을 활성화하세요:"
echo -e "${YELLOW}source .venv/bin/activate${NC}"
echo ""
echo "가상환경에서 나가려면:"
echo -e "${YELLOW}deactivate${NC}"

