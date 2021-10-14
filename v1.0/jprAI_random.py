from random import seed, choice
from jpr_player import Player
from pdb import set_trace


class JaipurAIRandom(Player):
    def __init__(self, name='AI', seed_ai=None):
        super().__init__(name)
        self.seed = seed_ai
        seed(self.seed)

    def ask_move(self, moves, board, coins, history):
        move = choice(moves)
        return move