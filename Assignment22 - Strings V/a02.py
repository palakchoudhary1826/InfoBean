'''
Docstring for Assignment22 - String V.a02
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india
'''

n=input("Enter : ")

high=0
wo=""
# temp=""
for word in n.split():
    # print(word)
    count=0

    for w in n.split():
        if word==w:
            count+=1
    
    if count>high:
        high=count
        wo=word

print(wo)