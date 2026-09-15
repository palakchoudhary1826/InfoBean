n=int(input("The Number : "))

i=1
while i<=n:
    # j=1
    # while j<=n-i:
    #     print(" ",end=" ")
    #     j+=1
    
    if i<=2:
        j=1
        while j<=i:
            print(1,end=" ")
            j+=1
        
    else:
        j=1
        print(1,end=" ")
        while j<=i-2:
            print(i-1,end=" ")
            j+=1
        print(1,end=" ")
    print()
    i+=1



    

