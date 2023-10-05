from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status

from main import app
from models import GameModel
from database import GameTable, get_db

@app.post("/games/")
async def create_game(game: GameModel, db: Session = Depends(get_db)):

    existing_game = db.query(GameTable).filter(GameTable.game_name == game.game_name).first()
    if existing_game:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    db_game = GameTable(**dict(game))
    db_game.game_state = 0
    db_game.players_in = 0

    db.add(db_game)
    db.commit()
    db.refresh(db_game)

    return {"game_name": db_game.game_name}
