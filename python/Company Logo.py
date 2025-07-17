# Enter your code here. Read input from STDIN. Print output to STDOUT
from unicodedata import numeric

logo = input()
count_list = []
unique_list= []

for letter in logo:
    c = logo.count(letter)
    if letter not in unique_list:
        temp = [letter,c]
        count_list.append(temp)
        unique_list.append(letter)
        unique_list.sort()


#print("Count =",count_list)
# sort count list based on letters count
sorted_list = sorted(count_list,key=lambda x:x[1],reverse=True)
#print("sorted = ", sorted_list )


# if first 3 are equal
if sorted_list[0][1] == sorted_list[1][1] and sorted_list[2][1] == sorted_list[1][1]:
    s = sorted(sorted_list) # sort the list alphabitically
    [print(s[i][0], s[i][1]) for i in range(3)]
# if third and fourth are equal
elif sorted_list[3][1] == sorted_list[2][1]:
    comp = sorted([sorted_list[3],sorted_list[2]])
    res = [sorted_list[0],sorted_list[1],comp[0]]
    [print(res[i][0], res[i][1]) for i in range(3)]
# if second and third are equal
elif sorted_list[1][1] == sorted_list[2][1]:
    comp = sorted([sorted_list[1],sorted_list[2]])
    res = [sorted_list[0],comp[0],comp[1]]
    [print(res[i][0], res[i][1]) for i in range(3)]
# if first and second are equal
elif sorted_list[1][1] == sorted_list[0][1]:
    comp = sorted([sorted_list[1],sorted_list[0]])
    res = [comp[0],comp[1],sorted_list[2]]
    [print(res[i][0], res[i][1]) for i in range(3)]
#else
else:
    [print(sorted_list[i][0], sorted_list[i][1]) for i in range(3)]
