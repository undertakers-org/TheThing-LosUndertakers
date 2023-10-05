from pydantic import BaseModel


class GameModel(BaseModel):
    game_name: str
    min_players: int
    max_players: int
    id_creator: int
