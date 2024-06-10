#This is a text-based adventure game. 
#alice explores the cafe, but the cafe is not what it seems.
#Tip: Use numbers for choices.
def item():
  items = ["1. choco bar", "2. star coin", "3. diary"]
  print(items)
  user = input("Enter (1/2/3): ")
  if user == "1":
    print("Yum\n\n Ending: You were poisoned.")
  elif user == "2":
    print("\nYou selected a star coin.")
  else:
    print("\nYou have selected diary.")
    diary()

def diary():
  code = input("Looks like the diary has a lock in it. You have to enter three digits to unlock it. Enter the code with no spaces: ")
  if code == "013":
    print("\nYou unlocked the diary.\n")
    print("\nAs you look through the pages, you notice that there's a letter hidden between the pages. The letter had prints of lipstick stain on it.\n\nIt's a love letter!\n\nEagerly, you opened the letter and realized that it was addressed to the barista of the cafe.\n\nHowever, something peculiar caught your eye. The letter date is the year of 1888, but the current year is 1986 . . .\n\n You return upstairs.")

  else:
    print("\nInvalid entry. Recall what was the last thing NPC said to you.")

def menu():
  options = {
    "1": "Coffee",
    "2": "Cheesecake",
    "3": "Muffin"
  }
  print(options)
  input("\nEnter(1/2/3): ")
  print("NPC: Enjoy!")
  
  
def cafe():
  print("\nYou have entered the Cafe.\n")
  response = input("NPC: Hello! What can I help you with?\n\n 1.Menu \n 2.Work \n 3.Ignore \n\nPlease enter your choice: ")

  if response == "1":
    menu()
  elif response == "2":
    work()
  else:
    print("You chose to ignore . . .")

def work():
  
  print("\nYou worked for the day. The cafe closes at 11 pm and right now it's 10:01 pm. You notice that it's quite dark already and wonder how you'll get home. At the entrance, a man walks in and orders a cheesecake. As you prepare you cut a slice of the cake, you notice the man's ring has the same star symbol as the picture at the manager's desk. You served a slice of cheesecake and received 10 coins as a tip.\n")

  print("NPC: Go0d job at work today. Since there's no1 a lot of customers today, why don't you take a look at some item3 you can purchase in the basement?\n")

  response = input("Enter basement? \n 1.Yes \n 2.No \nPlease enter (1/2): ")
  if response == "1":
    print("\nYou've entered the basement. . .")
    print("You have come across some interesting items.\n")
    item()
  else:
    print("You have completed today's work!")
    print(" Ending: Employee!")


def home():
  print("You have entered your home. You find a mysterious letter on your table. You open the letter and proceed to read it.\n\nDear friend,\n\n It's been a long time. How are you doing?\n\n Hope everything is alright. How’s your day? For me, I went on a stroll to my garden. The garden nearby has the most beautiful flowers. You know my favorite flower is Marigold and it was filled with such beautiful flowers.\n\n Anyways, my birthday is coming up and I hope to see you there soon!\n\nSincerely,\nMelissa.")
  print("\nAs you look up from your letter, your home does not look like home anymore. Rather you are in a strange room with two doors. Which door do you go to, left or right?")


#WELCOME
print("Welcome to Alice's Adventures!\n")
user_input = input("Where to explore? \n 1.Cafe (This option works.) \n 2.Home \n 3.Info \n 4.Exit \n\nPlease enter (1/2/3/4): ")

if user_input == "1":
  cafe()
elif user_input == "2":
  home()
else:
  print("This is unavailable at the moment.")