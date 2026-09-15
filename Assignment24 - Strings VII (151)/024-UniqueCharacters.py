# 24. Check if all characters in a string are unique (no repetition).


n=input("Enter The String : ")
new=""

for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    
    if count==1:
        new+=i

print(new)