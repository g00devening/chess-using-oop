from Piece import *


class Rook(Piece):
    def char(self):
        return 'R'

    def can_move(self, row_to, col_to):
        if self.row == row_to or \
           self.col == col_to:
            return True
        return False
