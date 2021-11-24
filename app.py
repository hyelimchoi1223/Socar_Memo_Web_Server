from flask import Flask, redirect, url_for, request, render_template, session
import requests
import json
from operator import itemgetter

app = Flask(__name__)

rest_url = "http://34.132.153.232:5000/"


@app.route("/")
def index():
    blogger = {"name": "jvvp", "eloc": "songpa"}

    return render_template("index.html", suggestion=blogger)


@app.route("/layout")
def layout():
    return render_template("layout.html")


@app.route("/home", methods=["GET", "POST"])
def home():
    data = {}
    if request.method == "POST":
        description = request.form["description"]
        # description = "미션 교체 카맨모터스 법인카드 결제건"
        res = requests.get(f"{rest_url}classify?desc={description}")
        data = res.content.decode("unicode-escape")
        data = json.loads(data)
        data = sorted(data.items(), key=(lambda x: x[1]), reverse=True)
        data = dict(data[:5])
        data = {k: round(v, 2) * 100 for k, v in data.items()}
        return render_template("home.html", description=data)

    return render_template("home.html", description=data)


@app.route("/result", methods=["POST"])
def result():
    data = request.form["word"]
    print(data)
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
