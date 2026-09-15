'''
Docstring for Assignment17(Pattern-II).a15
A 
B B
C C C
D D D D
E E E E E

'''

n=int(input("Enter The Number : "))

i=0
while i<n:
    j=0
    while j<=i:
        
        print(chr(ord("A")+i),end=" ")
        j+=1
    print()
    i+=1