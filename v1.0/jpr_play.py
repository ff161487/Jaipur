from jaipur import Jaipur
from jprAI_lrp2 import JaipurAILinRegPoly2
from jprHuman import HumanPlayer
from pdb import set_trace


def play_jaipur():
    game = Jaipur([JaipurAILinRegPoly2(), HumanPlayer()])
    game.play()
    set_trace()


if __name__ == '__main__':
    play_jaipur()