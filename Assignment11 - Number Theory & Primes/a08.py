'''
Docstring for a08
Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''

n=int(input("Enter The Number : "))
max=0
min=n%10

while n>0:
    d=n%10
    max=max if max>d else d
    min=min if min<d else d
    n//=10

print(f"Largest Number : {max}")
print(f"Smallest Number : {min}")
sum=max+min
print(f"Sum :{sum}")

flag=True

if sum <= 1:
    flag=False
else:
    i = 2
    while i * i <= sum:
        if sum % i == 0:
            flag=False
            break
        i += 1
    else:
        flag=True

if flag:
    print("prime number")
else:
    print("Not prime number")
