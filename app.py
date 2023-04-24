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


@scheduler.task(trigger="interval", id="#send_email", seconds=20)
def send_mail():
    logger.info("Mail sent successfully.")
    # port = 465
    # smtp_server = "smtp.gmail.com"
    # username = "dorababua67@gmail.com"
    # password = "gylbwsryythnhfko"

    # message = EmailMessage()
    # message["From"] = "Alapakam Dorababu <dorababua67@gmail.com>"
    # message["To"] = "dorababua67@gmail.com"
    # message["Subject"] = "Greetings"

    # date_time = datetime.now().strftime("%c")
    # content = f"Hey time date and is: {date_time}"
    # message.set_content(content)

    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #     server.login(username, password)
    #     server.send_message(message)


@app.route("/")
def home():
    return {"message": "Welcome to the flask scheduler."}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
