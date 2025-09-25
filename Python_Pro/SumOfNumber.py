# a = 5

import random


def sum():
    global a
    a = 5 * (5 + 1) / 2
    print(a)


b = random.randrange(1, 10)
sum()
print(a, b)
