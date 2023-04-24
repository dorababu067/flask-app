import smtplib, ssl
from flask import Flask
from datetime import datetime
from email.message import EmailMessage
from flask_apscheduler import APScheduler
from config import logger


app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.api_enabled = True
scheduler.start()


@scheduler.task("interval", id="#send_email", seconds=10)
def send_mail():
    logger.info("Mail sent successfully.")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
