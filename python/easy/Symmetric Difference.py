N = int(input())
s1 =set(input().split())
M = int(input())
s2 =set(input().split())

[print(i) for i in sorted([int(num) for num in s1.union(s2) - s1.intersection(s2)])]
