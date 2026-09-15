# 19. Find the highest frequency character in a string.

s=input("Enter The String : ")
# ch=input("Enter The Character : ")
freq=0
char=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    
    if count>freq:
        freq=count
        char=i

print(freq,char)