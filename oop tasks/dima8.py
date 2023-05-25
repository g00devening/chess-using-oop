class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map[row][col] = '*'
        elif result == 'hit':
            self.map[row][col] = 'x'
        elif result == 'sink':
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1))
            for direction in directions:
                r, c = row + direction[0], col + direction[1]
                if 0 <= r < 10 and 0 <= c < 10 and self.map[r][c] != 'x':
                    self.map[r][c] = '*'
            self.map[row][col] = 'x'

    def cell(self, row, col):
        return self.map[row][col]


sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(6, 9, 'hit')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()