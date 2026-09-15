'''
Docstring for Assignment17(Pattern-II).a22
A
A B
A . C
A . . D
A B C D E
'''

n=int(input("Enter the Number : "))

i=0
while i<n:
    if i<2:
        j=0
        while j<=i:
            print(chr(ord("A")+j),end=" ")
            j+=1
        
    elif i==n-1:
        j=0
        while j<n:
            print(chr(ord("A")+j),end=" ")
            j+=1

        
    else:
        j=0
        print("A",end=" ")
        while j<=i-2:
            print(".",end=" ")
            j+=1
        print(chr(ord("A")+i),end=" ")

    print()
    
    i+=1