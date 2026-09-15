# 1. Count Pairs with Difference K

# A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

# Problem Statement:

# Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

# Example:

# Input:

# N = 5
# K = 2
# ages[] = {1, 5, 3, 4, 2}

# Output:

# 3

# Explanation:

# (1,3), (3,5), (2,4)


arr=list(map(int,input("Enter The Age Of Employee : ").split(" ")))
print(arr)
k=int(input("Enter The Difference : "))

count=0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        diff=abs(arr[i]-arr[j])

        if diff==k:
            count+=1
        
            print(f"{arr[i],arr[j]}")

print(count)
