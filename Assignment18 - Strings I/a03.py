'''
Docstring for Assignment18.a03
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
'''
n=input("Enter  : ")
c=input("Enter : ")
count=0

i=0
while i<len(n):
    if n[i]==c:
        count+=1
    i+=1

print(f"Character : '{c}' occurs : {count} times")