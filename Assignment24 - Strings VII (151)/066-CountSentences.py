"""
Count Number of Sentences in a Paragraph

Write a Python program to input a paragraph and count the
total number of sentences.

A sentence ends with:
. (full stop)
? (question mark)
! (exclamation mark)

Do not count multiple consecutive punctuation marks as
multiple sentences.

Input:
Enter a paragraph: Hello! How are you? I am fine.

Output:
Number of Sentences: 3
"""

s = input("Enter The paragraph : ")

count = 0

for i in range(len(s)):

    if i == 0 or s[i - 1] not in ".!?":
        if s[i] in ".!?":
            count += 1

print(count)
