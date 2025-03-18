from character import Character

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)

        def hero_attacks(self, monster):
            print(F"hero attacks {monster.name}")
            if self.combat_strength >= monster.health_points:
                monster.health_points = 0
                print("Hero defeated the monster!")
            else:
                monster.health_points -= self.combat_strength
                print(f"Monster reamining health: {monster.health_points}")
