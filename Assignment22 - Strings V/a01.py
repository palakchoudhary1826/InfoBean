'''
Docstring for Assignment22 - String V.a01
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc
'''

n=input("Enter : ")

long=""

for i in range(len(n)):
    temp=""
    for j in range(i,len(n)):
        if n[j] in temp:
            break
        temp+=n[j]
    if len(temp)>len(long):
        long=temp


print(f"Longest Substring :{long} ")