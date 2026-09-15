# 1.Student Marks Management
# Create a program to store student marks in a List and perform operations.

# Requirements:

# Add student marks into a List
# Display all marks
# Find highest and lowest marks
# Count students who scored above 75

# Test Cases:

# Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
# Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
# Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3

n=int(input("Enter The Number Of Student : "))

marks=[]

for i  in range(1,n+1):
    a=float(input(f"The Marks Of student {i} :"))
    marks.append(a)
print("Marks List : ",marks)

low=marks[0]
high=marks[0]
count=0

for i in marks:
    # count+=1
    if i > high:
        high=i
    elif i< low:
        low=i
    

    if i>75:
        count+=1

print("\n\nHighest Marks:", high)
print("Lowest Marks:", low)
print("Students Scored Above 75:", count)


