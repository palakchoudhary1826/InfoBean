'''
Docstring for Assignment17(Pattern-II).a47
. . . . A 
. . . A B
. . A - C
. A - - D
A B C D E

'''

n=int(input("The Number : "))

i=0
while i<n:

    j=0
    while j<n-i-1:
        print(".",end=" ")
        j+=1

    if i<=1:
        k=0
        while k<=i:
            print(chr(ord('A')+k),end=" ")
            k+=1
    elif i==n-1:
        l=0
        while l<=i:
            print(chr(ord('A')+l),end=" ")
            l+=1
               
    else:
        print("A",end=" ")
        l=1
        while l<=i-1:
            print("-",end=" ")
            l+=1
        print(chr(ord('A')+i),end=" ")

    print()
    i+=1


