from Piece import *


class Bishop(Piece):
    def char(self):
        return 'B'

    def can_move(self, row_to, col_to):
        if abs(self.row - row_to) == abs(self.col - col_to):
            return True
        return False
