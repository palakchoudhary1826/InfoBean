def display():

    print("""
=========================================
       STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit

""")


def add(id):

    if id not in d:
        name = input("Enter The Student Name : ")
        mobile = int(input("Enter The Student Mobile : "))
        fees = int(input("Enter The Student Fees : "))
        course = input("Enter The Course : ")
        city = input("Enter The City : ")

        d[id] = {
            "name": name,
            "mobile": mobile,
            "fees": fees,
            "course": course,
            "city": city
        }

        print(f"Student Added Successfully At ID : {id}")

    else:
        print("Student ID Already Exists")
        print(d[id])


def search(id):

    if id in d:
        print()
        print("Student ID :", id)
        print("Name       :", d[id]["name"])
        print("Mobile     :", d[id]["mobile"])
        print("Fees       :", d[id]["fees"])
        print("Course     :", d[id]["course"])
        print("City       :", d[id]["city"])

    else:
        print("Student Not Found")


def update(id):

    if id in d:
        newCourse = input("Enter The New Course : ")

        d[id]["course"] = newCourse

        print("Course Updated Successfully")

    else:
        print("Student Not Found")


def delete(id):

    if id in d:
        d.pop(id)

        print("Student Deleted Successfully")

    else:
        print("Student Not Found")


def displaystudent():

    for i in d:
        print()
        print("-" * 30)
        print("Student ID :", i)
        print("Name       :", d[i]["name"])
        print("Course     :", d[i]["course"])
        print("Mobile     :", d[i]["mobile"])
        print("Fees       :", d[i]["fees"])
        print("City       :", d[i]["city"])
        print("-" * 30)


def findCourseInStudent(course):

    found = False

    for i in d:
        if d[i]["course"] == course:
            print(f"{i}  {d[i]['name']}")
            found = True

    if not found:
        print(f"No Student Is Found With {course}")


def findCityInStudent(city):

    found = False

    for i in d:
        if d[i]["city"] == city:
            print(f"{i}  {d[i]['name']}")
            found = True

    if not found:
        print(f"No Student Is Found From {city}")


def highestFees():

    high = 0
    id = 0

    for i in d:
        fees = d[i]["fees"]

        if fees > high:
            high = fees
            id = i

    print("Highest Fee Paying Student")
    print(f"Student ID : {id}")
    print(f"Student Name : {d[id]['name']}")
    print(f"Course : {d[id]['course']}")
    print(f"Fees : {d[id]['fees']}")


def lowestFees():

    low = d[0]["fees"]
    id = 0

    for i in d:
        fees = d[i]["fees"]

        if fees < low:
            low = fees
            id = i

    print("Lowest Fee Paying Student")
    print(f"Student ID : {id}")
    print(f"Student Name : {d[id]['name']}")
    print(f"Course : {d[id]['course']}")
    print(f"Fees : {d[id]['fees']}")


d = {}
id = 100


while True:

    display()

    choice = int(input("Enter The Option : "))

    match choice:

        case 1:
            print("ADD NEW STUDENT")

            id += 1
            add(id)

        case 2:
            print("Search Student")

            userId = int(input("Enter The ID : "))
            search(userId)

        case 3:
            print("Update Student Course")

            userId = int(input("Enter The ID : "))
            update(userId)

        case 4:
            print("Delete Student Record")

            userId = int(input("Enter The ID : "))
            delete(userId)

        case 5:
            print("Display All Students")

            displaystudent()

        case 6:
            print("Count Total Students")

            print(f"Total Students : {len(d)}")

        case 7:
            print("Display Students By Course")

            userCourse = input("Enter The Course : ")
            findCourseInStudent(userCourse)

        case 8:
            print("Display Students By City")

            userCity = input("Enter The City : ")
            findCityInStudent(userCity)

        case 9:
            print("Find Student Paying Highest Fees")

            highestFees()

        case 10:
            print("Find Student Paying Lowest Fees")

            lowestFees()

        case 11:
            print("Thank You For Using Student Management System")
            break

        case _:
            print("Invalid Choice")