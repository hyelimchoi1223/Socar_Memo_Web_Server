from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)


@app.route("/")
def index():
    blogger = {"name": "jvvp", "eloc": "songpa"}

    return render_template("index.html", suggestion=blogger)


@app.route("/layout")
def layout():
    return render_template("layout.html")


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form["description"]
        return render_template("home.html", description=data)

    return render_template("home.html")


@app.route("/result", methods=["POST"])
def result():
    data = request.form["word"]
    print(data)
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
