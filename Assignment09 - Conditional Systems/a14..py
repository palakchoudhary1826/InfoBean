'''
Docstring for Assignment09.a14.
University Result Classification System

A university assigns final class based on marks, backlog, and project score.

If marks are 75 or above, then check backlog. If backlog is 0, then check project score. If project score is 80 or above, assign First Class with Distinction; otherwise First Class. If backlog is not 0, assign First Class.

If marks are between 60 and 74, then check backlog. If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.

If marks are between 50 and 59, assign Pass. Otherwise Fail.

Input:
Marks = 78
Backlogs = 0
Project = 85

Output:
Result = First Class with Distinction
'''
marks = int(input("Enter Marks: "))
backlogs = int(input("Enter Number of Backlogs: "))
project_score = int(input("Enter Project Score: "))
assign=""
if marks>=75:
    if backlogs==0:
        if project_score>=80:
            assign="first class with distinction"
        else:
            assign="first class"
    else:
        assign="first class"
elif marks >=60 and marks<=74:
        if backlogs<=2:
            assign="second class"
        else:
            assign="pass class"

else:
    if marks>=50 and marks<=59 :
          assign="Pass"
    else:
         assign="fail"

print(f"Result :  {assign}")