from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

app = FastAPI()

@app.get("/")
async def root(db: AsyncSession = Depends(get_db)):
    return {"message": "Connection to DB successful!"}
