import qrcode
import os

#1 generate_qrcode 함수
def generate_qrcode(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    #2 static 폴더 생성 및 qrcode.png 저장
    if not os.path.exists('./static'):
        os.makedirs('./static', exist_ok=True)

    img.save("./static/qrcode.png")

