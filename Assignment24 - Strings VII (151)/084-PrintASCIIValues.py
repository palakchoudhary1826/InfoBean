'''
Print ASCII Value of Each Character

Write a Python program to input a string and print the
ASCII value of each character in the string.

Input:
Hello

Output:
H = 72
e = 101
l = 108
l = 108
o = 111
'''


s=input("Enter The Strig : ")

for i in s:
    print(f"{i} = {ord(i)}")