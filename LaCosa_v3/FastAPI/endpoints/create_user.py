from fastapi import HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from main import app
from database import UserTable, get_db


@app.post("/users/")
async def create_user(nickname: str, db: Session = Depends(get_db)):
    existing_user = db.query(UserTable).filter(UserTable.nickname == nickname).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    db_user = UserTable(nickname=nickname)

    db.add(db_user)
    db.commit()

    return JSONResponse(content={"user_id": db_user.id})
