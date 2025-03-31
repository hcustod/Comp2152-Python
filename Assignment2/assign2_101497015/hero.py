from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()  # Call parent constructor

    def hero_attacks(self, monster):
        ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
        print(ascii_image)
        print("Hero attacks Monster!")
        print(f"Hero Strength: {self.combat_strength}, Monster Health: {monster.health_points}")

        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("Hero defeated the monster!")
        else:
            monster.health_points -= self.combat_strength
            print(f"Monster's remaining health: {monster.health_points}")

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()  # Call parent destructor
