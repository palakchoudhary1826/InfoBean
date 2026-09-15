'''

Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0

'''
valueInMb=int(input("Enter The Value In MB : "))
print(f"GB = {valueInMb/1024}")