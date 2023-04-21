from Piece import *


class Pawn(Piece):
    def char(self):
        return 'P'

    def can_move(self, row_to, col_to):
        if self.col != col_to:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.row + direction == row_to:
            return True
        if self.row == start_row and \
           self.row + 2 * direction == row_to:
            return True
        return False
