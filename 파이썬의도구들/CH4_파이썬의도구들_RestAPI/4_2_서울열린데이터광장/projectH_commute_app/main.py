#0 projectH를 위한 manager 모듈
from datakorea_manager import send_kakaoapi
from rainfall_API_manager import get_rainfall_data
from subwayAPI_manager import get_subway_info

#1 서울 열린 데이터 광장 API 키 설정
datacenter_apikey = "열린 데이터 광장 API 키"
datacenter_subway_apikey = "열린 데이터 광장 지하철 API 키"

#2 카카오 API 사용을 위한 인증 정보 설정
kakao_apikey = "카카오 API 키"
kakao_redirect_url = "카카오 리다이렉트 URL"
kakao_id = "카카오 아이디"
kakao_pw = "카카오 비밀번호"

#3 get_rainfall_data 함수 호출
rainfall_msg = get_rainfall_data(datacenter_apikey, num_disp=3, district="강서구")

#6 get_subway_info 함수 호출
subway_msg = get_subway_info(datacenter_subway_apikey, num_disp=5, stationName="마곡")

#9 send_kakaoapi 함수 호출
kakao_msg = rainfall_msg + "\n" + subway_msg + "\n"
send_kakaoapi(kakao_apikey, kakao_redirect_url, kakao_id, kakao_pw, kakao_msg)

