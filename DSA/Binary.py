def search(arr, targat):

    start = 0
    end = len(arr)

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] == targat:
            return mid
        elif arr[mid] > targat:
            end = mid - 1
        else:
            start = mid

    return -1


arr = [2, 34, 45, 65, 70]
print(search(arr, 65))
