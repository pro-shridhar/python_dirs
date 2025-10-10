import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
arr1 = np.arange(9, dtype=int).reshape(3, 3)
arr2 = np.arange(9, 18, dtype=int).reshape(3, 3)

new_arr = np.stack((a, b), axis=1)
print(new_arr)

# new_arr = np.stack((arr1, arr2), axis=0)
# print(new_arr)
# print(new_arr.flatten())
# print(new_arr.transpose())

# befor and after use of swapaxes
# print(new_arr.shape)
# sawp = np.swapaxes(new_arr, axis1=0, axis2=1)
# print(sawp.shape)


"""np.squeeze(arr)"""
# arr = np.array([[[1, 2, 3]]])
# print(arr.shape)  # (1, 1, 3)

# squeezed = np.squeeze(arr)
# print(squeezed.shape)  # (3,)
# print(squeezed)

# arr = np.array([1, 2, 3])
# print(arr.shape)  # (3,)

# # Add a new axis at position 0
# expanded = np.expand_dims(arr, axis=0)
# arr = np.array([1, 2, 3])
# print(arr.shape)  # (3,)

# # Add a new axis at position 0
# expanded = np.expand_dims(arr, axis=0)
# print(expanded.shape)  # (1, 3)
# expanded = np.expand_dims(expanded, axis=0)
# print(expanded.shape)

# print(expanded.shape)  # (1, 3)
# expanded = np.expand_dims(expanded, axis=0)
# print(expanded.shape)
