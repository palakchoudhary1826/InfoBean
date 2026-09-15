'''
Docstring for a06
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''
n = int(input("Enter the number: "))
factor=1
small=0

i=2

while i<=n:
    if n%i==0:
        factor+=1
        # print(factor)
        if i>1 and small==0:
            small=i
    i+=1

if factor>=2:
    print(f"composite number")
    print(f"factor :{factor} (including {n})")
    print(f"small factor :{small}")
else:
    print(f"not composite")
