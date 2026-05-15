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
        RF_NM = i.find('RF_NM').text
        DATA_CLCT_TM = i.find('DATA_CLCT_TM').text
        RN_10M = i.find('RN_10M').text
        print("[강우량] 측정 위치:", RF_NM, "| 업데이트 시간:", DATA_CLCT_TM, "| 10분 강우량:", RN_10M)
