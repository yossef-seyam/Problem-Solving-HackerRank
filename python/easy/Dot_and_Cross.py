import numpy as np
N=int(input())
temp =[]
for _ in range(N*2):
    temp.append(list(map(int, input().split())))
arr1 = np.array(temp[:N])
arr2 = np.array(temp[N:])
print(np.dot(arr1,arr2))