'''
Count the Sum of Digits Present in a String

Write a Python program to input a string and find the
sum of all digits present in the string.

Only numeric characters (0-9) should be considered.
Alphabets, spaces, and special characters should be ignored.

Input:
Enter a string: abc12de3

Output:
Sum of Digits: 6
'''

s=input("Enter The String : ")

sum=0

for i in s:
    if '0'<=i<='9':
        sum+=int(i)

print(sum)