import numpy as np
N,M,P = input().split()
N_array = []
M_array = []
for _ in range (int(N)):
    N_array.append(list(map(int,input().split())))
for _ in range (int(M)):
    M_array.append(list(map(int,input().split())))
arr1 = np.array(N_array)
arr2 = np.array(M_array)
print(np.concatenate((arr1,arr2),axis=0))