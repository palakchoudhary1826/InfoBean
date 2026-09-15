'''
Docstring for Assignment23 - String VI.a07
Intelligent Search Query Compressor

A search engine company wants to compress user queries.

Write a Python program to compress a search query using the following rules:

Rules:
• Count the frequency of each character
• Display characters in alphabetical order
• Ignore spaces
• Treat uppercase and lowercase letters as the same (case-insensitive)

Input:
Google Search

Output:
a1c1e2g2h1l1o2r1s1t1
'''

n=input("Enter : ").lower()
new=""

for word in n.split():
    for i in word:
        new+=i
print(sorted(new).join(""))


        
        