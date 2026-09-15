"""
Generate a Hash Code for a Given String

Write a Python program to generate a hash code for a given string
without using Python's built-in hash() function.

Algorithm:
1. Initialize a hash value.
2. Traverse each character of the string.
3. Convert the character into its ASCII/Unicode value.
4. Update the hash using the formula:

       hash = hash * 31 + ord(character)

5. Return the final hash value.

Input:
Enter the string: hello

Output:
Hash Code: 99162322

Constraints:
- 1 <= length of string <= 10^5
- The string may contain uppercase letters, lowercase letters,
  digits, spaces, and special characters.
- Do not use hash().
"""


s=input("Enter The String  : ")

hash=0

for i in s:
    hash=hash*31+ord(i)

print(f"hash value of '{s}' is : {hash}")