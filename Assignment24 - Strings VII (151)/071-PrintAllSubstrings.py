'''
Print All Substrings of a String

Write a Python program to input a string and print all
possible substrings.

Input:
Enter a string: abc

Output:
a
ab
abc
b
bc
c
'''

s = input("Enter The String : ")

for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]
        print(temp)

        

