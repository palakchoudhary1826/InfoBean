'''
Leap Year Event Scheduler – Multi-Year Analysis System

A city event management system schedules special festivals only in leap years.

To plan future events, the system analyzes multiple years instead of just one.

Write a program to:

- Read start year and end year from user
- For every year in the range, check whether it is a Leap Year or Not 
- Apply rules:
    - Divisible by 4 → Leap Year candidate  
    - Divisible by 100 → Not Leap Year  
    - Divisible by 400 → Leap Year  

- If leap year → print year with "Event Scheduled"
- Else → print year with "No Event"

- After checking all years:
    - Count total leap years
    - Print total events scheduled

Input:
2000
2005

Output:
2000 → Event Scheduled
2001 → No Event
2002 → No Event
2003 → No Event
2004 → Event Scheduled
2005 → No Event

Total Leap Years = 2
Total Events Scheduled = 2
'''

a=int(input("Enter Starting Number : "))
b=int(input("Enter Ending Number : "))
leap=0
notLeap=0
while a<=b:
    if a % 400 == 0:
        print(f"{a} :Event Scheduled")
        leap+=1
    elif a % 100 == 0:
        print(f"{a} :No Event")
        notLeap+=1
    elif a % 4 == 0:
        print(f"{a} :Event Scheduled")
        leap+=1
    else:
        print(f"{a} :No Event")
        notLeap+=1
    
    a+=1

print(f"total Leap Year :{leap}")
print(f"total Event Scheduled :{leap}")
