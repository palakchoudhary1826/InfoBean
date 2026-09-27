"""Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

Employee ID

Employee name

Basic salary

HRA percentage

DA percentage

Create the following methods:

calculate_hra() – Calculate HRA.

calculate_da() – Calculate DA.

calculate_gross_salary() – Calculate gross salary.

display_salary() – Display employee salary details.

Formula:

HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA
"""
class employe:
    def accept(self,employe_id,employe_name,salary,hra,da):
        self.employe_id=employe_id
        self.employe_name=employe_name
        self.salary=salary
        self.hra=hra
        self.da=da
    def calculate_hra(self):
        self.hra=self.salary*self.hra/100

    def calculate_da(self):
        self.da=self.salary*self.da/100
    def calculate_gs(self):
                self.gs=self.salary+self.hra+self.da
    def display(self):
        print("Employee ID =", self.employe_id)
        print("Employee Name =", self.employe_name)
        print("Basic Salary =", self.salary)
        print("HRA =", self.hra)
        print("DA =", self.da)
        print("Gross Salary =", self.gs)
 
e1=employe()
e1.accept(101,"ajay",20000,20,10)
e1.calculate_hra()
e1.calculate_da()
e1.calculate_gs()
e1.display()  
