import gc


# Create a cycle
def fun(i):
    x = {}
    x[i + 1] = x
    return x


# Trigger garbage collection
c = gc.collect()
print(c)

for i in range(10):
    fun(i)

c = gc.collect()
print(c)
