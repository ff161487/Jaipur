from itertools import combinations
from pdb import set_trace


def exchange_n(h_e, b_e, n):
    h_c = set([tuple(sorted(x)) for x in combinations(h_e, n)])
    b_c = set([tuple(sorted(x)) for x in combinations(b_e, n)])
    e_c = [('exchange', x, y) for x in h_c for y in b_c if len(set(x).intersection(set(y))) == 0]
    return e_c


def possible_moves(hand, camel, board):
    moves = []
    # Cannot hold more than 7 goods cards
    # 'mc' for 'max_camels', 'me' for 'max_exchange'
    n_b, n_c, n_h = len(board), board.count('Camels'), len(hand)
    n_mc = min(len(camel), 7 - n_h)
    n_me = min(n_h + n_mc, n_b - n_c)

    # Could take all camels if there is at least 1 camel on the board
    if n_c > 0:
        moves += [('take_camel', n_c)]
    # Could take one goods card if less than 7 goods cards in hand
    if n_h < 7:
        moves += [('take_one', x) for x in set(board) if x != 'Camels']
    # Could sell goods if non-empty hand
    if n_h > 0:
        for item in set(hand):
            n_oc = hand.count(item)
            if item in ['Diamonds', 'Gold', 'Silver'] and n_oc >= 2:
                moves += [('sell', item, x) for x in range(2, n_oc + 1)]
            elif item not in ['Diamonds', 'Gold', 'Silver']:
                moves += [('sell', item, x) for x in range(1, n_oc + 1)]
    # Could exchange goods if there are more than one goods card on the board
    if n_me >= 2:
        # Generate hand and board for exchange
        b_e = [x for x in board if x != 'Camels']
        h_e = hand + ['Camels'] * n_mc
        for n_e in range(2, n_me + 1):
            moves += exchange_n(h_e, b_e, n_e)
    return moves