import smtplib
from email.mime.text import MIMEText
from typing import List

def send_email_smtp(to: List[str], subject: str, body: str, is_html: bool = False):
    sender = "test@example.com"
    smtp_host = "mailpit"  # сервис в docker-compose
    smtp_port = 1025

    msg = MIMEText(body, "html" if is_html else "plain")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(to)

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.sendmail(sender, to, msg.as_string())
