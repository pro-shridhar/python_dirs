import numpy as np

arr = np.arange(4, dtype=int).reshape(2, 2)
arr1 = np.arange(4, 8, dtype=int).reshape(2, 2)
# print(arr)
# print(arr1)
# print(np.dot(arr, arr1))
# print(np.matmul(arr, arr1))
# print(np.cross(arr, arr1))

ex = np.log(arr)
print(ex)
