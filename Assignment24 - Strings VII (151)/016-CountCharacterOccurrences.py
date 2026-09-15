# 16. Count total occurrences of a character in a string.

s = input("Enter String : ")
ch = input("Enter The Character : ")

count = 0

for c in s:
    if c == ch:
        count += 1

print(f"Total occurrences of '{ch}' : {count}")