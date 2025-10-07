def pascal_tri(num):

    lst = []

    for i in range(num):
        lst.append([])
        for j in range(i + 1):
            if j == i or j == 0:
                lst[i].append(1)
            else:
                lst[i].append(lst[i - 1][j] + lst[i - 1][j - 1])

    return lst


pascal = pascal_tri(6)
for i in pascal:
    print(i)
