'''
Docstring for Assignment17(Pattern-II).a34
E E E E E 
D D D D
C C C
B B
A
'''
n=int(input("Enter The Number : "))
i=0
while i<n:
    
    j=0
    while j<n-i:
        print(chr(ord("E")-i),end=" ")
        j+=1
        
    print()
    i+=1
    