# Find the longest word in a string.


n=input("Enter The Sentence : ")

result=0
new=''
for word in n.split():
    
    if result<len(word):
        result=len(word)
        new=word
    
print(result)
print(new)


