import requests

def request_to_load_users():
    #1 jsonplaceholder 서버의 users 정보 request
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    #2 request에 대한 reponse 확인
    if response.status_code == 200:
        users = response.json()  # JSON 응답을 파이썬 객체로 변환
        for user in users:
            print(f"이름: {user['name']}, 이메일: {user['email']}")
    else:
        print(f"오류 발생: {response.status_code}")

#3 request_to_load_users 함수 호출
request_to_load_users()