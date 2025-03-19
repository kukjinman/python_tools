
from webapp_manager import init_app
from qrcode_manager import generate_qrcode

#0 QR코드 생성
generate_qrcode("https://kukjinman.pythonanywhere.com/")

#3 웹앱 서버 실행
init_app()
