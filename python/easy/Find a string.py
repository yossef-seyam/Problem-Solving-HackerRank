def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        pos = string.find(sub_string, start)
        if pos != -1:
            count += 1
            start = pos + 1  # Move by 1 to catch overlapping
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)