'''
Docstring for Assignment17(Pattern-II).a30
* * * * * 
* * * * 
* * * 
* * 
* 
'''


n=int(input("Enter The Number : "))

i=1
while i<=n:
    
    j=n
    while j>=i:
        print("*",end=" ")
        j-=1
        
    print()
    i+=1
    