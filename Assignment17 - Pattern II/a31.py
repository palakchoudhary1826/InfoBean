'''
Docstring for Assignment17(Pattern-II).a31
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''

n=int(input("Enter The Number : "))
i=n
while i>=1:
    
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
        
    print()
    i-=1
    