import numpy as np
from jpr_func import tup2vec
from jpr_player import Player
from pdb import set_trace

"""
cf01 = np.array([2.67349646,  2.42895593,  2.18538865,  1.61401378,  1.61613371, 1.16109139, -0.89043815, -0.90029283,
               -0.91084495, -0.94980026, -0.95063905, -0.94737655, -0.40132275])

cf02 = np.array([2.71592318,  2.52535919,  2.30179355,  1.38088651,  1.12705332, 0.94437997, -0.65187055, -0.65716768,
               -0.66511313, -0.74856075, -0.68828685, -0.78072511, -0.59311038])
               
cf03 = np.array([2.64172455, 2.42191009, 2.18424653, 1.43748141, 1.42688592, 0.86221886, -0.54952802, -0.58401232,
                -0.62177508, -0.85442776, -0.6678352 , -0.83027526, -0.14684381])
"""
cf = np.array([0.02847886, 0.01655056, 0.00437802, 0.00412979, 0.00413957, -0.01146223, -2.18084891, -2.15301288,
               -2.12112533, -1.94647093, -1.94605879, -1.85507836, -0.68107124])


class JaipurAILinear(Player):
    def __init__(self, name='AI', beta=cf):
        super().__init__(name)
        self.beta = beta
        self.sa = []

    def ask_move(self, moves, board, tokens, history):
        # Transform moves and token state into vectors
        mv_a = tup2vec(moves, tokens)

        # Select move with the biggest gain
        q_a = mv_a.dot(self.beta)
        id_max = np.argmax(q_a)
        move = moves[id_max]

        # Record the move vector with 'sa' list
        self.sa.append(mv_a[id_max])
        return move