'''
Docstring for a76
Enter The Input :5
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
n=int(input("Enter The Input :"))

i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1

n1=n-1
j=1
while j<=n1:
    k=1
    while k<=n1-j+1:
        print(k,end=" ")
        k+=1
    print()
    j+=1