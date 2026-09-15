# 20. Find the lowest frequency character in a string.


s=input("Enter The String : ")
# ch=input("Enter The Character : ")
freq=len(s)
char=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    
    if count<freq:
        freq=count
        char=i

print(freq,char)