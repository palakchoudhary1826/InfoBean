# 38. Reverse words without using split().


s = input("Enter the String: ")

words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words = words + [word]
            word = ""

if word != "":
    words = words + [word]

# print(words)

result=""
for i in words:

    result=i+" "+result

print(result)
    
