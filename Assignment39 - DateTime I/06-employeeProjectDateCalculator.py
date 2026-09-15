"""
Docstring for 06-employeeProjectDateCalculator

Assignment 6 — Employee Working Date & Deadline Calculator

You are developing a small HR/Project Management utility.

Create a menu-driven Python program using the datetime module to calculate
important dates related to an employee or project.

========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit

Enter your choice:


CASE 1 — Calculate Probation End Date

Read:
- Employee joining date
- Probation period in days

Calculate the probation end date using timedelta(days=...).

Input:
Enter your choice: 1
Enter employee joining date (DD-MM-YYYY): 15-07-2026
Enter probation period in days: 90

Output:
Joining Date       : 15-07-2026
Probation Period   : 90 days
Probation End Date : 13-10-2026


CASE 2 — Calculate Project Deadline

Read:
- Project start date
- Project duration in days

Calculate the project deadline using timedelta(days=...).

Input:
Enter your choice: 2
Enter project start date (DD-MM-YYYY): 10-09-2026
Enter project duration in days: 120

Output:
Project Start Date : 10-09-2026
Project Duration   : 120 days
Project Deadline   : 08-01-2027

The program must correctly handle:
- Month changes
- Year changes
- Leap years

Do not manually calculate these date changes.


CASE 3 — Calculate Notice Period End Date

Read:
- Employee resignation date
- Notice period in days

Calculate the last working date using timedelta(days=...).

Input:
Enter your choice: 3
Enter resignation date (DD-MM-YYYY): 20-09-2026
Enter notice period in days: 60

Output:
Resignation Date : 20-09-2026
Notice Period    : 60 days
Last Working Date: 19-11-2026

Additional Test:
Resignation Date : 15-12-2026
Notice Period    : 60 days

The program must correctly move into the next year.


CASE 4 — Calculate Days Remaining for Deadline

Read:
- Current date
- Project deadline

Calculate the difference between the current date and deadline.

If the deadline is in the future:

Input:
Enter your choice: 4
Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 25-09-2026

Output:
Current Date     : 10-09-2026
Project Deadline : 25-09-2026
Days Remaining   : 15 days

If the deadline has already passed:

Input:
Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 01-09-2026

Output:
Current Date     : 10-09-2026
Project Deadline : 01-09-2026
Deadline Status  : Deadline has already passed
Days Overdue     : 9 days


CASE 5 — Check Employee Work Anniversary

Read:
- Employee joining date
- Current date

Check whether the employee's joining day and month match the current
day and month.

Also calculate the number of completed working years.

If the anniversary is today:

Input:
Enter your choice: 5
Enter employee joining date (DD-MM-YYYY): 10-09-2020
Enter current date (DD-MM-YYYY): 10-09-2026

Output:
Joining Date : 10-09-2020
Current Date : 10-09-2026

Work Anniversary: YES
Completed Years  : 6 years

If the anniversary is not today:

Input:
Enter employee joining date (DD-MM-YYYY): 15-05-2022
Enter current date (DD-MM-YYYY): 10-09-2026

Output:
Joining Date : 15-05-2022
Current Date : 10-09-2026

Work Anniversary: NO
Completed Years  : 4 years


CASE 6 — Exit

Input:
Enter your choice: 6

Output:
Thank you for using Employee & Project Date Calculator!


Requirements:
1. Use the datetime module.
2. Use date/datetime objects for date calculations.
3. Use timedelta for date arithmetic.
4. Use a menu-driven approach.
5. Correctly handle month and year changes.
6. Correctly handle leap years.
7. Use conditional statements to determine deadline status.
8. Calculate completed years for work anniversaries.

"""

from datetime import date, time, datetime, timedelta


def display():
    print()
    print("""
            EMPLOYEE & PROJECT DATE CALCULATOR 

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit

""")
    print()


while True:
    display()
    choice = int(input("Enter Choice : "))
    print()

    match choice:
        case 1:
            d1, m1, y1 = map(
                int, input("Employee Joining Date(DD-MM-YYYY) :").split("-")
            )
            start = date(y1, m1, d1)
            add = int(input("Probatin Period In Days :"))

            future = start + timedelta(days=add)

            print(f"""
Joining date       :{datetime.strftime(start,"%d-%m-%Y")}
Probation Period   :{add}
Probation End Date :{datetime.strftime(future,"%d-%m-%Y")}
""")
        case 2:
            d1, m1, y1 = map(int, input("Project Start Date(DD-MM-YYYY) :").split("-"))
            start = date(y1, m1, d1)
            add = int(input("Project Duration In days :"))

            future = start + timedelta(days=add)

            print(f"""
Project Start Date :{datetime.strftime(start,"%d-%m-%Y")}
Project Duration   :{add}
Project Deadline   :{datetime.strftime(future,"%d-%m-%Y")}
""")
        case 3:
            d1, m1, y1 = map(
                int, input("Employee resignation date(DD-MM-YYYY) :").split("-")
            )
            start = date(y1, m1, d1)
            add = int(input("Notice period in days :"))

            future = start + timedelta(days=add)

            print(f"""
Employee resignation date :{datetime.strftime(start,"%d-%m-%Y")}
Noticce Period            :{add}
Last Working Date         :{datetime.strftime(future,"%d-%m-%Y")}
""")
        case 4:
            d1, m1, y1 = map(
                int, input("Project dealine Date(DD-MM-YYYY) :").split("-")
            )
            deadline = date(y1, m1, d1)
            today = date.today()

            diff = deadline - today

            print(f"""
Current Date       :{datetime.strftime(today,"%d-%m-%Y")}
Project Deadline   :{datetime.strftime(deadline,"%d-%m-%Y")}
""")

            if diff.days < 0:
                print(f"Deadline Status   :Deadline Has Already Passed ")
                print(f"Days Overdue      :{abs(diff.days)}")
            else:
                print(f"Days Remaining     :{abs(diff.days)}")

        case 5:
            joining_date = datetime.strptime(
                input("Enter employee joining date (DD-MM-YYYY): "), "%d-%m-%Y"
            )

            current_date = datetime.strptime(
                input("Enter current date (DD-MM-YYYY): "), "%d-%m-%Y"
            )

            years = current_date.year - joining_date.year

            if (current_date.month, current_date.day) < (
                joining_date.month,
                joining_date.day,
            ):
                years -= 1

            anniversary = (
                joining_date.day == current_date.day
                and joining_date.month == current_date.month
            )

            print(f"""
Joining Date :{datetime.strftime(joining_date, "%d-%m-%Y")}
Current Date :{datetime.strftime(current_date, "%d-%m-%Y")}

Work Anniversary: {"YES" if anniversary else "NO"}
Completed Years  :{years} years
""")

        case 6:
            print("Thanks For Using ")
            print("Exist ....")

        case 7:
            print("Invalid Choice")
