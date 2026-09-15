'''
Docstring for Assignment17(Pattern-II).a36
A B C D E 
A . . D 
A . C 
A B 
A 
'''
n=int(input("Enter The Number : "))

i=0

while i<n:
    if i==0:
        j=0
        while j<n-i:
            print(chr(ord('A')+j),end=" ")
            j+=1
    
    elif i>0 and i<n-1:
        j=0
        print('A',end=" ")
        while j<n-(i+2):
            print(".",end=" ")
            j+=1
        print(chr(ord('A')+(n-i-1)),end=" ")

    else:
        j=0
        while j<n-i:
            print(chr(ord('A')+j),end=" ")
            j+=1
    print()
    i+=1
