import numpy as np
import os


arr = np.arange(20)
np.save("Day_25/temp_arra.npy", arr)

if os.path.exists("Day_25/temp_arra.npy"):

    data = np.load("Day_25/temp_arra.npy")
    print(data)
