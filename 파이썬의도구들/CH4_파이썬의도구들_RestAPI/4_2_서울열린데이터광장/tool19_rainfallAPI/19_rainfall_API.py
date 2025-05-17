#1 requests와 xml 모듈을 import
import requests
import xml.etree.ElementTree as ET

#2 기상관측정보 API key와 URL을 설정
api_key ='API key'
num_disp = 5
url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/ListRainfallService/1/{num_disp}/'


#3 기상관측정보 API에 요청 및 response 객체 생성
response = requests.get(url)

#4 응답 상태 코드를 확인
if response.status_code != 200:
    print("Error:", response.status_code)
else:
    print("Success:", response.status_code)

    #5 응답 데이터를 XML 형식으로 파싱
    root = ET.fromstring(response.text)
    # print(response.text)

    #6 XML 데이터에서 기상관측정보 응답 정보를 추출
    for i in root.iter('row'):
        RAINGAUGE_NAME = i.find('RAINGAUGE_NAME').text
        RECEIVE_TIME = i.find('RECEIVE_TIME').text
        RAINFALL10 = i.find('RAINFALL10').text
        print("[강우량] 측정 위치:", RAINGAUGE_NAME, "| 업데이트 시간:", RECEIVE_TIME, "| 10분 강우량:", RAINFALL10)
