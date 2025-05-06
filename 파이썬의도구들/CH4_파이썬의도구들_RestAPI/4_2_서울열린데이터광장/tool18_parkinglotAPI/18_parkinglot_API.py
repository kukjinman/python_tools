import requests
import xml.etree.ElementTree as ET

api_key ='API key'
url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/GetParkingInfo/1/5/'

response = requests.get(url)

if response.status_code != 200:
    print("Error:", response.status_code)
else:
    print("Success:", response.status_code)

    root = ET.fromstring(response.text)
    # print(response.text)

    for i in root.iter('row'):
        PKLT_NM = i.find('PKLT_NM').text
        NOW_PRK_VHCL_UPDT_TM = i.find('NOW_PRK_VHCL_UPDT_TM').text
        TPKCT = i.find('TPKCT').text
        NOW_PRK_VHCL_CNT = i.find('NOW_PRK_VHCL_CNT').text
        print("주차장명:", PKLT_NM, "주차장 업데이트 시간:", NOW_PRK_VHCL_UPDT_TM, "총 주차면 수:", TPKCT, "현재 주차 차량 수:", NOW_PRK_VHCL_CNT)

