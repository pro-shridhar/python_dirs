import numpy as np
import os


arr = np.arange(12).reshape(3, 4)

header = "col1 col2 col3"

# Saving the array 'x' into a text file named 'temp.txt' using np.savetxt()
# Specifying the format as "%d" (integer) and including a header with column names
np.savetxt("Day_25/txtarr.txt", arr, fmt="%d", header=header)

if os.path.exists("Day_25/txtarr.txt"):
    result = np.loadtxt("Day_25/txtarr.txt")

    print(result)
