#1 requests와 xml 모듈을 import
import requests
import xml.etree.ElementTree as ET

#2 지하철 운행정보 API key와 URL을 설정
api_key ='614a4e786774686139364a59775670'
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

    #6 XML 데이터에서 지하철 운행정보 응답 정보를 추출
    for i in root.iter('row'):
        subwayId = i.find('subwayId').text
        trainLineNm = i.find('trainLineNm').text
        updnLine = i.find('updnLine').text
        statnNm = i.find('statnNm').text
        arvlMsg2 = i.find('arvlMsg2').text
        arvlMsg3 = i.find('arvlMsg3').text

        print("[지하철 운행정보] 지하철 ID:", subwayId, "| 노선명:", trainLineNm, "| 상하행선:", updnLine, "| 역명:", statnNm, "| 도착 메시지 2:", arvlMsg2, "| 도착 메시지 3:", arvlMsg3)
