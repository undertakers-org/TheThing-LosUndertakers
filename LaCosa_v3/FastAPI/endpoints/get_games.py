from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from main import app
from models import GameModel
from database import GameTable, get_db


@app.get("/games_list/", response_model=List[GameModel])
async def get_games(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    games = db.query(GameTable).filter(GameTable.game_state == 0).offset(skip).limit(limit).all()
    return games
