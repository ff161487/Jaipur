import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from jaipur import Jaipur
from jprAI_lrp2 import JaipurAILinRegPoly2
from pdb import set_trace

GOODS = ['Diamonds', 'Gold', 'Silver', 'Cloth', 'Spice', 'Leather', 'Camels']


def sim_1g(seed_g):
    game = Jaipur([JaipurAILinRegPoly2(), JaipurAILinRegPoly2()], seed_g=seed_g)
    money_list = game.play(verbose=False)
    money_list = np.array(money_list)
    scores = np.zeros((len(money_list), 2))
    scores[:, 0], scores[:, 1] = money_list[:, 0] - money_list[:, 1], money_list[:, 1] - money_list[:, 0]
    dsc = np.diff(scores, axis=0, prepend=0)
    n_tot = len(money_list)
    kn = np.zeros((n_tot, n_tot))
    for i in range(n_tot):
        for j in range(i, n_tot):
            kn[i, j] = 0.9 ** (j - i)
    q_h = kn.dot(dsc)
    sa_1, sa_2 = np.array(game.players[0].sa), np.array(game.players[1].sa)
    sa_1, sa_2 = np.hstack((q_h[::2, 0][:, None], sa_1)), np.hstack((q_h[1::2, 1][:, None], sa_2))
    rst = np.vstack((sa_1, sa_2))
    return rst


def sim(n):
    sa_l = Parallel(n_jobs=-1, verbose=10, batch_size=100)(delayed(sim_1g)(x) for x in range(n))
    sa_l = np.vstack(sa_l)
    sa_l = np.unique(sa_l, axis=0)
    sa_l = pd.DataFrame(sa_l, columns=['q'] + [f"n_{x}" for x in GOODS[:6]] + [f"x_{x}" for x in GOODS])
    sa_l.to_parquet("qsa_lrp2.pqt")


if __name__ == '__main__':
    # sim_1g(0)
    sim(100000)