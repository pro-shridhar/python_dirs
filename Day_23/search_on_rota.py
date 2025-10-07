def search(arr):
    left, right = 0, len(arr) - 1

    # Handle case when array is not rotated
    if arr[left] < arr[right]:
        return right

    while left <= right:
        mid = (left + right) // 2

        # Check if mid is the maximum
        if mid < right and arr[mid] > arr[mid + 1]:
            return mid
        if mid > left and arr[mid] < arr[mid - 1]:
            return mid - 1

        # Decide which side to search
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1

    return 0  # fallback (shouldn't reach here)


ele = [3, 4, 5, 6, 7, 8, 1, 2]
print(search(ele))
