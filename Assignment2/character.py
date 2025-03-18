import randoms

class Character:
    def __init__(self, name):
        self._name = name
        self._combat_strength = random.randint(1, 6)
        self._health_points = random.randint(1, 6)

        @property
        def combat_strength(self):
            return self._combat_strength

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
            print(f"{self.__class__.__name__} is being destroyed.")





