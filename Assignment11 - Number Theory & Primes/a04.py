'''
Docstring for a04
Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''
n = int(input("Enter the number: "))
flag=True
ans=0

if n <= 1:
    flag=False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            flag=False
            break
        i += 1
    else:
        flag=True

if flag:
    print("Prime")
    flag=True
    n1=n+1
    
    while n1<(n*2):
        i=2
        while i*i<=n1:
            if n1%i==0:
                flag=False
                break
            i+=1
        if flag:
            ans=n1
            break
        else:
            flag=True
            n1+=1
    print(f"next prime :{ans}")

else:
    print("Not Prime")
    flag=True
    n2=n-1
    
    while n2>1:
        i=2
        while i*i<=n2:
            if n2%i==0:
                flag=False
                break
            i+=1
        if flag:
            ans=n2
            break
        else:
            flag=True
            n2-=1
    print(f"Previous Prime :{ans}")


