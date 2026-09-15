"""
Count Frequency of Each Vowel

Write a Python program to input a string and count the
frequency of each vowel present in the string.

Consider:
a, e, i, o, u

The program should be case-insensitive.

Input:
Enter a string: Hello World

Output:
a : 0
e : 1
i : 0
o : 2
u : 0
"""

s = input("Enter The String : ").lower()
freq = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}


for i in s:
    if i in "aieou":
        if i in freq:
            freq[i] += 1
        elif i not in freq:
            freq[i] = 0

        else:
            freq[i] = 1

for i in freq: 
    print(f"{i}:{freq[i]}")
