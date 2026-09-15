'''
Docstring for Assignment18.a02
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
'''

n=input("Enter : ")
count=0
i=0
while i <len(n):
    if n[i]==" ":
        count+=1
    i+=1


print(count)