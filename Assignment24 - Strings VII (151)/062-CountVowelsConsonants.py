'''
Count Vowels and Consonants

Write a Python program to input a string and count:
1. Total vowels
2. Total consonants

Only alphabets should be considered.
Spaces, digits, and special characters should be ignored.

Input:
Enter a string: Hello World 123!

Output:
Vowels: 3
Consonants: 7
'''
s=input("Enter The String  : ")

vCount=0
cCount=0

for i in s:

    if ("A"<=i<="Z") or ("a"<=i<="z"):
        if i in "aeiouAEIOU":
            vCount+=1
        else:
            cCount+=1

print(f"Vowels :  {vCount}")
print(f"Consonants :  {cCount}")