from google import genai

#7 send_gemini_api 함수 정의
def send_gemini_api(api_key, data):

    #8 prompt 변수에 요청할 내용을 작성
    prompt = data + "\n 내일의 금값이 어떻게 될지 예측해 줘"

    client = genai.Client(api_key=api_key)
    #9 generate_content 메서드를 사용하여 LLM에 요청
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )

    return response.text
