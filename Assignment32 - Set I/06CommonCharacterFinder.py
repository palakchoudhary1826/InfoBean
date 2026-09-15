'''
=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}
'''
first_string = ""
second_string = ""

while True:

    print()
    print("         COMMON CHARACTER FINDER")
    print("Menu")
    print()

    print("1. Enter First String")
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            first_string = input("Enter First String: ")
            print("First String Stored Successfully.")

        case 2:
            second_string = input("Enter Second String: ")
            print("Second String Stored Successfully.")

        case 3:
            if not first_string or not second_string:
                print("Please enter both strings first.")
            else:
                common = set(first_string) & set(second_string)
                print("Common Characters:", common)

        case 4:
            if not first_string or not second_string:
                print("Please enter both strings first.")
            else:
                common = set(first_string) & set(second_string)
                print("Count of Common Characters:", len(common))

        case 5:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please try again.")