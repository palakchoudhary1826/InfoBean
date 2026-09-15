# Check if two strings are equal without using equals()

s1=input("Enter The First String  : ")
s2=input("Enter The Second String : ")



ans=True

if len(s1)!=len(s2):
    ans=False

else:

    for i in  range (len(s1)):
        if s1[i]!=s2[i]:
            ans=False
            break

if ans:
    print("match")
else:
    print("not match")

