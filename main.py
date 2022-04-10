import os 
from waitress import serve
from app.routes import init_app

app = init_app()

app.secret_key = "1234235534534"

if __name__ == "__main__":
    serve(app=app, host="0.0.0.0", port=8080)