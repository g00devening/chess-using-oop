class MinMaxWordFinder:
    def __init__(self):
        self.words_max = set()
        self.words_min = []
        self.max_length = 0
        self.min_length = float('inf')

    def add_sentence(self, string):
        for word in string.split():
            if len(word) > self.max_length:
                self.words_max.clear()
                self.words_max.add(word)
                self.max_length = len(word)
            elif len(word) == self.max_length:
                self.words_max.add(word)
            if len(word) == self.min_length:
                self.words_min.append(word)
            elif len(word) < self.min_length:
                self.words_min.clear()
                self.words_min.append(word)
                self.min_length = len(word)

    def shortest_words(self):
        return sorted(self.words_min)

    def longest_words(self):
        return sorted(self.words_max)


finder = MinMaxWordFinder()
finder.add_sentence('aa aa dsfskj dima lg sdfasdf tytytytytytyt')
finder.add_sentence('uuuu     adf    uhfabghfychgq')
finder.add_sentence('aa uhfabghfychgq')
print(*finder.longest_words())
print(*finder.shortest_words())

