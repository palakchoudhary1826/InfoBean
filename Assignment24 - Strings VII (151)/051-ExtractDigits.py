'''
Question:
Extract only digits from a string.

Given a string, extract and print only the
digits (0-9) present in the string.
Remove/ignore all letters, spaces, and
special characters.

Test Cases:

1. Input:
   hello123
   Output:
   123

2. Input:
   abc123xyz456
   Output:
   123456

3. Input:
   Python 3.12
   Output:
   312

4. Input:
   abc@123#45
   Output:
   12345

5. Input:
   12345
   Output:
   12345

6. Input:
   hello world
   Output:
   Empty string

7. Input:
   My age is 21!
   Output:
   21

8. Input:
   2026-08-20
   Output:
   20260820
'''

s=input("Enter The String : ")
digit="0123456789"
new=""
for i in s:
    if i  in digit:
        new+=i

if new:
    print(new)
else:
    print("Empty String")