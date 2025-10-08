import numpy as np

arr1 = np.arange(15, dtype=np.int64).reshape(3, 5)
arr2 = np.random.random((3, 5))
print(np.round(arr2 * 100))
# scaler operation
# print(arr1**2)
# vector operation

# print(arr1 > arr2)

# operation on spesfic column and row
print(arr1)
# 1 for row and 0 for column
print(np.max(arr1, axis=1))
