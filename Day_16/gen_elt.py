import sys
import time

start = time.time()
# here let is iterable object
let = [x for x in range(10000000)]
print(sys.getsizeof(let))
print(time.time() - start)
# print(dir(let))

start = time.time()
# now let is iterator
let = range(10000000)
print(sys.getsizeof(let))
print(time.time() - start)


start = time.time()
# here let is generator
let = (x for x in range(10000000))
print(sys.getsizeof(let))
print(time.time() - start)
