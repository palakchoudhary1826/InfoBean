'''
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
'''

python_course = set()
java_course = set()

while True:

    print("\n=========================================")
    print("       ONLINE COURSE ENROLLMENT SYSTEM")
    print("=========================================")

    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            email = input("Enter Email for Python: ")
            python_course.add(email)
            print("Student Added to Python Course.")

        case 2:
            email = input("Enter Email for Java: ")
            java_course.add(email)
            print("Student Added to Java Course.")

        case 3:
            if not python_course:
                print("No Students in Python Course.")
            else:
                print("Students in Python Course:", python_course)

        case 4:
            if not java_course:
                print("No Students in Java Course.")
            else:
                print("Students in Java Course:", java_course)

        case 5:
            if not python_course or not java_course:
                print("No Students Enrolled in Both Courses.")
            else:
                both = python_course & java_course
                print("Students Enrolled in Both Courses:", both)

        case 6:
            if not python_course:
                print("No Students in Python Course.")
            else:
                only_python = python_course - java_course
                print("Students Only in Python:", only_python)

        case 7:
            if not java_course:
                print("No Students in Java Course.")
            else:
                only_java = java_course - python_course
                print("Students Only in Java:", only_java)

        case 8:
            email = input("Enter Email to Check: ")

            if email in python_course:
                print("Student is Enrolled in Python Course.")
            else:
                print("Student is NOT Enrolled in Python Course.")

        case 9:
            total = len(python_course | java_course)
            print("Total Unique Students:", total)

        case 10:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please try again.")