'''
Question:
Remove all punctuation characters from a string.

Given a string, remove all punctuation characters
while keeping alphabets, digits, and spaces unchanged.

Punctuation includes characters such as:
! @ # $ % ^ & * ( ) , . ? : ; ' " - _

Test Cases:

1. Input:
   Hello, World!
   Output:
   Hello World

2. Input:
   Python is great!!!
   Output:
   Python is great

3. Input:
   Hello@World#2026
   Output:
   HelloWorld2026

4. Input:
   What's your name?
   Output:
   Whats your name

5. Input:
   Python-3.12
   Output:
   Python312

6. Input:
   Hello... World!!!
   Output:
   Hello World

7. Input:
   12345
   Output:
   12345

8. Input:
   !@#$%^&*()
   Output:
   Empty string
'''

punctuation="""!@#$%^&*(),.?:;'"-_"""
s=input("Enter The String: ")

new=""

for i in s:
    if i  not in punctuation:
        new+=i

if new:
    print(new)
else:
    print("Empty String")