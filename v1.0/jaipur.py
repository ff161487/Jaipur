from random import seed, shuffle
from pdb import set_trace


class Jaipur:
    def __init__(self, players, seed_g=None):
        # Attributes that accept input parameters
        self.seed = seed_g
        seed(self.seed)
        self.players = players

        # Initialize attributes related to card piles
        self.draw_pile = ['Diamonds'] * 6 + ['Gold'] * 6 + ['Silver'] * 6 + ['Cloth'] * 8 + ['Spice'] * 8 +\
                         ['Leather'] * 10 + ['Camels'] * 8
        shuffle(self.draw_pile)
        self.board = ['Camels'] * 3 + self.draw_pile[:2]
        self.draw_pile = self.draw_pile[2:]

        # Attributes related to the game process
        self.history = []

        # Initialize attributes related to rewards/coins
        self.coins = {'Diamonds': [7, 7, 5, 5, 5], 'Gold': [6, 6, 5, 5, 5], 'Silver': [5, 5, 5, 5, 5], 'Cloth': [5, 3,
            3, 2, 2, 1, 1], 'Spice': [5, 3, 3, 2, 2, 1, 1], 'Leather': [4, 3, 2, 1, 1, 1, 1, 1, 1], 'R3': [1, 1, 2, 2,
            2, 3, 3], 'R4': [4, 4, 5, 5, 6, 6], 'R5': [8, 8, 9, 10, 10], 'Camel': [5]}
        shuffle(self.coins['R3'])
        shuffle(self.coins['R4'])
        shuffle(self.coins['R5'])

        # Dealt card to players
        self.players[0].draw_cards(self.draw_pile[:5])
        self.players[1].draw_cards(self.draw_pile[5:10])
        self.draw_pile = self.draw_pile[10:]

    def is_over(self):
        cond_1 = (len(self.draw_pile) == 0)
        n_coins = [len(self.coins[x]) for x in ['Diamonds', 'Gold', 'Silver', 'Cloth', 'Spice', 'Leather']]
        cond_2 = (n_coins.count(0) >= 3)
        return cond_1 or cond_2

    def play(self):
        ply_idx = 0
        while not self.is_over():
            # Player make move and append to history
            self.draw_pile, self.board, self.coins, self.history = self.players[ply_idx].make_move(
                self.draw_pile, self.board, self.coins, self.history)

            # Switch player
            ply_idx = (ply_idx + 1) % 2

        # Camel reward
        ply_c = (len(self.players[0].camel), len(self.players[1].camel))
        if ply_c[0] != ply_c[1]:
            self.coins['Camel'] = []
            if ply_c[0] > ply_c[1]:
                self.players[0].money += 5
                self.players[0].n_coins += 1
            elif ply_c[1] > ply_c[0]:
                self.players[1].money += 5
                self.players[1].n_coins += 1

        # Determine the winner
        ply_m = (self.players[0].money, self.players[1].money)
        n_coins = (self.players[0].n_coins, self.players[1].n_coins)
        n_bonus = (self.players[0].n_bonus, self.players[1].n_bonus)
        winner = None
        if ply_m[0] > ply_m[1]:
            winner = 0
        elif ply_m[0] < ply_m[1]:
            winner = 1
        else:
            if n_bonus[0] > n_bonus[1]:
                winner = 0
            elif n_bonus[0] < n_bonus[1]:
                winner = 1
            else:
                if n_coins[0] > n_coins[1]:
                    winner = 0
                elif n_coins[0] < n_coins[1]:
                    winner = 1

        # Print out the result of the game
        msg_t = f"#### Player 1: money: {ply_m[0]}, number of bonus: {n_bonus[0]}, number of coins: {n_coins[0]};" \
                f"  Player 2: money: {ply_m[1]}, number of bonus: {n_bonus[1]}, number of coins: {n_coins[1]} ####"
        if winner is None:
            print(f"The game end with a tie! {msg_t}")
        elif winner == 0:
            print(f"Player 1 is the winner! {msg_t}")
        elif winner == 1:
            print(f"Player 2 is the winner! {msg_t}")