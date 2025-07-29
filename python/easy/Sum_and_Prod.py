import numpy as np
N,M = map(int,input().split())
temp =[]
for i in range(N):
    temp.append(list(map(int, input().split())))
arr = np.array(temp)
print(np.prod(np.sum(arr,axis=0)))