def minion_game(string):
    s, k=0, 0

    for i in range(len(string)):
        if string[i] in "AEIOU":
            k += len(string[i:])
        else:
            s += len(string[i:])

    if k>s:
        print("Kevin",k)
    elif s>k:
        print("Stuart",s)
    else:
        print("Draw")







if __name__ == '__main__':
    s = input()
    minion_game(s)