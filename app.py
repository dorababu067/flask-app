import smtplib, ssl
from flask import Flask
from decouple import config
from datetime import datetime
from email.message import EmailMessage


app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Welcome to the flask scheduler."}


@app.route("/send-mail")
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
            return {"message": "Mail send sucessfully"}
        except:
            return {"message": "Mail sending failed"}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
