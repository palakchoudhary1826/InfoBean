'''
Multi-Level Employee Promotion System

A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike
'''

experience = int(input("Enter Experience (in years): "))
rating = int(input("Enter Rating: "))
projects = int(input("Enter Number of Projects Completed: "))
salary = int(input("Enter Salary: "))
p=""
if experience>=5:
    if rating >=4:
        if projects>=3:
            if salary<=50000:
                p="30%"
            else:
                p="20%"
        else:
            p="10%"
    else:
        p="no promotion"
else:
    if rating==5:
        p="fast track promotion"
    else:
        p="no promotion"

print(f"Promotion Status :{p}")