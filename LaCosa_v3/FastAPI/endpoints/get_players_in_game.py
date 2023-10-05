from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session

from main import app
from database import GameTable, UserTable, get_db


@app.get("/games/{game_name}/players", response_model=List[str])
async def get_players_in_game(game_name: str, db: Session = Depends(get_db)):
    game = db.query(GameTable).filter(GameTable.game_name == game_name).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    players = db.query(UserTable.nickname).filter(UserTable.user_game == game_name).all()
    return [row[0] for row in players]
