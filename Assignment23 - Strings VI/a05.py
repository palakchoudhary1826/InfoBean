'''
Docstring for Assignment23 - String VI.a04
Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all u characters from a hashtag.

Write a Python program to find the smallest substring that contains all the u characters present in the given string.

If multiple substrings have the same minimum length, print the first one found.

Input:
aabcbcdbca

Output:
dbca

Explanation:
The substring "dbca" contains all the u characters (a, b, c, d) and is the smallest such substring.
'''

n=input("Enter : ")
u=""

for i in n:
    if i not in u:
        u+=i
    
print(u)

ans = ""


for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):

        sub = n[i:j]

       
        flag = True

        for ch in u:
            if ch not in sub:
                flag = False
                break

       
        if flag:
            if ans == "" or len(sub) < len(ans):
                ans = sub

print("Smallest Substring :", ans)