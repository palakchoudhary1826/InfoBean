"""
QUESTION 2: STUDENT RESULT PROCESSING

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

2. Display all student details.

3. Find and display the topper of the class.

4. Count and display the number of students scoring above 80 marks.

5. Calculate and display the average marks.

6. Accept a course name from the user and display all students enrolled in that course.

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
"""

from collections import namedtuple


emp=namedtuple("emp",["roll_no","name","course","marks"])


n=int(input("Enter The Number of Student : "))
list=[]


for i in range(n):
    print(f"Enter Student {i+1} Details")
    id=input("Enter Roll No.          : ")
    name=input("Enter Name              : ")
    course=input("Enter Course            : ")
    mark=input("Enter Marks             : ")
    list.append(emp(id,name,course,int(mark)))
    print(f"{i+1}th Student Details Stored ...")
    print()


print(list)


print("All Student Details : ")


count=1


for i in list:
    print(f"{count}th Student Details")
    print(f"Roll No.   : {i.roll_no}")
    print(f"Name       : {i.name}")
    print(f"Course     : {i.course}")
    print(f"Marks      : {i.marks}")
    count+=1
    print()


max=list[0]
count=0
above80=[]
sum=0

for i in list:
    if i.marks > max.marks:
        max=i

    if i.marks>80:
        count+=1
        above80.append(i)

    sum+=i.marks


print("Topper Of Class")
print(f"Roll No.   : {max.roll_no}")
print(f"Name       : {max.name}")
print(f"Course     : {max.course}")
print(f"Marks      : {max.marks}")


print()
print(f"Above 80 Marks Students Are : {count}")

for i in above80:
    print(i)


print()
print(f"Average Marks : {sum/n}")


course=input("Enter Course : ")

print(f"Students in {course} Course : ")

for i in list:
    if i.course==course:
        print(f"Roll No.   : {i.roll_no}")
        print(f"Name       : {i.name}")
        print(f"Course     : {i.course}")
        print(f"Marks      : {i.marks}")
        print()