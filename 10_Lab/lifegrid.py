from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                self.clear_cell(i,j)
        for i,j in coord_list:
            self.set_cell(i,j)

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return bool(self._grid.__getitem__((row,col)))

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row,col), None)

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid.__setitem__((row,col), 1)

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        live_num = 0
        neighbors = [(row+i, col+j) for i,j in [(0,1), (1,0), (-1, 0), (0, -1)]\
                     if -1<col+j< self.num_cols() and -1<row+i< self.num_rows() ]
        for i,j in neighbors:
            if self.is_live_cell(i,j):
                live_num += 1

        return live_num
    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        result = []
        for i in range(self._grid.num_rows()):
            for j in range(self._grid.num_cols()):
                result.append('L' if self.is_live_cell(i,j) else 'D')
            result.append('\n')
        return ''.join(result[:-1])
