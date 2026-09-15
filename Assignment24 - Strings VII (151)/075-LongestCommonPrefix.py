"""
Find the Longest Common Prefix Among Strings

Write a Python program to input multiple strings and find
the longest prefix common to all strings.

Input:
Enter number of strings: 3

Enter string 1: flower
Enter string 2: flow
Enter string 3: flight

Output:
Longest Common Prefix: fl
"""

n = int(input("Enter The number of Strings : "))

l = []

for i in range(n):
    s = input(f"Enter String {i+1} : ")
    l.append(s)


print(l)

prefix=l[0] 
print(prefix)


for i in range(1,len(l)):
    temp="" #reset in each iteration

    for j in range(min(len(prefix),len(l[i]))):

        if prefix[j]==l[i][j]:
            temp+=prefix[j]
        

    if len(temp)<len(prefix):
        prefix=temp

print(prefix)

    





# # prefix=l[0] #flower

# # for i in range(1,len(l)):
# #     # print(l[i])
# #     temp=""

# #     for j in range(min(len(prefix),len(l[i]))): 
        
        
# #             if prefix[j]==l[i][j]:
# #                 temp+=prefix[j] 
# #             else:
# #                 break
    
# #     prefix=temp

# # print(f"Longest Common Prefix  : {prefix}")


# for i in range(len(l[0])):

        


