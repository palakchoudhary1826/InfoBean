"""Question 4: Student Result Processing System
Scenario
A college wants to automate result generation by calculating total marks, percentage, and grade.
Requirements
Create a class named Student with:
roll_number
student_name
marks1
marks2
marks3
Initialize the values using a constructor.
Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B"""

class student():
    def __init__(self):
        self.name="Priya sharma"
        self.roll_no=101
        self.marks1=85
        self.marks2=90
        self.marks3=88
        self.total=self.marks1+self.marks2+self.marks3
        self.percentage=self.total/3
        if self.percentage > 90:
            self.grade="A"
        elif self.percentage > 75 and self.percentage < 89:
            self.grade="B"
        elif self.percentage > 60 and self.percentage <74:
           self.grade="C"
        else:
            self.grade="D"
    def display(self):
        print("Student Nmae:",self.name)
        print("Roll NO:",self.roll_no)
        print("Total Marks:",self.total)
        print("Percentage:",self.percentage)
        print("Grade:",self.grade)

s=student()
s.display()
                
