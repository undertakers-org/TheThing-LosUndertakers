from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session

from main import app
from database import GameTable, UserTable, get_db


@app.post("/games/{game_name}/start/{player_id}")
async def start_game(game_name: str, player_id: int, db: Session = Depends(get_db)):
    game = db.query(GameTable).filter(GameTable.game_name == game_name).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if game.players_in < game.min_players:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        user = db.query(UserTable).filter(UserTable.id == player_id).first()

        if user.is_creator:
            game.game_state = 1
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return {"message": "Game started successfully"}
