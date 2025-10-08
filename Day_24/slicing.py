import numpy as np

arr1 = np.arange(10)
arr2 = np.arange(9).reshape(3, 3)
arr3 = np.arange(27).reshape(3, 3, 3)

# slicing for 1D array
# print(arr1)
# print(arr1[3:5])


# slicing for 2D array
# print(arr2)
# print(arr2[1, 1])
# print(arr2[::2, ::2])
# print(arr2[:, 1])


# slicing for 3D array
print(arr3)
print(arr3[2, ::2, 1])
print(arr3[::2, ::, ::2])
