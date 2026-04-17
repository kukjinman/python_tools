from datakorea import kakaoapi

#9 send_kakaoapi 함수
def send_kakaoapi(kakao_apikey, kakao_redirect_url, kakao_id, kakao_pw, msg):

    m_kakao = kakaoapi(kakao_apikey, kakao_redirect_url, kakao_id, kakao_pw)
    m_kakao.send_text_msg(msg)
