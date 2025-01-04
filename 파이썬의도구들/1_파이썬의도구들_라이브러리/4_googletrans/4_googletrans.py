#1 googletrans 패키지의 Translator 모듈 가져오기
from googletrans import Translator

#2 Translator 객체 생성
translator = Translator()

#3 번역할 텍스트
text1 = "Hello, how are you?"  # 영어
text2 = "你好，你怎么样？"  # 중국어
text3 = "こんにちは、お元気ですか？"  # 일본어

#4 텍스트 번역 (한국어로)
translated1 = translator.translate(text1, dest='ko')
translated2 = translator.translate(text2, dest='ko')
translated3 = translator.translate(text3, dest='ko')

#5 텍스트 언어 감지
detected1 = translator.detect(text1)
detected2 = translator.detect(text2)
detected3 = translator.detect(text3)

#6 결과 출력
print(f"Original (English): {text1}")
print(f"Translated (Korean): {translated1.text}")
print(f"Detected Language: {detected1.lang}")
print()
print(f"Original (Chinese): {text2}")
print(f"Translated (Korean): {translated2.text}")
print(f"Detected Language: {detected2.lang}")
print()
print(f"Original (Japanese): {text3}")
print(f"Translated (Korean): {translated3.text}")
print(f"Detected Language: {detected3.lang}")
