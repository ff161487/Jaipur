import numpy as np
from joblib import load
from jpr_func import tup2vec
from jpr_player import Player
from pdb import set_trace


class JaipurAIRegTreePoly2(Player):
    def __init__(self, name='AI'):
        super().__init__(name)
        self.model = load("rt_p2.joblib")
        self.sa = []

    def ask_move(self, moves, board, tokens, history):
        # Transform moves and token state into vectors
        mv_a = tup2vec(moves, tokens)

        # Select move with the biggest gain
        q_a = self.model.predict(mv_a)
        id_max = np.argmax(q_a)
        move = moves[id_max]

        # Record the move vector with 'sa' list
        self.sa.append(mv_a[id_max])
        return move