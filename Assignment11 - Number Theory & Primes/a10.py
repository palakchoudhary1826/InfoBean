'''
Docstring for a10
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime

'''
n=int(input("Enter The Number : "))
zeroCount=0
sum=0
small=0

while n>0:
    d=n%10
    if d==0:
        zeroCount+=1
    sum+=d
    small=small if small<d else d
    n//=10
print(f"Zero Count : {zeroCount}")
print(f"Sum :{sum}")
print(f"Smallest Digit :{small}")
final=sum*small
print(f"Final Result :{final}")

flag=True

if final <= 1:
    flag=False
else:
    i = 2
    while i * i <= final:
        if final % i == 0:
            flag=False
            break
        i += 1
    else:
        flag=True

if flag:
    print("prime number")
else:
    print("Not prime number")
