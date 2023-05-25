class Balance:
    right = 0
    left = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.right == self.left:
            return '='
        elif self.right < self.left:
            return 'L'
        else:
            return 'R'

balance = Balance()
balance.add_right(10)
balance.add_left(9)
print(balance.result())
balance.add_left(1)
print(balance.result())