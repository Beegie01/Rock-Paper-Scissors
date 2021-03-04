# import sys
# # adding MyFuncs package to Python's list of lookup paths
# sys.path.append('C:\\Users\\welcome\\Desktop\\MyFuncs')

from fave_app_funcs import name_inp, password_inp, ask_to_save

import random


class RocPapSci:

    def __init__(self):
        self.p1 = {'username': None, 'current_guess': None, 'games_won': 0, 'games_lost': 0, 'draws': 0}
        self.p2 = {'username': None, 'current_guess': None, 'games_won': 0, 'games_lost': 0, 'draws': 0}


    def guess_inp(self, prompt):

        acc_range = ['rock', 'r', 'paper', 'p', 'scissors', 's']

        while True:

            inp = input(prompt)

            if inp.lower() not in acc_range:
                print("Error: Invalid Entry!")
                continue

            if inp.lower() in ['r', 'rock']:
                inp = 'rock'
            elif inp.lower() in ['s', 'scissors']:
                inp = 'scissors'
            elif inp.lower() in ['p', 'paper']:
                inp = 'paper'

            return inp.lower()

    def win_check(self, p1, p2):
        # player 1 shows rock
        if self.p1['current_guess'] in ['r', 'rock']:

            if self.p2['current_guess'] in ['s', 'scissors']:
                print(f"\n\n{self.p1['username']} WINS!")
                self.p1['games_won'] += 1
                self.p2['games_lost'] += 1

            elif self.p2['current_guess'] in ['p', 'paper']:
                print(f"\n\n{self.p2['username']} WINS!")
                self.p2['games_won'] += 1
                self.p1['games_lost'] += 1

            else:
                print("\nSTALEMATE.\n\nNO WINNER!!")
                self.p1['draws'] += 1
                self.p2['draws'] += 1

        # player 1 shows paper
        elif self.p1['current_guess'] in ['p', 'paper']:

            if self.p2['current_guess'] in ['s', 'scissors']:
                print(f"\n\n{self.p2['username']} WINS!")
                self.p2['games_won'] += 1
                self.p1['games_lost'] += 1

            elif self.p2['current_guess'] in ['r', 'rock']:
                print(f"\n\n{self.p1['username']} WINS!")
                self.p1['games_won'] += 1
                self.p2['games_lost'] += 1

            else:
                print("\nSTALEMATE.\n\nNO WINNER!!")
                self.p1['draws'] += 1
                self.p2['draws'] += 1

        #player 1 shows a scissors
        elif self.p1['current_guess'] in ['s', 'scissors']:

            if self.p2['current_guess'] in ['p', 'paper']:
                print(f"\n\n{self.p1['username']} WINS!")
                self.p1['games_won'] += 1
                self.p2['games_lost'] += 1

            elif self.p2['current_guess'] in ['r', 'rock']:
                print(f"\n\n{self.p2['username']} WINS!")
                self.p2['games_won'] += 1
                self.p1['games_lost'] += 1

            else:
                print("\nSTALEMATE.\n\nNO WINNER!!")
                self.p1['draws'] += 1
                self.p2['draws'] += 1

    def scoreboard(self, p1, p2):

        print(f"\n\n{self.p1['username']}\n\tGAMES WON: {self.p1['games_won']}")
        print(f"\n\n{self.p2['username']}\n\tGAMES WON: {self.p2['games_won']}")
        print(f"\n\nGAMES DRAWN: {self.p1['draws']}")

    def save_details(self):

        SEP1, SEP2 = random.choice(['*', '-', '@', '&', '!']), random.choice(['%', '>', '<', '/', '|'])

        password = random.choice('abcdefgsh')+SEP1+str(random.randint(0,2000))+SEP2+random.choice('zywxvjknmpr')

        hand = open('C:\\Users\\welcome\\Desktop\\SimplePythonChallenges\\RockPaperScissors\\game_data.txt', 'a')

        # stored fields include
        # {password: [[username1, games_won, games_lost, games_drawn], [username2, games_won, games_lost, games_drawn]]}
        info = f"\n{dict( [ (password, [[self.p1['username'], self.p1['games_won'], self.p1['games_lost'], self.p1['draws'] ], [self.p2['username'], self.p2['games_won'], self.p2['games_lost'], self.p2['draws'] ]] )])}"

        hand.write(info)

        hand.close()

        print(f"\n\nGame saved!\nTo continue as {self.p1['username']} and {self.p2['username']} \nUse the password given below:\n{password}")

    def retrieve(self):

        # ask for the saved usernames
        prompt = "\nEnter password:\n>\t"
        pword = password_inp(prompt)


        # retrieve stored information from file
        hand = open('C:\\Users\\welcome\\Desktop\\SimplePythonChallenges\\RockPaperScissors\\game_data.txt')

        # file data contains a list of dictionary pairs
        file_data = hand.read().strip()

        # declaring useful array variables
        passwords = {}
        draws = []
        usernames = []
        wins = []
        losses = []


        # for each dictionary list in the file
        for n, dic in enumerate(file_data.split("\n")):
            # eliminating the first line containing the comment on column order
            if n == 0:
                continue

            # transform the dict saved in str format back into dict type
            di = eval(dic)

            # here, each key is a unique password
            # value is a list of list containing each player's records
            for k,v in di.items():

                # collecting and indexing the passwords from the file
                if k == pword:
                    print("Password Found!")

                    # here value is the list of lists containing each player's records
                    for each_player_rec in v:
                        # segmenting the information onto separate lists
                        usernames.append(each_player_rec[0]), wins.append(each_player_rec[1]), losses.append(each_player_rec[2]), draws.append(each_player_rec[3])

        # when username was collected
        if len(usernames) < 1:
            print(f"Password: {pword} is not on record\nPlease check for incorrect spelling")
            return "Not Found"

        else:
            # after match has been found
            # print(f"Users: {usernames}\nWins: {wins}\nLosses: {losses}")
            self.p1['username'], self.p2['username'] = usernames[0], usernames[1]
            self.p1['games_won'], self.p2['games_won'] = wins[0], wins[1]
            self.p1['games_lost'], self.p2['games_lost'] = losses[0], losses[1]
            self.p1['draws'], self.p2['draws'] = draws[0], draws[1]

            print("\n\nPlayers' records have been retrieved and restored!")
            return 'Done'

def game_mode():

    acc_range = ['new', 'n', 'c', 'cont']
    while True:
        # ask to start new or continue saved game
        prompt = "To start new game, enter 'new'\nTo continue saved game, enter 'cont'\n>\t"
        inp = input(prompt)

        if inp[0].lower() not in acc_range:
            print("\nPlease select 'new' or 'cont'!")
            continue

        return inp[0].lower()
