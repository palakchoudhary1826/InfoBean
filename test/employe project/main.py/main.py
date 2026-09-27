import models.employe
import models.project
emp=[]
for i in range(1,6):
    emp_id=int(input("enter the employe id:"))
    emp_name=input("enter the employee name:")
    department=input("enter tthe department:")
    salary=int(input("enter the salary:"))
    e=models.employe.emp(emp_name,emp_id,department,salary)
    emp.append(e)

pro=[]
for i in range(1,6):
    pro_id=int(input("enter the project id:"))
    pro_name=input("enter the project name:")
    emp_id=int(input("enter tthe employe id:"))
    project_cost=int(input("enter the projet cost:"))
    e=models.employe.pro(pro_id,pro_name,emp_id,project_cost)
    emp.append(pro)

while True:
    print("1. Display All Employees")
    print("2.  Search Employee by ID")
    print("3.Display Employees by Department")
    print("4.Find Highest Paid Employe")
    print("5.Display Employee Projects")
    print("6.Find Highest Cost Project")
    print("7.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        emp_id=int(input("enter the employe id:"))
        emp_name=input("enter the employee name:")
        department=int(input("enter the department:"))
        salary=int(input("enter the salary:"))
        models.employe.emp.append(models.employe.employe(emp_name,emp_id,department,salary))
    elif choice==2:
        for i in models.employe.emp:
            print(i.display_info())
    elif choice==3:
        department=int(input("enter the department:"))
        for i in models.employe.emp:
            if i.department==department:
                print(i.display_info())
    elif choice==4:
        highest=models.employe.emp[0]
        for i in models.employe.emp:
            if i.salary>highest.salary:
                highest=i
        print("Highest Paid Employee:")
        print(highest.display_info())
    elif choice==5:
        emp_id=int(input("enter the employe id:"))
        for i in models.employe.pro:
            if i.emp_id==emp_id:
                print(i.display_info())
    elif choice==6: 
         highest=models.employe.pro[0]
         for i in models.employe.pro:
                if i.project_cost>highest.project_cost:
                 highest=i
         print("Highest Cost Project:")
         print(highest.display_info())
    elif choice==7:
        break

for i in emp:
    i.display()


search_id=int(input("enter the id:"))
for i in emp:
    if i.emp_id==search_id:
        i.display.emp()

search_department=int(input("enter the department:"))
for i in emp:
    if i.department==search_department:
        i.display.emp()
    else:
        print("no employe found in this department")

highest=emp[0]
for i in emp:
    if i.salary>highest.salary:
        highest=i

print("-----highest paid-----")
highest.display()
for i in emp:
    if i.salary>highest.salary:
        highest=i

print("--------employe projects------")
id=int(input("enter the id:"))
for i in emp:
    if i.emp_id==id:
        i.display.emp()

print("-----highest cost project--------")
high=emp[0]
for i in emp:
    if i.project_cost>high.project_cost:
        high=i

print(high.display_info())
print("-----highest cost project--------")
projects=emp[0]
for i in emp:
    if i.project_cost>projects.project_cost:
        projects=i
display=projects.display_info()
print(display)



