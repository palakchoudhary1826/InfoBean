# 35. Find the first word that is a palindrome.


n=input("Enter the Sentence : ")


for word in n.split():
    rev=word[::-1]
    if word == rev:
        print(word)
        break
else:
    print("no palindrome")