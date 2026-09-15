'''
Docstring for Assignment14(Nested Loop).a08
Online Exam Result Processing System

An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277
'''
a=int(input("Enter Number Of Classes : "))
b=int(input("Enter Students Per Class : "))
c=int(input("Enter Subjects Per Student : "))
total=0

i=1
while i<=a:
    print(f"Class: {i}") 
    j=1
    while j<=b:
        print(f"  Student: {j}")
        k=0
        while k<c:
            m=int(input(f"\tEnter The Mark {k+1}: "))
            total+=m
            k+=1
        print(f"\tStudent: {j} ==> Total: {total}")
        total=0
        j+=1
    i+=1
   
