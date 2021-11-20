from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)


@app.route('/')
def index():
    blogger = {'name': 'jvvp', 'eloc': 'songpa'}

    return render_template('index.html', suggestion=blogger)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.form['word']
    print(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)
