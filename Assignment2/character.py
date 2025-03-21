import random

import main
from main import *

class Character:
    def __init__(self):
        #TODO: Need to choose a random option from the dice - to "Roll the dice"
        self._combat_strength = main.small_dice_options()
        self._health_points = main.big_dice_options()

    @property
    def get_combat_strength(self):
        return self._combat_strength

    # TODO: Why can I not add set to the start of this?
    # Use of set_ in decorator name leads to errors (?), cannot resolve name and suggests self.set
    @combat_strength.setter
    def combat_strength(self, value):
        if not 1 <= value <= 6:
            raise ValueError('Combat strength must be between 1 and 6.')
        else:
            self._combat_strength = value

    @property
    def get_health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if not value >= 0:
            raise ValueError('Health points must be greater than 0.')
        else:
            self._health_points = value

    def __del__(self):
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector")





