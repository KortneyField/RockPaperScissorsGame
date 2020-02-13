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



def play():
    human = 0
    computer = 0
    
    play_num = int(input("How many wins do you want to play to?:  "))

    while (human <= play_num or computer <= play_num):
        
        c_hand=random.choice(selections_list).upper()
        p_hand=input("Choose rock, paper or scissors: ").upper()

        if play == "yes":
            if p_hand == c_hand:
                print("It is a Tie")
            elif p_hand == 'ROCK':
                if c_hand == 'PAPER':
                    print("Paper covers rock, YOU LOST")
                    computer += 1
                elif c_hand == 'SCISSORS':
                    print("Rock beats Scissors, YOU WIN")
                    human += 1
            elif p_hand == 'PAPER':
                if c_hand == 'ROCK':
                    print("Paper covers Rock, YOU WIN")
                    human += 1
                elif c_hand == 'SCISSORS':
                    print("Scissors cut Paper, YOU LOST")
                    computer += 1
            elif p_hand == 'SCISSORS':
                if c_hand == 'PAPER':
                    print("Scissors cut Paper, YOU WIN")
                    human += 1
                elif c_hand == 'ROCK':
                    print("Rock beats Scissors, YOU LOST")
                    computer += 1
            
            print("The Score>>>")
            print("    HUMAN = {}".format(human))
            print("  COMPTER = {}".format(computer))
        
        if play == "no":
            play == False

    else:
        print("game over")

main()
