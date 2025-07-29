import numpy as np
N,M = map(int,input().split())
temp =[]
for _ in range(N):
    temp.append(list(map(int, input().split())))
arr = np.array(temp)
print(np.max(np.min(arr,axis=1)))