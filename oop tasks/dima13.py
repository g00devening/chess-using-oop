class MinStat:
    def __init__(self):
        self.values = []

    def add_number(self, value):
        self.values.append(value)

    def result(self):
        if len(values) == 0:
            return None
        return min(self.values)


class MaxStat:
    def __init__(self):
        self.values = []

    def add_number(self, value):
        self.values.append(value)

    def result(self):
        if len(values) == 0:
            return None
        return max(self.values)


class AverageStat:
    def __init__(self):
        self.values = []

    def add_number(self, value):
        self.values.append(value)

    def result(self):
        if len(values) == 0:
            return None
        return sum(values) / len(values)


values = [1, 2, 4, 5]
mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), average.result())