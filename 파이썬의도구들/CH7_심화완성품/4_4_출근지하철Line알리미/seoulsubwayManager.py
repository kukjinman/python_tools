import xml.etree.ElementTree as ET

import requests
import lineMessage


seoulApi = '684469536a74686136336364556f68'
stationName = "가양"

url = f"http://swopenAPI.seoul.go.kr/api/subway/{seoulApi}/xml/realtimeStationArrival/0/5/{stationName}"

data = requests.get(url)
print(data.text)

root = ET.fromstring(data.text)
total_count = int(root.find('RESULT/total').text)

message = "\n"

for i in range(total_count):
    row = root.find(f'row[rowNum="{i+1}"]')
    updnLine = row.find('updnLine').text
    trainLineNm = row.find('trainLineNm').text
    arvlMsg2 = row.find('arvlMsg2').text
    print(f'updnLine: {updnLine}, trainLineNm: {trainLineNm}, arvlMsg2: {arvlMsg2}')
    message += f'updnLine: {updnLine}\ntrainLineNm: {trainLineNm}\narvlMsg2: {arvlMsg2}\n'
    message += '-----------------------------'


lineMessage.sendMsg(message)
