#convert to lowercase


s=input("Enter The String  : ")

# by method 

print(s.lower())

#by mannual 
result=""
for i in range(len(s)):
    if "A"<=s[i]<="Z":
        result+=chr(ord(s[i])+32)
    else:
        result+=s[i]

print(result)