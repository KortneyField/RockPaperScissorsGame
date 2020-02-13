import random
import os

WIN_LIST_RPS = [('ROCK', 'SCISSORS'),
                ('SCISSORS', 'PAPER'),
                ('PAPER', 'ROCK')]

SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']

selections_list = SELECTIONS_LIST_RPS

win_list = WIN_LIST_RPS

computer_selection = random.choice(selections_list)



def start_game():
    print("*** Let's Play the Rock Paper Scissor Game ***")
    print(" ")
    print("Choose ROCK, PAPER or SCISSOR")

def user_input():
    user_input = input("Play your hand:  ")
    return user_input
    #print("You are fighting with {}".format(user_input))

def match ():
    user_input=user_input()
    computer_selection=random.choice(selections_list)
    match = hand, computer_selection
    print("You are {}, going against {}".format(hand,computer_selection))

def competition(match):
    if user_input == computer_selection:
        print("It is a Tie!")
    elif match in win_list:
        print("\nResult: The power of {} beats {}! You won!".format(user_input, computer_selection))
    else:
        print("\nResult: The power of {} is stronger than {}! You lost!".format(computer_selection, user_input))

def play_again():
    play = input("Want to play again? y/n:  ")
    if play.lower() == 'p':
        main()

def main():
    #os.system("CLEAR")
    start_game()
    user_input()
    match()
    competition(match)

main()
