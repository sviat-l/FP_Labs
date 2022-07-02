"""
Lab 13.3 TicTacToe Game
"""
from board import Board

# set cell symbols
X, O, E = 'x', '0', '_'

def play_game():
    """
    Run one game simulation
    """
    game_board = Board()

    while not endgame_board(game_board):
        print(game_board)
        if game_board.last_move is not None:
            print(f'\nOpponent last move: {game_board.last_move[0]}\n')
        make_user_move(game_board)
        if not endgame_board(game_board):
            game_board.make_computer_move()

    endgame(game_board)

def make_user_move(board:Board):
    """
    Ask user coords. Make user move, if possible.
    Otherwise run function again
    """
    try:
        coords = get_input()
    except ValueError:
        print('\nEntered position with not integer values. Try again\n')
        make_user_move(board)
    try:
        board.make_move(coords, X)
        return
    except IndexError:
        print('\nPosition out of board. Try one more time\n')
    except ValueError:
        print("\nYou can't make move. Cell is not empty\n")
    make_user_move(board)


def endgame_board(board:Board) -> bool:
    """
    Check if it is the end of the game
    """
    return board.get_status() != 'continue'

def endgame(board:Board):
    """
    Return string about game results
    """
    print(board)
    if board.get_status() == O:
        print('\nOops... You losed!\n')
    elif board.get_status() == X:
        print('\nWinner winner chicken dinner!\n')
    else:
        print('\nIt is a draw!\n')


def get_input() -> tuple[int]:
    """
    Get input coordinates from the user
    """
    print('Enter cell coordinates (from 0 to 2)')
    row = int(input('Row number: '))
    collumn = int(input('Collumn number: '))
    print()
    return row, collumn

if __name__ == '__main__':
    play_game()
