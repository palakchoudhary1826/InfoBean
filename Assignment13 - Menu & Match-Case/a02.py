'''
Docstring for a02
Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!
'''
print("=" * 50)
print("         EMPLOYEE SALARY PROCESSOR")
print("=" * 50)

haveSalary = False
isAllow = False

salary = 0
allow = 0 #dra ha
tax = 0
hra = 0
da = 0
netSal = 0

while True:

    print("\nMENU")
    print("-" * 50)
    print("1. Enter Basic Salary")
    print("2. Calculate HRA (20%) and DA (10%)")
    print("3. Calculate Net Salary")
    print("4. Tax Deduction")
    print("5. Display Salary Slip")
    print("6. Exit")
    print("-" * 50)

    choice = int(input("Enter your choice: "))
    print()

    match choice:

        case 1:
            n = int(input("Enter Basic Salary: "))
            if n > 0:
                salary = n
                haveSalary = True
                print("\n Basic salary recorded successfully.")
                print(f" Basic Salary : ₹{salary}")
            

        case 2:
            if haveSalary:
                hra = salary * 20 // 100
                da = salary * 10 // 100
                allow = hra + da
                isAllow = True

                print("\n Allowances Calculated")
                print("-" * 30)
                print(f"HRA (20%)  : ₹{hra}")
                print(f"DA  (10%)  : ₹{da}")
                print(f"Total      : ₹{allow}")
            else:
                print(" Please enter Basic Salary first.")

        case 3:
            if isAllow:
                netSal = salary + allow

                print("\n Net Salary")
                print("-" * 30)
                print(f"Net Salary (Before Tax) : ₹{netSal}")
            else:
                print(" Please calculate HRA and DA first.")

        case 4:
            if netSal > 0:
                if netSal > 50000:
                    tax = netSal * 10 // 100
                    rate = 10
                else:
                    tax = netSal * 5 // 100
                    rate = 5

                print("\n Tax Details")
                print("-" * 30)
                print(f"Tax Rate : {rate}%")
                print(f"Tax      : ₹{tax}")
            else:
                print(" Please calculate Net Salary first.")

        case 5:
            if tax > 0:
                finalSalary = netSal - tax

                print("\n" + "=" * 45)
                print("              SALARY SLIP")
                print("=" * 45)
                print(f"Basic Salary      : ₹{salary}")
                print(f"HRA (20%)         : ₹{hra}")
                print(f"DA (10%)          : ₹{da}")
                print("-" * 45)
                print(f"Net Salary        : ₹{netSal}")
                print(f"Tax Deduction     : ₹{tax}")
                print("-" * 45)
                print(f"Final Salary      : ₹{finalSalary}")
                print("=" * 45)

            else:
                print(" Please calculate Tax first.")

        case 6:
            print("\nThank you for using Employee Salary Processor.")
            print("Program Closed Successfully.")
            break

        case _:
            print(" Invalid Choice! Please try again.")

    print("\n" + "*" * 50)