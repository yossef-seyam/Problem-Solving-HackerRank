import numpy as np


numbers = list(map(int, input().split()))
arr = np.array(numbers)
print(arr.reshape(3,3))