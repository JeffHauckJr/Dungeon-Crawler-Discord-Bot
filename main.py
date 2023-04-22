import random
import time


class Challenger:
    def __init__(self, name, profession, health):
        self.name = name
        self.health = health
        self.profession = profession

    def intro(self):
        print(f"Hello {self.name}. Welcome to Wicked Dungeon.")


def pause():
    time.sleep(1)


def challenger_selection():
    while True:
        profession = input("Select a class (Warrior or Mage): ")
        if profession.lower() in ["warrior", "mage"]:
            break
        print("Invalid profession. Please choose again.")
    if profession.lower() == "warrior":
        health = 100
    else:
        health = 75

    return (health, profession)


def random_encounter(challenger):
    print("Welcome to your first encounter!")
    monster_name = "Goblin"
    monster_health = random.randint(50, 100)
    print(f"A {monster_name} with {monster_health} health appears!")

    # Fight against the monster
    while True:
        user_choice = input(
            "What would you like to do? (Type 'attack' or 'escape'): ")
        if user_choice.lower() == "attack":
            print(f"{challenger.name} attacks the enemy!")
            pause()
            print(f"{monster_name} attacks {challenger.name}!")
            pause()
            challenger.health -= random.randint(5, 15)
            print(f"{challenger.name} has {challenger.health} health remaining.")
            if challenger.health <= 0:
                print(f"{challenger.name} has been defeated by {monster_name}!")
                break
            print(f"{challenger.name} attacks {monster_name}!")
            pause()
            monster_health -= random.randint(10, 20)
            print(f"{monster_name} has {monster_health} health remaining.")
            if monster_health <= 0:
                print(f"{challenger.name} has defeated {monster_name}!")
                break
            # logic for attacking the enemy
        elif user_choice.lower() == "escape":
            print(f"{challenger.name} attempts to escape!")
            escape_chance = random.randint(1, 2)
            if escape_chance == 1:
                print(f"{challenger.name} has successfully escaped!")
            else:
                print("You have failed to escape. The battle continues.")
                challenger.health - random.randint(5, 10)
                print(
                    f"{challenger.name} has taken damage on the escape attempt. {challenger.name} is now at {challenger.health} health")
                if challenger.health <= 0:
                    print(f"{challenger.name} has been defeated by {monster_name}")
                    break
            # logic for attempting to escape
            break
        else:
            print("Invalid choice. Please choose 'attack' or 'escape'.")


def main():
    name = input("Who is your challenger: ").capitalize()
    health, profession = challenger_selection()
    challenger = Challenger(name, profession, health)
    print(
        f"You have selected {challenger.profession}. This class has a base health of {challenger.health}")
    challenger.intro()

    user_input = input(
        "Would you like to enter the world of Wicked Dungeon? Remember, you can always exit by entering 'exit': ")
    while user_input.lower() != "exit":
        if user_input.lower() == "yes":
            random_encounter(challenger)
            if challenger.health <= 0:
                print("You are unable to continue fighting.")
                break
        else:
            print("We did not recognize that input.")
        user_input = input(
            "Would you like to enter another encounter? Enter 'yes' to continue or 'exit' to quit: ")

    print("Thanks for playing!")


main()
