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
            RF_NM = i.find('RF_NM').text
            DATA_CLCT_TM = i.find('DATA_CLCT_TM').text
            RN_10M = i.find('RN_10M').text
            print("[강우량] 측정 위치:", RF_NM, "| 업데이트 시간:", DATA_CLCT_TM, "| 10분 강우량:", RN_10M)

            #5 ret_msg에 강우량 정보를 추가
            ret_msg += f"[강우량] 측정 위치: {RF_NM} | 업데이트 시간: {DATA_CLCT_TM} | 10분 강우량: {RN_10M}\n"

    return ret_msg