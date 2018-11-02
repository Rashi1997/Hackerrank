import numpy as np
n, m=map(int,(input()).split())

np_array=np.array([list(map(int,(input()).split())) for j in range(n)])
print(np.transpose(np_array))
print(np_array.flatten())
