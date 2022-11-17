from random import randint

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

#Remember that lits aren't 1, 2, 3. They start at 0.

#declaring the variable computer, then using randint() to select randomly
#from the list

computer = options[randint(0,4)]

player = False

while player == False:
    #now player is being set to true, once they input something
    player = input("Choose: ")
    if player == computer:
        print("Draw")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose, ", computer, "covers ", player)
        elif computer == "Spock":
            print("You lose, ", computer, "vaporizes ", player)
        elif computer == "Lizard":
            print("you win, ", player, "crushes ", computer)
        else:
            print("You win, ", player, "crushes ", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("you lose ", computer, "cut ", player)
        elif computer == "Spock":
            print("You win, ", player, "disproves ", computer)
        elif computer == "Lizard":
            print("You lose, ", computer, "eats ", player)
        else:
            print("You win")
    elif player == "Scissors":
        if computer == "Rock":
            print("you lose, ", computer, "crushes ", player)
        elif computer == "Spock":
            print("You lose, ", computer, "smashes ", player)
        elif computer == "Lizard":
            print("You win, ", player, "decapitates ", computer)
        else:
            print("You win, ", player, "cuts ", computer)
    elif player == "Lizard":
        if computer == "Rock":
            print("you lose, ", computer, "crushes ", player)
        elif computer == "Paper":
            print("You win, ", player, "eats ", computer)
        elif computer == "Scissors":
            print("You lose, ", computer, "decapitates ", player)
        else:
            print("you win, ", player, "poisons ", computer)
    elif player == "Spock":
        if computer == "Rock":
            print("You win, ", player, "vaporizes ", computer)
        elif computer == "Scissors":
            print("You win, ", player, "smashes ", computer)
        elif computer == "Paper":
            print("You lose, ", computer, "disproves ", player)
        else:
            print("You lose, ", computer, "poisons ", player)
    else:
        print("Invalid play")

    player = False
    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    computer = options[randint(0,4)]
