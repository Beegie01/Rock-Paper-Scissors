class RocPapSci:

    def __init__(self):
        self.p1 = {'name': None, 'current_guess': None, 'games_won': 0, 'games_lost': 0}
        self.p2 = {'name': None, 'current_guess': None, 'games_won': 0, 'games_lost': 0}
        self.draws = 0


    def guess_inp(self, prompt):

        acc_range = 'rock paper scissors'

        while True:

            inp = input(prompt)

            if inp.lower() not in acc_range:
                print("Error: Invalid Entry!")
                continue

            if inp.lower() in 'rock':
                inp = 'rock'
            elif inp.lower() in 'scissors':
                inp = 'scissors'
            elif inp.lower() in 'paper':
                inp = 'paper'

            return inp.lower()

    def win_check(self, p1, p2):
        # player 1 shows rock
        if self.p1['current_guess'] in 'rock':

            if self.p2['current_guess'] in 'scissors':
                print(f"\n\n{self.p1['name']} WINS!")
                self.p1['games_won'] += 1
                self.p2['games_lost'] += 1

            elif self.p2['current_guess'] in 'paper':
                print(f"\n\n{self.p2['name']} WINS!")
                self.p2['games_won'] += 1
                self.p1['games_lost'] += 1

            else:
                print("\nSTALEMATE.\n\nNO WINNER!!")
                self.draws += 1

        # player 1 shows paper
        elif self.p1['current_guess'] in 'paper':

            if self.p2['current_guess'] in 'scissors':
                print(f"\n\n{self.p2['name']} WINS!")
                self.p2['games_won'] += 1
                self.p1['games_lost'] += 1

            elif self.p2['current_guess'] in 'rock':
                print(f"\n\n{self.p1['name']} WINS!")
                self.p1['games_won'] += 1
                self.p2['games_lost'] += 1

            else:
                print("\nSTALEMATE.\n\nNO WINNER!!")
                self.draws += 1

        #player 1 shows a scissors
        elif self.p1['current_guess'] in 'scissors':

            if self.p2['current_guess'] in 'paper':
                print(f"\n\n{self.p1['name']} WINS!")
                self.p1['games_won'] += 1
                self.p2['games_lost'] += 1

            elif self.p2['current_guess'] in 'rock':
                print(f"\n\n{self.p2['name']} WINS!")
                self.p2['games_won'] += 1
                self.p1['games_lost'] += 1

            else:
                print("\nSTALEMATE.\n\nNO WINNER!!")
                self.draws += 1

    def scoreboard(self, p1, p2):

        print(f"\n\n{self.p1['name']}\n\tGAMES WON: {self.p1['games_won']}")
        print(f"\n\n{self.p2['name']}\n\tGAMES WON: {self.p2['games_won']}")
        print(f"\n\nGAMES DRAWN: {self.draws}")
