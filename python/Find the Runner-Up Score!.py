if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = list(arr)
    for i in range(lst.count(max(lst))):
        lst.remove(max(lst))
    print(max(lst))