'''
Question:
Remove all digits from a string.

Given a string, remove all numeric digits (0-9)
from the string while keeping letters, spaces,
and special characters unchanged.

Test Cases:

1. Input:
   hello123
   Output:
   hello

2. Input:
   12345
   Output:
   Empty string

3. Input:
   hello123world
   Output:
   helloworld

4. Input:
   Python 3.12
   Output:
   Python .

5. Input:
   abc@123#xyz
   Output:
   abc@#xyz

6. Input:
   123 hello 456
   Output:
   hello

7. Input:
   hello!
   Output:
   hello!

8. Input:
   2026
   Output:
   Empty string
'''

s=input("Enter The String : ")
digit="0123456789"
new=""
for i in s:
    if i not in digit:
        new+=i

if new:
    print(new)
else:
    print("Empty String")