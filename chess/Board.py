from Pawn import *
from Knight import *
from Queen import *
from King import *
from Bishop import *
from Rook import *


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        for col in range(8):
            self.field[1][col] = Pawn(1, col, WHITE)
            self.field[6][col] = Pawn(6, col, BLACK)
        self.field[0][0] = Rook(0, 0, WHITE)
        self.field[0][7] = Rook(0, 7, WHITE)
        self.field[7][0] = Rook(7, 0, BLACK)
        self.field[7][7] = Rook(7, 7, BLACK)
        self.field[0][1] = Knight(0, 1, WHITE)
        self.field[0][6] = Knight(0, 6, WHITE)
        self.field[7][1] = Knight(7, 1, BLACK)
        self.field[7][6] = Knight(7, 6, BLACK)
        self.field[0][2] = Bishop(0, 2, WHITE)
        self.field[0][5] = Bishop(0, 5, WHITE)
        self.field[7][2] = Bishop(7, 2, BLACK)
        self.field[7][5] = Bishop(7, 5, BLACK)
        self.field[0][3] = Queen(0, 3, WHITE)
        self.field[7][3] = Queen(7, 3, BLACK)
        self.field[0][4] = King(0, 4, WHITE)
        self.field[7][4] = King(7, 4, BLACK)

    def correct_coords(self, row, col):
        """
        функция проверяет, что координаты фигуры
        не выходят за границы доски
        """
        return 0 <= row <= 8 and 0 <= col <= 8

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j] is None or i == row and j == col:
                    continue
                this = self.field[i][j]
                if this.get_color() == color:
                    if isinstance(this, Rook):
                        if self.no_rook_obstacle(this.row, this.col, row, col):
                            return True
                    elif isinstance(this, Bishop):
                        if self.no_bishop_obstacle(this.row, this.col, row, col):
                            return True
                    elif isinstance(this, Queen):
                        if self.no_rook_obstacle(this.row, this.col, row, col) or \
                           self.no_bishop_obstacle(this.row, this.col, row, col):
                            return True
                    elif isinstance(this, Pawn):
                        if row - this.row == 1 and abs(col - this.col) == 1:
                            return True
                    else:
                        if this.can_move(row, col):
                            return True
        return False

    def show_board(self):
        print('    +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end=' ')
            for col in range(8):
                print('|', self.cell(row, col), end=' ')
            print('|')
            print('    +----+----+----+----+----+----+----+----+')
        print(end='      ')
        for col in range(8):
            print(col, end='    ')
        print()

    def current_player_color(self):
        return self.color

    def get_piece(self, row, col):
        return self.field[row][col]

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def no_rook_obstacle(self, row, col, row_to, col_to):
        if not self.field[row][col].can_move(row_to, col_to):
            return False
        if row == row_to:
            for i in range(min(col, col_to) + 1, max(col, col_to)):
                if isinstance(self.field[row][i], Piece):
                    return False
        elif col == col_to:
            for i in range(min(row, row_to) + 1, max(row, row_to)):
                if isinstance(self.field[i][col], Piece):
                    return False
        return True

    def no_bishop_obstacle(self, row, col, row_to, col_to):
        if not self.field[row][col].can_move(row_to, col_to):
            return False
        if row_to - row > 0:
            if col_to - col > 0:
                for i in range(1, row_to - row):
                    if isinstance(self.field[row + i][col + i], Piece):
                        return False
            else:
                for i in range(1, row_to - row):
                    if isinstance(self.field[row + i][col - i], Piece):
                        return False
        else:
            if col_to - col > 0:
                for i in range(1, row - row_to):
                    if isinstance(self.field[row - i][col + i], Piece):
                        return False
            else:
                for i in range(1, row - row_to):
                    if isinstance(self.field[row - i][col - i], Piece):
                        return False
        return True
    def move(self, row, col, row_to, col_to):
        if not self.correct_coords(row, col) or \
                not self.correct_coords(row_to, col_to):
            return False
        if row == row_to and col == col_to:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color != self.color:
            return False
        if not piece.can_move(row_to, col_to):
            return False
        if isinstance(piece, Rook):
            return self.rook_obstacle(row, col, row_to, col_to)
        elif isinstance(piece, Bishop):
            return self.bishop_obstacle(row, col, row_to, col_to)
        elif isinstance(piece, Queen):
            return self.rook_obstacle(row, col, row_to, col_to) and \
                   self.bishop_obstacle(row, col, row_to, col_to)
        self.field[row][col] = None
        self.field[row_to][col_to] = piece
        piece.set_position(row_to, col_to)
        self.color = piece.opponent()
        return True
