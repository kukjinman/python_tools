import requests

api_key ='key'
url = f'http://openapi.seoul.go.kr:8088/{api_key}/xml/GetParkingInfo/1/5/'

response = requests.get(url)
print(response.content)