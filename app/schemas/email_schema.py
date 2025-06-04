from typing import List
from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    to: List[EmailStr]
    subject: str
    body: str
    is_html: bool = False
