'''
Docstring for a03
Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
'''
n = int(input("Enter the number: "))

if n <= 1:
    print("Not Composite")
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("Composite")
            break
        i += 1
    else:
        print("Not Composite")