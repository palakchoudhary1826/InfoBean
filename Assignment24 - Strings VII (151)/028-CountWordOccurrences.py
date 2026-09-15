# Count occurrences of a word in a string

s = input("Enter the String: ")
word = input("Enter the Word: ")

idx = -1;
subStringSearch=len(s)-len(word)+1
count=0

for i in range(subStringSearch):
    match=True
    for j in range(len(word)):
        if s[i+j]!=word[j]:
            match=False
            break
    
    if match:
        count+=1
        # break

print(f"count of {word} : {count}")