from datetime import datetime

import requests
import json

api_key = 'key'
url = f'http://openapi.seoul.go.kr:8088/{api_key}/json/citydata/1/5/광화문·덕수궁'  # json 형식으로 요청

response = requests.get(url)

# 응답이 성공적일 경우
if response.status_code == 200:
    # JSON 데이터로 변환
    data = response.json()
    date = datetime.now().strftime('%Y%m%d_%H%M%S')
    # JSON 파일로 저장
    with open(f'{date}_citydata.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print("JSON 파일이 성공적으로 저장되었습니다.")
else:
    print(f"API 요청 실패: {response.status_code}")