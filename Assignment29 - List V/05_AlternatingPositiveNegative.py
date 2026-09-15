# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers.
# Your task is to create an array of alternate positive and negative numbers
# without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# Example 1:
# Input:
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:
# Input:
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0


arr=list(map(int,input("Enter The num : ").split(" ")))
print(arr)
pos=[]
neg=[]

for i in arr:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

print(pos)
print(neg)

# arr[0]=pos[0]

i=0
j=0
k=0

while i<len(pos) and j<len(neg):
    arr[k]=pos[i]
    i+=1
    k+=1

    arr[k]=neg[j]
    j+=1
    k+=1


while i<len(pos):
    arr[k]=pos[i]
    i+=1
    k+=1

while j<len(neg):
    arr[k]=neg[i]
    j+=1
    k+=1

print(arr)
