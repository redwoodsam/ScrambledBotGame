"""
Mechanic factory class that will communicate with the main program file.
"""
from ScrambledWordsBot.game.mechanics.game_mechanic import GameMechanic

class MechanicFactory:
    def __init__(self) -> None:
        self._game_mechanic = GameMechanic()


    def get_game_mechanic(self) -> object:
        return self._game_mechanic