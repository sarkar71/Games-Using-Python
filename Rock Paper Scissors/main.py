import random
while True:
    name = input("Enter your name:")
    choices = ["rock", "paper", "scissor"]
    comp = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissor: ")
    if player == comp:
        print("computer: ", comp)
        print("player :", player)
        print("Tie!")
    elif player == 'rock':
        if comp == "paper":
            print("computer: ", comp)
            print("player: ", player)
            print("YOU WIN!")
        if comp == "scissor":
            print("computer: ", comp)
            print("player: ", player)
            print("YOU WIN!")
    elif player == 'scissor':
        if comp == "rock": 
            print("computer: ", comp)
            print("player: ", player)
            print("YOU LOSE!")
        if comp == "paper":
            print("computer: ", comp)
            print("player: ", player)
            print("YOU WIN!")
    elif player == 'paper':
        if comp == "scissor": 
            print("computer: ", comp)
            print("player: ", player)
            print("YOU LOSE!")
        if comp == "rock":
            print("computer: ", comp)
            print("player: ", player)
            print("YOU WIN!")
    play_again = input("Play Again? Enter your choice(Y/N) ").upper()
    if play_again != 'Y':
        break
print("Thanks for playing "+name+"!")
