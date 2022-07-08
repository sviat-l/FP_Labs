"""
ETERNAS GAME
"""
import random


def board_generation():
    """
    Generates a game board of 16 x 4 size, i.e.
    two dimensional list (array) of 'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'], [0, 0, 0, 'g'],
          [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'], [0, 0, 'g', 'w']]

    """
    options = [0, 'g', 'w']
    board = []
    for collumn in range(16):
        board.append([0, 0, 0, 0])
        for row in range(3, 0, -1):
            board[collumn][row] = (random.choice(options))
            if board[collumn][row] == 0:
                break
    return board


def winning_combination(board) :
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning combinations
    if there is winning combination or False if not.

    >>> winning_combination([[0, 'g', 'g', 'g'], [0, 'g', 'w', 'w'], [0, 0, 'g', 'g'],\
    [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 0, 0, 0],\
    [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'], ['w', 'g', 'w', 'w'], [0, 'g', 'w', 'g'],\
    [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'g', 'g', 'w'],\
    [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], ['w', 'g', 'g', 'g'], ['w', 'w', 'g', 'w'],\
    [0, 0, 0, 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 'g', 'w', 'w'],\
    [0, 0, 'w', 'g'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], \
    ['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], \
    [0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],\
    [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'],\
    ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'g'], \
    [0, 0, 'w', 'w'], [0, 'w', 'w', 'g'], ['g', 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'],\
    [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 'w', 'g'], ['g', 'g', 'w', 'g'],\
    [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 'w'],\
    [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 0, 0, 0], [0, 0, 0, 0],\
    ['g', 'w', 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g']])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination([[0, 'w', 'w', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'w'],\
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'w', 'g'], [0, 0, 'w', 'g'], \
    [0, 0, 0, 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], \
    [0, 'g', 'w', 'g'], ['g', 'g', 'w', 'g'], ['w', 'g', 'w', 'g']])
    (True, [[(2, 13), (2, 14), (2, 15), (2, 0)], [(3, 5), (3, 6), (3, 7), (3, 8)], [(3, 11), (2\
, 12), (1, 13), (0, 14)]])
    >>> winning_combination([[0, 0, 'g', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0],\
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'g', 'g'], ['w', 'w', 'g', 'g'],\
    ['w', 'g', 'g', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'],\
    [0, 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g']])
    (True, [[(3, 9), (3, 10), (3, 11), (3, 12)]])
    >>> winning_combination([[0, 0, 'w', 'w'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'],\
    [0, 'w', 'g', 'g'], ['g', 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'w', 'w'], [0, 0, 'g', 'w'],\
    [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 'w', 'w', 'w'], ['g', 'g', 'w', 'g'], \
    [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w']])
    (True, [[(3, 4), (3, 5), (3, 6), (3, 7)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    >>> winning_combination([['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'],\
    [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'],\
    [0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'],\
    [0, 0, 'g', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (3, 15), (3, 0), (3, 1)],\
 [(3, 15), (3, 0), (3, 1), (3, 2)]])
    """
    line_check = []
    for column in range(16):
        if board[column][0] != 0:
            if board[column][0] == board[column][1] == board[column][2] == board[column][3]:
                line_check.append(
                    [(0, column), (1, column), (2, column), (3, column)])

    for row in range(4):
        for column in range(16):
            if board[column][row] != 0:
                if board[column][row] == board[(column+1) % 16][row] == \
                    board[(column+2) % 16][row] == board[(column+3) % 16][row]:
                    line_check.append(
                                      [(row, column), (row, (column + 1) % 16),\
                                       (row, (column+ 2) % 16), (row, (column+3) % 16)])

    for column in range(16):
        if board[column][0] != 0:
            # if board[column][row] == board[(column+1) % 16][1] == board[(column+2) % 16][2] == \
            #      board[(column+3) % 16][3]:
            #     line_check.append(
            #         [(0, column), (1, (column+1) % 16), (2, (column+2) % 16), (3, (column+3) % 16)])
            if board[column][row] == board[(column-1) % 16][1] == board[(column-2) % 16][2] == \
                 board[(column-3) % 16][3]:
                line_check.append(
                    [(3, (column-3) % 16), (2, (column-2) % 16), (1, (column-1) % 16), (0, column)])
    if len(line_check) == 0:
        return False
    return True, sorted(line_check)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())