# 3. Prime Number Analyzer using List (Python)
#
# Scenario
#
# A coaching institute stores student lucky numbers in a Python List.
# Your task is to analyze the list and identify prime numbers for a scholarship selection process.
#
# You must iterate through every element of the list and perform prime number analysis.
#
# Requirements
#
# 1. Store integer values in a List
# 2. Iterate through all elements of the List
# 3. Check whether each number is prime or not
# 4. Display all prime numbers
# 5. Count total prime numbers
# 6. Count total non-prime numbers
# 7. Find the largest prime number from the List
# 8. Store all prime numbers into another List
# 9. Sort the prime numbers in ascending order and display them
#
# Test Case 1
#
# Input:
# [2, 3, 4, 5, 6, 7, 8]
#
# Expected Output:
# Prime Numbers: 2 3 5 7
# Prime Count: 4
# Non-Prime Count: 3
# Largest Prime Number: 7
# Prime List: [2, 3, 5, 7]
# Sorted Prime List: [2, 3, 5, 7]
#
# Test Case 2
#
# Input:
# [10, 11, 12, 13, 14, 15]
#
# Expected Output:
# Prime Numbers: 11 13
# Prime Count: 2
# Non-Prime Count: 4
# Largest Prime Number: 13
# Prime List: [11, 13]
# Sorted Prime List: [11, 13]
#
# Test Case 3
#
# Input:
# [1, 2, 17, 19, 20, 25]
#
# Expected Output:
# Prime Numbers: 2 17 19
# Prime Count: 3
# Non-Prime Count: 3
# Largest Prime Number: 19
# Prime List: [2, 17, 19]
# Sorted Prime List: [2, 17, 19]
#
# Test Case 4
#
# Input:
# [4, 6, 8, 9, 10]
#
# Expected Output:
# Prime Numbers: None
# Prime Count: 0
# Non-Prime Count: 5
# Largest Prime Number: Not Available
# Prime List: []
# Sorted Prime List: []
#
# Test Case 5
#
# Input:
# [29, 31, 37, 41]
#
# Expected Output:
# Prime Numbers: 29 31 37 41
# Prime Count: 4
# Non-Prime Count: 0
# Largest Prime Number: 41
# Prime List: [29, 31, 37, 41]
# Sorted Prime List: [29, 31, 37, 41]


n=int(input("Enter The Number Of Student : "))

lucky=[]

for i  in range(1,n+1):
    a=int(input(f"The Lucky Number Of student {i} :"))
    lucky.append(a)
print("Lucky List : ",lucky)

prime=[]

nonPrimeCount=0

for i in lucky:
    if i<=1:
        nonPrimeCount+=1
        continue
    else:
        j=2
        while(j<i):
            if i%j==0:
                break
            j+=1
        
        if j==i:
            prime.append(i)
        else:
            nonPrimeCount+=1

print(f"Prime Number List : {prime}")
print(f"Total Prime Number : {len(prime)} ")
print(f"Total Non-Prime Number : {nonPrimeCount}")


high=prime[0]

for i in prime:
    if i>high:
        high=i

print(f"Largest Prime Number in List : {high}")
prime.sort()
print(f"Sort Of Prime List : {prime}")