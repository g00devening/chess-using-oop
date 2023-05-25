WHITE = 1
BLACK = 2
#uniDict = {BLACK: {'P': "♙", 'R': "♖", 'N': "♘", 'B': "♗", 'K': "♔", 'Q': "♕"},
#           WHITE: {'P': "♟", 'R': "♜", 'N': "♞", 'B': "♝", 'K': "♚", 'Q': "♛"}}


class Piece:
    """
    класс шахматной фигуры
    """

    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col

    def opponent(self):
        if self.color == WHITE:
            return BLACK
        return WHITE

    def is_black(self):
        return self.color == BLACK

    def is_white(self):
        return self.color == WHITE

    def get_color(self):
        return self.color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return ''

    def __eq__(self, other):
        return self.color == other.color

    def __str__(self):
        color = self.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + self.char()
