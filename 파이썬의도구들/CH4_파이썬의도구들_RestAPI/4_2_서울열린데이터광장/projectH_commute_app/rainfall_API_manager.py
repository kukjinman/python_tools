import requests
import xml.etree.ElementTree as ET

#3 get_rainfall_data 함수
def get_rainfall_data(api_key, num_disp, district):

    url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/ListRainfallService/1/{num_disp}/{district}'

    #4 ret_msg 변수 초기화
    ret_msg = ""
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
    else:
        print("Success:", response.status_code)

        root = ET.fromstring(response.text)
        # print(response.text)

        for i in root.iter('row'):
            RAINGAUGE_NAME = i.find('RAINGAUGE_NAME').text
            RECEIVE_TIME = i.find('RECEIVE_TIME').text
            RAINFALL10 = i.find('RAINFALL10').text
            print("[강우량] 측정 위치:", RAINGAUGE_NAME, "| 업데이트 시간:", RECEIVE_TIME, "| 10분 강우량:", RAINFALL10)

            #5 ret_msg에 강우량 정보를 추가
            ret_msg += f"[강우량] 측정 위치: {RAINGAUGE_NAME} | 업데이트 시간: {RECEIVE_TIME} | 10분 강우량: {RAINFALL10}\n"

    return ret_msg