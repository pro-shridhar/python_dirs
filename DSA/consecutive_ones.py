lst = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]


def lonstOnes(lst, k):
    maxx = 0
    num_zero = 0

    l = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            num_zero += 1

        while num_zero > k:
            if lst[l] == 0:
                num_zero -= 1

            l += 1
        maxx = max(maxx, (i - l + 1))

    return maxx


print(lonstOnes(lst, 2))
