#1 requests와 xml 모듈을 import
import requests
import xml.etree.ElementTree as ET

#2 지하철 운행정보 API key와 URL을 설정
api_key ='API key'
num_disp = 5
stationName = '서울'
url = f'http://swopenAPI.seoul.go.kr/api/subway/{api_key}/xml/realtimeStationArrival/0/{num_disp}/{stationName}'

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
        subway_mapping = {
            '1001': '1호선', '1002': '2호선', '1003': '3호선', '1004': '4호선',
            '1005': '5호선', '1006': '6호선', '1007': '7호선', '1008': '8호선',
            '1009': '9호선', '1061': '중앙선', '1063': '경의중앙선', '1065': '공항철도',
            '1067': '경춘선', '1075': '분당선', '1077': '신분당선'
        }
        subwayLine = subway_mapping.get(subwayId, subwayId)

        trainLineNm = i.find('trainLineNm').text
        updnLine = i.find('updnLine').text
        statnNm = i.find('statnNm').text
        arvlMsg2 = i.find('arvlMsg2').text
        arvlMsg3 = i.find('arvlMsg3').text

        print("[지하철 운행정보] 지하철 호선:", subwayLine, "| 노선명:", trainLineNm, "| 상하행선:", updnLine, "| 역명:", statnNm, "| 도착 메시지 2:", arvlMsg2, "| 도착 메시지 3:", arvlMsg3)
