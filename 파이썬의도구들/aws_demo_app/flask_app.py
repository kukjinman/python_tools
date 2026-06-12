import os

from flask import Flask, render_template, request, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

from check_and_add_word import add_word
from qrcode_manager import generate_qrcode


app = Flask(__name__)
if os.environ.get('TRUST_PROXY_HEADERS') == '1':
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,
        x_proto=1,
        x_host=1
    )

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def ensure_qrcode(site_url):
    """접속 주소가 바뀌면 QR 코드를 다시 생성한다."""
    qrcode_path = os.path.join(static_dir, 'qrcode.png')
    qrcode_url_file = os.path.join(static_dir, 'qrcode_url.txt')

    saved_url = None
    if os.path.exists(qrcode_url_file):
        with open(qrcode_url_file, 'r', encoding='utf-8') as file:
            saved_url = file.read().strip()

    if not os.path.exists(qrcode_path) or saved_url != site_url:
        generate_qrcode(site_url)
        with open(qrcode_url_file, 'w', encoding='utf-8') as file:
            file.write(site_url)


def static_image_url(filename):
    """파일 수정 시간을 붙여 브라우저 이미지 캐시를 갱신한다."""
    file_path = os.path.join(static_dir, filename)
    if not os.path.exists(file_path):
        return None

    return url_for(
        'static',
        filename=filename,
        version=os.stat(file_path).st_mtime_ns
    )


@app.route('/', methods=['GET', 'POST'])
def root_page():
    error_message = None
    site_url = os.environ.get('PUBLIC_URL', request.url_root)
    site_url = f"{site_url.rstrip('/')}/"
    ensure_qrcode(site_url)

    if request.method == 'POST':
        word_input = request.form.get('word_input', '').strip()

        if not word_input:
            error_message = '단어를 입력해주세요.'
        elif not add_word(word_input):
            error_message = '부적절한 단어입니다. 다른 단어를 입력해주세요.'

    return render_template(
        'mainpage.html',
        error_message=error_message,
        wordcloud_image=static_image_url('wordcloud.png')
    )


if __name__ == '__main__':
    app.run(
        host=os.environ.get('FLASK_HOST', '127.0.0.1'),
        port=int(os.environ.get('FLASK_PORT', '5000')),
        debug=os.environ.get('FLASK_DEBUG') == '1'
    )
