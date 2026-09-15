'''
Question:
Replace all consonants in a string with '*'.

Given a string, replace every consonant with '*'
while keeping vowels, digits, spaces, and special
characters unchanged.

Vowels:
a, e, i, o, u
A, E, I, O, U

Test Cases:

1. Input:
   hello
   Output:
   *e**o

2. Input:
   python
   Output:
   *y**o*

3. Input:
   Hello World
   Output:
   *e**o *o***

4. Input:
   abcdef
   Output:
   *b*d*f

5. Input:
   123 hello!
   Output:
   123 *e**o!

6. Input:
   AEIOU
   Output:
   AEIOU

7. Input:
   xyz
   Output:
   ***

8. Input:
   "hello@123"
   Output:
   "*e**o@123"
'''

s=input("Enter The String : ")
new=""
vowel="aeiou"
num="0123456789"
special="!@#$%^&*()~ "
for i in s:
    if i not in vowel and i not in num and i not in special:
        new=new+"*"
    else:
        new=new+i

print(new) 