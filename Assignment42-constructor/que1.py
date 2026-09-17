"""Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
"""
class employe():
    def __init__(self,employe_id,employe_name,basic_salary):
        self.employe_id=employe_id
        self.employe_name=employe_name
        self.basic_salary=basic_salary
        self.hra=self.basic_salary*20/100
        self.da=self.basic_salary*15/100
        self.gross=self.basic_salary+self.hra+self.da
    def display(self):
        print("employe id:",self.employe_id)
        print("employe Name:",self.employe_name)
        print("Basic salary:",self.basic_salary)
        print("HRA:",self.hra)
        print("DA:",self.da)
        print("Gross Salary:",self.gross)
e=employe(101,"rahul sharma",50000)
e.display()
