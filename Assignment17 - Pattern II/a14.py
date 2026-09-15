'''
Docstring for Assignment17(Pattern-II).a14


1
2 3
4 5 6
7 8 9 10
'''

n=int(input("Enter The Number : "))

c=1

i=0
while i<n:
    j=0
    while j<i:
        print(c,end=" ")
        c+=1
        j+=1
        
    print()
    i+=1