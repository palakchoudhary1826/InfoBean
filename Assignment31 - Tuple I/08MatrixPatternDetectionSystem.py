"""
8.

MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit

Requirements

Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row

Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column

Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9

Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4
"""

n=int(input("Enter The Size Of Matrix : "))

matrix=[]

print("Enter Matrix Elements : ")

for i in range(n):
    row=[]

    for j in range(n):
        row.append(int(input(f"Enter Element [{i}][{j}] : ")))

    matrix.append(row)


while True:

    print("Menu")
    print("1. Count Even Numbers Above Main Diagonal")
    print("2. Count Odd Numbers Below Main Diagonal")
    print("3. Display Boundary Elements")
    print("4. Exit")

    choice=int(input("Enter Your Choice : "))


    if choice==1:

       pass


    elif choice==2:

        pass


    elif choice==3:

        print("\nBoundary Elements:")

        for j in range(n):
            print(matrix[0][j],end=" ")

        for i in range(1,n):
            print(matrix[i][n-1],end=" ")

        for j in range(n-2,-1,-1):
            print(matrix[n-1][j],end=" ")

        for i in range(n-2,0,-1):
            print(matrix[i][0],end=" ")

        print()


    elif choice==4:

        print("Program Exited ...")
        break


    else:

        print("Invalid Choice ...")