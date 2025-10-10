import numpy as np

arr1 = np.random.rand(6)
print(arr1)

# 170 is mean and 10 is a standerd deviation
arr2 = np.random.randn(3, 4) * 10 + 170
print(arr2)

# element between 15 to 3 without repitation
arr3 = np.random.choice([2, 3, 4, 5, 6], size=5, replace=False)
print(arr3)

arr4 = np.random.choice([2, 3, 4, 5, 6], p=[0.07, 0.33, 0.33, 0.22, 0.05], size=10)
print(arr4)

# in randint you need to specifi size as a szie = (m,n)
# np.random.randint(1, 6, size=(2, 3))
