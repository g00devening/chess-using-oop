class Selector:
    def __init__(self, values):
        self.values = values

    def get_odds(self):
        return [x for x in self.values if x % 2 != 0]

    def get_evens(self):
        return [x for x in self.values if x % 2 == 0]


values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(*odds)
print(*evens)