import random

options = ["rock", "paper", "scissors"]

user = input("Choose rock, paper or scissors: ").lower()
computer = random.choice(options)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win!")
else:
    print("You lose!")

