import smtplib
import email.message
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(flag):
    email_body = f"""
    <p>Alert of <b>{flag}</b> transactions above normal levels</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Monitoring Alert"
    msg['From'] = "rafaelcs_94@hotmail.com"
    msg['To'] = "rafaelcs_94@hotmail.com"
    password = os.getenv('PASSWORD')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp-mail.outlook.com', 587)
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("Alert sent")
