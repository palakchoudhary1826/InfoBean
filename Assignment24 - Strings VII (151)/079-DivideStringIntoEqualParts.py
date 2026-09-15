'''
Divide a String into N Equal Parts

Write a Python program to input a string and divide it into
N equal parts.

If the string cannot be divided into N equal parts, display
"Cannot divide equally".

Input:
Enter a string: abcdefgh
Enter number of parts: 4

Output:
ab
cd
ef
gh
'''

s=input("Enter the String : ")
n=int(input("Enter number of partss : "))
size=n//2
for i in range(0,len(s),size):
    print(s[i:i+size])
