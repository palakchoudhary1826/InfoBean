# ============================================================
# 1. First Non-Repeating Number
# ============================================================
#
# Scenario:
# An online voting system stores Vote IDs in a list.
# Find the first Vote ID that appears only once.
#
# Requirements:
# - Read N and list elements from the user.
# - Find the first non-repeating number.
# - If no such number exists, display an appropriate message.
#
# Test Case 1:
# Input:
# [4, 5, 1, 2, 1, 2, 4]
#
# Output:
# First Non-Repeating Number = 5
#
# Test Case 2:
# Input:
# [7, 7, 8, 8]
#
# Output:
# No Non-Repeating Number Found
# ============================================================


arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)


for i in arr:
    count=0
    

    for j in arr:
        if i==j:
            count+=1
            
    
    if count==1:
        print(i)
        break
else:
    print("no non-repeating number found")
    
        
