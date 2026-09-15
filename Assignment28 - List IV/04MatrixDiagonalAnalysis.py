# 4.

# =========================================================
#         MATRIX DIAGONAL ANALYSIS SYSTEM
# =========================================================

# Scenario

# A security company stores surveillance data in matrix form.
# The analyst wants a menu-driven application to examine the
# diagonal elements of the matrix and generate reports.

# The application should allow the user to:

# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Display Main Diagonal Elements
#    2. Display Secondary Diagonal Elements
#    3. Compare Main and Secondary Diagonal Sums
#    4. Exit

# 2. Read the size of a square matrix from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Display Main Diagonal Elements
#    -----------------------------------------
#    Display all elements present in the main diagonal.

# 5. Choice 2 - Display Secondary Diagonal Elements
#    ----------------------------------------------
#    Display all elements present in the secondary diagonal.

# 6. Choice 3 - Compare Main and Secondary Diagonal Sums
#    ---------------------------------------------------
#    Calculate the sum of both diagonals and display:

#    - Main Diagonal Sum
#    - Secondary Diagonal Sum
#    - Which diagonal has the greater sum
#    - Or whether both sums are equal

# 7. Choice 4 - Exit
#    -----------------------------------------
#    Display:
#    "Thank You for Using Matrix Diagonal Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Enter size of matrix: 3

# Enter matrix elements:

# 1 2 3
# 4 5 6
# 7 8 9

# Menu
# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# Enter your choice: 1

# Output:
# Main Diagonal Elements:
# 1 5 9

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Secondary Diagonal Elements:
# 3 5 7

# ---------------------------------------------------------

# Enter your choice: 3

# Output:
# Main Diagonal Sum = 15
# Secondary Diagonal Sum = 15
# Both Diagonal Sums are Equal

# =========================================================



r1,c1=map(int,input("Enter The Row 1 And Column 1 : ").split(" "))


print("Fill The 1st Matrix")
arr1=[]

for i in range(r1):
    row=list(map(int,input(f"Enter The Element in {i+1}th Row : ").split(" ")))
    arr1.append(row)

print("First Matrix",arr1)  

while True:
    print("1. Display Main Diagonal Elements")
    print("2. Display Secondary Diagonal Elements")
    print("3. Compare Main and Secondary Diagonal Sums")
    print("4. Exit")

    choice = input("Enter your choice: ")



    match choice:

        case "1":

            
            

            for i in range(len(arr1)):
                print(arr1[i][i])
               
                

        case "2":
            

            for i in range(len(arr1)):
                print(arr1[i][len(arr1)-i-1])
                
                
                    

        case "3":
            
            sum1=0
            sum2=0
            for i in range(len(arr1)):
                sum1+=arr1[i][i]
                sum2+=arr1[i][len(arr1)-1-i]
            
            print(f"Main Diagonal Sum = ",sum1)
            print(f"Secondary Diagonal Sum = ",sum2)

            if sum1>sum2:
                print("main diagonal sum is greater")
            elif sum2>sum1:
                print("Secondary Diagonal Sum is Greater")
            else:
                print("both Diagonal Sums are equal")
            
                
                    
                
            


        case "4":
            print("Thank You for Using Matrix Operations Management System")
            break

        case _:
            print("Invalid Choice")