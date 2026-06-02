#!/usr/bin/env python3
"""
qrcode_manager.py - PHP에서 shell_exec으로 호출 가능한 QR코드 생성기
사용법: python3 qrcode_manager.py "https://example.com/"
"""
import qrcode
import os
import sys


def generate_qrcode(data):
    """QR코드를 생성하여 static/qrcode.png로 저장"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir, exist_ok=True)

    png_path = os.path.join(static_dir, 'qrcode.png')
    img.save(png_path)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        generate_qrcode(url)
        print(f"QR code generated for: {url}")
    else:
        print("Usage: python3 qrcode_manager.py <url>")

