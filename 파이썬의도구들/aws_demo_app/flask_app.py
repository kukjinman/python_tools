import os

from flask import Flask, render_template, request, url_for

from check_and_add_word import add_word
from qrcode_manager import generate_qrcode


app = Flask(__name__)
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


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
    qrcode_path = os.path.join(static_dir, 'qrcode.png')

    if not os.path.exists(qrcode_path):
        generate_qrcode(request.url_root)

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
    app.run(debug=True)
