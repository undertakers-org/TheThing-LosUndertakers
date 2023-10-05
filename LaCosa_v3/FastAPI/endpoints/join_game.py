from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session

from main import app
from database import GameTable, UserTable, get_db


@app.post("/games/{game_name}/join/{player_id}")
async def join_game(game_name: str, player_id: int, db: Session = Depends(get_db)):
    game = db.query(GameTable).filter(GameTable.game_name == game_name).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if game.players_in is not None and game.players_in >= game.max_players:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    existing_player_game = db.query(UserTable).filter(UserTable.id == player_id).first()
    if existing_player_game and existing_player_game.user_game:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if game.id_creator == player_id:
        user = db.query(UserTable).filter(UserTable.id == game.id_creator).first()
        if user:
            user.user_game = game.game_name
            user.is_creator = 1
    else:
        user = db.query(UserTable).filter(UserTable.id == player_id).first()
        user.is_creator = 0
        user.user_game = game_name

    game.players_in += 1
    db.commit()

    return {"message": "Te has unido a la partida."}
