# 5. Student Grade Classification System (Python List Assignment)
#
# Scenario
#
# A school stores student marks in a list. The system must analyze
# the marks and generate a clear performance report by grouping
# students into grade categories.
#
# Requirements
#
# 1. Iterate through the list of marks.
# 2. Assign grades based on marks:
#    - Marks >= 90       → A Grade
#    - Marks >= 75 < 90  → B Grade
#    - Marks >= 50 < 75  → C Grade
#    - Marks < 50        → Fail
# 3. Store each category in separate lists.
# 4. Count students in each category.
# 5. Display the final structured report.
#
# Output Format (Mandatory)
#
# ===== STUDENT GRADE REPORT =====
#
# A Grade Students   : [list]
# B Grade Students   : [list]
# C Grade Students   : [list]
# Fail Students      : [list]
#
# --------------------------------
# A Count   : X
# B Count   : X
# C Count   : X
# Fail Count: X
# --------------------------------
#
# Total Students: X
#
# Test Case
#
# Input:
# [95, 82, 67, 45, 30]
#
# Expected Output:
#
# ===== STUDENT GRADE REPORT =====
#
# A Grade Students   : [95]
# B Grade Students   : [82]
# C Grade Students   : [67]
# Fail Students      : [45, 30]
#
# --------------------------------
# A Count   : 1
# B Count   : 1
# C Count   : 1
# Fail Count: 2
# --------------------------------
#
# Total Students: 5


n=int(input("Enter The Number Of Student : "))

marks=[]

for i  in range(1,n+1):
    a=float(input(f"The Marks Of student {i} :"))
    marks.append(a)
print("Marks List : ",marks)

a=[]
b=[]
c=[]
fail=[]

for i  in marks:

    if i>=90:
        a.append(i)
    elif 75<=i<90:
        b.append(i)
    elif 50<=i<75:
        c.append(i)
    
    if i<50:
        fail.append(i)


print(" ")

print("===== STUDENT GRADE REPORT =====\n")

print("A Grade Students   :", a)
print("B Grade Students   :", b)
print("C Grade Students   :", c)
print("Fail Students      :", fail)

print("\n--------------------------------")
print("A Count   :", len(a))
print("B Count   :", len(b))
print("C Count   :", len(c))
print("Fail Count:", len(fail))
print("--------------------------------")

print("\nTotal Students:", len(a)+len(b)+len(c)+len(fail))