import imp, string
imp.load_source('general_app_funcs', 'C:\\Users\\welcome\\Desktop\\MyFuncs\\general_app_funcs.py')
from general_app_funcs import *

from rocpapsci_app import RocPapSci

print("\n\n\nWelcome To the ROCK PAPER SCISSORS GAME!!")

game = RocPapSci()

START = True
while START:

    # collect names
    prompt = "\nEnter your username below\n>\t"
    p1, p2 = name_inp(prompt), name_inp(prompt)

    # assign names
    game.p1['name'] = p1
    game.p2['name'] = p2

    GAME_ON = True
    while GAME_ON:
        # player1 & player 2 start play
        prompt = f"{p1} RockPaperScissors?\n>\t"
        game.p1['current_guess'] = game.guess_inp(prompt)
        prompt = f"{p2} RockPaperScissors?\n>\t"
        game.p2['current_guess'] = game.guess_inp(prompt)

        # win check
        game.win_check(game.p1, game.p2)

        # score display
        game.scoreboard(game.p1, game.p2)

        ans = ask_next()

        if ans in 'yes':
            continue

        print("Thanks for playing!")
        GAME_ON = False
        START = False
