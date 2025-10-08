import numpy as np

arr1 = np.arange(10, dtype=np.int32)
arr2 = np.arange(12, dtype=float).reshape(3, 4)
arr3 = np.arange(8).reshape(2, 2, 2)

# ndim, shape, size, itemsize, dtype,
print(arr3.ndim, "array dimension")
print(arr2.shape, "array attributes")
print(arr1.size, "array total element")
print(arr1.itemsize, "array element size")
print(arr3.dtype, "array element data type")
