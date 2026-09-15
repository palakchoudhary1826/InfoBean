"""
5. Employee Data Processing System

A company stores information about its employees in two forms:
1. A list of employee ages.
2. A string containing employee names separated by spaces.

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List):

1. find_second_highest_age(age_list)
   Accept a list of employee ages.
   Return the second highest age.

2. count_senior_employees(age_list)
   Accept a list of employee ages.
   Consider employees aged 50 years or above as senior employees.
   Return the count of senior employees.

3. remove_duplicate_ages(age_list)
   Accept a list of employee ages.
   Return a new list after removing duplicate ages while maintaining the original order.

Functions on Employee Names (String):

4. count_names_starting_with_vowel(names)
   Accept a string containing employee names separated by spaces.
   Return the number of names that start with a vowel (A, E, I, O, U).

5. longest_name(names)
   Accept a string containing employee names separated by spaces.
   Return the employee name having the maximum number of characters.

Menu:

========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
Enter your choice:

Sample Input:

Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha

Sample Output:

Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita

Instructions:
1. Implement all operations using separate functions.
2. Each function must accept parameters and return the result.
3. Do not print results inside the functions.
4. The menu should continue to appear until the user selects Exit.
5. Display an appropriate message for an invalid choice.
6. Use meaningful function and variable names.
7. Follow proper indentation.
"""


def display():
    print()
    print("""
===EMPLOYEE DATA PROCESSING SYSTEM ===
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
=====================================
""")
    print()


def secondHighestAge(age):
    fMax = 0
    sMax = 0

    for i in age:
        if i > fMax:
            sMax = fMax
            fMax = i
        if i < fMax and i > sMax:
            sMax = i

    return sMax


def countSenior(i):
    if i >= 50:
        return i


def startWithVowel(name):
    count = 0
    for i in range(len(name)):

        if i == 0 or name[i - 1] == " ":
            if name[i] in "aeiou" or name[i] in "AEIOU":
                count += 1

    return count


def longEmp(name):
    long = ""
    word = ""

    for i in name:
        if i != " ":
            word += i
        else:
            if len(word) > len(long):
                long = word
            word = ""

    if len(word) > len(long):
        long = word

    return long


age = list(map(int, input("Enter Age : ").split()))
name = input("Enter The Name  : ")
while True:
    display()
    choice = int(input("Enter Your Choice :"))

    match choice:
        case 1:
            print("Second Highest Employee Age")
            print(secondHighestAge(age))
        case 2:
            print("Count Senior Employees")
            result = list(filter(countSenior, age))

            print(result)
            print(f"count of senior : {len(result)}")
        case 3:
            ageSet = set(age)
            print("remove Duplicate Ages")
            print(ageSet)
        case 4:
            print(f"Name Start With Vowel Count {startWithVowel(name)}")
        case 5:
            print(f"Longest Employee Name : {longEmp(name)}")
        case 6:
            print("Thanks For Using ")
            print("Existing ...")
            break
        case _:
            print("Invalid Choice")
