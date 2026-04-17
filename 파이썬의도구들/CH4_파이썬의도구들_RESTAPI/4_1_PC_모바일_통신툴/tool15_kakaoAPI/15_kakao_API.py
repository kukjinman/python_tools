import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#1 카카오톡 API 사용을 위한 인증 정보 설정
REST_API_KEY = "REST API 키"
REDIRECT_URI = "REDIRECT URI"
kakao_id = "kakao 아이디"
kakao_pw = "kakao 비밀번호"

#7 agreek_to_terms 함수 정의
def agreek_to_terms(browser):
    check_box = browser.find_element(by=By.CSS_SELECTOR, value='#line_ctr > label > span.ico_agree.ico_chk')
    check_box.click()
    agree_btn = browser.find_element(by=By.CSS_SELECTOR, value='#acceptButton')
    agree_btn.click()
    time.sleep(1)

#3 get_auth_code 함수 정의
def get_auth_code():

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=opt)

    #4 browser로 카카오톡 인증 페이지 열기
    browser.get(f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}")
    time.sleep(1)

    #5 카카오톡 로그인 정보 입력 및 로그인 버튼 클릭
    login_input_id = browser.find_element(by=By.CSS_SELECTOR, value='#loginId--1')
    login_input_id.send_keys(kakao_id)
    login_input_pw = browser.find_element(by=By.CSS_SELECTOR, value='#password--2')
    login_input_pw.send_keys(kakao_pw)
    login_btn = browser.find_element(by=By.CSS_SELECTOR, value='#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit')
    login_btn.click()
    time.sleep(1)

    #6 현재 URL에서 동의 페이지 확인
    current_url = browser.current_url
    # print(current_url)

    if("code=" not in current_url):
        agreek_to_terms(browser)

    #8최종 인증 코드가 포함된 URL에서 code 값 추출
    current_url = browser.current_url
    # print(current_url)

    code = current_url.split("code=")[1]
    print(f"code: {code}")
    browser.quit()

    return code

def get_new_token(code_val_):

    #9 카카오톡 API 토큰 발급 요청
    url = 'https://kauth.kakao.com/oauth/token'
    data = {
        "grant_type": "authorization_code",
        "client_id": REST_API_KEY,
        "redirect_uri": REDIRECT_URI,
        "code": code_val_
    }

    response = requests.post(url, data=data)
    res_json = response.json()

    #10 access_token 값 추출 및 반환
    print(res_json)
    try:
        access_token = res_json['access_token']
    except KeyError:
        print("Error: 'access_token' not found in the response.")
        access_token = None

    return access_token

def send_msg(access_token_):

    #11 카카오톡 메시지 전송
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
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

#2 코드 실행
code_val = get_auth_code()
token = get_new_token(code_val)
send_msg(token)
