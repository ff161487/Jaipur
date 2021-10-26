from random import seed, choice
from jpr_player import Player
from pdb import set_trace

GOODS = ['Diamonds', 'Gold', 'Silver', 'Cloth', 'Spice', 'Leather', 'Camels']


class JaipurAIRandom(Player):
    def __init__(self, name='AI', seed_ai=None):
        super().__init__(name)
        self.seed = seed_ai
        seed(self.seed)
        self.sa = []

    def ask_move(self, moves, board, tokens, history):
        # Randomly choose a move
        move = choice(moves)

        # Represent state-action as a vector
        tkn_a = [len(tokens[kind]) for kind in GOODS[:6]]
        mv_a = [0] * 7
        if move[0] == 'take_camel':
            mv_a[6] = move[1]
        elif move[0] == 'take_one':
            mv_a[GOODS.index(move[1])] = 1
        elif move[0] == 'exchange':
            for x in move[1]:
                mv_a[GOODS.index(x)] -= 1
            for y in move[2]:
                mv_a[GOODS.index(y)] += 1
        elif move[0] == 'sell':
            mv_a[GOODS.index(move[1])] = -move[2]
        rst = tkn_a + mv_a
        self.sa.append(rst)
        return move