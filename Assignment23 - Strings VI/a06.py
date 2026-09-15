'''
Docstring for Assignment23 - String VI.a05
AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

Write a Python program to check whether any character repeats three times consecutively in the given sentence.

If found, print:

Spam Pattern Found

Otherwise, print:

Clean Message

Input:
heyyy broooo welcome

Output:
Spam Pattern Found
'''

n=input("Enter  : ")
found=False

for word in n.split():
    for i in word :
        
        count=0
        for j in word:
            if j==i:
                count+=1
        
        if count>=3:
            found=True
            break

if found:
    print("spam pattern found")
else:
    print("not found")
        