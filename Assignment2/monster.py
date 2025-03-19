from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()  # Call parent constructor

    def monster_attacks(self, hero):
        ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
        print(ascii_image2)
        print("Monster attacks Hero!")
        print(f"Monster Strength: {self.combat_strength}, Hero Health: {hero.health_points}")
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("Monster defeated the hero!")
        else:
            hero.health_points -= self.combat_strength
            print(f"Hero's remaining health: {hero.health_points}")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()





