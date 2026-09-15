'''
Docstring for a87

Enter The  Number 5
        1 
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''

n=int(input("Enter The  Number "))

i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    
    k=1
    
    while k<=i-1:        
        print(i-k+1,end=" ")
        
        k+=1
    
    print(1,end=" ")
        
    l=2
    while l<=i:        
        print(l,end=" ")
        l+=1
        
    print()
   
    i+=1
