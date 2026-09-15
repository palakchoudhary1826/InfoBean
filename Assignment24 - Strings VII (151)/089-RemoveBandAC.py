'''
Problem:
Remove 'b' and 'ac' from a string.

Given a string s, remove every occurrence of 'b' and the substring
'ac' from the string.

"abcac" → ""
"aabbc" → "a"
"abac"  → "a"
"hello" → "hello"
'''
s=input("Enter The String : ")

a1=""
for i in s:
    if i!="b":
        a1+=i

# print(a1)

a2=''
i=0

while i<len(a1):

    if i+1<len(a1) and a1[i]=='a' and a1[i+1]=='c':
        i+=2
    else:
        a2+=a1[i]
        i+=1

if not a2:
    print("Empty")
else:
    print(a2)



#!

# a = ""

# i = 0

# while i < len(s):

#     if s[i] == 'b':
#         i += 1

#     else:
#         a += s[i]
#         i += 1

#         if len(a) >= 2 and a[-2] == 'a' and a[-1] == 'c':
#             a = a[:-2]

# if not a:
#     print("Empty")
# else:
#     print(a)




