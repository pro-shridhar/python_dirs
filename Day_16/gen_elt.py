import sys

# here let is iterable object
let = [x for x in range(10000000)]
print(sys.getsizeof(let))
# print(dir(let))

# now let is iterator
let = range(10000000)
print(sys.getsizeof(let))

# here let is generator
let = (x for x in range(10000000))
print(sys.getsizeof(let))
