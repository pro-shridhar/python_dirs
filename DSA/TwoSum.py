def two_sum(arr, target):
    set1 = dict()
    for i, j in enumerate(arr):
        rem = target - j
        if j not in set1:
            set1[rem] = i
        else:
            print(i, set1[j])
            return
    print("no such element")


arr = [6, 4, 8, 12, 9]
two_sum(arr, int(20))
