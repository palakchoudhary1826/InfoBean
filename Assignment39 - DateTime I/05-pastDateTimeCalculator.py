'''
Docstring for 05-pastDateTimeCalculator
ASSIGNMENT 5 – MENU-DRIVEN PAST DATE & TIME CALCULATOR


Create a menu-driven Python program that allows the user to calculate a date/time in the past by subtracting days, weeks, hours, or minutes.

Menu
========== PAST DATE & TIME CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit

Enter your choice:
CASE 1 – Subtract Days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to subtract: 100
Output
Starting Date : 10-09-2026
Days Subtracted : 100
Past Date : 02-06-2026
CASE 2 – Subtract Weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to subtract: 6
Output
Starting Date : 10-09-2026
Weeks Subtracted : 6
Past Date : 30-07-2026
CASE 3 – Subtract Hours

Here the student must read both date and time.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to subtract: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Subtracted     : 15
Past Date & Time     : 09-09-2026 19:30
CASE 4 – Subtract Minutes
Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 01:00
Enter number of minutes to subtract: 90
Output
Starting Date & Time : 10-09-2026 01:00
Minutes Subtracted   : 90
Past Date & Time     : 09-09-2026 23:30
CASE 5 – Exit
Enter your choice: 5

Thank you for using Past Date & Time Calculator!

'''

from datetime import datetime, date, timedelta, time


def display():
    print()
    print(""" 
          FUTURE DATE CALCULATOR 

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
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
            add = int(input("Number Of days SumUp :"))

            future = start - timedelta(days=add)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y")}
Days Subtract    :{add}
Future Date   :{datetime.strftime(future,"%d-%m-%Y")}
""")

        case 2:
            d1, m1, y1 = map(
                int, input("Enter Starting date (DD-MM-YYYY) :").split("-")
            )
            start = date(y1, m1, d1)
            week = int(input("Number Of Weeks SumUp :"))

            future = start - timedelta(weeks=week)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y")}
Weeks Subtract    :{week}
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
            add = int(input("Number Of hours SumUp :"))

            future = start + timedelta(hours=add)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y")}
Weeks Subtract    :{add}
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
            add = int(input("Number Of Min SumUp :"))

            future = start - timedelta(minutes=add)

            print(f"""
Starting date :{datetime.strftime(start,"%d-%m-%Y %H:%M")}
Weeks Subtract    :{add}
Future Date   :{datetime.strftime(future,"%d-%m-%Y %H:%M")}
""")
        case 5:
            print("Thanks For Using")
            print("Existing...")
        case _:
            print("Invalid Choice")
