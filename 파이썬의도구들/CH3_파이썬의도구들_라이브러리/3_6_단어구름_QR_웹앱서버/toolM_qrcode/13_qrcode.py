import qrcode

#1 QR code에 담을 데이터
data = "https://github.com/kukjinman/python_tools"

#2 qrcode 객체 생성
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#3 QR code에 데이터 추가
qr.add_data(data)
# qr.make(fit=True)

#4 QR code 이미지 생성
img = qr.make_image(fill='black', back_color='white')

#5 QR code 이미지 저장
img.save("qrcode.png")