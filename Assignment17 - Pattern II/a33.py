'''
Docstring for Assignment17(Pattern-II).a33
A B C D E 
A B C D
A B C
A B
A
'''





n=int(input("Enter The Number : "))
i=0
while i<n:
    
    j=0
    while j<n-i:
        print(chr(ord("A")+j),end=" ")
        j+=1
        
    print()
    i+=1
    