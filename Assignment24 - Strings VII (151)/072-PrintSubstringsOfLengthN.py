'''
Print All Substrings of Length N

Write a Python program to input a string and an integer n.
Print all substrings having exactly n characters.

Input:
Enter a string: abcde
Enter length: 3

Output:
abc
bcd
cde
'''


s = input("Enter The String : ")
l=int(input("Enter The Length : "))
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]
        if len(temp)==l:
            print(temp)