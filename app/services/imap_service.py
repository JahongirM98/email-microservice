import imaplib
import email
from email.header import decode_header
from typing import List
import os


def fetch_emails(limit=10) -> List[dict]:
    host = os.getenv("IMAP_HOST")
    port = int(os.getenv("IMAP_PORT"))
    user = os.getenv("IMAP_USER")
    password = os.getenv("IMAP_PASS")

    mail = imaplib.IMAP4_SSL(host, port)
    mail.login(user, password)
    mail.select("inbox")

    result, data = mail.search(None, "ALL")
    email_ids = data[0].split()[-limit:]

    emails = []

    for eid in reversed(email_ids):
        result, msg_data = mail.fetch(eid, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject, _ = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(errors="ignore")

        date = msg["Date"]
        sender = msg["From"]
        recipients = msg.get_all("To", [])

        emails.append({
            "date": date,
            "subject": subject,
            "sender": sender,
            "recipients": recipients
        })

    mail.logout()
    return emails


def count_incoming_emails(from_date: str, to_date: str) -> int:
    from datetime import datetime

    host = os.getenv("IMAP_HOST")
    port = int(os.getenv("IMAP_PORT"))
    user = os.getenv("IMAP_USER")
    password = os.getenv("IMAP_PASS")

    mail = imaplib.IMAP4_SSL(host, port)
    mail.login(user, password)
    mail.select("inbox")

    result, data = mail.search(None, "ALL")
    email_ids = data[0].split()

    count = 0
    for eid in email_ids:
        result, msg_data = mail.fetch(eid, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        date_str = msg["Date"]
        try:
            msg_date = datetime.strptime(date_str[:25], "%a, %d %b %Y %H:%M:%S")
        except:
            continue

        f_date = datetime.strptime(from_date, "%Y-%m-%d")
        t_date = datetime.strptime(to_date, "%Y-%m-%d")

        if f_date <= msg_date <= t_date:
            count += 1

    mail.logout()
    return count
