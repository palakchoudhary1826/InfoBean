# Check if two strings are rotations of each other

#* left rotation how it works  for e.g "abcd" , k=1 ===> "bcda"


# s=input("Enter The String : ")
# k=int(input("Enter The rotate by value : "))
# new=""
# k=k%len(s)




# for i in range(k,len(s)):
#     new+=s[i]

# for i in range(k):
#     new+=s[i]

# print(new)


s=input("Enter The String  : ")
rot=input("Enter The Rotated String  : ")

s1=s+s
ans=False
for i in range(len(s1)-len(rot)+1):
    match=True
    for j in range(len(rot)):
        if s1[i+j]!=rot[j]:
            match=False
            break
    if match:
        ans=True
        break

print(ans)





