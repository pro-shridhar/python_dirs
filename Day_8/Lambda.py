# sum_of_n_number = lambda x: x * (x + 1) / 2


def funfun(fun, num):
    return fun(num) * 2


# passing function on function
print(funfun(lambda x: x * (x + 1) / 2, 5))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# use of map
l = [1, 2, 3, 4, 5, 6]

print(list(map(lambda x: x + x, l)))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 1+2+3+4+5
# use of filter

list1 = list(map(lambda x: x**2, range(10)))
print(list1)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


print(list(filter(lambda x: x % 2 == 0, l)))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# use of reduce
from functools import reduce

print(reduce(lambda x, y: x + y, l))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


"""Explanation: reduce(lambda x, y: x + y, a, 10)
starts with 10 as initial value, then adds each
element in the list ((10+1)+2)+3 = 16."""


a = [1, 2, 3]
res = reduce(lambda x, y: x + y, a, 10)
print(res)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


"""The accumulate() function (from itertools) and reduce()
both apply a function cumulatively to items in a sequence.
However, accumulate() returns an iterator of intermediate
results, while reduce() returns only final value."""

from itertools import accumulate
from operator import add

a = [1, 2, 3, 4, 5]
res = accumulate(a, add)
print(list(res))
