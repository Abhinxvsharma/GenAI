import random

choices = ["rock", "paper", "scissors"]

player = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("You chose:", player)
print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

else:
    print("Computer wins!")
