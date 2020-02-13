import random
import sys

SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']
selections_list = SELECTIONS_LIST_RPS
c_hand=random.choice(selections_list).upper()

def main():
    print(" **************************")
    print("    Welcome to the Game")
    print(" **************************")
    print()
    play()

def play_amount():
    play_num = int(input("Best out of how many rounds (must be an odd #):  "))
    if (play_num % 2) != 0:  
        return play_num  
    else:  
        play_num = input("INVALID: Must pick a odd number. ")

def play():
    human = 0
    computer = 0
    
    n = play_amount()
    wins = 0  
    
    while (wins < n):
        c_hand=random.choice(selections_list).upper()
        p_hand=input("Choose rock, paper or scissors: ").upper()
        if: 
            p_hand = input("INVALID- Try again:")
        if p_hand == c_hand:
            print("It is a Tie")
        elif p_hand == 'ROCK':
            if c_hand == 'PAPER':
                print("Paper covers rock, YOU LOST")
                computer += 1
                wins += 1
            elif c_hand == 'SCISSORS':
                print("Rock beats Scissors, YOU WIN")
                human += 1
                wins += 1
        elif p_hand == 'PAPER':
            if c_hand == 'ROCK':
                print("Paper covers Rock, YOU WIN")
                human += 1
                wins += 1
            elif c_hand == 'SCISSORS':
                print("Scissors cut Paper, YOU LOST")
                computer += 1
                wins += 1
        elif p_hand == 'SCISSORS':
            if c_hand == 'PAPER':
                print("Scissors cut Paper, YOU WIN")
                human += 1
                wins += 1
            elif c_hand == 'ROCK':
                print("Rock beats Scissors, YOU LOST")
                computer += 1
        
        
        print("The Score>>>")
        print("    HUMAN = {}".format(human))
        print("  COMPTER = {}".format(computer))

main()
