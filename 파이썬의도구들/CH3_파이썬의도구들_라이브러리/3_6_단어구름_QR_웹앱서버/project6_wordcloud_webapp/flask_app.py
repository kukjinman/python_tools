
from qrcode_manager import generate_qrcode
from flask import Flask, request, render_template, url_for
from wordcloud_manager import add_word

#0 QR코드 생성
generate_qrcode("https://kukjinman.pythonanywhere.com/")

#3 Flask 앱 생성 및 실행
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def root_page():
    wordcloud_image = None
    if request.method == 'POST':
        word_input = request.form.get('word_input')

        #4 wordcloud_manager의 add_word 함수 호출
        add_word(word_input)
        wordcloud_image = url_for('static', filename='wordcloud.png')

    return render_template('mainpage.html', wordcloud_image=wordcloud_image)

# pythonanywhere에서는 app.run()을 사용하면 안됩니다.!
# app.run(debug=True)