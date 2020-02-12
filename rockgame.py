import random

WIN_LIST_RPS = [('ROCK', 'SCISSORS'),
                ('SCISSORS', 'PAPER'),
                ('PAPER', 'ROCK')]

SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']

selections_list = SELECTIONS_LIST_RPS

win_list = WIN_LIST_RPS

computer_selection = random.choice(selections_list)

def user_input():
    user_input = input("Play your hand:  ")
    user_input = user_input.upper()

def start_game(player_hand):
    print("*** Let's Play the Rock Paper Scissor Game ***")
    print(" ")
    print("Choose ROCK, PAPER or SCISSOR")
    player_hand = user_input()

def match (user_input, computer_selection):
    match = user_input, computer_selection

def competition(match):
    if user_input == computer_selection:
        print("It is a Tie!")
    elif match in win_list:
        print("\nResult: The power of {} beats {}! You won!".format(user_input, computer_selection))
    else:
        print("\nResult: The power of {} is stronger than {}! You lost!".format(computer_selection, user_input))




start_game(user_input)
competition(match)
