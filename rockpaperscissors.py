from random import randint

choices = ["Rock", "Paper", "Scissors"]

computer = choices[randint(0,2)]

player = False

while player == False:

    player = input("Type Rock, Paper, Scissors To Play.. or End to end the game!")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "End":
        print("The game finished.. See You Soon :)")  
        break
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = choices[randint(0,2)]
    
    