"""
=========================================
2. EMPLOYEE DEPARTMENT COUNT
=========================================

A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"] # list 

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.

Sample Output:
{'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}
"""

dept=list(map(str,input("Enter The Department : ").split()))
print(dept)
d={}
for i in dept:
    d[i]=d.get(i,0)+1


print("Dictionary ", d)