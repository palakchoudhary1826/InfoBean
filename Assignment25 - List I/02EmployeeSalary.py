# 2.Employee Salary Processing
# Store employee salaries in a List and calculate details.

# Requirements:

# Store salaries
# Find average salary
# Display salaries greater than average
# Remove salaries below 15000

# Test Cases:

# Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
# Input: [15000, 15000, 15000] → Average = 15000
# Input: [5000, 7000] → Remaining List = []

n=int(input("Enter The Number Of Employee : "))

salary=[]

for i  in range(1,n+1):
    a=float(input(f"The Salary Of Employee {i} :"))
    salary.append(a)
print("Salary List : ",salary)



new=[]
sum=0

for i in salary:
    sum+=i

    if i>15000:
        new.append(i)
print(f"List of Salary above 15000: {new}")

avg=sum//len(salary)
print(f"Average : {avg}")

aboveAvg=[]

for i in salary:
    if i>avg:
        aboveAvg.append(i)

print(f"Above Average list : {aboveAvg}")




