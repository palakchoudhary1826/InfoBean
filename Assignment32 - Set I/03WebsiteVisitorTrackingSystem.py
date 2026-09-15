'''
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.
'''

visitors = set()

while True:

    print()
    print("       WEBSITE VISITOR TRACKING SYSTEM")
    print("Menu")


    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    print()

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            id = input("Enter Visitor ID: ")

            if id in visitors:
                print("Visitor already exists.")
            else:
                visitors.add(id)
                print("Visitor added successfully.")
            

        case 2:
            id = input("Enter Visitor ID: ")

            if id in visitors:
                visitors.remove(id)
                print("Visitor removed successfully.")
            else:
                print("Visitor not found.")

        case 3:
            id = input("Enter Visitor ID: ")

            if id in visitors:
                print("Visitor exists.")
            else:
                print("Visitor does not exist.")

        case 4:
            if visitors:
                print("All Visitors:", visitors)
            else:
                print("No visitors found.")

        case 5:
            print("Total Unique Visitors:", len(visitors))

        case 6:
            visitors.clear()
            print("Visitor data cleared successfully.")

        case 7:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please try again.")