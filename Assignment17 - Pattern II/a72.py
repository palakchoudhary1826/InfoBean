'''
Docstring for a72
Enter the number 5
A   B   C   D   E   
  A   B   C   D   
    A   B   C   
      A   B   
        A  
'''
n=int(input("Enter the number "))

i=0

while i<n:

    j=0
    while j<i:
        print(" ",end=" ")
        j+=1

    k=0
    while k<=n-i-1:
        print(chr(ord("A")+k),end="   ")
        k+=1

    

    print()
    i+=1