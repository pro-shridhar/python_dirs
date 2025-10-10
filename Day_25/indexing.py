import numpy as np

arr = np.random.randint(15, size=(5, 3))
print(arr)

# 1 for row and 0 for column
filt = np.all(arr > 10, where=[True, True, True], axis=1)
print(filt)

out_arr = np.empty((5,), dtype=bool)
""" "any" and "all" give us result on row or on column
    out to use array made by as
"""
# filt = np.any(arr > 10, where=[True, True, True], out=out_arr, axis=1)
# print(filt)
# filt = np.all(arr > 10, where=[True, True, True], keepdims=True)
# print(filt)

arr1 = np.random.randint(15, size=(5, 3))

# result = np.where(arr1 == arr, arr, 0)
# print(result)

# result = np.where(arr1 == arr, arr1, "a")
# print(result)

# print(np.where((arr > 5) & (arr < 10), arr, "n"))

# mask
# mask = (arr > 5) & (arr < 10)
# print(arr[mask])
