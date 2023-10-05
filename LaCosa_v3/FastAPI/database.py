from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String


__Base__ = declarative_base()


class UserTable(__Base__):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50), unique=True)
    is_creator = Column(Boolean)
    user_game = Column(String(50))


class GameTable(__Base__):
    __tablename__ = 'games'

    game_name = Column(String(50), primary_key=True)
    game_state = Column(Integer)
    players_in = Column(Integer)
    min_players = Column(Integer)
    max_players = Column(Integer)
    id_creator = Column(Integer)


__URL_DATABASE__ = 'mysql+pymysql://root:admin@localhost:3306/TheThing_undertakers'
__engine__ = create_engine(__URL_DATABASE__)
__Base__.metadata.create_all(bind=__engine__)
__SessionLocal__ = sessionmaker(autocommit=False, autoflush=False, bind=__engine__)


def get_db():
    db = __SessionLocal__()
    try: yield db
    finally: db.close()
