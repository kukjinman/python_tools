import requests
import xml.etree.ElementTree as ET

#6 get_subway_info() 함수
def get_subway_info(api_key, num_disp, stationName):
    url = f'http://swopenAPI.seoul.go.kr/api/subway/{api_key}/xml/realtimeStationArrival/0/{num_disp}/{stationName}'
    #7 ret_msg 변수 초기화
    ret_msg = ""
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
    else:
        print("Success:", response.status_code)
        root = ET.fromstring(response.text)
        # print(response.text)
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

            #8 ret_msg에 지하철 운행정보 추가
            ret_msg += f"[지하철 운행정보] 지하철 호선: {subwayLine} | 노선명: {trainLineNm} | 상하행선: {updnLine} | 역명: {statnNm} | 도착 메시지 2: {arvlMsg2} | 도착 메시지 3: {arvlMsg3}\n"
    return ret_msg