from jaipur import Jaipur
from jprAI_lgbm_p2 import JaipurAILGBMPoly2
from jprHuman import HumanPlayer
from pdb import set_trace


def play_jaipur():
    game = Jaipur([JaipurAILGBMPoly2(), HumanPlayer()])
    game.play()
    set_trace()


if __name__ == '__main__':
    play_jaipur()