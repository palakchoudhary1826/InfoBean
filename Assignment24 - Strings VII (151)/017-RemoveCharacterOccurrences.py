# 17. Remove the first, last, or all occurrences of a given character

s=input("Enter The String : ")
ch=input("Enter The character : ")
new=""

for i in s:
    if i!=ch:
        new+=i

print(new)
