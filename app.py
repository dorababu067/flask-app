import smtplib, ssl
from flask import Flask
from datetime import datetime
from email.message import EmailMessage


app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Welcome to the flask scheduler."}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
