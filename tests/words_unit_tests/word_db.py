from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setting the initial things to create the database
engine = create_engine('sqlite:///words.db', echo=True)
Base = declarative_base()


class Word(Base):
    __tablename__ = 'words'

    # Setting up the tables
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, unique=True, nullable=False)
    tip = Column(String, unique=True, nullable=False)

    def get_word(self) -> str:
        Session = sessionmaker(bind=engine)
        session = Session()

        random_word = session.query(Word).order_by(func.random()).first()

        session.close()
        return random_word.word

    def get_tip(self, word) -> str:
        Session = sessionmaker(bind=engine)
        session = Session()

        specified_word = session.query(Word).filter(Word.word == word).first()

        session.close()

        return specified_word.tip

    def add_word(self, word, tip):
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            word = Word(word=word, tip=tip)
            session.add(word)

            session.commit()
            session.close()
            return True
        except Exception as e:
            session.close()
            return False, e.args


Base.metadata.create_all(engine)
