'''
Docstring for Assignment17(Pattern-II).a07

1 
0 0
1 1 1
0 0 0 0
1 1 1 1 1
'''

n=int(input("Enter The Number : "))

i=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print(1,end=" ")
        else:
            print(0,end=" ")
        j+=1
    print()
    i+=1