'''
Problem 9: Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their
intersection.

Each element in the result must appear as many times as it shows in
both arrays.

The result can be returned in any order.

Example 1:
Input:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

Output:
[2, 2]

Example 2:
Input:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

Output:
[4, 9]

Explanation:
[9, 4] is also accepted.

Note:
The order of the output does not matter.
'''

num1=list(map(int,input("Enter : ").split()))
num2=list(map(int,input("Enter : ").split()))



# ans=[]
# visit=[False]*len(num2)
# # print(visit)
# for i in num1:
#     for j in range(len(num2)):
#         if i==num2[j] and visit[j]==False:
#             ans.append(i)
#             visit[j]=True
#             break
    
# print(ans)

map={}
for i in num2:
    map[i]=map.get(i,0)+1

print(map)
ans=[]

for i in num1:
    if i in map and map[i]>0:
        ans.append(i)
        map[i]-=1

print(ans)

