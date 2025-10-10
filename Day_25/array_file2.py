import numpy as np
import os


arr = np.arange(20)
arr1 = np.arange(20, 40)

np.savez("Day_25/2arr.npz", arr=arr, arr1=arr1)

if os.path.exists("Day_25/2arr.npz"):
    with np.load("Day_25/2arr.npz") as data:
        a = data["arr"]
        b = data["arr1"]

        print(a)
        print(b)
