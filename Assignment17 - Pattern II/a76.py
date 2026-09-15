'''
Docstring for a76
Enter The Input :5
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
n=int(input("Enter The Input :"))

i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1

n1=n-1
j=1
while j<=n1:
    k=1
    while k<=n1-j+1:
        print("*",end=" ")
        k+=1
    print()
    j+=1