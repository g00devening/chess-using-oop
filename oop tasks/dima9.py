class TicTacToeBoard:
    def __init__(self):
        self.map = [['-' for _ in range(3)] for _ in range(3)]
        self.game_finished = False
        self.move = 0

    def new_game(self):
        self.__init__()

    def get_field(self):
        return self.map

    def check_field(self, symbol):
        for i in range(3):
            if (self.map[i][0] == self.map[i][1] == self.map[i][2] == symbol or
                    self.map[0][i] == self.map[1][i] == self.map[2][i] == symbol):
                self.game_finished = True
                return f'{symbol} победил!'
        if (self.map[0][0] == self.map[1][1] == self.map[2][2] == symbol or
                self.map[0][2] == self.map[1][1] == self.map[2][0] == symbol):
            self.game_finished = True
            return f'{symbol} победил!'

    def make_move(self, row, col):
        if self.map[row][col] != '-':
            return 'Эта клетка занята!'
        if self.game_finished:
            return 'Игра уже завершена!'
        if self.move % 2 == 0:
            self.map[row][col] = '0'
            self.move += 1
            self.check_field('0')
        else:
            self.map[row][col] = 'X'
            self.move += 1
            self.check_field('X')


board = TicTacToeBoard()
print(*board.get_field(), sep='\n')
print(board.make_move(1, 1))
print(board.make_move(2, 1))
print(board.make_move(0, 0))
print(board.make_move(0, 1))
print(board.make_move(2, 2))
print(board.make_move(0, 2))
print(*board.get_field(), sep='\n')