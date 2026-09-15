# 40 . Search all occurrences of a word


s = input("Enter the String: ")
word = input("Enter the Word: ")


subStringSearch=len(s)-len(word)+1

for i in range(subStringSearch):
    match=True
    for j in range(len(word)):
        if s[i+j]!=word[j]:
            match=False
            break
    
    if match:
        left=(i==0 or s[i-1]==" ")
        right = (i + len(word) == len(s) or s[i + len(word)] == " ")
        

        if left and right :
            print(i)



    