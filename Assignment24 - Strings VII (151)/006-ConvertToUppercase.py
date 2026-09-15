#convert to uppercase


s=input("Enter The String  : ")

# by method 

print(s.upper())

#by mannual 
result=""
for i in range(len(s)):
    if "a"<=s[i]<="z":
        result+=chr(ord(s[i])-32)
    else:
        result+=s[i]

print(result)