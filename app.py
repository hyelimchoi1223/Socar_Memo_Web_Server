from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)


@app.route('/')
def index():
    blogger = {'name': 'jvvp', 'eloc': 'songpa'}

    return render_template('index.html', suggestion=blogger)


if __name__ == '__main__':
    app.run(debug=True)
