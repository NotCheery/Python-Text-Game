#Started on this the middle of July and late July

#Text Adventure Based Game in Python!
# A simple Text Based Game. A collection of scenarios where you aim to escape by luck and right choices.

#Stats may change based on your choices.
def character_stats():
    charm = 0
    smart = 0
    friendliness = 0
    luck = 0
    inventory = {}
    
    #Display character stats when called
    print(f"Charm: {charm} ")
    print(f"Smart: {smart} ")
    print(f"Friendliness: {friendliness} ")
    print(f"Luck: {luck} ")
    print(f"Inventory: {inventory}")

def game1(name):
        #Print out the scene after name
    print(f"Hi {name}! You are working as a cashier at a local cafe.\nIt's nearly 10 pm and there's no one around.")
    print(f"Suddenly, you hear the door open and noitce a man walk in.\n{name}: Hi, welcome to Rosy Cafe!")
    
    #Can increase luck points
    print(f"The man: Want to play a game of rock, papers, scissors?")

    
    #your response to play rock paper scissors
    response = int(input(f"Enter a number: \n1 = Yes\n2 = No\n"))
    ask_again = 2 #number of times the man will ask to play
    
    #While loop based on your response
    while ask_again > 0:
        if response == 1:
            #What happens when you play? What happens when you win? Obtain key. Lose?
            print("Good luck!")
            break
        else:
            response = int(input(f"Enter a number: \n1 = Yes\n2 = No\n"))
            ask_again -= 1
    
    #What happens after you refuse to play 3 times?
    if ask_again == 0:
        print("The man goes crazy and takes out a pocket knife!")
        response2 = int(input(f"Enter a number: \n1 = Hide in basement\n2 = Run outside\n"))
        if response2 == 1:
            basement() #call to basement scenario
        else:
            print("You got hit by an oncoming car and died. You've unlocked ending 1.")
            print("\nEnding: Hit by a car")

#Scenario 2    
def basement():
    inventory = {}
    print("You are in basement.\nYou find a note. Open note?")
    answer = int(input("1 = Yes\n2 = NoEnter a number: "))
    if answer == 1:
        Note_1 = "Hide 1"
        print("Hide - 1\nNote 1 has been added to your inventory.")
    
if __name__ == "__main__":
    #Enter your name
    user_name = str(input("Hello there! What is your name? "))
    game1(user_name)