class ones_threes_nines:

    threes = 0
    ones = 0
    nines = 0

    def __init__(self, num):
        self.threes = num // 3
        self.ones = num // 1
        self.nines = num // 9


num = ones_threes_nines(17)
print(num.ones, num.threes, num.nines)
