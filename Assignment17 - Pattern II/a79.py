'''
Docstring for a76
Enter The Input :5
Enter The Input :5
1 
1 2
1 . 3
1 . . 4
1 . . . 5
1 . . 4
1 . 3
1 2
1
'''
n=int(input("Enter The Input :"))

i=1
while i<=n:
    
    if i<=2:
        j=1
        while j<=i:
            print(j,end=" ")
            j+=1
    else:
        j=1
        print(1,end=" ")
        while j<=i-2:
            print(".",end=" ")
            j+=1
        print(i,end=" ")


    print()
    i+=1

n1=n-1
j=1
while j<=n1:
    if j>=n1-1:
        k=1
        while k<=n1-j+1:
            print(k,end=" ")
            k+=1
    else:
        k=1
        print(1,end=" ")
        while k<=n1-j-1:
            print(".",end=" ")
            k+=1
        print(n1-j+1,end=" ")

    
    print()
    j+=1