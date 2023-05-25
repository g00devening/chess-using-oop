class Queue:
    def __init__(self, *args):
        self.args = list(args)

    def append(self, new):
        self.args = [new] + self.args

    def copy(self):
        return self

    def pop(self):
        if len(self.args) != 0:
            first = self.args[0]
            self.args.remove(self.args[0])
            return first
        else:
            return None

    def extend(self, other):
        self.args += other.args

    def next(self):
        return Queue(*self.args[1::])

    def __add__(self, other):
        return Queue(*(self.args + other.args))

    def __iadd__(self, other):
        self.args += other.args

    def __rshift__(self, shift):
        if shift > len(self.args):
            return Queue(*[])
        return Queue(*self.args[shift::])
    
    def __eq__(self, other):
        if self.args == other.args:
            return True
        else:
            return False

    def __str__(self):
        if len(self.args) == 0:
            return '[]'
        representation = ''
        for i in self.args:
            representation += str(i) + ' -> '
        representation = representation[:-4]
        return f'[{representation}]'
