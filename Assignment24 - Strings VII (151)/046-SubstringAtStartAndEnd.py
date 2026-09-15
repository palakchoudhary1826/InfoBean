s=input("Enter The Sentence : ")
c=input("Enter The Check String : ")

word=s.split()
print(word)

if c in word[0] and c in word[-1]:
    print("Start and end sub string matched")
else:
    print("Not Match ")
