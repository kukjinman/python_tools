from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    greeting = None
    if request.method == 'POST':
        name = request.form.get('name', 'World')
        greeting = f'Hello {name}!'
    return render_template('mainpage.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)