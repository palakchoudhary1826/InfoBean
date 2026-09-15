'''
Docstring for Assignment17(Pattern-II).a12
a
a b
a b c
a b c d
a b c d e
'''

n=int(input("Enter The Number : "))

i=0
while i<=n:
    j=0
    while j<i:
        
        print(chr(ord("a")+j),end=" ")
        j+=1
    print()
    i+=1