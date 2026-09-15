'''
Docstring for Assignment16.a01
Leap Year Event Scheduler – Multi-Year Analysis

Write a program that:

Takes start year and end year as input.
Checks every year in the range to determine whether it is a Leap Year using these rules:
Divisible by 4 → Leap Year candidate
Divisible by 100 → Not a Leap Year
Divisible by 400 → Leap Year

If the year is a leap year, print:

year → Event Scheduled

Otherwise, print:

year → No Event
After processing all years, print:
Total number of leap years.
Total events scheduled.

Input

2000
2005

Output

2000 → Event Scheduled
2001 → No Event
2002 → No Event
2003 → No Event
2004 → Event Scheduled
2005 → No Event

Total Leap Years = 2
Total Events Scheduled = 2
'''

s=int(input("Enter The Starting Year : "))
e=int(input("Enter The Ending Year : "))
leap=0

while s<=e:
    d=s%100
    if d==00:
        if s%400==0 & s%100==0 & s%4==0:
            print(f"{s} -> Event Scheduled")
            leap+=1
        else:
            print(f"{s} -> No Event ")
    else:
        if s%4==0:
            print(f"{s} -> Event Scheduled")
            leap+=1
        else:
            print(f"{s} -> No Event")
    s+=1

print(f"Total Number Of leap years : {leap}")
print(f"Total Events Scheduled  :{leap} ")