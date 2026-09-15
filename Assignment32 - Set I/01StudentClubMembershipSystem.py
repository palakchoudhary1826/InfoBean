'''
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
'''

coding_club = set()
robotics_club = set()

while True:

    print("\nStudent Club Membership System")
    print("Menu")
    print()

    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            student_id = input("Enter Student ID: ")
            coding_club.add(student_id)
            print("Student added to Coding Club.")

        case 2:
            student_id = input("Enter Student ID: ")
            robotics_club.add(student_id)
            print("Student added to Robotics Club.")

        case 3:
            if coding_club:
                print("Coding Club Students:", coding_club)
            else:
                print("No students in Coding Club.")

        case 4:
            if robotics_club:
                print("Robotics Club Students:", robotics_club)
            else:
                print("No students in Robotics Club.")

        case 5:
            if coding_club and robotics_club:
                both = coding_club.intersection(robotics_club)
                print("Students in Both Clubs:", both)
            else:
                print("Enter students in both clubs first.")

        case 6:
            if coding_club:
                only_coding = coding_club.difference(robotics_club)
                print("Students Only in Coding Club:", only_coding)
            else:
                print("No students in Coding Club.")

        case 7:
            if robotics_club:
                only_robotics = robotics_club.difference(coding_club)
                print("Students Only in Robotics Club:", only_robotics)
            else:
                print("No students in Robotics Club.")

        case 8:
            if coding_club or robotics_club:
                all_members = coding_club.union(robotics_club)
                print("All Unique Club Members:", all_members)
            else:
                print("Enter the Student First.")

        case 9:
            if coding_club or robotics_club:
                total_members = len(coding_club.union(robotics_club))
                print("Total Unique Club Members:", total_members)
            else:
                print("Enter the Student First.")

        case 10:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please try again.")