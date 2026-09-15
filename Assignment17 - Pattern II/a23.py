'''
Docstring for Assignment17(Pattern-II).a23
a
a b
a . c
a . . d
a b c d e
'''


n=int(input("Enter the Number : "))

i=0
while i<n:
    if i<2:
        j=0
        while j<=i:
            print(chr(ord("a")+j),end=" ")
            j+=1
        
    elif i==n-1:
        j=0
        while j<n:
            print(chr(ord("a")+j),end=" ")
            j+=1

        
    else:
        j=0
        print("a",end=" ")
        while j<=i-2:
            print(".",end=" ")
            j+=1
        print(chr(ord("a")+i),end=" ")

    print()
    
    i+=1