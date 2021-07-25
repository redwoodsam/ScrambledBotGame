"""
Class defining the player database and its management functions
"""
from ScrambledWordsBot.database.db_settings import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_ENCODING
from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set the initial things to create the database
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset={DB_ENCODING}',
                       echo=False)
Base = declarative_base()


# Defining the database body and its methods
class Player(Base):

    __tablename__ = 'players'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False)
    first_name = Column(String(20))
    last_name = Column(String(30))
    username = Column(String(15), unique=True, nullable=False)
    xp = Column(BigInteger, default=0)
    highest_score = Column(BigInteger, default=0)


    def check_if_player_exists(self, username):
        """
        Checks if a player exists in the database.
        """
        # Creating the session
        Session = sessionmaker(bind=engine)
        session = Session()

        player = session.query(Player).filter(Player.username == username).first()
        if player == None:
            return False

        else:
            return True

    def add_player(self, chat_id, first_name, last_name, username):
        """
        Adds a player into the database.
        """
        # Creating the session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Adding the player to the session
        player = Player(chat_id=chat_id, username=username, first_name=first_name, last_name=last_name)
        session.add(player)

        # Sending the data to the database and closing the session
        session.commit()
        session.close()

    def check_admin(self, username):
        """
        Checks if a specified player is an admin.
        """
        Session = sessionmaker(bind=engine)
        session = Session()

        player = session.query(Player).filter(Player.username == username).first()

        if player is not None:
            if player.is_admin:
                session.close()
                return True
            else:
                session.close()
                return False
        else:
            return False

    def grant_admin(self, username):
        """
        Grants admin status to a player.
        """
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            player = session.query(Player).filter(Player.username == username).first()
            player.is_admin = True

            session.commit()
            session.close()
            return True

        except Exception as e:
            return False, e.args

    def add_experience(self, chat_id):
        """
        Adds points to the player's experience stat.
        """

        Session = sessionmaker(bind=engine)
        session = Session()

        # Adds one point to the player's experience.
        player = session.query(Player).filter(Player.chat_id == chat_id).first()
        player.xp += 1

        # Commit the changes to the database.
        session.commit()
        # Closes the session
        session.close()

    def add_highest_score(self, chat_id, score):
        """
        Adds the current highest score of a player.
        """
        Session = sessionmaker(bind=engine)
        session = Session()

        # Queries the player based on the given chat_id and stores in a variable
        player = session.query(Player).filter(Player.chat_id == chat_id).first()
        if player.highest_score < score:
            player.highest_score = score
            session.commit()
            session.close()
        else:
            session.close()

    def get_leaderboard(self) -> list:
        """
        Gets the current leaderboard of the game.
        """
        leaderboard = []
        Session = sessionmaker(bind=engine)
        session = Session()
        count = 1

        # Iterates over the players in the database and orders by a descending list of hiscores
        for instance in session.query(Player).order_by(Player.highest_score.desc()):
            leaderboard.append(f'{(count)}. @{instance.username} - {instance.highest_score}')
            count += 1

        session.close()
        return leaderboard

    def get_stats(self, chat_id) -> dict:
        """
        Gets the statistics of a specific player.
        """
        Session = sessionmaker(bind=engine)
        session = Session()

        player = session.query(Player).filter(Player.chat_id == chat_id).first()
        stats = {
                 'name': player.first_name,
                 'last_name': player.last_name,
                 'xp': player.xp,
                 'hiscore': player.highest_score
                 }

        session.close()
        return stats


# Create the tables
Base.metadata.create_all(engine)
