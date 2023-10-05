from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from endpoints.create_game import create_game
from endpoints.create_user import create_user
from endpoints.get_game_status import get_game_status
from endpoints.get_games import get_games
from endpoints.get_players_in_game import get_players_in_game
from endpoints.join_game import join_game
from endpoints.start_game import start_game
