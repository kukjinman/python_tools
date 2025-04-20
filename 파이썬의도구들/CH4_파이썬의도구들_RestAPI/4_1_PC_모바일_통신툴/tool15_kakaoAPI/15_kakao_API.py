import requests
import json

#1 카카오톡 API 사용을 위한 인증 정보 설정
REST_API_KEY = "REST API 키"
REDIRECT_URI = "REDIRECT URI"

#2 토큰을 받기 위한 CODE 값 설정
CODE = "code 값"

#3 카카오톡 API 인증 URL 생성
# print(f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}")

#4 get_new_token 함수 정의
def get_new_token():

    #5 카카오톡 API 토큰 요청 URL
    url = 'https://kauth.kakao.com/oauth/token'

    data = {
        "grant_type": "authorization_code",
        "client_id": REST_API_KEY,
        "redirect_uri": REDIRECT_URI,
        "code": CODE
    }

    response = requests.post(url, data=data)
    res_json = response.json()

    #6 access_token 값 추출 및 반환
    print(res_json)
    try:
        access_token = res_json['access_token']
    except KeyError:
        print("Error: 'access_token' not found in the response.")
        access_token = None

    return access_token

#7 send_msg 함수 정의
def send_msg(access_token_):

    #8 카카오톡 API 메시지 전송 URL
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    #9 메시지 전송을 위한 헤더와 template_object 설정
    headers = {
        "Authorization": f"Bearer {access_token_}"
    }
    data = {
        "object_type": "text",
        "text": "kakao 메신저 테스트 메세지입니다!",
        "link": {
        },
    }
    data = {"template_object": json.dumps(data)}
    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    print(response.json())

#10 get_new_token 함수 호출 및 send_msg 함수 호출
token = get_new_token()
send_msg(token)
