import random
import functions
import os
import platform
from hero import Hero
from monster import Monster

# All player references have been renamed to Hero given assignment 2 instructions.
# User input to hero/monster strength has been removed, given assignment requirements of rolling for hero/monster strength/health.

# Assignment 2 - #9.
# Start by printing OS info - and additional platform info (useful and neat)
print(f"Operating System Info: {os.name}")
print(f"Platform Info: {platform.system()}")
# Assignment 2 - #10.
print(f"Python Version: {platform.python_version()}")

hero = Hero()
monster = Monster()

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons and Loot
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the Hero
num_stars = 0

# Lazy way to avoid check created during lab
input_invalid = False

if not input_invalid:

    # Auto rolling for hero and monster stats
    print(f"Hero has rolled {hero.combat_strength} combat strength and {hero.health_points} health points.")
    print(f"Monster has rolled {monster.combat_strength} combat strength and {monster.health_points} health points.")

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    # Will create a local var by the same name using the global combat_strength
    hero.combat_strength = min(6, (hero.combat_strength + weapon_roll))
    print(f"    |    The hero\'s weapon is {weapons[weapon_roll - 1]}" )

    # Lab 06 - Question 5b
    functions.adjust_combat_strength(hero.combat_strength, monster.combat_strength)

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Rolling for health points removed given assignment 2 requirements.

    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Use Loot
    belt, health_points = functions.use_loot(belt, hero.health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Hero vs Monster's strength
    print("    |    --- You are matched in strength: " + str(hero.combat_strength == monster.combat_strength))

    # Check the Hero's overall strength and health
    print("    |    --- You have a strong Hero: " + str((hero.combat_strength + health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)

    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power, but ensure its never above 6.
    temp_strength = monster.combat_strength + monster_powers[power_roll]
    monster.combat_strength = min(6, temp_strength)
    print("    |    The monster's combat strength is now " + str(
        monster.combat_strength) + " using the " + power_roll + " magic power")

    # Lab Week 06 - Question 6
    # Initialize the number of dream levels
    # Inconsistent; will sometimes produce a value error (?)
    num_dream_lvls = -1
    running = True

    while running:
        print("    |", end="    ")
        user_input = input("How many dream levels do you want to go down? (Enter a number 0-3)")

        try:
            num_dream_lvls = int(user_input)

            if 0 <= num_dream_lvls <= 3:
                hero.health_points -= 1
                crazy_level = functions.inception_dream(num_dream_lvls)
                monster.combat_strength += crazy_level
                print("combat strength: " + str(hero.combat_strength))
                print("health points: " + str(hero.health_points))
                print("num_dream_lvls: ", num_dream_lvls)
                running = False
            #   If the value entered was not an integer, set the number of dream levels to -1 and loop again
            else:
                print("Number entered must be a whole number between 0-3 inclusive, try again")
                continue

        except ValueError:
            print("Invalid input (ValueError)! Please enter a whole number between 0 and 3.")
            continue

    # Removed redundant check here

    # Fight Sequence
    # Loop while the monster and the hero are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while hero.health_points > 0 and monster.health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        # Lab 5: Question 5:
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            hero.hero_attacks(monster)
            if monster.health_points == 0:
                num_stars = 3
                break
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                monster.monster_attacks(hero)
                if hero.health_points == 0:
                    num_stars = 1
                    break
                else:
                    num_stars = 2
        else:
            # This is the monster striking first if roll is higher
            print("    |", end="    ")
            input("The Monster strikes first (Press enter)")
            monster.monster_attacks(hero)
            if hero.health_points == 0:
                num_stars = 1
                break
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                hero.hero_attacks(monster)
                if monster.health_points == 0:
                    num_stars = 3
                    break
                else:
                    num_stars = 2

    if hero.health_points > 0:
        print("Hero wins!")
        winner = "Hero"
    else:
        print("Monster wins!")
        winner = "Monster"

    print(f"{winner} wins the battle!")


    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")

        hero_name = input("Enter your Hero's name (in two words)")
        name_split = hero_name.split()

        if len(name_split) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name_split[0].isalpha() or not name_split[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name_split[0][0:2:1] + name_split[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")

        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)       


