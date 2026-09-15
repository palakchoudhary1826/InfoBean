# 34. Find the shortest word in a string.




n=input("Enter The Sentence : ")

result=len(n)
new=''
for word in n.split():
    
    if result>len(word):
        result=len(word)
        new=word
    
print(result)
print(new)


