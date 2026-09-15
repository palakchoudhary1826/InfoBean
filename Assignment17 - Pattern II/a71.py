'''
Docstring for a69
Enter the number 5
1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
'''

n=int(input("Enter the number "))

i=1

while i<=n:
    j=1
    while j<=i-1:
        print(" ",end=" ")
        j+=1

    k=1

    while k<=2*(n-i)+1:
        print(k,end=" ")
        k+=1

    print()
    i+=1
