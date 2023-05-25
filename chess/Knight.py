from Piece import *


class Knight(Piece):
    def char(self):
        return 'N'

    def can_move(self, row_to, col_to):
        if abs(self.row - row_to) == 2 and \
           abs(self.col - col_to) == 1:
            return True
        if abs(self.col - col_to) == 2 and \
           abs(self.row - row_to) == 1:
            return True
        return False
