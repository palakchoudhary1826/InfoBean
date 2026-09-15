'''
Docstring for Assignment17(Pattern-II).a28
1 
1 2 3
1 2 3 4 5
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
'''

n=int(input("Enter The Number : "))

i=1
while i<=n:
    if i%2!=0:
        j=1
        while j<=i:
            print(j,end=" ")
            j+=1
        print()
   
    i+=1
    
    
