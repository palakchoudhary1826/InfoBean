'''
Docstring for a78
Enter The Number : 5
        1 
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
'''
n=int(input("Enter The Number : "))

i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    
    k=1
    while k<=i:
        print(k,end=" ")
        k+=1
    
    print()
    i+=1

n1=n-1
j=1
while j<=n1:
    k=1
    while k<=j:
        print(" ",end=" ")
        k+=1

    l=1
    while l<=n1-j+1:
        print(l,end=" ")
        l+=1

    print()
    j+=1 
