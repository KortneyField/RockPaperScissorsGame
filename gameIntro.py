import time, os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def game_intro():
    game_title = """
     ___        _       ___                      ___    _               
    | _ \___ __| |__   | _ \__ _ _ __ ___ _ _   / __|__(_)_________ _ _ 
    |   / _ / _| / /_  |  _/ _` | '_ / -_| '__  \__ / _| (_-(_-/ _ | '_|
    |_|_\___\__|_\_( ) |_| \__,_| .__\___|_|( ) |___\__|_/__/__\___|_|  
                   |/           | |         |/
    """

    game_subtitle = """
     ___ _            _   _ _ 
    / __| |_  ___ ___| |_| | |
    \__ | ' \/ _ / _ |  _|_|_|
    |___|_||_\___\___/\__(_(_)

    """

    author = "       by kortney field"


                                                                                                                            
                                                                                                                            
    clear_screen()

    print(game_title)
    print(author)

    time.sleep(2)

    print(game_subtitle) 

    input("    Press return to start!")

    clear_screen()

game_intro()

                                                                                                                           
                                                                                                                           
