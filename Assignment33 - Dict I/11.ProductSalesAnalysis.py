"""
=========================================
11. PRODUCT SALES ANALYSIS
=========================================

sales = [
    "Mobile",
    "Laptop",
    "Mobile",
    "Tablet",
    "Laptop",
    "Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
"""

sales = [
    "Mobile",
    "Laptop",
    "Mobile",
    "Tablet",
    "Laptop",
    "Mobile"
]

d={}

for i in sales:
    d[i]=d.get(i,0)+1

d1=dict(sorted(d.items()))                       # by key
d2=dict(sorted(d.items(), key=lambda x: x[1]) )  # by value
sorted(d.items(), key=lambda x: x[1], reverse=True)  # value descending

print(d1)
print(d2)

