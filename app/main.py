from fastapi import FastAPI
from app.api.routes_email import router as email_router

app = FastAPI()

app.include_router(email_router, prefix="/emails", tags=["Emails"])
