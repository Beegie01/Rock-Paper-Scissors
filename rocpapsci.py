# import sys, string

# # adding MyFuncs package to Python's list of lookup paths
# sys.path.append('C:\\Users\\welcome\\Desktop\\MyFuncs')

from fave_app_funcs import *

from rocpapsci_app import RocPapSci

print("\n\n\nWelcome To the ROCK PAPER SCISSORS GAME!!")

# game object for starting afresh
game = RocPapSci()

# game object for continuing with saved records
contd = RocPapSci()

PLAY = True
while PLAY:
    # ask to start new game or continue saved game
    mode = game_mode()

    if mode == 'c':

        CONTD = True
        while CONTD:
            result = contd.retrieve()

            if result == 'Not Found':
                CONTD = False
                continue

            GAME_ON = True
            while GAME_ON:
                # player1 & player 2 continue play
                prompt = f"{contd.p1['username']} \nRock, Paper, Scissors?\n>\t"
                contd.p1['current_guess'] = contd.guess_inp(prompt)

                prompt = f"{contd.p2['username']} \nRock, Paper, Scissors?\n>\t"
                contd.p2['current_guess'] = contd.guess_inp(prompt)

                # win check
                contd.win_check(contd.p1, contd.p2)

                # score display
                contd.scoreboard(contd.p1, contd.p2)

                ans = ask_next()

                if ans in 'yes':
                    continue

                if ask_to_save():
                    # save game details before exiting
                    contd.save_details()

                print("\n\nExiting game...\nThanks for playing!")
                PLAY, GAME_ON, CONTD = False, False, False


    else:

        START = True
        while START:

            # collect names
            prompt1 = "\nFirst player, please enter your username below\n>\t"
            prompt2 = "\nSecond player, please enter your username below\n>\t"
            inp_name1, inp_name2 = name_inp(prompt1), name_inp(prompt2)

            # assign names
            game.p1['username'] = inp_name1
            game.p2['username'] = inp_name2

            GAME_ON = True
            while GAME_ON:
                # player1 & player 2 start play
                prompt = f"{game.p1['username']} Rock, Paper, Scissors?\n>\t"
                game.p1['current_guess'] = game.guess_inp(prompt)

                prompt = f"{game.p2['username']} Rock, Paper, Scissors?\n>\t"
                game.p2['current_guess'] = game.guess_inp(prompt)

                # win check
                game.win_check(game.p1, game.p2)

                # score display
                game.scoreboard(game.p1, game.p2)

                # ask to continue
                ans = ask_next()

                if ans in 'yes':
                    continue

                if ask_to_save():
                    # save game details before exiting
                    game.save_details()

                print("\n\nExiting game...\nThanks for playing!")
                PLAY, GAME_ON, START = False, False, False
