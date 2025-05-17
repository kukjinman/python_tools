#1 requests와 xml 모듈을 import
import requests
import xml.etree.ElementTree as ET

#2 지하철 운행정보 API key와 URL을 설정
api_key ='API key'
num_disp = 10
stationName = '서울'
url = f'http://swopenAPI.seoul.go.kr/api/subway/{api_key}/xml/realtimeStationArrival/0/5/{stationName}'

#3 지하철 운행정보 API에 요청 및 response 객체 생성
response = requests.get(url)

#4 응답 상태 코드를 확인
if response.status_code != 200:
    print("Error:", response.status_code)
else:
    print("Success:", response.status_code)

    #5 응답 데이터를 XML 형식으로 파싱
    root = ET.fromstring(response.text)
    print(response.text)

    # #6 XML 데이터에서 지하철 운행정보 응답 정보를 추출
    # for i in root.iter('row'):
    #     M_NAME = i.find('M_NAME').text
    #     A_NAME = i.find('A_NAME').text
    #     A_PRICE = i.find('A_PRICE').text
    #     P_DATE = i.find('P_DATE').text
    #
    #     print("[물가정보] 마트명:", M_NAME, "| 품목명:", A_NAME, "| 가격:", A_PRICE, "| 업데이트 시간:", P_DATE)