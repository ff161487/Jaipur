from jpr_player import Player
from pdb import set_trace


class HumanPlayer(Player):
    def __init__(self, name='Human'):
        super().__init__(name)

    def show(self, board, coins):
        print(f"Your current hand: {self.hand}, number of camels: {len(self.camel)}, money: {self.money},"
              f" number of coins: {self.n_coins}, number of bonus: {self.n_bonus};\nThe current board is: {board};\n"
              f"Coins left are: {coins}；")

    def take_input(self, op_s, board, coins):
        s = None
        set_s = [str(x) for x in range(len(op_s))]
        while s not in set_s:
            s = input(f"Please choose from {op_s} by entering the index of your choice."
                      f"You can type 'h' for 'help' or type characters listed in the help.")
            if s == 'h':
                print('''
                    'h': view help;
                    'c': check current status(board, hand, coins);
                    'q'：quit；''')
            elif s == 'c':
                self.show(board, coins)
            elif s == 'q':
                exit("Thanks for playing and see you next time.")
            elif s not in set_s:
                print("Invalid input encountered")
        s = int(s)
        op = op_s[s]
        return op

    def ask_move(self, moves, board, coins, history):
        # Step 1: Select the general type of move
        gt = sorted(set([x[0] for x in moves]))
        gt_c = self.take_input(gt, board, coins)

        # Step 2: Select the specific
        if gt_c == 'take_camel':
            move = ('take_camel', board.count('Camels'))
        elif gt_c == 'take_one':
            set_trace()
        return move