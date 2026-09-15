'''
A
BCD
EFGHI
JKLMNOP
'''

n=int(input("Enter The Number : "))
s=1

i=0
while i<n:
    j=0
    
    while j<s:
        print(chr(ord("A")+i*i+j),end=" ")
        j+=1
        
    print()
    
    s+=2
    i+=1