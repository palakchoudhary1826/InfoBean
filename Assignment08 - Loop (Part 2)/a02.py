'''

2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''

n=int(input("Enter The Num : "))
min=n%10

while n>0:
    d=n%10
    if min>d:
        min=d
    n//=10
    
print(f"Largest Digit : {min}")