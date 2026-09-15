'''
Docstring for Assignment17(Pattern-II).a06
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''

n=int(input("Enter The Number : "))

i=1
while i<=n:
    j=1
    while j<=n:
        print(i,end=" ")
        j+=1
    print()
    i+=1