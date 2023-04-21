from Piece import *


class Queen(Piece):
    def char(self):
        return 'Q'

    def can_move(self, row_to, col_to):
        if abs(self.row - row_to) == abs(self.col - col_to):
            return True
        if self.row == row_to or \
           self.col == col_to:
            return True
        return False
