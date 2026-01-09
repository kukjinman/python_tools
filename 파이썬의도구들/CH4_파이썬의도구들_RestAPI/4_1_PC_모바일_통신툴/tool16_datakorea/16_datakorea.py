#1 datakorea 패키지 가져오기
from datakorea import kakaoapi

#2 kakao api 사용을 위한 인증 정보 설정
REST_API_KEY = "REST API 키"
REDIRECT_URI = "REDIRECT URI"
kakao_id = "kakao 아이디"
kakao_pw = "kakao 비밀번호"

#3 datakorea의 send_text_msg test code
def test_kakaoapi():

    m_kakao = kakaoapi(REST_API_KEY, REDIRECT_URI, kakao_id, kakao_pw)
    m_kakao.send_text_msg("kakao 메신저 테스트 메세지입니다!")

#4 test_kakaoapi 함수 호출
test_kakaoapi()