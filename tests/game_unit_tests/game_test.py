from ScrambledWordsBot.game.mechanic_factory import MechanicFactory

game = MechanicFactory()
game = game.get_game_mechanic()

print(type(game))