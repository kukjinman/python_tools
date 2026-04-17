#1 google의 genai 패키지 불러오기
from google import genai

#2 Gemini API 키 설정
api_key = "API 키"

#3 genai.Client 객체 생성
client = genai.Client(api_key=api_key)

#4 generate_content 메서드를 사용하여 LLM에 요청
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="LLM에 대해서 간략하게 1문장으로 설명해 줘"
)

#5 응답 결과 출력
print("출력 결과")
print(response.text)
