#run on python 2
if _name_ == '_main_':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list) 
    print hash(t)