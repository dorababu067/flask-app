import smtplib, ssl
from flask import Flask
from datetime import datetime
from email.message import EmailMessage
from flask_apscheduler import APScheduler
from config import logger


app = Flask(__name__)
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


@scheduler.task(trigger="interval", id="#send_email", seconds=5)
def send_mail():
    logger.info("Mail sent successfully.")


@app.route("/")
def home():
    return {"message": "Welcome to the flask scheduler."}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
