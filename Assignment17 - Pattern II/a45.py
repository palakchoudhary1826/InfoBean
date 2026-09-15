'''
The Number : 5
. . . . 5 
. . . 4 4
. . 3 3 3
. 2 2 2 2
1 1 1 1 1


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
        print(n-i+1,end=" ")
        k+=1
    print()
    i+=1

