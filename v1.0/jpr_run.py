from jaipur import Jaipur
from jprAI_random import JaipurAIRandom
from jprHuman import HumanPlayer
from pdb import set_trace


if __name__ == '__main__':
    my_game = Jaipur([JaipurAIRandom(), HumanPlayer()])
    my_game.play()
    set_trace()