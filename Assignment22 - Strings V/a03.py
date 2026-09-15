'''
Docstring for Assignment22 - String V.a03
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''


n=input("Enter : ")
new=""

for i in n: 
    print(i)  

    if new=="" or i!=new[-1]:
        print("selected - ",i)
        new+=i
    

    
    

print(new)