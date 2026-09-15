'''
Docstring for Assignment17(Pattern-II).a42
54321
5432
543
54
5

'''
n=int(input("Enter The Number : "))


i=1
while i<=n:
    j=1
    
    while j<=n-i+1:
        print(n-j+1,end=" ")
        j+=1
        
    print()
    
    
    i+=1