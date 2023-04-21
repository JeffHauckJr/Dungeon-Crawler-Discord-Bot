import random

class Challenger:
    def __init__(self, name, profession, health):
        self.name = name
        self.health = health
        self.profession = profession

    def intro(self):
        print(f"Hello {self.name}. Welcome to Wicked Dungeon.")

def challenger_selection():
    while True:
        profession = input("Select a class (Warrior or Mage): ")
        if profession.lower() in ["warrior", "mage"]:
            break
        print("Invalid profession. Please choose again.")
    if profession.lower == "warrior":
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
        print(f"{monster_name} attacks {challenger.name}!")
        challenger.health -= random.randint(5, 15)
        print(f"{challenger.name} has {challenger.health} health remaining.")
        if challenger.health <= 0:
            print(f"{challenger.name} has been defeated by {monster_name}!")
            break
        print(f"{challenger.name} attacks {monster_name}!")
        monster_health -= random.randint(10, 20)
        print(f"{monster_name} has {monster_health} health remaining.")
        if monster_health <= 0:
            print(f"{challenger.name} has defeated {monster_name}!")
            break


def main():
    name = input("Who is your challenger: ")
    health, profession = challenger_selection()
    challenger = Challenger(name, profession, health)
    print(
        f"You have selected {challenger.profession}. This class has a base health of {challenger.health}")
    challenger.intro()

    user_input = input("Would you like to enter the world of Wicked Dungeon? Remember, you can always exit by entering 'exit': ")
    while user_input.lower() != "exit":
        if user_input.lower() == "yes":
            random_encounter(challenger)
        else:
            print("We did not recognize that input.")
        user_input = input("Would you like to enter another encounter? Enter 'yes' to continue or 'exit' to quit: ")

    print("Thanks for playing!")


main()
