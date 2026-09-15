'''
Create a String from a Byte Array

Write a Python program to create a string from a given
byte array.

Input:
[72, 101, 108, 108, 111]

Output:
Hello
'''


arr = list(input("Enter The Unicode : ").split())

s = ""

for i in arr:
    s += chr(int(i))

print(s)