"""
Count Frequency of Each Character

Write a Python program to input a string and count the
frequency of each character.

Spaces should also be counted if they are present.

Input:
Enter a string: hello

Output:
h : 1
e : 1
l : 2
o : 1
"""

s = input("Enter The String : ")
# seen=""
# for i in s:
#     count=0
#     if i not in seen:
#         seen+=i
#         for j in s:
#             if i==j:
#                 count+=1
#         print(f"{i} : {count}")

# approach-2:

freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in freq:
    print(f"{i}:{freq[i]}")
