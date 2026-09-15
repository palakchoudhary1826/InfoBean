'''
Problem:
Check whether one string is a substring of another
using only concatenation.

Example:
s = "hello"
sub = "ell"

Expected Output:
True


Test Case 1:
s = "hello"
sub = "ell"
Output: True

Test Case 2:
s = "hello"
sub = "world"
Output: False

Test Case 3:
s = "aaaaa"
sub = "aaa"
Output: True

Test Case 4:
s = "python"
sub = "thon"
Output: True

Test Case 5:
s = "python"
sub = "java"
Output: False
'''

s=input("Enter The String  : ")
sub=input("Enter The Sub String : ")

found=False

for i in range(len(s)-len(sub)+1):
    temp=""
    for j in range(i,i+len(sub)):
        temp=temp+s[j]
    
    if temp==sub:
        found=True
        break

print(found)