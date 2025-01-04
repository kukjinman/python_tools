#1 googletrans 패키지에서 지원 언어 list를 제공할 LANGUAGES 가져오기
from googletrans import LANGUAGES

#2 지원되는 언어 목록 출력
print("Supported languages:")
for lang_code, lang_name in LANGUAGES.items():
    print(f"{lang_code}: {lang_name}")
