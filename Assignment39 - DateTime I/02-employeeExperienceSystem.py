'''
Docstring for 02-employeeExperienceSystem
## Assignment 2 — Employee Joining & Experience System

Create a Python program that calculates an employee's total work experience.

### Input

Read the following details from the user:

1. Employee name
2. Joining date
3. Current date

Both dates should be entered in the format **DD-MM-YYYY**.

### Calculate

The program should calculate and display:

1. Total days worked
2. Total years worked
3. Total months worked approximately
4. Exact experience in **Years, Months, and Days**
5. Whether the employee has completed **1 year**
6. Whether the employee has completed **5 years**

### Input Example

```text
Enter employee name: Rahul
Enter joining date: 10-06-2021
Enter current date: 10-09-2026
```

### Expected Output

```text
Employee: Rahul
Joining Date: 10-06-2021

Experience: 5 Years 3 Months 0 Days
Total Days Worked: 1918
Total Years Worked: 5
Total Months Approximately: 63

1 Year Completed: Yes
5 Years Completed: Yes
```

'''

from datetime import datetime
name=input("Enter Name :")
joinDate=input("Ennter Join Date (DD-MM-YYYY): ")
joinDate=datetime.strptime(joinDate,"%d-%m-%Y").date()
today=datetime.today().date()
# print(today,joinDate)

# Total days worked
tdays = today - joinDate

print(f"Total Days Worked: {tdays.days}")


# Total years worked
tyears = today.year - joinDate.year

if (today.month, today.day) < (joinDate.month, joinDate.day):
    tyears -= 1

print(f"Total Years Worked: {tyears}")


# Total months approximately
tmonth = (today.year - joinDate.year) * 12 + (today.month - joinDate.month)

print(f"Total Months Approximately: {tmonth}")



#experience



matchJoinToday=joinDate.replace(year=joinDate.year+tyears)

remainMonth=today.month-matchJoinToday.month
remainDay=today.day-matchJoinToday.day

print(f"Experience: {tyears} Years {remainMonth} Months {remainDay} Days")


#check employee year>1year

print(f"1 Year Completed: {'Yes' if tyears >= 1 else 'No'}")

print(f"5 Years Completed: {'Yes' if tyears >= 5 else 'No'}")