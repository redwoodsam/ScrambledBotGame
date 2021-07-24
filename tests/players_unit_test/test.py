from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, BigInteger, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

#Set the initial things to create the database
engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


#Defining the database body and its methods
class Player(Base):

    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    is_admin = Column(Boolean, default=False)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    highest_score = Column(BigInteger, default=0)

    def check_if_player_exists(self, first_name):
        #Creating the session
        Session = sessionmaker(bind=engine)
        session = Session()

        player = session.query(Player).filter(Player.first_name == first_name).first()

        if player == None:
            return False

        else:
            return True


    def add_player(self, first_name, last_name, username):
        try:
            #Creating the session
            Session = sessionmaker(bind=engine)
            session = Session()

            #Adding the player to the session
            player = Player(username=username, first_name=first_name, last_name=last_name)
            session.add(player)

            #Sending the data to the database and closing the session
            session.commit()
            session.close()
            return True

        except Exception as e:
            return False, e.args


    def check_admin(self, first_name):
        Session = sessionmaker(bind=engine)
        session = Session()

        player = session.query(Player).filter(first_name == first_name).first()

        if player is not None:
            if player.is_admin:
                session.close()
                return True
            elif not player.is_admin:
                session.close()
                return False
        else:
            return False

    def grant_admin(self, first_name):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            player = session.query(Player).filter_by(first_name = first_name).first()
            player.is_admin = True

            session.commit()
            session.close()
            return True
        except Exception as e:
            return False, e.args


    def add_highest_score(self, first_name, highest_score):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            player = session.query(Player).filter(Player.first_name == first_name).first()
            player.highest_score = highest_score
            session.commit()
            session.close()
            return True

        except Exception as e:
            return False, e.args

    def get_my_hiscore(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        player = session.query(Player).filter(Player.username == '@redwoodsam').first()
        return player.highest_score

    def get_leaderboard(self) -> list:
        leaderboard = []
        Session = sessionmaker(bind=engine)
        session = Session()
        count = 1
        for instance in session.query(Player).order_by(Player.highest_score.desc()):
            leaderboard.append(f'{(count)}. {instance.username} {instance.first_name} - {instance.highest_score}')
            count += 1
        session.close()
        return leaderboard

Base.metadata.create_all(engine)