"""
The Number : 5
        * 
      *   *
    *       *
  *           *
* * * * * * * * *
"""
n=int(input("The Number : "))
i=1
while i<=n:

    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    if i==1 :
        k=1 
        while k<=i:
            print("*",end=" ")
            k+=1

    elif i==n:
        k=1
        while k<=2*i-1:
            print("*",end=" ")
            k+=1
    
    else:
        k=1
        print("*",end=" ")
        while k<=(2*i-1)-2:
            print(" ",end=" ")
            k+=1
        print("*",end=" ")

    print()
    i+=1