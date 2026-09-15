# 22. Find the last repeating character.

n=input("ENter : ")

l=""

for i in n:
    temp=0
    for j in n:
        if i==j:
            temp+=1
    
    if temp>1:
        l=i

if l=="":
    print("no repeat ")
else:
    print(l)