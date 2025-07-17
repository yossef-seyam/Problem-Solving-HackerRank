from pkgutil import resolve_name

if __name__ == '__main__':
    s = input()
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smal = cap.lower()
    dig = "0123456789"
    flag = 0
    for i in s:
        flag = 0
        if i in cap or i in smal or i in dig:
            print("True")
            flag = 1
            break
    if flag == 0:
        print("False")

    for i in s:
        flag = 0
        if i in cap or i in smal:
            print("True")
            flag = 1
            break
    if flag == 0:
        print("False")

    for i in s:
        flag = 0
        if i in dig:
            print("True")
            flag = 1
            break
    if flag == 0:
        print("False")

    for i in s:
        flag = 0
        if i.islower() == 1:
            print("True")
            flag = 1
            break
    if flag == 0:
        print("False")

    for i in s:
        flag = 0
        if i.isupper() == 1:
            print("True")
            flag = 1
            break
    if flag == 0:
        print("False")
