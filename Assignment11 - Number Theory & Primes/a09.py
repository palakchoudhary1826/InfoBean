'''
Docstring for a09
Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
n=int(input("Enter The Number : "))
eve=0
odd=0

while n>0:
    d=n%10
    if d%2!=0:
        odd+=1
    else:
        eve+=1
    n//=10

print(f"Even Count :{eve}")
print(f"Odd Count :{odd}")
diff=abs(odd-eve)
print(f"Difference :{diff}")

flag=True

if diff <= 1:
    flag=False
else:
    i = 2
    while i * i <= diff:
        if diff % i == 0:
            flag=False
            break
        i += 1
    else:
        flag=True

if flag:
    print("prime number")
else:
    print("Not prime number")
