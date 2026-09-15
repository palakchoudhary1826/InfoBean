'''
Docstring for Assignment17(Pattern-II).a54
The Number : 5
A B C D E 
. A - - D
. . A - C
. . . A B
. . . . A
'''
n=int(input("The Number : "))

i=0
while i<n:
    j=0

    while j<=i-1:
        print(".",end=" ")
        j+=1

    if i==0:
        k=0
        while k<n-i:
            print(chr(ord("A")+k),end=" ")
            k+=1

    elif i>=n-2:
        k=0
        while k<n-i:
            print(chr(ord("A")+k),end=" ")
            k+=1
    else:
        print("A",end=" ")
        k=1
        while k<n-i-1:
            print("-",end=" ")
            k+=1
        print(chr(ord('A')+n-i-1),end=" ")
   
    print()
    i+=1