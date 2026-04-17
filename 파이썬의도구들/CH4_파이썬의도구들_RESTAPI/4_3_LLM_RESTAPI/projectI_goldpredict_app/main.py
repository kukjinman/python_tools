from selenium_manager import get_gold_data
from gemini_manager import send_gemini_api

#0 gemini API 키 설정
gemini_api_key = "API 키"

#1 get_gold_data 함수를 호출
gold_predict_data = get_gold_data()

#7 send_gemini_api 함수를 호출
result = send_gemini_api(gemini_api_key, gold_predict_data, "\n 내일의 금값이 어떻게 될지 예측해 줘")

#10 결과 출력
print("금값 예측 결과:")
print(result)

