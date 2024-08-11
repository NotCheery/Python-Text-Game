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
    print(f"Character status: \nCharm: {charm}/5 ")
    print(f"Smart: {smart}/5 ")
    print(f"Friendliness: {friendliness}/5 ")
    print(f"Luck: {luck}/5 ")
    print(f"Inventory: {inventory}")

def game1():
        #Print out the scene after name
    print(f"Hi! You are working as a cashier at a local cafe.\nIt's nearly 10 pm and there's no one around.")
    print(f"Suddenly, you hear the door open and noitce a man walk in.\nYou: Hi, welcome to Rosy Cafe!")
    
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
    print("You are in basement.\nSelect which rooms you want to explore.")
    answer = int(input("1 = Kitchen\n2 = Storage\n\nEnter a number: "))
    if answer == 1:
        kitchen()
    else:
        storage()
        
def kitchen():
    answer = int(input("You are in the kitchen. Take a look at the . . .\n1 = Fridge\n2 = Sink\n3 = Return to main room"))
    if answer == 1:
        open_inventory = int(input("You look closer and find a note. The note has been added to your inventory. To open inventory and character stats, press and enter 1: "))
        if open_inventory == 1:
            character_stats()
    elif answer == 2:
        print("You find nothing interesting. To return to kitchen, enter 1.\n To return to the main room, enter 2.")
        #input and consider while loop?
    else:
        basement()
        
def storage():
    print("You are in the storage room. You look around and you notice there's a safe. You need code **** to unlock.")
    answer = int(input("You may enter code or enter 1 to return to the main room: "))
    if answer == 1:
        basement()
    elif answer == 1786:
        print("You've unlocked the safe! You have obtained a key.")
        smart += 1
    else:
        print("Invalid entry. Try again!")
        storage()
    
if __name__ == "__main__":
    game1()