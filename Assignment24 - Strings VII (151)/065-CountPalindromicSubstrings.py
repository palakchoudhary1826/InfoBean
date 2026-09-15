"""
Count Palindromic Substrings

Write a Python program to input a string and count the
total number of palindromic substrings.

A substring is considered palindromic if it reads the same
forward and backward.

Note:
- Count every occurrence separately.
- Single characters are also palindromic substrings.

Input:
Enter a string: aaa

Output:
Total Palindromic Substrings: 6
"""

s = input("Enter The String : ")
count = 0
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]

        rev = temp[::-1]
        if rev == temp:
            print(temp)
            count += 1

print(count)


#second approach

# for i in range(len(s)):
#     left=i
#     right=i

#     #odd ke liye:
#     while left>=0 and right<len(s) and s[left]==s[right]:
#         count+=1
#         left-=1
#         right+=1
    
#     left=i
#     right=i+1

#     #even ke liye

#     while left>=0 and right<len(s) and s[left]==s[right]:
#         count+=1
#         left-=1
#         right+=1

# print(count)
