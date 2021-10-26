import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from jaipur import Jaipur
from jprAI_rt import JaipurAIRegressionTree
from pdb import set_trace

GOODS = ['Diamonds', 'Gold', 'Silver', 'Cloth', 'Spice', 'Leather', 'Camels']


def sim_1g(seed_g):
    game = Jaipur([JaipurAIRegressionTree(), JaipurAIRegressionTree()], seed_g=seed_g)
    game.play(verbose=False)
    sa_1, sa_2 = np.array(game.players[0].sa), np.array(game.players[1].sa)
    sa_1[:, 0] = sa_1[-1, 0] - sa_1[:, 0]
    sa_2[:, 0] = sa_2[-1, 0] - sa_2[:, 0]
    rst = np.vstack((sa_1, sa_2))
    return rst


def sim(n):
    sa_l = Parallel(n_jobs=-1, verbose=10, batch_size=100)(delayed(sim_1g)(x) for x in range(n))
    sa_l = np.vstack(sa_l)
    sa_l = np.unique(sa_l, axis=0)
    sa_l = pd.DataFrame(sa_l, columns=['money'] + [f"n_{x}" for x in GOODS[:6]] + [f"x_{x}" for x in GOODS])
    sa_l.to_parquet("sa02.pqt")


if __name__ == '__main__':
    sim(100000)