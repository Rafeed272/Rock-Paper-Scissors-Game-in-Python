import random

choices = ['rock', 'paper', 'scissor']

rounds = int(input("How many rounds do you want to play?: "))

for _ in range(rounds):

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissor?: ").lower()

    print("Computer: "+computer)
    print("Player: "+player)

    if player == computer:
        print("DRAW!")
    elif player == "rock":
        if computer == "paper":
            print("You lost! :(")
        else:
            print("You won!")

    elif player == "scissor":
        if computer == "rock":
            print("You lost! :(")
        else:
            print("You won!")

    elif player == "paper":
        if computer == "scissor":
            print("You lost! :(")
        else:
            print("You won!")