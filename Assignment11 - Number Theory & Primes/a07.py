'''
Docstring for a07
Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''
n=int(input("Enter The Number : "))

sum=0
while n>0:
    d=n%10
    sum+=d
    n//=10

print(f"sum :{sum}")

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
    print("lucky Number")
else:
    print("Not Lucky Number")