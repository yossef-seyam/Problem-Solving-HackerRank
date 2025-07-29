import numpy as np
N=int(input())
temp =[]
for _ in range(N):
    temp.append(list(map(float, input().split())))
arr = np.array(temp)
print(round(np.linalg.det(arr),2))