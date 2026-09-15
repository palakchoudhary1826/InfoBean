'''
Count How Many Times 'life' Appears in a String

Write a Python program to input a string and count how many
times the substring "life" appears in it.

The search should be case-insensitive.

Overlapping occurrences should also be counted.

Input:
Enter a string: lifelife

Output:
Occurrences of 'life': 2
'''

s=input("Enter The String : ").lower()



sub="life"
count = 0
# for i in range(len(s)):
#     temp = ""
#     for j in range(i, len(s)):
#         temp += s[j]

        
#         if sub == temp:
#             print(temp)
#             count += 1

# print(count)

for i in range(len(s)-len(sub)+1):
    if s[i:i+len(sub)]==sub:
        count+=1

print(count)



