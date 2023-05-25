class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, new):
        self.year = new

    def set_month(self, new):
        self.month = new

    def set_day(self, new):
        self.day = new

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f'{str(self.month).zfill(2)}.{str(self.day).zfill(2)}.{self.year}'


class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, new):
        self.year = new

    def set_month(self, new):
        self.month = new

    def set_day(self, new):
        self.day = new

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f'{str(self.day).zfill(2)}.{str(self.month).zfill(2)}.{self.year}'


date = AmericanDate(2000, 4, 10)
date2 = EuropeanDate(2000, 4, 10)
print(date.format())
print(date2.format())