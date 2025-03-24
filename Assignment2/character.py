import random

import main
from main import *

class Character:
    def __init__(self):
        #TODO: Need to choose a random option from the dice - to "Roll the dice"
        self._combat_strength = random.choice(range(1, 7))
        self._health_points = random.choice(range(1, 21))

    @property
    def combat_strength(self):
        return self._combat_strength

    # Use of set_ in decorator name leads to errors, cannot resolve name and suggests self.set.
    @combat_strength.setter
    def combat_strength(self, value):
        if not 1 <= value <= 6:
            raise ValueError('Combat strength must be between 1 and 6.')
        else:
            self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if not value >= 0:
            raise ValueError('Health points must be greater than 0.')
        else:
            self._health_points = value

    def __del__(self):
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector")





