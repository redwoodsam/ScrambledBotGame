"""
Class to manage the words database.
"""

from sqlalchemy import Column, String, BigInteger, Identity
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Setting the initial things to create the database
Base = declarative_base()


class Word(Base):

    engine = None

    __tablename__ = 'words'

    # Setting up the tables
    id = Column(BigInteger, Identity(start=1, cycle=True), primary_key=True)
    word = Column(String(20), unique=True, nullable=False)
    tip = Column(String(100), unique=True, nullable=False)

    def start_db(self) -> None:
        Base.metadata.create_all(self.engine)


    def get_word(self) -> str:
        """
        Fetches a random word from the database and return it.
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        random_word = session.query(Word).order_by(func.random()).first()

        session.close()
        return random_word.word


    def add_word(self, word, tip):
        """
        Adds a new word to the database alongside with its tip.
        """

        Session = sessionmaker(bind=self.engine)
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

    def get_tip(self, word) -> str:
        """
        Returns the tip from a specific word in the database
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        specified_word = session.query(Word).filter(Word.word == word).first()

        session.close()

        return specified_word.tip

    def set_tip(self, word, new_tip) -> bool:
        """
        Sets a new tip for a specified word in the database
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()

        specified_word = session.query(Word).filter(Word.word == word).first()

        if specified_word is None:
            session.close()
            return False
        else:
            specified_word.tip = new_tip
            session.commit()
            session.close()
            return True
