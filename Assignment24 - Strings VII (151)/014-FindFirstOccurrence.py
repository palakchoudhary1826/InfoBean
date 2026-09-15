# Find the first occurrence of a character in a string.

s=input("Enter String : ")
ch=input("Enter The Character : ")
idx=0
found=False
for i in range(len(s)):
    
    if s[i]==ch:
        idx=i
        found=True
        break
    else:
        found=False


if found:

    print(f"first occurence of character {ch} found at index  : {idx}")
else:
    print("not found")


    

