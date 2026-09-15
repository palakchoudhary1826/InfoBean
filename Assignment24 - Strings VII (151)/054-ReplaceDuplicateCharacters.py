"""
Question:
Replace all duplicate characters with '$'.

Given a string, identify all characters that occur
more than once. Replace every occurrence of those
duplicate characters with '$'.

Characters that occur only once should remain unchanged.

Test Cases:

1. Input:
   hello
   Output:
   he$$o

2. Input:
   banana
   Output:
   b$$$$$

3. Input:
   programming
   Output:
   $rog$am$$n$

4. Input:
   abcde
   Output:
   abcde

5. Input:
   aabbcc
   Output:
   $$$$$$

6. Input:
   apple
   Output:
   a$$le

7. Input:
   success
   Output:
   $u$$$$

8. Input:
   112233
   Output:
   $$$$$$

9. Input:
   python
   Output:
   python

10. Input:
    mississippi
    Output:
    m$$$$$$$$$$
"""

s = input("Enter The String : ")
new = ""

#& --> approach for hello  -> he$l0
# for i in range(len(s)):
#     count = 0
#     for j in range(i+1,len(s)):
#         if s[i] == s[j]:
#             count += 1
#     if count > 0:
#         new += "&"
#     else:
#         new += s[i]

# print(new)



for i in range(len(s)):
    found=False
    
    for j in range(i):
        if s[i] == s[j]:
            found=True
            break
    if found:
        new += "&"
    else:
        new += s[i]

if not new: 
    print("empt")
else:
    print(new)
