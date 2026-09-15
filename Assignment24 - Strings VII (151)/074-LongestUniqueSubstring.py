'''
Find the Longest Substring Without Repeating Characters

Write a Python program to input a string and find the
longest substring in which no character is repeated.

If multiple substrings have the same maximum length,
print the first one.

Input:
Enter a string: abcabcbb

Output:
Longest Substring: abc
Length: 3
'''
s = input("Enter The String : ")
long=""
l=0

for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        if s[j] in temp:
            break
        
        temp+=s[j]
        if len(temp)>l:
            l=len(temp)
            long=temp

print(long)
print(l)
