'''
Find the Longest Common Suffix Among Strings

Write a Python program to input multiple strings and find
the longest suffix common to all strings.

Input:
Enter number of strings: 3

Enter string 1: running
Enter string 2: swimming
Enter string 3: jumping

Output:
Longest Common Suffix: ing
'''

n = int(input("Enter The number of Strings : "))

l = []

for i in range(n):
    s = input(f"Enter String {i+1} : ")
    l.append(s)

prefix=l[0] 

for i in range(1,len(l)):
    # print(l[i])
    temp=""

    for j in range(1,min(len(prefix),len(l[i]))+1): 
        
        
            if prefix[-j]==l[i][-j]:
                temp=prefix[-j]+temp 
            else:
                break
    
    prefix=temp

print(f"Longest Common Suffix  : {prefix}")