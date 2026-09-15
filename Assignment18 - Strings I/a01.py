
"""

1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
"""

n=input("Enter : ")
count=0
i=0
while i<len(n):
    if n[i] in  "aeiou" or n[i] in "AEIOU":
        count+=1
    i+=1

print(f"Total Vowels : {count}")