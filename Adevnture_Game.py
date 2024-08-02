#Started on this the middle of July and late July

#Text Adventure Based Game in Python!
# A simple Text Based Game. A collection of scenarios where you aim to escape by luck and right choices.
# Scene 1 As you are working in a shift at the cafe, you encounter a man. A man asks you to play a game of rock, paper, scissors.
# You lose... you die.
# You win (Escaped)

def game1(name):
    #Print out the scene
    print(f"Hi {name}! You are working as a cashier at a local cafe.")
    print(f"It's nearly 10 pm and there's no one around.")
    print(f"Suddenly, you hear the door open and noitce a man walk in.\n{name}: Hi, welcome to Rosy Cafe!")
    
    print(f"The man: Want to play a game of rock, papers, scissors?")
    
    #your response to play rock paper scissors
    response = int(input(f"Enter a number: \n1 = Yes\n2 = No\n"))
    ask_again = 3 #number of times the man will ask to play
    
    #While loop based on your response
    while ask_again > 0:
        if response == 1:
            print("Good luck!")
            break
        else:
            response = int(input(f"Enter a number: \n1 = Yes\n2 = No\n"))
            ask_again -= 1
    
    if ask_again == 0:
        print("The man goes crazy and takes out a pocket knife!")
        
    
    

if __name__ == "__main__":
    user_name = str(input("Hello there! What is your name? "))
    game1(user_name)