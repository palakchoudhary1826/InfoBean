'''
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2

'''

s1=int(input("Enter Subject 1 Marks :- "))
s2=int(input("Enter Subject 2 Marks :- "))
s3=int(input("Enter Subject 3 Marks :- "))
s4=int(input("Enter Subject 4 Marks :- "))
s5=int(input("Enter Subject 5 Marks :- "))

totalMarks=s1+s2+s3+s4+s5
avg=totalMarks/5
percent=(totalMarks/500)*100

print(f"Total : {totalMarks}")
print(f"Average : {avg}")
print(f"percent : {percent}")