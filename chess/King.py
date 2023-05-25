from Piece import *


class King(Piece):
    def char(self):
        return 'K'

    def can_move(self, row_to, col_to):
        if abs(self.row - row_to) <= 1 and \
           abs(self.col - col_to) <= 1:
            return True
        return False
