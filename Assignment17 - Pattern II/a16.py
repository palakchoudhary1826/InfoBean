'''
Docstring for Assignment17(Pattern-II).a16


a 
b c
d e f
g h i j
k l m n o

'''


n=int(input("Enter The Number : "))
c=0
i=0
while i<n:
    j=0
    while j<=i:
        
        print(chr(ord("a")+c),end=" ")
        c+=1
        j+=1
    print()
    i+=1