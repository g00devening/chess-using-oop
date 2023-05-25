class OddEvenSeparator:
    even_nums = []
    odd_nums = []

    def add_number(self, num):
        if num % 2 == 0:
            self.even_nums.append(num)
        else:
            self.odd_nums.append(num)

    def even(self):
        return self.even_nums

    def odd(self):
        return self.odd_nums


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(3)
separator.add_number(4)
separator.add_number(6)
separator.add_number(5)
separator.add_number(10)
print(*separator.even())
print(*separator.odd())