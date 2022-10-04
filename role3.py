#last part of the game
print("you see there was something inside the ground so you start digging.")
print("you found an axe in the ground near the tree with blood on it and a t-shirt with blood stains on it.")
print("you look around and you see a small house near by.")
print("you walk towards it and peek inside the window.")
print("you see someone's shadow.")
response = ""
while response not in yes_no:
    response = input("Would you like to enter inside the house?\nyes/no\n")
    if response == "yes":
        print("You enter into the house, catch the criminal, send the criminal to jail and you got promoted.\n")
    elif response == "no":
        print("You are not ready for this mystery case. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")