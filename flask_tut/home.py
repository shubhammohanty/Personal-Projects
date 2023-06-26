from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<anything_else>")
def redi(anything_else):
    return render_template("error.html", page = anything_else)


if __name__ == "__main__":
    app.run(debug=True)