# MATRIX PERFORMANCE EVALUATION SYSTEM

# A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

# The HR department wants a menu-driven application to analyze employee performance.

# Menu
# 1. Find Employee with Highest Total Score
# 2. Find Month with Lowest Average Score
# 3. Display Employee-wise Maximum Score
# 4. Exit
# Requirements
# Choice 1 – Find Employee with Highest Total Score
# Calculate the sum of each row.
# Display the employee number having the highest total score.
# Choice 2 – Find Month with Lowest Average Score
# Calculate the average of each column.
# Display the month having the lowest average score.
# Choice 3 – Display Employee-wise Maximum Score
# Find and display the maximum value present in each row.
# Sample Input
# 10 20 30
# 40 50 60
# 25 35 45
# Output
# Employee 2 has Highest Total Score = 150

# Month 1 Average = 25
# Month 2 Average = 35
# Month 3 Average = 45

# Employee 1 Max Score = 30
# Employee 2 Max Score = 60
# Employee 3 Max Score = 45

r,c=map(int,input("Enter The no. of employee and no. of month : ").split(" "))
print("Fill The Array by performance")
arr=[]
for i in range(r):
    row=list(map(int,input("Enter the element : ").split(" ")))
    arr.append(row)
print(arr)

print()

while True:
    print(" ")
    print("Menu")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")

    choice=int(input("Enter The Choice : "))
    print()

    match choice:
        case 1:
            max=0
            t=0
            for i in range(r):
                sum=0
                for j in range(c):
                    n=arr[i][j]
                    sum+=n
                if sum>=max:
                    max=sum
                    t=i
                    
            
            print(f"Employee {i} has Highest Total Score = {max}")
        case 2:
            total=0
            low=0
            for i in range(r):
                total+=arr[i][0]
            low=total/r
            month=1

            print(f"Month {month} Average = {low}")


            for col in range(1,c):
                sum=0
                for row in range(r):
                    sum+=arr[row][col]
                avg=sum/r
                print(f"Month {col+1} Average = {avg}")

                if avg<low:
                    low=avg
                    month=col+1
            
            print(f"Lowest Average Of {month} month : {low}")
            
            
        case 3:
           
            for i in range(r):
                max=0
                for j in range(c):
                    if arr[i][j]>=max:
                        max=arr[i][j]
                print(f"Employee {i+1} Max Score = {max}")
        case 4:
            print("Thank You for Using ")
            break
        case _:
            print("Invalid Choice")



