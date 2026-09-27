import models.employe
emp=[]
for i in range(1,6):
    id=int(input("enter the employee id:"))
    name=input("enter the employee name:")
    salary=int(input("enter the employee salary:"))
    dep=input("enter the employee department:")
    e=models.employe.Employe(id,name,salary,dep)
    emp.append(e)

for i in emp:
    i.display()

print("----grater salary------")
for i in emp:
    if i.salary > 40000:
        i.display()

print("----Only IT department employee-----")
for i in emp:
    if i.department=="IT":
        i.display()

print("------Highest salary------")
highest=emp[0]
for i in emp:
    if i.salary > highest.salary:
        highest=i
highest.display()

print("--------calculate total salary-------")
total=0
for i in emp:
    total+=i.salary
print(total)

print("------Average salary-------")
total=0
for i in emp:
    total+=i.salary
print(total/len(emp))

       