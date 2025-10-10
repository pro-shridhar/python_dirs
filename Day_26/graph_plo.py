import scipy
from scipy.datasets import electrocardiogram
import numpy as np
import matplotlib.pyplot as plt

scipy.datasets.download_all(".")
ecg = electrocardiogram()
# print(ecg)
# print(ecg.shape, ecg.mean(), ecg.std())

# fs = 360
# time = np.arange(ecg.size) / fs
# plt.plot(time, ecg)
# plt.xlabel("time in s")
# plt.ylabel("ECG in mV")
# plt.xlim(9, 10.2)
# plt.ylim(-1, 1.5)
# plt.show()
