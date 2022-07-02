"""
Lab 13.3 TicTacToe Board
"""
# set cell symbols
X, O, E = 'x', '0', '_'

class BTNode:
    """
    Node for binary tree
    """
    def __init__(self, data, left = None, right = None):
        """
        Init values with default right and left as None
        """
        self.data = data
        self.right = right
        self.left = left


class Board:
    """
    Class with methods related to the game board
    """

    def __init__(self) -> None:
        """
        Init by default empty board and last move as None
        """
        self.board = [[E for _ in range(3)] for _ in range(3)]
        self.last_move = None

    def __str__(self) -> str:
        """
        String representation of self
        """
        return '\n'.join(' '.join(row) for row in self.board)

    def get_status(self) -> str:
        """
        Check status of the board (4 variants)
        Return:
            'x' if x wins
            '0' if 0 wins
            'continue' if there are empty cells
            'draw' otherwise
        """
        if self.last_move is None:
            return 'continue'
        (i, j), turn = self.last_move
        # check last move row and collumn
        if self.board[i][0] == self.board[i][1] == self.board[i][2] or\
           self.board[0][j] == self.board[1][j] == self.board[2][j]:
            return turn
        # check diagonal
        if (turn ==self.board[0][0] == self.board[1][1] == self.board[2][2] or\
            turn ==  self.board[0][2] == self.board[1][1] == self.board[2][0]) :
            return turn
        # draw check if there is an empty cell
        return 'continue' if any(E in row for row in self.board) else 'draw'


    def make_move(self, position: tuple[int], turn: str) -> None:
        """
        Make move on the board, if it is possible.
        Otherwise raise errors.
        """
        i, j = position
        if i < 0 or i > 2 or j > 2 or j < 0:
            raise IndexError('Position out of board')
        if turn not in (X, O):
            raise ValueError("You can't make move. Cell is not empty")
        if self.board[i][j] != E:
            raise ValueError('Invalid turn symbol value')
        self.board[i][j] = turn
        self.last_move = position, turn


    def first_two_moves(self) -> list:
        """
        Return first two possible moves
        """
        result = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == E:
                    result.append((i, j))
                    if len(result) == 2:
                        break
        return result

    def copied_board(self):
        """
        Create and return new board with the same possitions
        """
        return [[state for state in row] for row in self.board]

    @staticmethod
    def endgame_sum(root) -> int:
        """
        Calculate sum for the tree game result children
        """
        if root is None:
            return 0
        # it is a tree leaf
        if isinstance(root.data, int):
            return root.data
        return Board.endgame_sum(root.left) + Board.endgame_sum(root.right)

    def create_tree(self, turn) -> BTNode:
        """
        Create tree from with the next moves board children
        """
        # The game is finished on the self board. Return its result
        if self.get_status() != 'continue':
            res = self.get_status()
            return BTNode(1 if res == O else -1 if res ==X else 0)
        # get two moves and next turn
        next_turn = X if turn==O else O
        moves = self.first_two_moves()
        # create left node for the root as board with the first move
        left_board = Board()
        left_board.board = self.copied_board()
        left_board.make_move(moves[0], turn)
        # create root and add its left child
        root = BTNode(self)
        root.left = left_board.create_tree(next_turn)
        # create right node for the root as a board
        # with the second move if it is possible
        if len(moves) != 1:
            right_board = Board()
            right_board.board = self.copied_board()
            right_board.make_move(moves[1], turn)
            root.right = right_board.create_tree(next_turn)
        return root

    def make_computer_move(self):
        """
        Make move as computer. Consider only first two
        possible moves(sorted by rows and columns.
        """
        moves = self.first_two_moves()
        tree = self.create_tree(O)
        return self.make_move(moves[0], O)\
            if tree.right is None or Board.endgame_sum(tree.left) > Board.endgame_sum(tree.right)\
          else self.make_move((moves[1]), O)
