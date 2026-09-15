"""
The Number : 5
                A 
              B   B
            C       C
          D           D
        E E E E E E E E E
"""
n=int(input("The Number : "))
i=0
while i<n:

    j=0
    while j<=n-i+2:
        print(" ",end=" ")
        j+=1

    if i==0 :
        print("A",end=" ")

    elif i==n-1:
        k=0
        while k<2*i+1:
            print(chr(ord("A")+i),end=" ")
            k+=1
    
    else:
        k=1
        print(chr(ord("A")+i),end=" ")
        while k<=(2*i-1):
            print(" ",end=" ")
            k+=1
        print(chr(ord("A")+i),end=" ")

    print()
    i+=1