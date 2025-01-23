import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()  # JSON 응답을 파이썬 객체로 변환
        for user in users:
            print(f"이름: {user['name']}, 이메일: {user['email']}")
    else:
        print(f"오류 발생: {response.status_code}")

if __name__ == "__main__":
    fetch_users()