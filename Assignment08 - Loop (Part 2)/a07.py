'''
Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32

'''

n1=int(input("Enter The Base Num : "))
n2=int(input("Enter The Power Num : "))
p=1
i=1

while i<=n2:
    p=p*n1
    i+=1

print(f"Output : {p}")
    