'''
Assignment 2: Binary Converter for Embedded System

Task:
Write a recursive function to convert a decimal number
into its binary representation.

Input:
Enter a decimal number:
25

Output:
Binary Number = 11001
'''
s=""
def binary(n):
    global s
    if n==0:
        return s
    
    s+=str(n%2)   
    
    return binary(n//2)
    

binary(25)
print(s[::-1])
