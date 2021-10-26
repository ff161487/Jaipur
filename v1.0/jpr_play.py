from jaipur import Jaipur
from jprAI_rtp2 import JaipurAIRegTreePoly2
from jprHuman import HumanPlayer
from pdb import set_trace


def play_jaipur():
    game = Jaipur([HumanPlayer(), JaipurAIRegTreePoly2()])
    game.play()
    set_trace()


if __name__ == '__main__':
    play_jaipur()