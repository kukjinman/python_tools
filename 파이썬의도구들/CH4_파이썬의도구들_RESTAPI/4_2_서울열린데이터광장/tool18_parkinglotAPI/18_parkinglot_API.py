#1 requests와 xml 모듈을 import
import requests
import xml.etree.ElementTree as ET

#2 공영주차장정보 API key와 URL을 설정
api_key ='API key'
num_disp = 5
url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/GetParkingInfo/1/{num_disp}/'


#3 공영주차장정보 API에 요청 및 response 객체 생성
response = requests.get(url)

#4 응답 상태 코드를 확인
if response.status_code != 200:
    print("Error:", response.status_code)
else:
    print("Success:", response.status_code)

    #5 응답 데이터를 XML 형식으로 파싱
    root = ET.fromstring(response.text)
    # print(response.text)

    #6 XML 데이터에서 공영주차장정보 응답 정보를 추출
    for i in root.iter('row'):
        PKLT_NM = i.find('PKLT_NM').text
        NOW_PRK_VHCL_UPDT_TM = i.find('NOW_PRK_VHCL_UPDT_TM').text
        TPKCT = i.find('TPKCT').text
        NOW_PRK_VHCL_CNT = i.find('NOW_PRK_VHCL_CNT').text
        print("[주차장] 주차장명:", PKLT_NM, "| 업데이트 시간:", NOW_PRK_VHCL_UPDT_TM, "| 총 주차면 수:", TPKCT, "현재 주차 차량 수:", NOW_PRK_VHCL_CNT)

