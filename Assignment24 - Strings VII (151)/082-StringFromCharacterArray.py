'''
Create a String from a Character Array

Write a Python program to create a string from a given
character array.

Input:
['H', 'e', 'l', 'l', 'o']

Output:
Hello
'''

arr = list(input("Enter characters: "))
print(arr)

s = ""

for ch in arr:
    s += ch

print(s)