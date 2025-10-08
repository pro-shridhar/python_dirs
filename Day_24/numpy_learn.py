import numpy as np

arr = np.array([3, 4, 5, 4, 2])
# print(arr)

arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr1)

arr2 = np.arange(3, 31, 3)
# print(arr2)

"""
2 blocks
└─ each block has 3 rows × 2 columns
  or
main array -> 2 array -> each have 3 array -> each have 2 element
"""
arr3 = np.arange(3, 37, 3).reshape((2, 3, 2))
# print(arr3)
arr3_1 = np.arange(3, 37, 3).reshape((4, 3))
# print(arr3_1)
arr3_2 = np.arange(12).reshape(4, -1)
# print(arr3_2)

arr4 = np.ones((2, 3, 4))
# print(arr4)

arr5 = np.zeros((2, 3, 4))
# print(arr5)


arr6 = np.random.random((3, 3, 4))
# print(arr6)

# np.random.randint(low, high=None, size=None, dtype=int)
# to create rendom value
arr6_1 = np.random.randint(1, 12, (3, 3, 4))
# print(arr6_1)

# arr = np.linspace(start,end,number of element)
arr7 = np.linspace(-10, 10, 10, retstep=True)
print(arr7)

arr8 = np.identity(3)
print(arr8)
