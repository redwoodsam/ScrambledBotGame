from venv import create
from bot.bot import Bot
from database.words.words import Word
from database.players.players import Player
from database.engine_factory import generate_engine
from game.mechanics.game_mechanic import GameMechanic
from game.word_generator import WordGenerator
from settings import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_ENCODING, TELEGRAM_ACCESS_TOKEN
from bot.log.path import LOG_PATH

DB_ENGINE = generate_engine(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_ENCODING)

word_db = Word()
word_db.engine = DB_ENGINE
word_db.start_db()

# Make the first check if there's any words in the database, if not, add the first word.
try:
    word_db.get_word()

except Exception:
    word_db.add_word("butterfly", "A beautiful flying insect which its first stage is a caterpillar.")

player_db = Player()
player_db.engine = DB_ENGINE
player_db.start_db()

word_generator = WordGenerator(word_db=word_db)

bot = Bot(ACCESS_TOKEN=TELEGRAM_ACCESS_TOKEN, game_mechanic=GameMechanic(word_generator=word_generator), words_db=word_db, players_db=player_db, LOG_PATH=LOG_PATH)
bot.run()
