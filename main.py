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

    return(health, profession)

def main():
    name = input("Who is your challenger: ")
    health, profession = challenger_selection()
    challenger = Challenger(name, profession, health)
    print(f"You have selected {challenger.profession}. This class has a base health of {challenger.health}")
    challenger.intro()

    while True:
        user_input = input("Enter a command (or type 'exit' to quit): ")
        if user_input == "exit":
            break 
main()