from pydantic import BaseModel
from typing import List

class EmailMetadata(BaseModel):
    date: str
    subject: str
    sender: str
    recipients: List[str]
