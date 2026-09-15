'''
Problem 10: Move Zeroes

Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.

Example 1:
Input:
nums = [0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]

Example 2:
Input:
nums = [0]

Output:
[0]

Example 3:
Input:
nums = [1, 2, 3]

Output:
[1, 2, 3]
'''

l=list(map(int,input("Enter :").split()))
#-->bubble sort
# for i in range(len(l)):
    
#     for j in range(len(l)-1):

#         if l[j]==0 and l[j+1]!=0:
#             #swap
#             temp=l[j]
#             l[j]=l[j+1]
#             l[j+1]=temp
           
# zero=[]
# nonzero=[]
# for i in l:
#     if i==0:
#         zero.append(i)
#     else:
#         nonzero.append(i)

# nonzero=nonzero+zero
# print(nonzero)


#approach --> two pointer
j=0

for i in range(len(l)):
    if l[i]!=0:
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
        j+=1

print(l)




