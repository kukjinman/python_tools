from flask import Flask, request, render_template, url_for
from wordcloud_manager import add_word

app = Flask(__name__)

#5 app.route 루트 페이지
@app.route('/', methods=['GET', 'POST'])
def root_page():
    wordcloud_image = None
    if request.method == 'POST':
        word_input = request.form.get('word_input')

        #6 wordcloud_manager의 add_word 함수 호출
        add_word(word_input)
        wordcloud_image = url_for('assets', filename='wordcloud.png')

    #7 mainpage.html 렌더링
    return render_template('mainpage.html', wordcloud_image=wordcloud_image)

