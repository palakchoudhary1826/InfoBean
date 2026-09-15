# 23. Print all characters that occur exactly twice.


n=input("ENter : ")

l=""
done=""
for i in n:
    temp=0
    for j in n:
        if i==j:
            temp+=1
    
    if temp==2:
        if i not in done:
            l+=i
            done+=i

if l=="":
    print("no repeat ")
else:
    print(l)