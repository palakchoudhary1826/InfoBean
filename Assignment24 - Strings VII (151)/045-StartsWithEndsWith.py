# Check whether a string starts with or ends with another string


s=input("Enter The Sentence : ")
c=input("Enter The Check Stirng : ")

word=s.split()
print(word)

if word[0]==c and word[-1]==c:
    print("Start and end string match")
else:
    print("Not Match ")
