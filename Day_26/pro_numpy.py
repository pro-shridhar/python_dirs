from scipy.datasets import face

img = face()
print(img.shape)

import matplotlib.pyplot as plt

plt.gray()
plt.imshow(img)
plt.show()
