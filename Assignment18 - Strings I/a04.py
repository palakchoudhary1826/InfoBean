'''
Docstring for Assignment18.a04
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''

n=input("Enter Student Name : ").lower()

count=0

i=0
while i<len(n):
    if n[i] in "aeiou":
        pass
    else:
        count+=1
    i+=1

print(f"Total Consonants : {count}")