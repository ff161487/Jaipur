import pandas as pd
from jpr_player import Player
from pdb import set_trace

GOODS = ['Diamonds', 'Gold', 'Silver', 'Cloth', 'Spice', 'Leather', 'Camels']


class HumanPlayer(Player):
    def __init__(self, name='Human'):
        super().__init__(name)

    def show(self, board, tokens):
        visible_tokens = {x: tokens[x] for x in GOODS[:6]}
        print(f"####################################################################################\n"
              f"Your current hand: {self.hand}, number of camels: {len(self.camel)}, number of tokens: {self.n_tokens},"
              f" number of bonus: {self.n_bonus};\n"
              f"####################################################################################\n"
              f"The current board is: {board};\n"
              f"####################################################################################\n"
              f"Tokens left are: {visible_tokens}；\n"
              f"####################################################################################")

    def take_input(self, op_s, board, tokens):
        op_s = pd.Series(op_s)
        s = None
        set_s = [str(x) for x in range(len(op_s))]
        while s not in set_s:
            s = input(f"Please choose from: \n{op_s} \nby entering the index of your choice."
                      f"You can type 'h' for 'help' or type characters listed in the help.")
            if s == 'h':
                print('''
                    'h': view help;
                    'c': check current status(board, hand, tokens);
                    'q'：quit；''')
            elif s == 'c':
                self.show(board, tokens)
            elif s == 'q':
                exit("Thanks for playing and see you next time.")
            elif s not in set_s:
                print("Invalid input encountered")
        s = int(s)
        op = op_s[s]
        return op

    def ask_move(self, moves, board, tokens, history):
        # Step 1: Select the general type of move
        gt = sorted(set([x[0] for x in moves]))
        gt_c = self.take_input(gt, board, tokens)

        # Step 2: Select the specific
        if gt_c == 'take_camel':
            print("Your camel herds are ready!")
            move = ('take_camel', board.count('Camels'))
        elif gt_c == 'take_one':
            t1_l = list(set(board))
            if 'Camels' in t1_l:
                t1_l.remove('Camels')
            print("You have chosen to take one goods card, now please choose the card.")
            t1 = self.take_input(t1_l, board, tokens)
            move = ('take_one', t1)
        elif gt_c == 'exchange':
            cg_l = list(set([x[2] for x in moves if x[0] == 'exchange']))
            print("You have chosen to exchange cards, now please choose the cards you want to get from the board.")
            cg = self.take_input(cg_l, board, tokens)
            print("And now, choose the cards you want to put on the board.")
            cp_l = list(set([x[1] for x in moves if x[0] == 'exchange' and x[2] == cg]))
            cp = self.take_input(cp_l, board, tokens)
            move = ('exchange', cp, cg)
        elif gt_c == 'sell':
            s_l = list(set(self.hand))
            s_l = [x for x in s_l if x not in ['Diamonds', 'Gold', 'Silver'] or self.hand.count(x) > 1]
            print("You have chosen to sell cards, now please choose the kind of goods you want to sell.")
            s_k = self.take_input(s_l, board, tokens)
            n_c_s = self.hand.count(s_k)
            if s_k in ['Diamonds', 'Gold', 'Silver']:
                ncs_l = list(range(2, n_c_s + 1))
            else:
                ncs_l = list(range(1, n_c_s + 1))
            print("And please choose the number of cards to sell.")
            ncs = self.take_input(ncs_l, board, tokens)
            move = ('sell', s_k, ncs)
        return move