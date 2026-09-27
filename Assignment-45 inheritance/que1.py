"""============================================================
ASSIGNMENT 1 — EMPLOYEE MANAGEMENT SYSTEM
=========================================

SCENARIO:

A company wants to maintain information about different types of employees.

Create the following class hierarchy:

Employee
|
+-------- Developer
|
+-------- Manager

REQUIREMENTS:

1. Create a parent class Employee.

Employee should contain:

* employee_id
* employee_name
* salary

2. Create Developer and Manager classes that inherit from Employee.

3. Employee should have a method:

display_details()

4. Developer should have:

programming_language

and a method:

write_code()

5. Manager should have:

team_size

and a method:

manage_team()

6. The child-class constructors must initialize parent-class data using super().

7. Override display_details() in both child classes.

8. From the overridden method, call the parent display_details() using super().

9. salary must be encapsulated.

Implement:

@property
@salary.setter
@salary.deleter

10. Salary setter must reject salary <= 0.

11. Read ALL employee information from the user.

INPUT REQUIREMENT:

Ask the user:

Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:

1. Developer
2. Manager

If Developer:

Enter Programming Language:

If Manager:

Enter Team Size:

SAMPLE INPUT:

Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python

EXPECTED OUTPUT:

## Employee Details

Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python

Rahul is developing applications using Python.

============================================================"""

class Employee:

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Salary must be greater than 0")

        self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.salary}")


class Developer(Employee):

    def __init__(self, emp_id, emp_name, salary, language):
        super().__init__(emp_id, emp_name, salary)
        self.language = language

    def display_details(self):
        super().display_details()
        print("Role: Developer")
        print(f"Programming Language: {self.language}")

    def write_code(self):
        print(f"{self.emp_name} is developing application")
        print(f"using {self.language}")


class Manager(Employee):

    def __init__(self, emp_id, emp_name, salary, team_size):
        super().__init__(emp_id, emp_name, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print("Role: Manager")
        print(f"Team Size: {self.team_size} members")

    def manage_team(self):
        print(
            f"{self.emp_name} is managing a team "
            f"of {self.team_size} members"
        )


emp_id = int(input("Enter the employee ID: "))
emp_name = input("Enter the employee name: ")
salary = int(input("Enter the salary: "))

print("Enter the employee type:")
print("1. Developer")
print("2. Manager")

emp_type = int(input("Enter the employee type: "))


if emp_type == 1:

    language = input("Enter programming language: ")

    employee = Developer(
        emp_id,
        emp_name,
        salary,
        language
    )

elif emp_type == 2:

    team_size = int(input("Enter the team size: "))

    employee = Manager(
        emp_id,
        emp_name,
        salary,
        team_size
    )

else:
    print("Invalid employee type")
    exit()


print("\n## Employee Details")

employee.display_details()

print()

if emp_type == 1:
    employee.write_code()
else:
    employee.manage_team()