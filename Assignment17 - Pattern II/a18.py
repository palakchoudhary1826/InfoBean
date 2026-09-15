'''
Docstring for Assignment17(Pattern-II).a18
1
10
101
1010
10101

'''

n=int(input("Enter The Number  : "))

i=0
while i<=n:
    j=0
    while j<i:
        if j%2!=0:
            print(0,end=" ")
        else:
            print(1,end=" ")
        j+=1
    print()
    i+=1
