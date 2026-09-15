"""
Docstring for 04-futureDateCalculator


Assignment 4 — Menu-Driven Future Date Calculator

Develop a menu-driven Python program using the datetime module to calculate a future date or date-time.

The program should allow the user to add days, weeks, hours, or minutes to a given date/time.

Use timedelta for all date and time calculations.

Menu
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Case 1 — Add Days

Read:
- Starting date
- Number of days

Input:
Enter your choice: 1
Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to add: 100

Output:
Starting Date : 10-09-2026
Days Added    : 100
Future Date   : 19-12-2026


Case 2 — Add Weeks

Read:
- Starting date
- Number of weeks

Input:
Enter your choice: 2
Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to add: 4

Output:
Starting Date : 10-09-2026
Weeks Added   : 4
Future Date   : 08-10-2026


Case 3 — Add Hours

Read:
- Starting date and time
- Number of hours

Input:
Enter your choice: 3
Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to add: 15

Output:
Starting Date & Time : 10-09-2026 10:30
Hours Added          : 15
Future Date & Time   : 11-09-2026 01:30

Note:
Adding hours may change the date.


Case 4 — Add Minutes

Read:
- Starting date and time
- Number of minutes

Input:
Enter your choice: 4
Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 23:30
Enter number of minutes to add: 90

Output:
Starting Date & Time : 10-09-2026 23:30
Minutes Added        : 90
Future Date & Time   : 11-09-2026 01:00

Note:
Adding minutes may change the date.


Case 5 — Exit

Input:
Enter your choice: 5

Output:
Thank you for using Future Date Calculator!


Requirements:
1. Use the datetime module.
2. Use timedelta for all date and time calculations.
3. Use a menu-driven approach.
4. Correctly handle changes in month and year.
5. Correctly handle date changes when adding hours or minutes.


"""

from datetime import datetime, date, timedelta, time


def display():
    print()
    print(""" 
          FUTURE DATE CALCULATOR 

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit
""")
    print()


while True:
    display()

    choice = int(input("Enter Choice : "))
    print()

    match choice:
        case 1:
            d1, m1, y1 = map(
                int, input("Enter Starting date (DD-MM-YYYY) :").split("-")
            )
            start = date(y1, m1, d1)
            add = int(input("Number Of days AddUp :"))

            future = start + timedelta(days=add)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y")}
Days Added    :{add}
Future Date   :{datetime.strftime(future,"%d-%m-%Y")}
""")

        case 2:
            d1, m1, y1 = map(
                int, input("Enter Starting date (DD-MM-YYYY) :").split("-")
            )
            start = date(y1, m1, d1)
            week = int(input("Number Of Weeks AddUp :"))

            future = start + timedelta(weeks=week)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y")}
Weeks Added    :{week}
Future Date   :{datetime.strftime(future,"%d-%m-%Y")}
""")

        case 3:
            d1, m1, y1 = map(
                int, input("Enter Starting date (DD-MM-YYYY) :").split("-")
            )

            h1, min1 = map(int, input("Enter Time (HH:MM) : ").split(":"))
            startDate = date(y1, m1, d1)
            StartTime = time(h1, min1)
            start = datetime.combine(startDate, StartTime)
            add = int(input("Number Of hours AddUp :"))

            future = start + timedelta(hours=add)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y")}
Weeks Added    :{add}
Future Date   :{datetime.strftime(future,"%d-%m-%Y %H:%M")}
""")
        case 4:
            d1, m1, y1 = map(
                int, input("Enter Starting date (DD-MM-YYYY) :").split("-")
            )

            h1, min1 = map(int, input("Enter Time (HH:MM) : ").split(":"))
            startDate = date(y1, m1, d1)
            StartTime = time(h1, min1)
            start = datetime.combine(startDate, StartTime)
            add = int(input("Number Of Min AddUp :"))

            future = start + timedelta(minutes=add)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y %H:%M")}
Weeks Added    :{add}
Future Date   :{datetime.strftime(future,"%d-%m-%Y %H:%M")}
""")
        case 5:
            print("Thanks For Using")
            print("Existing...")
        case _:
            print("Invalid Choice")
