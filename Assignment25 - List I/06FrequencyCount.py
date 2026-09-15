# 6. Frequency Count of Elements (Advanced Scenario-Based Problem)
#
# Scenario
#
# A government survey department collects responses from different
# regions. Each response is stored as an integer in a list
# (representing selected option IDs).
#
# The department wants to analyze:
# 1. How many times each option was selected.
# 2. Most popular option.
# 3. Least popular option.
# 4. Detect invalid entries (negative numbers or zeros).
#
# Requirements
#
# 1. Store survey responses in a list.
# 2. Ignore invalid entries (<= 0).
# 3. Count frequency of each valid number.
# 4. Display frequency in sorted order.
# 5. Find the most frequently selected option.
# 6. Find the least frequently selected option.
# 7. Store frequency in a dictionary.
#
# Note:
# - Do NOT use the built-in Counter class.
#
# Test Case 1
#
# Input:
# [1, 2, 2, 3, 3, 3, 4, 1, 2]
#
# Expected Output:
#
# Frequency Count:
# 1 -> 2
# 2 -> 3
# 3 -> 3
# 4 -> 1
#
# Most Frequent: 2 or 3 (Tie)
# Least Frequent: 4
#
# --------------------------------------------------
#
# Test Case 2
#
# Input:
# [1, 2, -1, 3, 0, 2, 4, -5, 3, 3]
#
# Expected Output:
#
# Invalid Entries Ignored: [-1, 0, -5]
#
# Frequency Count:
# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 1
#
# Most Frequent: 3
# Least Frequent: 1 or 4
#
# --------------------------------------------------
#
# Test Case 3
#
# Input:
# [5, 5, 5, 5, 2, 2, 1]
#
# Expected Output:
#
# Frequency Count:
# 1 -> 1
# 2 -> 2
# 5 -> 4
#
# Most Frequent: 5
# Least Frequent: 1
#
# --------------------------------------------------
#
# Test Case 4
#
# Input:
# [7, 7, 7, 7, 7]
#
# Expected Output:
#
# Frequency Count:
# 7 -> 5
#
# Most Frequent: 7
# Least Frequent: 7
#
# --------------------------------------------------
#
# Test Case 5
#
# Input:
# [-1, 0, -3]
#
# Expected Output:
#
# No valid data found



n=int(input("Enter The Survey  Range: "))

entries=[]
valid=[]
invalid=[]


for i  in range(1,n+1):

    
    a=int(input(f"The survey {i} :"))
    if a<0:
        invalid.append(a)
    else:
        valid.append(a)



    
print("Valid List : ",valid)
print("Invalid List : ",invalid)

if len(valid) == 0:
    print("No valid data found")
else:
    valid.sort()

    visit=[]
    max=[]
    least=[]
    maxCount=0
    minCount=len(valid)


    print("frequency count ")
    for i in valid:
        found=False
        for j in  visit:
            if i==j:
                found=True
                break
        if found:
            continue
        count=0

        for j in valid:
            if j==i:
                count+=1
        print(f"{i} ---> {count}")
        visit.append(i)

    if count > maxCount:
        maxCount = count
        max = [i]

    elif count == maxCount:
        max.append(i)
    
    if count<minCount:
         minCount=count
         least=[i]
    elif count==minCount:
         least.append(i)

    if len(invalid) > 0:
        print("\nInvalid Entries Ignored:", invalid)

    print("\nMost Frequent:", max)
    print("Least Frequent:", least)
         



        




    



