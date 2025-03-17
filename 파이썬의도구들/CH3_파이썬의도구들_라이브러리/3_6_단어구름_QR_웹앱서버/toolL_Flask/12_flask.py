from flask import Flask, request, render_template

#1 Flask 객체 생성
app = Flask(__name__)

#2 웹 앱 루트 페이지('/')
@app.route('/', methods=['GET', 'POST'])
def root_page():
    greeting = None
    #3 POST 요청 처리
    if request.method == 'POST':
        intput_name = request.form.get('intput_name')
        greeting = f'Hello {intput_name}!'
    #4 mainpage.html 페이지 렌더링
    return render_template('mainpage.html', greeting=greeting)

#5 웹 앱 실행
app.run(debug=True)