player1 = input("Player 1: ")
player2 = input("Player 2: ")

if player1 == player2:
    print("Draw!")

elif player1 == "rock" and player2 == "scissors":
    print("Player 1 Won!")

elif player1 == "scissors" and player2 == "paper":
    print("Player 1 Won!")

elif player1 == "paper" and player2 == "rock":
    print("Player 1 Won!")

elif player2 == "rock" and player1 == "scissors":
    print("Player 2 Won!")

elif player2 == "scissors" and player1 == "paper":
    print("Player 2 Won!")

elif player2 == "paper" and player1 == "rock":
    print("Player 2 Won!")
