import numpy as np
N,M = map(int,input().split())
temp =[]
for _ in range(N):
    temp.append(list(map(int, input().split())))
arr = np.array(temp)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(round(np.std(arr,axis=None),11))