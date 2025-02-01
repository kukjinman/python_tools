#1 googletrans 모듈 가져오기
from googletrans import Translator

#2 번역 기능의 함수입니다.
def translate_contents(text, dest='ko'):
    translator = Translator()
    translated = translator.translate(text, dest=dest)
    return translated.text
