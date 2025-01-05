import requests

api_key ='key'
url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/citydata/1/5/광화문·덕수궁'

response = requests.get(url)
print(response.content)