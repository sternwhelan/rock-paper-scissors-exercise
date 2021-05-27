# game.py

import random

import os

import dotenv

dotenv.load_dotenv()

player_name = os.getenv("player_name")


print("-------------------")
print("Welcome to a game of rock, paper, scissors" + player_name + "!")
print("-------------------")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")


print("USER CHOICE: ", user_choice)


if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Good Choice!")
else:
    print("OOPS, invalid input. Please try again.")
    exit()


valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)

#USER WINNING AND TIE SCENARIOS

if user_choice == computer_choice:
    print("It's a tie, try again!")

elif (user_choice == "scissors") and (computer_choice == "paper"):
     print("Scissors cuts paper, you win!")
elif (user_choice == "rock") and (computer_choice == "scissors"):
    print("rock smashes scissors, you win!")
elif (user_choice == "paper") and (computer_choice == "rock"):
    print("Paper covers rock, you win!")

#COMPUTER WINNING SCENARIOS

elif (user_choice == "scissors") and (computer_choice == "rock"):
    print("rock smashes scissors, you lose!")
elif (user_choice == "rock") and (computer_choice == "paper"):
    print("paper covers rock, you lose!")
elif (user_choice == "paper") and (computer_choice == "scissors"):
    print("Scissors cuts paper, you lose!")

print("THIS IS THE END OF OUR GAME. THANKS FOR PLAYING. PLEASE PLAY AGAIN!")


#replay = input("Would you like to play again? y/n: ")
#while(replay != "n") and (replay != "y"):
