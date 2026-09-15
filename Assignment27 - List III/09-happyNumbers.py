# ============================================================
# 9. Happy Numbers
# ============================================================
#
# Scenario:
# Store numbers in a list and identify Happy Numbers.
#
# A number is called Happy if repeatedly replacing it with
# the sum of the squares of its digits eventually results in 1.
#
# Example:
#
# 19
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1
#
# Therefore, 19 is a Happy Number.
#
# Another Example:
#
# 7
# 7² = 49
# 4² + 9² = 97
# 9² + 7² = 130
# 1² + 3² + 0² = 10
# 1² + 0² = 1
#
# Therefore, 7 is a Happy Number.
#
# Non-Happy Number Example:
#
# 4
# 4² = 16
# 1² + 6² = 37
# 3² + 7² = 58
# 5² + 8² = 89
# 8² + 9² = 145
# 1² + 4² + 5² = 42
# 4² + 2² = 20
# 2² + 0² = 4
#
# Since 4 appears again, the process enters a cycle.
#
# Therefore, 4 is NOT a Happy Number.
#
# Requirements:
# - Read N and list elements from the user.
# - Find all Happy Numbers.
# - Store Happy Numbers in another list.
# - Count the number of Happy Numbers.
# - Find the largest Happy Number.
# - Display the Happy Number list.
# - If no Happy Number exists, display "Not Available"
#   for the largest Happy Number.
#
# Test Case 1:
#
# Input:
# [19, 7, 4, 20]
#
# Output:
# Happy Numbers = [19, 7]
# Count = 2
# Largest Happy Number = 19
#
# Test Case 2:
#
# Input:
# [13, 10, 4]
#
# Output:
# Happy Numbers = [13, 10]
# Count = 2
# Largest Happy Number = 13
#
# Test Case 3:
#
# Input:
# [2, 3, 4]
#
# Output:
# Happy Numbers = []
# Count = 0
# Largest Happy Number = Not Available
#
# ============================================================

arr=list(map(int,input("Enter The Elements : ").split(' ')))
n=len(arr)
print(arr)

result=[]
count=0
large=0
found=False

for i in arr:
    #& happy logic

    
    
    num=i
    sum=0
    seen=[]
        

    while sum != 1 and num not in seen:

        seen.append(num)
        sum = 0

        while num > 0:
            d = num % 10
            sum += d * d
            num //= 10

        if sum == 1:
            result.append(i)
        else:
            num = sum

print(f"List Of Happy Number : {result}")

if len(result)!=0:
    print(f"Count Of Happy Number : {len(result)}")
    for i in result:
        if i>large:
            large=i

    print(f"large number in happy list : {large}")
else:
    print(f"Happy number are not happy in this list")






        
    
