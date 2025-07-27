import numpy as np
N,M = input().split()
lst=[]
for i in range(int(N)):
    lst.append(list(map(int,input().split())))
arr = np.array(lst)
print(arr.transpose())
print(arr.flatten())