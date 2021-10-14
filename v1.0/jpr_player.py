from jpr_func import possible_moves
from pdb import set_trace


class Player:
    def __init__(self, name):
        # Attributes related to player
        self.name = name
        self.hand = []
        self.camel = []
        self.money = 0
        self.n_coins = 0
        self.n_bonus = 0

    def draw_cards(self, cards):
        self.camel = self.camel + ['Camels'] * cards.count('Camels')
        self.hand = self.hand + [x for x in cards if x != 'Camels']

    def ask_move(self, moves, board, coins, history):
        # A non-sense strategy
        n_mv, n_h, n_c = len(moves), len(self.hand), len(self.camel)
        n_tot = n_h + n_c + self.money + self.n_coins + self.n_bonus
        return moves[n_tot % n_mv]

    def make_move(self, draw_pile, board, coins, history):
        # Get all possible moves
        moves = possible_moves(self.hand, self.camel, board)

        # Make decision with player's strategy
        move = self.ask_move(moves, board, coins, history)

        # Update game according to player's move
        # 1. Update 'hand'(also 'camel') and 'board'
        if move[0] == 'take_camel':
            # 1.1 Just add to 'camel' and remove all 'Camels' from 'board'
            self.camel += ['Camels'] * move[1]
            board = [x for x in board if x != 'Camels']
        elif move[0] == 'take_one':
            # 1.2 Add one to 'hand' and remove one from 'board'
            self.hand += [move[1]]
            board.remove(move[1])
        elif move[0] == 'exchange':
            # 1.3.1 Remove first tuple of cards from hand and add second tuple
            # 1.3.1.1 Figure out camels
            n_ec = move[1].count('Camels')
            if n_ec > 0:
                self.camel = ['Camels'] * (len(self.camel) - n_ec)
            # 1.3.1.2 Figure out goods
            for x in move[1]:
                if x != 'Camels':
                    self.hand.remove(x)
            # 1.3.1.3 Add second tuple of cards
            self.hand += list(move[2])
            # 1.3.2 Remove second tuple of cards from board and add first tuple
            for x in move[2]:
                board.remove(x)
            board += list(move[1])
        elif move[0] == 'sell':
            # 1.4 The only part where coins are involved
            # 1.4.1 Remove cards from hand
            for i in range(move[2]):
                self.hand.remove(move[1])
            # 1.4.2 Earn coins with selling
            n_ce = min(move[2], len(coins[move[1]]))
            if n_ce > 0:
                self.n_coins += n_ce
                for i in range(n_ce):
                    self.money += coins[move[1]].pop(0)
                # 1.4.2.1 Condition of getting bonus coin
                if 3 <= n_ce <= 5:
                    self.n_bonus += 1
                    self.money += coins[f"R{n_ce}"].pop(0)

        # 2. Re-fill board
        n_rf = 5 - len(board)
        if n_rf > 0:
            board += draw_pile[:n_rf]
            draw_pile = draw_pile[n_rf:]

        # Append move to game history
        history += [move]
        return draw_pile, board, coins, history
