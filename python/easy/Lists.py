if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        cmd = input()
        cmd_trans = cmd.split(" ")
        cmd_str = cmd_trans[0]
        if cmd_str == "insert":
            lst.insert(int(cmd_trans[1]),int(cmd_trans[2]))

        elif cmd_str == "remove":
            lst.remove(int(cmd_trans[1]))

        elif cmd_str == "append":
            lst.append(int(cmd_trans[1]))

        elif cmd_str == "sort":
            lst.sort()

        elif cmd_str == "pop":
            lst.pop()

        elif cmd_str == "reverse":
            lst.reverse()

        elif cmd_str == "print":
            print(lst)
