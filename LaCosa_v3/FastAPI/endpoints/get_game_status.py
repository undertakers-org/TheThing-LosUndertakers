from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session

from main import app
from database import GameTable, get_db


@app.get("/games/{game_name}/status")
async def get_game_status(game_name: str, db: Session = Depends(get_db)):
    game = db.query(GameTable).filter(GameTable.game_name == game_name).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"gameStarted": game.game_state == 1}
