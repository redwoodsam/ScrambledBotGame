"""
Mechanic factory class that will communicate with the main program file.
"""

class MechanicFactory:
    def __init__(self, game_mechanic) -> None:
        self._game_mechanic = game_mechanic()


    def get_game_mechanic(self) -> object:
        return self._game_mechanic