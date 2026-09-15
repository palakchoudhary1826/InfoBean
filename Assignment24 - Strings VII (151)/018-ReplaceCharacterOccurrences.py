# 18. Replace the first, last, or all occurrences of a character
# S = "apple", Old='p', New='x' 
# "axxle"


s=input("Enter the string : ")
old=input("Enter The Old word : ")
new =input("Enter The New Word : ")

result=""

for i in s:
    if old==i:
        result+=new
    else:
        result+=i

print(result)