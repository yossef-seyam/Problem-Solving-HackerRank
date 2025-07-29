# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

num = input()
number = []
for i in num:
    number.append(int(i))
for key,n in groupby(number):
    print((len(list(n)), key) ,end=" ")