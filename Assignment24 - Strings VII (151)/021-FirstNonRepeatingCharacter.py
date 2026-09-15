# 21. Find the first non-repeating character.

s=input("Enter The String : ")
# ch=input("Enter The character : ")
new=""

for i in s:
    
    count=0
    for j in s:
        if i==j:
            count+=1

    if count==1:
        new+=i
    
# print(new)
print(new[0])

