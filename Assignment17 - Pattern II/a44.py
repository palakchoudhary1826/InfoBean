'''
. . . . 1 
. . . 2 2
. . 3 3 3
. 4 4 4 4
5 5 5 5 5

'''

n=int(input("The Number : "))

i=1
while i<=n:

    j=1
    while j<=n-i:
        print(".",end=" ")
        j+=1
    k=1
    while k<=i:
        print(i,end=" ")
        k+=1
    print()
    i+=1
