# Check if a string contains a substring (without using contains())


s=input("Enter The String : ")

sub=input("Enter The Substring : ")
subStringSearchLen=len(s)-len(sub)+1
idx=[]

for i in range (subStringSearchLen):
    match=True
    for j in range(len(sub)):
        if s[i+j]!=sub[j]:
            match=False
            break
    
    if match:
        idx.append(i)
    
if  idx:
    print("True")
    print(idx)
else:
    print("False")
