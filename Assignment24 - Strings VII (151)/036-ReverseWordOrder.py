# 36. Reverse the order of words in a string

n=input("Enter The sentence : ")

result=""
for word in n.split():
    result=word+" "+result

print(result)