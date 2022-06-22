import os 
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask('app')

app.secret_key = "1234235534534"

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/mission")
def mission():
    return render_template("/mission.html")

@app.route("/format")
def format():
    return render_template("/format.html")

@app.route("/archive")
def archive():
    return render_template("/archive.html")

@app.route("/current")
def current():
    return render_template("/current.html")

@app.route("/people")
def people():
    return render_template("people.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug=True)