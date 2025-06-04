from fastapi import APIRouter, HTTPException
from app.schemas.email_schema import EmailRequest
from app.services.email_service import send_email_smtp

router = APIRouter()

@router.post("/send")
async def send_email(email: EmailRequest):
    try:
        send_email_smtp(email.to, email.subject, email.body, email.is_html)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
