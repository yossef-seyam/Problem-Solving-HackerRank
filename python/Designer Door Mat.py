# Enter your code here. Read input from STDIN. Print output to STDOUT
s= input()
ss= s.split(" ")
N,M = int(ss[0]),int(ss[1])
mid= N//2  #7 21   mid = 4
for i in range(N):

    if i<mid:
        print((".|."*((i*2)+1)).center(M,"-"))
    elif i>mid:
        print((".|."*(2*(N-i)-1)).center(M,"-")) #I am the king 
    else:
        print("WELCOME".center(M,"-"))
