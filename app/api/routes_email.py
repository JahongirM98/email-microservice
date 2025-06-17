from fastapi import APIRouter, HTTPException, Query
from app.schemas.email_schema import EmailRequest
from app.services.email_service import send_email_smtp
from typing import List
from app.services.imap_service import fetch_emails
from app.schemas.email_response import EmailMetadata
from app.schemas.email_stats import EmailStats
from app.services.imap_service import count_incoming_emails
from datetime import datetime
from typing import Optional

router = APIRouter()

@router.post("/send")
async def send_email(email: EmailRequest):
    try:
        send_email_smtp(email.to, email.subject, email.body, email.is_html)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats", response_model=EmailStats)
async def get_stats(from_date: str, to_date: str):
    incoming = count_incoming_emails(from_date, to_date)
    outgoing = 0  # нет логирования отправки — заглушка

    return {"incoming": incoming, "outgoing": outgoing}


@router.get("/", response_model=List[EmailMetadata])
async def get_emails(
    limit: int = Query(10, le=50),
    from_date: Optional[str] = Query(None, description="Формат YYYY-MM-DD"),
    to_date: Optional[str] = Query(None, description="Формат YYYY-MM-DD"),
    subject: Optional[str] = None,
    email: Optional[str] = None,
):
    emails = fetch_emails(limit)

    def str_to_date(s):
        try:
            return datetime.strptime(s, "%Y-%m-%d")
        except:
            return None

    from_dt = str_to_date(from_date)
    to_dt = str_to_date(to_date)

    filtered = []
    for e in emails:
        try:
            msg_date = datetime.strptime(e["date"][:25], "%a, %d %b %Y %H:%M:%S")
        except:
            msg_date = None

        if from_dt and msg_date and msg_date < from_dt:
            continue
        if to_dt and msg_date and msg_date > to_dt:
            continue
        if subject and subject.lower() not in e["subject"].lower():
            continue
        if email:
            if email.lower() not in (e["sender"] or "").lower() and \
               not any(email.lower() in r.lower() for r in e["recipients"]):
                continue

        filtered.append(e)

    return filtered


