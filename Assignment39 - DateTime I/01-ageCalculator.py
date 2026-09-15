'''
Assignment 1 — Age Calculator

Create a Python program that accepts the user's date of birth and calculates:

1. Current age in years
2. Completed months
3. Total number of days lived
4. Next birthday date
5. Number of days remaining for the next birthday

Input:
Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:
Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
'''

from datetime import datetime, date

dob = input("Enter DOB : {DD-MM-YYYY}: ")

dob = datetime.strptime(dob, "%d-%m-%Y").date()

print(f"Date Of Birth : {dob.day}-{dob.month}-{dob.year}")

# Age
today = date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print(f"Age : {age}")

#complete month

month=age*12+(today.month-dob.month)

if(today.day)<(dob.day):
    month-=1
print(f"Total Months used : {month}")

#total number of days:

day=today-dob
print(f"Total days lived : {day.days}")

#next dob

newDob=date(today.year+1,dob.month,dob.day)
print("Next Date Of Birth : ",newDob.day,'-',newDob.month,'-',newDob.year)

#day remains to next birth

remain=newDob-today
print("Day remains : ",remain.days)







