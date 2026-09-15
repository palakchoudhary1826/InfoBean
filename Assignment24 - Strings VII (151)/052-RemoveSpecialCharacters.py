'''
Question:
Remove all special characters from a string.

Given a string, remove all special characters
while keeping alphabets, digits, and spaces unchanged.

Special characters include:
! @ # $ % ^ & * ( ) _ - + = etc.

Test Cases:

1. Input:
   hello@world!
   Output:
   helloworld

2. Input:
   Hello, World!
   Output:
   Hello World

3. Input:
   abc@123#xyz
   Output:
   abc123xyz

4. Input:
   Python_3.12
   Output:
   Python312

5. Input:
   Hello! 123 @ Python
   Output:
   Hello 123  Python

6. Input:
   abc123
   Output:
   abc123

7. Input:
   @#$%^&*
   Output:
   Empty string

8. Input:
   Hello World 123
   Output:
   Hello World 123
'''

s=input("Enter The String : ")
new=""
# special = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
# for i in s:
#     if i  not in special:
#         new+=i

# if new:
#     print(new)
# else:
#     print("Empty String")

#! approach 2

for i in s:
    x=ord(i)

    if(65<=x<=90 or 97<=x<=122 or 48<=x<=57 or x==32):
        new+=i
print(new)