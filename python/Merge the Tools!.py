def merge_the_tools(string, k):
    # your code goes here 
    # AAB CAA ADA ACA   k = 3  and n = 4
    result = []
    lst = []

    n = int(len(string) / k)
    #divide the string into sets
    for i in range(n): #iterate on whole string 0:AAB 1:CAA 2:ADA 3:ACA
        temp = []
        for j in range(k):
            temp.append(string[j+(k*i)])
        s="".join(temp)
        lst.append(s)

    for word in lst:
        unique = ""
        for letter in word:
            if letter not in unique:
                unique += letter
        result.append(unique)

    print("\n".join(result))
    return


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)