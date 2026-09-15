'''
Docstring for a89
Enter The Number : 5
        1 
      1 0 1 
    1 0 1 0 1 
  1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 

'''
n=int(input("Enter The Number : "))


i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    k=1
    while k<=2*i-1:
        if k%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
        k+=1
    print()
    i+=1