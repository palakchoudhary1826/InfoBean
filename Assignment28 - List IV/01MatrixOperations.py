# 1.
# =========================================================
#         MATRIX OPERATIONS MANAGEMENT SYSTEM
# =========================================================


# A data analysis company stores numerical information in matrix form.
# To help employees perform matrix-related operations efficiently,
# the company wants a menu-driven application.

# The application should allow the user to:

# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# The user must enter the number of rows, columns, and all matrix
# elements. The program should perform the selected operation and
# display the result.

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user chooses Exit.

#    1. Add Two Matrices
#    2. Subtract Two Matrices
#    3. Compare Two Matrices
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all elements of Matrix A and Matrix B from the user whenever
#    required.

# 4. Based on the user's choice:

#    Choice 1 - Add Two Matrices
#    --------------------------------
#    Add corresponding elements of both matrices and display
#    the resultant matrix.

# 5. Choice 2 - Subtract Two Matrices
#    --------------------------------
#    Subtract corresponding elements of Matrix B from Matrix A
#    and display the resultant matrix.

# 6. Choice 3 - Compare Two Matrices
#    --------------------------------
#    Check whether both matrices are equal.

#    Two matrices are considered equal if:
#    - They have the same dimensions.
#    - Corresponding elements are equal.

#    Display:
#    "Matrices are Equal"
#    or
#    "Matrices are Not Equal"

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Operations Management System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 1

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 5 6
# 7 8

# Result Matrix:
# 6 8
# 10 12

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 3

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 1 2
# 3 4

# Output:
# Matrices are Equal

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Operations Management System

# =========================================================


r1,c1=map(int,input("Enter The Row 1 And Column 1 : ").split(" "))
r2,c2=map(int,input("Enter The Row 1 And Column 1: ").split(" "))

print("Fill The 1st Matrix")
arr1=[]
for i in range(r1):
    row=list(map(int,input(f"Enter The Element in {i+1}th Row : ").split(" ")))
    arr1.append(row)

print("Fill The 2st Matrix")
arr2=[]
for i in range(r2):
    row=list(map(int,input(f"Enter The Element in {i+1}th Row : ").split(" ")))
    arr2.append(row)

print("First Matrix",arr1)  
print("Second Matrix",arr2) 
while True:
    print("\n1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")

    choice = input("Enter your choice: ")



    match choice:

        case "1":

            if r1 != r2 or c1 != c2:
                print("Matrices cannot be added.")
                continue
            c=[]

            for i in range(len(arr1)):
                row=[]
                sum=0
                for j in range(len(arr1[i])):
                    sum=arr1[i][j]+arr2[i][j]
                    row.append(sum)
                c.append(row)
            
            print("Result Matrix:")
            for row in c:
                print(*row)

                
                    


        case "2":


            if r1 != r2 or c1 != c2:
                print("Matrices cannot be subtracted.")
                continue
            c=[]

            for i in range(len(arr1)):
                row=[]
                sum=0
                for j in range(len(arr1[i])):
                    sum=arr1[i][j]-arr2[i][j]
                    row.append(sum)
                c.append(row)
            
            print("Result Matrix:")
            for row in c:
                print(*row)

        case "3":
            
            if r1 != r2 or c1 != c2:
                print("Matrices are Not Equal")
                continue
            equal=True
            for i in range(len(arr1)):
                for j in range(len(arr1[i])):
                    if arr1[i][j]!=arr2[i][j]:
                        equal=False
                        break
                
            if equal:
                print("Matrices Are Equal")
            else:
                print("Matrices Are Not Equal")    


        case "4":
            print("Thank You for Using Matrix Operations Management System")
            break

        case _:
            print("Invalid Choice")