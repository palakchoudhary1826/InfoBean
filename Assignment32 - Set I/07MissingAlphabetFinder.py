'''
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.
'''
sentence = ""

alphabets = set("abcdefghijklmnopqrstuvwxyz")

while True:

    print()
    print("          MISSING ALPHABET FINDER")
    print()
    print("Menu")
    print()
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")
    print()

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            sentence = input("Enter Sentence: ").lower()
            print("Sentence Stored Successfully.")

        case 2:
            if not sentence:
                print("Please enter a sentence first.")
            else:
                present = set(sentence)
                missing = alphabets - present
                print("Missing Alphabets:", missing)

        case 3:
            if not sentence:
                print("Please enter a sentence first.")
            else:
                present = set(sentence)
                missing = alphabets - present
                print("Count of Missing Alphabets:", len(missing))

        case 4:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please try again.")