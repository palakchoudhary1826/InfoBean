'''
Count Total Alphabets, Digits, and Special Characters

Write a Python program to input a string and count:
1. Total alphabets (A-Z, a-z)
2. Total digits (0-9)
3. Total special characters

Spaces should not be counted as special characters.

Input:
Enter a string: Hello@123 World#45

Output:
Alphabets: 10
Digits: 5
Special Characters: 2
'''

s=input("Enter The String : ")

aCount=0
dCount=0
sCount=0


for i in s:
    if "a"<=i<="z" or 'A'<=i<='Z':
        aCount+=1
    elif "0"<=i<="9":
        dCount+=1
    
    elif i!=" ":
        sCount+=1

print(f"Alphabets : {aCount}")
print(f"Digits : {dCount}")
print(f"Special Characters : {sCount}")