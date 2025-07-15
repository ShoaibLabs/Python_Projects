import os
import time
from random import randint


def clear():
    os.system("cls" if os.name == "nt" else "clear")


choices = {
    'r': 1,
    'rock': 1,
    'stone': 1,
    '1': 1,
    '1.0': 1,
    'p': 0,
    'paper': 0,
    '2': 0,
    '2.0': 0,
    's': -1,
    'scissors': -1,
    '3': -1,
    '3.0': -1,
}

items = {
    1: "Rock",
    0: "Paper",
    -1: "Scissors"
}


def user_guess():
    while True:
        clear()
        userchoice = input("Enter your choice\nRock/Paper/Scissors or q to quit: ").lower().strip()
        print()

        if userchoice in ['q', 'quit']:
            print("Exiting the program...")
            exit()
        elif userchoice in choices:
            return userchoice
        else:
            print("Invalid Value. Try again!")
            time.sleep(0.4)


def result(userchoice, player_score, computer_score):
    comp = randint(-1, 1)
    user = choices[userchoice]

    print(f"Computer's choice: {items[comp]}")
    time.sleep(0.4)
    print(f"Your choice: {items[user]}\n")
    time.sleep(0.4)

    if user == comp:
        print("It's a Draw!\n")
    else:
        if (comp == 1 and user == 0) or (comp == 0 and user == -1) or (comp == -1 and user == 1):
            player_score += 1
            print("You Won!\n")
        else:
            computer_score += 1
            print("Computer Won!\n")

    print(f"Your score: {player_score}\nComputer's score: {computer_score}\n")
    time.sleep(0.4)
    input("Press Enter to continue...")

    return player_score, computer_score


player_score = 0
computer_score = 0

while True:
    userchoice = user_guess()
    player_score, computer_score = result(userchoice, player_score, computer_score)
