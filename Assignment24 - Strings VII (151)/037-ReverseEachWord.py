# 37. Reverse each word in a string.

n=input("Enter The sentence : ")

result=""
for word in n.split():
    result=result+" "+word[::-1]

print(result)