"""
The Number : 5
        1 
      1 * 1
    1 * * * 1
  1 * * * * * 1
1 1 1 1 1 1 1 1 1
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
            print("1",end=" ")
            k+=1

    elif i==n:
        k=1
        while k<=2*i-1:
            print("1",end=" ")
            k+=1
    
    else:
        k=1
        print("1",end=" ")
        while k<=(2*i-1)-2:
            print("*",end=" ")
            k+=1
        print("1",end=" ")

    print()
    i+=1