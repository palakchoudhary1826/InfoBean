'''
Docstring for Assignment17(Pattern-II).a25
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

'''
n=int(input("Enter The Number : "))

i=1
while i<=n:
    j=1
    while j<=i:
        print(n-j+1,end=" ")
        j+=1
    print()
    i+=1
