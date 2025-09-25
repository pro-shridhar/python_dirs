# import math as m

# print("squer root = ", int(m.sqrt(16)))
# print("pi value = ", m.pi)
# print("ceil value of pi = ", m.ceil(m.pi))
# print("floor value of pi = ", m.floor(m.pi))
# print("choosing 2 things out of 5 = ", m.comb(5, 2))
# print("factorial of 5 = ", m.factorial(5))
# print("ceil value of pi = ", m.perm(5, 2))


list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list2 = []
for i in range(0, len(list)):
    list2.append([])
    for j in range(len(list[i]) - 1, -1, -1):
        list2[i].append(list[i][j])
print(list2)

list3 = [x for x in list[::-1]]
print(list3)

list1 = [x[::-1] for x in list]
print(list1)
