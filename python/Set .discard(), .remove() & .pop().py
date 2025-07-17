n = int(input())
numbers_set = set(map(int, input().split()))
N = int(input())

for j in range(N):
    cmd = input()
    cmd_trans = cmd.split(" ")
    cmd_str = cmd_trans[0]
    if cmd_str == "discard":
        numbers_set.discard(int(cmd_trans[1]))

    elif cmd_str == "remove":
        numbers_set.remove(int(cmd_trans[1]))

    elif cmd_str == "pop":
        numbers_set.pop() # run on python 3
        #numbers_set.remove(min(numbers_set)) # for code to work on Pypy 3
    
print(sum(numbers_set))