"""
QUESTION 1: EMPLOYEE SALARY ANALYSIS

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

2. Display all employee details.

3. Find and display the employee with the highest salary.

4. Find and display the employee with the lowest salary.

5. Calculate and display the average salary of all employees.

6. Accept a department name from the user and display all employees belonging to that department.

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
"""

from collections import namedtuple


emp=namedtuple("emp",["id","name","dept","salary"])


n=int(input("Enter The Number of Employees : "))
list=[]


for i in range(n):
    print(f"Enter Employee {i+1} Details")
    id=input("Enter ID          : ")
    name=input("Enter Name        : ")
    dept=input("Enter Department  : ")
    salary=input("Enter Salary      : ")
    list.append(emp(id,name,dept,int(salary)))
    print(f"{i+1}th Employee Details Stored ...")
    print()

print(list)

print("All Employee Details : ")

count=1

for i in list:
    print(f"{count}th Employee Details")
    print(f"ID         : {i.id}")
    print(f"Name       : {i.name}")
    print(f"Department : {i.dept}")
    print(f"Salary     : {i.salary}")
    count+=1
    print()



max=list[0]

for i in list:
    if i.salary > max.salary:
        max=i

print("Highest Salary Employee : ")
print(f"ID         : {max.id}")
print(f"Name       : {max.name}")
print(f"Department : {max.dept}")
print(f"Salary     : {max.salary}")

min=list[0]

for i in list:
    if i.salary < min.salary:
        min=i

print("Lowest Salary Employee : ")
print(f"ID         : {min.id}")
print(f"Name       : {min.name}")
print(f"Department : {min.dept}")
print(f"Salary     : {min.salary}")

sum=0
for i in list:
    sum+=i.salary
avg=sum/n

print(f"Average Salary : {avg}")


deptCheck=input("Enter Department For sort  : ")
print(f"Employess in {deptCheck} Department :")
for i in list:
    if i.dept==deptCheck:
        print(i)