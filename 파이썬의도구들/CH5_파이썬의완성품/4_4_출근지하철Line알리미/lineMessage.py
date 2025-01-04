import requests

token = "token"

def sendMsg(text):

    data = {
        "message": text,
        # "imageThumbnail": "https://img.siksinhot.com/seeon/1622690187294631.jpg",
        # "imageFullsize": "https://img.siksinhot.com/seeon/1622690187294631.jpg"
    }
    requests.post("https://notify-api.line.me/api/notify", headers={"Authorization": f"Bearer {token}"}, data=data)
