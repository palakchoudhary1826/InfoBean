# 39. Search all occurrences of a character.
n=input("Enter The String : ")
ch=input("Enter The Character : ")

for i in range(len(n)):

    if n[i]==ch:
        print(i)