'''
A 
A B
A B C
A B C D
A B C D E
'''
n=int(input("Enter The Number : "))

i=0
while i<n:
    j=0
    while j<=i:
        
        print(chr(ord("A")+j),end=" ")
        j+=1
    print()
    i+=1