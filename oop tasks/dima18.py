days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        sum_of_days1 = sum(days[:self.month]) + self.day
        sum_of_days2 = sum(days[:other.month]) + other.day
        return sum_of_days1 - sum_of_days2


mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)
