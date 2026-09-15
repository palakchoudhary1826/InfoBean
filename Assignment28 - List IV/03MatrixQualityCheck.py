# 3.

# =========================================================
#          MATRIX QUALITY CHECK SYSTEM
# =========================================================

# Scenario

# A manufacturing company records quality inspection values in
# matrix form. The Quality Control team wants a menu-driven
# application to analyze the inspection data and generate reports.

# The application should allow the user to:

# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Armstrong Numbers Row-wise
#    2. Count Palindrome Numbers Column-wise
#    3. Display Average of Each Row
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Armstrong Numbers Row-wise
#    -------------------------------------------
#    Count and display the number of Armstrong numbers
#    present in each row.

#    Examples:
#    153, 370, 371, 407

# 5. Choice 2 - Count Palindrome Numbers Column-wise
#    -----------------------------------------------
#    Count and display the number of palindrome numbers
#    present in each column.

#    Examples:
#    121, 131, 444, 1221

# 6. Choice 3 - Display Average of Each Row
#    --------------------------------------
#    Calculate and display the average of each row.

# 7. Choice 4 - Exit
#    --------------------------------------
#    Display:
#    "Thank You for Using Matrix Quality Check System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 153 121 10
# 370 22 44
# 407 15 131

# Output:
# Row 1 Armstrong Count = 1
# Row 2 Armstrong Count = 1
# Row 3 Armstrong Count = 1

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Column 1 Palindrome Count = 0
# Column 2 Palindrome Count = 3
# Column 3 Palindrome Count = 2

# =========================================================



r1,c1=map(int,input("Enter The Row 1 And Column 1 : ").split(" "))


print("Fill The 1st Matrix")
arr1=[]

for i in range(r1):
    row=list(map(int,input(f"Enter The Element in {i+1}th Row : ").split(" ")))
    arr1.append(row)

print("First Matrix",arr1)  

while True:
    print("1. Count ArmStrong Row-wise")
    print("2. Count Palindrome Column-wise")
    print("3. Average Of each row")
    print("4. Exit")

    choice = input("Enter your choice: ")



    match choice:

        case "1":

            
            

            for i in range(len(arr1)):
               
                count=0
                for j in range(len(arr1[i])):
                    n=arr1[i][j]
                    t=n
                    p=len(str(n))
                    sum=0
                    while n>0:
                        d=n%10
                        sum+=d**p
                        n//=10
                    if sum==t:
                        count+=1

                print(f"Row {i+1}th ArmStrong Number Count : {count}")

        case "2":
            

            for col in range(len(arr1[0])):
                
                count=0
                for row in range(len(arr1)):
                    n=arr1[row][col]
                    t=n
                    rev=0
                    while n>0:
                        d=n%10
                        rev=rev*10+d
                        n//=10
                    if rev==t:
                        count+=1

                print(f"Col {col+1} Palindrome count : {count}")
                    

        case "3":
            
            
            for i in range(len(arr1)):
                sum=0
                for j in range(len(arr1[i])):
                    sum+=arr1[i][j]
                avg=sum/len(arr1[i])
                print(f"Average of {i+1}th row  : {avg}")
                
                    
                
            


        case "4":
            print("Thank You for Using Matrix Operations Management System")
            break

        case _:
            print("Invalid Choice")