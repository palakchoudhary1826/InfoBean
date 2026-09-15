'''
2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction
'''

mark=int(input("Enter The Marks : "))

if mark>=40:
    print("Pass")
if mark>=75:
    print("Distinction")