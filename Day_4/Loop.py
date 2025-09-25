list = [2, 3, 4, 5, 6, 7]

for i in list:
    pass
print(i)

for i in reversed(list):
    print(i, end=" ")

print()

for i in range(len(list) - 1, -1, -1):
    print(list[i], end=" ")

print("\n")

for i in range(5):
    if i == 3:
        # pass
        continue
    else:
        print(i, end=" ")

print()

fru = ["apple", "kiwi", "mango"]

for i, j in enumerate(fru):
    print(i, j)
