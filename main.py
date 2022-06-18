import os 
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask('app')

app.secret_key = "1234235534534"

@app.route("/")
def index():
    return render_template("/index.html")

if __name__ == "__main__":
    app.run(debug=True)