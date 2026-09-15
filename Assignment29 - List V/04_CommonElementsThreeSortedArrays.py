# 4.
# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
# Example 1:
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.


n1 = int(input("Enter The Size Of A : "))
A = list(map(int, input("Enter The Elements Of A : ").split()))

n2 = int(input("Enter The Size Of B : "))
B = list(map(int, input("Enter The Elements Of B : ").split()))

n3 = int(input("Enter The Size Of C : "))
C = list(map(int, input("Enter The Elements Of C : ").split()))

i=0
j=0
k=0

while i<n1 and j<n2 and k <n3:
    if A[i]==B[j]==C[k]:
        print(A[i],end=" ")
        value=A[i]

        while i<n1 and A[i]==value:
            i+=1
        while j<n2 and B[j]==value:
            j+=1
        
        while k<n3 and C[k]==value:
            k+=1

    elif A[i]<B[j]:
        i+=1
    elif B[j]<C[k]:
        j+=1
    else:
        k+=1


