
from qrcode_manager import generate_qrcode
from flask import Flask, request, render_template, url_for
from wordcloud_manager import add_word

#0 QR코드 생성
generate_qrcode("https://kukjinman.pythonanywhere.com/")

# 한글 비속어 리스트
BANNED_WORDS = [
    '씨발', '병신', '객년', '년놈', '놈', '개새끼', '새끼', '지랄', '미친', '미쳤',
    '씨', '개', '뻑', '띠', '한심', '정신'
]

def is_bad_word(word):
    """비속어 포함 여부 확인"""
    lower_word = word.lower()
    for banned in BANNED_WORDS:
        if banned in lower_word:
            return True
    return False

#3 Flask 앱 생성 및 실행
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def root_page():
    wordcloud_image = None
    error_message = None
    if request.method == 'POST':
        word_input = request.form.get('word_input')

        # 비속어 검증
        if is_bad_word(word_input):
            error_message = "❌ 부적절한 단어입니다. 다른 단어를 입력해주세요."
        else:
            #4 wordcloud_manager의 add_word 함수 호출
            add_word(word_input)
            wordcloud_image = url_for('static', filename='wordcloud.png')

    return render_template('mainpage.html', wordcloud_image=wordcloud_image, error_message=error_message)

# pythonanywhere에서는 app.run()을 사용하면 안됩니다.!
app.run(debug=True)