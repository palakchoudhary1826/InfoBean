'''
Find the Longest Palindromic Substring

Write a Python program to input a string and find the
longest substring that is a palindrome.

If multiple palindromic substrings have the same maximum
length, print the first one.

Input:
Enter a string: babad

Output:
Longest Palindromic Substring: bab
'''


s = input("Enter The String : ")
l = 0
long=""
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]

        rev = temp[::-1]
        if rev == temp:  # noqa: SIM102
            if len(temp)>l:
                l=len(temp)
                long=temp
            

print(l,long)
