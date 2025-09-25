import sys
import gc


x = [1, 2, 3]
y = [4, 5, 6]

# x = y reference count 3
# y = x reference count 3

x.append(y)
y.append(x)

print(sys.getrefcount(x))
print(sys.getrefcount(y))
print(x, y)

a = [1, 2, 3]  # big object
del a
print(gc.collect())  # may collect memory

b = [1, 2, 3]
print(gc.collect())  # won't collect, because b still holds reference
