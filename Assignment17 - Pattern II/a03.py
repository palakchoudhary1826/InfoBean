'''
Docstring for Assignment17(Pattern-II).a03
*
.*
..*
...*
....*

'''

n=int(input("The Number Of Range : "))

i=0

while i<n:
    k=0
    while k<i:
        print(".",end=" ")
        k+=1
    print("*")
    
    print()
    i+=1