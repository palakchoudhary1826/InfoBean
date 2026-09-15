'''
Docstring for Assignment17(Pattern-II).a50
The Number : 5

A B C D E 
. A B C D
. . A B C
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
    k=0
    while k<n-i:
        print(chr(ord('A')+k),end=" ")
        k+=1
    
   
    print()
    i+=1