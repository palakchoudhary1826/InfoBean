'''
Docstring for Assignment17(Pattern-II).a47
. . . . 1
. . . 1 1
. . 1 * 1
. 1 * * 1
1 1 1 1 1

'''

n=int(input("The Number : "))

i=1
while i<=n:

    j=1
    while j<=n-i:
        print(".",end=" ")
        j+=1

    if i<=2:
        k=1
        while k<=i:
            print(1,end=" ")
            k+=1
    elif i==n:
        l=1
        while l<=n:
            print(1,end=" ")
            l+=1
               
    else:
        print(1,end=" ")
        l=1
        while l<=i-2:
            print("*",end=" ")
            l+=1
        print(1,end=" ")

    print()
    i+=1

