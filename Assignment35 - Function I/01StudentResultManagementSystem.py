
def display():

    print("*" * 30)
    print("Student Result Management")
    print("*" * 30)

    print("Choose the Choice From Menu")
    print()

    print("""
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
""")

def add():

    print("\nAdd Student Details")
    print("-" * 30)

    name = input("Enter Student Name : ")
    rollNo = input("Enter Roll Number : ")

    marks = []

    for i in range(5):
        mark = int(input(f"Enter Mark {i + 1} : "))
        marks.append(mark)

    StudentDB.append(name)
    StudentDB.append(rollNo)
    StudentDB.append(marks)

    print("\nStudent Details Added Successfully")


def total(studentDB):

    sum = 0

    for i in studentDB[2]:
        sum += i

    return sum


def percent():

    return (total(StudentDB) / 500) * 100


def grade():

    result = percent()

    if 90 < result <= 100:
        return "A+"

    elif 80 < result <= 90:
        return "A"

    elif 70 < result <= 80:
        return "B"

    elif 60 < result <= 70:
        return "C"

    elif 50 < result <= 60:
        return "D"

    else:
        return "FAIL"


def high(studentDB):

    max = 0

    for i in studentDB[2]:

        if i > max:
            max = i

    return max


def low(studentDB):

    min = float("inf")

    for i in studentDB[2]:

        if i < min:
            min = i

    return min


def displayResult(studentDB):

    print("\n" + "*" * 30)
    print("Result Card")
    print("*" * 30)

    print()

    print(f"Name        : {studentDB[0]}")
    print(f"Roll Number : {studentDB[1]}")

    print()
    print("Marks")

    for i in range(len(studentDB[2])):
        print(f"Subject {i + 1}   : {studentDB[2][i]}")

    print()

    print(f"Total Marks  : {total(studentDB)}")
    print(f"Percentage   : {percent()}%")
    print(f"Grade        : {grade()}")
    print(f"Highest Mark : {high(studentDB)}")
    print(f"Lowest Mark  : {low(studentDB)}")


StudentDB = []

while True:

    display()

    choice = int(input("Enter The Choice : "))

    match choice:

        case 1:
            add()

        case 2:
            print(f"\nTotal Marks : {total(StudentDB)}")

        case 3:
            print(f"\nPercentage : {percent()}%")

        case 4:
            print(f"\nGrade : {grade()}")

        case 5:
            displayResult(StudentDB)

        case 6:
            print(f"\nHighest Mark : {high(StudentDB)}")

        case 7:
            print(f"\nLowest Mark : {low(StudentDB)}")

        case 8:
            print("\nExiting ....")
            break

        case _:
            print("\nInvalid Choice")
            print("Choose The Correct Option From The Menu")
