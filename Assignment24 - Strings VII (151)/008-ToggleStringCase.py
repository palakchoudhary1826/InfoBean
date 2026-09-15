# 8. Toggle the case of each character in a string.




s=input("Enter The String  : ")

# by method 

print(s.swapcase())

#by mannual 
result=""
for i in range(len(s)):
    if "A"<=s[i]<="Z":
        result+=chr(ord(s[i])+32)
    elif "a"<=s[i]<="z" :
        result+=chr(ord(s[i])-32)
    else:
        result+=s[i]

print(result)