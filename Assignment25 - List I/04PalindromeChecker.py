# 4.
# Palindrome Number List Checker
# Scenario

# A system checks lucky numbers which are palindromes.

# Requirements
# Check palindrome numbers
# Store palindrome numbers in list
# Count palindrome numbers
# Find largest palindrome
# Sort palindrome list
# Test Cases

# Input:
# [121, 131, 20, 44, 55, 100]

# Output:

# Palindromes: [121, 131, 44, 55]
# Count: 4
# Largest: 131
# Sorted: [44, 55, 121, 131]

n=int(input("Enter The Range Of Number : "))

temp=[]

for i  in range(1,n+1):
    a=int(input(f"The {i} Number :"))
    temp.append(a)

palin=[]
for i in temp:
    t=i
    rev=0
    while i>0:
        d=i%10
        rev=rev*10+d
        i//=10

    i=t
    if rev==i:
        palin.append(i)
    else:
        continue

high=palin[0]
for i in palin:
    if i>high:
        high=i

palin.sort()
print(f"List Of Palindrome : {palin}")
print(f"Count Of Palindrome Number in List : {len(palin)}")
print(f"Largest Palindrome : {high}")
print(f"Sorted palindrome :{palin}")




