#!/bin/bash

# ANSI 색상 코드
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 스크립트 위치 기준으로 실행
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=============================================="
echo "    python_tools 환경 세팅을 시작합니다...    "
echo "=============================================="
echo ""

PYTHON_CMD=""

# ─────────────────────────────────────────────
# [Step 1] resource/python312 준비
# 이미 압축 해제됨 → 바로 사용
# tar.gz 있음 → 압축 해제
# 둘 다 없음 → curl로 자동 다운로드 후 압축 해제
# ─────────────────────────────────────────────
ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    TARFILE="resource/cpython-3.12-aarch64-apple-darwin.tar.gz"
    TARURL="https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-aarch64-apple-darwin-install_only.tar.gz"
    ARCH_DESC="Apple Silicon (M1/M2/M3)"
else
    TARFILE="resource/cpython-3.12-x86_64-apple-darwin.tar.gz"
    TARURL="https://github.com/indygreg/python-build-standalone/releases/download/20231002/cpython-3.12.0+20231002-x86_64-apple-darwin-install_only.tar.gz"
    ARCH_DESC="Intel"
fi

if [ -f "resource/python312/bin/python3" ]; then
    echo -e "${GREEN}[✓] resource/python312 Python 3.12 사용합니다. ($ARCH_DESC)${NC}"
    PYTHON_CMD="resource/python312/bin/python3"
else
    # tar.gz 없으면 curl로 다운로드
    if [ ! -f "$TARFILE" ]; then
        echo -e "${YELLOW}[1/4] Python 3.12 다운로드 중 ($ARCH_DESC)...${NC}"
        mkdir -p resource
        curl -L --progress-bar -o "$TARFILE" "$TARURL"
        if [ $? -ne 0 ]; then
            echo -e "${RED}[오류] 다운로드에 실패했습니다. 인터넷 연결을 확인하거나${NC}"
            echo "       resource/README.txt 를 참고하여 수동으로 파일을 넣어주세요."
            exit 1
        fi
        echo -e "${GREEN}완료!${NC}"
        echo ""
    fi

    echo -e "${YELLOW}[1/4] Python 3.12 압축 해제 중 ($ARCH_DESC)...${NC}"
    mkdir -p resource/python312
    tar -xzf "$TARFILE" -C resource/python312 --strip-components=1
    if [ $? -ne 0 ]; then
        echo -e "${RED}[오류] 압축 해제에 실패했습니다.${NC}"
        exit 1
    fi
    echo -e "${GREEN}완료!${NC}"
    echo ""
    PYTHON_CMD="resource/python312/bin/python3"
fi


# ─────────────────────────────────────────────
# [Step 2] 가상환경(.venv) 생성
# ─────────────────────────────────────────────
echo -e "${GREEN}[2/4] 가상환경(.venv) 생성 중...${NC}"

# standalone Python은 venv 미포함 → virtualenv 사용
if [[ "$PYTHON_CMD" == resource/* ]]; then
    "$PYTHON_CMD" -m pip install virtualenv -q
    "$PYTHON_CMD" -m virtualenv .venv
else
    "$PYTHON_CMD" -m venv .venv
fi

if [ $? -ne 0 ]; then
    echo -e "${RED}[오류] 가상환경 생성에 실패했습니다.${NC}"
    exit 1
fi
echo -e "${GREEN}완료!${NC}"
echo ""

# ─────────────────────────────────────────────
# [Step 3] 가상환경 활성화
# ─────────────────────────────────────────────
echo -e "${GREEN}[3/4] 가상환경 활성화 중...${NC}"
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}[오류] 가상환경 활성화에 실패했습니다.${NC}"
    exit 1
fi
echo -e "${GREEN}완료!${NC}"
echo ""

# ─────────────────────────────────────────────
# [Step 4] 패키지 설치
# ─────────────────────────────────────────────
echo -e "${GREEN}[4/4] 패키지 설치 중... (시간이 걸릴 수 있습니다)${NC}"
python -m pip install --upgrade pip -q
python -m pip install -r requirement.txt --no-cache-dir
if [ $? -ne 0 ]; then
    echo -e "${RED}[경고] 일부 패키지 설치에 실패했습니다.${NC}"
fi
echo -e "${GREEN}완료!${NC}"
echo ""

# ─────────────────────────────────────────────
# googletrans 4.x async → sync 호환 패치
# ─────────────────────────────────────────────
echo -e "${GREEN}[+] googletrans 동기 호환 패치 적용 중...${NC}"
SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")
cat > "$SITE_PACKAGES/sitecustomize.py" << 'PATCH'
try:
    import asyncio
    import googletrans as _gt
    _Orig = _gt.Translator

    class _SyncTranslator:
        def translate(self, text, dest='en', src='auto', **kwargs):
            async def _run():
                t = _Orig()
                result = await t.translate(text, dest=dest, src=src)
                await t.client.aclose()
                return result
            return asyncio.run(_run())

        def detect(self, text, **kwargs):
            async def _run():
                t = _Orig()
                result = await t.detect(text)
                await t.client.aclose()
                return result
            return asyncio.run(_run())

    _gt.Translator = _SyncTranslator
except Exception:
    pass
PATCH
echo -e "${GREEN}완료!${NC}"
echo ""

echo "=============================================="
echo "    세팅이 완료되었습니다!                   "
echo "=============================================="
echo ""
echo -e "${GREEN}[PyCharm 인터프리터 설정 방법]${NC}"
echo "  1. PyCharm 우측 하단 인터프리터 클릭"
echo "  2. Add New Interpreter - Add Local Interpreter"
echo "  3. Existing 선택 후 아래 경로 입력:"
echo -e "     ${YELLOW}$SCRIPT_DIR/.venv/bin/python3${NC}"
echo ""
echo "앞으로 코드 실행 전, 아래 명령어로 가상환경을 활성화하세요:"
echo -e "${YELLOW}source .venv/bin/activate${NC}"
echo ""
echo "가상환경에서 나가려면:"
echo -e "${YELLOW}deactivate${NC}"

