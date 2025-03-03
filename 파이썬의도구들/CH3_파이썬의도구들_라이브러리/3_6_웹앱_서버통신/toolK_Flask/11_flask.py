from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML 템플릿
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Function</title>
</head>
<body>
    <h1>Say Hello</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Enter your name" required>
        <button type="submit">Submit</button>
    </form>
    {% if greeting %}
        <p>{{ greeting }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def hello():
    greeting = None
    if request.method == 'POST':
        name = request.form.get('name', 'World')
        greeting = f'Hello {name}!'
    return render_template_string(HTML_TEMPLATE, greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)