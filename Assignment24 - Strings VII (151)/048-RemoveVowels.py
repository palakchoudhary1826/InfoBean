'''
Question:
Remove all vowels from a string.

Given a string, remove all vowels
(a, e, i, o, u) from it and print the
resulting string.

Test Cases:

1. Input:
   hello world
   Output:
   hll wrld

2. Input:
   education
   Output:
   dctn

3. Input:
   python
   Output:
   pythn

4. Input:
   AEIOU
   Output:
   Empty string

5. Input:
   xyz
   Output:
   xyz
'''

s=input("Enter The String : ")
new=""

for i in s:
    if i not in "aeiouAEIOU":
        new=new+i;

if new:
    print(new)
else:
    print("empty string")