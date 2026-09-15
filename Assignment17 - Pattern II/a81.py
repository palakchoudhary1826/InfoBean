n=int(input("The Number : "))

i=1
while i<=n:

    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    k=1
    while k<=2*i-1:
        print("*",end=" ")
        k+=1
    

    print()
    i+=1

i=n-1
while i>=1:

    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    k=1
    while k<=2*i-1:
        print("*",end=" ")
        k+=1
    

    print()
    i+=1