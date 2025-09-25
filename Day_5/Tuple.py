t1 = (3, 4, 1, 2)
# l2 = t1.sort() it only work with list
# print(l2)
l1 = sorted(t1)
print(l1)
t2 = tuple(["a", "s", "r"])

t3 = t1 + t2
print(t3)

t4 = t1, t2
print(t4)

for i in t3:
    print(i, end=" ")
print()

for i in t3[-5:-2]:
    print(i, end=" ")
print()

print(t3[-3:-1])

t5 = ((4, 8), (2, 5), (6, 7), (4, 7))
l3 = sorted(t5, key=lambda x: x[0])
print(t5)
print(l3)

print(list(filter(None, t5)))  # for deleting emty tuple

[print(val, end="") for val in t5 if val]  # for deleting emty tuple
# with conprehances
print()

t6 = (("a", 1), ("b", 2), (8, 3))  # converting tuple into dictionary
d1 = dict(t6)
print(d1)
