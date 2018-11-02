import numpy as np
n=int(input())
arr=np.array([list(map(float, input().split())) for i in range(n)])
print (np.linalg.det(arr))
