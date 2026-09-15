'''
Print List Items Containing All Characters of a Given Word

Write a Python program to input a list of strings and a
given word. Print all list items that contain every character
of the given word.

Character order does not matter.

Input:
List: ["apple", "banana", "grape", "pineapple"]
Word: "ape"

Output:
apple
grape
pineapple
'''

l = list(map(str, input("Enter The Items : ").split()))
word=input("Enter The word : ")

for i in l:
    found=True
    for j in word:
        if j not in i:
            found=False
            break
    if found:
        print(i)
        
