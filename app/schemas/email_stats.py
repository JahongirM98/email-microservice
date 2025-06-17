from pydantic import BaseModel

class EmailStats(BaseModel):
    incoming: int
    outgoing: int
