'''   '''
# 5 5 5 5 5
# 4 . . 4
# 3 . 3
# 2 2
# 1

n=int(input("Enter The Number : "))
i=1

while i<=n:
    if i==1:
        j=1
        while j<=n-i+1:
            print(n,end=" ")
            j+=1
    
    elif i>1 and i<n-1:
        j=1
        print(n-i+1,end=" ")
        while j<=n-(i+1):
            print(".",end=" ")
            j+=1
        print(n-i+1,end=" ")

    else:
        j=1
        while j<=n-i+1:
            print(n-i+1,end=" ")
            j+=1
    print()
    i+=1
