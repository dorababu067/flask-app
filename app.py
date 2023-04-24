import logging
import smtplib, ssl
from flask import Flask
from datetime import datetime
from email.message import EmailMessage
from flask_apscheduler import APScheduler
from decouple import config


app = Flask(__name__)
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


@scheduler.task(trigger="interval", id="#send_email", seconds=20)
def send_mail():
    port = 465
    smtp_server = "smtp.gmail.com"

    message = EmailMessage()
    message["From"] = "Alapakam Dorababu <dorababua67@gmail.com>"
    message["To"] = "dorababua67@gmail.com"
    message["Subject"] = "Greetings"

    date_time = datetime.now().strftime("%c")
    content = f"Hey time date and is: {date_time}"
    message.set_content(content)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(config("MAIL_USERNAME"), config("MAIL_PASSWORD"))
            server.send_message(message)
            logging.info("Mail send sucessfully")
        except:
            logging.exception("Authentication Error")


@app.route("/")
def home():
    return {"message": "Welcome to the flask scheduler."}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
