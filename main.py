from bot.bot import Bot
from database.words.words import Word
from database.players.players import Player
from game.mechanics.game_mechanic import GameMechanic
from game.word_generator import WordGenerator
from settings import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_ENCODING, TELEGRAM_ACCESS_TOKEN
from bot.log.path import LOG_PATH

word_db = Word(DB_HOST=DB_HOST, DB_PORT=DB_PORT, DB_NAME=DB_NAME, DB_USER=DB_USER, DB_PASSWORD=DB_PASSWORD, DB_ENCODING=DB_ENCODING)
player_db = Player(DB_HOST=DB_HOST, DB_PORT=DB_PORT, DB_NAME=DB_NAME, DB_USER=DB_USER, DB_PASSWORD=DB_PASSWORD, DB_ENCODING=DB_ENCODING)

word_generator = WordGenerator(word_db=word_db)


bot = Bot(ACCESS_TOKEN=TELEGRAM_ACCESS_TOKEN, game_mechanic=GameMechanic(word_generator=word_generator), words_db=word_db, players_db=player_db, LOG_PATH=LOG_PATH)
bot.run()
