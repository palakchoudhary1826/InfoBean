'''

13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''
s=int(input("Enter The Salary : "))
r=int(input("Enter The Rating : "))
h=0

if r==5:
    if s<20000:
        h=s+(s*25)/100+2000
    else:
        h=s+(s*25)/100
elif r==4:
    if s<20000:
        h=s+(s*20)/100+2000
    else:
        h=s+(s*20)/100
elif r==3:
    h=s+(s*10)/100
elif r==2:
    h=s+(s*20)/100
else:
    print("no hike")
 
 
print(f"Revised Salary: {h}")
    