"""
=========================================
6. MOBILE APP DOWNLOAD COUNTER
=========================================

Downloads received from different cities:

cities = [
    "Indore",
    "Bhopal",
    "Indore",
    "Pune",
    "Delhi",
    "Pune",
    "Indore"
]

Write a program to:

* Count downloads city-wise.
* Display the city with maximum downloads.

Sample Output:
{'Indore': 3, 'Bhopal': 1, 'Pune': 2, 'Delhi': 1}

Most Downloads : Indore
"""

cities=list(map(str,input("Enter The Cities : ").split()))

d={}

for i in cities:
    d[i]=d.get(i,0)+1

print(d)

high=0
highKey=''

for k,v in d.items():
    if v>high:
        high=v
        highKey=k

print(f"Most Downloads : {highKey}")