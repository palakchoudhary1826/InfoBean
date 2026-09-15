# 30. Replace a word with another word.
s = input("Enter the String: ")
word = input("Enter the Word: ")
new=input("Enter The new Word : ")


ans=""
k=0

for i in range(len(s)):

    if k>0:
        k-=1
        continue
    match=True
    for j in range(len(word)):
        if s[i+j]!=word[j]:
            match=False
            break
    
    if match:
        ans+=new
        k=len(word)-1
    else:
        ans+=s[i]

print(ans)